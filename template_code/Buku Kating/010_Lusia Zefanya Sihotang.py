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
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"NIM: {data_list[i]['Nim']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobbi: {data_list[i]['Hobbi']}")
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
            "https://drive.google.com/uc?export=view&id=1rNX8JWhepOwpQ3Kv3_M0IUS4YnkM09Rd", #fajar
            "https://drive.google.com/uc?export=view&id=1AH9lznjyK0Nu28zxDlhnnPOvC_EBKHXS", #aqil
            "https://drive.google.com/uc?export=view&id=1grdCErrJIeSHUbT8EuQtHoSU5KskhWTC", #efi
            "https://drive.google.com/uc?export=view&id=1yB9zDdneKVq6in5YWmgU-qUEZj_K-2EL", #qois
            "https://drive.google.com/uc?export=view&id=1W-ZACfd_5fCOvJ5cM1JZKty9SBoT9tAf", #hafsa
            "https://drive.google.com/uc?export=view&id=1CCaZprQaFDkd236ce27rQVkGtleDlvLU", #luthfia
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "Nim": "123450103",
                "Umur": "22 tahun",
                "Asal":"Batam",
                "Alamat": "Kesektariatan HMSD",
                "Hobbi": "Push IMO",
                "Sosmed": "@jars_mrp",
                "Kesan": "Bang Fajar orangnya baik, humble, ramah, keren.",  
                "Pesan":"Semoga selalu amanah dan semangat terus!"
            },
            {
                "Nama": "Muhammmad Aqil Ramadhan",
                "Nim": "1233450066",
                "Umur": "22 tahun",
                "Asal":"Bangkinang",
                "Alamat": "Kesekretariatan HMSD",
                "Hobbi": "Dzikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Bang Aqil orangnya keren, ramah, baik, lucu, humble.",  
                "Pesan":"semangat terus kuliahnya, semoga suksess!"
            }, 
            {
                "Nama": "Efi Defiyati",
                "Nim": "123450005",
                "Umur": "21 tahun",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobbi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "Kak efi baikk, cantik, ramah, humble, menginspirasi",  
                "Pesan":"semangat terus, semoga kuliahnya lancar"# 1
            },
            {
                "Nama": "Qois Olifio",
                "Nim": "123450067",
                "Umur": "22 tahun",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio",
                "Kesan": "Bang Qois humble, baik, dan juga ramah.",  
                "Pesan":"Semoga selalu semangat menjalani kuliahnya."
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "Nim": "123450079",
                "Umur": "21 tahun",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Berkuda",
                "Sosmed": "@Hafsafazilaa",
                "Kesan": "Kak Hafsa orangnya sangat humble, baik, ramah, cantik, lucu.",  
                "Pesan":"Semangat teruss, semoga kuliahnya lancar!"# 1
            },
            {
                "Nama": "Luthfia Laila RAmadhani",
                "Nim": "123450004",
                "Umur": "21 tahun",
                "Asal":"Bengkulu",
                "Alamat": "Airan",
                "Hobbi": "Bermain ke kost Efi",
                "Sosmed": "@luthfiaarmdhni",
                "Kesan": "Kak luthfia cantik, baik, lucu, imut",  
                "Pesan":"Semangat terus kuliahnya, semoga segala urusan dipermudah"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K-isIFgn6HvwJtwTmbI-3RtqdS7aGK_S", #ridho
            "https://drive.google.com/uc?export=view&id=1gJ0bWveF75juLLKSv7Wz5M6f1b7cOOPE", #juesi
            "https://drive.google.com/uc?export=view&id=13hOQxPJhR0LP-4NLHZ6Tq22IknUroKev", #dharu
            "https://drive.google.com/uc?export=view&id=1uf7X3C-e-6q6hC9NdYcz4resSg3vrZJM", #niko
            "https://drive.google.com/uc?export=view&id=1unhvBuU4oIhHEICwm203iQ2fNZ1zowh3", #siti
            "https://drive.google.com/uc?export=view&id=1hymilXDXDFtHVvoI3wpLYa3zVPS7VfIh", #givaro
            "https://drive.google.com/uc?export=view&id=1dWCfMFeECsVXDOAourJtOaxN5DKo8IOQ", #afghanis
            "https://drive.google.com/uc?export=view&id=1SrbqqKK0GbkBQ0kAAPOI_UlmZBMTme_O", #hani
            "https://drive.google.com/uc?export=view&id=14Zi5341mjd7Gyz0dGX0s0LrannlgKtlt", #jeremia
            "https://drive.google.com/uc?export=view&id=1VpR1pzSnRTt9hqlhNRDTDTB07Yd0j1tq", #monica
            "https://drive.google.com/uc?export=view&id=1L-Tf8joRiSpRjavQltAT8aux1v4-azmH", #jona
            "https://drive.google.com/uc?export=view&id=1fFx49X97EvHMW3J8MXPbXeVn_OKNDok6", #sekar
            "https://drive.google.com/uc?export=view&id=18CuJjVPSbFHD0ujBimjECwLt5wAHXd3b", #wan

        ]
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "Nim": "123450060",
                "Umur": "20 tahun",
                "Asal": "Kuala lumpur",
                "Alamat": "GH",
                "Hobbi": "Bernyanyi",
                "Sosmed": "@iamridhomanik",
                "Kesan": "Bang Ridho orangnya baik, keren, hebat, ramah",  
                "Pesan":"Semoga selalu semangat dan amanah menjalani tanggungjawabnya"# 1
            },
            {
                "Nama": "Juesi Apridelia Saragih",
                "Nim": "123450085",
                "Umur": "19 tahun",
                "Asal": "Singkawang",
                "Alamat": "Pelangi",
                "Hobbi": "ngerepeat lagu lover dari taylor swiff",
                "Sosmed": "@j__eesie",
                "Kesan": "Kak Jue sangat lucu dan aktif, sangat ramah dan baik sekali",  
                "Pesan":"semangat terus kak, semoga selalu bahagia dan semoga lancar kuliahnya"# 1
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "Nim": "123450023",
                "Umur": "19 tahun",
                "Asal":"Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Suka nonton AGZ",
                "Sosmed": "@ddharu_",
                "Kesan": "bang Dharu keren, gacor sekali, ramah, baik, humble",  
                "Pesan":"Selalu semangat dan semoga sukses. Semoga pinternya nular ke saya"# 1
            },
            {
                "Nama": "GH. Mikael Niko Antoni Setiadi",
                "Nim": "123450025",
                "Umur": "20 tahun",
                "Asal":"Jombang",
                "Alamat": "Jatiagung",
                "Hobbi": "Jalan-jalan nyari mangsa",
                "Sosmed": "@me._kael",
                "Kesan": "Bang Niko lucu, keren, baik, humble, ramah",  
                "Pesan":"Semoga selalu semangat dan semoga sukses. God Bless U!"
            },
            {
                "Nama": "Siti Sarifah Sumamahsa",
                "Nim": "124450015",
                "Umur": "18 tahun",
                "Asal":"Palembang",
                "Alamat": "Kedaton",
                "Hobbi": "Bikin Pempek",
                "Sosmed": "@syt.sarifa",
                "Kesan": "Kak siti lucu, baik, ramah, cantik, manisss",  
                "Pesan":"Semangat terus, semoga selalu bahagia menjalani hidup"# 1
            },
            {
                "Nama": "Givaro Ananta",
                "Nim": "123450078",
                "Umur": "20 tahun",
                "Asal":"Gunung Pesagi",
                "Alamat": "Sukabumi",
                "Hobbi": "Minum Kopi",
                "Sosmed": "@givarooo",
                "Kesan": "Bang Givaro keren, ramah, baik, humble",  
                "Pesan":"Semangat terus bang, semoga segala urusannya dipermudah"# 1
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "Nim": "124450042",
                "Umur": "20 tahun",
                "Asal":"Krui",
                "Alamat": "Jatimulyo",
                "Hobbi": "Memancing",
                "Sosmed": "@afghanisnt_",
                "Kesan": "Kak Nisa baik banget, ramah, lucu, cantik",  
                "Pesan":"Semangat terus kak, semoga selalu datang hal hal baik untuk kakak"# 1
            },
            {
                "Nama": "Hani Qurrota Aini",
                "Nim": "124450020",
                "Umur": "19 tahun",
                "Asal":"City Eart",
                "Alamat": "Sukarame",
                "Hobbi": "Baca Au",
                "Sosmed": "@haniquratuain_",
                "Kesan": "Kak hani lucu banget, cantik juga, baik, manis",  
                "Pesan":"Semangat kuliahnyaa, semoga nasinya selalu hangat"# 1
            },
            {
                "Nama": "Jeremia Halim",
                "Nim": "124450101",
                "Umur": "20 tahun",
                "Asal":"Beijing",
                "Alamat": "Teluk",
                "Hobbi": "Olahraga",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Bang Jeremia sangat humble, ramah, kerennn",  
                "Pesan":"Semangat bang!! Semoga sukses dan impiannya dapat tercapai"# 1
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "Nim": "123450073",
                "Umur": "21 tahun",
                "Asal":"Sumatera Utara",
                "Alamat": "Kota Baru",
                "Hobbi": "Tidur",
                "Sosmed": "@monica_tjg",
                "Kesan": "Sangat baik, ramah, lucu, cantik, humble",  
                "Pesan":"Semoga lancar terus kuliahnya dan selalu bahagia"# 1
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "Nim": "123450121",
                "Umur": "20 tahun",
                "Asal":"Depok",
                "Alamat": "Pemda Raya",
                "Hobbi": "Ngegym dan Koleksi Figure",
                "Sosmed": "@nagatseee",
                "Kesan": "Bang Jona baik, ramah, keren, humble",  
                "Pesan":"semangat terus kuliahnya dan semoga dipermudah segala urusannya"# 1
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "Nim": "124450082",
                "Umur": "20 tahun",
                "Asal":"Metro",
                "Alamat": "Pemda",
                "Hobbi": "Main",
                "Sosmed": "@sekardnwp",
                "Kesan": "Kakak nya baik, cantik, ramahh, humble, manis",  
                "Pesan":"semangat kuliahnya kak! Semoga bantalnya selalu dingin"# 1
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "Nim": "123450077",
                "Umur": "20 tahun",
                "Asal":"Pasay",
                "Alamat": "Belwis",
                "Hobbi": "Nyapa",
                "Sosmed": "@nshaysk",
                "Kesan": "Kakaknya baik, ramah, cantik, humble, keren",  
                "Pesan":"semangat kuliahnya, semoga sukses dan urusannya dipermudah di segala hal"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CJIu5sTnUs6JNNWiYs-2AdasT_aej_xo", #kevin
            "https://drive.google.com/uc?export=view&id=1wX0BymmYMlRwClJKN6t1-8hEVVYJdtPk", #gusti
            "https://drive.google.com/uc?export=view&id=1ON8FBjE95Z9LCOak7NkP94MOuX2uvEk-", #ali
            "https://drive.google.com/uc?export=view&id=1h6fyIiHFZpu1seeQQlpf_Yz6kDCIRYad", #ayu
            "https://drive.google.com/uc?export=view&id=177Ai9cOfSLvee5asW3jIGo4fLaq-38Om", #dafa
            "https://drive.google.com/uc?export=view&id=1EvuW6TTyR4CG7kalq_Ze6LScCeDAvMzT", #salsabila
            "https://drive.google.com/uc?export=view&id=1cS7fK5FoMGluiZh6p6s2O-ztZlVwBUO4", #afdal
            "https://drive.google.com/uc?export=view&id=1h8hf9VI2KwG61mEWflRWOun4T7od8qQi", #juwita
            "https://drive.google.com/uc?export=view&id=12orv3wrkpcDjyrDR3ica0hchewVNlcE3", #ridwan
            "https://drive.google.com/uc?export=view&id=1m9BcmPjOeWPpVTdMM2jmptlgBxqjI2vN", #andra
            "https://drive.google.com/uc?export=view&id=18oHkIFpp7CO6KYVrGJDQS3PpSlDnzjJ4", #bryan
            "https://drive.google.com/uc?export=view&id=1fWLqujL3WZrJaqPNaD-JRSyusrd3aKW2", #ghiyats
            "https://drive.google.com/uc?export=view&id=1Z8s2-r5slmsCTkXCWCyA02xQJv81ZRTk", #indah
            "https://drive.google.com/uc?export=view&id=1eSzDKM-W8pNm4KTDent8525LLW999hJL", #jacinda
            "https://drive.google.com/uc?export=view&id=1h3FaobzvfXeXjEoLdozJb-qqggLckWJA",#rafka
        ]
        data_list = [
            {
                "Nama": "Kevin Antonio Junior",
                "Nim": "123450109",
                "Umur": "20 tahun",
                "Asal": "Maluku",
                "Alamat": "Panjang",
                "Hobbi": "Menari",
                "Sosmed": "@kevinaj__",
                "Kesan": "Bang Kevin orangnya sangat humble, baik, dan menginspirasi ",  
                "Pesan":"Semoga amanah dan selalu semangat kuliahnya"
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "Nim": "123450046",
                "Umur": "21 tahun",
                "Asal": "Lampung Utara",
                "Alamat": "Way Halim",
                "Hobbi": "Mendaki",
                "Sosmed": "@ferazkaa",
                "Kesan": "Kakak nya baik, cantik, ramah, humble, manis",  
                "Pesan":"semangat terus kuliahnya dan semoga sukses"
            },
            {
                "Nama": "Ali Aristo Muthahhari Parisi",
                "Nim": "123450088",
                "Umur": "21 tahun",
                "Asal":"Lampung Timur",
                "Alamat": "Gang Sakum Belwis",
                "Hobbi": "Bawa makanan dari Luar",
                "Sosmed": "ali_parisi3",
                "Kesan": "Bang Ali orangnya humble, ramah, keren",  
                "Pesan":"Semoga lancar terus kuliahnya dan semoga sukses"
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "Nim": "123450025",
                "Umur": "20 tahun",
                "Asal":"Jombang",
                "Alamat": "Jatiagung",
                "Hobbi": "Jalan-jalan nyari mangsa",
                "Sosmed": "@me._kael",
                "Kesan": "Kakaknya baik, ramah, humble, keren",  
                "Pesan":"Semoga selalu sehat dan bahagia selalu, serta lancar kuliahnya"
            },
            {
                "Nama": "Dafa Elpriza",
                "Nim": "124450131",
                "Umur": "21 tahun",
                "Asal":"Bekasi",
                "Alamat": "Way Kandis",
                "Hobbi": "Mancing",
                "Sosmed": "@dafaelpriza_",
                "Kesan": "Bang Dafa ramah, keren, humble, baik",  
                "Pesan":"Semoga selalu lancar kuliahnya dan semangat terus!"# 1
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "Nim": "124450002",
                "Umur": "20 tahun",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobbi": "Pulang Kampung",
                "Sosmed": "@slbnzw_",
                "Kesan": "Kak salsabila orangnya baik, ramah, humble, cantik",  
                "Pesan":"Semoga lancar kuliahnya dan selalu bahagia ya kak"# 1
            },
            {
                "Nama": "Muhammad Afdal Lutfi",
                "Nim": "124450047",
                "Umur": "19 tahun",
                "Asal":"Lampung Tengah",
                "Alamat": "Jln. Pulau Damar",
                "Hobbi": "Surving",
                "Sosmed": "@afdall.03",
                "Kesan": "Bang Afdal orangnya baik, keren, ramah, humble",  
                "Pesan":"Semoga selalu sehat dan semoga kuliahnya lancar ya bang"# 1
            },
            {
                "Nama": "Juwita Sari",
                "Nim": "124450066",
                "Umur": "19 tahun",
                "Asal":"Lampung Barat",
                "Alamat": "Pemda",
                "Hobbi": "Liat Bila nulis",
                "Sosmed": "@ju.juwitaaa_",
                "Kesan": "Kak juwita baik, cantikk, ramah, keren",  
                "Pesan":"Semoga selalu ketemu lampu hijau tiap di perempatan"# 1
            },
            {
                "Nama": "Muhammad Ridwan",
                "Nim": "123450091",
                "Umur": "21 tahun",
                "Asal":"Lampung Tengah",
                "Alamat": "Belwis",
                "Hobbi": "Nontonin Fadyl Badminton",
                "Sosmed": "@mridwaan_22",
                "Kesan": "Baik sekali, ramah, humble, kerenn",  
                "Pesan":"semangat terus kuliahnya kakak ! Semoga dipermudah segala urusannya."# 1
            },
            {
                "Nama": "Andra Ilham Bintang",
                "Nim": "124450060",
                "Umur": "18",
                "Asal":"Sumatera Selatan",
                "Alamat": "Kota Baru",
                "Hobbi": "Nonton Drama Korea",
                "Sosmed": "@andra.lhm",
                "Kesan": "bang Andra baik, ramah, kerenn, humble banget",  
                "Pesan":"semoga kuliahnya lancar dan segala urusannya dipermudah"# 1
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "Nim": "124450003",
                "Umur": "20 tahun",
                "Asal":"Nias",
                "Alamat": "Belwis",
                "Hobbi": "Yoga",
                "Sosmed": "@bryantel_",
                "Kesan": "Bang Bryan keren, lucu, baik, ramah, humble",  
                "Pesan":"semangat terus bang! Semoga menjadi kebanggan orangtua" 
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "Nim": "124450067",
                "Umur": "17 tahun",
                "Asal":"Jati Asih",
                "Alamat": "Korpri",
                "Hobbi": "Nyawit",
                "Sosmed": "@meardhy_ghiyats",
                "Kesan": "Abangnya lucu, keren, baik, humble",  
                "Pesan":"semangat terus bang, semoga selalu bahagia dan senang" 
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "Nim": "124450055",
                "Umur": "20 tahun",
                "Asal":"Pringsewu",
                "Alamat": "Airan",
                "Hobbi": "Main",
                "Sosmed": "@indahjuliaa",
                "Kesan": "Kakak nya baik, cantik, ramah",  
                "Pesan":"semangat terus kuliahnya kakak dan semoga bahagia selalu kakak"
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "Nim": "....",
                "Umur": "..",
                "Asal":"...",
                "Alamat": "....",
                "Hobbi": "...",
                "Sosmed": "@....",
                "Kesan": "Kakak nya baik, humble, kerenn",  
                "Pesan":"semangat terus kakak semoga nasinya selalu hangat"# 1
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "Nim": "124450089",
                "Umur": "20 tahun",
                "Asal":"Padang",
                "Alamat": "Kota Baru",
                "Hobbi": "Bangun Pagi",
                "Sosmed": "@muhammdrafka_",
                "Kesan": "Bang Rafka keren, baik, humble, ramah",  
                "Pesan":"semangat terus, semoga selalu bahagia dan segala urusan diperlancar"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qxbBD6czsVvJ4cqC69ab6_79nzy4coD_", #haikal
            "https://drive.google.com/uc?export=view&id=1p-k60X15MJjHQhrnTb3z5SX251WLtbWH", #kharisma
            "https://drive.google.com/uc?export=view&id=1sndFgONdHm-vYdutBIPrIbvo0kRCbmn4", #hanna
            "https://drive.google.com/uc?export=view&id=19CpFORRvs7H2Wo1MCZRHhP_iFEt1aLo5", #farhan
            "https://drive.google.com/uc?export=view&id=1lDuzjioWFOgZQKLaJf9fELfrVWoZLyIj", #aisyah
            "https://drive.google.com/uc?export=view&id=1TC6soPOyhMr9FWXoDUmdoNU8Y3UkDe8l", #cerine
            "https://drive.google.com/uc?export=view&id=1VntZ_fZ5216tNnoQGjgQGUI1w9VO0cBq", #jaya
            "https://drive.google.com/uc?export=view&id=1tJ8wlsUid3e7Vxp1UmdFFTHr99GIlb9j", #najla
            "https://drive.google.com/uc?export=view&id=1Ge-6ysk-JO9gog4QooeBE2M1t_Elh8LK", #rozak
            "https://drive.google.com/uc?export=view&id=1FvIrVA5IAC4T863j79UMAL8mNgIcrkIE", #teresa
            "https://drive.google.com/uc?export=view&id=1BhoQuImukdQ5zTEH0VP5SBHjo48ErN4I", #hanif
            "https://drive.google.com/uc?export=view&id=1Y5jPem66McDOpQFxb58IZUvvHXLnpx7S", #audina
            "https://drive.google.com/uc?export=view&id=1H2bCRXhpPeLgQeI_aOs5oijdLvhSjJhV", #cika
            "https://drive.google.com/uc?export=view&id=1sqi9nGf4Ql4p7HvfHiPlKzjEEuViPn0r", #gustin
            "https://drive.google.com/uc?export=view&id=1goED48S0PjjaYjjPeELk8jU1bWLKQvuF", #harvinsyah
            "https://drive.google.com/uc?export=view&id=1KQP8_iK2dE3ZoIyyzQE6iEJSBPNLd21f", #sabina     
        ]
        data_list = [
            {
                "Nama": "Haikal Fransiskus Simbolon",
                "Nim": "123450123",
                "Umur": "23",
                "Asal": "Bengkulu",
                "Alamat": "Belwis",
                "Hobbi": "Merokok",
                "Sosmed": "@haikalsbln_",
                "Kesan": "Bang Haikal keren, baik, ramah, humble.",  
                "Pesan":"Semoga selalu bahagia dan semoga amanah menjalani tugasnya"# 1
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "Nim": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "untung suropat",
                "Hobbi": "Suka menolong orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Kakak nya baik, manis, humble, ramah, lucuu",  
                "Pesan":"semangat kuliahnya dan semoga selalu lancar"# 1
            },
            {
                "Nama": "Hanna Grecia Sinaga",
                "Nim": "123450038",
                "Umur": "21",
                "Asal": "Kisaran",
                "Alamat": "Sukarame",
                "Hobbi": "menyapa satpam gedung f",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Kakak nya aktif, baik, lucu, ramah, manis sekalii",  
                "Pesan":"selalu bahagia ya kak! semoga kuliahnya juga lancar terus"# 1
            },
            {
                "Nama": "Farhan Ghani",
                "Nim": "123450121",
                "Umur": "19",
                "Asal": "Kemiling",
                "Alamat": "Kemiling",
                "Hobbi": "Suka motor bukan ngabers",
                "Sosmed": "@farhanghani",
                "Kesan": "Bang Farhan baik, ramah, humble, keren",  
                "Pesan":"Semoga selalu bahagia dan lancar kuliahnya"
            },
            {
                "Nama": "Aisyah Khairun Nissa",
                "Nim": "124450096",
                "Umur": "18",
                "Asal":"Riau",
                "Alamat": "Belwis",
                "Hobbi": "Ngestalker in orang",
                "Sosmed": "@aisyahkhair",
                "Kesan": "Kak Aisyah humble, cantik, lucu, manis",  
                "Pesan":"Semoga selalu bahagia dan lancar kuliahnya"# 1
            },
            {
                "Nama": "Cerine Sihotang",
                "Nim": "124450049",
                "Umur": "20 tahun",
                "Asal":"....",
                "Alamat": "....",
                "Hobbi": "....",
                "Sosmed": "@cceluv3",
                "Kesan": "Kak Cerine baik, ramah, cantik, manis, lucu banget",  
                "Pesan":"Semoga lancar kuliahnya dan semoga nasinya selalu hangat"# 1
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "Nim": "124450094",
                "Umur": "22",
                "Asal":"kisaran city",
                "Alamat": "Pemda city",
                "Hobbi": "Balap liar",
                "Sosmed": "@jay_saputra_tmb",
                "Kesan": "Bang Jaya baik, keren, ramah, humble",  
                "Pesan":"Semoga selalu disertai setiap langkah hidupnya sama Tuhan ya bang"# 1
            },
            {
                "Nama": "Najla Nursyifa",
                "Nim": "124450051",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@...",
                "Kesan": "Kakaknya baik, ramah, humble, cantik, manis",  
                "Pesan":"Semoga selalu bahagia dan lancar kuliahnya"# 1
            },
            {
                "Nama": "Rozak Ramdani",
                "Nim": "124450100",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@...",
                "Kesan": "Bang rozak keren, baik, ramah, humble",  
                "Pesan":"semangat terus kuliahnya dan semoga selalu bahagia"# 1
            },
            {
                "Nama": "Teresa Christiani Purba",
                "Nim": "124450046",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@...",
                "Kesan": "Kakak nya baik, ramah, humble, keren, cantik",  
                "Pesan":"semangat terus kuliahnya kak, semoga selalu bahagia!"# 1
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "Nim": "123450064",
                "Umur": "21",
                "Asal":"Padang",
                "Alamat": "Perumnas Way Kandis",
                "Hobbi": "Main game fps",
                "Sosmed": "@hndfzky_",
                "Kesan": "Bang Hanif baik, ramah, keren, humble",  
                "Pesan":"semangat selalu semoga bahagia!"# 1
            },
            {
                "Nama": "Audina Fitria",
                "Nim": "124450038",
                "Umur": "...",
                "Asal":"....",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@...",
                "Kesan": "Kk audina baikk, ramah, lucu, cantik, manis",  
                "Pesan":"semangat kuliahnya semoga sukses dan selalu bahagia kak"# 1
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "Nim": "124450050",
                "Umur": "20",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobbi": "Dengerin Musik",
                "Sosmed": "@Cikamrbn",
                "Kesan": "Kknya cantikkk, baik, ramah, humble, maniss",  
                "Pesan":"semoga bahagia selalu dan sukses dalam kuliahnya!"# 1
            },
            {
                "Nama": "Gustin H. Tampubolon",
                "Nim": "124450068",
                "Umur": "...",
                "Asal": "...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@...",
                "Kesan": "Kakak nya baik, ramah, cantikk, manis",  
                "Pesan":"semangat terus kuliahnya dan semoga selalu dalam lindungan Tuhan"# 1
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "Nim": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobbi": "Berkuda",
                "Sosmed": "@Muhvnz_",
                "Kesan": "Abangnya baik, ramah, keren, humble",  
                "Pesan":"selalu bahagia dan semoga segala urusannya dipermudah"# 1
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "Nim": "124450036",
                "Umur": "...",
                "Asal": "...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@snasaa._",
                "Kesan": "Kakaknya baik, ramah, cantik, manisss",  
                "Pesan":"semangat kuliahnya dan semoga selalu bahagia ya kak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()


elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BsfxXTJZj_3X2_Sqy6evNJ_KNkk2ts-k", #arienta
            "https://drive.google.com/uc?export=view&id=1k-Nu76CIYTIb108N3ipbhJwlT-rwtyHY", #vany
            "https://drive.google.com/uc?export=view&id=1yF_q0ROV_oomGPkrGM3X8FnFvb769iKW", #nobel
            "https://drive.google.com/uc?export=view&id=1yqnJ5_qfrhtsOqX01F4DY6m5-mL3gxAW", #azmi
            "https://drive.google.com/uc?export=view&id=1HOv1T_A2fJPC0FBPcAFRoNMg4YzOFu8k", #ayake
            "https://drive.google.com/uc?export=view&id=1B4QdfQDrdJ6SdPJp85_ZJx9i44P4W6mv", #caesar
            "https://drive.google.com/uc?export=view&id=1v7pnsIP34t09mY9uSnXFDcqbVlUL4WFx", #euodia
            "https://drive.google.com/uc?export=view&id=1FLOqtdGQNah2bNGsq4jFVPAsCMW6nWux", #haikal
            "https://drive.google.com/uc?export=view&id=181DcNQDnkB9PVuKGmjcPVeKqImQp85Ng", #putri
            "https://drive.google.com/uc?export=view&id=1zpUq-oeCPqIIPGz8tHNqHH_uuIOK5zDJ", #queenta
            "https://drive.google.com/uc?export=view&id=1B8khPr4ZAvDLA8i3JaHPJhaHjkr2VDWA", #desman
            "https://drive.google.com/uc?export=view&id=1-F-21IxjxtkXytETP_tBG7OlpJvAFWs8", #azzelya
            "https://drive.google.com/uc?export=view&id=1DOoSVtGd49vPhGVnlN1-USAM4T9Urb5Y", #charrlindah
            "https://drive.google.com/uc?export=view&id=1OErvkDNwh5qN17uZzFwpEA11tQbVQ53J", #jeremi
            "https://drive.google.com/uc?export=view&id=1RwMLVpyOPDVWckCMfsYi6P2rtDrJAABF", #nabila
            "https://drive.google.com/uc?export=view&id=1x2gqyRCdFHntUlyff6NxbvlrYvlFWQV8", #rafli
            "https://drive.google.com/uc?export=view&id=11Q-9xSVfxz0s9QKWSTklPvCm0sln3Ph-", #salavi

        ]
        data_list = [
            {
                "Nama": "Arienta Khusnul Ananda",
                "Nim": "123450097",
                "Umur": "21",
                "Asal": "Pinggir Pantai",
                "Alamat": "Samping Kost Capo",
                "Hobbi": "Ngerjain Anak Kader",
                "Sosmed": "@arientakhsnl_",
                "Kesan": "Kak Arienta baik, ramah, humble, cantik, manis",  
                "Pesan":"Semoga selalu semangat jalanin kuliahnya"# 1
            },
            {
                "Nama": "Vany Salsabila Putri",
                "Nim": "123450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Pudan Kost",
                "Hobbi": "Pacaran",
                "Sosmed": "@vany.salsabilaa",
                "Kesan": "Kak Vany lucu, baik, dan ramah",  
                "Pesan":"Semoga selalu bahagia dan sukses dalam menjalani kuliahnya"# 1
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "Nim": "123450023",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Banyak",
                "Sosmed": "@nobelnizam",
                "Kesan": "Bang Nobel baik, ramah, humble, keren",  
                "Pesan":"Semoga selalu sehat dan sukses selalu"# 1
            },
            {
                "Nama": "Afriza Azmi",
                "Nim": "124450110",
                "Umur": "20",
                "Asal":"Malang",
                "Alamat": "Lapangan",
                "Hobbi": "Berantem",
                "Sosmed": "@friezazmi",
                "Kesan": "Bang Azmi ramah, humble, baik",  
                "Pesan":"Semoga selalu bahagia dan menjadi kebanggaan orang tua"
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "Nim": "124450059",
                "Umur": "21",
                "Asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "Alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "Hobbi": "Cekek Ayam",
                "Sosmed": "@ykeall",
                "Kesan": "Bang Ayake ramah, baik, keren, humbleee",  
                "Pesan":"Semoga selalu sehat dan sukses dalam menjalani kuliahnya"# 1
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "Nim": "124450017",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobbi": "Pulang Kampung",
                "Sosmed": "@caesar.oriza",
                "Kesan": "Bang Caesar lucu, baik, ramah, keren",  
                "Pesan":"Semoga kuliahnya lancar, menjalani kuliah dengan penuh semangat"# 1
            },
            {
                "Nama": "Euodia Meiliana Fredita",
                "Nim": "124450029",
                "Umur": "18",
                "Asal":"dari mana aja boleh",
                "Alamat": "Didalam Kamar dibalik pintu",
                "Hobbi": "Surving",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Kak Euodia baik, ramah, humble, cantik, manis",  
                "Pesan":"Semoga selalu dalam lindungan Tuhan dan semangat"# 1
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "Nim": "124450032",
                "Umur": "Tinggi Bang Azmi - 155",
                "Asal":"Jambi",
                "Alamat": "Belakang Pemancingan",
                "Hobbi": "Tidur",
                "Sosmed": "@_haikaaall",
                "Kesan": "Bang Haikal baik, ramah, keren, humble",  
                "Pesan":"Semoga selalu sehat dan bahagia dan dapat membanggakan orangtua"# 1
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "Nim": "....",
                "Umur": "...",
                "Asal": "....",
                "Alamat": "...",
                "Hobbi": "....",
                "Sosmed": "@putrimannaa",
                "Kesan": "Kakaknya baik, ramah, dan menginspirasi.",  
                "Pesan":"Semoga selalu semangat jalanin kuliahnya dan semoga Tuhan memberkati"# 1
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "Nim": "124450059",
                "Umur": "19",
                "Asal": "Rumah sakit",
                "Alamat": "Depan pemancingan",
                "Hobbi": "Makanin anak ayam",
                "Sosmed": "@queentanaabila",
                "Kesan": "Kakaknya baik, ramah, humble, cantik, manis",  
                "Pesan":"Semoga selalu sehat dan bahagia ya kak"# 1
            },
            {
                "Nama": "Desman Velius Halawa",
                "Nim": "123450114",
                "Umur": "...",
                "Asal": "...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@dsmanhal",
                "Kesan": "Bang Desman baik, ramah, humble, keren",  
                "Pesan":"Semoga selalu bahagia dan sehat selalu"# 1
            },
            {
                "Nama": "Azzelya Thianandry",
                "Nim": "124450041",
                "Umur": "...",
                "Asal": "...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@azzelytn",
                "Kesan": "Kakaknya baik, ramah, cantik, humble, manis",  
                "Pesan":"Semoga selalu sehat, kuliah lancar, dan sukses"# 1
            },
            {
                "Nama": "Charrlindah",
                "Nim": "124450041",
                "Umur": "...",
                "Asal": "...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@charrlln",
                "Kesan": "Kakaknya cantik, baik, ramah, manis, lucuu",  
                "Pesan":"Semoga selalu sehat dan semangat jalanin kuliahnya ya kak"# 1
            },
            {
                "Nama": "Jeremi Marolop P. Situmorang",
                "Nim": "...",
                "Umur": "...",
                "Asal":"....",
                "Alamat": "....",
                "Hobbi": "...",
                "Sosmed": "@jemarrro",
                "Kesan": "Bang jeremi baik, ramah, humble, keren",  
                "Pesan":"Semoga kuliahnya lancar dan dipermudah segala urusannya"# 1
            },
            {
                "Nama": "Nabila Nur Azizah",
                "Nim": "124450048",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@n.bila_a",
                "Kesan": "Kakaknya baik, ramah, cantik, humble, manis",  
                "Pesan":"Semoga selalu bahagia dan selalu dalam lindungan Tuhan"
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "Nim": "124450007",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@dearfkvmfl",
                "Kesan": "Bang Rafli baik, ramah, humble, keren",  
                "Pesan":"Semoga selalu sehat dan sukses dalam kuliahnya"
            },
            {
                "Nama": "Salavi Naharani",
                "Nim": "124450090",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@avi.nhr",
                "Kesan": "Kakaknya cantik, baik, ramah, humble, manis",  
                "Pesan":"Semoga selalu sehat dan sukses menjalani kuliahnya."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
