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
            }, #kesan smpe sini
            {
                "Nama": "Efi Defiyati",
                "Nim": "123450005",
                "Umur": "21 tahun",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobbi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Qois Olifio",
                "Nim": "123450067",
                "Umur": "22 tahun",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl"
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "Nim": "123450079",
                "Umur": "21 tahun",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Berkuda",
                "Sosmed": "@Hafsafazilaa",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Luthfia Laila RAmadhani",
                "Nim": "123450004",
                "Umur": "21 tahun",
                "Asal":"Bengkulu",
                "Alamat": "Airan",
                "Hobbi": "Bermain ke kost Efi",
                "Sosmed": "@luthfiaarmdhni",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
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
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Juesi Apridelia Saragih",
                "Nim": "123450085",
                "Umur": "19 tahun",
                "Asal": "Singkawang",
                "Alamat": "Pelangi",
                "Hobbi": "ngerepeat lagu lover dari taylor swiff",
                "Sosmed": "@j__eesie",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "Nim": "123450023",
                "Umur": "19 tahun",
                "Asal":"Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Suka nonton AGZ",
                "Sosmed": "@ddharu_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "GH. Mikael Niko Antoni Setiadi",
                "Nim": "123450025",
                "Umur": "20 tahun",
                "Asal":"Jombang",
                "Alamat": "Jatiagung",
                "Hobbi": "Jalan-jalan nyari mangsa",
                "Sosmed": "@me._kael",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl"
            },
            {
                "Nama": "Siti Sarifah Sumamahsa",
                "Nim": "124450015",
                "Umur": "18 tahun",
                "Asal":"Palembang",
                "Alamat": "Kedaton",
                "Hobbi": "Bikin Pempek",
                "Sosmed": "@syt.sarifa",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Givaro Ananta",
                "Nim": "123450078",
                "Umur": "20 tahun",
                "Asal":"Gunung Pesagi",
                "Alamat": "Sukabumi",
                "Hobbi": "Minum Kopi",
                "Sosmed": "@givarooo",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "Nim": "124450042",
                "Umur": "20 tahun",
                "Asal":"Krui",
                "Alamat": "Jatimulyo",
                "Hobbi": "Memancing",
                "Sosmed": "@afghanisnt_",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Hani Qurrota Aini",
                "Nim": "124450020",
                "Umur": "19 tahun",
                "Asal":"City Eart",
                "Alamat": "Sukarame",
                "Hobbi": "Baca Au",
                "Sosmed": "@haniquratuain_",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Jeremia Halim",
                "Nim": "124450101",
                "Umur": "20 tahun",
                "Asal":"Beijing",
                "Alamat": "Teluk",
                "Hobbi": "Olahraga",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "Nim": "123450073",
                "Umur": "21 tahun",
                "Asal":"Sumatera Utara",
                "Alamat": "Kota Baru",
                "Hobbi": "Tidur",
                "Sosmed": "@monica_tjg",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "Nim": "123450121",
                "Umur": "20 tahun",
                "Asal":"Depok",
                "Alamat": "Pemda Raya",
                "Hobbi": "Ngegym dan Koleksi Figure",
                "Sosmed": "@nagatseee",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "Nim": "124450082",
                "Umur": "20 tahun",
                "Asal":"Metro",
                "Alamat": "Pemda",
                "Hobbi": "Main",
                "Sosmed": "@sekardnwp",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "Nim": "123450077",
                "Umur": "20 tahun",
                "Asal":"Pasay",
                "Alamat": "Belwis",
                "Hobbi": "Nyapa",
                "Sosmed": "@nshaysk",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "Nim": "123450046",
                "Umur": "21 tahun",
                "Asal": "Lampung Utara",
                "Alamat": "Way Halim",
                "Hobbi": "Mendaki",
                "Sosmed": "@ferazkaa",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Ali Aristo Muthahhari Parisi",
                "Nim": "123450088",
                "Umur": "21 tahun",
                "Asal":"Lampung Timur",
                "Alamat": "Gang Sakum Belwis",
                "Hobbi": "Bawa makanan dari Luar",
                "Sosmed": "ali_parisi3",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "Nim": "123450025",
                "Umur": "20 tahun",
                "Asal":"Jombang",
                "Alamat": "Jatiagung",
                "Hobbi": "Jalan-jalan nyari mangsa",
                "Sosmed": "@me._kael",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl"
            },
            {
                "Nama": "Dafa Elpriza",
                "Nim": "124450131",
                "Umur": "21 tahun",
                "Asal":"Bekasi",
                "Alamat": "Way Kandis",
                "Hobbi": "Mancing",
                "Sosmed": "@dafaelpriza_",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "Nim": "124450002",
                "Umur": "20 tahun",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobbi": "Pulang Kampung",
                "Sosmed": "@slbnzw_",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Muhammad Afdal Lutfi",
                "Nim": "124450047",
                "Umur": "19 tahun",
                "Asal":"Lampung Tengah",
                "Alamat": "Jln. Pulau Damar",
                "Hobbi": "Surving",
                "Sosmed": "@afdall.03",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Juwita Sari",
                "Nim": "124450066",
                "Umur": "19 tahun",
                "Asal":"Lampung Barat",
                "Alamat": "Pemda",
                "Hobbi": "Liat Bila nulis",
                "Sosmed": "@ju.juwitaaa_",
                "Kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "Pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "Nama": "Muhammad Ridwan",
                "Nim": "123450091",
                "Umur": "21 tahun",
                "Asal":"Lampung Tengah",
                "Alamat": "Belwis",
                "Hobbi": "Nontonin Fadyl Badminton",
                "Sosmed": "@mridwaan_22",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Andra Ilham Bintang",
                "Nim": "124450060",
                "Umur": "18",
                "Asal":"Sumatera Selatan",
                "Alamat": "Kota Baru",
                "Hobbi": "Nonton Drama Korea",
                "Sosmed": "@andra.lhm",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "Nim": "124450003",
                "Umur": "20 tahun",
                "Asal":"Nias",
                "Alamat": "Belwis",
                "Hobbi": "Yoga",
                "Sosmed": "@bryantel_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "Nim": "124450067",
                "Umur": "17 tahun",
                "Asal":"Jati Asih",
                "Alamat": "Korpri",
                "Hobbi": "Nyawit",
                "Sosmed": "@meardhy_ghiyats",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "Nim": "124450055",
                "Umur": "20 tahun",
                "Asal":"Pringsewu",
                "Alamat": "Airan",
                "Hobbi": "Main",
                "Sosmed": "@sekardnwp",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "Nim": "....",
                "Umur": "..",
                "Asal":"...",
                "Alamat": "....",
                "Hobbi": "...",
                "Sosmed": "@....",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "Nim": "124450089",
                "Umur": "20 tahun",
                "Asal":"Padang",
                "Alamat": "Kota Baru",
                "Hobbi": "Bangun Pagi",
                "Sosmed": "@muhammdrafka_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450123",
                "umur": "23",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Merokok",
                "sosmed": "@haikalsbln_",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya fadyl"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "....",
                "asal":"....",
                "alamat": "....",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "...",
                "asal":"....",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
