import streamlit as st
from streamlit_option_menu import option_menu
import sys
import os

# Menambahkan root project ke sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from tools.ui_helper import (
    inject_custom_css,
    load_image,
    render_kating_cards,
    get_menu_styles,
)

# Injeksi tema estetis global
inject_custom_css()

# Header Halaman Buku Kating
st.markdown(
    """
    <div style="text-align: center; padding: 10px 0 16px 0;">
        <h1 class="g-title" style="font-size: 2.8rem; margin-top: 4px;">
            BUKU KATING
        </h1>
    </div>
    """,
    unsafe_allow_html=True,
)


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
        styles=get_menu_styles(),
    )
    return selected


def display_images_with_data(gambar_urls, data_list):
    """Menampilkan kating dalam bentuk Wide Horizontal Showcase Cards elegan dengan fitur live search."""
    render_kating_cards(gambar_urls, data_list, department_title=menu)


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
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22 ",
                "asal":"Batam",
                "alamat": "Kesektariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Fajar orangnya baik, humble, ramah, keren.",  
                "pesan":"Semoga selalu amanah dan semangat terus!"
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22 ",
                "asal":"Bangkinang",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil orangnya keren, ramah, baik, lucu, humble.",  
                "pesan":"semangat terus kuliahnya, semoga suksess!"
            }, 
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21 ",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak efi baikk, cantik, ramah, humble, menginspirasi",  
                "pesan":"semangat terus, semoga kuliahnya lancar"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22 ",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois humble, baik, dan juga ramah.",  
                "pesan":"Semoga selalu semangat menjalani kuliahnya."
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21 ",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa orangnya sangat humble, baik, ramah, cantik, lucu.",  
                "pesan":"Semangat teruss, semoga kuliahnya lancar!"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21 ",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak luthfia cantik, baik, lucu, imut",  
                "pesan":"Semangat terus kuliahnya, semoga segala urusan dipermudah"# 1
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
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20 ",
                "asal": "Kuala lumpur",
                "alamat": "GH",
                "hobbi": "Bernyanyi",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho orangnya baik, keren, hebat, ramah",  
                "pesan":"Semoga selalu semangat dan amanah menjalani tanggungjawabnya"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19 ",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue sangat lucu dan aktif, sangat ramah dan baik sekali",  
                "pesan":"semangat terus kak, semoga selalu bahagia dan semoga lancar kuliahnya"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19 ",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "bang Dharu keren, gacor sekali, ramah, baik, humble",  
                "pesan":"Selalu semangat dan semoga sukses. Semoga pinternya nular ke saya"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20 ",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Niko lucu, keren, baik, humble, ramah",  
                "pesan":"Semoga selalu semangat dan semoga sukses. God Bless U!"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18 ",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kak siti lucu, baik, ramah, cantik, manisss",  
                "pesan":"Semangat terus, semoga selalu bahagia menjalani hidup"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20 ",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro keren, ramah, baik, humble",  
                "pesan":"Semangat terus bang, semoga segala urusannya dipermudah"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20 ",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak Nisa baik banget, ramah, lucu, cantik",  
                "pesan":"Semangat terus kak, semoga selalu datang hal hal baik untuk kakak"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19 ",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kak hani lucu banget, cantik juga, baik, manis",  
                "pesan":"Semangat kuliahnyaa, semoga nasinya selalu hangat"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20 ",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremia sangat humble, ramah, kerennn",  
                "pesan":"Semangat bang!! Semoga sukses dan impiannya dapat tercapai"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21 ",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Sangat baik, ramah, lucu, cantik, humble",  
                "pesan":"Semoga lancar terus kuliahnya dan selalu bahagia"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20 ",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jona baik, ramah, keren, humble",  
                "pesan":"semangat terus kuliahnya dan semoga dipermudah segala urusannya"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20 ",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak nya baik, cantik, ramahh, humble, manis",  
                "pesan":"semangat kuliahnya kak! Semoga bantalnya selalu dingin"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20 ",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya baik, ramah, cantik, humble, keren",  
                "pesan":"semangat kuliahnya, semoga sukses dan urusannya dipermudah di segala hal"
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
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20 ",
                "asal": "Maluku",
                "alamat": "Panjang",
                "hobbi": "Menari",
                "sosmed": "@kevinaj__",
                "kesan": "Bang Kevin orangnya sangat humble, baik, dan menginspirasi ",  
                "pesan":"Semoga amanah dan selalu semangat kuliahnya"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21 ",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak nya baik, cantik, ramah, humble, manis",  
                "pesan":"semangat terus kuliahnya dan semoga sukses"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21 ",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Bang Ali orangnya humble, ramah, keren",  
                "pesan":"Semoga lancar terus kuliahnya dan semoga sukses"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20 ",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakaknya baik, ramah, humble, keren",  
                "pesan":"Semoga selalu sehat dan bahagia selalu, serta lancar kuliahnya"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21 ",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Dafa ramah, keren, humble, baik",  
                "pesan":"Semoga selalu lancar kuliahnya dan semangat terus!"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20 ",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kak salsabila orangnya baik, ramah, humble, cantik",  
                "pesan":"Semoga lancar kuliahnya dan selalu bahagia ya kak"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19 ",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Bang Afdal orangnya baik, keren, ramah, humble",  
                "pesan":"Semoga selalu sehat dan semoga kuliahnya lancar ya bang"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19 ",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak juwita baik, cantikk, ramah, keren",  
                "pesan":"Semoga selalu ketemu lampu hijau tiap di perempatan"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21 ",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Baik sekali, ramah, humble, kerenn",  
                "pesan":"semangat terus kuliahnya kakak ! Semoga dipermudah segala urusannya."# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "bang Andra baik, ramah, kerenn, humble banget",  
                "pesan":"semoga kuliahnya lancar dan segala urusannya dipermudah"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20 ",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang Bryan keren, lucu, baik, ramah, humble",  
                "pesan":"semangat terus bang! Semoga menjadi kebanggan orangtua" 
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17 ",
                "asal":"Jati Asih",
                "alamat": "Korpri",
                "hobbi": "Nyawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Abangnya lucu, keren, baik, humble",  
                "pesan":"semangat terus bang, semoga selalu bahagia dan senang" 
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20 ",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakak nya baik, cantik, ramah",  
                "pesan":"semangat terus kuliahnya kakak dan semoga bahagia selalu kakak"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri ",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kakak nya baik, humble, kerenn",  
                "pesan":"semangat terus kakak semoga nasinya selalu hangat"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20 ",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Bang Rafka keren, baik, humble, ramah",  
                "pesan":"semangat terus, semoga selalu bahagia dan segala urusan diperlancar"# 1
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
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "23",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Merokok",
                "sosmed": "@haikalsbln_",
                "kesan": "Bang Haikal keren, baik, ramah, humble.",  
                "pesan":"Semoga selalu bahagia dan semoga amanah menjalani tugasnya"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak nya baik, manis, humble, ramah, lucuu",  
                "pesan":"semangat kuliahnya dan semoga selalu lancar"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak nya aktif, baik, lucu, ramah, manis sekalii",  
                "pesan":"selalu bahagia ya kak! semoga kuliahnya juga lancar terus"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan baik, ramah, humble, keren",  
                "pesan":"Semoga selalu bahagia dan lancar kuliahnya"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak Aisyah humble, cantik, lucu, manis",  
                "pesan":"Semoga selalu bahagia dan lancar kuliahnya"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "20 ",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cceluv3",
                "kesan": "Kak Cerine baik, ramah, cantik, manis, lucu banget",  
                "pesan":"Semoga lancar kuliahnya dan semoga nasinya selalu hangat"# 1
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya baik, keren, ramah, humble",  
                "pesan":"Semoga selalu disertai setiap langkah hidupnya sama Tuhan ya bang"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya baik, ramah, humble, cantik, manis",  
                "pesan":"Semoga selalu bahagia dan lancar kuliahnya"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpro Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Bang rozak keren, baik, ramah, humble",  
                "pesan":"semangat terus kuliahnya dan semoga selalu bahagia"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "masak",
                "sosmed": "@christiani8872",
                "kesan": "Kakak nya baik, ramah, humble, keren, cantik",  
                "pesan":"semangat terus kuliahnya kak, semoga selalu bahagia!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Bang Hanif baik, ramah, keren, humble",  
                "pesan":"semangat selalu semoga bahagia!"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kk audina baikk, ramah, lucu, cantik, manis",  
                "pesan":"semangat kuliahnya semoga sukses dan selalu bahagia kak"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kknya cantikkk, baik, ramah, humble, maniss",  
                "pesan":"semoga bahagia selalu dan sukses dalam kuliahnya!"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara ",
                "alamat": "airan",
                "hobbi": "nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakak nya baik, ramah, cantikk, manis",  
                "pesan":"semangat terus kuliahnya dan semoga selalu dalam lindungan Tuhan"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Abangnya baik, ramah, keren, humble",  
                "pesan":"selalu bahagia dan semoga segala urusannya dipermudah"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Kakaknya baik, ramah, cantik, manisss",  
                "pesan":"semangat kuliahnya dan semoga selalu bahagia ya kak"# 1
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
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal": "Pinggir Pantai",
                "alamat": "Samping Kost Capo",
                "hobbi": "Ngerjain Anak Kader",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arienta baik, ramah, humble, cantik, manis",  
                "pesan":"Semoga selalu semangat jalanin kuliahnya"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany lucu, baik, dan ramah",  
                "pesan":"Semoga selalu bahagia dan sukses dalam menjalani kuliahnya"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel baik, ramah, humble, keren",  
                "pesan":"Semoga selalu sehat dan sukses selalu"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi ramah, humble, baik",  
                "pesan":"Semoga selalu bahagia dan menjadi kebanggaan orang tua"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang Ayake ramah, baik, keren, humbleee",  
                "pesan":"Semoga selalu sehat dan sukses dalam menjalani kuliahnya"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar lucu, baik, ramah, keren",  
                "pesan":"Semoga kuliahnya lancar, menjalani kuliah dengan penuh semangat"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Euodia baik, ramah, humble, cantik, manis",  
                "pesan":"Semoga selalu dalam lindungan Tuhan dan semangat"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal baik, ramah, keren, humble",  
                "pesan":"Semoga selalu sehat dan bahagia dan dapat membanggakan orangtua"# 1
            },
            { 
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak putri baik, ramah, humble, cantikk, keren",
                "pesan": "Semoga selalu sehat dan semangat kak"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@andra.lhm",
                "kesan": "cantik banget, senyumnya juga maniss",
                "pesan": "semangat kuliahnya kak, semoga dipermudah"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Keren, humble, ramah, baikk",
                "pesan": "tetap semnangat jalanin hari-hari bang"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "kakanya lucu, cantik dan baik banget",
                "pesan": "Semangat kuliahnya dan tetap jaga kesehatan kak"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "kakanya cantik dan lucu",
                "pesan": "Tetap semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal": "Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "keren bang, humble dan baik",
                "pesan": "semoga kuliahnya lancar dan sehat selau"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal": "Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "kakanya baikk dan cantik banget",
                "pesan": "semoga selalu bahagia dan semangat "
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal": "Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "abangnya baik dan ramah",
                "pesan": "semangat kuliahnya bang, semoga bahagia"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                 "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "kakaknya baik dan manis sekalii",
                "pesan": "semangat kuliah dan ngejalanin hari-harinya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()


elif menu == "Departemen Senator":
    def DepartemenSenator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LkhFXq5faxyG3i9ou5XjLDUY0GGExhyB", #fathinah
            "https://drive.google.com/uc?export=view&id=1qFb53Ww3ITeCndvz6tbNRkgcqY4Fr0J3", #helmy
            "https://drive.google.com/uc?export=view&id=1I3H_8NM30uMJXNkUT7D-iZzAQ00YO7oG", #fernando
            "https://drive.google.com/uc?export=view&id=1obmFFiBk5TeWdpcrofOqpiHlqEEmWBmi", #suci
            "https://drive.google.com/uc?export=view&id=1UM4CUQ2sN4Vr9nJtluEpIjUnHCkB2wcl", #wielman
            "https://drive.google.com/uc?export=view&id=1MY-KWSITMo2qkCRVTWZ6S9C0-eTXzY35", #lia hana
            "https://drive.google.com/uc?export=view&id=1dM3Yok7EholztwlKWvWs3PEVlL_ohWwL", #aqila
            "https://drive.google.com/uc?export=view&id=1fcGHnnOeGb3bnLofA4k9xj3xdivdOuf4", #hazel
            "https://drive.google.com/uc?export=view&id=15WwSBsvhb3jkJuuoZ1Y2m6LG4rSW14ZM", #nadya
            "https://drive.google.com/uc?export=view&id=1ACXVRWxHMX4qSq4FTHeL5lX6Fw-tzpeO", #dwi rahma


        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta ",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak azizah keren banget, auranya sangat positif dan bikin semangat",
                "pesan": "Makasih kak atas penyampaian yang mudah diterima, Semangat kuliahnya kak!!"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "keren bang, baik juga",
                "pesan": "semangat terus kuliahnya, semoga lancar"# 1
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Nemenin Wielman MC",
                "sosmed": "@barus.fernando",
                "kesan": "Bang fernando keren, humble dan baik banget",
                "pesan": "Semangat selalu menjalani kuliahnya bang"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru ",
                "hobbi": "Baca",
                "sosmed": "@sciia__",
                "kesan": "ka suci orangnya baik dan ramah banget, asik juga",
                "pesan": "Semangat terus dan selalu jadi MC ya kak"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "jadi MC",
                "sosmed": "@wielhawn",
                "kesan": "keren sih bang, suaranya juga keren pas jadi mc",
                "pesan": "semangat menjadi mc dan semoga sukses"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "main hp",
                "sosmed": "@lia.h_264",
                "kesan": "Aku suka liat kakaknya karena keren gitu",
                "pesan": "Semangat kak kuliahnya, semoga dipermudah urusannya"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "identiknya aksesoris matahari itu",
                "pesan": "Semangat kak dan semoga selalu ceria"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "jadi sekjen",
                "sosmed": "@hazelhandhaka",
                "kesan": "keren bang, baik juga",
                "pesan": "Semangat  terus bang, semoga sukses!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya baik, cantik juga",
                "pesan": "semoga selalu bahagia ya kak"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani ",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang ",
                "alamat": "Jl. Lapas",
                "hobbi": "nonton film,musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "kakanya manis, cantik, dan baik sekalii",
                "pesan": "semangat terus kak, semoga sehat selalu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSenator()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1p3-mKp7TYnQcPZgvUw7rwUuicPtp4ex2", #arini
            "https://drive.google.com/uc?export=view&id=12-RgEJezEqBbF_aGb_2IxC0JaOMZcWXa", #nabyla
            "https://drive.google.com/uc?export=view&id=1wFudRQ94Nsnow1TMuZT30_6JyfmifidV", #aditya
            "https://drive.google.com/uc?export=view&id=1-jdn-VZyj4BlVuhkfz0yS0CMzYenpC6h", #Fathya
            "https://drive.google.com/uc?export=view&id=15dftUukXiB3sbz5Y-922YJNf0qjwYDtv", #tarisya
            "https://drive.google.com/uc?export=view&id=1XDdGyL4r-x1k1sWKOJnXU0K4Y5GndMIn", #selma 
            "https://drive.google.com/uc?export=view&id=1AwMllPnurpvdmQ-SnprWOTkQqeTFhIVS", #ashila
            "https://drive.google.com/uc?export=view&id=1AuGsn4NiLvLwiP1SwBTj3RXGajfwtBsE", #danil
            "https://drive.google.com/uc?export=view&id=1wIp3xHzdLEiCpMNVWPYCz6sZFcOg31_X", #favian
            "https://drive.google.com/uc?export=view&id=1g6EccFvoWj-6wAGZNtj-Old1MsfJWkkv", #yazid
            "https://drive.google.com/uc?export=view&id=1N60CeNzsKowz4ywk_r17MpjHLEQJuAxx", #rizaldi
            "https://drive.google.com/uc?export=view&id=1iuCLzE0UyNMQbogFD4Jllv3bNh7qNGCb", #saskia
            "https://drive.google.com/uc?export=view&id=1oZz0-Krt13N5Mmf50f6CbKoWO1a4aWmd", #khoirul
            "https://drive.google.com/uc?export=view&id=1V4m41jK9L3jFtlJjlxlHGQpCxqiVsTGr", #ahmad
            "https://drive.google.com/uc?export=view&id=1x_G_hC6cokeL_N3MJ6Loam6RkKRwRt8P", #indah
            "https://drive.google.com/uc?export=view&id=14NQ6xZOhbGPoyr7w9BYF6RGXv20oypHL", #bima
            "https://drive.google.com/uc?export=view&id=1t5aqMJNgGl7xVzr3ztjwYwLRSCwXScCB", #bimo
            "https://drive.google.com/uc?export=view&id=1VYBFk_9EhPgSaQaQ_Xi2lU0RZDWvLG_p", #adinda deswita
            "https://drive.google.com/uc?export=view&id=1vecgG7MH1SycGfvXCGZ5Gz8kvf5eCEB6", #yollanda
            "https://drive.google.com/uc?export=view&id=1PRDv6ipuO__SXkDPbuPGinyuGVFXWE2Y", #riska
            "https://drive.google.com/uc?export=view&id=1nBpAh6zKEEnlbd_538Hb_LIHFCTaSSQf", #alfaya
            "https://drive.google.com/uc?export=view&id=19Vsicis9gyM3aa5XaydBb0eYCkhXvwpe", #asri

        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "21",
                "asal": "LAMPUNG!!!",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "vibenya positif, keren juga",
                "pesan": "Semangat dan semoga lancar kuliahnya "# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya manis banget dan ramahh",
                "pesan": "selalu bahagia dan semangat kak"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "abangnya asik dan seruu",
                "pesan": "sehat-sehat bang, semoga selalu lancar kuliahnya"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "kak fathya lucu, imut, dan baik banget",
                "pesan": "semangat menjalani kuliahnya ya kak!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "-",
                "asal": "Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "tari_",
                "kesan": "kakanya baik, ramah jugaa",
                "pesan": "semangat terus semoga sukses"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "kakanya baik dan ramah sekalii",
                "pesan": "semangat kak, semoga selalu bahagia"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "sini",
                "alamat": "jauh pokoknya",
                "hobbi": "tidur",
                "sosmed": "@kshigf",
                "kesan": "kakanya lucu , baik, dan humble",
                "pesan": "Tetap semangat menjalani hari-hari kak"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "kerenn, baik, humble",
                "pesan": "semangat terus bang, semoga sukses"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "keren bang, asik dan humble banget",
                "pesan": "semoga selalu bahagia dan dipermudah kuliahnya"# 1
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "baikk dan ramah banget, keren bang",
                "pesan": "semangat terus bang, semoga bisa bahagiain ortu"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah ",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "ga balas chat",
                "sosmed": "@jaldii._",
                "kesan": "abangnya asikk banget dan sangat humble",
                "pesan": "semangat bang, selalu ceria ya bang"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "kakanya baik dan ramah ",
                "pesan": "semangat terus menjalani kuliah di itera kak"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kak muthoharoh lucu dan imut banget deh",
                "pesan": "semangat pimnasnya dan semoga menang kak"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "keren bang, vibenya positif",
                "pesan": "semoga selalu bahagia dan semangat bang"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "makasih kak atas banyak bantuannya",
                "pesan": "semoga selalu sehat, bahagia, dan kuliahnya lancar"# 1
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung ",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "abangnya baik dan keren",
                "pesan": "semangat bang semoga selalu bahagia"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus ",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "keren sih bang, baik juga",
                "pesan": "semoga rumah yang diincer bisa dibeli"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "21",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "kakanya cantik dan manis banget",
                "pesan": "Semoga selalu dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "21",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "nyari duit",
                "sosmed": "@yollanda_agustina16",
                "kesan": "baik dan humble banget, keren",
                "pesan": "Semoga selalu bahagia kak."
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "sangat imup dan lucu banget",
                "pesan": "makasih kak udah jadi mentor Tensor yang keren. semoga selalu bahagia dan maaf banyak ngerepotin kakak karena status akamsi ini... semoga sukses ya kak!!"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "keren bang, baik dan seru",
                "pesan": "Tetap semangat ngejalanin hari-harinya"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "kak mei baik, humble, ramah dan cantik banget",
                "pesan": "bahagia selalu ya, kanim! semoga selalu bahagia dan makasih atas kebaikannya, kak."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Bj1LaWxYaPPUiJV-2xaGGnyvsfcr2XkH", #fabio
            "https://drive.google.com/uc?export=view&id=1ym29mBpuCJre24AjKpars_pJDdXlnz2Z", #tanty
            "https://drive.google.com/uc?export=view&id=1Ve3YWvKq7AkxVuJO21GTSc6wUvfRsznq",#fadil prasetyo
            "https://drive.google.com/uc?export=view&id=1VI_cUNyTsYkIEFEju8rsYTnswzm-fn-j", #manuel
            "https://drive.google.com/uc?export=view&id=1rKtR60kIyDMv0GhXMz_C6W4DpolYt1Np",#ni made
            "https://drive.google.com/uc?export=view&id=1_10mQxwlnk0bu58N-lNWzZS2U0x5TmPR", #risa
            "https://drive.google.com/uc?export=view&id=1FwJjp6Uh8_RhFVUhrAG9Gyyx-TNpIy9v",#vanissa
            "https://drive.google.com/uc?export=view&id=11J61azImHr0DFEGeiY8uWW3SCef-Hg3-",#yulia
            "https://drive.google.com/uc?export=view&id=1_hCwKNd_F4yjdcykrAVhWuvMUb6ooePc",#akeyla
            "https://drive.google.com/uc?export=view&id=1w-PvqUAD_aWIoJgYRl0TN06_xYLYRoUd",#elsa
            "https://drive.google.com/uc?export=view&id=1itsOlZa2kxbSb43kuFxpJgXmi3Aoksx_",#fadya
            "https://drive.google.com/uc?export=view&id=1kmxWVgMle4dn3v_QQzKnfMplI2qVBz0R",#lovia
            "https://drive.google.com/uc?export=view&id=1hbFSMpNgx7DvXXmpvW-Ay8CWfmYQaVy3",#alsi
            "https://drive.google.com/uc?export=view&id=1wmrYk4_83RnCnU9S_4BzN-m6HH-Sx62_",#sherena
            "https://drive.google.com/uc?export=view&id=1gY724rsjdF0XEgPJ_fpx1SLkaBIKaki3",#razin
            "https://drive.google.com/uc?export=view&id=1x6irYFPOT82w5wB701kTmCv-U1RXsVH4",#Faiza
            "https://drive.google.com/uc?export=view&id=15qRbEPJc-ur5JW8XD8ZjwzAw1IwAr2ZI",#gathfan
            "https://drive.google.com/uc?export=view&id=1_68s6DfJGX_nq0Wuzp7CRwGUC8sn0qrg",#hafidz
            "https://drive.google.com/uc?export=view&id=1ilJai38jeoyz_JfS6ioS5ErItRdyXKiR",#kaleb
            "https://drive.google.com/uc?export=view&id=1U1ocMfHYOhajoJ8EYVv6HEhv8YTtLDUt",#melva
            "https://drive.google.com/uc?export=view&id=1lbpPGZZSGzV1o36cdro_ycsuPl4fhqE6",#syafiqul
            "https://drive.google.com/uc?export=view&id=1qScw1OlEByW4JtA2nyoHzxLrXOApf3XP", #henry

        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton Bandar Lampung ",
                "hobbi": "Gangguin bang keya",
                "sosmed": "@biyokcb",
                "kesan": "keren dan menginspirasi",
                "pesan": "semangat bang dan semoga selalu bahagia"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Nonton film",
                "sosmed": "@tvnty_",
                "kesan": "baik dan ramah banget, keren dan ceria banget",
                "pesan": "Semoga energi positif dan semangatnya menular "# 1
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "orangnya baik dan keren",
                "pesan": "semoga diberikan tempat terbaik di sisi-Nya"# 1
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis ",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "humble dan ramah banget, asik juga",
                "pesan": "semangat terus bang, makasih banyak udah ngebimbing kami anak psd ini... semoga saya bisa join juga ya"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12",
                "asal": "Bali",
                "alamat": "nusa peninda",
                "hobbi": "menghayal",
                "sosmed": "@violaadrtr_",
                "kesan": "baik dan cantik banget",
                "pesan": "Semoga selalu bahagia dan semangat"# 1
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "ka risa baik dan mengayomi, cantik dan keren jugaa",
                "pesan": "terimakasih atas ilmunya kak, semoga selalu semangat jalanin kuliahnya"# 1
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "1244500078",
                "umur": "19",
                "asal": "kepulauan riau",
                "alamat": "teluk betung",
                "hobbi": "nonton khw",
                "sosmed": "@vunnycaa",
                "kesan": "baik dan keren banger, manis jugaa",
                "pesan": "selalu bahagia dan semangat kuliahnya kak"# 1
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "lucuu, cantik, dan baik hati",
                "pesan": "Semoga kuliahnya lancar ya kak"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@keyashafi_",
                "kesan": "keren bang dan asik",
                "pesan": "Tetap semangat bang kuliahnya"# 1
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara ",
                "alamat": "Pemda",
                "hobbi": "Sibuk",
                "sosmed": "@_els.a",
                "kesan": "baik dan humble banget, asik juga",
                "pesan": "Semoga selalu sehat dan bahagia kak. GBU!"# 1
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "airan",
                "hobbi": "mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "kakaknya baik dan ramah banget",
                "pesan": "selalu semangat kuliahnya" # 1
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "keren dan sangat aktif",
                "pesan": "Semoga selalu bahagia dan semangat kak"# 1
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "kalianda",
                "alamat": "kota baru",
                "hobbi": "main game, tidur",
                "sosmed": "@aluccy_",
                "kesan": "keren bang, asik dan baik",
                "pesan": "semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal":"Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "mirip sama sepupuku banget, sangat lucu",
                "pesan": "Semangat kak kuliahnya, semoga sehat terus"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "keren bang, baik juga",
                "pesan": "Tetap semangat bang"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel ",
                "sosmed": "@faizaanjanii",
                "kesan": "kakaknya baik dan lucu sekali",
                "pesan": "semangat terus kak, semoga bahagia"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Rajabasa Raya",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "keren sih bang, humble juga",
                "pesan": "Tetap semangat bang, semoga sehat selalu"
            },
{
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur ",
                "hobbi": "3N ( Ngoding , Ngegame, Nyibukin Diri)",
                "sosmed": "@apiszzaja",
                "kesan": "baik, humble, dan lucu",
                "pesan": "semoga jalannya dipermudah"# 1
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Campang Raya, Sukabumi",
                "hobbi": "Gym, membaca, dan bermain",
                "sosmed": "@kelelep_comberan",
                "kesan": "keren bang, humble juga",
                "pesan": "sangat menginspirasi, semoga selalu bahagia"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal":"Sumatera Selatan ",
                "alamat": "Sukarame ",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "baik dan ramah banget, cantik jugaa",
                "pesan": "semangat terus ya kak..."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syafiqui",
                "kesan": "baik dan keren",
                "pesan": "semoga selalu bahagia dan semangat"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal":"Kotabumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "keren dan ramah",
                "pesan": "semangat bang, semoga lancar kuliahnya"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PLNIvD3bHSoPHQjEhwkvmF6rAA75-PEj",#ihsan
            "https://drive.google.com/uc?export=view&id=17c3wMe_0tWsMzQxRaSsnc_8uEg5UyQ7R",#hanifah
            "https://drive.google.com/uc?export=view&id=15Cl7P0n7NlUWogRRD97v36mrcUd_KgVt",#afifah
            "https://drive.google.com/uc?export=view&id=1YUHx0iqvaNb1Xdp5XZaTRUQ7oEIYu7AN",#hasan
            "https://drive.google.com/uc?export=view&id=1lwGNqT9m2Bj39WG_JDWFJeDBInRcFrU0",#layina
            "https://drive.google.com/uc?export=view&id=14ICkyw_G6dtTxc_VHtYPekw9-aMfEr0D",#moch
            "https://drive.google.com/uc?export=view&id=1WGNlkq2rnMOOPwq9p98o6hp670EN6hU8",#talitha
            "https://drive.google.com/uc?export=view&id=1YCB1Lc6Ex2icoXv2LJ8GkDlcPglG1uq0",#anadia
            "https://drive.google.com/uc?export=view&id=18ykExF-NYQmY8MS83rDw9n47nIA4tzUF",#Abdilah
            "https://drive.google.com/uc?export=view&id=1RePfFmpnNkhGhbnZTG3q7K1NFPeWKkE9",#Afdhal
            "https://drive.google.com/uc?export=view&id=1va7Wa40WU-3rEqA9o4-LfcHmYlNYliHQ",#anggun
            "https://drive.google.com/uc?export=view&id=1V3OiwMibRW2caTWAUVvLHU9dAfng4wIV",#dela



        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Jualan",
                "sosmed": "@ihsan.myusuf",
                "kesan": "keren sih bang, vibenya  positif gitu",
                "pesan": "Semoga selalu amanah dan semangat"# 1
            },
            {
                "nama": "hanifah inaya sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "lucu dan baik banget",
                "pesan": "Semangat kuliahnya, semoga lancar kak"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "keren dan gacor banget",
                "pesan": "Ssemangat terus dan semoga bahagia kak"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "keren sih bang, baik juga",
                "pesan": "Semoga selalu lancar kuliahnya"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin",
                "sosmed": "@lay.inr_",
                "kesan": "keren kak, humble, dan baik",
                "pesan": "Semangat terus semoga bahagia"# 1
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "baik dan humble sekali",
                "pesan": "Semoga selalu bahagia dan semangat"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "@talljtine_",
                "kesan": "baik dan ramah banget",
                "pesan": "semangat terus kak, semoga sukses"# 1
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "cantik dan baik hati sekali",
                "pesan": "Semoga selalu sehat dan bahagia kak"# 1
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "baik dan ramah banget",
                "pesan": "Semoga dipermudah segala urusannya"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "keren bang dan gacor",
                "pesan": "Semoga selalu bahagia dan semangat terus kuliahnya"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "kakaknya baik dan ramah banget",
                "pesan": "Semangat terus dan semoga lancar kuliahnya"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "kakanya cantik dan lucu",
                "pesan": "Semangat kak menjalani kehidupan ini"# 1
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bttJKp1kbc6IpcHQhMcjmlkezdv6Jgnr",#nayla
            "https://drive.google.com/uc?export=view&id=1ESeOxlaRsvumWz9qv1_UFWCNazvY3x2A",#dona
            "https://drive.google.com/uc?export=view&id=1RPA6CWOutDmvdbsIBw7kPLipOyoGa1bd",#labo
            "https://drive.google.com/uc?export=view&id=1b184PLu07d-i60sfRVVRjVtdm3HNibsg",#anash
            "https://drive.google.com/uc?export=view&id=1Ft_xpYGr30axvtFO9ybQrWh6nHYj8ckP",#felisya
            "https://drive.google.com/uc?export=view&id=1d9oYDVgmR1OjPovzN4UTQXGOMj5-RTuj",#m razan
            "https://drive.google.com/uc?export=view&id=1m3BjwNRUDPn_PXZVF1eIm_y8i7CQ98wE",#sania
            "https://drive.google.com/uc?export=view&id=1PJBUiOef93Yvxx1aZGUcL6m_W28A5D3x",#allisha
            "https://drive.google.com/uc?export=view&id=1Drxv5MXZFtrfJMJrhZBDZUTKSJWgjQI5",#alya
            "https://drive.google.com/uc?export=view&id=1dAQEasxqwJoIAaN5tqfkA9p5mR0EWi92",#bunga
            "https://drive.google.com/uc?export=view&id=1J473LXQAYu109oMrkmcVnwdk5Rlh59Ft",#difanya
            "https://drive.google.com/uc?export=view&id=1kMJad3E2KzzcQuc8a-aaHGiQgAVnHNbP",#nazlah
            "https://drive.google.com/uc?export=view&id=1qhORoSSn6bCcO4xfReILCDBFaLGeINHl",#raihana
            "https://drive.google.com/uc?export=view&id=1-3vnmbA4tyKB0aHlhWlEWMLpfM9UiOZj",#dafa
            "https://drive.google.com/uc?export=view&id=1MYUg2LP1R-G-qrIOYOYxWLqyhFxGlX_A",#edsel
            "https://drive.google.com/uc?export=view&id=1tjUkd2RWJupqCbEZIuWNs8yrcirwVSJ2",#lucia
            "https://drive.google.com/uc?export=view&id=1mW9y9ia1ZLvtIcHbnk9tMqMFbqZAiLlB",#shafa
            "https://drive.google.com/uc?export=view&id=1vfMhoP7eek4EQ06bITZ_AEcPv8nKvp0V",#zanuba

        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi, Jati Agung, Lampung Selatan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "baik dan ramah banget, auranya positif",
                "pesan": "semangat ya kak jalanin kuliah dan tanggungjawabnya"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "keren dan baik hati banget",
                "pesan": "makasih ya ka udah jadi penutor yang keren dan baik"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran ",
                "sosmed": "@noerruuu",
                "kesan": "sangat keren dan baik",
                "pesan": "semangat terus jalanin kuliahnya bang"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Way Halim ",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "kakanya cantik dan manis",
                "pesan": "semangat terus kak, semoga bahagia"
            },
            {
                "nama": "Felisya Nabila Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal": "Lampung Timur ",
                "alamat": "Kota Baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "kakaknya baik dan ramah bangett",
                "pesan": "semangat ya kak kuliahnya..."# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "21",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "baik dan keren sih, humble juga",
                "pesan": "semoga selalu ceria dan semangat terus"# 1
            },
            {
                "nama": "Sania DWi Ayu Lestari",
                "nim": "124450086",
                "umur": "21",
                "asal": "Karawang ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "kakaknya baik dan keren sih",
                "pesan": "semoga lancar kuliahnya ya kak"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "keren namanya cuman satu",
                "pesan": "semangat terus ya kak, selalu jaga kesehatan"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "kakanyaknya baik dan ramah sekali",
                "pesan": "Semoga selalu bahagia dan dipermudah segala urusannya"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "keren dan baik banget sih",
                "pesan": "Semoga selalu semangat dan sehat selalu kak"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Alquran",
                "sosmed": "@difanyhsa_",
                "kesan": "baikk dan ramah sih kak, manis juga",
                "pesan": "semoga kulliahnya dipermudah dan semangat kak"# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@nzlhauly_",
                "kesan": "kakaknya lucu dan ramah sekali",
                "pesan": "Semoga nasinya selalu hangat"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Aira Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "kakaknya baik dan keren, manis juga",
                "pesan": "semangat terus ya kak!"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame ",
                "hobbi": "-",
                "sosmed": "@daffascript",
                "kesan": "kayak lucu gitu",
                "pesan":"semoga selalu lucu dan semangat bang"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "keren bang, baik juga",
                "pesan": "apapun yang lagi dijalani, semoga diberi kekuatan"# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "kakaknya baik dan lucu banget",
                "pesan": "Semoga dipermudah segala urusan dan GBU!"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis dan menulis",
                "sosmed": "@_shaazzh",
                "kesan": "kakaknya ramah dan kerenn",
                "pesan": "Semoga selalu bahagia dan semangat kak"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "kakaknya baik dan ramah, keren juga",
                "pesan": "Semoga selalu bahagia dan semangat terus ya kak"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
# Tambahkan menu lainnya sesuai kebutuhan

