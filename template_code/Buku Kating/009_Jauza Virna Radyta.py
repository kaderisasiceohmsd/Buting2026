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
            "https://drive.google.com/uc?export=view&id=1xVOIyVcEWA9aIu_rhjmMrtG54l6VKKph", 
            "https://drive.google.com/uc?export=view&id=1TyG2J2lHVCUhmFKcuSOC8i6mSs4QANUr",
            "https://drive.google.com/uc?export=view&id=1eQ3MZJScvHPLMUXEfYwGKXxviL9aplOr",
            "https://drive.google.com/uc?export=view&id=1kbc6pWhzoTIVEmQy9Hln_BuNe8hpVo2s",
            "https://drive.google.com/uc?export=view&id=1_nm-21LBwwNcaFOavgXokGcj1ryhstWK",
            "https://drive.google.com/uc?export=view&id=1EV5SMSozsmYDhoa-PCojVgu3nH4jyhUM",
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
                "kesan": "Bang Fajar keren, tegas, dan juga baik sekalii",  
                "pesan":"Semoga semua keinginan bang fajar cepat terwujud"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil asikk benerr, dan juga keren apalagi pas basket",  
                "pesan":"Semoga bang aqil bisa dapetin yang bang aqil inginkan"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi keren sekali, sangat baikk dan ramah sekalii",  
                "pesan":"Semoga cepat mendapatkan apa yang kak efi inginkan"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois kerenn, sangat humble, dan juga baikk",  
                "pesan":"Semoga bang qois selalu dapet hal-hal baik"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa kerenn, baik jugaa, dan sangat ramahh",  
                "pesan":"Semoga kak hafsa selalu mendapatkan apa yang kak hafsa mau"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak luthfi sangat lucuu, baikk, dan juga ramah",  
                "pesan":"Semoga kak luthfi selalu mendapatkan semua yang hal yang diinginkan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BX8BNHfcyTHiKq_zK-RRLuhx4RJEi5H5",
            "https://drive.google.com/uc?export=view&id=1hnEDNm0H0jP-Kdqs5Md39FQyP90k9NG4",
            "https://drive.google.com/uc?export=view&id=1v5v4oEq29VnWv5GARTEHhWvyHDLIFlCd",
            "https://drive.google.com/uc?export=view&id=1O6ts_ok5mJdBHpTjc-t0I1DE99znRTuG",
            "https://drive.google.com/uc?export=view&id=1VAIQ1RkK5PPl3SWpb2UMwaqYnGUiPk5n",
            "https://drive.google.com/uc?export=view&id=1tX4ynAeCTr0TNwP8t1yXVMw7X8lAz6UV",
            "https://drive.google.com/uc?export=view&id=1-T9rxSCfRayBJbUVW14UPW7nIlR8x8S2",
            "https://drive.google.com/uc?export=view&id=1KwYUzTWb9KFzlN3jmJE-RY6d1nLglZrx",
            "https://drive.google.com/uc?export=view&id=1cAaiTd02s7SulDyp9e-O_sHxOlHIdflx",
            "https://drive.google.com/uc?export=view&id=10bNbwhUIH_CNPOxbRjPyaCr1reKRJevf",
            "https://drive.google.com/uc?export=view&id=1S5pukEDCihA6CQS0cAvu8VeaRxEpkDrR",
            "https://drive.google.com/uc?export=view&id=1TcNu2NTawMrtSagNW4CTpadDOooHSV7U",
            "https://drive.google.com/uc?export=view&id=1aU0xjMdjGW92Qwlrn_NhrrZJxMC0W2xT",

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
                "kesan": "Bang Ridho cool sangat lh, dan juga baikk",  
                "pesan":"Semoga bang ridho selalu didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Juesi lucuu, humble, dan baik",  
                "pesan":"Semoga kak juesi cepat mendapatkan hal yang diinginkan"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Bang Dharu asikk, baik, dan juga sangat ramah",  
                "pesan":"Semoga bang dharu selalu didekatkan hal-hal baik"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Mikael sangat kerenn, dan juga baikk apalagi pas pplk",  
                "pesan":"Semoga semua keingininan bang mikael segera terkabulkan"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kak Siti lucuu, baik, dan juga sangat ramah",  
                "pesan":"Semoga kak siti selalu mendapatkan hal-hal yang diingingkan"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Giovaro keren sihh, dan juga baikk",  
                "pesan":"Semoga apa yang bang gio semogakan cepat terkabulkan"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak afghanis sangat manis, baik jugaa, dan juga ramahh",  
                "pesan":"Semoga semua keinginan kak afghanis cepat terkabulkan"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kak Hani lucuu, ramah juga, dan tidak lupa dengan baiknyaa",  
                "pesan":"Semoga kak habi selalu didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremi keren sih, suaranya baguss, dan juga baikk",  
                "pesan":"Semoga semua keinginan bang jere cepat terkabul"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica sangat baik, lucuu, dan juga ramahh",  
                "pesan":"Semoga kak monica cepat mendapatkan apa yang kak monica inginkan"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jona sangat amat kocak, dan baikk",  
                "pesan":"Semoga bang jona selalu mendapatkan semua yang hal yang diinginkan"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Sekar sangat baikk, dan juga maniss",  
                "pesan":"Semoga kak sekar didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kak Nashwa sangat asik, baikk, dan ramah jugaa",  
                "pesan":"Semoga semua keinginan kak nashwa cepat terkabul"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mq7zSb_-Rcd6WrGIpjXA5XtEXCrKyMef", 
            "https://drive.google.com/uc?export=view&id=16-18WEmdA5b5e7RnUVH8U-pgnqmPKGDV",
            "https://drive.google.com/uc?export=view&id=1gfAldKEpplPXtYC7KT1i5dteSgabhlwv",
            "https://drive.google.com/uc?export=view&id=1mq-BN2vWE4i2siPXkbgnejBckxU4LoMh",
            "https://drive.google.com/uc?export=view&id=1Kh5Gxz1qM68tpxXOwBMK18k8Jm0TYIxt",
            "https://drive.google.com/uc?export=view&id=1KeSOw5FJeXfdz3lJemQ0Eh3zeZLAPsyR", #kak salsabila
            "https://drive.google.com/uc?export=view&id=1DpPmQ89CFSOhqpDTu1k-akEubVW7ACn4",
            "https://drive.google.com/uc?export=view&id=19tRYQyOWC0EibBNbmsvUfHu5uWKAWELQ", #kak juwita
            "https://drive.google.com/uc?export=view&id=1YnE0mw6F-vVFzD-AT97axqX0v3KmAsb8", #bang ridwan
            "https://drive.google.com/uc?export=view&id=1NYDTtQwnjd5ntrqY_kzxahMLTalU0lzp", #bang andra
            "https://drive.google.com/uc?export=view&id=1QaslTCYxCADzGoYe-l98cJ7l820Qu0gC", #bang bryan
            "https://drive.google.com/uc?export=view&id=1i7unJhu3zrtE_lu23ZHnJAmkoe7oYf01", #kak indah
            "https://drive.google.com/uc?export=view&id=1dg3fGlKxHLtvd8xjRGfjxjBTVH7rEsez", #kak jacinda
            "https://drive.google.com/uc?export=view&id=1ovSnuwctxlxs5O0CVskCiaw9s4V9Rlpc", #bang rafka
            "https://drive.google.com/uc?export=view&id=1zeWR78XroFiBG66j9b-5p_ALyyM31-_-", #bang ghiyats


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
                "kesan": "Bang Kevin sangat amat cool, dan juga baik",  
                "pesan":"Semoga bang kevin mendapatkan apa yang bang kevin inginkan"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kak Gusti sangat asikkk, dan juga baik sekali",  
                "pesan":"Semoga kak Gusti sealalu didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Bang Ali sangat keren, dan juga baik",  
                "pesan":"Semoga semua keinginan bang ali cepat terwujud"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kak Ayu sangatt baikk, dan juga sangat amat ramahhhh",  
                "pesan":"Semoga semua yang kak ayu mau cepat kak ayu dapat"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Dafa keren, baik apalagi saat mengasprak",  
                "pesan":"Semoga bang dafa selalu mendapatkan apa yang bang dafa mau"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kak Salsabila lucuu, baikk, dan ramahh",  
                "pesan":"Semoga kak salsa didekatkan dengan hal-hal baikk"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Bang Afdal kocak sangat lah, baik jugaa",  
                "pesan":"Semoga kedepannya bang afdal selalu mendapatkan apa yang diinginkan"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak Juwita sangat baikk dan juga ramah",  
                "pesan":"Semoga semua keinginan kak juwita cepat terwujud"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang Ridwan asik sih orangnya, baik, dan ramah jugaa",  
                "pesan":"Semoga bang ridwan didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Bang Andra baikkk sekalii, dan juga kerennn",  
                "pesan":"Semoga bang andra mendapatkan semua keinginan bang andra"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang Bryan sangat kocak, dan juga baikkk",  
                "pesan":"Semoga bang bryan selalu didekatkan dengan hal-hal yang baik"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Indah sangat baikk, dan juga ramah sangatt",  
                "pesan":"Semoga kak indah mendapatkan semua yang diinginkan"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri ",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kak Jacinda lucuu, dan juga baikkk",
                "pesan": "Semoga kak jacinda selalu mendapatkan apa yang kakak inginkan"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Bang Rafka keren, baikk, dan juga ramahh",  
                "pesan":"Semoga semua keinginan bang rafka cepat terwujud"# 1
            }
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal":"Surabaya ",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Bang ghiyats keree, asikk, dan baik sihh",
                "pesan": "Semoga apa yang bang ghiyats inginkan cepat tercapai"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tRs700cUp_ltIVDvFe8JK2h1DPQU9s-L",#bang haikal
            "https://drive.google.com/uc?export=view&id=1S_CUhSQPLbq1EYBwLWZBqVGSCWMS7-Sf",#kak kharisma
            "https://drive.google.com/uc?export=view&id=1KBmKm1uS8nZKyGHn1PkTWcpteHyYr8FV",#kak hanna
            "https://drive.google.com/uc?export=view&id=1qxxSzBalqydJCGw0VZVHuOLhNrNUKpXP",#bang farhan
            "https://drive.google.com/uc?export=view&id=1Vve_ylKSy5ilrRP3gvUEa0pn1sgqNvDq",#kak aisya
            "https://drive.google.com/uc?export=view&id=1L-PF2EgVIYCrgLAeEfVWWYJiHOsVZ2k4",#kak cerine
            "https://drive.google.com/uc?export=view&id=1GcHgRYXdW5zVM5G29xbVDtYl2fQwteCu",#bang jaya
            "https://drive.google.com/uc?export=view&id=1I0DTA9qqcYAnD6YxbDk7zRLxOrbm18FJ",#kak najla
            "https://drive.google.com/uc?export=view&id=1119djuVLsanaWw_IDWJBoEP0pTT6TUeO",#bang rozak
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#kak teresa
            "https://drive.google.com/uc?export=view&id=1Lpn4uABtN9Cxqy-1jieIX48CwC-clU0d",#bang hanif
            "https://drive.google.com/uc?export=view&id=1ouP6BhvGNwUVxPyKyuFFBGLq9VkpQsqX",#kak audina
            "https://drive.google.com/uc?export=view&id=1WaPxkjJLi5CXvxIDFc9ivz1LRj8tMEWP",#kak cika
            "https://drive.google.com/uc?export=view&id=16SOCLG7UNAG55v3Z2nMD_KPAnDUCYLb1",#kak gustin
            "https://drive.google.com/uc?export=view&id=1b0iLMiiR7vYuojjbJvLGxoHIeRkJOBPm",#bang harvin
            "https://drive.google.com/uc?export=view&id=1zzNqM64Q_vOLiVZYy-BnmqFjC1HLGrTg",#kak sabina

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
                "kesan": "Bang Haikal kerennn, enak di ajak bercerita, dan juga baikk",  
                "pesan":"Semoga bang haikal selalu bisa mendapatkan hal-hal yang abang inginkan"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma lucuu, baikk, dan juga ramah",  
                "pesan":"Semoga kak kharisma selalu dikelilingi hal-hal baik"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna seru sihhh, baikk, lucu jugaa",  
                "pesan":"Semoga semua yang kak hanna inginkan semuanyaa tercapaii"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan keren, selalu kece pas damaskus",  
                "pesan":"Semoga bang farhan selalu mendapatkan keinginan abang"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak Aisyah lucuuu, dan juga asikkk sekali",  
                "pesan":"Semoga semua keinginan kak aisyah cepat terwujud"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kak Cerine sangat asikk, humble, dan juga baikk",  
                "pesan":"Semoga kak cerine selalu dikelilingi hal-hal baikk"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya keren, baikk juga, dan asikk",  
                "pesan":"Semoga bang jaya mencapai semua keinginannya secepatnya"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kak Najla sangat baikk, dan juga ramah sekalii",  
                "pesan":"Semoga semua keinginan kak najla tercapi secepatnya"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"lampung selatan",
                "alamat": "korpri raya",
                "hobbi": "isengin harvin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "Bang Rozak asik sihh, dan juga senyumnya lebarr sukaa",  
                "pesan":"Semoga bang rozak didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"riau",
                "alamat": "belwis",
                "hobbi": "masak",
                "sosmed": "@christiani8872",
                "kesan": "Kak Teresa lucuu, baikk, dan juga ramahh",  
                "pesan":"Semoga kak teresa segera mendapatkan semua keinginannya"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Bang Hanif baikk, dan juga asikk, eh ramah jugaa",  
                "pesan":"Semoga bang hanif selalu menjadi yang terbaik"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"sumbar",
                "alamat": "sukarame",
                "hobbi": "main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kak Audina lucuu, baikk, dan juga sangat amat ramah",  
                "pesan":"Semoga kak audin selalu dilingkung yang memiliki hal-hal baik"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kak Cika lucuu, baikk, dan juga asikk",  
                "pesan":"Semoga semua keinginan kak cika tercapai secepatnyaaa"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara ",
                "alamat": "airan",
                "hobbi": "nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kak Gustin lucuu, baikk, dan juga ramahh",  
                "pesan":"Semoga kak gustin selalu didekat hal-hal baik"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Bang Harvin baiikk sihh, tapi sedikit pendiam",  
                "pesan":"Semoga semua keinginan bang harvin tercapai secepatnyaa"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "nginep di rumah kak yollanda",
                "sosmed": "@snasha._",
                "kesan": "Kak Sabina baikk, dan juga sangat ramahh",  
                "pesan":"Semoga kak sabina mendapatkan hal-hal baik teruss"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hmnOgiekX0BJuYnBc_7RB2sKiSg-w_Vp",
            "https://drive.google.com/uc?export=view&id=10pxW5IyZ1vxYOxefR7vQU2h7k_-Nn7Sc",
            "https://drive.google.com/uc?export=view&id=1R7Gt5PV3o5Vsh6kpM_0xvmrh36w0NjFx",
            "https://drive.google.com/uc?export=view&id=1w_p7KU_YNdHC0cWUvX9zkh3YAe0uPL3N",
            "https://drive.google.com/uc?export=view&id=1b-poQcRRVmRPitoT5Anvr1vNUReqYKY8",
            "https://drive.google.com/uc?export=view&id=1apj1fn8lmeHxjE_wYdZmkwrPXdAMYiwL",
            "https://drive.google.com/uc?export=view&id=1CgNfVVMX-S9a9iyS-YGYc361fDWUnM32",
            "https://drive.google.com/uc?export=view&id=1t67HOceUW6iH-s_W49NghbTSbI3ZoaEI",
            "https://drive.google.com/uc?export=view&id=1zyu2FvIjlcfPnAVQNf534vpbXE9XhfHr",
            "https://drive.google.com/uc?export=view&id=1yT6Pge6Amnc4QJgOqKPOM8AJGzzmum9Z",
            "https://drive.google.com/uc?export=view&id=1DxdQa1dF-qqxZxiQTEBfgQ8qycHk8BzO",
            "https://drive.google.com/uc?export=view&id=1ImbjAOzVb7oatJyiC_1H-JwMRHu8Y3Ij",
            "https://drive.google.com/uc?export=view&id=1IOIoxVZzr8Wxy3wgtD3Cug-0VmD2dHTx",
            "https://drive.google.com/uc?export=view&id=17-ar6qtPoFKNLWwIQqy9Xmzp9vrOpR6L",
            "https://drive.google.com/uc?export=view&id=1AEyDhbizmv0sRJ5fdqFv-Bbr_P05GFDk",
            "https://drive.google.com/uc?export=view&id=1Nbb8WGasyTbIpMWO0OQMu34OxUbSfXuF",
            "https://drive.google.com/uc?export=view&id=1FQ6Q9msLLdfcUjUFFImAytsqTwQaHrXF",

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
                "kesan": "Kak Arienta lucuu, dan juga ramahh",  
                "pesan":"Semoga semua keinginan kak arienta tercapai"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany maniss, dan baik juga",  
                "pesan":"Semoga kak vany mencapai semua keinginannya secepatnya"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel kerenn, dan juga baiik",  
                "pesan":"Semoga bang nobel selalu didekat hal-hal baik"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi kerenn, dan juga baikk",  
                "pesan":"Semoga semua keinginan bang azmi tercapaii"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang Ayake lucuu, kerenn, dan juga baikk",  
                "pesan":"Semoga bang ayake bisa mencapai semua keinginan bang ayake"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar kereen, dan baikk",  
                "pesan":"Semoga bang caesar segera mencapai semua keinginannya"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Euodia maniss, dan juga baikk, lucu juga sihh",  
                "pesan":"Semoga kak euodia selalu didekat hal-hal baikk"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal kerenn, baikk, dan juga ramahh",  
                "pesan":"Semoga bang haikal mencapai semua hal yang bang haikal inginkan"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450029",
                "umur": "18",
                "asal": "Depok",
                "alamat": "Oiya Cefa",
                "hobbi": "Jalan kaki gaboleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri lucuu, baikk, dan juga ramah",  
                "pesan":"Semoga semua keinginan kak putri segera terwujud"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@quenntanaabilaa",
                "kesan": "Kak Queenta maniss, lucuu, dan juga baikk",  
                "pesan":"Semoga kak queenta selalu bisa mencapai keinginannya"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "23",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman kerenn, dan juga asikk, baikk",  
                "pesan":"Semoga bang desman selalu didekat hal-hal baikk"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel maniss, dan juga baikkk sekali",  
                "pesan":"Semoga semua keinginan kak azzel tercapai"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah baikk, dan juga ramah",  
                "pesan":"Semoga kak charlindah dikelilingi hal-hal baik"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jeremi kerenn apalagi saat damaskus",  
                "pesan":"Semoga bang jeremi bisa menggapai semua keinginannya"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila maniss, dan juga baik, ramah jugaa",  
                "pesan":"Semoga kak nabila mendapatkan hal-hal yang diinginkan"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearrfkvmfl",
                "kesan": "Bang Rafli manis, baik, dan juga ramah",  
                "pesan":"Semoga bang rafli selalu bisa mencapai semua keinginannya"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salavi lucuu, dan juga baik, ramahh",  
                "pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

elif menu == "Departemen Senator":
    def DepartemenSenator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ljbNOGEtWybfbmUyvn-1YRhkObjszF64",#kak fathinah
            "https://drive.google.com/uc?export=view&id=1ZxXRd1pCp693lgl5qrcMfR1mn-FdaSRk",#bang helmy
            "https://drive.google.com/uc?export=view&id=1Kz7JWTHfpIOeCNt44C0GbOG2S3e6bGKa",#bang fernando
            "https://drive.google.com/uc?export=view&id=16clY_NiOpZXWHtJyij7PBGHn-DV-O6Ic",#kak suci
            "https://drive.google.com/uc?export=view&id=1s4f1LAjtHd4L-s_-0GqbQDa8YZOESJon",#bang wielman
            "https://drive.google.com/uc?export=view&id=1P0jYpsJJFmvJvk0C1WjUQ9IqFHNWix8B",#kak lia
            "https://drive.google.com/uc?export=view&id=15PIKm0EX-6AAPb4uNdKUleZ7ACeo6pGa",#kak aqila
            "https://drive.google.com/uc?export=view&id=17PWyL5w09jSExl9RDltZOJpLRC8jY5Zs",#bang hazel
            "https://drive.google.com/uc?export=view&id=1lxjzvP5gQcINfAHcAofuTv1M89NDDkkF",#kak nadya
            "https://drive.google.com/uc?export=view&id=15eT8YT8xMH_6iwidB-sNzMRCgu-LtCnH",#kak dwi

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
                "kesan": "Kak Fathinah seruuu, ketemu pas kelas KDP baik sangat lahh",
                "pesan": "Semoga kak fathinah segera mendapatkan apa yang kak fathinah inginkan"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Bang Helmy asikk, pas ngeasprak enak sih selalu memberikan hal baru",
                "pesan": "Semoga semua hal yang bang helmy inginkan cepat tercapai"# 1
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Nemenin Wielman MC",
                "sosmed": "@barus.fernando",
                "kesan": "Bang fernando keren, asik sih pas pertama kali lihat",
                "pesan": "Semoga bang nando selalu didekat hal-hal baikk"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru ",
                "hobbi": "Baca",
                "sosmed": "@sciia__",
                "kesan": "Kak suci manis senyumnya, baik, dan asik jugaa",
                "pesan": "Semoga kak suci selalu mendapatkan apa yang kak suci mau"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "jadi MC",
                "sosmed": "@wielhawn",
                "kesan": "Bang wielman seruu sihh, kalo ngomong ntah kenapa selalu kedengeran nada MC",
                "pesan": "Semoga semua keinginan bang wielman cepat terwujud "# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "main hp",
                "sosmed": "@lia.h_264",
                "kesan": "Kak lia lucuu, baik sekalii, dan juga ramahh ",
                "pesan": "Semoga kak lia segera mencapai semua keinginannya"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kak aqila lucuu, asikk, dan selalu happy bawaannya",
                "pesan": "Semoga kak aqila selalu didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "jadi sekjen",
                "sosmed": "@hazelhandhaka",
                "kesan": "Bang hazel keren sih, ramah jugaa",
                "pesan": "Semoga semua keinginan bang hazel segera tercapai"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                 "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak nadya maniss sekali, baikk, dan juga sangat ramah",
                "pesan": "Semoga kak nadya segera mendapatkan apa yang kak nadya inginkan"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani ",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang ",
                "alamat": "Jl. Lapas",
                "hobbi": "nonton film,musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kak dwi lucuu, sangat baikk, dan juga ramah sekalii",
                "pesan": "Semoga kak dwi selalu dikelilingi hal-hal baik dimanapun"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSenator()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pxvGu3epoSLArzn7_OvfOmfNufpKlb4N",#kak arini
            "https://drive.google.com/uc?export=view&id=1nmDw_fouX65zVC9AfLCl7Er4hiGhhnhS",#kak nabyla
            "https://drive.google.com/uc?export=view&id=1ooyuzaV6Z59CWqsR7TtcAgUFumRhOudh",#bang aditya
            "https://drive.google.com/uc?export=view&id=1SE_1D4C-KA3R0gipqiw8eEBsqZag6avc",#kak fathya
            "https://drive.google.com/uc?export=view&id=1xjn3UXJjuVzbKKeuVqy-e-k_mKBdHcDY",#kak tarisya
            "https://drive.google.com/uc?export=view&id=1_5Mhn3MbyDHmX7qRNFpFLgIZrV9YkHHP",#kak selma
            "https://drive.google.com/uc?export=view&id=11TPJAt1efo5-i03d2JVECFWsYiblcN8L",#kak ashila
            "https://drive.google.com/uc?export=view&id=1EPRvogr3OD9QrQYLGkgAscg3hBy1q47s",#bang danil
            "https://drive.google.com/uc?export=view&id=1-57keZ6xg0QAuLQqaWJQBxevqEMlARj4",#bang favian
            "https://drive.google.com/uc?export=view&id=1NPA6xLNJHBIXJ6CT_5mG2nFpNgHXNney",#bang yazid
            "https://drive.google.com/uc?export=view&id=151C5khb6ReD0SBmIauyPBg-plQghouw_",#bang rizaldi
            "https://drive.google.com/uc?export=view&id=1eJHSXhePyjqGgAL2XGnnqjcRKINshjkv",#kak saskia
            "https://drive.google.com/uc?export=view&id=1sQEEHM3hv_8BnWQiPX3-tPWr4JcW4BiN",#kak khoirul
            "https://drive.google.com/uc?export=view&id=1otESiAuO8Yafc62KWS9namE-QvGH2PmP",#bang ahmad
            "https://drive.google.com/uc?export=view&id=10mTtg_87tzH_3JfuDLrEnB9PD4jcLrG2",#kak indah
            "https://drive.google.com/uc?export=view&id=1YpI6cJ-U9F5rnpRwNkS7X0RVKDIJE0it",#bang bima
            "https://drive.google.com/uc?export=view&id=122qGZGNtSV0d0K_Xu4m4adYfKjeThE_6",#bang bimo
            "https://drive.google.com/uc?export=view&id=1POQWtvp3_EQZT2RjXbcFT45ueQB6xVYo",#kak adinda
            "https://drive.google.com/uc?export=view&id=1Arz2yH367KozGsE3OPOFLccINZgT8pXs",#kak yolanda
            "https://drive.google.com/uc?export=view&id=16pmLw-X2EKph3sIEZ4cT6EqcV0hXrCdB",#kak riska
            "https://drive.google.com/uc?export=view&id=1ktgmR7r7NTbZ7sdKyfNGs0js5XA4aGxl",#bang alfaya
            "https://drive.google.com/uc?export=view&id=1HYdeOOcEwVL4lN6U44hlxyAB63bdSoF4",#kak asri

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
                "kesan": "Kak arini pas awal terlihat garang, tapi aslinya tidakk",
                "pesan": "Semoga kak arini segera mendapatkan apapun yang kak arini inginkan"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak nabyla maniss, dan juga pas ngeasprak sangat baikk sekali",
                "pesan": "Semoga semua keinginan kak nabyla segere terwujud yaa"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "Bang aditya sangat seru, pas pplk bang adit asik benerr",
                "pesan": "Semoga bang adit selalu didekatkan dengan hal-hal baikk"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "lll",
                "pesan": "semangat menjalani hari-harinya kakk"# 1
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
                "pesan": "semangat menjali semester akhirnya kak"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "kakanya cantik dan senyumnya maniss",
                "pesan": "semangat kuliahnya kak selma"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "sini",
                "alamat": "jauh pokoknya",
                "hobbi": "tidur",
                "sosmed": "@kshigf",
                "kesan": "kakanya lucu , ramah dan gemass",
                "pesan": "Tetap semangat untuk Kakak dalam menyelesaikan tugas"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "baru tau kalo bang danil ternyata yang masuk ITERA ganteng itu tohhh",
                "pesan": "semoga ikan cupangnya sehat ya bangg"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "makasih bang yang selalu gercep kalo ada yang sakit selama rangkaian",
                "pesan": "semoga selalu bahagia dan ayo badmin lagi bangg"# 1
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "((15≪1) & 31) ⊕ 10",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "aku kira orangnya galak, ternyata asik juga kalo lagi ngobrol dan ternyata anak smanda",
                "pesan": "rajin-rajin pulang yuk banggg"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah ",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "tanyain sama yuder",
                "sosmed": "@jaldii._",
                "kesan": "orangnya asikk banget dan ada aja yang dibuat lelucon",
                "pesan": "semangat mc nya banggg"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "kaknya cantik, lucu dan ramahh",
                "pesan": "Tetap semangat untuk Kakak dalam menyelesaikan tugas"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kak mut lucu dan gemass, keren banget sihh bisa lolos pimnas",
                "pesan": "semangat pimnasnya semoga menang ya kakkk"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                 "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "keren bang ahmad dengan segala prestasinya",
                "pesan": "Tetap semangat untuk Kakak dalam menyelesaikan tugas"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "makasih kak dah bantu kallo sakit selama rangkaian, seneng bisa kenal di hublu juga",
                "pesan": "energinya jangan pernah habis ya kak buat selalu heboh, tetap semangat untuk Kakak dalam menyelesaikan tugas"# 1
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung ",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "jujur serem liat bang abim waktu di kotbar karna mukanya serius banget dan aku ga terlalu jelas ngeliatnya",
                "pesan": "makasih bang atas ilmu yang di beri saat magang hublu"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus ",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "hobinya sangat keren sihh bang, pasti mau bangun claster yaaa",
                "pesan": "Tetap semangat untuk Kakak dalam menyelesaikan tugas"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "21",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "kakanya cantik banget suka ngeliatnyaaa omgg",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "mentor yang baik dan ceriaa bangettt",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                 "umur": "20",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "pertama kenal waktu jadi asprak alpro, ternyata lanjut jadi mentor kesayangan tensor",
                "pesan": "makasih kak udah perhatian ke tensor, dah mau dengerin cerita keluh kesah ku dan kasih saran yang terbaik, dan banyak hal lagi yang ga bisa ku unggkapkan lewat kata-kata kakk"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "hobbinya sangat mengundang semut sih itu bang",
                "pesan": "Tetap semangat untuk Kakak dalam menyelesaikan tugas"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "kak mei cantik banget suka ngeliatnyaa omgg, baik hati banget lagi",
                "pesan": "semoga selalu bahagia dan ceria ya kakk, Tetap semangat untuk Kakak dalam menyelesaikan tugas"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vc1yGhpyx2PCJKg7mavJ0JMssR5T3Al_",#bang fabio
            "https://drive.google.com/uc?export=view&id=1PZO4mpVwLMQsoT2xKKi-hWF794Sb92ve",#kak tanty
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#bang fadil
            "https://drive.google.com/uc?export=view&id=1ZghJxnrrRHAaezD_pXyQZontK-bEwgFZ",#bang manuel
            "https://drive.google.com/uc?export=view&id=115SeNzR1qIsopvimZj_Wx-uG0Jn0gq_q",#kak ni made okta
            "https://drive.google.com/uc?export=view&id=1LfFGyvmfdFdVtNWLKly4_rftaRIaCMpq",#kak risa
            "https://drive.google.com/uc?export=view&id=17Dgs5w_P63wZafMm0wu_aq5C3FTxqkAT",#kak vannisa
            "https://drive.google.com/uc?export=view&id=1c9gPLBasSDNAWjNcNLUq6WC2GCEauCCR",#kak yulia
            "https://drive.google.com/uc?export=view&id=1bAmV_RBdEmgJ9VAWL2sQLCSSzABDeG35",#bang akeyla
            "https://drive.google.com/uc?export=view&id=1E4edCwYHawYzeQKy-jzjnhKfbBf2xIrR",#kak elsa
            "https://drive.google.com/uc?export=view&id=1EsRXcKWZFOjd6KPvMJE2y-W0wZai1rUr",#bang fadya
            "https://drive.google.com/uc?export=view&id=1ZGy-S2ZhN_q7G0uU2GHe4Ogy0mXiGdk3",#kak lovi
            "https://drive.google.com/uc?export=view&id=1kq8IeatO8k9rw5tFrZycjpxTbQFCEcD0",#bang alsi
            "https://drive.google.com/uc?export=view&id=1venv2VzL9Wim7HQrGogJcahwtgMuSTPm",#kak sherena
            "https://drive.google.com/uc?export=view&id=1OBvERRs5k9gaIPdkrUKOWY7pG6eSjMiX",#bang razin
            "https://drive.google.com/uc?export=view&id=1CPeIoCDfHlIUtdrSY8gP0b1i4cVaHmoP",#kak faiza
            "https://drive.google.com/uc?export=view&id=1ZUwXjkc5cdv3wErpnQhGDCc6I5fpuKcy",#bang gathfan
            "https://drive.google.com/uc?export=view&id=1kAC0LmOPx2luRY0joiwRWbyzoL0h7a4B",#bang hafidz
            "https://drive.google.com/uc?export=view&id=1jums2hUccWkwb8SpcAAdM-pLa69D0dKp",#bang kaleb
            "https://drive.google.com/uc?export=view&id=1RDewv1lCDTJOUjPZyp79IjxkWTkf9ktA",#kak melva
            "https://drive.google.com/uc?export=view&id=1mlg_BSmN7q-hKZT8Fk_opK64SEjQiqIk",#bang syafiq
            "https://drive.google.com/uc?export=view&id=11cH8hNEMk1CQnopD6JP_wPKpiG_rDy1E",#bang henry

        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton Bandar Lampung ",
                "hobbi": "Gangguin bang keya",
                "sosmed": "@biyokcb ig",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Nonton film",
                "sosmed": "@tvnty_",
                "kesan": "...",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak."# 1
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "...",
                "pesan": "Tetap semangat menjalani pengobatannya yang bang semoga lekas sembuh, semoga sukses selalu menyertai abang."# 1
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis ",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12",
                "asal": "Bali",
                "alamat": "nusa peninda",
                "hobbi": "menghayal",
                "sosmed": "@violaadrtr_",
                "kesan": "...",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "..",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "1244500078",
                "umur": "19",
                "asal": "kepulauan riau",
                "alamat": "teluk betung",
                "hobbi": "nonton khw",
                "sosmed": "@vunnycaa",
                "kesan": "....",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "...",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                 "nim": "123450119",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@keyashafi_",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."# 1
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara ",
                "alamat": "Pemda",
                "hobbi": "Sibuk",
                "sosmed": "@_els.a",
                "kesan": "...",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "airan",
                "hobbi": "mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "...",
                "pesan": "...."# 1
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "....",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "kalianda",
                "alamat": "kota baru",
                "hobbi": "main game, tidur",
                "sosmed": "@aluccy_",
                "kesan": "...",
                "pesan": ".Selamat melanjutkan aktivitas kuliah! Semoga IPK semester ini memuaskan dan sesuai harapan.."# 1
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal":"Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "...",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                 "umur": "21",
                "asal":"Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel ",
                "sosmed": "@faizaanjanii",
                "kesan": "...",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Rajabasa Raya",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            },
{
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur ",
                "hobbi": "3N ( Ngoding , Ngegame, Nyibukin Diri)",
                "sosmed": "@apiszzaja",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Campang Raya, Sukabumi",
                "hobbi": "Gym, membaca, dan bermain",
                "sosmed": "@kelelep_comberan",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                 "umur": "19",
                "asal":"Sumatera Selatan ",
                "alamat": "Sukarame ",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "..",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syafiqui",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal":"Kotabumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "....",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dr4JxNbLQ7EZdN7C6hm1xSVlNermly_r",#bang ihsan
            "https://drive.google.com/uc?export=view&id=1GAspjlnw_q-T9p_DMhey_AWMfilWQIFp",#kak hanifah
            "https://drive.google.com/uc?export=view&id=1_GrkLRpEmgoiyQic5sIw1XSOzaOd6vPf",#kak afifah
            "https://drive.google.com/uc?export=view&id=1Bqv6hKGiBAxqePfBnCsXHSNWswXxzvxS",#bang hasan
            "https://drive.google.com/uc?export=view&id=1QOXkh6M_A5-NCtHhKc_g310yk5izjOY4",#kak layina
            "https://drive.google.com/uc?export=view&id=1z3gcw3aSKSOFm_d8iNNQxcBHlNRNdSuA",#bang iqbal
            "https://drive.google.com/uc?export=view&id=11lECPvvnlhJs8zforwi_bK6neEuIKrHN",#kak talitha
            "https://drive.google.com/uc?export=view&id=1XZniWFMCqfAuKwtVKsHCaNOLopN-xHCH",#kak anadia
            "https://drive.google.com/uc?export=view&id=1MFksn0eM6rcXYe41O48mm2Lc6YZvZODA",#kak abdilah
            "https://drive.google.com/uc?export=view&id=1GcS8opanBzIeo1DmId6ROgK0_Nj3S0m2",#bang afdhal
            "https://drive.google.com/uc?export=view&id=1nC5ZKnJZcGfgyOEKkKQRqJvWOMvInDst",#kak anggun
            "https://drive.google.com/uc?export=view&id=11hevOsDW3ItaqcJueu_ST6Isxp4FkJ4L",#kak della


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
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "hanifah inaya sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "...",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "...",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin",
                "sosmed": "@lay.inr_",
                "kesan": "...",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "....",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "...",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Abdilah Fikri Alpome",
                 "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "...",
                "pesan": ".Selamat melanjutkan aktivitas kuliah! Semoga IPK semester ini memuaskan dan sesuai harapan.."# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FIja-sAlEljxPyVgo2B0Dtc8KADIEzC2",#kak nayla
            "https://drive.google.com/uc?export=view&id=1pXvMZH3O5QXJSdnl0V77tGYo5StoEq_f",#kak donna
            "https://drive.google.com/uc?export=view&id=1P0-RxhdZk4ZGH8ujFIhfxGG3-7FlaUSB",#bang labo
            "https://drive.google.com/uc?export=view&id=1Ee6z2F2subUM_P1FEeqTA8aLwKdUTbYX",#kak anash
            "https://drive.google.com/uc?export=view&id=10KlKO1l_-4hUfscYUjmSMPnUZKR9atEW",#kak felisya
            "https://drive.google.com/uc?export=view&id=1aQXf5ZCNnus2eKs6g3_-wWp_AFU0sEJE",#bang razan
            "https://drive.google.com/uc?export=view&id=1kQ9sznhp7zj8H3m5VRMe6EnhuKlXILU0",#kak sania
            "https://drive.google.com/uc?export=view&id=1hgxszK33olxryoCdRJ267-wcXiUqLiIk",#kak alisha
            "https://drive.google.com/uc?export=view&id=1Q4JTGHJUuGgJMnm6bzuscxmL9Q5obDrY",#kak alya
            "https://drive.google.com/uc?export=view&id=136solLTW-9j9M5kzYWL05rvXJ0He68XL",#kak bunga
            "https://drive.google.com/uc?export=view&id=1V99HC6sTL3SmNWpP64cB926iRvW9dOjk",#kak difanya
            "https://drive.google.com/uc?export=view&id=151KEY9TVr3ffmlZ7Jl-YUiY8Vm8LXmRg",#kak nazlah
            "https://drive.google.com/uc?export=view&id=1y26myrUciXDKAm6U9eeH2odD69doN5cB",#kak raihana
            "https://drive.google.com/uc?export=view&id=1je3oVKZUJ9TCfJ9Y2J3xnsk7F6sS-0aG",#bang dafa 
            "https://drive.google.com/uc?export=view&id=1sddGo_PUS7V8v5vW9g8wxjm4LgEzQygi",#bang edsel
            "https://drive.google.com/uc?export=view&id=1Fw4NjT8IHO_y88kIZbXl5DOr2NEpfEcw",#kak lucia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#kak shafa
            "https://drive.google.com/uc?export=view&id=1NIviKZtMCV_Nx1hY4TEzL9SkO-JF8E51",#kak zannuba

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
                "kesan": "..",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "...",
                "pesan": "Semangat terus ya kakaaaa semester ini, semoga lancar2 kuliahnya sampai lulus"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu ",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran ",
                "sosmed": "@noerruuu",
                "kesan": "...",
                "pesan": "..."# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Way Halim ",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."
            },
            {
                "nama": "Felisya Nabila Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal": "Lampung Timur ",
                "alamat": "Kota Baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "21",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "...",
                "pesan": "..."# 1
            },
            {
                "nama": "Sania DWi Ayu Lestari",
                "nim": "124450086",
                "umur": "21",
                "asal": "Karawang ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "pertama kali liat waktu pplk, kakanya cantik dan cute",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Alya Ramadhanti",
                 "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "kakanya cantik, ramahh dan cute",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "kakaaa cantik banget aku suka ngeliatnya",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Alquran",
                "sosmed": "@difanyhsa_",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@nzlhauly_",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Aira Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "kakanya cantik,ramhhh dan cute",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame ",
                "hobbi": "-",
                "sosmed": "@daffascript",
                "kesan": "..",
                "pesan":".."
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "...",
                "pesan": "..."# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "cute, gemass banget waktu liatnya karna  cantik bgt",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis dan menulis",
                "sosmed": "@_shaazzh",
                "kesan": "kakanya cantik dan ramah",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "kakanya cantik,ramahh dan baikk",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
# Tambahkan menu lainnya sesuai kebutuhan
