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
            "https://drive.google.com/uc?export=view&id=1Mvj4tDoyJuPkMWIYokSDNEyRcHUTKoN6",
            "https://drive.google.com/uc?export=view&id=1Kx6f3HY2PN-blpsA5vkhV2wFCf9kxFAm",
            "https://drive.google.com/uc?export=view&id=1K0ARtrEq5RkZBl1qqLC8sv90FAG8soyb",
            "https://drive.google.com/uc?export=view&id=1v3FhepfnYaMfMaVLdrM8cK7dObqhJJtJ",
            "https://drive.google.com/uc?export=view&id=1nSBFxZu3Ne7RWq7Fx5CAETiHynpV6_6-",
            "https://drive.google.com/uc?export=view&id=1XwsNoQHKTeBvDAU7j0NszAx0CA7D3ATB",
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
                "kesan": "Bang Fajar orangnya bijak dan berwibawa banget",  
                "pesan":"Semoga kedepannya Bang Fajar bisa terus mengisnpirasi kita semua"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil keren banget, asik, idola basket",  
                "pesan":"Semoga kedepannnya terus berdzikir dan menjadi orang keren"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi orangnya baik dan ramah",  
                "pesan":"Semoga Kak Efi terus berkembang dan suskes selalu"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois orangnya baik dan suka membantu",  
                "pesan":"Semoga kedepannya bisa terus mengispirasi dan menjadi orang yang hebat"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa orangnya seru dan baik banget",  
                "pesan":"Semoga kedepannya Kak Hafsa terus menjadi orang yang keren dan sukses"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak Luthfia orangnya imut dan lucu",  
                "pesan":"Semoga kedepannya Kak Luthfia terus berkembang dan terus menjadi lucu dan imut"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1A9n8cKpNT1QjMeNMMWz6JQLyPs6pAay0",
            "https://drive.google.com/uc?export=view&id=1e44m-C0WWdEUmzKdHlDTU-0IGAAJ8cOd",
            "https://drive.google.com/uc?export=view&id=1WZzOzXuoqzGUZC57292c2M4yQmqunEtt",
            "https://drive.google.com/uc?export=view&id=1tqWRkZlE0naShb568mWwy3jUOpiDl9cs",
            "https://drive.google.com/uc?export=view&id=1vzwAX-Z9ES29rrn6GTiqpCjOEl8BEgDG",
            "https://drive.google.com/uc?export=view&id=1I-kf5KKFOqlzx716yTpWylUGsauMPO0a",
            "https://drive.google.com/uc?export=view&id=1xuGp1UKzJfIry6-6fwN6EhrN2sNxaERj",
            "https://drive.google.com/uc?export=view&id=1xUcPeK7kzME93Ub2P0Li1z_IBYuRhPyy",
            "https://drive.google.com/uc?export=view&id=13tphyUeQ4gKSqzOFJ4N-23SkVkMtgaIN",
            "https://drive.google.com/uc?export=view&id=1ad1uk4q-JlqlcN4PFBcBoNB4_D414cKp",
            "https://drive.google.com/uc?export=view&id=1tyolbY-KsMgsajQFoLQU2giTU0q3ALws",
            "https://drive.google.com/uc?export=view&id=1W3rODDWeH1r7bVnKtdNkfHQ63C5faqNb",
            "https://drive.google.com/uc?export=view&id=1ePUb3hA463FPWMOM6p0fBjLT9Lmca7hP",

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
                "kesan": "Bang Ridho orangnya bijaksana banget dan lucu juga",  
                "pesan":"Semoga kedepannya Bang Ridho makin sukses"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue mentor tpb terbaikk",  
                "pesan":"Semangat terus kak, semoga lulus tepat waktu dan sukses  selalu"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Asik dan seru banget orangnya",  
                "pesan":"Semangat terus bang, semoga projeknya makin sukses"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Keren dan jago basket",  
                "pesan":"Sukses terus, dan lebih berkembang untuk kedepannya"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Ramah dan baik banget kakaknya",  
                "pesan":"Semangat terus kak,sehat selalu dan sukses"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Abang ini keren dan pinter banget",  
                "pesan":"Sukses terus dan semangat kuliahnya bang"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakak ini pinter banget, tutor metnumm fav",  
                "pesan":"Semangat terus, dan semoga perkuliahannya lancar selalu kak"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya lucu dan asik",  
                "pesan":"Semoga kuliahnya lancar dan sukses terus"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Penyanyi handal dan asik abangnya",  
                "pesan":"Sukses terus dan semangat kuliahnya bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Baik banget kakaknya",  
                "pesan":"Semoga hidupya diberi keberkahan dan kelancaran selalu"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Hobinya keren dan unik",  
                "pesan":"Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Asik dan baik banget",  
                "pesan":"Semoga kuliahnya selalu lancar dan sukses"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya asik dan seru",  
                "pesan":"Semoga hidupya diberi keberkahan dan dipermudah di segala hal"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cqg2oc5399BNRU_N5vf72JmTQiRjvBxz",
            "https://drive.google.com/uc?export=view&id=1ccLpTN_qsEM2W_K1EOR4Bq5VDHsQb477",
            "https://drive.google.com/uc?export=view&id=1mK5QHtgWM8MqAfcOJ5PkoNJy_X0C2xj7",
            "https://drive.google.com/uc?export=view&id=1w4ZFAdgjb3ejaWj5k6YYx7fbgi-FqXvM",
            "https://drive.google.com/uc?export=view&id=1YIuc9gbI3pkdIf4RwqJjfHqHNpnif3zN",
            "https://drive.google.com/uc?export=view&id=1jSxZ27AUzTDjYep3iihH8TxtMGB-bReq",
            "https://drive.google.com/uc?export=view&id=1--eMSTK6pkST0JPCwsdo3A4rmE-rLrZ_",
            "https://drive.google.com/uc?export=view&id=1pMhnCqlxbWwC3JZecVOo1S6FVJRoqSoD",
            "https://drive.google.com/uc?export=view&id=1Mj-3CkT87ahWIuGVOmc-PgZivA3TiIV1",
            "https://drive.google.com/uc?export=view&id=1n44R8OjCJ3-VxtwUjcYbd_k98kKU3KZt",
            "https://drive.google.com/uc?export=view&id=16Xt1PXIm1VeFCzDC7GSm3EX3JdMG3IMq",#
            "https://drive.google.com/uc?export=view&id=1TAKigJ7_LPXv9hi4MqsfwIiFdQ0MhOF8",
            "https://drive.google.com/uc?export=view&id=14fQZN1kqzNxbjUAuAP0REgKg6qKcyO_Q",
            "https://drive.google.com/uc?export=view&id=1UiSXrUvD1-l193y-Wt8zb6JtfDcCdFoh",
            "https://drive.google.com/uc?export=view&id=1evQIsU_Qlp0LsePkeFZDHd9ldv77Kch3",

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
                "kesan": "Asik dan seru banget, jago basket",  
                "pesan":"Semoga sukses selalu dan makin jago basketnya"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya lucu dan asik",  
                "pesan":"Semangat terus dan sehat selalu"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "@ali_parisi3",
                "kesan": "Baik dan seru banget abangnya",  
                "pesan":"Semoga sehat selalu dan sukses perkuliahannya"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakaknya baik dan asik sekali",  
                "pesan":"Semoga makin berkembang dan sukses"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Asik banget abangnya, jago futsal",  
                "pesan":"Sukses dan sehat selalu buat abangnya"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakaknya lucu dan baik banget",  
                "pesan":"Semoga kuliahnya diberi kelancaran dan sukses selalu"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Lucu dan seru banget abangnya",  
                "pesan":"Makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakaknya baik banget dan seru ngobrolnya",  
                "pesan":"Semoga makin berkembang dan sukses terus untuk kakaknya"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Baik dan supportif banget abangnya",  
                "pesan":"Makin sukses dan berkembang terus buat abangnya"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Coach basket fav, seru dan asik banget",  
                "pesan":"Semoga makin sukses dan makin jago main basketnya"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Abanya baik, dan lucu",  
                "pesan":"Semangat terus dan sehat selalu buat abangnya"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal":"Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Baik dan lucu banget abangnya",  
                "pesan":"Makin semangat dan makin sukses"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakaknya seruu dan baik banget",  
                "pesan":"Sukses terus buat kakaknya"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Baik dan semangat bangett kakaknya",  
                "pesan":"Semoga makin sukses dan makin berkembang"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Seru dan asik banget abangnya",  
                "pesan":"Semoga makin sukses dan sehat selalu buat abangnya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19KqPt-7G9ox0sduIpoa47ByIRNbJCu1W", #bang haikal
            "https://drive.google.com/uc?export=view&id=1Ph5wTIfuIZeZvi08UEQq5eRV8Y0EC6_0", #kak kharisma
            "https://drive.google.com/uc?export=view&id=1en0vKIQSG3KRWILjicY26LaXm_QrAtw9", #kak hanna
            "https://drive.google.com/uc?export=view&id=1B4W635yKfuwzzxRSuWfK7cebNSOIvYee", #bang farhan
            "https://drive.google.com/uc?export=view&id=1pVEZWfCdnvnZtsgDi7SXWL6E1BCtO1dS", #kak aisyah
            "https://drive.google.com/uc?export=view&id=1jAwSAngD6OYu7YpDlJ0DE7ZF271kFxzY", #kak cerine
            "https://drive.google.com/uc?export=view&id=1_k0MwwnNo2xyaAd9Dao9zxdc5vkkTj9q", #bang jaya
            "https://drive.google.com/uc?export=view&id=1H5yJPC9wGAZXG8jcFJfq43essIwbHCDq", #kak najla
            "https://drive.google.com/uc?export=view&id=10pabq75lQc8JwD_HfHyRnjbqiX57EJ7o", #bang rozak
            "https://drive.google.com/uc?export=view&id=17s0r1MaJ2wNLivgQn3zHj4Ll79bpGaAY", #kak teresa
            "https://drive.google.com/uc?export=view&id=1QZDI7lJUN_OUl0bFoNIHKP9yTuaJXkbq", #bang hanif
            "https://drive.google.com/uc?export=view&id=10u1nPbqA_OqxO-6dqZPrUPFjWQ27cdLo", #kak audina
            "https://drive.google.com/uc?export=view&id=1YY8_S1LAfXUE2NeXpXWUDkEYRggHvZAP", #kak cika
            "https://drive.google.com/uc?export=view&id=1RgTwI_Tvq-e-MAky15m1Jn7dLs8FCqas", #kak gustin
            "https://drive.google.com/uc?export=view&id=1oMlx0Y8Mce8R_HUVpIMDH0JuGxJ_Gpys", #bang harvinsyah
            "https://drive.google.com/uc?export=view&id=1WwbubkFFBu4zqWEw8WpUoyAfVGi7sWPx", #kak rafa

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
                "kesan": "Abangnya asik dan suka merokok",  
                "pesan":"Semoga makin sukses dan sehat selalu buat abangnya"# 1
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
                "kesan": "Kakaknya baik, senyumnya lucu banget",  
                "pesan":"Semakin berkembang dan sukses kak"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan orangnya asik dan jago basket",  
                "pesan":"Makin sukses dan motornya makin keren"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Baik dan seruu banget kakaknya",  
                "pesan":"Semoga makin sukses dan semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kak cerine orangnya seru dan ceria",  
                "pesan":"Makin berkembang dan sehat selalu buat kakaknya"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya orangnya seru dan jago basket juga",  
                "pesan":"Makin sukses dan berkembang untuk kedepannya"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya baik dan lucu",  
                "pesan":"Makin berkembang dan sukses perkuliahannya"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "Keren dan asik abangya",  
                "pesan":"Semangat terus buat abangnya"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "masak",
                "sosmed": "@christiani8872",
                "kesan": "Kakaknya baik banget dan senyumnya lucu",  
                "pesan":"Semangat terus buat kakaknya, semoga makin sukses"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Seru, asik, dan lucu abangnya",  
                "pesan":"Selalu semangat dan terus berkembang buat abangnya"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Bima",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Lucu dan baik banget kakaknya",  
                "pesan":"Semoga makin sukses dan bahagia selalu"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kakaknya baik banget dan asik sekali",  
                "pesan":"Semangat terus buat kakaknya, semoga makin sukses, dan sehat selalu"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "airan",
                "hobbi": "nonton",
                "sosmed": "@gustin.tpb",
                "kesan": "Kakaknya lucu, baik, dan ramah sekali",  
                "pesan":"Semangat teruss buat kakaknya, semoga makin berkemban dan sukses"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Abangnya baik dan ramah banget",  
                "pesan":"Semangat dan makin sukses selalu"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "nginep di rumah kak yollanda",
                "sosmed": "@snasaa._",
                "kesan": "Kakaknay seru dan asik",  
                "pesan":"Semangat terus buat kakaknya, semoga makin sukses, dan sehat selalu"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Y3vcyfOJQRnFtUQaEqdH3x5KfDKXkCY-", #kak arienta
            "https://drive.google.com/uc?export=view&id=1844MFmmgAKdz2QnHm_NoUN48f8oyrqUp", #kak vany
            "https://drive.google.com/uc?export=view&id=1tjC1fUf4_5_GALWjxZ24M-IXxISa8W0j", #bang nobel
            "https://drive.google.com/uc?export=view&id=17Q7ZY7Jzayrpbw-1Y4S_icnB4IOknH6C", #bang azmi
            "https://drive.google.com/uc?export=view&id=1peZkeZvKPoWv3GCZF19ivu93IECYV4tA", #bang ayake
            "https://drive.google.com/uc?export=view&id=13gY82xeuQH5X4QjjlMrIOe2ynPSeBM1G", #bang caesar
            "https://drive.google.com/uc?export=view&id=1rxyIeYZl-l2_2CA3wVi_-E9uR9SZOCxe", #kak euodia
            "https://drive.google.com/uc?export=view&id=1XQw0X1R6uyCXfMX2KBKuvjQ9lOu6puKn", #bang haikal
            "https://drive.google.com/uc?export=view&id=1PZMDd59U2FmXEGgVk6xNd84kisEOFj3r", #kak putri
            "https://drive.google.com/uc?export=view&id=1HFa7avyd7bEM690PXXLUwvHpTYl8EQxU", #kak queenta
            "https://drive.google.com/uc?export=view&id=1HWrrOHZ52oGxsK2A_WAcUZclwGz5YMVY", #bang desman
            "https://drive.google.com/uc?export=view&id=1o54aiI5ZGcplDNJUWfHEUq-UVSX3L17f", #kak azzelya
            "https://drive.google.com/uc?export=view&id=1FU6F8Fvk8DOl-KEXaCh0zD0S0jkA3qpM", #kak charrlindah
            "https://drive.google.com/uc?export=view&id=16WWclUsSIMkwxMbALOlEhOITpxzvMdo_", #bang jeremi
            "https://drive.google.com/uc?export=view&id=1OH5DsiP4p9o2xBIDcV3Cj5z9GdpQlFPy", #kak nabila
            "https://drive.google.com/uc?export=view&id=1XSg4M-poq0VL4YsSALwfri591NsH13Lo", #bang rafli
            "https://drive.google.com/uc?export=view&id=1QgQjDTJ5IM3vGd4GD0N8cmez4HgkKbpr", #kak salavi

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
                "kesan": "Kakaknya baik, dan pembimbing",  
                "pesan":"Sehat selalu dan dipermudah urusannya"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Baik dan lucu kakaknya",  
                "pesan":"Makin sukses dan terus berkemmbang buat kakak nim kuh"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Jago sulap dan profesional abangnya",  
                "pesan":"Semoga makin sukses dan dipermudah segala urusannya"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Seru dan paling semangat pas supporteran",  
                "pesan":"Sukses terus dan sehar selalu buat abangnya"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Ramah dan baik abangnya",  
                "pesan":"Makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Humble dan keren abangnya",  
                "pesan":"Semoga semakin berkembang dan makin sukses"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Seru dan asik kakaknya",  
                "pesan":"Semangat terus dalam menjalani kuliahnya dan makin sukses"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Baik dan humble abangnya",  
                "pesan":"Semangat dan sukses buat abangnya"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Baik dan ramah banget kakaknya",  
                "pesan":"Sehat selalu sehat dan sukses buat kakaknya"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@queentanaabila",
                "kesan": "Kakaknya ramah dan baik dan humble",  
                "pesan":"Semoga dipermudah segala urusan dan makin sukses"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Keren dan asik abangnya",  
                "pesan":"Sehat selalu dan sukses buat abangnya"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kakaknya baik, ramah, dan lucu",  
                "pesan":"Semoga makin sukses dan kuliahnya lancar"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Baik dan ramah dan lucu banget kakaknya",  
                "pesan":"Dipermudah segala urusan dan semakin sukses"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Keren dan salah satu penyemangat pas supporteran",  
                "pesan":"Semoga makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal": "Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Baik dan ramah sekali kakaknya",  
                "pesan":"Dipermudah segala urusan dan makin sukses buat kakaknya"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal": "Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Keren dan asik banget abangnya",  
                "pesan":"Sehat selalu dan sukses buat abangnya"# 1
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@avi.nhr",
                "kesan": "Baik dan ramah dan lucu banget kakaknya",  
                "pesan":"Semoga selalu sehat dan sukses menjalani kuliahnya."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
    
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tk102yLNmE242BdeyDA4O_SrPBPR87n_", #kak fathinah
            "https://drive.google.com/uc?export=view&id=1EmeClNhREOJbUU-ipvraoAcNR0tHSXwB", #kak nadya
            "https://drive.google.com/uc?export=view&id=1HvkGb5umZLKda3GYFJl54C9lP8I-t8FO", #kak dwi
            "https://drive.google.com/uc?export=view&id=1GWZeR0rGtNSDFNWcXK_RTGdtZ07jtYu0", #bang helmy
            "https://drive.google.com/uc?export=view&id=1SNvq6JMk6cemFY-IFsuhbdEaZR5QOC1_", #bang fernando
            "https://drive.google.com/uc?export=view&id=1hNB96viy2M0Yj3jZHvK6MybLwW1TOt0V", #kak suci
            "https://drive.google.com/uc?export=view&id=1anQzPoFwLjtWW-jyez6z5DLRx764v9wg", #bang wielman
            "https://drive.google.com/uc?export=view&id=1jdvMjaC97PPm2Dvefg7i33Wy2vrnKchV", #kak hana
            "https://drive.google.com/uc?export=view&id=1I2TXtCo-fEPs9gr69Mb7tP1LWEUP04AT", #kak aqila
            "https://drive.google.com/uc?export=view&id=1s_VX9V8wYkPEQHjScJFegLQ88qBRgCGo", #bang hazel
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
                "kesan": "Kak Fathinah, orangnya baik dan bijak banget",  
                "pesan":"Semoga lulus tepat waktu dan diterima di perusahaan yang diinginkan"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak Nadya orangnya seru dan lucu",  
                "pesan":"Semoga kuliahnya dilancarakan dan sukses terus"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kak Dwi orangnya ramah dan baik",  
                "pesan":"Sehat selalu dan sukses terus"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen Kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Bang Helmy asik banget dan lucuu",  
                "pesan":"Semoga Sukses selalu dan terus semangat"
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tanggerang Kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Bang fernando orangnya seru dan ramah",  
                "pesan":"Sukses terus dan sehat selalu buat abangnya"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Kota Baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia__",
                "kesan": "Kak Suci orangnya asik banget",  
                "pesan":"Semoga diberi kemudahan dalam kuliahnya dan sukses terus"# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Bang Wielman orangnya ramah dan seru",  
                "pesan":"Semoga kuliahnya lancar dan lulut tepat waktu"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jaarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Hana orangnya baik dan ramah",  
                "pesan":"Semoga makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "18",
                "asal":"lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kak Aqila asik dan lucu bangett",  
                "pesan":"Semoga diberikan kesehatan dan dilancarkan semua urusannya"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "Giring Ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abangnya asik, rambutnnya keren parah",  
                "pesan":"Semoga sehat dan sukses selalu buat abangnya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HOD9G7fPExSrCl-U1lbd7ESe-YGrMnXJ",# kak arini
            "https://drive.google.com/uc?export=view&id=152UAeftA-NbN2maO6kF6hBrp9dcgga2w",# kak nabyla
            "https://drive.google.com/uc?export=view&id=174e-f5w8h8iFX6woY5MeEgdmqXt38xYv",# bang adit
            "https://drive.google.com/uc?export=view&id=1YpgLElYG15vbnPXP_5LNLHvbMlNEKGk9",# kak Fathya---
            "https://drive.google.com/uc?export=view&id=1g2Oac7XR7fh0ys_s9RFlWPmRagCT-How",# kak tarisa
            "https://drive.google.com/uc?export=view&id=1ArVRitcs7Bt1LpiPR-nXgFetHLKlQ1HT",# kak selma
            "https://drive.google.com/uc?export=view&id=166YjN0om4u9esBuAI1bfe9nWRmPkst-o",# kak ashila
            "https://drive.google.com/uc?export=view&id=1NZp7XB6ds4Me_qfl75VVApemxqFmosFI",# bang danil
            "https://drive.google.com/uc?export=view&id=18RGRlTqOK80bsn-3bxwKeIlGfoSECksH",# bang vian
            "https://drive.google.com/uc?export=view&id=1w71lastqbi49h4PszghqcQai4JFunCI6",# bang yazid
            "https://drive.google.com/uc?export=view&id=1RkFWA05e8hHa1_h9r8mZX4QRJ-IYweXR",# bang zaldi
            "https://drive.google.com/uc?export=view&id=1BXbsi2NQA7CW-0yJEFqDTTmxUI9QxWhc",# kak saskia
            "https://drive.google.com/uc?export=view&id=1m1n719YU9dIsaP9gl9Yooru17UKUphbJ",# kak muthoharoh
            "https://drive.google.com/uc?export=view&id=1SbItcp4EPVBjh2Jm_HhPveSJuFYVXYZs",# bang ahmad
            "https://drive.google.com/uc?export=view&id=1Q7-adx9kCYjo7LqDRnyHIqHNG1dFu5Ut",# kak indah
            "https://drive.google.com/uc?export=view&id=1Fp4AzpbPf306BO_RLu5iTQOi4N_ldpY0",# bang bima
            "https://drive.google.com/uc?export=view&id=1V0U06tUFEvEbwEDS7uLjuER0UtLhJ_gM",# bang bimo
            "https://drive.google.com/uc?export=view&id=1QPcIs0K34RIeHiFbQ8yalxBd3HEE8lVE",# kak adinda
            "https://drive.google.com/uc?export=view&id=1vnJtc8MLat4NC5y1hxyZXX57nJTinxfg",# kak yollanda
            "https://drive.google.com/uc?export=view&id=1ygStEoFaGVktHCv37n5XH5_unwN5HtXU",# kak riska
            "https://drive.google.com/uc?export=view&id=1_-AXsthApSgg0zrkbIBNX1wmFMnsvr79",# kak riska
            "https://drive.google.com/uc?export=view&id=104QDfEOogj7pZMqfiLGxh8tdjvlbTvIX",# kak mei

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
                "kesan": "Kakaknya baik dan seru banget",
                "pesan": "Semoga makin sukses dan kuliahnya dilancarkan"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya baik dan lucu",
                "pesan": "Sukses terus dan sehat selalu"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "Abangnya keren banget",
                "pesan": "Semoga sukses terus buat abangnya"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Seru dan asik kakaknya",
                "pesan":"Semoga diberi kemudahan di perkuliahannya dan semangat terus kak"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "-",
                "asal": "Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Keren dan ramah banget kakaknya",
                "pesan": "Sehat selalu dan sukses terus kak"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Lucu dan imut banget kakaknya",
                "pesan": "Semoga kuliahnya lancar dan lulus tepat waktu"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "sini",
                "alamat": "jauh pokoknya",
                "hobbi": "tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakaknya lucu dan baik",
                "pesan": "Sehat selalu dan sukses kak"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Abangnya keren dan asik banget, kadiv desain fav",
                "pesan": "Sukses terus dan dilancarkan kuliahnya"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Ramah dan baik banget abangnya",
                "pesan": "Semoga sehat selalu dan sukses terus bang"# 1
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "((15≪1) & 31) ⊕ 10",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Abangnya kerenn, ketuplak sdm fav",
                "pesan": "Sukses terus buat abangnya"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah ",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "tanyain sama yuder",
                "sosmed": "@jaldii._",
                "kesan": "Abangnya imut dan lucu",
                "pesan": "Semoga kuliahnya dipermudah dan lulus tepat waktu"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakaknya lucuu dan ramah banget",
                "pesan":"Semoga diberi kesehatan selalu dan dipermudah urusannya"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya baik dan ramah bangett",
                "pesan": "Semoga kuliahnya lancar selalu"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Abangnya keren dan berwibawa banget",
                "pesan":"Semoga sukses terus dan sehat selalu bang."
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakaknya baik dan imut",
                "pesan": "Semoga makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung ",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Abangnya keren abis",
                "pesan":"Semoga sukses terus dan lancar kuliahnya"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus ",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Abangnya keren dan baik",
                "pesan":"Semoga makin sukses dan sehat terus"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "21",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya ramah bangett",
                "pesan": "Semoga sehat selalu dan sukses terus"# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "21",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Nyari duit",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakaknya baik dan ramah",
                "pesan":"Semoga makin sukses buat kakaknya"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kakaknya baikk baikk bangett, kakanim favv pokoknya",
                "pesan":"Semoga terus berkembang, lulus tepat waktu dan diterima diperusahaan yang diinginkan"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Abangnya baik dan ramah sekali",
                "pesan": "Semgoa kuliahnya dilancarkan dan lulus tepat waktu"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakaknya lucu dan imut",
                "pesan": "Semoga sehat selalu dan sukses terus kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=158PzP1PqWfBqITdWMbWu3laAA4sGs4bP", #bang fabio
            "https://drive.google.com/uc?export=view&id=1J7LOEH-0o6Vc5vvIIrilLfEKRgkF22XV", #kak tanty
            "https://drive.google.com/uc?export=view&id=",#bang fadil
            "https://drive.google.com/uc?export=view&id=1aUq4WH3D_2fYPAMxqmf-M0k4xHw1TWDj", #bang manuel
            "https://drive.google.com/uc?export=view&id=1wk6O5Xj2UA8ZcuZy8wekimem1-sdihjJ", #kak okta
            "https://drive.google.com/uc?export=view&id=1KPwUWokEwKDkG8coUDDa70_RouEUy3zo", #kak risa
            "https://drive.google.com/uc?export=view&id=1q4TG4UwSiBWArr0LkfVMoqslt38M7_fV", #kak vannisa
            "https://drive.google.com/uc?export=view&id=1Kpn3w9dreIoa27wTSF4tne8Tl91ij_T-", #kak yulia
            "https://drive.google.com/uc?export=view&id=1geCYCJeAzIH_3xDUiEhFQwuHZqOWse_A", #bang akeyla
            "https://drive.google.com/uc?export=view&id=1vO0ykWjpIIkAXa4wevF9WYUogsLVFVq-", #kak elsa
            "https://drive.google.com/uc?export=view&id=1MLYrtKBy4SPE93PccQfdHvyWFAGLotS_", #kak fadya
            "https://drive.google.com/uc?export=view&id=1U2HQoIUXyED4wYsmP90YIOzsAs2CYg2O", #kak lavainora
            "https://drive.google.com/uc?export=view&id=1nQcXabnZp98fzW5NTgbcjUc2j5bzyLi_", #bang alsi
            "https://drive.google.com/uc?export=view&id=1D4ak3wIJ0CNilPDBytdqF9f1tm7tTXqV", #kak sherena
            "https://drive.google.com/uc?export=view&id=123bD5OKLA62vWxMW7RW-9wFb8S6lUbsy", #bang razin
            "https://drive.google.com/uc?export=view&id=1EIKG8hE1lDi3GonKhhrmg4rtCHYpJ0Cm", #kak Faiza
            "https://drive.google.com/uc?export=view&id=1JfKpIynh_W21YXmFThUk9VnpctoFVmrC", #bang gathan
            "https://drive.google.com/uc?export=view&id=1sP5WhjooWsFiKHnT0cxeC9vbMlqdsR1j", #bang hafidcz
            "https://drive.google.com/uc?export=view&id=1f2_qwVEXeOwcJlfeO15pJwRADzi5eGWi", #bang kaleb
            "https://drive.google.com/uc?export=view&id=1dJsQJboSAU1KNNpFHNVOubMq41r8jUIc", #kak melva
            "https://drive.google.com/uc?export=view&id=1UdZ62zoGqevZSRfmY2hU21LBJiBlWMFC", #bang syafiq
            "https://drive.google.com/uc?export=view&id=18MlGEj9sCgjHNycFEZJG_F_423xATBtm", #bang henry

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
                "kesan": "Abangnya keren dan asik",
                "pesan": "Semoga kuliahnya dilancarkan dan lulus tepat waktu"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Nonton film",
                "sosmed": "@tvnty_",
                "kesan": "Kakaknya asik dan hiperaktif bangett",
                "pesan": "Semoga makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Abangnya baik dan keren banget",
                "pesan": "Semoga amal ibadah dan kebaikannya diterima di sisi Tuhan Yang Maha Esa"# 1
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis ",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "Abangnya keren dan pinter",
                "pesan": "Sukses selalu buat abangnya"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12",
                "asal": "Bali",
                "alamat": "nusa peninda",
                "hobbi": "menghayal",
                "sosmed": "@violaadrtr_",
                "kesan": "Kakaknya asik dan seru banget",
                "pesan": "Sukses selalu dan semangat terus kuliahnya"# 1
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Kakaknya imut dan rammah",
                "pesan": "Semoga kuliahnya lancar dan lulus tepat waktu"# 1
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "1244500078",
                "umur": "19",
                "asal": "kepulauan riau",
                "alamat": "teluk betung",
                "hobbi": "nonton khw",
                "sosmed": "@vunnycaa",
                "kesan": "Kakaknya baik hati dan asik",
                "pesan": "Semoga selalu diberkahi dan dipermudah segala urusannya"# 1
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Kakaknya lucu dan ramah",
                "pesan": "Semoga semakin sukses dan dilancarkan perkuliahannya"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya keren dan asik",
                "pesan": "Semoga sehat selalu dan sukses"# 1
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara ",
                "alamat": "Pemda",
                "hobbi": "Sibuk",
                "sosmed": "@_els.a",
                "kesan": "Kakaknya seru dan baik",
                "pesan": "Semoga makin sukses dan kuliahnya lancar"# 1
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "airan",
                "hobbi": "mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kakaknya seru dan asik",
                "pesan": "Semoga kuliahnya lancar dan lulus tepat waktu"# 1
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "Kakaknya imut dan menggemaskan",
                "pesan": "Semoga makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "kalianda",
                "alamat": "kota baru",
                "hobbi": "main game, tidur",
                "sosmed": "@aluccy_",
                "kesan": "Abangnya keren dan asik",
                "pesan": "Semoga makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal":"Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kakaknya baik hati dan ramah",
                "pesan":"Sehat selalu dan dipermudah perkuliahannya"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya keren dan jago futsal",
                "pesan":"Semoga makin sukses buat abangnya"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel ",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakaknya baik hati dan lucu",
                "pesan":"Semoga kuliahnya lulus tepat waktu dan diterima di perusahaan yang diinginkan"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Rajabasa Raya",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Abangnya baik dan ramah banget",
                "pesan":"Sukses selalu dan sehat selalu"
            },
{
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur ",
                "hobbi": "3N ( Ngoding , Ngegame, Nyibukin Diri)",
                "sosmed": "@apiszzaja",
                "kesan": "Abangnya lucu dan asiq banget",
                "pesan": "Semoga dipermudah urusannya dan sukses terus"# 1
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Campang Raya, Sukabumi",
                "hobbi": "Gym, membaca, dan bermain",
                "sosmed": "@kelelep_comberan",
                "kesan": "Abangnya keren, pinter ngoding",
                "pesan":"Semoga makin sukses dan sehat selalu"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal":"Sumatera Selatan ",
                "alamat": "Sukarame ",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakaknya baik hati dan ramah sekali",
                "pesan":"Semoga sehat selalu dan semangat terus"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syafiqui",
                "kesan": "Abangnya asik dan pinter berkomunikasi",
                "pesan":"Semoga semakin sukses dan dilancarkan perkuliahannya"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal":"Kotabumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "Abangnya keren dan berwibawa",
                "pesan":"Semoga dipermudah perkuliahannya dan sukses selalu"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1D8lkO_2mfJyzWqgmvNYfEDSDglW_Lzsf", #bang ihsan
            "https://drive.google.com/uc?export=view&id=1uLQ6V4Y8nywYziHkZSY5y9sz-FN4Bb-x", #kak hanifah
            "https://drive.google.com/uc?export=view&id=10_fxuKyGtohR3s4oUfaW3Oyd4OtHAG9W", #kak afifah
            "https://drive.google.com/uc?export=view&id=1M6ce0JwoayGzfmSpRrPsNCtXPdDxo7NK", #bang hasan
            "https://drive.google.com/uc?export=view&id=1-UcjRLzCCfUfNMc4wnSHrPKg186ngbqd", #kak layina
            "https://drive.google.com/uc?export=view&id=1_HWWyddh0m3p_gmEKrcA0r3Pro6FlaIA", #bang iqbal
            "https://drive.google.com/uc?export=view&id=1Lknnq3WH6ymosiyOZp3bg_R4yG15Pp40", #kak talitha
            "https://drive.google.com/uc?export=view&id=1g_UKLYgGRCD7dq0t9-RZ6uZPxF-KeszA", #kak carana
            "https://drive.google.com/uc?export=view&id=1wrue2G6PZJKbn4h8cd3CbRUWCNn7z4rP", #bang pome
            "https://drive.google.com/uc?export=view&id=1IVXyvdDL_If-UuQgMoIic4nv-2eo0CxJ", #bang afdhal
            "https://drive.google.com/uc?export=view&id=1bcLPDpb-P2TsDEc5HeHeGGDpS2QKm9HA", #kak anggun 
            "https://drive.google.com/uc?export=view&id=10uLhOGpWld_nxHug3qiaKRQdyy0g1_8E", #kak della


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
                "kesan": "Abangnya asik dan ramah banget, risolnya enak",
                "pesan": "Semoga makin sukses dan semoga isian risolnya semakin melimpah"# 1
            },
            {
                "nama": "hanifah inaya sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya baik hati dan lucu",
                "pesan": "Semoga makin suskses dan terus berkembang"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya seru dan asik",
                "pesan": "Makin semangat kuliahnya dan sukses selalu"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Abangnya pendiem dan seru",
                "pesan": "Semoga makin sukses dan sehat terus"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin",
                "sosmed": "@lay.inr_",
                "kesan": "Kakaknya baik dan ramah banget",
                "pesan": "Semoga sehat selalu dan dilancarkan perkuliahannya"# 1
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Abangnya asik, kacamatanya keren",
                "pesan": "Semoga kedepannya sukses terus dan lancar kuliahnya"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "@talljtine_",
                "kesan": "Kakaknya lucu dan ramah",
                "pesan": "Semoga kuliahnya lancar dan sukses terus kak"# 1
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya baik hati dan lucu",
                "pesan": "Semoga sukses selalu dan sehat selalu"# 1
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "Abangnya keren dan asik sekali, idola basket",
                "pesan": "Semoga kuliahnya lancar dan lulus tepat waktu"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "Abangnya seru dan baik banget",
                "pesan": "Sukses terus dan semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakaknya imut dan baik hati",
                "pesan": "Semoga sukses terus dan sehat selalu kak"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semangat terus kuliahnya kak dan semoga selalu dipermudah urusannya"# 1
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1scKhPSfiRM-zzmQjXwGEKCVa72DTLAhC", #kak nayla 
            "https://drive.google.com/uc?export=view&id=1n1cNzI1Q_LnzebtopA_-D8X3heLjg_M7", #kak donna 
            "https://drive.google.com/uc?export=view&id=1FLBfbbihPHnweSKHk4KaUvXcbI1mLuU-", #bang labo 
            "https://drive.google.com/uc?export=view&id=1OQRsJMZ2goVlC2TRR0cEo1eyAlDkfslg", #kak anash
            "https://drive.google.com/uc?export=view&id=1zS8EIAzsrmfyGdfq-CVQpziXRcyepjpF", #kak felisya
            "https://drive.google.com/uc?export=view&id=1Es13dMp8VprKBfpnDbxf3i-ZyfiadEEC", #bang razan 
            "https://drive.google.com/uc?export=view&id=1GxqWnzH09l-V-cpsxqn2OJWT4FkTViXE", #kak sania 
            "https://drive.google.com/uc?export=view&id=1P90qxsk5EBA2ooKlN0EjuUM77Do0zV7d", #kak Allisha
            "https://drive.google.com/uc?export=view&id=1SrxLDJhcCOl8lQ8CVdUoew0MXQcFR8Zf", #kak alya
            "https://drive.google.com/uc?export=view&id=1lFuT9K_shjP2PlG-tCTko-yZgVMRJeu8", #kak bunga
            "https://drive.google.com/uc?export=view&id=1vYLUh6X-vjT6ORXOJsTR5rOoFos0qnNi", #kak difanya
            "https://drive.google.com/uc?export=view&id=1bH0e6cHCK9bb9PrLyivxkpBmtzxsNW96", #kak Nazlah
            "https://drive.google.com/uc?export=view&id=1IjBTIt5gIASyvreWd6k4Q7wULSahjYFD", #kak raihana
            "https://drive.google.com/uc?export=view&id=1TpNl2nO63fJhb5F3jjmouWkwpvx_Ltwf", #bang daffa
            "https://drive.google.com/uc?export=view&id=1pWsVYohPoWDxCLStLZX9StG_4fbtWWNi", #bang edsel
            "https://drive.google.com/uc?export=view&id=12U_o5XVDcWFxl7YvYLuSQyIOWxFLuzFi", #kak lucia
            "https://drive.google.com/uc?export=view&id=19xdCLpEbHi7Eud8962AXB0vyh_kiPfu6", #kak shafa
            "https://drive.google.com/uc?export=view&id=1TRzhkceip55b4Peb8Si1J6HTwKL6gSP4", #kak zannuba

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
                "kesan": "Kak Nayla baik banget, suka ngasi saran dan masukan",
                "pesan": "Sukses selalu dan semoga perkuliahannya dipermudah"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Donna baik, tutor lmd favv",
                "pesan": "Semangat terus ya buat kakaknya dan sehat selalu"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu ",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran ",
                "sosmed": "@noerruuu",
                "kesan": "seru, asik dan menyenangkan",
                "pesan": "Semoga sukses dan semangat selalu bang"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Way Halim ",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "kakak ini lucu dan asik",
                "pesan": "Semoga dipermudah seluruh urusannya"
            },
            {
                "nama": "Felisya Nabila Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal": "Lampung Timur ",
                "alamat": "Kota Baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "Asik banget dan ramah kakaknya",
                "pesan": "Semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "21",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "Abangnya asik dan seru, kameranya keren",
                "pesan": "Semangat kuliahnya bang, semoga koleksi kameranya makin melimpah"# 1
            },
            {
                "nama": "Sania DWi Ayu Lestari",
                "nim": "124450086",
                "umur": "21",
                "asal": "Karawang ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya lucu, suaranya imut",
                "pesan": "Semoga kuliahnya lancar dan sehat selalu kak"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "Asik bangett kakaknya",
                "pesan": "Semoga semangat terus dan sukses terus"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakaknya baik hati dan ramah",
                "pesan": "Semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "kakaknya asik dan positif bawaanya",
                "pesan": "Semoga terus berkembang dan semangat terus"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Alquran",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakaknya ramah dan baik banget",
                "pesan": "Semoga kuliahnya lancar dan selalu diberi keberkahan"# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@nzlhauly_",
                "kesan": "Kakaknya seru dan asik banget",
                "pesan": "Sukses terus buat kakaknya"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Aira Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kakaknya baikkk bangett, diajarin cara ngedesain yang bener gimmana dan ngajarnya juga seru",
                "pesan": "Semangat terus dan semoga kuliahnya lancar"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame ",
                "hobbi": "-",
                "sosmed": "@daffascript",
                "kesan": "Abangnya asik dan seru banget",
                "pesan": "Sehat selalu dan terus berkembang"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "Abangnya ramah dan asik",
                "pesan": "Semoga kuliahnya lancar dan sukses terus"# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Kakanya imut dan lucu banget",
                "pesan":"Semoga sehat selalu dan sukses terus"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis dan menulis",
                "sosmed": "@_shaazzh",
                "kesan": "Kakaknya pendiem tapi seru dan menyenagkan, mentor desain favv",
                "pesan": "Semoga sukses selalu kak"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "Kakaknya baik hati dan ramah",
                "pesan": "Sukses terus buat kakaknya"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan
