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
    dept_menu,
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
    return dept_menu(
        [
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
        ]
    )


def display_images_with_data(gambar_urls, data_list):
    """Menampilkan kating dalam bentuk Wide Horizontal Showcase Cards elegan dengan fitur live search."""
    render_kating_cards(gambar_urls, data_list, department_title=menu)


menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jTt4osiJlmcxLGM6anHugKQ4p6NmDUFu",
            "https://drive.google.com/uc?export=view&id=1lV3AFkRaJ-f8n0ILwYZE7igGiST8LQ5O",
            "https://drive.google.com/uc?export=view&id=1cKoLOVA0C-uGTZAWHK9ij-KJ2kWYZlKU",
            "https://drive.google.com/uc?export=view&id=1ZjJrfHoTdNclPxZOY7iXAIH2Bek7sHtl",
            "https://drive.google.com/uc?export=view&id=1_gi-ChNER8A-MpEIs3noBFLZOO_pdZXO",
            "https://drive.google.com/uc?export=view&id=1zu0Vf0wTxK0GgGLWkhVWilKlgaIQX2Ew",
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
                "kesan": "Bang fajar him orang yang baik, ramah dan rendah hati, belajar banyak hal juga dari bang him",
                "pesan":"Semoga kedepannya reza bisa mewujudkan apa yang bang fajar harapkan dari saya nantinya, terimakasih bang"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang aqil jen orang yang ramah, rendah hati, suka sharing ilmu dan peduli antar sesama",
                "pesan":"Semangat teruss bang aqil, semoga impiannya bisa terwujud"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak efi baik hati, murah senyum, bisa mengispirasi banyak orang",
                "pesan":"keep strong kak, semoga keinginannya terwujud!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang qois orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan":"Semoga kedepannya reza bisa tumbuh seperti bang qois, terimakasih bang"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak hafsa orangnya sangat baik, ramah, dan juga berkesan.",
                "pesan":"Semoga kedepannya kak hafsa dikelilingi dengan hal baik ya kak"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak luthfia orangnya sangat baik, ramah, dan juga sangat menginspirasi bagi saya karena jadi asprak baik hati.",
                "pesan":"Semoga kedepannya kak luthfia bisa tumbuh seperti kak luthfia, terimakasih kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hgy9q3amN5Ed-UsxvF3X7ETqlxrXKMAN",
            "https://drive.google.com/uc?export=view&id=1ayKNDuFh7xL76p8l4nFCLyh0iutfT5je",
            "https://drive.google.com/uc?export=view&id=1f-NdOIjLabE45U5idBE5cdRFcyQ_6nze",
            "https://drive.google.com/uc?export=view&id=1muE5178D3qZwbasNm5XDyhcNBizmu80o",
            "https://drive.google.com/uc?export=view&id=12deNFjAzGlr5IJjH4eBB-u93pYsdi1I7",
            "https://drive.google.com/uc?export=view&id=1l_ONFSNbXI4sJmbvhYDwQ6BmPO4CxvHt",
            "https://drive.google.com/uc?export=view&id=1D00XpO2mhmq-6hEgwpIRBBgsBxaG_y99",
            "https://drive.google.com/uc?export=view&id=1LYlY2i1ExdTUKKKKenFAtyVR7faGNduT",
            "https://drive.google.com/uc?export=view&id=1OyQ9zNfDy-m48A0f6HVAoVkXc67PdtDF",
            "https://drive.google.com/uc?export=view&id=1D46Ytn7hSO9EpIX6BIgCPj7k9qyxWvjd",
            "https://drive.google.com/uc?export=view&id=1baq71b6miwzh7f2TTBVZrg_LnajmeMOL",
            "https://drive.google.com/uc?export=view&id=1JlzSUy2Ybrols4BnViuGs06fPqBGZuS1",
            "https://drive.google.com/uc?export=view&id=1NOcecP852f6Hpogp0wxGOMx9z26nVfqN",

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
                "kesan": "Bang Ridho orangnya sangat humble, baik, dan juga sangat berkesan bagi saya.",
                "pesan":"Semoga kedepannya reza bisa tumbuh seperti bang ridho, terimakasih bang ilmunya, infokan ps aja bang langsung."# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak jue yang memberikan banyak insight hal baru, berkesan, baik, ramah",
                "pesan":"semangat terus kuliahnya kakak dan semoga terus menginspirasi orang banyak yak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Bang dharu menjadi role model karena prestasi yang membanggakan dan cara berpikir yang baik",
                "pesan":"semangat menginspirasinya bang dharu, semoga tercapai segala keinginannya yaa"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Niko orangnya sangat humble, baik, dan juga sangat berkesan bagi saya.",
                "pesan":"Semoga kedepannya bang Niko dikelilingi dengan hal baik ya bang"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kak siti orangnya sangat humble, baik, dan juga memiliki energi yang kuat dalam bersosialisasi.",
                "pesan":"Semoga kedepannya kak siti keinginannya tercapai dan segala hal urusannya dimudahkan"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang givaro orang yang baik, ramah, senang bersosialisasi kepada siapapun.",
                "pesan":"Semoga kedepannya bang givaro bisa terus menginspirasi dan semangat kuliahnya yak bang"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa orangnya sangat humble, baik, dan juga ramah.",
                "pesan":"Semoga kak nisa kuliahnya dilancarkan dan segala hal urusannya dimudahkan"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kak hani orangnya sangat humble, baik, dan juga berkesan.",
                "pesan":"Semoga kedepannya kak hani keinginannya tercapai dan kuliahnya dimudahkan"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang jeremia orang yang baik, ramah, menginspirasi banyak orang.",
                "pesan":"Semoga kedepannya bang jeremia bisa terus menginspirasi dan segala urusannya dimudahkan"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak monica yang memberikan banyak ilmu hal baru, berkesan, baik, ramah",
                "pesan":"semangat terus kuliahnya kakak dan semoga sehat as always"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang jona orangnya humble, baik, ramah, dan juga asik dengan semua orang",
                "pesan":"semangat terus kuliahnya bang, semoga cumlaude biar mantap"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak sekar orangnya baik, ramah, peduli sesama dan juga humble",
                "pesan":"semangat terus kuliahnya kakak dan semoga usahanya selalu dimudahkan."# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kak nashwa yang memberikan banyak insight hal baru, berkesan, baik, ramah",
                "pesan":"semangat terus kuliahnya kakak dan semoga terus diberi kesehatan"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14YENE-OttLu9t6-K1D3EiVItt9VWgMFi",
            "https://drive.google.com/uc?export=view&id=1dpGP6YKR6uNScQ310uzfGga7y9pyXFHr",
            "https://drive.google.com/uc?export=view&id=1nziGOtWvoE56r050VfNywXLuxqxhjOyb",
            "https://drive.google.com/uc?export=view&id=1CHWAexG6h9pgrF47C39pXCPOwkRW3PK1",
            "https://drive.google.com/uc?export=view&id=1_9LmIb8SHBTmsJzBXV1lS6loX-Uv4wIc",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1x_Tl2UiGCWgXIWLOl3wqf8oZiF-pbbhr",
            "https://drive.google.com/uc?export=view&id=1IVfl9n6xhg6LMNRCK9TcKyfYe8IPiLa6",
            "https://drive.google.com/uc?export=view&id=1_Ma3wlwjrohrks0QJnbrZxfRMfIJWEbH",
            "https://drive.google.com/uc?export=view&id=1y-jE3qswGgkURBQHg2m6rOp9YIKcI8Y3",
            "https://drive.google.com/uc?export=view&id=1WcqyfQwvpry_pOsTu-lSnlwCOucxQBiW",
            "https://drive.google.com/uc?export=view&id=1v6WwuUUbytkBJS9m6fWfUm6sn1BFi2Rf",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1XgVw4Dk65snrhmCEJPjtIu89C8WstF71",
            "https://drive.google.com/uc?export=view&id=1ps1AIPSHIWjV-Z98SY7bA7xj4Y5BwTUw",

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
                "kesan": "Bang kevin orang yang ramah, baik, suka sharing ilmu dan rendah hati",
                "pesan":"Semoga kedepannya bang kevin selalu diberikan kemudahan dalam segala hal"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kak razka orangnya humble, baik, seru dan berkesan, kakak kelas SMP yang sama ini",
                "pesan":"semangat terus menggapai mimpinya ya kak"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Bang ali orang yang humble, ramah, senang bersoialisasi dengan siapapun",
                "pesan":"semangat terus kuliahnya dan menggapai keinginannya bang alii"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kak ayu adalah orang yang seru, baik, ramah dan juga senang bersosialisasi dengan banyak orang",
                "pesan":"Semoga kedepannya kak ayu dimudahkan segala urusannya dan impiannya tergapai"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang dafa orangnya humble, murah senyum, baik, dan suka sharing ilmu.",
                "pesan":"Semoga kedepannya bang dapa selalu dikelilingi hal baik"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kak ayu adalah orang yang seru, baik, ramah dan juga senang bersosialisasi dengan banyak orang",
                "pesan":"Semoga kedepannya kak ayu dimudahkan segala urusannya dan impiannya tergapai"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Bang afdal orang yang humble, ramah, dan tegas",
                "pesan":"semangat terus kuliahnya dan semoga dimudahkan segala urusannya bang afdall"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak juwi adalah orang yang seru, baik, asik",
                "pesan":"Semoga kedepannya kak juwi dikelilingi hal baik dan dimudahkan kuliahnya"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang ridwa orang yang asik, humble, dan murah senyum",
                "pesan":"semangat terus dalam menginspirasi dan semoga sehat selalu"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Bang andra orangnya rendah hati, humble, respect each other",
                "pesan":"semangat terus mengembangkan potensinya bang, dan semoga impiannya kegapai"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang bryan orangnya seru, suka sharing ilmu juga dan asik",
                "pesan":"semangat terus menghadapi dunia dan sehat selalu"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang ghiyats orangnya humble, suka sharing ilmu juga dan humoris",
                "pesan":"semangat terus menghadapi dunia dan dimudahkan kuliahnya"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak indah adalah orang yang seru, humble, ramah dan asik",
                "pesan":"Semoga kedepannya kak ayu dilancarkan kuliahnya dan semoga senang selalu"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kak caca adalah orang yang seru, baik, ramah dan juga murah senyum",
                "pesan":"Semoga kak caca dimudahkan segala urusannya dan dilancarkan kuliahnya"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Bang rafka orangnya respect each other, humoris dan humble",
                "pesan":"semangat terus futsalnya bang dan tetap sehat seperti biasanya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZbtFYqRx-UIRexCjvPMg19hbaHNtLEuE",
            "https://drive.google.com/uc?export=view&id=1U-wgpB8AywS5Uigfmbq0p_ngJl1WLpen",
            "https://drive.google.com/uc?export=view&id=178Cjp5REe0ppDV_o7hltZjO7LaZ4RSqy",
            "https://drive.google.com/uc?export=view&id=1PsrHc2055Iq1FHwalxnPL5NTHeOfDAj9",
            "https://drive.google.com/uc?export=view&id=13eDh0BIBZEUkOWj7qh34OyrRCJg9ZA9l",
            "https://drive.google.com/uc?export=view&id=16_rmx71QOIPQItsODJVjZENguCmNCewP",
            "https://drive.google.com/uc?export=view&id=1vrvQiXL0TR4J3kthgXqdmaBSrVNFEFCl",
            "https://drive.google.com/uc?export=view&id=1ltwdCfA44EZsQS43xSv239_49lUj0zsu",
            "https://drive.google.com/uc?export=view&id=16c0jKZo_QgIZdJKuNiH49kfZLBWkUdVX",
            "https://drive.google.com/uc?export=view&id=1FOMOic0Fca9yMv6uLZazbaLclrsAy0BB",
            "https://drive.google.com/uc?export=view&id=1LUweCaL1wL5KTBtbUbYIrwNP2-gXviAR",
            "https://drive.google.com/uc?export=view&id=1SIeaxcCezWHWSgRNM4LCebhkcu1cvOlZ",
            "https://drive.google.com/uc?export=view&id=1cc4c5fIY3N4PJWHp6wFtAziImmEhIdVz",
            "https://drive.google.com/uc?export=view&id=1hclkdQoRLZTnluBOivih1djjnc15hKlh",
            "https://drive.google.com/uc?export=view&id=1Tp24KS-vwTrXWtim3_DHbNli0kYdI7RW",
            "https://drive.google.com/uc?export=view&id=1uZHGxQzH9CwAhHs2N1KUcUa6vvqd60j3",

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
                "kesan": "Bang haikal orangnya seru, asik, baik, dan humoris level up, ini abang-abangan snare gaul ini.",
                "pesan":"Semoga kedepannya bang haikal dimudahkan urusannya dan selalu diberkati"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma orangnya super humble, cukup humoris dan berkesan.",
                "pesan":"semangat terus menginspirasinya yaa kak"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna orangnya humble, humoris, murah senyum dan ramah.",
                "pesan":"semangat terus kuliahnya yaa kak dan semoga selalu diberkati"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang farhan orangnya baik hati, ramah, murah senyum, humoris.",
                "pesan":"Semoga kedepannya bang farhan ddilancarkan rezekinya dan dilancarkan kuliahnya"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak Aisyah orangnya baik, ramah, respect each other dan murah senyum.",
                "pesan":"semangat terus kuliahnya kak dan semoga dimudahkan segala urusannnya"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kak Kharisma orangnya murah senyum, positive energy, baik.",
                "pesan":"semoga selalu diberi kesehatan dan keberkahan"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang jaya orangnya humble, ramah, senang bersosialisasi, asik.",
                "pesan":"Semoga bang jaya diberikan umur yang panjang dan selalu diberkati"# 1
            },
            {
                "nim": "124450051",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kak najla orangnya humble, respect each other, low profile dan baik hati.",
                "pesan":"semoga kak najla hidupnya selalu dikelilingi hal baik yaa kak"# 1
            },
            {
                "nim": "124450100",
                "umur": "18",
                "asal":"Lampung Selatan",
                "alamat": "Korpri raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Bang rozak orangnya seru, asik, ramah, dan murah senyum.",
                "pesan":"Semoga kedepannya bang rozak diberikan umur yang panjang dan selalu dimudahkan urusannya"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "masak",
                "sosmed": "@christian8872",
                "kesan": "Kak teresa orangnya asik, baik, dan humoris.",
                "pesan":"semoga selalu dikelilingi hal baik dan semoga selalu diberkati"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan":"Bang hanif orangnya ramah, humble, low profile, dan cukup humoris.",
                "pesan":"Semoga kedepannya bang hanif dimudahkan urusannya dan rezekinya dilancarkan selalu."# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20 tahun",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Bima",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Kak audina orangnya humble, positive energy dan berkesan.",
                "pesan":"semoga hal baik selalu mengelilingi yaa kak, keep strongg!"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kak cika orangnya low profile, ramaah, baik, dan humble.",
                "pesan":"semoga selalu diberi kesehatan dan diberkati selalu"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kak gustin orangnya humble, ramah, baik dan humoris.",
                "pesan":"semangat terus kuliahnya yaa kak, god bless u"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan":"Bang harvin orangnya seru, asik, baik, dan humoris level up.",
                "pesan":"Semoga kedepannya bang harvin dimudahkan urusannya dan selalu diberkati"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Kak bina orangnya baik, cukup humoris, ramah, dan positive energy.",
                "pesan":"semangat terus kuliahnya kak, dan semoga dilancarkan selalu urusannya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15kkuKeZXvSlIsL03c9BnFAHKhCpH2LWG",
            "https://drive.google.com/uc?export=view&id=1DPACbfL9qKbbjl_68Lu1u8weG0YiHQlN",
            "https://drive.google.com/uc?export=view&id=1_EyoZNucEcdKhdValFp7TlRlM9ZOYC1T",
            "https://drive.google.com/uc?export=view&id=1O9vWJp7UdLzVzEvvIp9GTtWmL7dSZGc7",
            "https://drive.google.com/uc?export=view&id=11l6yKGYxnFONauY1yoyNMkaSPhsE3rfO",
            "https://drive.google.com/uc?export=view&id=1sZvsbrvw3xobNjcAtWvrB7a5ODQ8JHFX",
            "https://drive.google.com/uc?export=view&id=1_9EBsaKR9VJ52thx8MlZ6kNYkl8OCXm4",
            "https://drive.google.com/uc?export=view&id=1xxly_yAEM7BYUjIjYrufvazLrP9a4n62",
            "https://drive.google.com/uc?export=view&id=1iqv6SqyZiD9seFaQJHN_et58M2O-UeIT",
            "https://drive.google.com/uc?export=view&id=1Tzj6Fc6J8wp-IpTomMM_K7ChVatytJRO",
            "https://drive.google.com/uc?export=view&id=1GEgyd4bq77rkjinAHgXT_uT_G2uzhlj6",
            "https://drive.google.com/uc?export=view&id=1XB4MnbquWxxiBDX4CfhtrPxruHasanXw",
            "https://drive.google.com/uc?export=view&id=1atxF4ZINctSc4ETv8wHMII7kTRqL2ftr",
            "https://drive.google.com/uc?export=view&id=10mbFZwLHV5pWk7_DwDW0a9ifeXPVHKDu",
            "https://drive.google.com/uc?export=view&id=1sqeAo7wle6UZbn-0QcjreJRl0ecbTsBl",
            "https://drive.google.com/uc?export=view&id=1UlR-ad508ASzMpMQu-rOnjPrWHS8hx5H",
            "https://drive.google.com/uc?export=view&id=1s6XTjJQiqKqGXwoVfxqP-5GREihCvB44",

        ]
        data_list =[
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal": "Pinggir Pantai",
                "alamat": "Samping Kost Capo",
                "hobbi": "Ngerjain Anak Kader",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakak NIM baik hati, tidak sombong, lemah lembut, humble, dan ramah hahay",
                "pesan":"Semangat kuliahnya yaaa kak, semoga selalu dilancarkan rezekinya dan jangan nyebrang di sirkuit kalo lagi ada balapan kak"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany orangnya ramah, humble, cukup humoris",
                "pesan":"Semangat terus dalam segala hal yaaa kak, semoga selalu dimudahkan urusannya, don't forget to say wallahi"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel orangnya welcome, baik, humble, dan respect each other",
                "pesan":"Semangat terus menggapai mimpinya bang, semoga sehat selalu bang, one word for bang Nobel 'GHAUWW'"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi orangnya humble, humble, low profile, dan ramah",
                "pesan":"Semangat terus menjalankan kehidupan bang, semoga segala urusannya dipermudah"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang yake orangnya welcome, low profile, baik, dan menginspirasi dan cocok kalo jadi captain america kalo di film gundala",
                "pesan":"Semangat terus kuliahnya bang, semoga selalu dipermudah urusannya bang"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang caesar orangnya supportif, ramah, humble, dan berkesan serta selalu ngasi jalan buat adik-adik tercintah",
                "pesan":"Semangat terus menggapai mimpinya bang, semoga sehat selalu bang."# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak yudia itu baik hati, ramahh, baik hati, humble, dan menginspirasi",
                "pesan":"Semangat terus dalam menjalankan kehidupan yaaa kak, semoga selalu dilancarkan rezekinya"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang haikal orangnya ramah, low profile, humble, dan menginspirasi",
                "pesan":"Semoga apapun yang diharapkan terjadi di tahun ini bang"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak putri orangnya humoris, lucu, baik hati, dan low profile",
                "pesan":"Semangat kuliahnya yaaa kak, god bless u kak"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@andra.lhm",
                "kesan": "Kak bila orangnya baik, murah senyum, ramah, dan sangat interaktif, intinya baik dan berhati hello kitty",
                "pesan":"Semangat terus yaaa kak, semoga dimudahkan segala urusannya."# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Abang ini humble, baik, ramah, seru juga abang ni",
                "pesan":"sukses selalu bang (coach) desman, semoga lancar sampai lulus ya bangg ketang DATANOVAS"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "kak azzelya lucu dan baik, serta ramah ",
                "pesan":"Semangat dan sehat selaluu kakaa, semoga hal baik selalu berdatangan"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "Kak caca itu ramah, baik, dan humoris",
                "pesan":"sehat sehat ka cacaa, semoga semester ini dan kedepannya dilancarinn segala urusan kaka yaa"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang jemar ini baik dan humble serta welcome kepada siapapun",
                "pesan":"Semangat terus bang capo, kece dah udh masuk tiktok itera ganteng"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak nabila humble dan talkative, serta humoris",
                "pesan":"sehat sehat kakaa, semoga hal baik selalu berdatangan yaaa"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Abang ini baik, welcome dan ramah",
                "pesan":"Semangat teruss bang rafli, semoga sehat selalu bahagia selaluu dan dimudahkan urusannya"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "Kakak imut, lucu, baik, ramah dan talkative",
                "pesan":"sehat sehat dan lancar luncur kuliahnyaa kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

elif menu == "Departemen Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14Rz2UuS_U76fIX13dPQlrQPFQ1Ig8QqN",
            "https://drive.google.com/uc?export=view&id=1OAHOyesLeOhxq1ozPzNVKf0BMY8HM95O",
            "https://drive.google.com/uc?export=view&id=1wI3HVHNaF3DWCZTw4VmJrF-sY_BdbhuL",
            "https://drive.google.com/uc?export=view&id=1e5wlN7lpkMcaIKlAXfweWhVgHfyr1-SC",
            "https://drive.google.com/uc?export=view&id=1c3ASvGBKtdoKHGaOFP0dQfLDiPIM8tBh",
            "https://drive.google.com/uc?export=view&id=1ztdQyzhMHYNy-SayUcoKXEDJb_Y9LA6F",
            "https://drive.google.com/uc?export=view&id=1DQkyL--pgRtvFWcpUAUDvZxwS8oXVyDb",
            "https://drive.google.com/uc?export=view&id=1os0z4moD8V_gK_cOxk--OCSnahgi9n48",
            "https://drive.google.com/uc?export=view&id=1_aVQrmVSVorVXC6hTBwkE7QbPnF8Ect4",
            "https://drive.google.com/uc?export=view&id=19_HGdsrIlx8CNe0RnXMWxmmySlwm8oYK",


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
                "kesan": "Kak azizah, senator gokil, elegan dan menawan, itera bagoyang kalo ka azizah menyampaikan aspirasi, dan ini adalah the next bang rian, sang pembawa aspirasi masa sobat data",
                "pesan": "kak azizah yang WARROWWW itu seru banget, jujur ilmu magangnya gharrow alias gokil banget broww, tetaplah humble dan jangan lupakan cipayung itu ya kaks, hahay"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "abang ini orangnya baik dan asik, punya byd, gawul dan punya gaya sendiri kalo foto sama bang helmy ini",
                "pesan": "Semangat kuliahnya bang!! terbang setinggi mungkin tapi jangan ketinggian nanti nyangkut di sutet sukarame repot"# 1
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Nemenin Wielman MC",
                "sosmed": "@barus.fernando",
                "kesan": "Bang fernando keren banget, hobinya yang supportif menandakan beliaw cocok menjadi the next rocky gerung",
                "pesan": "Semangat buat selalu nemenin bang wielman nge-MC, semoga bang wielman jadi seskab"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru ",
                "hobbi": "Baca",
                "sosmed": "@sciia__",
                "kesan": "kaa suci orangnya asik banget, soat baik warung bandung belwis, bunda cosval sahabat baik kami",
                "pesan": "Semangat terus kaka kuliahnya, dan akhir tahun ini langsung aja ke bandung, kisah manis mont blanc nya enak jujur"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "jadi MC",
                "sosmed": "@wielhawn",
                "kesan": "Jiwa MC (bukan Main Character) nya jujur gharrr, pembawaannya oke banget, big rispek bang wiel",
                "pesan": "Semoga nanti bang wielman makin semangat kalo ditemenin bang nando buat nge-MC yakkk"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "main hp",
                "sosmed": "@lia.h_264",
                "kesan": "Aku suka nih karena jabodetabek connection, pecinta FM sejati, tapi tetep tuku dihati, wharrowwww",
                "pesan": "Semangat, sehat, kuat dan nanti jadi seskab nya pak lucky, siapa tau dia jadi presiden kan"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Mentor bayes sahabat baikk kami, motornya stylo gaul mentok, style ootd nya setara kent hadi",
                "pesan": "Semangat buat kuliahnya, dilancarkan urusannya dan jangan jadi the next Queen of the kingdom Puan Maharani"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "jadi sekjen",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abang-abangan ketuplak, motornya XSR kebut, salah satu orang yang wibawanya cukup GHARRR",
                "pesan": "Semangat kuliahnya bang plak, semoga besok jadi presiden biar seluruh rakyat Indonesia tau di dunia ini ada orang yang namanya bang Hazel"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak Nadya, baik, humble, humoris, huahaha, semoga nanti suka denger lagu dari BANDALM my band kesukaan ak",
                "pesan": "Semoga hal-hal baik akan selalu datang ke kak nadya, udah itu aja, tapi boong hahay. Timakasi loh ya julukan golden retrievernya, terkenang itu"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani ",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang ",
                "alamat": "Jl. Lapas",
                "hobbi": "nonton film,musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "kakanya murah senyum, jujur ghawull kakak ini, dan kakak ini menyenangkann kalo diajak ngobrol",
                "pesan": "semangat kuliahnya kak, jangan nyerah dulu sebelum perang di itera ini usai"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1v836V-BYXVAAdkfH0ppJg3BEPQ_KHIuq",
            "https://drive.google.com/uc?export=view&id=1JtDhtejgk29kN9m4V91RTAkgfWsjeg-B",
            "https://drive.google.com/uc?export=view&id=1KeBHmyKpdjkP_maYWZWdSwY7T0xpF_nj",
            "https://drive.google.com/uc?export=view&id=11XpA-gp23ZSo-1TTM3eJ0qBZlxp7_Eey",
            "https://drive.google.com/uc?export=view&id=1U3l-QKmph_XOGiU8ktGT0bMiq_cAfFCD",
            "https://drive.google.com/uc?export=view&id=1jhPwLdu5GydsqqqtYtAlb-gNJ8aliU-I",
            "https://drive.google.com/uc?export=view&id=1CJ-xYOBkkGa622SdkWTZ6YhmscGY-J3I",
            "https://drive.google.com/uc?export=view&id=1yBJ9m2EhJAjCDRGJEmxJjWXsOz2Y98Ec",
            "https://drive.google.com/uc?export=view&id=1g-ZoldbFgLwrqxVAvEHYmiC8n2DFu25L",
            "https://drive.google.com/uc?export=view&id=10vF9ewuEHh5sfoTsNJu831-HRcKte6Fy",
            "https://drive.google.com/uc?export=view&id=1p5cOU4y5WWMqLZn7-0HvsliZpVXb8AVZ",
            "https://drive.google.com/uc?export=view&id=1VUs1hht9-kJuBsAxEqrDSJzdf8xPx1PA",
            "https://drive.google.com/uc?export=view&id=1CN2ijY5-gpOQikScZIeOHRSBtRGkdROm",
            "https://drive.google.com/uc?export=view&id=1Ur6MaOYppe7XvrhEnq-o8ikGUF2-_5Bq",
            "https://drive.google.com/uc?export=view&id=1NaIa403gfz5wgljIMjq4v5CbA6TsXrMV",
            "https://drive.google.com/uc?export=view&id=1l6xc0DF_WVBR4U-8ST7b3klWCPU222pM",
            "https://drive.google.com/uc?export=view&id=1VSJYLENVBF-TY_cgd_p1pt_La7lnVEjy",
            "https://drive.google.com/uc?export=view&id=1rW-7_ZSeuAxeK2jbPWdf56WU6p2WhOOf",
            "https://drive.google.com/uc?export=view&id=1AjQu8HynzlOQ8IW3gMpj3HqjLQWy-xrL",
            "https://drive.google.com/uc?export=view&id=12QzvFKReq7UZTlwkvIJJ1KThieDPFTxv",
            "https://drive.google.com/uc?export=view&id=1NSdGPYua3dRNTEr-nq1f9WT3umivmlI0",
            "https://drive.google.com/uc?export=view&id=1O0WzpXaoDSBdjjyNtfkP8_-FrvW1Il46",

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
                "kesan": "ngeliat kak arini tuh kawa wanita carier banget",
                "pesan": "Semangat dan semoga lancar TA nyaa "# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya manis banget suka ngeliatnyaaa",
                "pesan": "always senyum yaa kaa"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "jujur bang Adit ini supportif, ramah dan gampang bikin suasana jadi cair, banyak ilmu baru yang didapat dari bang Adit",
                "pesan": "Sehat sehat terus ya bang, semoga sukses selalu menyertai bang Adit"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "kak fathya ceria banget orangnya omggg sukaa",
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
                "nama": "Danil Nur Fadillah",
                "nim": "124450103",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "SOBAT DUGENN, tapi abang ini dugen yang berhasil, kan kalo saya dugen gagal, tapi gapapa ilmunya tetap daging karena dapet insight baru.",
                "pesan": "semoga ikan cupangnya jago buat gelut sama ikan cupang laen, btw adu boleh lah bang ikan cupangnya, hahay"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "kata pak helmy di wayhalim",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Abang-abangan asprak alpro yang baik ini, cepat tanggap kalau sang adik lagi rangkaian sakit",
                "pesan": "semoga selalu sehat, kuat, semangat, hebat dan ayo jadi asprak lagi bang, sama jangan ngesen kanan belok ke nasi padang pas puasa bang, tuhan marah nanti"# 1
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "abang-abangan ini, gawull, asik juga kalo diajak ngobrol abang ini memang",
                "pesan": "Tetap semangat bangg, gawulll"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah ",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "ga balas chat orang",
                "sosmed": "@jaldii._",
                "kesan": "orangnya asikk banget dan kalo liat abang ini keinget 'bestie bestie, well' pas PPLK",
                "pesan": "semangat mc nya bangg, dan semoga next nya ga malas lagi balas chat orang"# 1
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
                "kesan": "the role model, orang yang keren buat propaganda dan support adik dan menuntun kemanapun adik berjalan",
                "pesan": "Tetap semangat untuk bang Ahmad, semoga segala usaha bang Ahmad bisa menjadi terealisasi nantinya"
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
                "kesan": "BANG BIM BIM, ini bang bima tau pas di confess FG karena ada foto bareng bang azmi sama bang hazel",
                "pesan": "semangat terus abang abangan kadiv OP sciencefest, semoga yang disemogakan tersemogakan"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus ",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "hobinya keren bang, ini kayanya cocok buat jadi agency perumahan di BSD",
                "pesan": "Tetap semangat bang, semoga nanti punya ruah di Menteng yak, biar deket kemana mana"
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
                "umur": "21",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "nyari duit",
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
                "kesan": "pertama kenal waktu jadi asprak alpro (agak ketat dikit tapi oke), ternyata lanjut jadi mentor kesayangan tensor (btw piscok enak lho ya)",
                "pesan": "tetap menjadi mentor gokil, tampan dan pemberani, elegan dan menawan, walaw dunia kaya gini, kakak harus kaya gitu intinya, gokill, dan jangan terbang ketinggian nanti agak skeptis ngeliat ketinggian, semoga bisa membantu bang zaldi untuk membalas chat agar tidak malas balas chat"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "hobbinya sangat dicintai sama dokter spesialis menangani diabetes bang tapi semoga ga sampe diabetes",
                "pesan": "Tetap jalani kehidupan bang, sertakan yang manis manis juga kaya minum americano gitu"
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
            "https://drive.google.com/uc?export=view&id=1wH-ReftykbKMGMcFS0ErmXvIrbzw-ztl",
            "https://drive.google.com/uc?export=view&id=1l6sXjImASD4KyLrUxwmJqxd9KYdhpiOp",
            "https://drive.google.com/uc?export=view&id=",#fadil prasetyo
            "https://drive.google.com/uc?export=view&id=1UKakdbOXwwSWpFtHwu2cXEam9603JM0H",
            "https://drive.google.com/uc?export=view&id=1JtlxtCc97sIKsipm-FVFEw0yjZXfRvqj",
            "https://drive.google.com/uc?export=view&id=1jHI0pXANxGd5gJ_L8T_D41d5C8quF8iT",
            "https://drive.google.com/uc?export=view&id=1o6YBxrQsOqwU77t_MbsyBtHryQddCgyn",
            "https://drive.google.com/uc?export=view&id=1RSNqNM7wgezfMxzx_t91jBtE8_x3wgv-",
            "https://drive.google.com/uc?export=view&id=1q8uTqeQF--WiDdUtugA5hb0tR7oNg1Ck",
            "https://drive.google.com/uc?export=view&id=1Rk6bwIBn1r4T6C7m3HZ8hwBIffZ325fZ",
            "https://drive.google.com/uc?export=view&id=1f8iUO7V3nAeCchtRgO6p9FbodFC_gRKY",
            "https://drive.google.com/uc?export=view&id=1sFYRaOvclAt-2pTQV97Ta5ATf8MOxFkR",
            "https://drive.google.com/uc?export=view&id=1AFKWqEPjzw3DKEDoUJhu3BbOTqldDwvh",
            "https://drive.google.com/uc?export=view&id=1wnna2BE2VZuDSeMmK6IyhxxhIoy6AJAV",
            "https://drive.google.com/uc?export=view&id=1ZezFxtcVE6rsBrvORTvrsw8XhIHQ-Fmo",
            "https://drive.google.com/uc?export=view&id=1MAs9HfrJTz95qMVFh3r2LZkE7wGO0XX_",
            "https://drive.google.com/uc?export=view&id=1VyVMuBgen3gjeCv2ZejJUm5Enn0AO-W5",
            "https://drive.google.com/uc?export=view&id=1JyLiHrDzp23263C3HRuI66BE1NxUvldf",
            "https://drive.google.com/uc?export=view&id=1_EyNqn3B4c0gvPqPXR2r0rPbo43jgS8-",
            "https://drive.google.com/uc?export=view&id=16FK4l2LEx8Fz9Ak6VCgvSMVbgd9vIcg0",
            "https://drive.google.com/uc?export=view&id=1Do3EuDxMoyrGxBi1_9C6jytlg70qMVG-",
            "https://drive.google.com/uc?export=view&id=1K7KVCMcRQee2ar-yZ7jRRBj7dacBnD6u",

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
                "kesan": "keren banget ketika liat prestasi bang fabio, jago ngoding pake R, gawul abang abangan sekjenn FG 2025 ini",
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
                "kesan": "kak tantyyyyyy, MC FG yang paling seru, orangnya hiperaktif dan energi nya kaya unlimitedd",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak, dan semoga aku jadi bisa lolos dan juara PIMNAS nanti yak, siapa tau keresahan dari balap bisa jadi temuan yang berguna"# 1
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "bang fadil orangnya baik banget dan ditengah berjuangan melawan sakitnya tapi tetap produktif dengan berbagai prestasi yang diperolehnya",
                "pesan": "Semoga almarhum/almarhumah mendapatkan tempat terbaik dan kedamaian abadi di sisi Tuhan Yang Maha Esa. Segala amal baik, bimbingan, dan ketulusannya semasa hidup akan selalu kami kenang. Semoga keluarga yang ditinggalkan diberikan kekuatan, ketabahan, dan keikhlasan"# 1
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis ",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "setelah kenal, ternyata bang nuel orangnya keren banget, suka sharing ilmu dan pendengar yang baik, gak nyesel bisa kenal bang nuel",
                "pesan": "Makasih banyak ilmunya bang, semoga hal baik selalu berdatangan, god bless."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12",
                "asal": "Bali",
                "alamat": "nusa peninda",
                "hobbi": "menghayal",
                "sosmed": "@violaadrtr_",
                "kesan": "kaka viola orangnya jujur seru bangett, dan energy nya positif juga kakak ini",
                "pesan": "Semoga apapun yang terjadi di dunia, tetep jadi S.SI.D nanti yakk, semangatt"# 1
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "kakak ini orangnya seru, baik hati, ramah, tidak sombong",
                "pesan": "Semoga tuhan selalu melancarkan urusan kak risa as always"# 1
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "1244500078",
                "umur": "19",
                "asal": "kepulauan riau",
                "alamat": "teluk betung",
                "hobbi": "nonton khw",
                "sosmed": "@vunnycaa",
                "kesan": "kakak ini yang ngajarin dugen jugak ini, orang yang support buat adik adiknya berkembang",
                "pesan": "Semoga sehat, sukses, hebat, mantap"# 1
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "kak yulia itu vibes nya positif, asik juga kalo diajak ngobrol",
                "pesan": "Semangat menginspirasinya ya kak, saya doakan kak dilancarkan kuliah dan organisasinya"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@keyashafi_",
                "kesan": "ngeliat bang keya selama ini, orangnya humoris level up, peduli sama sesama dan pembawaannya tenang, terutama waktu wwc kemarin",
                "pesan": "Sehat sehat terus ya bang, semoga selalu dikelilingi orang-orang baik, ditunggu cerita suksesnya karna kerja di Aussie"# 1
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara ",
                "alamat": "Pemda",
                "hobbi": "Sibuk",
                "sosmed": "@_els.a",
                "kesan": "kak elsa baik dan kakak ini jujur ADS alias Asik Dan Seru kalo diajak ngobrol",
                "pesan": "Semoga kedepannya kak diberi kemudahan dalam segala hal dan bisa mewujudkan semua impiannya, god bless"# 1
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "airan",
                "hobbi": "mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "kak fadya ternyata dari SMA yang sama dan terimakasih atas bantuan yang diberikan, baik banget",
                "pesan": "Semangat organisasinya ya kak, saya doakan kak dilancarkan kuliah dan organisasinya"# 1
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "SOBAT DUGENKUUUU, anjay dah orang ini ghawull mentok, jujur dengan kebaikannya, baik banget kakak ni",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak dan semoga musik yang di dengar Hannah Montana Rex Orang Country"# 1
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "kalianda",
                "alamat": "kota baru",
                "hobbi": "main game, tidur",
                "sosmed": "@aluccy_",
                "kesan": "jujur bang alsi ini respect each other, PS nya lumayan ngelawan dan gampang bikin suasana jadi cair, vibes nya positif",
                "pesan": "Keep strong bang, semoga makin banyak prestasinya"# 1
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal":"Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kak sherena orangnya gampang akrab dan murah senyum",
                "pesan": "Saya doakan semoga kak sherena selalu diberkati dan tetap jadi pribadi yang humble."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "ngeliat bang Razin selama ini, orangnya keren banget, nyambung diajak ngobrol apa aja, welcome sama siapapun dan baik, terutama waktu wwc dan nongkrong bareng",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga urusan akademis dan organisasinya lancar semua."
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel ",
                "sosmed": "@faizaanjanii",
                "kesan": "kakak OZT yang cocok untuk jadi role model, bisa meninspirasi banyak orang",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga bisa jadi juara mahasiswa berprestasi nantinya."
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Rajabasa Raya",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Setelah kenal, ternyata bang gathfan orangnya keren banget, gak pelit ilmu, rajin dan konsisten seru, pokoknya Gawul dah",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            },
{
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur ",
                "hobbi": "3N (Ngoding , Ngegame, Nyibukin Diri)",
                "sosmed": "@apiszzaja",
                "kesan": "mentor poisson sahabat baik yang keren, baik, dan PAPAAAAHH POISONNN ini seru banget orangnya",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus, semoga hobinya jadi 4N (Ngopi)"# 1
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Campang Raya, Sukabumi",
                "hobbi": "Gym, membaca, dan bermain",
                "sosmed": "@kelelep_comberan",
                "kesan": "dari pertama ketemu udah kerasa kalo bang kaleb kalo udah serius gharrr banget, suka sharing ilmu dan low profile, bikin aku makin semangat buat belajar",
                "pesan": "Semangat terus menginspirasi ya bang, semoga makin banyak prestasinya dan jadi astut baik hati"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal":"Sumatera Selatan ",
                "alamat": "Sukarame ",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "kakak ini seru banget, kak melva juga orangnya low profile, suka sharing ilmu",
                "pesan": "Tetap semangat belajarnya ya kak, semoga bisa lulus tepat waktu, inna ma'al usri yusra kak."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syafiqui",
                "kesan": "dari pertama ketemu udah kerasa kalo bang syafiq welcome sama siapapun, humble dan santai tapi tetep tanggung jawab, gokil MC C.U.I PPLK",
                "pesan": "Jangan lupa istirahat ya bang, semoga cepet lulus dan wisuda tepat waktu, hahay."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal":"Kotabumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "setelah kenal, ternyata bang henry orangnya gampang akrab, cara ngomongnya enak didenger, gak sombong sama sekali dan pembawaannya tenang, jadi contoh buat adek-adek, gacong pak ketang DATASENA",
                "pesan": "Jangan lupa istirahat ya bang, semoga cepet lulus dan wisuda tepat waktu, aamiin."
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1q76XBB0qnb4VGFBUlKyTmL_78rBQOper",
            "https://drive.google.com/uc?export=view&id=1W6vO6rBAGF4Im7-sT0vjoHN2rOR0LTwY",
            "https://drive.google.com/uc?export=view&id=1rPMr3ol_iBFxY7Vp_VaafwFRtO3_gOsr",
            "https://drive.google.com/uc?export=view&id=1CGGrdwvOQKxU4A1-AZTq2XI-3NQVm16R",
            "https://drive.google.com/uc?export=view&id=1uW6wcaxou3mYOYqb4jMAwn2gflMgdecE",
            "https://drive.google.com/uc?export=view&id=1lNgsmstj9-mar_SmoKj--dj0HDA_fhqE",
            "https://drive.google.com/uc?export=view&id=1D0E-X-pJbAPlwSOoaVuMlFkXE0ZrCdY5",
            "https://drive.google.com/uc?export=view&id=10I8BSkagFCsgRfGn40P4PJZcrQt1WHlD",
            "https://drive.google.com/uc?export=view&id=1b7mXXZaHjocvWUDoaGd3QDb5ond5Eya_",
            "https://drive.google.com/uc?export=view&id=1TtjSH0EHlXpk-QnTp2NtRc11a0jjKSkX",
            "https://drive.google.com/uc?export=view&id=1U46IoHZzxhzlz-1XgHZLA_HFuwXj3Rsv",
            "https://drive.google.com/uc?export=view&id=19upkoAtNqJ-3W9UbEmvFUh1SZpek7fU5",


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
                "kesan": "bang Ihsan, kalo saya yang manggil gitu tapi kalo abang abang lain manggilnya Lek Ku yang ikut ke bandung buat viscom jirr,",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus, dan ga beserak lagi perkara kucing di jalan pemda yang aspalnya SETARA ASPAL MONACO"# 1
            },
            {
                "nama": "hanifah inaya sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "kakaknya cantik, baik, humoris dan juga suka sharing pengalaman",
                "pesan": "Semangat buat kuliahnya, sampai lulus S.Si.D nanti terus kerja di MBU Group"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "kakaknya orangnya gampang akrab dan murah senyum",
                "pesan": "Semangat terus organisasinya kak, semoga kak sukses di mana pun beradas"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Bang hasan orangnya sangat sabar, baik, humble juga abang ini",
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
                "kesan": "kak Layina itu orangnya baik, welcome sama siapapun, low profile dan humoris juga",
                "pesan": "Semoga kedepannya kak Layina selalu diberkati dan dimudahkan segala urusannya "# 1
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "bang Iqbal itu gampang akrab, komunikatif juga, asik abang ini intinya",
                "pesan": "Semoga segala urusan akademis, organisasi, dan pas lulus semoga kerja di Telkom bang atau jadi PNS kan siapa tau"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "talljtine_",
                "kesan": "kak talitha orangnya suka sharing ilmu, nyambung diajak ngobrol apa aja, dan seruu juga kakak ini",
                "pesan": "Semoga apa yang kak talitha harapkan bisa terwujud, dan kak makin berkembang dan bersinar"# 1
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya cantik, seru kalo diajak ngobrol, humoris, dan juga asik",
                "pesan": "Semangat buat kuliahnya semoga cepat sidang dan uangnya diperbanyak buat jadi boss boss an"# 1
            },
            {
                "nama": "Abdilah Fikri Alpome",
                 "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "bang pome orangnya seru banget, baik dan ramahh banget, humoris juga abang abangan ini",
                "pesan": "Selamat melanjutkan aktivitas kuliah! Semoga bisa cepet SEMPRO, SEMHAS dan SIDANG dan semoga lulus PON basket"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "bang afdhal hobinya sangat seru buat lomba galatama",
                "pesan": "semoga mancingnya strike terus, dan infokan aja kalo ada galatama pake umpan aci"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "kakanya jujur humoris, ngobrol apa aja bisa nyambung",
                "pesan": "Semangat terus belajarnya kak anggun, semoga kak selalu dimudahkan kuliahnyaa"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "Semangat terus belajarnya kak, semoga kak selalu diberkati",
                "pesan": "Semoga kak della sukses di mana pun berada, dan tetap semangat organisasinya ya"# 1
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uuCTpUjJ4OCcoMJ5vsZ_PGj-IzYi2ZGA",
            "https://drive.google.com/uc?export=view&id=1eWy2-TmmiA2Pe6gWqU6FMsVcx9H9RHdk",
            "https://drive.google.com/uc?export=view&id=1l2_E67QwP2kzmpJ1z2iSP7wzhRhji0xV",
            "https://drive.google.com/uc?export=view&id=1h8Gpb6atADQmFW75T8yy5nvxyCZ8SSDx",
            "https://drive.google.com/uc?export=view&id=1JJ_X73qg-fw_3bCY5bEt32qUisuFyTTO",
            "https://drive.google.com/uc?export=view&id=1xUAfUJrJmsEz8VBBOiiwrspV1-JKUKgI",
            "https://drive.google.com/uc?export=view&id=1sYhwuH-1A50woUI6p3pNmI2CqNK-eoRg",
            "https://drive.google.com/uc?export=view&id=1pcreYSy07vF2HrFQN1eZcUwS3q79M3lm",
            "https://drive.google.com/uc?export=view&id=1WiO5d9Np-9xht4bR3TKm7IbBqJW1cEva",
            "https://drive.google.com/uc?export=view&id=1ym5katdzThCEykWsctbm37vy37YzRoxn",
            "https://drive.google.com/uc?export=view&id=1dO2qyKimlvEwcT-HA_ZhLVN0HiFtGbFV",
            "https://drive.google.com/uc?export=view&id=1K1cp3PP2rXNOsU29Vxc9nmepxfVzAqPO",
            "https://drive.google.com/uc?export=view&id=1p8xx-mNQctB6fskuL-Tt5QVQEooVx2C1",
            "https://drive.google.com/uc?export=view&id=1vnrGoqTlAZ5NMHK5Oa3lI_ro88lAWoWv",
            "https://drive.google.com/uc?export=view&id=1lsXYENEl_oVUIDxkM2hIa31YpJN0LH53",
            "https://drive.google.com/uc?export=view&id=1C9RQiUBY1O61RQNvgpRXh1f3MmDslmYG",
            "https://drive.google.com/uc?export=view&id=1MWTNtyKxesTD_RYigeWxaOI7_F8jsoZS",
            "https://drive.google.com/uc?export=view&id=1dPoN38eM8wuA_W9PFFASFI5mm18PAYk8",

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
                "kesan": "itu humble, ramah, dan punya cara bicara yang ada keunikannya sendiri",
                "pesan": "Semoga cepat sidang ya kak, semoga nanti dapat tawaran kerja jadi kartap di BRIN setelah lulus."# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "kakaktutor lmd yang goks banget, penjelasannya mudah dipahami karena pembawaannya yang santai",
                "pesan": "Semangat terus ya kakaaaa semester ini, semoga selalu dikelilingi hal baik dan semoga cepat sidang nanti"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu ",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran ",
                "sosmed": "@noerruuu",
                "kesan": "bang labo orangnya seru nih, jabodetabek connection abang ini memang, care juga",
                "pesan": "dikit lagi wisuda bang, ntar kerja di SCBD aja bang, bangganya seumur hidup. Semangat!"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Way Halim ",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "kakanya cantik dan cute, seru juga kalo diajak ngobrol dan humoris juga kakak ini",
                "pesan": "Selamat melanjutkan semester 5 ini kak, semoga segala tugas dan praktikumnya selalu membuat ka tasya senang."
            },
            {
                "nama": "Felisya Nabila Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal": "Lampung Timur ",
                "alamat": "Kota Baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "kakan ini orangnya kreatif, seru, punya gaya bicara yang khas",
                "pesan": "Tetap semangat berkarya ya kak, semoga diberi kesehatan dan keberkahan."# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "21",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "bang razan orangnnya seru, abang-abangan tensor juga ini, badmintonnya lumayan ngelawan",
                "pesan": "semangat bang perantau, nanti pulang semester kalo balik kanan bekasi barengan lagi aja bang, semangat trus"# 1
            },
            {
                "nama": "Sania DWi Ayu Lestari",
                "nim": "124450086",
                "umur": "21",
                "asal": "Karawang ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "pertama kali liat waktu verbek 25 dan kakak ini juga pertama kenal di DAMASKUS juga",
                "pesan": "Semoga apa yang kak harapkan bisa terwujud, dan kak bisa lulus tepat waktu nanti."# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "kakanya cantik dan cute, pemain snare paling kece DAMASKUS",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus dan tetap menjadi Kesatria DAMASKUS sejati"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "kak alya orangnya rajin dan jadi pendengar yang baik, humble",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus S.SI.D."# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "kakaaa NIM juga ini, orang yang awal kenal karena 'siapa nim 97' dan humoris juga kakak ini",
                "pesan": "Semoga apa yang disemogakan bisa tersemogakan sesuai apa yang disemogakan sejak awal hal itu disemogakan yakkk kakak nim"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Alquran",
                "sosmed": "@difanyhsa_",
                "kesan": "kakak ini ya, orangnya itu seru kalo diajak ngobrol, fotonya juga bagus bagus, dan gawul",
                "pesan": "Semoga segala urusan di dunia, itu dilancarkan dan semoga senang."# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@nzlhauly_",
                "kesan": "kakanya seru, badminton nya ngelawan, kakak kakak tensor juga ini",
                "pesan": "Semoga berenangnya makin jago biar bisa ngelawan ronaldo berenang nanti."# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Aira Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "kakanya cantik, itu kreatif, orangnya sangat berkesan dan low profile",
                "pesan": "Semoga semangat terus terjaga, selalu diberikan kesehatan kak, semoga makin banyak prestasinya."# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame ",
                "hobbi": "-",
                "sosmed": "@daffascript",
                "kesan": "bang daffa ni orangnya aktif, humoris, seru juga abang ini, dan abang ini juga low profile ini",
                "pesan": "bang kuliahnya semangat yak, ntar belajar design juga dari bang dapa ini"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "bang edsel orangnya seru kalau diajak ngobrol, lumayan seru juga bang edsel ini",
                "pesan": "semangat terus kuliahnya dan semoga apapun yang diinginkan bisa tercapai yakk"# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "kakak ini orangnya welcome sama siapapun, seru, respect each other dan low profile",
                "pesan": "Semangat terus menjalani harinya kak, semoga kak selalu sehat dan bahagia."
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis dan menulis",
                "sosmed": "@_shaazzh",
                "kesan": "kakanya, ramah, bisa jadi pendengar yang baik, dan komunikatif",
                "pesan": "Semangat menggapai mimpinya ya kak, saya doakan kak cepat meraih cita-citanya."# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "kakak zannuba orangnya rendah hati, tidak sombong, dan juga respect each other",
                "pesan": "Keep setronx kak, semoga kak bisa mewujudkan semua impiannya dan dipermudah untuk S.SI.D kaks."
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
# Tambahkan menu lainnya sesuai kebutuhan
