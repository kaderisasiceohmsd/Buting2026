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
            "https://drive.google.com/uc?export=view&id=1xGPANYdh1va2y4_fUP0WdBnA1xDfB2Xb",
            "https://drive.google.com/uc?export=view&id=1CZuWR8cgBUVwATr1WrMIpsUfXDrh3N4b",
            "https://drive.google.com/uc?export=view&id=1rGKMfosDCQltl41Sz2ehjEUQV3LAaw8K",
            "https://drive.google.com/uc?export=view&id=1A9_GD_ng31Z0eTg1uvrwEUQFq-K-b4dL",
            "https://drive.google.com/uc?export=view&id=1fTovPjdfQCSGBXSg_viryFMm8yWEVGvc",
            "https://drive.google.com/uc?export=view&id=1bDcokqXsfus5IqecUG12RU9PS4ISZn4F",
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
                "pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bangkinam",
                "alamat": "Sekretariatan HMSD",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil orangnya asik dan ramah, penjelasannya juga mudah dipahami, jadi saya bisa lebih mengenal apa itu Kesekjenan.",  
                "pesan":"Semoga ke depannya selalu dilancarkan segala urusannya dan sukses terus, Bang!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi orangnya ramah dan baik, penjelasannya juga menambah wawasan saya tentang apa itu peran dan tugas dari Sekretaris.",  
                "pesan":"Semoga ke depannya selalu diberikan kelancaran dan bisa terus menjadi inspirasi bagi orang-orang di sekitarnya, Kak!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois orangnya soft gituu, keknya memang suka banget jadi sekre, dari bang qois saya jadi mengenal apa aja tugas dan peran dari sekretaris.",  
                "pesan":"Semoga kedepannya selalu diberikan kesehatan, kebahagiaan, dan kesuksesan. Semangat terus, ya baang!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa orangnya humble, dan seru banget , setiap penjelasan yang kakak berikan itu mudah di pahami",  
                "pesan":"Semoga kedepannya kak Hafsa selalu diberi kelancaran dalam segala hal, dan kesehatan ,terimakasih Kak!!"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak Luthfia orangnya lucu banget, aktif, dan seruu, jadi yang disampaikan oleh kak lutfhia mudah dipahami.",  
                "pesan":"Semoga kedepannya kakak diberikan kelancaran dalam menjalankan amanahnya. Semangat terus, Kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Y49NnwlsJgchox-dpAJ_oLGvCRVAKFny",
            "https://drive.google.com/uc?export=view&id=16930zRdf_dMA0Ypql4JHUAELHfN-RWd3",
            "https://drive.google.com/uc?export=view&id=1J7xzHS9TsMFtkhEE03EHuatKGs_5wMpI",
            "https://drive.google.com/uc?export=view&id=1CxT72HLkJ0nW_Bfna0MnoCstRvd2c1WS",
            "https://drive.google.com/uc?export=view&id=1_qgv0owpNP54PdE7Ig-_pV87dlFOaXCD",
            "https://drive.google.com/uc?export=view&id=1mHdZPK_B2QsTuNkAd9KyhztiYe_ZZPtJ",#bang givaro
            "https://drive.google.com/uc?export=view&id=1J4LYA1wkvGzxChY91Ycb9gViQ7dwkHnv",#kak nisa
            "https://drive.google.com/uc?export=view&id=12CQfaIZvka8FgAkJSjjt5bae_EDJhFEY",#kak hani
            "https://drive.google.com/uc?export=view&id=1kgGtDVpPBXi5zOC0Hxi01HeF7G3mgYvV",
            "https://drive.google.com/uc?export=view&id=1YfSz_QrQjcxUaSEn6_3_jjIc2swixEhg",
            "https://drive.google.com/uc?export=view&id=1BE4KMXJSuumEBg3HBV0IEpA5LuzYlmMO",
            "https://drive.google.com/uc?export=view&id=10J3lvqECDicycNBgosiYgYwBgIn0dZUY",
            "https://drive.google.com/uc?export=view&id=1g9zaiv_IYHB-1F64f9v0cengjHXZ_p0I",

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
                "kesan": "Bang Ridho orangnya asik banget, to the point dan penjelasan yang di kasih mudah dipahami",  
                "pesan":"Semoga kedepannya abang selalu diberi kelancaran dalam segala hal , dan diberi kesehatan, terimakasih bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue orangnyaaa asik banget, lucuu, penyampaian tentang Balegnya juga mudah dipahami",  
                "pesan":"Semoga Kedepannya kak jue selalu diberi kelancaran dalam segala hal, dan juga selalu diberikan kesehatan, Terimakasih kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya asik banget, vibes-nya bikin betah belajar. Kalau ngajarin jangan bosen-bosen ya, Bang, soalnya ilmu dari bang dharu masih banyak yang mau fadyl serap,wkwkkwk.",
                "pesan": "Semangat terus kuliahnya, Bang! Semoga tugas lancar, nilai aman, dan rezeki mengalir deras. Jangan lupa bahagia bang!"
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Mikael orangnya humble dan asik, auranya presidiumnya kenceng banget.",
                "pesan": "Semoga kuliahnya lancar terus, dan semoga diberi kesehatan dan kelancaran dalam segala hal ya Bang! "
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kakaknya baik dan seru, jujur syok pas tau kakaknya orang palembang jugaa.",
                "pesan": "Semoga kuliahnya lancar terus, Kak! Semoga nanti saya bisa nyicip pempek buatan kakak :)"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro orangnya asik, penjelasan yang bang givaro kasih jujur mudah banget dipahami",
                "pesan": "Semoga kuliahnya lancar, Bang! Semoga kopinya selalu enak, dompetnya selalu aman, dan hidupnya jauh dari deadline dadakan."
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa orangnya baik, humble, kenal kak nisa udah dari semester satu, kak nisa orangnya sangat sangat bertanggung jawab.",  
                "pesan":"Semoga kedepannya kak nisa selalu diberikan kelancaran dalam segala hal ya kak"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya asik dan ramah. keliatan soft spoken banget",  
                "pesan":"Semoga kedepannya kak hani selalu diberi kesehatan dan kelancaran dalam segala hal yaa kak ."# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremia orangnya asik, dan humble parah.",  
                "pesan":"Semoga Kedepannya Abang selalu diberikan kelancaran dan Kesehatan ya bang."# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica orangnya murah senyum, baik dan lucu",  
                "pesan":"semangat terus kuliahnya kakak, semoga sehat selaluuu"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jona orangnya lucu paraaah, seruuu, dan juga suka sharing biskuat kalau abangnya lagi jadi operator.",  
                "pesan":"semangat terus kuliahnya bang, sehat selaluuu ya bang, SUKSEEES !!!"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Sekar orangnya baik banget, humble, dan tegas, tapi perhatian",  
                "pesan":"semangat terus kuliahnya kak, dan sehat selaluu ya kak."# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya seruuu asik dan humbleee banget.",  
                "pesan":"semangat terus kuliahnya kak, dan sehat selaluu ya kak."# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ouaPh_WXCa7L4UaB1zjcpW1GtpU4chkg",
            "https://drive.google.com/uc?export=view&id=1e3PpoxaPTy4Wbz0LRtD53S3C8y5R92gV",
            "https://drive.google.com/uc?export=view&id=1PcF4IYKT6uaflaYDQqiP2iUqzi5sfcQK",
            "https://drive.google.com/uc?export=view&id=1D_lia9zgl7mJ2WnrFajpgbxFc_bl7hwB",
            "https://drive.google.com/uc?export=view&id=1T0pBCaOoUGWePzplk23vzKIA_inZGs5S",
            "https://drive.google.com/uc?export=view&id=1G7ILhw5Jw6OGFqR9JZXXGl6_ZH8q7EUk",
            "https://drive.google.com/uc?export=view&id=1dEarZTBT7jEC24kqQ9Lm2zPTdGr3ZkJ9",
            "https://drive.google.com/uc?export=view&id=1Q0bzo7yr0D8xh-RSlxK5cYCg8wEstMh3",
            "https://drive.google.com/uc?export=view&id=1LFx7gMEf7keEm0HQUrqGsR_UfOJuqT8l",
            "https://drive.google.com/uc?export=view&id=1AnZyWjeehYZsmuiiUFgjlISXfiyn_DJI",
            "https://drive.google.com/uc?export=view&id=1cifStK5BxXbvoLmLc9fnqt_K5X2dOXHZ",
            "https://drive.google.com/uc?export=view&id=1-J_1seNxOKN-f5IbBCnSW9iLuwLis6hb",
            "https://drive.google.com/uc?export=view&id=1ccwodwWoFNGo-INHooISJQFw4TZXsDba",
            "https://drive.google.com/uc?export=view&id=1a7KIM--DVa1kPGydGNACbTyLa8tqJtlD",

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
                "kesan": "Bang Kevin orangnya asik dan lucuu parah.",  
                "pesan":"Semangat terus kuliahnya bangg, dan sehat selalu ya bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kak Ferazka orangnya lucuuu parah, dan selalu ngajakin muncak.",  
                "pesan":"semangat terus kuliahnya ya kak, dan semoga kita bisa muncak kak!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Bang Ali orangnya baik, seru dan soft spoken.",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kak Ayu orangnya baik dan humble parah",  
                "pesan":"semangat terus kuliahnnya kak!!"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Dafa orangnya baik dan asik banget.",  
                "pesan":"Semangat terus ya bang kuliahnya, dan sehat selalu ya bang, terimakasih bang"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kak nazwa orangnya baik dan soft spoken banget.",  
                "pesan":"Semoga kedepannya kakak diberi kelancaran dalam segala hal."# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Bang afdal orangnya lucu dan seruuu banget.",  
                "pesan":"Semangat terus ya bang kuliahnya, dan sehat selalu yaa bang"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak juwita orangnya lucu dan baik bangett",  
                "pesan":"Semoga kedepannya kakak diberi kelancaran dalam segala hal."# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang ridwan orangnya asik dan seru banget, my mentor badminton",  
                "pesan":"semangat terus kuliahnya ya bang !!!"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "BAng andra orangnya lucuu dan seruuu banget",  
                "pesan":"semangat terus kuliahnya yaa bang !!!"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang Bryan orangnya soft spoken dan humble banget",  
                "pesan":"semangat terus kuliahnya ya bangg !!!"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak indah orangnya asik dan baik bangetttt",  
                "pesan":"semangat terus kuliahnya yaa kak!!!"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Bang rafka orangnya baik dan humble banget",  
                "pesan":"semangat terus kuliahnya Bang !!!"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450089",
                "umur": "17",
                "asal":"Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Bang ghiyats orangnya lucu dan humble parah",  
                "pesan":"Semangattt bang bangg jadi pj game nyaaa hihi"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bT1YM9F8WpmBeKP4Yx8pDr8zcCRV14MW",
            "https://drive.google.com/uc?export=view&id=1-FVJcb8_s8YJkq0HkBEhFPGBGQ8xiFub",
            "https://drive.google.com/uc?export=view&id=1F1tFv0fBId9--MGUNvmwrk5nhXVnyuV6",
            "https://drive.google.com/uc?export=view&id=1zBjX3AOuFcsYpyC7OmsMrS_DNRdHPn4v",
            "https://drive.google.com/uc?export=view&id=1ylTjx1jMS2BJyV8LyAIq6eVG9LCLmIg_",
            "https://drive.google.com/uc?export=view&id=1pKnivmS6dH15FFVn3Z9JcJ5QKrtPWTUQ",
            "https://drive.google.com/uc?export=view&id=1TmY6If5h8WyzZgC4llSji1hBn3fSMw97",
            "https://drive.google.com/uc?export=view&id=1LDCbYlttrvSsD_S2r_hAZx67wIvmFvaG",
            "https://drive.google.com/uc?export=view&id=1I0nKh6on9ACRXN2C8OKNB9jwZ3m7E6C_",
            "https://drive.google.com/uc?export=view&id=1d6gIZBL2tLcrKL1BQ0NCLhy2qPRBe8Vj",
            "https://drive.google.com/uc?export=view&id=1bf3h2uGnF2fGb0lhUeMY0ye1DAjut1yh",
            "https://drive.google.com/uc?export=view&id=1myaxcbsKW-_umtwNqzj6bMQAZZVAkQvQ",
            "https://drive.google.com/uc?export=view&id=1GrntdlPBAPoSx_avKHNYakeCVVZ81xml",
            "https://drive.google.com/uc?export=view&id=1wMtEtv90vd06zGpKYmxp-IyF8ANCDEc5",
            "https://drive.google.com/uc?export=view&id=1Cb7ZhFT1e5XbQw6eTcp6to0qdLB_UcKx",
            "https://drive.google.com/uc?export=view&id=1A9W8r_xJLH7wRQZZ9L1356eXscr3a0_4",

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
                "kesan": "Bang haikal orangnya seruu banget.",  
                "pesan":"Semoga kedepannya bang haikal diberi kelancaran dalam segala hal."# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma lucuu, baikk, dan juga ramah paraaah",  
                "pesan":"Semoga kak kharisma selalu dikelilingi dengan orang baik"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna seru, baikk, lucu ",  
                "pesan":"Semoga semua yang kak hanna inginkan semuanyaa tercapaii, aamiin"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan orangnya keren, selalu keren pas damaskus",  
                "pesan":"Semoga bang farhan selalu diberi kelancaran dan kesehatan"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak Aisyah orangnya lucuuu, dan juga asikkk sekali",  
                "pesan":"Semoga semua apa yang kakak lakuin sekarang dan nanti diberi kelancaran"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipnyb",
                "kesan": "Kak Cerine orangnya sangat asikk, humble, dan juga baikk banget",  
                "pesan":"Semoga kak cerine selalu dikelilingi orang orang baikk"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya orangnya keren, baikk, dan seru",  
                "pesan":"Semoga bang jaya diberi kesehatan dan kelancaran dalam segala hal!"
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kak Najla orangnya baikk, dan juga ramah sekalii",  
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
                "kesan": "Bang Rozak orangnya asik sihh, dan juga murah senyuum",  
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
                "kesan": "Kak Teresa orangnya lucuu, baikk, dan juga ramahh",  
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
                "kesan": "Bang Hanif orangnya baikk, dan juga asikk",  
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
                "kesan": "Kak orangnya Audina lucuu, baikk, dan juga sangat amat ramah",  
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
                "kesan": "Kak Cika orangnya lucuu, baikk, dan juga asikk",  
                "pesan":"Semoga semua keinginan kak cika tercapai secepatnyaaa"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kak Gustin orangnya lucuu, baikk, dan juga ramahh",  
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
                "kesan": "Bang Harvin orangnya baiikk , dan soft spoken",  
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
                "kesan": "Kak Sabina orangnya baikk, dan juga sangat ramahh",  
                "pesan":"Semoga kak sabina mendapatkan hal-hal baik teruss"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lIzS74rle4qjVfzhxdgfVNIKjlmETJ_s",
            "https://drive.google.com/uc?export=view&id=1xJ5HsRnxSw74bwoTl2KkIo3MYDerSn4j",
            "https://drive.google.com/uc?export=view&id=13AfDTj6E-wTS76FLp7ZBj42t76KHOfaf",
            "https://drive.google.com/uc?export=view&id=1yGnS0XAtp0dOuYf8nylWcI1eskKpiW6l",
            "https://drive.google.com/uc?export=view&id=1ZytisXJYU7txYU1J7qoPI6VkBDyC4dVX",
            "https://drive.google.com/uc?export=view&id=1R325O4wtuzavloL9bwjUXHE8O7GsMimK",
            "https://drive.google.com/uc?export=view&id=1bb9jPqQ_FlNDOV60Y6s29AT6j9qBBPMi",
            "https://drive.google.com/uc?export=view&id=1wYC5zY_lTSJqO36bauZT9eTvWzy9Fpvg",
            "https://drive.google.com/uc?export=view&id=1BV5lebBanBUnVvrISrfbznmwjOytmPvD",
            "https://drive.google.com/uc?export=view&id=1s2s0fYbCVIpmV7V-9wazL4iS5EeMyn4c",
            "https://drive.google.com/uc?export=view&id=1f5nhmESP5YRRftXYsj8II0EXNMO0NddK",
            "https://drive.google.com/uc?export=view&id=1SoEbXjn1veyzIeor7bXY4zSyFuHF0fUG",
            "https://drive.google.com/uc?export=view&id=1c2c9ZL2C1It7269sQCry1Femrj9WOzf7",
            "https://drive.google.com/uc?export=view&id=1nint9s3ptTAPbJhWEhUJFwCbQkUhD0rZ",
            "https://drive.google.com/uc?export=view&id=1PpXAW5E9hjFsi2qqzt65QVCG2R1KXhTO",
            "https://drive.google.com/uc?export=view&id=1AtP5O1H1g5KF9SKEO0e91kamQFccayyn",
            "https://drive.google.com/uc?export=view&id=1d68jdST1atxpWas85Rr4Ii6F3bp0uxhu",
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
                "kesan": "Kak Arienta orangnya baik, dan juga ramahh",  
                "pesan":"Semoga semua keinginan kak arienta sgera tercapai"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany orangnya humble, dan baik juga",  
                "pesan":"Semoga kak vany mencapai semua keinginannya secepatnya, salam dari orang sesama palembang"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel orangnya kerenn, Tegas,dan juga baiik",  
                "pesan":"Semoga bang nobel selalu diberi kelancaran dan kesehatan dalam segala hal."# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi orangnya kerenn, to the point dan juga baikk",  
                "pesan":"Semoga semua keinginan bang azmi cepat tercapaii"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang Ayake orangnyaa humble , kerenn, Tegas dan baikk",  
                "pesan":"Semoga bang ayake diberi kelancaran dalam segala hal dan semoga selalu diberi kesehatan"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar orangnya kereen, Tegas dan Humble",  
                "pesan":"Semoga bang caesar diberi kesehatan dan kelancaran"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Euodia orangnya seru, Tegas , dan juga baikk,",  
                "pesan":"Semoga kak euodia selalu didekatkan hal-hal baikk"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal orangnya kerenn, Tegas ,baikk, dan juga ramahh",  
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
                "kesan": "Kak Putri orangnya baikk, humble dan juga ramah",  
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
                "kesan": "Kak Queenta orangnya baik, humble, dan perhatian",  
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
                "kesan": "Bang Desman orangnya kerenn, dan juga asikk, baikk",  
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
                "kesan": "Kak Azzel orangnya humble, dan juga baikkk sekali",  
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
                "kesan": "Kak Charrlindah orangnya baikk, dan juga ramah",  
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
                "kesan": "Bang Jemar orangnya kerenn apalagi saat damaskus",  
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
                "kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa",  
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
                "kesan": "Bang Rafli orangnya humble , baik, dan juga ramah",  
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
                "kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh",  
                "pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18XGMyQrBVBcRMS2t-0YbdBiAkuFPJ96F",
            "https://drive.google.com/uc?export=view&id=13XFeNvSAJKcaFybye9asPTXqjVEkGBuM",
            "https://drive.google.com/uc?export=view&id=19vayTHJsT_iU1XfXLa5zmWC18uHXRW_n",
            "https://drive.google.com/uc?export=view&id=1568Y-2vFCZ7B4JqStbA_Q_h2mm3BaLn5",
            "https://drive.google.com/uc?export=view&id=1bQ3F_-3C7J-FJxEPlAWI560RnqfkaM0i",
            "https://drive.google.com/uc?export=view&id=1g2CSnwE4uMopBpRDVPP1-WqYFnjTqOqu",
            "https://drive.google.com/uc?export=view&id=1mWP_GSJdbXldrIcztKQ61vUAADsNK7sA",
            "https://drive.google.com/uc?export=view&id=1J3NZPNiwvtONp-jeZoxaqk_VU_Ze9tUu",
            "https://drive.google.com/uc?export=view&id=1RuVycp-3l9Tu95UzS1uKGhtZSHed5jaN",
            "https://drive.google.com/thumbnail?id=1L0EehavONuNd07vhvv2ezQTZt7CZ5KLY&sz=w1000",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah, orangnya seru dan baik banget.",  
                "pesan":"Semoga kak Fathinah selalu diberi kelancaran dalam mengemban tugas menjadi Senat KM-ITERA, Semangat terus kak."# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak Nadya orangnya baik bangeet, soft spoken dan seneng aja kalau berinteraksi dengan kakak",  
                "pesan":"Semoga kak Nadya selalu diberi kelancaran dalam segala hal, dan selalu diberi kesehatan."# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kak Dwi orangnya seru dan baik banget.",  
                "pesan":"Semoga apa yang kakak impikan dan kakak harapkan bisa segera tercapai. Terimakasih kak"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen Kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Bang Helmy orangnya lucu bangett, dan seruu abis. #salammelet",  
                "pesan":"Semoga bang helmy selalu diberi kelancaran dalam segala hal , Terimakasih ya bang"
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tanggerang Kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Bang Nando orangnya baik dan humble banget.",  
                "pesan":"Semoga bang nando selalu dikasih kesehatan dan kelancaran dalam segala hal. Terimakasih ya bang."# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Kota Baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia__",
                "kesan": "Kak Suci orangnya seruu, dan lucuuu.",  
                "pesan":"Semoga kakak selalu diberi kelancaran dalam segala hal yang kakak laluin, semangat teruuus ya kak."# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Bang Wielman orangnya baik bangeeet, dan humblee paraaah.",  
                "pesan":"Semoga bang wielman selalu diberi kesehatan dan kemudahan dalam segala kondisi, semangat terus ya bangg."
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jaarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Hana orangnya baik bangett, dan murah senyuum.",  
                "pesan":"Semangat teruss ya kak, dan semoga kakak selalu diberi kemudahan disetiap hal yang kakak lakuin"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "18",
                "asal":"lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kak Aqila orangnyaa aktif paraah, lucu, dan seruu abiss",  
                "pesan":"Semoga kak qila selalu diberi kemudahan dan kelancaran dalam segala hal. Semangat teruuus yaa kak."# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "Giring Ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Bang Hazel orangnya kereen banget, dengan rambutnya yang badai ituu, jujur saya pengen punya style kek abang, cuman keknya ga cocok deh sama saya.",  
                "pesan":"Semoga abang selalu diberi kesehatan dan kemudahan dalam segala hal. Semangat terus dan selalu beri dampak kepada orang sekitar yaa bang."# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_cyOHyY31GeJwpRUtwc1DWQHUU8Dr-xS",# kak arini
            "https://drive.google.com/uc?export=view&id=1jEQi0LH_QXm0MHisZG5UlDNOfs8gCQZ-",# kak nabyla
            "https://drive.google.com/uc?export=view&id=1DxpczGFV49JgWBMdngMITPLbkhllpM7H",# bang adit
            "https://drive.google.com/uc?export=view&id=1llwK9MkB0OTIohN2epeiwP-nkhN2CRXD",# kak Fathya
            "https://drive.google.com/uc?export=view&id=1z2QLDRXlAah54-a1rAw1omha4Fvdbhkr",# kak tarisa
            "https://drive.google.com/uc?export=view&id=1tlBcO0viJsMWll0WHUkqhH-xWO36jjN8",# kak selma
            "https://drive.google.com/uc?export=view&id=1A-59nJZsZN7inMHZz77DPkuH5AWNpafx",# kak ashila
            "https://drive.google.com/uc?export=view&id=1RqN2-gVcB1PLeQmmjAmZdtJAsznXGQYX",# bang danil
            "https://drive.google.com/uc?export=view&id=1_pLinNjx0oEvzSXcKCPX6icGUMwZB8Nh",# bang vian
            "https://drive.google.com/uc?export=view&id=1qPP9iWoZyUVWtokUSgZAPvlxdz7sE9KX",# bang yazid
            "https://drive.google.com/uc?export=view&id=1dxxVTTSsGPJKeAPJdb5HWHfg9ZSHP-yV",# bang zaldi
            "https://drive.google.com/uc?export=view&id=1pYGY62ILM-kHTKeFWxaYRGsKkqax6pBx",# kak saskia
            "https://drive.google.com/uc?export=view&id=1DYFb6QniZUbew9k3ida7lpuMpHNSMun4",# kak muthoharoh
            "https://drive.google.com/uc?export=view&id=1FKh9MgzcUgYbgeCaHsNgj6o483fcC--a",# bang ahmad
            "https://drive.google.com/uc?export=view&id=1UsKX5Cwd8AGLNi2mDyzWpLYMZswAfd78",# bang bima
            "https://drive.google.com/uc?export=view&id=1VtRJZYHrFhhZZnr1zymQGYu49I84hV25",# bang bimo
            "https://drive.google.com/uc?export=view&id=1M5LmUSTnZxMWZiavhl9DPB_VKMEJ2R6_",# kak adinda
            "https://drive.google.com/uc?export=view&id=1j_xu_IT3v7S2sPKrfUnoz3euruxj7SJJ",# kak yolanda
            "https://drive.google.com/uc?export=view&id=1blH-Rlxsop7-lAZ_tfelHqiU2jOLgEfc",# kak riska
            "https://drive.google.com/uc?export=view&id=16n6dQcEH32MfNuQX90DubzXa0X3n-kc5",# bang alfaya
            "https://drive.google.com/uc?export=view&id=1TSO5KESSkVl183rFUzvC1lgHMF87U5vR",# kak asri
            "https://drive.google.com/uc?export=view&id=1jsPQXFHOQbRm1YBWKB-AGDcv3oycME2p",

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
                "kesan": "Kak Arini orangnya baik bangett dan murah senyum",
                "pesan": "Semoga kakak selalu diberi kelancaran dan kesehatan dalam segala hal. Terimakasih Kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla orangnya baik bangeet, dan humble.",
                "pesan": "Semoga semua hal baik selalu menyertai kakak dan sukses terus untuk ke depannya. Sehat selalu ya, Kak."# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "Bang Adit orangnya asik banget, seru, dan selalu bikin suasana jadi rame",
                "pesan": "Semoga semua urusan abang selalu dimudahkan dan apa yang dicita-citakan bisa tercapai. Sehat dan bahagia selalu, Bang"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya orangnya seru bangett dan punya pembawaan yang menyenangkan. Senang banget bisa kenal Kakak..",
                "pesan":"Semoga kakak nselalu sehat, dan dilancarkan semua urusannya. Bahagia selalu ya, Kak"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "-",
                "asal": "Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kak Tarisya orangnya ramah buangeeet dan bikin nyaman kalau diajak ngobrol, maaf ya kak kalau saya suka merepotkan pas praktikum, hehehe.",
                "pesan": "Semoga kakak selalu dikelilingi oleh orang-orang baik dan dilancarkan semua kegiatan yang kakak jalanii. Sehat selalu ya, Kak"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kak Selma orangnya baik banget, ramah, dan seru abis",
                "pesan": "Semoga kakak selalu diberi kelancaran dalam segala hal. Bahagia dan sukses selalu ya, Kak"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "sini",
                "alamat": "jauh pokoknya",
                "hobbi": "tidur",
                "sosmed": "@kshigf",
                "kesan": "Kak Shila orangnya asik bangeeet, murah senyum, dan ramah sama semua orang",
                "pesan": "Semoga semua impian kakak bisa tercapai dan selalu ada hal baik di setiap harinya. Makasih ya, Kak"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Bang Danil ini orangnya kereeen parah, beprestasi, dan sangat humblee, salam NIM 103 bang.",
                "pesan": "Semoga abang makin sukses dan semua yang diusahakan bisa tercapai. Semangaat selalu ya baang."# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Way Halim",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Bang Vian orangnya LUCUUUU ABIZZ, humbleee, dan sangat perhatiaaan, #GGMU bang",
                "pesan": "Semoga abang selalu diberi kebahagiaan dan kesuksesan dalam apa pun yang abang kerjakan. Makasih banyak, Bang"# 1
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Bang Yazid orangnya baik banget dan asik diajak ngobrol. Pokoknya seru abis.",
                "pesan": "Semoga abang selalu diberikan kemudahan dalam setiap langkah dan selalu diberi kesehatan. Semangat terus, yaaa bang"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah ",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "Ga bales chat",
                "sosmed": "@jaldii._",
                "kesan": "Bang Zaldi orangnya punya selera humor yang bikin suasana jadi lebih hidup, intinya seru bangeet kalau deket bang zaldi.",
                "pesan": "Semoga abang selalu diberi kelancaran dan kesehatan dalam segala hal. sukses terus ya bang"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kak Saskia orangnya lucuu dan muraah senyum.",
                "pesan": "Semoga kakak selalu diberi kesehatan dan kelancaran dalam segala hal. Semangat dan sukses selalu kak"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak Mut pembawaannya tenang banget, ngomongnya lembut, tapi ternyata pinter banget. Keren abizz",
                "pesan": "Semangaat ya kak buat PIMNAS nya, semoga bisa mendapatkan hasil terbaik, sekali lagi semangat kak."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang Ahmad tipe orang yang berani banget buat bersuara, punya kepedulian tinggi, dan nggak tinggal diam melihat sesuatu yang perlu diperjuangkan. Salut saya bang!",
                "pesan":"Semoga setiap langkah abang dalam memperjuangkan aspirasi bisa memberikan dampak positif bagi banyak orang. Sukses selalu, Bang"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kak Indah orangnya kelihatannya kalem, tetapi punya sisi seru yang bikin makin asik kalau kenal lebih dekat",
                "pesan": "Semoga kakak selalu sehat dan semangaaat dalam menjalani hari-hari kakak."# 1
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung ",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Bang Bima orangnya asiik, dan humble paraah",
                "pesan":"Semoga abang selalu diberi kemudahan dan kelancaran dalam setiap hal yang abang lakukan."
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus ",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Bang Bimo orangnya keliatan dewasa bangeet, kek soft boy gituu, dan juga bang bimo orangnya humble parah.",
                "pesan":"Semoga abang selalu diberi kemudahan dan kelancaran dalam setiap langkah yang abang jalani."
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "21",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kak Adinda orangnya keliatan kaleem, baik dan murah senyuum.",
                "pesan": "Semoga kakak selalu diberi kelancaran dan kemudahan dalam setiap hal yang kakak lakuin, semangat ya kak."# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "21",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Nyari Duit",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kak yolandaa orangnyaa aktif bangeet, dan oarangnya humble paraah",
                "pesan":"Semoga kakak diberi kelancaran dan kemudahan dalam segala hal, semangat terus ya kak."
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Jujur, awalnya saya kira Kak ipin orangnya cuek banget, ternyata setelah kenal lebih jauh, Kak ipiiin ituu baikkkk bangettt, perhatian, dan sayang banget sama kami. Kakak bukan cuma jadi mentor, tapi juga jadi sosok yang selalu berusaha ada buat Tensor. Bahkan rela meluangkan waktu buat nemenin kami kerkom, padahal Kakak juga pasti punya kesibukan sendiri. Dari situ saya sadar kalau di balik kesan cuek kakak di awal, ternyata ada hati yang tulus banget buat membersamai kami. Senang banget bisa kenal sama kak ipin dan jadi bagian dari kelompok Tensor",
                "pesan": "Terima kasih banyak ya, Kak, sudah sabar menghadapi kami, meluangkan waktu, memberikan perhatian, dan selalu berusaha membersamai kami sampai sejauh ini. Mungkin buat Kak ipin, hal-hal yang Kakak lakukan terlihat sederhana, tapi buat dyla, itu berarti lebih dari yang Kakak bayangkan. Semoga semua kebaikan yang Kakak berikan ke kami bisa kembali ke Kakak berkali-kali lipat. Semoga Kakak selalu diberi kesehatan, kebahagiaan, dan kemudahan dalam setiap langkahnya. Jangan terlalu keras sama diri sendiri ya, Kak, karena Kakak juga pantas mendapatkan perhatian dan kasih sayang sebesar yang Kakak berikan ke orang lain. Semoga segala hal baik yang sedang Kakak perjuangkan bisa tercapai. Sekali lagi, terima kasih sudah menjadi mentor yang bukan cuma membimbing, tapi juga menyayangi kami dengan tulus. Sayang banyak-banyak buat Kakak!"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Bang Alfaya orangnya ramah bangeet dan nggak bikin canggung saat pertama kali ketemu",
                "pesan": "Semoga abang makin berkembang, makin sukses, dan selalu bahagia dengan apa yang abang jalani"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kak Mei orangnya lucuuu banget, seruuu, dan humble paraah.",
                "pesan": "Semoga kakak selalu diberikan kesehatan, kelancaran rezeki, dan kesuksesan dalam apa pun yang dikerjakan."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=138MDKRr7frhpre4mLd1yUYfgzAE14CZF",
            "https://drive.google.com/uc?export=view&id=1qPWenlsf7BJTyHojHMChWR0PLosQI-S0",
            "https://drive.google.com/uc?export=view&id=",#fadil prasetyo
            "https://drive.google.com/uc?export=view&id=1ET-xRI5dGfbQo8QYJvgikDKPh4KuQE1R",
            "https://drive.google.com/uc?export=view&id=1BSngD3gGu4X9WeGW1oxUaH8gmdQ-8bhn",#ni made
            "https://drive.google.com/uc?export=view&id=1zbYcYVZAV-Nb5AXwbfL3JqPYwXkBLipC",
            "https://drive.google.com/uc?export=view&id=1Upl7btwns6lbgxDmAeiGFt6Jat4G99KT",
            "https://drive.google.com/uc?export=view&id=1VyOfnB8n1hQ-14O4504zw4DhauZTY5R9",#yulia
            "https://drive.google.com/uc?export=view&id=1Wf_FBla4z2DYX3UjP6eOGdfW1TXU23Pm",
            "https://drive.google.com/uc?export=view&id=13ZE1IMoRgywpHcG4Odge_iT_RNvkU8QX",
            "https://drive.google.com/uc?export=view&id=19lXhqFGmDV1QfuRAVcjAS2kvlOjIWgOz",
            "https://drive.google.com/uc?export=view&id=1dEu37qir0pagSHnCT1FKGbM61npc6hrh",
            "https://drive.google.com/uc?export=view&id=13FZ3RLsIPvNxwjhwBDLEku3KT_Xr9Kdw",
            "https://drive.google.com/uc?export=view&id=1Su1GIpI0Ff4yqG-OaB5qmPwfOvsCJcLN",#sherena
            "https://drive.google.com/uc?export=view&id=1CDPaPMgG17ovTB4eDp96dj076LFh-KnM",
            "https://drive.google.com/uc?export=view&id=1px0xV9J4zM73H9ZPi5MSg3l7un4qfPPY",#Faiza
            "https://drive.google.com/uc?export=view&id=1bCC3d1OxJYbpYD9FLiuzik_d76w2Xn8M",
            "https://drive.google.com/uc?export=view&id=1wdzMaSjtBw-Ryf8X8-UxHh_wax1kePhd",
            "https://drive.google.com/uc?export=view&id=1JYuWYih1uXDP1dZ6NbsefsdJxt00QFpB",
            "https://drive.google.com/uc?export=view&id=1pRQmPxqIak8pHImXzgvONrGhdQYWWksE",#melva
            "https://drive.google.com/uc?export=view&id=1Ne1JPrANN2s2NjnHh8vUSyu2RUSgALZP",
            "https://drive.google.com/uc?export=view&id=1Z4jxSCHS_vziV9J88ntdhyIG9NgoQ77a",

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
                "kesan": "Bang Fabio orangnya seru banget, asik diajak ngobrol, dan pinter banget juga! Seneng banget kalau bisa ngobrol atau diskusi sama abang karena selalu ada hal baru yang bisa dipelajari. Pokoknya paket lengkap seru dapet, ilmunya juga dapet",
                "pesan": "Semoga abang selalu diberi kelancaran dalam segala hal dan ilmunya bisa bermanfaat buat banyak orang. Sukses terus ya, Bang"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Nonton film",
                "sosmed": "@tvnty_",
                "kesan": "Kak Tanty orangnya lucuuu banget, hyperaktif, dan selalu bikin suasana jadi rame. Ada aja tingkahnya yang bikin ngakak, nggak pernah kehabisan energi kak tanty ini.",
                "pesan": "Semoga kakak selalu bahagia, sehat, dan dilancarkan segala urusannya. Jangan pernah kehilangan sisi ceria kakak yaa, sukses terus, Kak"# 1
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Bang Fadil orangnya baikkk banget, humble parah, dan berprestasi. Walaupun punya banyak pencapaian, abang tetap rendah hati. Sosok yang baik dan pastinya akan selalu dikenang",
                "pesan": "Terima kasih ya, Bang, sudah menjadi sosok yang menginspirasi banyak orang. Semoga Allah mengampuni segala dosa abang, menerima semua amal ibadahnya, dan menempatkan abang di tempat terbaik di sisi-Nya"# 1
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis ",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "Bang Manuel orangnya humble banget, tapi kalau ngomong to the point, nggak bertele-tele. Asik dan seru banget orangnya, Bang",
                "pesan": "Semoga abang selalu diberi kelancaran dalam segala hal, dimudahkan urusannya, dan sukses terus ke depannya. Makasih ya, Bang"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12",
                "asal": "Bali",
                "alamat": "nusa peninda",
                "hobbi": "menghayal",
                "sosmed": "@violaadrtr_",
                "kesan": "Kak Viola orangnya humble banget, murah senyum, dan asik abiss, Senyumnya ramah banget. Seneng deh bisa kenal Kakak",
                "pesan": "Semoga kakak selalu bahagia, dilancarkan segala urusannya, dan dikelilingi hal-hal baik. Sukses terus ya, Kak"# 1
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Kak Risa orangnya baikkk banget dan humble parah! Pembawaannya sederhana dan ramah, seneng banget bisa kenal Kakak",
                "pesan": "Semoga kakak selalu dikelilingi hal-hal baik, dilancarkan segala urusannya, dan bahagia selalu. Makasih ya, Kak."# 1
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "1244500078",
                "umur": "19",
                "asal": "kepulauan riau",
                "alamat": "teluk betung",
                "hobbi": "nonton khw",
                "sosmed": "@vunnycaa",
                "kesan": "Kak Vannisa orangnya kalem banget dan pinter juga, Pembawaannya tenang, tapi pinteeer banget. Asik dan salut banget sama Kakak",
                "pesan": "Semoga kakak selalu diberi kelancaran dalam segala hal, ilmunya bermanfaat buat banyak orang, dan sukses terus ke depannya. Makasih ya, Kak"# 1
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Kak Yulia orangnya kalem banget dan baik parah, Pembawaannya tenang, dan ramah",
                "pesan": "Semoga kakak selalu diberi kebahagiaan, dilancarkan segala urusannya, dan dikelilingi orang-orang baik. Sehat dan sukses selalu ya, Kak."# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@keyashafi_",
                "kesan": "Bang keya orangnya soft spoken banget, pinter, dan humble parah,Pembawaannya kalem, dan kek soft boy.",
                "pesan": "Semoga abang selalu diberi kelancaran dalam segala hal, ilmunya bermanfaat buat banyak orang, dan sukses terus ke depannya."# 1
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara ",
                "alamat": "Pemda",
                "hobbi": "Sibuk",
                "sosmed": "@_els.a",
                "kesan": "Kak Elsa orangnya aktif banget ikut kepanitiaan dan ceria abis, Selalu semangat di setiap kegiatan, pokoknya energinya nggak ada habisnya",
                "pesan": "Semoga kakak selalu diberi kesehatan dan kelancaran dalam setiap kegiatan. Semoga semua kesibukan dan usaha kakak membuahkan hasil yang baik. Semangat terus ya, Kak"# 1
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "airan",
                "hobbi": "mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kak Fadya orangnya baikk banget dan humblee, selalu ramah sama orang-orang di sekitarnya",
                "pesan": "Semoga kakak selalu dikelilingi hal-hal baik, dilancarkan segala urusannya, dan bahagia selalu ya, Kak"# 1
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "Kak Lovi orangnya aktif bangett dan keren banget kalau lagi nge-MC, Pembawaannya seru, percaya diri, dan bisa bikin suasana jadi hidup. Keren deh, Kak",
                "pesan": "Semoga kakak selalu semangat dalam setiap kegiatan, makin berkembang, dan sukses terus ke depannya. Semoga skill MC-nya makin keren lagi ya, Kak"# 1
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "kalianda",
                "alamat": "kota baru",
                "hobbi": "main game, tidur",
                "sosmed": "@aluccy_",
                "kesan": "Bang Alsi orangnya kalem, dan asik bangeet.",
                "pesan": "Semoga abang selalu sehat, bahagia, dan dilancarkan semua urusannya. Tetap jadi abang yang kalem tapi asik ya, Bang"# 1
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kak Sherena orangnya baikk banget, humble, murah senyum, dan Ramah banget",
                "pesan": "Semoga kakak selalu bahagia, sehat, dan dilancarkan segala urusannya. Jangan pernah berhenti jadi orang baik dan tetap murah senyum ya, Kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Bang Razin orangnya baikk banget, humble, murah senyum, dan vibes soft boy-nya kerasa banget! Pembawaannya kalem dan ramah",
                "pesan":"Semoga abang selalu dikelilingi orang-orang baik, dilancarkan segala urusannya, dan bahagia selalu ya, Bang."
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel ",
                "sosmed": "@faizaanjanii",
                "kesan": "Kak Faiza orangnya baikk banget dan humblee, ramah juga sama orang-orang di sekitarnya.",
                "pesan":"Semoga kakak selalu sehat, bahagia, dan dilancarkan semua urusannya. Tetap jadi orang baik dan humble ya, Kak"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Rajabasa Raya",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Bang Gathfan orangnya emang pendiem, tapi kelihatan banget kalau abang punya sisi baik yang bikin orang nyaman.",
                "pesan":"Semoga abang selalu dimudahkan dalam setiap langkahnya, sukses terus ke depannya, dan semoga hal-hal baik selalu datang ke abang. Sehat-sehat terus ya, Bang"
            },
{
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur ",
                "hobbi": "3N ( Ngoding , Ngegame, Nyibukin Diri)",
                "sosmed": "@apiszzaja",
                "kesan": "Bang Hafidz orangnya lucuuu paraah, asik, dan baik banget,Selalu ada aja tingkah yang bikin suasana jadi lebih seru.",
                "pesan": "Semoga abang selalu bahagia, dilancarkan segala urusannya, dan dikelilingi orang-orang baik. Kalau butuh sniper, call me ya, Bang."# 1
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Campang Raya, Sukabumi",
                "hobbi": "Gym, membaca, dan bermain",
                "sosmed": "@kelelep_comberan",
                "kesan": "Bang Kaleb orangnya baikk banget, humble, dan pinter bangeet. Keren sih bang, bisa punya banyak pengetahuan tapi tetap rendah hati. Semoga ilmunya terus bermanfaat buat banyak orang ya, Bang",
                "pesan":" Semoga abang selalu diberi kelancaran dalam setiap urusan, makin sukses ke depannya, dan semua cita-citanya bisa tercapai. Tetap jadi abang yang rendah hati dan menginspirasi yaa"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal":"Sumatera Selatan ",
                "alamat": "Sukarame ",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kak Melva orangnya baikk banget dan keren juga karena jago ngodingg (kata kak ipin) Makasih banyak ya, Kak, udah sering nemenin dan bantu kak ipin.",
                "pesan":"Semoga kakak selalu dilancarkan segala urusannya, makin jago ngodingnya, dan sukses terus ke depannya. Makasih udah jadi teman yang baik buat kak ipin, semoga kebaikan kakak dibalas dengan banyak hal baik juga yaa, Kak"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syafiqui",
                "kesan": "Bang Syafiq keren bangeet sihh. Orangnya pinter dan berprestasi banget, apalagi bisa lolos PIMNAS, that s so cool, Bangg! Semoga prestasinya bisa terus bertambah dan jadi inspirasi buat banyak orang",
                "pesan":"Semangat terus buat PIMNAS-nya ya, Bangg! Semoga semua persiapan dan usahanya dilancarkan, bisa memberikan hasil yang terbaik, dan tentunya membawa pulang prestasi yang membanggakan. Good luck, Bang"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal":"Kotabumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "Bang Henry orangnya baikk banget dan punya jiwa pengayom yang kerasa banget sebagai ketua angkatan. Kelihatan kalau abang peduli sama teman-temannya dan bisa jadi sosok yang diandalkan.",
                "pesan":"Semoga segala urusannya dilancarkan dan tetap jadi sosok yang bisa mengayomi serta menginspirasi banyak orang ya bang, Semangat teruss."
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14wpQDgomnJa0c6hZnajbf5O9n_U4RN5Q",
            "https://drive.google.com/uc?export=view&id=1kG3KhqYFKc_G9dXqmcUV0qqfqODALZaR",
            "https://drive.google.com/uc?export=view&id=1KA36LJidYdPHw2vCx5Ug63rC32F_tnWh",
            "https://drive.google.com/uc?export=view&id=1gOEKGVZSvRQjWFw2ZHhKHRdf42JaMBRB",
            "https://drive.google.com/uc?export=view&id=1aWyMPVwCikjr644BmL-jkTFbkOc8-9rH",
            "https://drive.google.com/uc?export=view&id=1rOMwRvrY-5z10KgYJ_nsbJTqOdL4Z5vP",
            "https://drive.google.com/uc?export=view&id=1A-OPnBvysFok1aaNx2RaPEA3ZqGjo6Ge",
            "https://drive.google.com/uc?export=view&id=1dcEcLdV7-f3kcDHTedaybBewtfO0FmJm",
            "https://drive.google.com/uc?export=view&id=1HS9vPjePp2Ec_NvnGzQQyP0C4PFwyW1C",
            "https://drive.google.com/uc?export=view&id=1p9pCozW8zKJp1HhJMw_ae_sS4yzpMO4T",
            "https://drive.google.com/uc?export=view&id=11pjnEIQIP0U7rCl1zTYwIgosOAYl3Ebp",
            "https://drive.google.com/uc?export=view&id=1WoNLoN5-AtZem93x0-PacJanQKBAgtEl",


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
                "kesan": "Bang Ihsan orangnya lucuu banget, suka ngelawak, dan asik diajak ngobrol, selalu ada aja tingkah atau candaan yang bikin suasana jadi lebih rame.",
                "pesan": "Semoga abang selalu diberi kelancaran dan kemudahan dalam segala hal."# 1
            },
            {
                "nama": "hanifah inaya sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak Hanifah orangnya humble parahhh, lucu, dan baik banget",
                "pesan": "Semoga kakak selalu sehat, bahagia, dan dilancarkan semua urusannya. Sukses terus ke depannya ya, Kak"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah orangnya humblee dan asik banget! Ramah juga orangnya, pokoknya seru deh bisa kenal kakak",
                "pesan": "Semoga kakak selalu sehat, bahagia, dan dilancarkan semua urusannya. Sukses terus ya, Kak, semoga semua hal baik selalu menyertai kakak"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Bang Hasan orangnya kalem, tapi asik banget, apalagi kalau diajak diskusi, enak diajak bertukar pikiran dan bisa nyam",
                "pesan": "Semoga abang selalu dilancarkan segala urusannya, makin sukses ke depannya, dan semoga apa pun yang sedang diusahakan bisa tercapai."
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin",
                "sosmed": "@lay.inr_",
                "kesan": "Kak Layina orangnya kalem banget dan humble juga. Pembawaannya sederhana, tapi tetap ramah sama orang-orang di sekitarnya",
                "pesan": "Semoga kakak selalu sehat, bahagia, dan dimudahkan dalam setiap urusannya. Semoga semua hal yang sedang diperjuangkan bisa tercapai dan sukses terus ke depannya ya, Kak"# 1
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": " Bang Iqbal ini orangnya humble banget, baik pula. Menurutku kek tipe orang yang nggak banyak gaya, tapi kebaikannya kelihatan dari cara abang berinteraksi sama orang lain.",
                "pesan": "Semoga abang selalu dikelilingi orang-orang baik juga, dilancarkan apa pun yang lagi diusahakan, dan semoga ke depannya makin banyak hal seru dan baik yang abang temuin. Sukses terus ya, Bang"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "@alljtine_",
                "kesan": "Kak Talitha orangnya baik dan humblee paraah.",
                "pesan": "Semoga ke depannya banyak hal baik yang datang ke kakak, semua urusan dilancarkan, dan apa pun yang lagi kakak perjuangkan bisa tercapai"# 1
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kak Nadia orangnya baikk banget dan ceriaa, auranya positif banget.",
                "pesan": "Semoga kakak selalu bahagia, dilancarkan segala urusannya, dan sukses terus ke depannya. Salam hangat dari sesamo wong Palembang"# 1
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "Bang Pome orangnya baik dan humble bangeett, mana jago main basket lagi.",
                "pesan": "Semoga abang makin jago main basketnya, makin banyak prestasi yang bisa diraih, dan tentunya sukses terus dalam apa pun yang lagi diusahakan."# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "Bang Afdhal orangnya kalem dan humble banget. Baik juga orangnya",
                "pesan": "Semoga abang selalu sehat, dilancarkan segala urusannya, dan sukses terus ke depannya ya, Bang"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kak Anggun orangnya baik bangeet dan humble paraah.",
                "pesan": "Semoga kakak selalu sehat, bahagia, dan dilancarkan semua urusannya. Sukses terus ya, Kak"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": " Kak Della orangnya ceriaa dan humble parahh.",
                "pesan": "Semoga kakak selalu ceria, sehat, dan dilancarkan segala urusannya. Sukses terus ya, Kak, semoga banyak hal baik yang datang ke depannya"# 1
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_3y8F-vliK8AkYCygQLChLXRLKUSiGNQ",
            "https://drive.google.com/uc?export=view&id=1dAt8U0NFIdH0-WLCYH5w-sNUY0IjjJfB",
            "https://drive.google.com/uc?export=view&id=1TBtV2MjSFad_9Sr4IxfX-UQaYfR_RZ-B",
            "https://drive.google.com/uc?export=view&id=1Vm3yOKhZ4hC6YiJyP22MtgoL9ll1cTzL",
            "https://drive.google.com/uc?export=view&id=1XjQiW3zT7Eut1V1sxmBpYTLdHxPAk8GM",
            "https://drive.google.com/uc?export=view&id=1AR2bRkGuZUfEv-cRR8O4xbsc-L78aPCe",
            "https://drive.google.com/uc?export=view&id=1sFqRY7JV-Xditg8UOsF2E8jSJ9sBI_PC",
            "https://drive.google.com/uc?export=view&id=1yEGAhnufZi2uYyhMWGBKEru3ZGZHPTic",
            "https://drive.google.com/uc?export=view&id=1F57ux7UTZ6H9DcXwRws01pieWnK_M1pF",#alya
            "https://drive.google.com/uc?export=view&id=1johnIGexWrrUN89ZQY15Jv58FfbvmT1m",
            "https://drive.google.com/uc?export=view&id=1O8qbtgayc3bWsavFVjAINEVhTDiJv9jR",
            "https://drive.google.com/uc?export=view&id=1ePiKjXIrR2g7XT5a3KZDnVsmFQAzn_OX",
            "https://drive.google.com/uc?export=view&id=1a02153dKLZLFQMuIxK9c0xpFQTpMu6UN",
            "https://drive.google.com/uc?export=view&id=18x2jW-F2YTcIID1c9zKfKSNZbFOxkw2D",
            "https://drive.google.com/uc?export=view&id=1pShgwuTD_T301O2NvmsTfOIh26CmpAZO",
            "https://drive.google.com/uc?export=view&id=1RjAGINjoOxu54vKGlUSOHNZa4qTDr3EY",
            "https://drive.google.com/uc?export=view&id=1RjAGINjoOxu54vKGlUSOHNZa4qTDr3EY",#shafa
            "https://drive.google.com/uc?export=view&id=1yVaSGq1NN3cnqVATv4a4iDEw6OLndQod",

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
                "kesan": "Kak Nayla orangnya baik, humble, dan asik parahh! Seru banget bisa kenal kakak yang ramah dan nggak kaku sama orang lain",
                "pesan": "Semoga kakak selalu sehat, dilancarkan semua urusannya, dan semangat terus buat menjalankan amanah sebagai kadep yaa, Kak. Sukses terus ke depannya"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Dona orangnya baik dan humble parahh. Seneng bisa kenal kakak, apalagi kakak jadi pentutor LMD juga. Makasih ya, Kak, udah bantu ngajarin dan berbagi ilmunya selama tutor LMD ini",
                "pesan": "Semoga kakak selalu sehat, dilancarkan segala urusannya, dan sukses terus ke depannya. Semangat terus buat kuliah dan amanahnya di Medkraf yaa, Kak"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu ",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran ",
                "sosmed": "@noerruuu",
                "kesan": "Bang Labo orangnya baik dan ramah bangett",
                "pesan": "Semoga abang selalu sehat, dilancarkan segala urusannya, dan sukses terus ke depannya. Semangat terus ya, Bang"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Way Halim ",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kak Tasya orangnya ceriaa dan humble parahh",
                "pesan": "Semoga kakak selalu bahagia, sehat, dan dilancarkan semua urusannya. Semangat terus ya, Kak, semoga makin banyak hal baik yang datang ke depannya"
            },
            {
                "nama": "Felisya Nabila Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal": "Lampung Timur ",
                "alamat": "Kota Baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": " Kak Felisya orangnya lucuuu banget, tapi pembawaannya juga kalem gituu.",
                "pesan": "Semoga kakak selalu sehat, bahagia, dan dilancarkan semua urusannya. Sukses terus ya, Kak, semoga apa pun yang lagi diusahakan bisa tercapai."# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "21",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "Bang Razan orangnya kalem, tapi ternyata ceria juga yaa. Mana jago main badminton lagii, keren sih Bangg",
                "pesan": "Semoga abang selalu sehat, dilancarkan semua urusannya, dan makin jago main badminton-nya. Semoga bisa sering ketemu di lapangan ya, Bangg"# 1
            },
            {
                "nama": "Sania DWi Ayu Lestari",
                "nim": "124450086",
                "umur": "21",
                "asal": "Karawang ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania orangnya baik dan humble parahh. Keren juga bisa jadi Kepala Divisi Konten Spesialis di himpunan. Semoga makin banyak karya keren yang bisa dihasilkan bareng timnya yaa, Kak",
                "pesan": "Semoga kakak selalu sehat, dilancarkan semua urusannya, dan sukses terus ke depannya. Semangat terus buat mengembangkan konten-konten keren di himpunan yaa, Kak"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "Kak Allisha orangnya ceriaa banget dan multitalent parahh. Bisa ngonten, jago main perkusi juga, pokoknya keren banget sih, Kak. Banyak bangetlah bakat kakak inii.",
                "pesan": "Semoga kakak makin berkembang dengan semua bakat yang dimiliki, makin banyak kesempatan buat berkarya, dan sukses terus ke depannya. Ditunggu karya-karya kerennya yaa, Kak"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kak Alya orangnya baik dan seruu bangeet.",
                "pesan": "Semoga kakak selalu semangat berkarya, makin banyak ide-ide keren yang bisa direalisasikan, dan sukses terus ke depannya yaa, Kak"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kak Bunga orangnya baik, lucuu, dan seruu banget. Pokoknya asik deh bisa kenal kakak, semoga kakak selalu jadi orang yang menyenangkan yaa",
                "pesan": "Semoga kakak selalu bahagia, sehat, dan dilancarkan segala urusannya. Semangat terus ya, Kak, semoga makin banyak hal seru dan baik yang datang ke depannya."# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Alquran",
                "sosmed": "@difanyhsa_",
                "kesan": "Kak Difa orangnya seru banget dan baik jugaa. Apalagi suka ngajakin ngobrol pake bahasa Palembang, jadi berasa kek dirumah gituu, ngobrol dengan bahasa daerah.",
                "pesan": "Semoga kakak selalu sehat, bahagia, dan dilancarkan segala urusannya. Sukses terus ya, Kak"# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@nzlhauly_",
                "kesan": " Kak Nazlaa orangnya lucuu dan baik bangeet.",
                "pesan": "Semoga kakak selalu sehat, bahagia, dan dilancarkan semua urusannya. Semangat terus ya, Kak, semoga banyak hal baik yang datang ke depannya"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Aira Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kak Raihana orangnya baik banget. Keren bangeet kakaknya bisa jadi Ketua Divisi Desain, semoga bisa terus menghasilkan karya-karya yang bagus dan kreatif bareng timnya yaa, Kak",
                "pesan": "Semoga kakak selalu sehat, dilancarkan segala urusannya, dan makin berkembang dalam dunia desain. Semangat terus buat memimpin divisinya, Kak! Sukses selalu yaa"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame ",
                "hobbi": "-",
                "sosmed": "@daffascript",
                "kesan": "Bang Daffa orangnya lucuuu dan humble parahh! Mana suka ngelawak lagi",
                "pesan":"Semoga abang selalu sehat, bahagia, dan sukses terus ke depannya. Jangan kehabisan bahan lawakan ya, Bang."
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "Bang Edsel orangnya baik dan murah senyum banget.",
                "pesan": "Semoga abang selalu sehat, dilancarkan segala urusannya, dan sukses terus ke depannya. Semoga hari-harinya selalu dipenuhi hal-hal baik ya, Bang"# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Kak [Nama] baik bangeett! Seneng bisa kenal kakak, semoga kebaikan kakak selalu jadi hal positif buat orang-orang di sekitar yaa kak.",
                "pesan":"Semoga kakak selalu sehat, bahagia, dan dilancarkan semua urusannya. Semoga apa pun yang lagi kakak usahakan bisa berjalan dengan baik dan hasilnya sesuai harapan yaa, Kak"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis dan menulis",
                "sosmed": "@_shaazzh",
                "kesan": "Kak Shafa baik banget dan penyabar jugaa. Seneng deh bisa kenal kakak yang punya sifat sebaik itu. Semoga kebaikan kakak selalu dibalas dengan hal-hal baik juga yaa",
                "pesan": "Semoga kakak selalu diberi kesehatan, kebahagiaan, dan kesabaran dalam menghadapi berbagai hal. Semangat terus ya, Kak, semoga semua urusannya dilancarkan"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "Kak Zannuba humble dan seruu parahh. Asik banget orangnya.",
                "pesan": "Semoga kakak selalu bahagia, sehat, dan dilancarkan semua urusannya. Semoga ke depannya makin banyak hal seru dan menyenangkan yang kakak temuin yaa"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan
