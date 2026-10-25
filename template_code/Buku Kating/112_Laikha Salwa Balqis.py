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
            "https://drive.google.com/uc?export=view&id=1mwTglwSAO6XR-RPpDPlEzEz_my0_t8fd",
            "https://drive.google.com/uc?export=view&id=1RSot8q9RBbGCjSSqsA1BJjiQApzsg9eC",
            "https://drive.google.com/uc?export=view&id=1uGQykTLAbXffdOdSnH6Ay4h8pCRuJ2Ci",
            "https://drive.google.com/uc?export=view&id=19RRGjm139otsg9rIk28xWqoMvl5Pry7E",
            "https://drive.google.com/uc?export=view&id=1I-vOhuR2C9eggs8YX56E7kwuVjhviL_E",
            "https://drive.google.com/uc?export=view&id=1MF1bkPdW0wtoJtJyhwZ-GQeL_UtTDp-V",
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
                "kesan": "Menurut saya, Bang Fajar adalah orang yang mengayomi dan sangat menginspirasi.",
                "pesan": "Semoga Bang Fajar sukses dan sehat selalu ya bang"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil seru, santai, dan bisa memastikan semua orang masuk kedalam obrolan",
                "pesan": "Semangat terus bang Aqilll"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi asyik dan baikkk",
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois baik dan kerenn.",
                "pesan":"Semoga bang qois sukses dan sehat selaluu"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak hafsa orang yang humble.",
                "pesan":"Semoga kak hafsa sukses dan sehat selaluu"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak luthfia lucu dan asik.",
                "pesan":"Semangat terus ya kakkk kuliahnya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ag7-igTyHLOvBj43yGBEpKmieCz61t-B",
            "https://drive.google.com/uc?export=view&id=1B1Aij2L3bcAnsRPhJaWEHHLLB-d7Di4t",
            "https://drive.google.com/uc?export=view&id=18AgXt5LNUXQCovMR4O1QdKV_Q8sQMd5G",
            "https://drive.google.com/uc?export=view&id=1Ea9tQVdQZ_uUNCRbAbVqgCpmF_tn3afB",
            "https://drive.google.com/uc?export=view&id=1wiB1UJGqxzXsU8TcLC3JPAfYVqGYt5dD",
            "https://drive.google.com/uc?export=view&id=1Hz9RZMNX1-U57XmCSO70LO_Z90k9_2zi",
            "https://drive.google.com/uc?export=view&id=1H0ckAv5DPPt5P3oU7wU5T_CH9XMYkbTV",
            "https://drive.google.com/uc?export=view&id=1JQCSpxlgzqMfM2pv_mMIThgqW2D2ANi8",
            "https://drive.google.com/uc?export=view&id=1cAMBfPrO75aUP3pPOsm1Pt6HHwm5Ocvi",
            "https://drive.google.com/uc?export=view&id=1e9_aazaxOio0RBjkPV2n39xC2PAPKrWF",
            "https://drive.google.com/uc?export=view&id=1Tt_HZEvvXn9nxe-g1SZ1PhgCcJptvP0Y",
            "https://drive.google.com/uc?export=view&id=1hZjrhNYKd4_T7pywfiJKLWZh7vA04sAx",
            "https://drive.google.com/uc?export=view&id=1yG5AvLHhk3QGdHzf14RCNdt-E7y-nMIX",

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
                "kesan": "Jujur bang rido kocak banget, tapi tetep bisa serius.",
                "pesan":"Makasih udah bikin ketawa terus bang hahaha, semoga bang rido sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak jue asik, talkative, dan humble",
                "pesan":"Semangat kak juee kuliah dan siarannyaa!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Jujur bang dharu keren, panutan",
                "pesan":"Semangat terus bang!! semoga exvoltasnya lancarr"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang niko baikk, informatiff",
                "pesan":"Semoga bang niko sukses terusss"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kak sarifah lucuu, baik, humble",
                "pesan":"Semoga kak saripah sukses terus bahagia selaluu"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang givaro jujur humornya kaya receh gitu sering ketawa ngakak, tp abangnya baik dan informatif",
                "pesan":"Semoga bang givaro bahagia dan sukses selalu"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa baikk dan lucu, such a good organizer sepertinya",
                "pesan":"Semoga kedepannya laikha bisa kaya kak nisaa"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kak hani kalem, baik, lucu",
                "pesan":"Sukses terus kak hanii, sehat sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Abang yang suka nyanyi, looksnya kaya orang pintar dan hebat",
                "pesan":"semangat terus kuliahnya banggg !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang jona baik dan suka ada gerakan tambahan hahaha",
                "pesan":"semangat terus kuliahnya bang jonaa !!!"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak sekarr baikkk, lucu dan kalo udah kenal ternyata ekspresif",
                "pesan":"Semangat kuliahnya kak sekar semoga lancar terus semua urusannya!!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "ka wawa lucu dan imut",
                "pesan":"Semoga kuliahnya lancar terus ya kakk!!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K28aOhn06n1sOp1qiDGVibD-P0fkwjLL",
            "https://drive.google.com/uc?export=view&id=1GudBW4sElvNx8H4B1et-_C6g0F4AkKOx",
            "https://drive.google.com/uc?export=view&id=19yU1LJV_62a6wk7IRMJnDtB45dwP-Uap",
            "https://drive.google.com/uc?export=view&id=1YuQzPAMbSQqWKrZ3cjKrsM3bwbghlHn-",
            "https://drive.google.com/uc?export=view&id=1aqbasPRPlnG3T1FTxDaFcIjkfjvHKaHB",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#caesar
            "https://drive.google.com/uc?export=view&id=1r4zVSnpxIYLE3lmWDcBCnSDjmiogaiWA",
            "https://drive.google.com/uc?export=view&id=1lWimSBk4TkOwnSg3xp3PIxw_GHujDDzg",
            "https://drive.google.com/uc?export=view&id=1q-4aEbxKGq7W76VTR9KHMFm9fEscq2vl",
            "https://drive.google.com/uc?export=view&id=1kATfmNQxpwCCws0RA_CjJHTEKoht3De_",
            "https://drive.google.com/uc?export=view&id=1r1bNhzN239GdHbamj8rOP6TtRIahUmO_",
            "https://drive.google.com/uc?export=view&id=1-jJ_A2BNfm2_nHdb5h_Wdtu3OvMtMUok",
            "https://drive.google.com/uc?export=view&id=1Z63-dzVUOt3Fua4NSnD8LeQs13mParzk",
            "https://drive.google.com/uc?export=view&id=1L1p2mlC6JOw2PI3M_lvrOaKrDaQjyTAe",
            "https://drive.google.com/uc?export=view&id=1u_Qzm4Ku_8XYlnLBLCd5dtlcs6UQBC0h",

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
                "kesan": "Bang kevin keren,baik, namanya bagus",
                "pesan":"Semoga dilancarin ya bang kuliahnya sampai luluss"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kak razka asik, cantik, baik",
                "pesan":"Semangat terus kak razkaa, semoga sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Abang ini asik",
                "pesan":"Semangattt bang kuliahnyaaa!"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakak ini imut dan humble",
                "pesan":"sehat sehat kakakk, jangan lupa bahagia"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abangnya asik dan baik.",
                "pesan":"Lancar lancar yaa bang kuliahnya, semoga bahagia teruss"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakanya humble dan murah senyum.",
                "pesan":"Semoga kakanya sehat teruss yh kakk"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Abang ini baik dan asik",
                "pesan":"Semoga abangnya lancar rezekinya yhh, sehat selalu dan juga lancar kuliahnya"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak juwita ini lucuu",
                "pesan":"Kakkk yang semangat yah kuliahnya semester ini, kaka pasti bisaa"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Dengerin laikha nyanyi",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang ridwan baikk dan talkative hahaha",
                "pesan":"Bang ridwan semangat ya bang semester ini, nnt saya nyanyiin dah kl mumet WKWKWK"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Abang terexcited hahaha lucu",
                "pesan":"Makasih udah excited terus bang andraa, semoga abang sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Abang ini diem2 kocak gitu ya kayanya",
                "pesan":"makasih udah dampingi bandalm latihan terus bang bryannnn"# 1
            },
             {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal":"Surabaya ",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "pesan":"Semangattt bang bangg jadi pj game nyaaa hihi"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kaka ini lucuu n imup",
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri ",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kak caca humble dan asikk",
                "pesan":"Bahagia selalu kakakkk!!"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abang ini agak kalemm yaa, tapi baikk",
                "pesan":"semangat terus kuliahnya abanggg !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HdsPQEmwHDzA4-_v_CtfZAVAQ-7-Rp-4",
            "https://drive.google.com/uc?export=view&id=1Mg9SETbG0s37ZVbCdv0fv0R-tvg5R-2-",
            "https://drive.google.com/uc?export=view&id=1HYWfmIn3bCntw40Dww4qn2G3mDecxIXJ",
            "https://drive.google.com/uc?export=view&id=1_qXAoBXJ2XsiloHr5Wq8f6UTMZBRqn-a",
            "https://drive.google.com/uc?export=view&id=1NAJ9DyVnee4cRQ1rYoaYAUMuuN1eOOYR",
            "https://drive.google.com/uc?export=view&id=1ww_jP4geuIKcBfHGHz1USyMe3HAkIbkD",
            "https://drive.google.com/uc?export=view&id=1OANYGffDMxpLbmPymmvD36B4JZQO7rk-",
            "https://drive.google.com/uc?export=view&id=1RieRGmdYfgvObYCWZteqGhVYnCo7-jm1",
            "https://drive.google.com/uc?export=view&id=1Lo8ieDxkAvKjqrCl9BlzmE1SJJrLEYTS",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1IRXQLlGr-wDymGsTh7fw-mPWS3u4jsHz",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1iluGTbzKp9AhVSE4NkMVEIncnif_t_L5",
            "https://drive.google.com/uc?export=view&id=1jgT_4klP2CGbAOhoYPlIiBBtQ8lZBvAg",
            "https://drive.google.com/uc?export=view&id=1KAUzC1cTVRxBB4FrQp_pjnINd7b-E23U",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",

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
                "kesan": "Bang Haikal baik, suka bercerita",
                "pesan":"Semangat terus bang haikal, semoga kuliahnya lancar sampai lulus"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak inii baikk, humble skalii",
                "pesan":"semangat terus kuliahnya kakak baik !!!"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kaka terhumble dan friendly, sangat hangat rasanya",
                "pesan":"Sehat sehat kaka baikk, semoga segala urusan kaka dilancarin ya kakk!"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang farhan baikk",
                "pesan":"Semoga bang farhan sehat dan bahagia selaluu"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kakak ini baik dan lucuu.",
                "pesan":"semangat terus kuliahnya kakaaa"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kakak ini lucu banget, baik dan friendly",
                "pesan":"Bahagia selalu kakaaa, semoga kuliahnya lancar"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang jaya baik dan informatif",
                "pesan":"Semangat terus yaa bang jayaaaaa"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kak najla baikk dan imup",
                "pesan":"Yang semangat ya kakaaa semester ini, semoga sukses selaluu"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin Harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Abangnya baik dan sabar",
                "pesan":"semangat terus kuliahnya abangg !!!"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "masak",
                "sosmed": "@christiani8872",
                "kesan": "Kakak ini ramah senyum bangett",
                "pesan":"Makasih udah tutorin kita kakkk, semangat teruss"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Abang ini baikkkk",
                "pesan":"semangat terus kuliahnya abangg !!!"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20 tahun",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Bima",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
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
                "kesan": "kak cika lucu nan baik",
                "pesan":"Semoga lancar terus ya kakk kuliahnya"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "airan",
                "hobbi": "nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kak gustin seruu",
                "pesan":"Semoga kaka sehat dan bahagia selalu ya kakkk"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Abangnya asik dan seruuuw",
                "pesan":"Sukses terus abanggg, semoga semester ini lancar yaa"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Kakak ini baik dan asikkk",
                "pesan":"semangat terus kuliahnya kak rafa sabinaaaaa!!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K28aOhn06n1sOp1qiDGVibD-P0fkwjLL",
            "https://drive.google.com/uc?export=view&id=1H5gMz9Nh5cnlDhhV5m1D47oHsc8XtGp4",
            "https://drive.google.com/uc?export=view&id=1CNUx3P7Tfnm-kPFW9PR1b8kd6ueV2NeB",
            "https://drive.google.com/uc?export=view&id=1XAPqAswqDDMJ56ezH3ohjGYrNiYy904E",
            "https://drive.google.com/uc?export=view&id=1gQEYEs0Kr6-VJK04MWQTVvQSl7Yfn8v8",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=16_k4TLlJNoPg2fg3xgGJPCOWVavaZ_h5",
            "https://drive.google.com/uc?export=view&id=11xSlGz5Wbycd5T0Smv7Vn0HljEMqZynO",
            "https://drive.google.com/uc?export=view&id=1J6-KM20_X4JOJifP3bbcurSAlcqQW_kA",
            "https://drive.google.com/uc?export=view&id=15umQ11imTRB49YDtshcubKGQ5qRxx8Hp",
            "https://drive.google.com/uc?export=view&id=1NzD2kwQ_-TqxY7YAHWsjnwvaffCREu0N",
            "https://drive.google.com/uc?export=view&id=1IT3NoxnrA38cEbL9eaaqBHL9GtBHUKKL",
            "https://drive.google.com/uc?export=view&id=1QXya5z1UZZHoLHUeXbqkf4iVRYNP50ve",
            "https://drive.google.com/uc?export=view&id=1mb9cnG59FhtyO52O5OAv2IfUHrtck16f",
            "https://drive.google.com/uc?export=view&id=1GZPivq-khQeF-9SgZUILhPm-gwTGjpRo",
            "https://drive.google.com/uc?export=view&id=1uBahgweg7JXHbvvTogL5GB0_54a0U2gu",
            "https://drive.google.com/uc?export=view&id=1u_Qzm4Ku_8XYlnLBLCd5dtlcs6UQBC0h",

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
                "kesan": "Kak arienta awalnya keliatan serem hihi, tapi ternyata baikkk",
                "pesan":"Makasih banyak ya kak, udah jadi salah satu orang dibalik CEO HMSD yang bikin aku berkembang."# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany baikkk",
                "pesan":"Semangat terus ya kakaaaa semester ini, semoga lancar2 kuliahnya sampai lulus"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel tegas tapi lama-lama saya ngerasa bang nobel jadi kaya bapak dari datavora",
                "pesan":"Makasih banyak yaa bang udah jadi kadiv kader, saya beneran jadi banyak berubah jg karna dikaderr "# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi sangat enerjik apalagi kalo damaskusan hehe",
                "pesan":"Semangat kuliahnya bang azmii, semoga lancar dan sukses teruss yaaa bang"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang ayake keliatannya paling soft spoken diantara abang dan kaka timder lainnya",
                "pesan":"Semangat terus yaa bang ayake, semoga bahagia dan sehat selaluuuuu"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Terlihat sangar, tp ternyata asik juga",
                "pesan":"Sehat selalu dan sukses terusss bang caesaarr"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kaka ini terlihat asikkk (jujur)",
                "pesan":"Semangat ya kakaa semester ini, semoga lancar terusss kuliahnya ^^"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang haikal baikk",
                "pesan":"Sehat selalu dan sukses terus ya bang haikalll"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Sering ketemu di warteg bahari, kakanya sangat ramah bintang 5",
                "pesan":"Semangat terus kakaaa kuliahnya, semoga kapan kapan kita bisa makan warteg bareng ya kak hihi"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@queentanaabila",
                "kesan": "Kaka ini ramah, humble, dan asik",
                "pesan":"Semangat terus ya kak, semoga sehat dan sukses selalu!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Abang ini humble",
                "pesan":"sukses selalu bang desmannn, semoga lancar sampai lulus ya bangg"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "kak azzelya cantik dan baikk ",
                "pesan":"Semangat dan sehat selaluu kakaaa"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "Kaka ini suka nyanyi jugaa, baik, dan cantik mirip nagita slavina",
                "pesan":"sehat sehat ka cacaa, semoga semester ini dilancarinn segala urusan kaka yaa"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang jeremi ini baik dan humble",
                "pesan":"Semangat terus abangg"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak nabila humble dan talkative",
                "pesan":"sehat sehat kakaa, bahagia terus yaaa"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Abang ini stylishhh",
                "pesan":"Semangat teruss bang rafli, semoga sehat selalu bahagia selaluu"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "Kakak imut dan lucuuuu",
                "pesan":"sehat sehat dan lancar selalu kakaaa kuliahnyaaa^^"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

elif menu == "Senator":
    def DepartemenSenator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jYeIMQ8FT0EXA0zLJ0gABLD49JG7n43t",#fathinah
            "https://drive.google.com/uc?export=view&id=1zmDV95sO9xM12BOi7tBgMDOOqCk5GPiK",#helmy
            "https://drive.google.com/uc?export=view&id=1P-z8mEoGttLeRzuajqHVMpQTuzuZzLxt",#fernando
            "https://drive.google.com/uc?export=view&id=1mgjKYBUWwYv-SmJS28d1oRw3iV64XJVN",#suci
            "https://drive.google.com/uc?export=view&id=1S6oftedodBoqTfDvb6u40Vx4FVYsCKuD",#wielman
            "https://drive.google.com/uc?export=view&id=12AEnA4T6G39Dft-xa9e18hWrarBfcwBu",#liahana
            "https://drive.google.com/uc?export=view&id=1JtDKF4KwkI7DZNB9vrYy7cNJxssdEcKW",#aqila
            "https://drive.google.com/uc?export=view&id=1zZ7f6hMPeiypaKpW_X7ZXDS4WjWUI-1h",#hazel
            "https://drive.google.com/uc?export=view&id=1ozz2Vu-Ri2uoS6fl56R0GR_4TtAf2idS",#nadya
            "https://drive.google.com/uc?export=view&id=1FbCzIz6KmUE4R4a20JIZvrkQ29lLkIZs",#dwi


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
                "kesan": "Kak azizah perempuan keren!",
                "pesan": "Jujur ngefans krn kak azizah keren dan cantik, masyaallah bgt"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Bang hely baik bgtttt",
                "pesan": "Semangat kuliahnya bang helmyyyy"# 1
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Nemenin Wielman MC",
                "sosmed": "@barus.fernando",
                "kesan": "Bang nando baik jujurrr",
                "pesan": "Semangat kuliahnya bang nandoooooo"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru ",
                "hobbi": "Baca",
                "sosmed": "@sciia__",
                "kesan": "Kak suci asikkkk, baik, dan humble",
                "pesan": "Semangat kuliahnya kak suciiiiiii"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "jadi MC",
                "sosmed": "@wielhawn",
                "kesan": "Keren bang wielmannnnn",
                "pesan": "LANJUTKAN KEKERENANNYA BANG"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "main hp",
                "sosmed": "@lia.h_264",
                "kesan": "Kaka pemateri kerenn penyampaiannya jelas",
                "pesan": "Semangat kuliahnya kak!!"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kaka tercheerful yg pernah aku kenal di datasena",
                "pesan": "Semangat ngementornya kaka kerennnnnnnkuu"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "jadi sekjen",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abang-abang bermuka tegas bason ketuplak",
                "pesan": "Semangat kuliahnya yh bang hazelll!!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                 "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya diem-diem, manis, cantik",
                "pesan": "Sehat dan semangat terus kakaaaa"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani ",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang ",
                "alamat": "Jl. Lapas",
                "hobbi": "nonton film,musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "kakanya humble dan manis",
                "pesan": "semangat kuliahnya kak dwiiii"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSenator()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-Q9UjmlH_LgzZETxZyEtc08j9l16KBvu",#arini
            "https://drive.google.com/uc?export=view&id=1dHVaR-Hrh2Z1GoIzrW_DhHRi1H_TWGQj",#nabila
            "https://drive.google.com/uc?export=view&id=1XZI2tcrIryyRZYjlx-WksD_tIaUA-V-P",#aditya
            "https://drive.google.com/uc?export=view&id=13MyhjkPEtTeV46M-3Q64mRZMNJ1VTJWt",#Fathya
            "https://drive.google.com/uc?export=view&id=15FkNDI14ZB__pckuJtJd-G83JT5S06qy",#Tarisya
            "https://drive.google.com/uc?export=view&id=1u-6sX89Oa6P6nPI03R-cK-vI9kI2NIhz",#selma
            "https://drive.google.com/uc?export=view&id=1_HMVqOnrLgJhGke2M1-zDQLwLKQNeN_O",#ashila
            "https://drive.google.com/uc?export=view&id=15bh9V0JjCEmaUrjZwOvBZP8twCzWcrTB",#danil
            "https://drive.google.com/uc?export=view&id=10D78T1aNIue8-0gTfN2AghcgFDrG--uj",#favian
            "https://drive.google.com/uc?export=view&id=18vWbMwEn89pKeh13lQACGNoEPlkQQql4",#yazid
            "https://drive.google.com/uc?export=view&id=1CxYdfTuMvvw74LU_DgQYhgiMPfd4yb56",#zaldi
            "https://drive.google.com/uc?export=view&id=16ltm-7Omk3jalvtF3PMG2z6maAnxKksR",#saskia
            "https://drive.google.com/uc?export=view&id=19zO6nGqBNY8zs2nDw26CSbDjBguC0Iuu",#mut
            "https://drive.google.com/uc?export=view&id=1-Q9UjmlH_LgzZETxZyEtc08j9l16KBvu",#ahmad
            "https://drive.google.com/uc?export=view&id=16rweT_PV-nwiC8Sqh2hUhCR3fJoAKWoE",#indah
            "https://drive.google.com/uc?export=view&id=1ZH3_dsPx8ZxdIOBu5hcBmagv6RyMtR2b",#bima
            "https://drive.google.com/uc?export=view&id=1OjdlggrVm5Iz-0v2Ab-O_1ifS6vPmobJ",#bimo
            "https://drive.google.com/uc?export=view&id=1hEjV925A3vGaZBvHRxsIWy9jgKvRQyGp",#dinda
            "https://drive.google.com/uc?export=view&id=10L7UmTu7uAaZ0d54ESlCIyIeOLZNHR6o",#yola
            "https://drive.google.com/uc?export=view&id=1TTdOWlY7O32JpTXNT9hE6_eFp0hmeMSs",#riska
            "https://drive.google.com/uc?export=view&id=1rliPToEuFH4_KR1uUvRcPAU4jESoHh2u",#alfaya
            "https://drive.google.com/uc?export=view&id=14nWPfkddCZf1oz4uKNXrUvOY3QDVK60-",#meilani

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
                "kesan": "Kaka pemandu keren",
                "pesan": "Semangat ya kakaa kuliahnyaa"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kaka imut bangetttt",
                "pesan": "semangat terus kakaaaaa"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "Abangnya cheerfull, humble, dan mengayomi",
                "pesan": "Semoga abang bahgia terus yaaaaa"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "kak fathya baikkkkkk huhu",
                "pesan": "semangat kuliahnyaaa kakk"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                 "nim": "123450052",
                "umur": "-",
                "asal": "Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "tari_",
                "kesan": "Kakanya seruuwww",
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
                "kesan": "kakanya maniss",
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
                "kesan": "kakanya ramah, bintang 5!!",
                "pesan": "Bahagia selaluuu kakakkkkk"# 1
            },
            {
                "nama": "Danil Nur Fadillah",
                "nim": "124450103",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Bang danil mirip aktor di drakor ",
                "pesan": "Semangat terus kuliahnya bang danilll"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "abangnya terlihat asik hehehe",
                "pesan": "semoga selalu bahagia ya bang faviann"# 1
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20 ",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "abangnya baik hehehe",
                "pesan": "Semangat kuliahnya bang yazidd"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah ",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "tanyain sama yuder",
                "sosmed": "@jaldii._",
                "kesan": "Abang ini asik, lucu, ceriaa",
                "pesan": "Semangat terus ya bang jaldi, semoga abang sehat dan bahagia selaluu"# 1
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
                "pesan": "sehat2 kakaaa, bahagia selalu ya kak"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakanya baikkkk, humble",
                "pesan": "semangat pimnasnya kak muttt, ak bangga"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                 "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Inilah bintang data kita",
                "pesan": "Semangat terus bang kuliahnya, semoga segala urusan abang dilancarkan sebagaimana abang bantu menyuarakan hak-hak kita semua"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kaka medis baikk",
                "pesan": "Semoga kaka bahagia selalu dan sehat selalu ya kaka mediss"# 1
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung ",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Abangnya terlihat seru sihh",
                "pesan": "Semangat bang bimaaaa kuliahnyaaa"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus ",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Kirip siapa gitu abangnya, tp gatau mirip siapa",
                "pesan": "Bahagia selalu abangg"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "21",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "kakanyaa canciiii",
                "pesan": "Semoga dilancarin terus ya kak urusan kaka"# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "21",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Nyari duit",
                "sosmed": "@yollanda_agustina16",
                "kesan": "ceriaa bangettt",
                "pesan": "jangan lupa jaga Kesehatan kakaaaa, semangatt"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                 "umur": "20",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "KAKA TERIMUT, BAIK HATI, MENTOR YANG HEBAT, BEST MENTOR, SOLUTIF, INSPIRATIF, LOVEEEEE KA RISKAAAAAAAAAA",
                "pesan": "Bak mentari pagi yang membelah keheningan fajar, Hadirmu menyapu dingin dan ragu di dada kami. Wajahmu elok nan imut, bagai kelopak mawar yang baru mekar, Memancarkan pesona yang meneduhkan tiap pasang mata yang memandang. Namun bagaikan samudra yang menyimpan permata di kedalamannya, Kecantikan parasmu hanyalah awal dari keagungan hatimu. Usiamu muda, namun kasihmu bak dekap hangat seorang ibu; Ibarat embun yang membasahi pucuk-pucuk daun di kala subuh, Nasihatmu menyejukkan gelisah, merawat jiwa kami yang sedang bertumbuh. Wahai Kak Riska, sang pembimbing berhati mulia, Kaderisasi ini bak belantara luas yang tak lagi menakutkan, Sebab engkau hadir bagai kompas nan lembut, Menuntun tiap langkah kami menuju cahaya. Terima kasih atas segala tulus yang tak pernah usai, Semoga bahagiamu seluas angkasa yang tak bertepi!"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Abang ini sering ditemukan bareng seorang kaka datasena wkwkwk",
                "pesan": "Semoga bahagia terus yhhh bangggggg"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kaka ini sgt positive vibe, aku inget pernah diajak mirror selfie di toilet pas dsc hihihi",
                "pesan": "Semoga kaka bahagia selaluuu, sehat selaluuuuuu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Pk49V9dhDBC3bwAAJ3thLLzjBBJaAefo",#fabio
            "https://drive.google.com/uc?export=view&id=1RREsNfYncEgKsOlVmj31ts1estXpVJwn",#tanty
            "https://drive.google.com/uc?export=view&id=1wHB03qgD7mRiL-s1hBTDNLem-da7UGpf",#fadil prasetyo
            "https://drive.google.com/uc?export=view&id=10Qzpx1sY7SvWIWMiz94Jsmtce-d_-cdh",#manuelle
            "https://drive.google.com/uc?export=view&id=1NE-YL_16rH5ehZWNwcHlyd66C0Rl88wD",#ni made
            "https://drive.google.com/uc?export=view&id=1Piq6fGhbCUG0N5LgbQHKB79nfOZfSqJl",#risa
            "https://drive.google.com/uc?export=view&id=1Kpc4Fiu5oQfsUcnAEp5_eZYUiheB7wYb",#vaniisa
            "https://drive.google.com/uc?export=view&id=",#yulia
            "https://drive.google.com/uc?export=view&id=1QdwKsnfkeRRcTx4f-8fAUG01wmrcCNve",#akeyla
            "https://drive.google.com/uc?export=view&id=1cHQHiTXFqTVvOUAATJBtjXcSrj9_BmME",#elsa
            "https://drive.google.com/uc?export=view&id=1ZQWoXmK3IYJlqTtSzk9s5TMW8HHBRSfb",#fadia
            "https://drive.google.com/uc?export=view&id=ZehoByx0vDHB35YOcrVj-0AeA9xe_Td6",#lovia
            "https://drive.google.com/uc?export=view&id=1QJQZ8mz8Q-8WtQ6S7_DKqnAErFjfVxE-",#alsi
            "https://drive.google.com/uc?export=view&id=",#sherena
            "https://drive.google.com/uc?export=view&id=1PQsUvtx1oWa8ZjCssMMqvC2t4xBm4M2F",#razin
            "https://drive.google.com/uc?export=view&id=1asIBY8hj-UBI3y_iDzQhSnKKUsxYCPDZ",#Faiza
            "https://drive.google.com/uc?export=view&id=1MfY3vLRBj_wR9i4Z6ErQ_AtGg3u6HCk5",#gathan
            "https://drive.google.com/uc?export=view&id=1qinu6b94auvfRWkL5UwEVX9MAGK-l-q_",#hafidz
            "https://drive.google.com/uc?export=view&id=1lj_y2UvhZtdJu-OHpr2GtysiC-hNCdux",#kaleb
            "https://drive.google.com/uc?export=view&id=1ziZGR_D8VNf_SfuxNG7b27LU2gF_evd7",#melva
            "https://drive.google.com/uc?export=view&id=1S9p1ID8t3bAK_AFhTQyKI0G2VR-jZMOa",#syafiq
            "https://drive.google.com/uc?export=view&id=1DqteH52BfSe-uQiJv77-HxMTQc_OiMth",#henri

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
                "kesan": "Bang Fabio ini terlihat orang pinternyaaa dan humble jugaaaa",
                "pesan": "Tetap semangat yaaa banggggg kuliahnyaa, semoga sukses selalu"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Nonton film",
                "sosmed": "@tvnty_",
                "kesan": "Kaka ini lucuu bangettttttt, ekspresifff, sukaa",
                "pesan": "Tetap semangat yaaa kaka, semoga sukses selalu"# 1
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Bang fadil orang yang baik, inspiratif, dan humble",
                "pesan": "Terimakasih sudah jadi orang baik dan bermanfaat buat banyak orang selama hidup yaa bang fadil, aku seneng pernah kenal sama bang fadil. Semoga kita bisa ketemu lagi yaa in another universe bangg"# 1
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis ",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "abangnya asikkk",
                "pesan": "Tetap semangat bang, semoga sukses selalu menyertai abang."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12",
                "asal": "Bali",
                "alamat": "nusa peninda",
                "hobbi": "menghayal",
                "sosmed": "@violaadrtr_",
                "kesan": "Kakanya manis bangettt trus keliatan ramahhh",
                "pesan": "Semangat terus kak urusannya, sehat dan bahagia selaluuu"# 1
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Keren banget hobinya, kakanya juga asikkk",
                "pesan": "Lancar terus kuliahnya ya kak, semangattt"# 1
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "1244500078",
                "umur": "19",
                "asal": "kepulauan riau",
                "alamat": "teluk betung",
                "hobbi": "nonton khw",
                "sosmed": "@vunnycaa",
                "kesan": "Kakanya keliatan ramahhh",
                "pesan": "Semoga bahagia selalu dan lancar terus kuliahnya ya kakaaa"# 1
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Keliatan pinter dan ambis banget kakanyaaa",
                "pesan": "Semangat terus kuliahnya kak, sukses selalu untuk urusannya"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya keliatan sporty dan asik banget diajak ngobrol",
                "pesan": "Semangat terus kuliahnya ya abangg, sukses selalu"# 1
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara ",
                "alamat": "Pemda",
                "hobbi": "Sibuk",
                "sosmed": "@_els.a",
                "kesan": "Kakanya sibuk banget tapi tetep keliatan ramahhh",
                "pesan": "Jangan lupa jaga kesehatan kakaaaa, semangatt"# 1
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "airan",
                "hobbi": "mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Hobinya unik banget, kakanya keliatan ceriaaa",
                "pesan": "Semoga dilancarin terus ya kak urusan kaka"# 1
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "Kakanya keliatan chill dan baikkk banget",
                "pesan": "Lancar terus kuliahnya ya kak, semangattt"# 1
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "kalianda",
                "alamat": "kota baru",
                "hobbi": "main game, tidur",
                "sosmed": "@aluccy_",
                "kesan": "Abangnya santai banget tapi keliatan humble",
                "pesan": "Semangat bang kuliahnyaaa, sukses selalu ya bang"# 1
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kakanyaa canciiii dan keliatan rapiii",
                "pesan": "Semoga sehat dan bahagia selalu ya kakaaa"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya keren dan keliatan seru sihh",
                "pesan": "Bahagia selalu abangg, dilancarkan kuliahnya"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel ",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakanya keliatan kalem dan manisss banget",
                "pesan": "Semoga dilancarin terus urusan dan kuliahnya kaka"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Rajabasa Raya",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Abangnya baik dan keliatan santaiii",
                "pesan": "Semangat bang kuliahnyaaa, sukses selalu"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur ",
                "hobbi": "3N ( Ngoding , Ngegame, Nyibukin Diri)",
                "sosmed": "@apiszzaja",
                "kesan": "Keliatan pinter banget abangnya, mana pekerja keras gituuu",
                "pesan": "Semoga segala urusan akademis dan organisasi dilancarkan sampai lulus ya abangg"# 1
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Campang Raya, Sukabumi",
                "hobbi": "Gym, membaca, dan bermain",
                "sosmed": "@kelelep_comberan",
                "kesan": "Username sosmednya kocak, tapi abangnya keren bangettt",
                "pesan": "Semangat terus bang, semoga lancar kuliahnya"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan ",
                "alamat": "Sukarame ",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakanya manis dan keliatan keibuan bangettt",
                "pesan": "Semangat terus kuliahnya kak, sehat selalu ya kakaaa"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syafiqui",
                "kesan": "Abangnya keliatan tenang dan bijak sihh",
                "pesan": "Bahagia selalu abangg, lancar terus urusannya"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal": "Kotabumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "Hobinya unik, tapi abangnya asik dan kocak sihh",
                "pesan": "Semangat terus bang, sukses selalu untuk kuliahnya"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1X64Dk7Z6tyBP-jM7L8VvrxoKCfy-EAFH",#ihsan
            "https://drive.google.com/uc?export=view&id=1fPwsh8QOJb0TEye3LYiem3PUoUUx3l57",#naya
            "https://drive.google.com/uc?export=view&id=1ly-cMpEtbGKr9zUtg0MWA2IIXiHmtC0G",#afifah
            "https://drive.google.com/uc?export=view&id=1Wt2X0cfy5oMj1j6Xk4-H1h0cNh_NE7w3",#hasan
            "https://drive.google.com/uc?export=view&id=1Fv8x3h6COGaIpy10u2y2Mc0LDUEcGWuE",#layina
            "https://drive.google.com/uc?export=view&id=1UHT5iOhe4a6KFs1t_9lpXQrLHbCMwTC5",#iqbal
            "https://drive.google.com/uc?export=view&id=1unR3WyfN3isfxkbZ5Q8b5pKNBO-RFbRZ",#talitha
            "https://drive.google.com/uc?export=view&id=19XKy3gyx7Jt8Jszmt5lB_uGpxjzS5g9V",#anadia
            "https://drive.google.com/uc?export=view&id=1hMb-cdKXFpdh5mDIuODvVcDvNB9BKjM8",#pome
            "https://drive.google.com/uc?export=view&id=",#afdhal
            "https://drive.google.com/uc?export=view&id=1igEnypMq9AJIMJ2poKfWddkv-eupJGbc",#anggun
            "https://drive.google.com/uc?export=view&id=1FnFIm7I5XfK9IevjbjbTGB4sgXL9mRKv",#della


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
                "kesan": "Abangnya keren banget keliatan berjiwa entrepreneur sihh",
                "pesan": "Semoga bisnis dan kuliahnya sama-sama lancar ya abangg"# 1
            },
            {
                "nama": "hanifah inaya sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakanya keliatan lembut dan baikk bangettt",
                "pesan": "Lancar terus urusan kuliahnya ya kak, sehat selaluuu"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kakanya keliatan ramah dan seru diajak ngobrol",
                "pesan": "Semoga makin sukses dan bahagia selalu ya kakaaa"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Abangnya keliatan tenang dan mature bangettt",
                "pesan": "Sukses terus buat karir dan kuliahnya ya abangg"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin",
                "sosmed": "@lay.inr_",
                "kesan": "Kakanyaa canciiii dan keliatan humble",
                "pesan": "Semangat terus kuliahnya kak, jangan lupa bahagiaaa"# 1
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Abangnya chill banget dan keliatan gampang akrab",
                "pesan": "Semoga dilancarin terus urusan kuliahnya ya abangg"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "...",
                "kesan": "Kakanya manis banget dan keliatan rapiii",
                "pesan": "Semoga sehat selalu dan lancar terus kuliahnya ya kakaaa"# 1
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakanya pekerja keras dan keliatan ambis bangettt",
                "pesan": "Semoga selalu dimudahkan rezeki dan kuliahnya ya kak"# 1
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "Abangnya keliatan sporty dan wibawa sihh",
                "pesan": "Bahagia selalu abangg, semangat kuliah dan basketnya"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "Abangnya keliatan santai tapi baikkk banget",
                "pesan": "Semangat bang kuliahnyaaa, sukses selalu kedepannya"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakanya cute banget dan keliatan ceriaaa",
                "pesan": "Jangan lupa jaga kesehatan kakaaaa, semangatt"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakanya keliatan manis dan ramahhh banget",
                "pesan": "Semoga dilancarin terus ya kak urusan dan kuliahnya kaka"# 1
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":#DONE
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TAu3oBd11aViOgcUl8lVjNcuu1gjR7bv",#nayla
            "https://drive.google.com/uc?export=view&id=1kr0p2Ntlufac4-i6i3cxnE5ZLrjbqaP1",#donna
            "https://drive.google.com/uc?export=view&id=1U4Nft16Dq6BRFO-TS3OYBarXMywr8k2x",#labo
            "https://drive.google.com/uc?export=view&id=1pZs5cCB10bgu5AAMpxpAGEhPJ9ic99_F",#anash
            "https://drive.google.com/uc?export=view&id=1hmA1-t305P9MSWGA9BCo2OHQmL4o3hhK",#felisya
            "https://drive.google.com/uc?export=view&id=1OmtC17ZVQBPCylWzmBELdX4LPBsYyv0h",#razan
            "https://drive.google.com/uc?export=view&id=1Cbo64Lp2w5HfsYzPBOKklR4AeuY88gib",#sania
            "https://drive.google.com/uc?export=view&id=1txGqJCD1QOLaZwUhfTftIuSwiP_0qLhE",#allisha
            "https://drive.google.com/uc?export=view&id=18Xy_x6eQ_KFrypf0juh7ugl9adxWbqKT",#alya
            "https://drive.google.com/uc?export=view&id=1EaduuCuWSToRQKcZYprgRXBVeYjFPvsQ",#bunga
            "https://drive.google.com/uc?export=view&id=1SGvrW_5wmvl6GYwe-hpPYdNZdH61FVEU",#difa
            "https://drive.google.com/uc?export=view&id=1792f0D7IA7SHNhpHoVnG1I-I73dLqY_j",#nazlah
            "https://drive.google.com/uc?export=view&id=1rUJ0NR23xAkB9IHJbEwNMQaJW-6O7-w8",#raihana
            "https://drive.google.com/uc?export=view&id=1DDOBQl_laCx8zXMnRQYzdHAe_iNhQxWK",#daffa
            "https://drive.google.com/uc?export=view&id=1aGFSWZrreJ1JHPFtqWOsNI-lDcIOxjGM",#edsel
            "https://drive.google.com/uc?export=view&id=1a2eoIPds8LmHSSpmN7ha1IRuuiHUub7x",#lucia
            "https://drive.google.com/uc?export=view&id=",#shafa
            "https://drive.google.com/uc?export=view&id=1elByhilJdS3-K_5K5ebuio728iHzgOCQ",#zannoba

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
                "kesan": "Kakanyaa manisss banget dan keliatan ramahhh",
                "pesan": "Lancar terus kuliahnya ya kak, sehat dan bahagia selaluuu"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakanya keliatan chill dan baikkk banget",
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
                "kesan": "Abangnya keren dan keliatan asik diajak ngobrol",
                "pesan": "Semangat bang kuliahnyaaa, sukses selalu ya bang"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Way Halim ",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakanyaa canciiii banget dan cuteee",
                "pesan": "Semoga dilancarin terus urusan dan kuliahnya kaka"
            },
            {
                "nama": "Felisya Nabila Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal": "Lampung Timur ",
                "alamat": "Kota Baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "Hobinya kocak banget, kakanya seru dan ramahhh",
                "pesan": "Bahagia selalu ya kak, semangat terus kuliahnyaaa"# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "21",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "Abangnya keliatan santai tapi keren bangettt",
                "pesan": "Semangat terus bang, sukses selalu untuk kuliahnya"# 1
            },
            {
                "nama": "Sania DWi Ayu Lestari",
                "nim": "124450086",
                "umur": "21",
                "asal": "Karawang ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakanya manis banget trus keliatan humble",
                "pesan": "Semoga bahagia selalu dan lancar terus kuliahnya ya kakaaa"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "Biodatanya konyol banget, kakanya keliatan ceriaaa",
                "pesan": "Jangan lupa jaga kesehatan kakaaaa, semangatt"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakanya cantik, ramahh dan keliatan asikkk",
                "pesan": "Semoga dilancarin terus ya kak urusan kaka"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakanya cantik banget dan keliatan pinterrr",
                "pesan": "Semangat terus kuliahnya kak, sehat selalu ya kakaaa"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Alquran",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakanya keliatan adem, kalem, dan baikkk banget",
                "pesan": "Semoga segala urusannya dilancarkan selalu ya kakaaa"# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@nzlhauly_",
                "kesan": "Kakanyaa canciiii dan imuttt banget",
                "pesan": "Lancar terus kuliahnya ya kak, semangattt"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Aira Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kakanya keliatan pinter dan ramahhh banget",
                "pesan": "Semoga sehat dan bahagia selalu ya kakaaa"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame ",
                "hobbi": "-",
                "sosmed": "@daffascript",
                "kesan": "Abangnya keliatan santai tapi pinter ngoding sihh",
                "pesan": "Bahagia selalu abangg, semangat terus kuliahnya"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "Abangnya keliatan seru sihh dan asik diajak ngobrol",
                "pesan": "Semangat bang bimaaaa kuliahnyaaa, sukses selalu"# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Kakanya gemass banget dan cantikkk bgt",
                "pesan": "Semoga dilancarin terus urusan dan kuliahnya kaka"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis dan menulis",
                "sosmed": "@_shaazzh",
                "kesan": "Kakanya artistik banget dan keliatan ramahhh",
                "pesan": "Semangat terus kuliahnya kak, sukses selalu untuk urusannya"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "Hobinya lucu, kakanya manis dan baikkk banget",
                "pesan": "Jangan lupa bahagia selalu ya kakaaa, semangattt"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
# Tambahkan menu lainnya sesuai kebutuhan
