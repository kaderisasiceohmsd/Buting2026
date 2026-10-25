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
            "https://drive.google.com/uc?export=view&id=1n4Dr3NwqGSWJ6ePUZs_nx1rqlLiD0MSv",
            "https://drive.google.com/uc?export=view&id=1JGFXuvt-er7Q0GqgXsYn49tfeDmYJD1S",
            "https://drive.google.com/uc?export=view&id=1Q_X8T6Xf12b0tzagpOYr6YV_6ARXhm2H",
            "https://drive.google.com/uc?export=view&id=1BXPM3Ivv3F-J6-NKQ3Tukxjx1DjBYVjV",
            "https://drive.google.com/uc?export=view&id=1hu6rdYSy6W_qvlwaxiadjrGXIAIvlsZ_",
            "https://drive.google.com/uc?export=view&id=14UuJPYZhQ4RSgSU6wdiumJUqkJUiiLcR",
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
                "kesan": "Bang Fajar orangnya sangat humble dan juga baik.",  
                "pesan":"Semoga sukses selalu bang fajar."
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abang nya asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak nya baik banget dan suka deh di ajarin praktikum ads sama ka efi",  
                "pesan":"semangat terus kuliahnya ka efi" # 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "abangnya baik banget",  
                "pesan":"semangat terus kuliahnya abang"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "kakak nya baik banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kaka nya baik dan cantik",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18mLnnbUCg12xnbJWnbmIim86Ml5R2Nm9",
            "https://drive.google.com/uc?export=view&id=1xkljzLzprwqJs2e8OuY-GBfsawk4nH0O",
            "https://drive.google.com/uc?export=view&id=18tEvj4DX_3EN3B-MGoHUpW-qtPOOPGow",
            "https://drive.google.com/uc?export=view&id=1pBXTXSECkyedIT6K617E1C6-mE7uZm9D",
            "https://drive.google.com/uc?export=view&id=1KoBxYHvHpMp22v9DpNYOJtDiLDSoks3v",
            "https://drive.google.com/uc?export=view&id=1QhQ6-giusaF6bFlRgoZ2oXCCG7O-h819",
            "https://drive.google.com/uc?export=view&id=16DgMYKLMqHPp-J4CTtiD-VWv6mTugXn_",
            "https://drive.google.com/uc?export=view&id=1Vs0Zm2DWEoO3qqoSz4Lyd1jRCIMLqDF6",
            "https://drive.google.com/uc?export=view&id=1wzfx9-g65bE_GVEf02HITnWTNkDsokWS",
            "https://drive.google.com/uc?export=view&id=1DjOdoDRL0Jy7247-b9X3DWflrxPImT5W",
            "https://drive.google.com/uc?export=view&id=1z90cxrIxzJZHaqLGwrbMgZ6bjJF35mcJ",
            "https://drive.google.com/uc?export=view&id=1VMBkXPr3Vg_uEoEdLrL-krB84twgd9Bj",
            "https://drive.google.com/uc?export=view&id=1ErpWZ85yidkRFWADsGXkVTlI7pE-19Ek",
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
                "kesan": "Abang nya baik banget, seru di ajarin praktikum sama bang ridho",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini asik banget baik lagi dan cantik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Abang nya asik seru gitu, kerenn",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Abang nya seru banget",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kakak nya cantik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Abang nya baik seru juga",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakak nya asik dan baik banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakak nya asik dan baik banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Abang nya baik dan seru",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak nya baik dan cantik dehh",  
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
                "kesan": "Abang nya seru baik juga ",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak nya baik dan cantik dehh",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakak nya baik deh seruu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ld7xrgbZs_5Z1uflSi6e_uJnlnIizfVh",
            "https://drive.google.com/uc?export=view&id=1a9y5D2yh4K4rvYVqh2IOLexnehoOTjIG",
            "https://drive.google.com/uc?export=view&id=1-Vk6K-pbY7_jh35fuabrnE96KUmZMem7",
            "https://drive.google.com/uc?export=view&id=1BShh3Lrzh0Hho_osI7uDT-7b5vpqtyed",
            "https://drive.google.com/uc?export=view&id=1C5qTEyK8DJHHnVB5S83uGdMo6yI8uPcL",
            "https://drive.google.com/uc?export=view&id=1AIegfS6Ej2VBg3hiAcVVDoaYqnv90osE",
            "https://drive.google.com/uc?export=view&id=1ryEGHgDBUBO5TC8HDYq5rCH3M1ss5mgn",
            "https://drive.google.com/uc?export=view&id=12OX-sdqe6VaYH7nupoSBPYGFXB1iyC5V",
            "https://drive.google.com/uc?export=view&id=1fMmxFd0qDQh4kdQOlJZqlTKqJo75FP92",
            "https://drive.google.com/uc?export=view&id=1WJZ7PPlzxiHT9s9xH0DuwbXwtc6GcaDo",
            "https://drive.google.com/uc?export=view&id=1MFYOLDlr80Ilte4FJvtULigpZz3Nj-Nq",
            "https://drive.google.com/uc?export=view&id=1e5oTheqHTcvq9mtwBLE2JzkTbGisSpOG",
            "https://drive.google.com/uc?export=view&id=1BzU5a3zhv1J7cYGoRr4Bl5qH191R0uiz",
            "https://drive.google.com/uc?export=view&id=1oh8qn8HTouUujIJqo4lSzuMTnsKq3qe-",
            "https://drive.google.com/uc?export=view&id=1jUkdQ3p9WKKzR9A5_sexlldZtZ3aZowd",
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
                "kesan": "Abang nya baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak nya asik dan cantik deh",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Abang nya asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Abang nya random banget deh, tapi seru lucuu",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Abang nya asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal":"Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Abang nya asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
                
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak nya asik dan baik banget ",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kakak ini asik dan baik",  
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
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()
    
elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=123dTATmdwTUSadPFtqPpFKiLBGYL-1jz",
            "https://drive.google.com/uc?export=view&id=1WbtI870GlQaqSG8E-oxiF1WIjGbgqBaN",
            "https://drive.google.com/uc?export=view&id=1QT1AkScevYkdV0ZClUcJix_PH4C30JZe",
            "https://drive.google.com/uc?export=view&id=15MwxDa0vG8hmUTyKJyOgG9uRPcHtWMT4",
            "https://drive.google.com/uc?export=view&id=1IvsuwH5JPny4co3vy9fCjCpAmqyIcmtp",
            "https://drive.google.com/uc?export=view&id=1C1_qzyTvbgFLxIgUKfN3A84qsjZ9JmrR",
            "https://drive.google.com/uc?export=view&id=1U9J-Ye0aOZO_SGOsLleamKnZkqZECd1b",
            "https://drive.google.com/uc?export=view&id=1P7kOf-Ye6enFcO-2EoRjvS5G6y6Y_YLb",
            "https://drive.google.com/uc?export=view&id=1xEwf_lZGOSlQ_UjENfyVEJ18hH2X85lb",
            "https://drive.google.com/uc?export=view&id=19XEAP-6N2Tt8zNprgBXFhEJA_11e9JKR",
            "https://drive.google.com/uc?export=view&id=1jO2MBglLIT-GqFCfyfk6NoTWABYJ8NhT",
            "https://drive.google.com/uc?export=view&id=1hw2cLrzq9Uq3JQ6imEx_4iDlMYcR0OD3",
            "https://drive.google.com/uc?export=view&id=1YgXLT1bKMAJilOF6TDMCEOrgxoU9E1CA",
            "https://drive.google.com/uc?export=view&id=1l7-DI_Df6xbSOJJhdh2Rzp43JOCMnzgn",
            "https://drive.google.com/uc?export=view&id=1d0h1kJ-wd_5XI9sMeUWjHuMxftRTJ3Iy",
            "https://drive.google.com/uc?export=view&id=1ccGPVB1zKuK9PMz8mqtsLQfs1Um3kYwU",
            
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
                "kesan": "Kaka terhumble dan friendly, sangat hangat rasa",  
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
                "asal":"Medan",
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
                "alamat": "Korpri raya",
                "hobbi": "Isengin harvin di kelas",
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
                "sosmed": "@christian8872",
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
                "kesan": "Kakak nya cantik, terus soft spoken",  
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
                "alamat": "Airan",
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
                "kesan": "Abangnya asik dan seruu",  
                "pesan":"Sukses terus abanggg, semoga semester ini lancar yaa"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Kakak ini baik dan asikkk",  
                "pesan":"semangat terus kuliahnya kak rafa sabinaaaaa!!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
    
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls =[
            "https://drive.google.com/uc?export=view&id=1YBYf7bAz47Ynn9RRmMIB_rGLRjuoCjtv",
            "https://drive.google.com/uc?export=view&id=1CHaEGGZOt1klaGqfav7WAtOAMR43o1Kq",
            "https://drive.google.com/uc?export=view&id=1iyce4R69Tdzp_sVyAYH7BnNfCXkRTk5g",
            "https://drive.google.com/uc?export=view&id=1iE348pBH97woz5Gu0f2ar8Dn1ZZ4C55z",
            "https://drive.google.com/uc?export=view&id=1-4gERWLvMJec9VOL7tIlOLQc3JVlhh1X",
            "https://drive.google.com/uc?export=view&id=1bnHkwaq1i9vwcSFkeIJPbvE8P3lz2bMO",
            "https://drive.google.com/uc?export=view&id=1QwVXBL5jhBUrePmOZOvUYVkPPcPILfKX",
            "https://drive.google.com/uc?export=view&id=1K6aOm45KXJoh52jalnEEUZcdQArWtIM0",
            "https://drive.google.com/uc?export=view&id=13g7AK1wEFcvsAvVjrOeKnNdMwINrHUMP",
            "https://drive.google.com/uc?export=view&id=1pwiCeRfFbx--Q0SBJBQ64s6k_w6N16E4",
            "https://drive.google.com/uc?export=view&id=16fqLHRc2RzrP_appDgXbeqgvk3SypGBR",
            "https://drive.google.com/uc?export=view&id=1Dmkm_AFdHqAYLsnkwaUqWOYmVr8QWE6t",
            "https://drive.google.com/uc?export=view&id=1HlFbX3fhfMqImOLYwwt8afT_0cUV2LVt",
            "https://drive.google.com/uc?export=view&id=1OjgI1scB9A_Qwepfi2m2mlGkgZsUFUmY",
            "https://drive.google.com/uc?export=view&id=1xE_XLWO6RcfUHQkkv_MbRhLBHA8rfXzf",
            "https://drive.google.com/uc?export=view&id=1fQjNmRaiXcnxX0pqm5pOkmufC2hoxm3g",
            "https://drive.google.com/uc?export=view&id=1FaPEKpJPo5YjkpLik-t2YN1hfOvIt9kv",
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
                "kesan": "Kak arienta ternyata baikkk, walaupun awalnya keliatan serem.",  
                "pesan":"Semangat terus ya kak, lancar terus kuliahnya."#1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany baikkk, walaupun keliatan judes",  
                "pesan":"Semangat terus ya kak, lancar terus kuliahnya."# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan":"Bang nobel itu orang nya tegas, tapi asik juga ternyata.",  
                "pesan":"Semangat terus ya bang, lancar terus kuliahnya"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi orang nya semangat banget apalagi kalo damaskusan",  
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
                "pesan":"Semangat terus yaa bang ayake, lancar terus kuliahnya"# 1
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
                "pesan":"Semangat terus yaa bang caesar, lancar terus kuliahnya"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kaka euodia itu asikkk dan baik juga, tapi keliatan galak pas kader (jujur)",  
                "pesan":"Semangat ya kak, lancar terusss kuliahnya"# 1
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
                "pesan":"Semangat terus yaa bang haikal, lancar terus kuliahnya"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kakanya sangat ramah, baik, dan humble",  
                "pesan":"Semangat terus kaka kuliahnya"# 1
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
                "kesan": "Abang nya baik",  
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
                "pesan":"Semangat terus ya kak, lancar terus kuliahnya"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "kakanya baik dan asik ",  
                "pesan":"semoga semester ini dilancarinn segala urusannya ya ka"# 1
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
                "pesan":"Semangat terus abangg kuliahnya"
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
                "kesan": "Kakak nya baik dan lucu",  
                "pesan":"lancar lancar terus ya ka kuliahnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
    
elif menu == "Senator":
    def Senator():
        gambar_urls=[
            "https://drive.google.com/uc?export=view&id=1Cq45uDHWZciIeABqxL-1pmS_bv9arjJ-",
            "https://drive.google.com/uc?export=view&id=1859EndI2YcbLmtOTT2z5G_cago7yzrj6",
            "https://drive.google.com/uc?export=view&id=1E4nkElJXSIc6KH9P3PemBMT4Vn-Rav8T",
            "https://drive.google.com/uc?export=view&id=1DKX_F1yULYgBHo3xR87SklYhXib1xrkS",
            "https://drive.google.com/uc?export=view&id=1l18OxdebiZmT1B8qIoKvqtxfZnjRYgYf",
            "https://drive.google.com/uc?export=view&id=1J-_8An3MdF2xfZxqv-H-kbi8D28m0XNx",
            "https://drive.google.com/uc?export=view&id=1r9jnl7KbeK_i__FY1WdKVr8VxlyqWZb7",
            "https://drive.google.com/uc?export=view&id=11G8ycJgWHOZ8YANDAg6U4CBCxreqrbYd",
            "https://drive.google.com/uc?export=view&id=18OyRCSyYxiut1V5LIm4fZZPU_BAP_DIq",
            "https://drive.google.com/uc?export=view&id=1PCfjTeMJUknstJLPb8jcpBQ_OxS7Kww_",
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
                "kesan": "Kaka nya baik banget cantik lagi",
                "pesan": "Makasih kak udah menjelaskan tentang kesenatoran, semangat terus kuliah nya!!."# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "bang helmy itu seru banget orang nya random banget ",
                "pesan": "semangat bang buat kuliahnya"# 1
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Nemenin Wielman MC",
                "sosmed": "@barus.fernando",
                "kesan":"Abangnya keliatan pendiem",
                "pesan": "Semangat buat kuliah nya bang"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru ",
                "hobbi": "Baca",
                "sosmed": "@sciia__",
                "kesan": "kaa suci anaknya asik banget walaupun awal liat keliatan kek jutek gitu tapi aslinya bak dehh",
                "pesan": "Semangat terus menjalani kuliahnya kak"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "jadi MC",
                "sosmed": "@wielhawn",
                "kesan": "Abangnya keliatan kalem",
                "pesan": "Semangat buat kuliahnya bang"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "main hp",
                "sosmed": "@lia.h_264",
                "kesan": "Kaka nya baik banget dan ramah",
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
                "kesan": "Ka aqila cantik banget gayanya juga keren",
                "pesan": "Semangat ka kuliahnya dan jadi mentor bayes"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "jadi sekjen",
                "sosmed": "@hazelhandhaka",
                "kesan": "Awal kali ngeliat bang hazel itu keliatan galak gitu tapi aslinya baik",
                "pesan": "Semangat bang kuliahnya"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                 "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya cantik dan baik ramah",
                "pesan": "Semangat jalanin semester 7 nya ka"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani ",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang ",
                "alamat": "Jl. Lapas",
                "hobbi": "nonton film,musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "kakanya baik banget terus humble juga",
                "pesan": "semangat menjalani semester 5 nya ka"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
    
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1i3Y5eKPPxWh4hX1uhTt7xhbu20loRlbD",
            "https://drive.google.com/uc?export=view&id=1daRqZPErCxrGS-WXJ7Yyo6rcljwVNXai",
            "https://drive.google.com/uc?export=view&id=1qRp_gM2e46j1M0_blF8_1rpjOjnwsBvF",
            "https://drive.google.com/uc?export=view&id=1nqS9YGZb1aMhJCBMz5E-vUj78D8f54DS",
            "https://drive.google.com/uc?export=view&id=1fn-L6Sp-VFrXKhyIGI6i1uaGi4flklwh",
            "https://drive.google.com/uc?export=view&id=1lf7arxqJhyk33GfB4_XnenI-_TMrSrVt",
            "https://drive.google.com/uc?export=view&id=1aTEq7L8HoXjWWSy0fbqE8oIYNC7JIXle",
            "https://drive.google.com/uc?export=view&id=1Q1OKwcL3lcvUaXcVxSOdrc37-_OZnClm",
            "https://drive.google.com/uc?export=view&id=1WsqRF4LSPWBEee1_riZsN1c_jgc3jpEY",
            "https://drive.google.com/uc?export=view&id=1gs4iB0OyoyzRpIbt1m9birvsZa1ElPI3",
            "https://drive.google.com/uc?export=view&id=13zJDbAq1Oprfj6MUX6Nzi0L-XK0FginG",
            "https://drive.google.com/uc?export=view&id=1FcqLYMsFc4AhecwFfAI-MsDbnl2l6GZj",
            "https://drive.google.com/uc?export=view&id=1WZwuL5pPqWZJiHlDwV5E9icxxpCchmzm",
            "https://drive.google.com/uc?export=view&id=16DJYVChQxLokLPKlLNGVCbL_e7ivZFHc",
            "https://drive.google.com/uc?export=view&id=1SwRdlMeoiWjdyZ8MKOsCZEh8xjxku9Iv",
            "https://drive.google.com/uc?export=view&id=1JqkLE966QH9kqMIrjxthhHZPxrMbBguJ",
            "https://drive.google.com/uc?export=view&id=1Vugp2NKDMbi2btmDIKCBcGq3_zT69YiS",
            "https://drive.google.com/uc?export=view&id=1pD_W1BDvhZeC_WC0H4PQLlzAAHuc7sGO",
            "https://drive.google.com/uc?export=view&id=1VukXjRDIgRBhhubpuW5XuSllwzBoh1QV",
            "https://drive.google.com/uc?export=view&id=1RZzXNXGg0BV52R4WhlAU5STUHNDVWJKG",
            "https://drive.google.com/uc?export=view&id=1ftXl7Xp4J0r3uZgC4e3WSpeJJiFtcbBa",
            "https://drive.google.com/uc?export=view&id=1n4tR6dE474CoDRQrXbbBPuS-zuyczttW",

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
                "kesan": "awal kali liat ka arini itu keliatan nya jutek gitu, tapi ternyata orang nya baik dan asik ",
                "pesan": "Semangat kuliahnya ka, semoga lancar TA nya "# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakak nya cantik banget, senyum nya manis",
                "pesan": "semangat terus kuliahnya kakkk"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "bang adit orangnya seru bangettt tapi klk udah serius seram laa",
                "pesan": "Semangat terus menjalani kuliahnya bangg"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Sesuai panggilan nya kaka cantik, orang nya juga cantik kaliii",
                "pesan": "semangat kaka cantik menjalani kuliah nya!!!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                 "nim": "123450052",
                "umur": "-",
                "asal": "Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "tari_",
                "kesan": "kaka tari cantik bangett apalagi klk lagi senyum manis dehh, terus juga baik banget sangat ramahhh",
                "pesan": "semangat terus ka menjalani semester 7 nyaa"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "ka selma itu orangnya baik banget soft spoken juga dan pastinya orangnya cantikk",
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
                "kesan": "kaka ashila itu baik banget terus juga lucuu",
                "pesan": "Semangat kuliahnya ya kak, hati-hati selalu klk balik ke natar malam-malam hehe"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Abang duta keren bangett terlihat cool",
                "pesan": "semangat terus kuliahnya bang duta"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Awalnya ngeliat bang vian itu serem kek galak gitu tapi ternyata Bang vian itu anaknya random banget, ada aja yang bikin ketawa klk ngobrol sama bang vian",
                "pesan": "Semangat ya bang kuliahnya, bahagia selalu"# 1
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Ngeliat bang yazid jadi korlap itu awalnya ga cocok soalnya mukanya keliatan lucu tapi lama-lama kok jadi ngeri hehe, tapi bang yazid baikkk banget kokk asik juga",
                "pesan": "Semangat menjalani semester 5 nya bang, dan mangat juga jadi korlapnya"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah ",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "ga balesin chat",
                "sosmed": "@jaldii._",
                "kesan": "Awal ngeliat bang jaldi jadi MC PPLK keren banget, terus bang jaldi juga asik banget",
                "pesan": "Lanjutkan bakat mu jadi MC bangg"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kak kia itu keliatan kalem banget terus soft spoken juga",
                "pesan": "Semangat terus kak kuliahnya!!"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Awalnya ngeliat kaka nya itu kayak jutek gitu tapi kaka nya baik dan ramah juga kok ternyata",
                "pesan": "semangat ka menjalani semester 7 nya"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                 "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang ahmad keren banget",
                "pesan": "semangat terus ngerjain tugas-tugas semester 7 nya bang"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Ka indah orang nya asik banget pertama ketemu itu pas sosialisasi magenta",
                "pesan": "Semangat ka jadi medis nyaa"# 1
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung ",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "abang nya awal ketemu asik gitu tapi klk lagi serius keliatan serem",
                "pesan": "Semangat bang jalanin semester 5 nya"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus ",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Bang bimo keliatan keren",
                "pesan": "Semangat terus bang dan bahagia selalu"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "21",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "kakanya cantik dan baik banget",
                "pesan": "Semangat terus kak!!"# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "21",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "suka nyari duit",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kaka nya baik dan ramah banget",
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "ka riska itu humble banget dan perhatian banget sayang banyak banyak sama ka riska",
                "pesan": "Makasih kak udah jadi mentor Tensor yang perhatian dan pengertian, seneng banget Tensor bisa dapet mentor nya ka riska. "
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Abang nya asik banget seru deh ngobrol sama abang nya",
                "pesan": "Semangat bang jadi panit acaranya"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "kaka nya cantik dan baik sekali",
                "pesan": "Semangat ka kuliahnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sgb1h4A343kxAvfYxhWMgqxqCbO_TWxG",
            "https://drive.google.com/uc?export=view&id=1DSS6ND36BaFGPp5iDvqE_KQDkvDtS6p3",
            "https://drive.google.com/uc?export=view&id=1JyWqMx5rpUyEpcf3hVtXFqcJyriHlCGP",
            "https://drive.google.com/uc?export=view&id=18Mi09Jr1XdluV-AY2k_OdTHXfYz-vzkK",
            "https://drive.google.com/uc?export=view&id=12bQxOWKq0WP3CtxVd59W0dR26fufTvjA",
            "https://drive.google.com/uc?export=view&id=12iTn0uYp1UsQojlyi9k35SivOcgbl7C0",
            "https://drive.google.com/uc?export=view&id=1-HvjFM1BSWYccLSmGGGMdHNN5fDhr5ge",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#yulia
            "https://drive.google.com/uc?export=view&id=1yCKIoZN_kOSZItnWW9i4GkG7b3ai7jWK",
            "https://drive.google.com/uc?export=view&id=1tgYJdcEkkXPhU_e4eHy5FHqKZO-5i6Dm",
            "https://drive.google.com/uc?export=view&id=17E3gS_-gMcSI4ZrflvH-t6_AAIgVtmEq",
            "https://drive.google.com/uc?export=view&id=1xtx9fjMfd6oimFDh9yfAB3v4zV35ZGnI",
            "https://drive.google.com/uc?export=view&id=11lN8_atneklVDrd_KzUkvUhbgjIwaxdW",
            "https://drive.google.com/uc?export=view&id=1jTFcn7Rhyes6E0lIEOTvyFzXUXI3RqTw",
            "https://drive.google.com/uc?export=view&id=14BvEqCgLzk_5QBJVltUe8q4sqV_urSXp",
            "https://drive.google.com/uc?export=view&id=1LhQ3l4AXPCkcAAbN8PZN5hSb_Ig09T-v",
            "https://drive.google.com/uc?export=view&id=1dCjdUUm3TZzTxraH39Wrj1EjMQeH5BxO",
            "https://drive.google.com/uc?export=view&id=1XPVXGN7kxLqK3vOtuEOJWCYIkOgLZ_HB",
            "https://drive.google.com/uc?export=view&id=1mQLwt02ZkViryOyM9CpKWk3-jUzcGZ7v",
            "https://drive.google.com/uc?export=view&id=1AOVKUTUxbSXQvlXfoirXLvmmj6zP9yE4",
            "https://drive.google.com/uc?export=view&id=1SPZ2JCYXThqndAQnYD1LAdJJwq--Z2-Q",
            "https://drive.google.com/uc?export=view&id=15MOCXRdwxSt3Yt4E1zaWeLliBFv0YFYW",

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
                "kesan": "abangnya keliatan serius banget",
                "pesan": "Semangat terus kuliahnya bang, sehat sehat ya bang"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Nonton film",
                "sosmed": "@tvnty_",
                "kesan": "ka tanty orang nya ceria dan ramah banget",
                "pesan": "mangat terus ka kuliahnya"# 1
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Awal kenal sama bang fadil karena jadi kasuh TPB 37, orang nya baik dan ramah banget dan menginspirasi, banyak dapet tips-tips ngejalanin masa TPB saat itu.",
                "pesan": "semoga almarhum bang fadil husnul khatimah, dan amal ibadahnya dapat diterima disisi Allah Swt. Semoga ilmu-ilmu yang diberikan bang fadil selama hidup dapat menjadi amal jariyah, Aaminnn"# 1
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis ",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "Abangnya seru dan asik banget",
                "pesan": "Tetap semangat ya bang kuliahnya."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12",
                "asal": "Bali",
                "alamat": "nusa peninda",
                "hobbi": "menghayal",
                "sosmed": "@violaadrtr_",
                "kesan": "kaka nya cantik dan baik banget",
                "pesan": "Semangat ya ka ngejalanin semester 5 nya"# 1
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "kaka nya cantik dan baik banget",
                "pesan": "Semangat ka kuliahnya, sehat selalu"# 1
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "1244500078",
                "umur": "19",
                "asal": "kepulauan riau",
                "alamat": "teluk betung",
                "hobbi": "nonton khw",
                "sosmed": "@vunnycaa",
                "kesan": "kaka nya baik dan keliatan kalem gitu",
                "pesan": "semoga lancar-lancar selalu ya ka kuliahnya"# 1
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "kakanya cantik deh",
                "pesan": "Semangat ka kuliahnya"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                 "nim": "123450119",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@keyashafi_",
                "kesan": "kakanya cantik dan lucu",
                "pesan": "semangat ka ngejalanin semester 7 nya."# 1
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara ",
                "alamat": "Pemda",
                "hobbi": "Sibuk",
                "sosmed": "@_els.a",
                "kesan": "Kak elsa baik dan asik banget orang nya",
                "pesan": "sehat sehat selalu ka"# 1
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "airan",
                "hobbi": "mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "kaka nya baik dan asik",
                "pesan": "Semangat ka ngejalanin semester 5 nya"# 1
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "kakaknya baik dan ramah",
                "pesan": "sehat-sehat selalu ka"# 1
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "kalianda",
                "alamat": "kota baru",
                "hobbi": "main game, tidur",
                "sosmed": "@aluccy_",
                "kesan": "abangnya keren dan baik banget",
                "pesan": "Semangat bang kuliahnya"# 1
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal":"Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "kaka nya lucu dan cantik banget baik lagi ",
                "pesan": "Semangat terus ya ka jalanin kuliahnya, sehat sehat selalu ka."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                 "umur": "21",
                "asal":"Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abang nya baik dan ramah banget",
                "pesan": "sehat-sehat selalu bang dan semangat menjalani semester 7 nya"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel ",
                "sosmed": "@faizaanjanii",
                "kesan": "Ka faiza baik banget dan ramah banget juga pertama kali tau ka faiza karena jadi asprak dan astut nya RA",
                "pesan": "Semangat terus ka kuliahnya."
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Rajabasa Raya",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "abang nya baik dan ramah banget",
                "pesan": "Semangat terus bang kuliahnya"
            },
{
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur ",
                "hobbi": "3N ( Ngoding , Ngegame, Nyibukin Diri)",
                "sosmed": "@apiszzaja",
                "kesan": "abang nya seru dan asik banget lucu deh",
                "pesan": "Semangat bang kuliahnya"# 1
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Campang Raya, Sukabumi",
                "hobbi": "Gym, membaca, dan bermain",
                "sosmed": "@kelelep_comberan",
                "kesan": "abang nya keren dan ramah banget ",
                "pesan": "Semangat ya bang kuliahnya"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                 "umur": "19",
                "asal":"Sumatera Selatan ",
                "alamat": "Sukarame ",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "ka melva keliatan jutek gitu tapi aslinya ngga kok ka melva baik dan ramah banget",
                "pesan": "Semangat ka menjalani semester 5 nya"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syafiqui",
                "kesan": "abang nya sabar banget jadi astut metnum nya RA",
                "pesan": "Semangat ya bang tutor in RA"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal":"Kotabumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "bang henry ramah dan baik  ",
                "pesan": "Semangat ya bang kuliahnya."
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1D4xFswDIeKb9sFK1_ztlGQKySveUVzAM",
            "https://drive.google.com/uc?export=view&id=1Q1CEhphtmBvsiPeKDhPD3Pfv1ynUzTrK",
            "https://drive.google.com/uc?export=view&id=1POc6IKUj8esRLfwL-NQ86f5nJECk8a-b",
            "https://drive.google.com/uc?export=view&id=1Vsn3FIX-cZ-ki3qP8VoERU0H1Vt0uhc4",
            "https://drive.google.com/uc?export=view&id=1sX6Fci1T4jAqO5UuZntbSyeDxwRcvEZo",
            "https://drive.google.com/uc?export=view&id=1lJIENtP_favNfF_kVu83GfqgH-6JJ1Rf",
            "https://drive.google.com/uc?export=view&id=1At1UruEy7BDbw7i3v-r82Nfbec7aNtjD",
            "https://drive.google.com/uc?export=view&id=1VsE0wbjbTo83po6R0w8bXlQRWgG73p_a",
            "https://drive.google.com/uc?export=view&id=1WTl99bBT6Ud1x7V0rK9QDEZoTQDz18a7",
            "https://drive.google.com/uc?export=view&id=1OR0xqhVW639jPTYU8PSJyDSexZmO__52",
            "https://drive.google.com/uc?export=view&id=1CnQ-O22City75NK92dWjrHukW6JyvXyt",
            "https://drive.google.com/uc?export=view&id=1hMjeWKJiz5XmoL3gHo_AoEGtwcRNcv_j",


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
                "kesan": "Abang nya baik dan ramah banget",
                "pesan": "Semangat ya bang TA nya semoga lancar"# 1
            },
            {
                "nama": "hanifah inaya sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "kaka nya cantik dan baik banget",
                "pesan": "Semangat ka TA nya semoga lancar"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kaka nya baik dan ramah banget",
                "pesan": "Semangat ya ka kuliahnya"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "abang nya baik dan ramah",
                "pesan": "Semangat bang kuliahnya"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin",
                "sosmed": "@lay.inr_",
                "kesan": "kaka nya baik dan lucu",
                "pesan": "Semangat ka menjalani kuliahnya"# 1
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "abangnya baik dan ramah ",
                "pesan": "Semangat bang kuliahnya"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "talljtine_",
                "kesan": "kaka nya baik dan ramah",
                "pesan": "Semangat terus kuliahnya ka"# 1
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "kaka nya cantik dan baik banget",
                "pesan": "Semangat ya ka kuliahnya lancar-lancar selalu ka"# 1
            },
            {
                "nama": "Abdilah Fikri Alpome",
                 "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "Abang nya asik banget ",
                "pesan": "Semangat ya bang TA nya semoga lancar-lancar selalu"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "abang nya baik dan ramahnya",
                "pesan": "Sehat sehat selalu bang"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "kakanya cantik dan baik banget",
                "pesan": "Semangat kuliahnya ya ka"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "kakanya cantik dan baik",
                "pesan": "Semangat kuliahnya ka"# 1
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-k2kN7iiFfvYJvlLNb_ZpHZ6Psyn__Ab",
            "https://drive.google.com/uc?export=view&id=1HC1uj4eBjOzXY30gF4vZj24BY5qsFlfl",
            "https://drive.google.com/uc?export=view&id=130ML9ez5rf_g2cXfzmnrakqxuJYD85-7",
            "https://drive.google.com/uc?export=view&id=1vEFyp3QZwKMmWyYeqq72u6tcQW_fVr5A",
            "https://drive.google.com/uc?export=view&id=1oBPEOL_lIgcc3MetAx6FC-c3PTcVhA6G",
            "https://drive.google.com/uc?export=view&id=1EjnC4HUrPRf-3_pAc5qWolsplnSYVYrr",
            "https://drive.google.com/uc?export=view&id=1IZsO1rcxUPPvbSphYnBs6C5D3r-PE_at",
            "https://drive.google.com/uc?export=view&id=1vAAi85tFGWocJy6Smz1s03EKkWxEmNgS",
            "https://drive.google.com/uc?export=view&id=1GCUdP5y2tKIcU6zXEssQGeF0CjwFXb_n",
            "https://drive.google.com/uc?export=view&id=1cWKWMJsBZCMZxiXLhp6vfvUpQysqWfA-",
            "https://drive.google.com/uc?export=view&id=1aYhU-XrHgmHM5dCCRq9abYHRYvR8SHa7",
            "https://drive.google.com/uc?export=view&id=1hkuFq7pAmmif28C10ZbQQ3FxbNh9Vy_X",
            "https://drive.google.com/uc?export=view&id=1GDu2GlVMcv2jqfw-Z28OEjnon6yIbYxK",
            "https://drive.google.com/uc?export=view&id=1eTfWqwBvoSzHy26nHckLsVtrTXB0xhUC",
            "https://drive.google.com/uc?export=view&id=1p2MFKIIF37ra4i241LK8xC9c6o-DC6do",
            "https://drive.google.com/uc?export=view&id=1HYyCTf8Ihz--swhpV-d_QP2gE6YBF67V",
            "https://drive.google.com/uc?export=view&id=1u8DdMHvAt_W0zp1htf1l-7yuESZ4YQQj", 
            "https://drive.google.com/uc?export=view&id=1iaFBO046xOlrQCAP1m7Jiqs2-4eCu59O",
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
                "kesan": "kaka nya baik dan seru dehh",
                "pesan": "Semangat ya ka kuliahnya."# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "kaka nya baik dan ramah banget",
                "pesan": "Sehat-sehat selalu ya kak"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu ",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran ",
                "sosmed": "@noerruuu",
                "kesan": "Abang nya baik dan ramah",
                "pesan": "Semangat menjalani TA nya bang"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Way Halim ",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "kakanya cantik dan lucu deh",
                "pesan": "Semangat ka menjalani semester 5 nya "
            },
            {
                "nama": "Felisya Nabila Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal": "Lampung Timur ",
                "alamat": "Kota Baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "kakanya cantik dan lucu dehh",
                "pesan": "Semangat buat kuliahnya ka "# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "21",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "Abangnya asik banget lucu",
                "pesan": "Semangat bang kuliahnya"# 1
            },
            {
                "nama": "Sania DWi Ayu Lestari",
                "nim": "124450086",
                "umur": "21",
                "asal": "Karawang ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "Kaka nya cantik dan baik banget",
                "pesan": "Sehat-sehat selalu ka"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "kakanya baik dan cantik",
                "pesan": "Semoga lancar-lancar selalu ya ka kuliahnya"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                 "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "ka alya cantik dan baik banget",
                "pesan": "Semangat terus ka"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "kak bunga ramah dan baik banget seru lagi",
                "pesan": "Semangat ya ka bunga kuliahnya"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Alquran",
                "sosmed": "@difanyhsa_",
                "kesan": "kakanya baik dan ramah",
                "pesan": "Semangat ya ka kuliahnya"# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@nzlhauly_",
                "kesan": "kakanya cantik dan baik banget",
                "pesan": "Semangat terus ka kuliahnya"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Aira Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "kakanya cantik dan baik banget",
                "pesan": "Semangat terus kaka kuliahnya"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame ",
                "hobbi": "-",
                "sosmed": "@daffascript",
                "kesan": "Bang dafa seru dan ramah banget",
                "pesan":"Semangat bang kuliahnya"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "abang nya baik dan asik",
                "pesan": "Semangat ya bang kuliahnya"# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Ka lucia cantik banget dan ramah banget juga",
                "pesan": "Semangat ya ka kuliahnya"
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
                "pesan": "Semangat ya ka shafa kuliahnya"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "kakanya ramahh dan baikk",
                "pesan": "sehat-sehat selalu ya ka semangat menjalani kuliahnya."
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
