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
            "https://drive.google.com/uc?export=view&id=1ylTyguOrAV8IYRGYk4WOxCisIKRM57q0",
            "https://drive.google.com/uc?export=view&id=1vNGfVg7_bZOw_ZgF2GYcCLHiXSBgm4zV",
            "https://drive.google.com/uc?export=view&id=18Cs8dxvqb5oQM5cWfm1EF80yRaYCvdsV",
            "https://drive.google.com/uc?export=view&id=1vNGfVg7_bZOw_ZgF2GYcCLHiXSBgm4zV",
            "https://drive.google.com/uc?export=view&id=1jTrnSfmLIuVg1148b3O2ND11QmEFyL1q",
            "https://drive.google.com/uc?export=view&id=1T1dXFHniTIJOZYstPkxN8pniux4ptWtz",
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
                "kesan": "Bang Fajar orangnya keren, sangat memberi inspirasi, dan berwibawa.",  
                "pesan":"Sukses selalu kedepannya bang, semoga saya juga bisa memberi inspirasi seperti abang"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil asik orangnya dan ternyata orang Riau juga",  
                "pesan":"Semangat terus bang, dan sukses selalu kedepanya"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi ramah dan keren orangnya",  
                "pesan":"Semangat sehat selalu ya kakak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois orangnya kalem dan humble.",  
                "pesan":"Semangat menjalani kuliahnya bang"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa selain cantik keren juga orangnya.",  
                "pesan":"Semangat terus dan sehat selalu kak Hafsa"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak Lutfi ini asik dan baik, sangat menginspirasi.",  
                "pesan":"Semangat terus menjalani kuliahnya kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Gbkq64fAKYKLbakk9O3osFt4F5y587HS",
            "https://drive.google.com/uc?export=view&id=1U9DPdlS0CwiA9ZupVv66kMH8jTbVFgRR",
            "https://drive.google.com/uc?export=view&id=1p4IAwJgJJ47KQ-B5wN76TU8H4LBp_WQL",
            "https://drive.google.com/uc?export=view&id=1w3of3spVvQcOqGVtWMfHP1QEhecEKDGf",
            "https://drive.google.com/uc?export=view&id=1pOlYdgchtC2-XKKHHbu20QAA9PGV5p6b",
            "https://drive.google.com/uc?export=view&id=1Lz-V-DGRd3qJNnCgj3O4FZFMDRWCqWTz",
            "https://drive.google.com/uc?export=view&id=1eszhahOFsLqTsPSVDW_xMe1ncE_VbLV_",
            "https://drive.google.com/uc?export=view&id=1i3xYoxY_uhoZutBiDF0dYsmLBmya5Gzr/",
            "https://drive.google.com/uc?export=view&id=1FZEN9C0PNisfbTKsWPp0E9eNm8l_NZNI",
            "https://drive.google.com/uc?export=view&id=1f2X-3LG_QI9jvdhHbunh0M_6Ay9MIXcs",
            "https://drive.google.com/uc?export=view&id=1nIYuIJCpG4TDRJ4ctQHwng_jcNTNItES",
            "https://drive.google.com/uc?export=view&id=1OW_NkuQkNoaz8r-sQ7j-TaH5A42bBgzm",
            "https://drive.google.com/uc?export=view&id=1WGaCndIdUjupKfcRTyTeDoB9uyam4RHK",

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
                "kesan": "Bang Ridho orangnya keren, namun asik juga, dan menginspirasi.",  
                "pesan":"Sukses terus dan semoga selalu menginspirasi banyak orang ya bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Juesi sangat humble, dan cantik",  
                "pesan":"Semangat terus ya kuliahnya kak Juesi"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Bang Dharu pinter, asik, dan menginspirasi banget",  
                "pesan":"Sukses selalu kedepannya bang Dharu"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Niko orangnya ramah dan asik.",  
                "pesan":"Semangat dan semoga cepat lulus ya Bang Niko"#1
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kakak ini ramah dan cartik, keren juga.",  
                "pesan":"Semangat menjalani kuliahnya yaa kak"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro keren dan menginspirasi ketika diwawancara.",  
                "pesan":"Semoga sukses kedepannya bang Givaro"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa orangnya baik, ramah, dan cantik.",  
                "pesan":"Semangat menjalani kuliahnya kak Nisa"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kak Hani keren, ramah orangnya, cantik.",  
                "pesan":"Semangat dan jangan lupa jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremi keren orangnya, sangat menginspirasi saya",  
                "pesan":"Semoga sukses terus kedepannya abang nim!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica humble dan cantik orangnya",  
                "pesan":"Semangat menjalani kuliahnya kak Monica"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jona asik serta humble orangnya",  
                "pesan":"Sukses dan semangat terus ya bang"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Sekar ramah dan keren orangnya",  
                "pesan":"Semangat menjalani kuliahnya ya kak"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini ramah, cantik, dan keren",  
                "pesan":"Semangat dan semoga cepat lulus yaa kak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13cNIJiXiuYZ14bvCh-NNwm0Qy1XKwjWL",
            "https://drive.google.com/uc?export=view&id=1e6NqFA_yS73l8wT9IznFI1AWMRTDJ-u8",
            "https://drive.google.com/uc?export=view&id=1_6leaHNQE0WGUQw3sgd34bHCXOEyG2kT",
            "https://drive.google.com/uc?export=view&id=1vXiWaZTYIUi112QwNg00BFT_JarNLoxW",
            "https://drive.google.com/uc?export=view&id=14IhxjJrOuxRlKQz-1Xrai-RyyUjw7gIu",
            "https://drive.google.com/uc?export=view&id=1cW3owhmzczYMNpBD9bdFS4LyEGnm80ep",
            "https://drive.google.com/uc?export=view&id=1guCj0J7O6nTf8Q5HvAOmoObkWa3jfwX_",
            "https://drive.google.com/uc?export=view&id=1D--PDELYJO1z5Ky7Fp88rL4u7Xi_gju3",
            "https://drive.google.com/uc?export=view&id=16gPBkCl7NNlaEl4trawyDBYyYYccRGOy",
            "https://drive.google.com/uc?export=view&id=18FF1Oq7dOhsXJ1hFL85mHqrFp1bSWi0U",
            "https://drive.google.com/uc?export=view&id=1BTQMoocNsC_h0UwFr0c3CkmCypNC-hYa",
            "https://drive.google.com/uc?export=view&id=19gkgutV3OKfcBPVkobFD38JDpF3CFiuc",
            "https://drive.google.com/uc?export=view&id=1mI_S0DL3ggqRrVqn4RZk_slHat9gszvf",
            "https://drive.google.com/uc?export=view&id=13AFbH5ZvP48DpphPtpuMnJDkt3VDVRgZ",
            "https://drive.google.com/uc?export=view&id=19FwMZ8lq9wMi6ZpOlddZagDQjVHGl9rD",
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
                "kesan": "Bang kevin orangnya santai kalo ngobrol, humble juga.",  
                "pesan":"Semangat dan sukses selalu kedepannya bang kevin"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini baik dan humble, dan cantik",  
                "pesan":"Semangat dan jangan lupa jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Abangnya humble dan santai",  
                "pesan":"Sukses selalu kedepannya ya bang"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakak ini kalem, humble juga orangnya.",  
                "pesan":"Semoga sukses terus kedepannya yaa kak"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang dafa santai serta asik orangnya.",  
                "pesan":"Semoga terus berkembang dan sukses kedepannya yaa bang"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak ini kalem, namun ramah orangnya.",  
                "pesan":"Semangat terus menjalani kuliahnyaya kak"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "abang ini baik, humble, dan asik orangnya.",  
                "pesan":"sukses selalu dan semangat terus yaa bang"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakak ini kalem, namun ramah dan keren.",  
                "pesan":"Semangat dan jangan lupa jaga kesehatan yaa kak"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Abang ini santai serta humble  orangnya",  
                "pesan":"semangat terus menjalani kuliahnya bang"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Bang Andra sangat asik dan seru pembawaannya, dan keren",  
                "pesan":"Semangat terus menjalani kuliahnya bang Andra"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang Bryan asik serta santai pembawaannya",  
                "pesan":"semoga sukses kedepannya bang bryan"# 1
            },
            {
                "nama": "Giyats Thabularasa Meardhy",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@meardhy_ghiyast",
                "kesan": "Bang giyats santai namun humble orangnya",  
                "pesan":"semangat serta dimudahkan kuliahnya bang"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakak ini kalem, baik, namun humble orangnya",  
                "pesan":"Semangat dan jangan lupa jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kakak ini cantik, santai, dan humble orangnya",  
                "pesan":"Semangat terus menjalani kuliahnya yaa kak"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abang ini santai serta asik orangnya",  
                "pesan":"Sukses selalu kedepannya bang rafka"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10amg5TKBmdRxHin4ezG-wKZO9f9oBj4t",
            "https://drive.google.com/uc?export=view&id=1yy67ibf4acMxy6jekYiM0-SLuNj4WnoX",
            "https://drive.google.com/uc?export=view&id=1WxIX68-_ihczTDHLesaGRR9x9OcFWRXq",
            "https://drive.google.com/uc?export=view&id=18bTYbSpBCJRyFRvFQaBIfIE6Xo34l0Uh",
            "https://drive.google.com/uc?export=view&id=1VyxgqYFoyvosf1rVAPJbC3KX6h4erjUi",
            "https://drive.google.com/uc?export=view&id=1DwDCZ00Tc7ZelQhRaiBDXYByWGMYiBWe",
            "https://drive.google.com/uc?export=view&id=1xfnEEFCQeEkjTmW1dAcOgKrD3VGonLWa",
            "https://drive.google.com/uc?export=view&id=1RDgYnsmBHnEwf_Eg4UWTKDPgM7_j-W9N",
            "https://drive.google.com/uc?export=view&id=1_5l3HmjUPTB083aqTWebBj5GJWPfV5bb",
            "https://drive.google.com/uc?export=view&id=1BT1WfPgEX3R2FXy2vjSvCCxan5cRC8EE",
            "https://drive.google.com/uc?export=view&id=1AXoNBCwjbHNlSdvrTDAycbWUiJfEovmn",
            "https://drive.google.com/uc?export=view&id=1ZmaltQ-kmp63fhGs1HYUTX9kM9Ax3_tb",
            "https://drive.google.com/uc?export=view&id=10p7tI0cbqR-F1Qf3Evdl9_s5gxWvKS-k",
            "https://drive.google.com/uc?export=view&id=1h2DA8E-Xv4JALORn2D7OiZqdikYPeOhU",
            "https://drive.google.com/uc?export=view&id=1oVSC55JpMLbsWUn0DH2p5WjhtXj1yiPM",
            "https://drive.google.com/uc?export=view&id=1rLBf4uRQRXOV46j000ahcCT9QtduQdMm",

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
                "kesan": "bang haikal haikal orangnya santai dan asik",  
                "pesan":"Sukses dan semangat menjalani kuliahnya bang haikal"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma orangnya kalem dan cantik",  
                "pesan":"semangat terus dan jangan lupa jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kak hana super duper humble dan menginspirasi banget",  
                "pesan":"semangat terus dan semoga selal dikelilingi  orang baik ya kak" #1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang farhan santai namun ramah orangnya.",  
                "pesan":"Sukses dan semangat terus kedepanya bang"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "kakak ini kalem, ramah dan cantik.",  
                "pesan":"semangat terus dan jangan lupa jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "....",
                "asal":"....",
                "alamat": "....",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "kakak ini ceria dan sangat asik orangnya.",  
                "pesan":"semoga  sukses dan semangat terus kedepanya kak cerine"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "bang jaya ramah dan santai orangnya.",  
                "pesan":"semangat dan semoga dimudahkan kuliahnya bang jaya"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "kak najla kalem namun ramah orangnya.",  
                "pesan":"semangat dan jangan lupa jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "bang rozak santai namun ramah orangnya",  
                "pesan" :"semangat dan sukses terus bang"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "kak teresa baik, ramah dan pinter orangnya",  
                "pesan":"sukses terus dan makasih sudah mentutokarkan kelas RA kak"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "abang ini asik dan humble orangnya",  
                "pesan":"sukses terus kedepannya ya bang hanif"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "...",
                "asal":"....",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini kalem dan ramah, baik orangnya",  
                "pesan":"semangat dalam menjalani kuliahnya ya kak"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "kakak ini imput cantik dan ramah orangnya",  
                "pesan":"semangtat terus dan jangan lupa jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "kakak ini kalem, baik, namun humble orangnya",  
                "pesan":"semaangat terus menjalani kuliahnya  kak gustin"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "abang ini santai dan kalem namun ramah orangnya",  
                "pesan":"sukses  terus kedepannya bang harvin"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "kakak ini kalem namun ramah orangnya",  
                "pesan":"semangat dan jangan lupa jaga kesehatan ya kak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1j2Eia-rI7F6NQKA8E7cSxjLVOhVUDbYn",
            "https://drive.google.com/uc?export=view&id=1s8IBg5BjbJSMrlrhQZw5SPgMtxMXnbtl",
            "https://drive.google.com/uc?export=view&id=1444m6_o-fmqiFM4vwa2QypanpMNeu3Ds",
            "https://drive.google.com/uc?export=view&id=1JI0Ygp6CJnl2mrkpj1xsGMvH3zB2qM8F",
            "https://drive.google.com/uc?export=view&id=1CWeSftqjoTj8MlmZQIIUkMD2QqtuYdZh",
            "https://drive.google.com/uc?export=view&id=1GCShMY4WPgW1pSvhvBOVJZ6gfsD12L75",
            "https://drive.google.com/uc?export=view&id=1Q4YWn9-3xiGc5z2zLa3kPpEP7wuaK-dh",
            "https://drive.google.com/uc?export=view&id=1_Ia2V_YH3sRz--C5dza5W_be3GvqxAfD",
            "https://drive.google.com/uc?export=view&id=1epNqfIIZdZmbu1kS4XfSu2EfGHVNIFhj",
            "https://drive.google.com/uc?export=view&id=1wT7faDgb8xWGQqq3E8JfZnzIAK-rh2Em",
            "https://drive.google.com/uc?export=view&id=1DfL42Niw3I-pWLelwCQEGljkqFwmk29T",
            "https://drive.google.com/uc?export=view&id=1FF4vKf7T2Lgf2cjTq8IjLUQBlD6hbTSx",
            "https://drive.google.com/uc?export=view&id=1Rif4sHgf-nSSUylUazs7zrkkS4qn6bf6",
            "https://drive.google.com/uc?export=view&id=1Vwi_SCTkj8CGFoGYK1fXKrvVtFTeN1Ad",
            "https://drive.google.com/uc?export=view&id=1StYo_bf-AIre9xK798OuYkyXMPL19a1F",
            "https://drive.google.com/uc?export=view&id=12faBQ29fOjnGdp3eB0pq3RYRqEo285Pc",
            "https://drive.google.com/uc?export=view&id=1uBahgweg7JXHbvvTogL5GB0_54a0U2gu",
            

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
                "kesan": "Kak arienta keren dan sangat menginspirasi buat saya",  
                "pesan":"Semangat terus dan semoga tercapai cita-citanya ya kak"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany kalem dan baik orangnya",  
                "pesan":"Semangat terus menjalani kuliahnya  yaa  kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel tegas dan sangat baik dalam menyampaikan ilmu",  
                "pesan":"Semangat dan semoga dilaancarkan kuliahnya ya bang "# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi selalu semangat saat mendampingi supporteran",  
                "pesan":"Sukses terus kedepannnya ya bang"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang ayake orangnya humoris dan santai",  
                "pesan":"Semangat dan semoga dimudahkan terus ya bang"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang caesar tegas namun tetap humoris orangnya",  
                "pesan":"Sukses selalu dan dilancarkan terus rezekinya bang caesar"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "kak euodia asik dan santai orangnya",  
                "pesan":"Semangat terus menjalani kuliahnya ya kak"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang haikal terlihat santai orangnya",  
                "pesan":"Sukses selalu bang haikal"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak putri aslinya baik dan ramah orangnya",  
                "pesan":"Semangat terus dan jangan lupa jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@queentanaabila",
                "kesan": "Kakak ini terlihat santai orangnya",  
                "pesan":"Semangta terus menjalani kuliahnya ya kak"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman humble, baik dan menginspirasi",  
                "pesan":"Sukses terus dan semoga tercapai apa yang diinginkan ya bang"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "Kakak ini cantik dan ramah orangnya ",  
                "pesan":"Semangat dan jangan lupa jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "Kakak ini cantik, kalem dan baik",  
                "pesan":"Semangat terus dan jangan lupa istirahat ya kak"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Abang ini semangat sekali pas jadi capo",  
                "pesan":"Jangan pernah padam semangatnya ya bang"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kakak ini ramah dan cantik orangnya",  
                "pesan":"Semangat menjalani kuliahnya ya kak"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Abang ini santai dan rapi orangnya",  
                "pesan":"Sukses selalu kedepannhya ya bang"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "Kakak ini kalem dan baik orangnya",  
                "pesan":"semangat terus dan jangan lupa jaga kesehatan ya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
