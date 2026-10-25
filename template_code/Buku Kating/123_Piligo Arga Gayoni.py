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
            "https://drive.google.com/uc?export=view&id=1SRiCdfXwUoJzCrsldYcO1QJjnmHPYlXQ",
            "https://drive.google.com/uc?export=view&id=13jrcV2VxF6zWwlJSGJImRwQPe-z4ic6r",
            "https://drive.google.com/uc?export=view&id=1Jscj0-7kkTq2-MUf4O_snVTThbjYXdY7",
            "https://drive.google.com/uc?export=view&id=1vTZxoCos2uGY4B3QGi88sUdJCO7bFUvQ",
            "https://drive.google.com/uc?export=view&id=1kyBWYXpT6GzanZh1siuiKw6G2t4p4eba",
            "https://drive.google.com/uc?export=view&id=1FiVB3HrrK4NjV_gGogLYU6YZtkOV0Dtq",
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
                "kesan": "Bang Fajar orangnya kelihatan asik banget sih, soalnya hobinya push immo, beliau juga orang yang bertanggung jawab.",
                "pesan":"Semoga bang fajar cepat di wisuda dan sehat selalu"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Lucu banget abangnya, sifatnya itu yang suka bercanda gampang bikin suasana cair",
                "pesan":"Semangat terus ya bang aqil"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini soft spoken banget, nada suaranya enak didengar",
                "pesan":"Semangat terus kakak, semoga cepat diwisudaa"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois ini bagi saya orangnya pendiem, tapi selalu berkomitmen",
                "pesan":"Sehat terus ya banggg"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Orangnya lucu dan imut, suka bercanda",
                "pesan":"Jangan menyerah dan terus semangat ya kakkk"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakaknya baik dan enak diajak kalau ngobrol",
                "pesan":"jaga terus kesehatannya ya kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ebe1fVSVNTresFzcKDcfaJkUlB5m5Tga",
            "https://drive.google.com/uc?export=view&id=1bJC22-jrAp-A8NvjNxkQVM22QIcqMjEp",
            "https://drive.google.com/uc?export=view&id=1B9ciiPsIsSdiSxDDuYbPnXFIOuqKbBAJ",
            "https://drive.google.com/uc?export=view&id=1sNt_Uqaj80_jVSQrPIrbuH29Dqd4N-iK",
            "https://drive.google.com/uc?export=view&id=1n3GOhJK3mneaSJ2depgdT1vOGO_AnC26",
            "https://drive.google.com/uc?export=view&id=1zxBiNESHIr-JqH-yR_VwRtgjPEK12FwZ",
            "https://drive.google.com/uc?export=view&id=1kVupPbZ32unNHxpSgUQCKE5vtNKvK_7k",
            "https://drive.google.com/uc?export=view&id=1_T5ylXTa_L7vCYiUaKg5LJj9FI0fqqBR",
            "https://drive.google.com/uc?export=view&id=1yO909EJCcsnf_zUSzWjXcGy5xpFMEicM",
            "https://drive.google.com/uc?export=view&id=1_npit5aelARaYIpUbQxvU0Bzg9r-ko-c",
            "https://drive.google.com/uc?export=view&id=1G66mKSL-qHFg7Mx8HmTH4nvg18veNPmW",
            "https://drive.google.com/uc?export=view&id=1EM5KEmYYKjtOTUb3b5voAYU-AxcYZj0W",
            "https://drive.google.com/uc?export=view&id=1wYxhCeZadt9UcyfOYCzQFC1GLKoWgucY",
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
                "kesan": "Bang ridho berwibawa banget, auranya kuat banget.",
                "pesan":"Semangat terus ya bang, semoga juga bisa cepat diwisuda"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini lucu banget orangnya, suka bercanda, tapi bisa juga serius",
                "pesan":"Semangat kuliahnya ya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Abang ini seru orangnya, suka ngobrol dan pintarr",
                "pesan":"Jaga selalu kesehatannya ya bangg"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Pertama kali saya melihat abang ini pas pplkk, dan kesannya si abangnya ini pendiam",
                "pesan":"Kejar terus mimpinya bang, jangan kasih kendor"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Mukanya itu terlihat serius banget, tapi aslinya asik dan bisa diajak bercanda",
                "pesan":"Jangan sampai semangatnya turun ya kakk"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bagi saya abang ini keren aja gitu",
                "pesan":"Semoga selalu diberi kesehatan ya bang"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakaknya itu bagi saya tipikal orang ya bisa ngelucu dan serius disaat bersamaan",
                "pesan":"Semoga mimpi kakak bisa tercapai ya"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Lucu kakaknya, kelihatannya juga suka ngobrol",
                "pesan":"Semangat terus kak!"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Abang ini orangnya pintar dan jago berbicara",
                "pesan":"Sehat terus ya bangg"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak monica ini lucu dan suka senyum",
                "pesan":"Jangan kendor ya kak semangatnyaa"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Lucu banget  abang ini, suka ketawa dan ngejokes",
                "pesan":"Semangat mengejar mimpinya bangg"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Awal pas ketemu kakak ini saya merasa kakak ini galak banget, ternyata malah sebaliknya",
                "pesan":"semoga cepat wisuda dan dapat pekerjaan yang terbaik ya kakk"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "kakak ini aktif banget, suka ngobrol dan ketawa",
                "pesan":"semangat terus ya kak kuliahnyaa"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1utYP0n5FN6rTA_vxNyjAoBQQP2z_jvlH",
            "https://drive.google.com/uc?export=view&id=1qpiKnz0FQ-9BKXlPEKxqjvma6YuhIou_",
            "https://drive.google.com/uc?export=view&id=1RdwFELGZZVMMEYhzvvrL7g4m9DTD25Rk",
            "https://drive.google.com/uc?export=view&id=1kFCo_eo4BkoHD45hgv7ZLndC5wCugG9y",
            "https://drive.google.com/uc?export=view&id=1lta38E7ynCLizjqL-0IGzhpnXvcykZiR",
            "https://drive.google.com/uc?export=view&id=1znHuKNPq4RCS3lLP_jx9_3ZQt51UbQXW",
            "https://drive.google.com/uc?export=view&id=1N3Fitv6zT00NblYXCBRODUEQp7c90eWD",
            "https://drive.google.com/uc?export=view&id=1b-LnDZJOA7ASDsnYv_Pjp-eyU77xbyRj",
            "https://drive.google.com/uc?export=view&id=1h-3tyjWjQJr9esVsl7xzPHIJcA-E6WRB",
            "https://drive.google.com/uc?export=view&id=1oFfbghS29Z3oBT8c9oBRlf2q0p2u99Y1",
            "https://drive.google.com/uc?export=view&id=1YSaVrzYrI_VXZtVncTVJjSN8RGwJGXWa",
            "https://drive.google.com/uc?export=view&id=1jm-YNR0LSwJdj4FftQocVrXkPggjRB-L",
            "https://drive.google.com/uc?export=view&id=1hlm_XS6VKWbgq0JweOojfXQpSO_V9VL4",#indah
            "https://drive.google.com/uc?export=view&id=1qfftq9-XulUD6AXGPGOemSVlMSqTSWNg",
            "https://drive.google.com/uc?export=view&id=1dLeHorV5wdha37V7WwBwgLa2AOloF-yX",

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
                "kesan": "abangnya keren sih dan terlihat cocok banget untuk departemen ini",
                "pesan":"semangat terus ya bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "kakak ini lucu dan suka ketawa untuk bikin cair suasana",
                "pesan":"semangat dan sehat terus ya kakakk"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "kalau dari sudut pandangku itu abangnya bukan tipe orang yang sering ngobrol, tapi seru",
                "pesan":"semangat terus ya bangg"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "kakaknya lucu gitu tingkahnya, bikin ketawa",
                "pesan":"Semoga kedepannya bisa keterima di tempat yang kakak sukai"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Dafa itu orangnya cool gitu dari yang saya liat",
                "pesan":"Semoga selalu diberi kesehatan ya banggg"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak ini seru orangnya dan kelihatan aktif banget",
                "pesan":"Semangat kulahnya kak, semoga cepat luluss"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Aura ekstrovertnya kerasa banget dan asik juga abangnya",
                "pesan":"Semoga aura ekstrovernya ga luntur ya bangg"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Bukan tipe yang banyak bicara, tapi nyaman kalau mengobrol",
                "pesan":"Sehat sehat terus ya kakk"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Keren sih abangnya, dari yang saya lihat itu berwibawa gitu",
                "pesan":"Semangat terus dan pantang menyerah ya bang"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "asik dan suka ngobrol dengan bang andra, karna pembawaannya itu enak",
                "pesan":"semoga terus diberi kesehatan dan kekuatan untuk maju terus"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "abang ini lucu banget, suka bikin saya ketawa",
                "pesan":"apapun yang terjadi jangan patah semangat ya bang"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "keren sih abangnya dan cool gitu",
                "pesan":"semangat terus bang kuliahnya"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak lucu dan enak diajak ngobrol",
                "pesan":"semoga bisa tercapai ya cita citanya"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kakak ini lucu dan imut gitu",
                "pesan":"sehat terus ya kak, agar bisa terus maju"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w12G5JVVOQe9y-uwOGw1ENLBq0S3Rahs",
            "https://drive.google.com/uc?export=view&id=1iwcPCpLUUsf9Cyalzno1RueW3-ODmdGn",#kharisma
            "https://drive.google.com/uc?export=view&id=1MEwwWbQdVZ8LuSYKzJVLthLFQK2hV6SD",
            "https://drive.google.com/uc?export=view&id=1SAaYOs7fMtrcE6HY_kovK-yPcW4qSoIY",
            "https://drive.google.com/uc?export=view&id=1BPJp9IzdMF5OmpXZBevvYBWyt9PnTqH9",
            "https://drive.google.com/uc?export=view&id=1MHgZ5Acx6OZNFd2z2_EMiM6nutCj0-fQ",#cerine
            "https://drive.google.com/uc?export=view&id=1mUaxKB_-6crqS7k-rxiIc3kQBUFNj7xX",
            "https://drive.google.com/uc?export=view&id=1dpBZKB8fNsJMTfXntHmLhA7ibmDfbVr6",
            "https://drive.google.com/uc?export=view&id=1VjHYYka4LmOdd4Yb3I-IosnORj9nsaB-",#rozak
            "https://drive.google.com/uc?export=view&id=169VVEV6vKZvHYdBryk9yYMz_U84GBzNI",
            "https://drive.google.com/uc?export=view&id=1dPd2Kz49NNiq0G4OPJ0EtKbIG-VZIyaX",
            "https://drive.google.com/uc?export=view&id=1Z9JO4jkQwNaz0w5UIg2cfdsFMKXt1rHy",#audina
            "https://drive.google.com/uc?export=view&id=1g25n6U7nhnodrG-MkqLs4HpwRJzC2iJZ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#gustin
            "https://drive.google.com/uc?export=view&id=1usOIXqXuvgwImLT71NvCULHHP0GRX8ge",
            "https://drive.google.com/uc?export=view&id=1Hyqr8xaoN5oruOJtl6i71O11qopsg76l",#rafa

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
                "kesan": "Bang haikal ini keren orangnya, bisa serius dan bercanda",
                "pesan":"Semoga kedepannya bang haikal bisa semakin keren lagi"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak ini asik dan lucu orangnya",
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak kren banget dan seru juga",
                "pesan":"semangat ya kakkk"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "bang farhan ini kayak bisa serius dan bercanda disaat yang hampir bersamaan",
                "pesan":"Semoga terus diberi kesehatan"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "selalu semangat dan lucu kakaknya",
                "pesan":"Semoga terus bersemangat"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal":"medan",
                "alamat": "Belwis",
                "hobbi": "Balap Liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "kakaknya lucu dan menyenangkan, enak diajak ngobrol",
                "pesan":"semangat terus ya kakk"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "keren si abangnya, seru gitu dan bikin ketawa",
                "pesan":"sehat sehat ya banggg"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin Cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kak najla ini orangnya lucu dan enak untuk diajak bercanda",
                "pesan":"semoga kakak bisa cepat diwisuda dan bisa diterima kerja ditempat impian kakak"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Abang ini suka bikin saya ketawa sih kalau ngobrol",
                "pesan":"pokoknya untuk bang Rozak semangat terus yaaaaa !!!"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Kakak ini punya suara yang khas gitu, kayak menjadi pembeda, kakaknya juga baik dan murah senyum",
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
                "kesan": "abang ini dari yang saya lihat itu tipikal orang yang sering bercanda",
                "pesan":"semangat terus kuliahnya ya banggg, agar bisa cepat lulusss"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "dari yang saya liat, visual kakak ini tipikal orang yang sangat sangat pintar akademik",
                "pesan":"untuk kak gustin pokoknya semangat terusss"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "abang ini punya hobi yang dilakuin orang have ya",
                "pesan":"semangat terus ya bang, jangan kasih kendor materi perkuliahan ituu !"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "cari duit",
                "sosmed": "@snasaa._",
                "kesan": "kakaknya ini pendiam, namun sangat berdedikasi",
                "pesan":"semoga selalu diberi kesehatan dan semangat terus kak cari uangnya !!!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1d6A2BKF4zUIYZLLSbkH5Qs66FaiA_ZEt",
            "https://drive.google.com/uc?export=view&id=1qfNobLCWEwEWj55htPvsKA-tI-uJt47K",#vany
            "https://drive.google.com/uc?export=view&id=1v59Rorz4oYH3JeuVdbQMKjLY5opWfsOE",
            "https://drive.google.com/uc?export=view&id=1ZRKjCqagn92UBU68xYN-TZSRp6jUJ6mD",
            "https://drive.google.com/uc?export=view&id=1MFQi-ZIUMZk5Y6RvgvCYdrWafOXaBElX",
            "https://drive.google.com/uc?export=view&id=1oGhf6UMPR3KuLaxaPFc3oBSB6Fv8Glwq",
            "https://drive.google.com/uc?export=view&id=1Su2L8FtqvHOyXdzpgzALO8i-KNu0PZrr",
            "https://drive.google.com/uc?export=view&id=1OjCnm1rOY2rzVS78sC1vqo54Yx3Ubef6",
            "https://drive.google.com/uc?export=view&id=1r5RnsK1Ekkd7wOKjVynATqBFGkWUo31S",
            "https://drive.google.com/uc?export=view&id=1Dh3IRuF0h-mGz48r7kxAFBy59pcN6m4f",
            "https://drive.google.com/uc?export=view&id=1Tdb-sNBaN-bPNDmiv8tpAD4r_mXR3N9I",
            "https://drive.google.com/uc?export=view&id=1hx4fxHo0dwC6z018P3pkVvxGdPHx1WpN",
            "https://drive.google.com/uc?export=view&id=1WylCMfRCZOhJ85dtbQGKGE6RVlJvPPF5",
            "https://drive.google.com/uc?export=view&id=17cGMNzZP_jf6Wcx2u-M9kU6U3xVt1j-o",
            "https://drive.google.com/uc?export=view&id=1usOIXqXuvgwImLT71NvCULHHP0GRX8ge",
            "https://drive.google.com/uc?export=view&id=121J109uHW7YX8W4NdU_GCIiFDBx_PPN-",
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
                "kesan": "Kak arienta awalnya keliatan serem, tapi aslinya baik dan lucu banget",
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
                "kesan": "Kak vany lucu dan imut bangett",
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
                "kesan": "Keren, jago sulap dan ngoding, berusaha yang terbaik demi kami",
                "pesan":"sehat terus ya bangg"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "sering menjadi yang terlalu bersinar di damaskus :)",
                "pesan":"Semangat kuliahnya bang azmi"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang ayake ini paling lucu dan soft spoken bagiku",
                "pesan":"Semangat terus ya bang kuliahnya"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Keren dan tampak sangar",
                "pesan":"Sehat selalu ya bangg"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kaka ini lucu dan asik banget deh walau awalnya bikin takut",
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
                "kesan": "Bang haikal baik dan keren",
                "pesan":"Sehat selalu ya banggg"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Lucu dan baikk walau kadang galak",
                "pesan":"Semangat terus kakaaa kuliahnya"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@queentanaabila",
                "kesan": "Awalnya saya takut, cuma aslinya baik dan lucu bangett",
                "pesan":"Sukses swelalu ya kak"# 1
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
                "kesan": "Kaka ini suka nyanyi dan juga lucu",
                "pesan":"semoga sehat selalu ya kak"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang jeremi ini baik dan menyenangkan",
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
                "kesan": "Abang ini keren dan cool",
                "pesan":"semoga sehat selalu bahagia"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "Kakak lucu dan suka senyum",
                "pesan":"lancar selalu kakaaa kuliahnya yaa^"
            }
        ]
    display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11xA6Mf7gHMKxbjk-IMWqTlNvO0_A45cq",
            "https://drive.google.com/uc?export=view&id=1bbht-gRdDjKNJALcCGghxsvdvfTANP2z",
            "https://drive.google.com/uc?export=view&id=1rE3vAFJSMdsiEGi2f0fJRB5HuxTK3zbF",
            "https://drive.google.com/uc?export=view&id=1jWO8lS1Xd5sns-efz4RUEM5mDL-P110E",
            "https://drive.google.com/uc?export=view&id=1axTo4GW7JSyQqOBFAJygbXsx6QmJjHEz",
            "https://drive.google.com/uc?export=view&id=1UNGVFYTpClvGdYRyBXs9qfPq3k-O1fXU",
            "https://drive.google.com/uc?export=view&id=/1j53WD7EUoJK4UapBrgUSiFm9SLQISW6f",
            "https://drive.google.com/uc?export=view&id=1dngVWPupgADnBwdie8h1kKyJHlys5_sd",
            "https://drive.google.com/uc?export=view&id=1Bp7SEJTe1KX9IJrKeVG0IjFt7rCu_DVC",
            "https://drive.google.com/uc?export=view&id=1V-wuNMSyuA_L_MenxzMrdi_SBMUZwW3o",
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
                "kesan": "Kak azizah wajahnya itu kayak tipe orang yang selalu serius gitu, tapi ternyata asik juga kakaknya",
                "pesan": "semoga kakak semangat terus ya kuliahnya, ga pantang menyerah!!."
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "first impressionku bang helmi keren banget orangnya",
                "pesan": "semoga bang helmy terus diberi kesehatan dan kuat terus belajarnya"
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Nemenin Wielman MC",
                "sosmed": "@barus.fernando",
                "kesan": "abang ini lucu dan suka bikin ketawa, dan unik juga ya hobinya",
                "pesan": "semoga bang wielman tidak merasa sendirian ya bang"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru ",
                "hobbi": "Baca",
                "sosmed": "@sciia__",
                "kesan": "kak suci keren banget si orangnya, tampang seriusnya menambah 99% aura",
                "pesan": "sehat sehat terus ya kak, semoga cita cita kakak cepat tercapai"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "jadi MC",
                "sosmed": "@wielhawn",
                "kesan": "abang ini kelihatannya tampan dan berani, keren pokoknya",
                "pesan": "tunjukkan terus suara emasmu bang"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "main hp",
                "sosmed": "@lia.h_264",
                "kesan": "kak lia ini tipikal orang yang tampangnya serius tapi aslinya lucu",
                "pesan": "semoga kak lia cita citanya cepat tercapai ya kak"
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Mentor bayesmup yang lucu bangettt, pas ketemu ada aja yang bikin ketawa",
                "pesan": "jangan sampai luntur ya kak ketawanya, semangat terus kakkk"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "jadi sekjen",
                "sosmed": "@hazelhandhaka",
                "kesan": "keliatannya kalem dan pendiem, tapi ternyata bisa ngelucu juga abangnya",
                "pesan": "sehat sehat terus ya bang, semoga cita cita abang bisa tercapai"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kak nadya ini bikin saya bernadya terus kalau ktemu",
                "pesan": "semoga hari hari kakak selalu berwarna"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani ",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang ",
                "alamat": "Jl. Lapas",
                "hobbi": "nonton film,musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "kak dwi rahma ini dari yang saya lihat itu tipikal orang yang pendiem dan sedikit bicara gitu orangnya",
                "pesan": "semangat kuliahnya kak, biar cepat diwisudaaa"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1l-8hvhOwmfJWprJOv0Ykk22DNWJrPjWQ",
            "https://drive.google.com/uc?export=view&id=1-pwn6fGSVOWPpefr19JQDy_OReG3gbrf",
            "https://drive.google.com/uc?export=view&id=1Ie0kH53v4AQa6z-ddtlDbnLXL_ObI7zK",
            "https://drive.google.com/uc?export=view&id=198bNM2JTJLvg20eKwOFilA1LF7hgTET2",#Fathya
            "https://drive.google.com/uc?export=view&id=1dSXGIWFGwhsqGe79nitmJ9m89VTNYMeZ",
            "https://drive.google.com/uc?export=view&id=1aA_vM0LHm1yw17r09OZQO8T2FeIqx_Rr",
            "https://drive.google.com/uc?export=view&id=1YPl62QJ1--OliIABgD_f4CvPt0UNzyCu",
            "https://drive.google.com/uc?export=view&id=1n3mT8gJP3OmYtnultwnFlBUIcmxipMRi",
            "https://drive.google.com/uc?export=view&id=1-rxtsIQy8C8IEgxEbcffwUhWWm_dkURW",
            "https://drive.google.com/uc?export=view&id=1BO2GUhheRHymCqTXLH_CBda29om897eq",#yazid
            "https://drive.google.com/uc?export=view&id=1kKaB0xv5B-YX9ePpH5_z9SaXAf86Neep",
            "https://drive.google.com/uc?export=view&id=1qwKUs-z01aYGUKLzYUPRD7O85ulGA104",
            "https://drive.google.com/uc?export=view&id=1aQu1PLRqCPfcXh4hyjETowtNjYnjS93-",#muttoharoh
            "https://drive.google.com/uc?export=view&id=1WadifPhMB7P2NdcIYLDrS7QCwkgwuj8j",#ahmad rizki
            "https://drive.google.com/uc?export=view&id=1Un0QuoW6CWyWqZG2GvgkuDb3ZL6pdXuy",#indah
            "https://drive.google.com/uc?export=view&id=1u8XMtTJpbVny4Nmjm3zHsYHZlbw1F5-U",#bima
            "https://drive.google.com/uc?export=view&id=1kAPTZH_E_qLb2A5n2IA3lKjyZ-4E_yPE",#bimo
            "https://drive.google.com/uc?export=view&id=1CMJ-Yf3COH9aGxkmleR2-2Ght_1TDCBh",#adinda
            "https://drive.google.com/uc?export=view&id=1Qaa1EJuM0C2V27Ju6LgxSHXxLtGGg1Ld",#yollanda
            "https://drive.google.com/uc?export=view&id=1HgxPXo2BHNfoZ3SHSygNrJeQkqccHwox",#riska
            "https://drive.google.com/uc?export=view&id=1XT4U5mo_xX-jItoaHo6EKIrduBnr9w0H",#alfayya
            "https://drive.google.com/uc?export=view&id=1MJ8SS-ajVEsQJlefoQBc0_moSpIkdgRe",#asri

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
                "kesan": "ngeliat kak arini tuh awalnya bikin takut karna sifatnya tegas, tapi ternyata baik bangett",
                "pesan": "Semangat ya kakkkkkk, apalagi TAnya"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya itu lucu bangettt",
                "pesan": "apapun masalah kakak didepan, lewati dengan senyuman ya kakk"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "orang ter humble yang saya liat, cuma kalau sudah sekali ditanya itu, pasti  pertanyaan pertanyaan lain bisa tiba tiba muncull",
                "pesan": "terimakasih ya bang telah sering bikin saya ketawa dengan nyaman, meskipun saya orangnya nyebelin tapi dipanggil terus :)"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "kakak cantik ini awalnya karna dari tampangnya itu bikin takut, cuma ternyata lucu dan asik bangetttttt, jadi suka dehhh",
                "pesan": "Semoga kakak cantik menjadi semakin cantik dan berseri, gada yang bikin kakak sedih, serta menjadi kakak yang paling cantikkkkkk"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "-",
                "asal": "Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "@tari_",
                "kesan": "kakak paling lucuuuuuu dan sering bikin saya ketawa, kakaknya juga pinter pake banget banget banget banget deh pokoknya",
                "pesan": "pokoknya semangat terus ya kak, agar bisa diwisuda dan bisa diterima kerja di tempat yang kakak impikamn, serta berkeluarga yang bahagia :)"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "kak selma ini kalau senyum itu enak banget gitu diliatnya, kayak punya semacam senyuman khass",
                "pesan": "semangat terus ya kak selma, semoga diberikan kelancaran setiap urusannya dan cepat cepat cepat dapat pekerjaan yang diimpikan, yang dimau, yang disuka, yang yang deh"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "sini",
                "alamat": "jauh pokoknya",
                "hobbi": "tidur",
                "sosmed": "@kshigf",
                "kesan": "suaranya lucu gitu didengarrr, jadi enak kalau ngobrol dengan kakak, apalagi gaya bicara kak ashila juga enak banget didengerrr",
                "pesan": "semoga kak ashila dilancarkan urusannya, cepat diwisuda, dapat kerja, jadi ceo, berkeluarga yang sakinah mawadah warohmah deh pokoknya"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "bang duta dan itera ganteng ini keren banget sih jujur yaa, berdedikasi tinggi, pintar berbicara dan banyak lagi",
                "pesan": "untuk abang itera ganteng ini semoga bisa lulus tepat waktu dan tanpa kendala, dan ditunggu ya bang zumbanya"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "abang inimah paling beh beh beh, kerennya dirual nurul dan aziz, suka bercanda dan ternyata bisa serius juga abangnya, kadang saya juga sampai gabisa berkata kata sama tingkah bang vian",
                "pesan": "untuk bang vian tercintah semoga cepat diwisuda dan berkeluarga ya baang, sehat terus, jadi ceo, semangat terus, bahagia, sakinah mawadah warohmah"# 1
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "((15≪1) & 31) ⊕ 10",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Bang yazid inis secara visual itu enak diliat, gada tampang yang nyeremin gituu, dan orangnya asikk pake banget",
                "pesan": "untuk bang yazid semoga bisa masuk itera ganteng juga, karna visualnya itu mendukung banget, terus sehat selalu, dilancarkan urusannya, dan diberi kemudahan dalam hidup"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah ",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "tanyain sama yuder",
                "sosmed": "@jaldii._",
                "kesan": "Bang jaldi ini sih jujurr enak banget orangnya, enak diajak ngobrol, banyak banget topik yang disiapin, trus suka bercanda juga, public speakingny juga bagus",
                "pesan": "semangat terus ya bang jaldi, semoga rezekinya ngalir terussss ga habis habis, diberi kelancaran urusannya dan bisa diterima kerja ditempat yang abang mau"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "kak kia ini lucu banget karna tingkahnya yang kadang random dan diluar nurull, kakaknya juga imut ",
                "pesan": "semangat terus ya kak kuliahnya, sehat selalu, dilancarkan urusannya dan bahagia selalu, serta  diberi kemudahan dalam menjalankan hidup di pahtnya dunia"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kak mut itu orangnya lucu dan menggemaskan, suka bikin ketawa",
                "pesan": "semoga menang ya kak pimnasnyaaaaa, lalu diberi kesehatan serta ketabahan untuk menjalani hidup"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "termasuk salah satu abang terkeren sih bagiku",
                "pesan": "semangat terus ya bang menjalani perkuliahan ini"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "kakaknya ini lucu dan baik banget, selalu gercep kalau ada masalah",
                "pesan": "hidup dibawa enjoy aja ya kak, jangan terlalu dipusingkan"# 1
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung ",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "awalnya kalau ngeliat bang bima itu takut, karna tampangnya itu serius dan nyeremin banget, tpi ternyata lucu juga abangnya",
                "pesan": "semangat terus ya bang, dijaga juga kesehatannya"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus ",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "bang bimo ini tipikal orang apa apa itu dibawa enjoy",
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
                "kesan": "kak adinda ini dari kelihatannya terlihat seperti orang yang pintar, kalem dan pendiem",
                "pesan": "Semangat terus kuliahnya, semoga ilmunya berkah dan bermanfaat."# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "lucu dan imut, asik banget kalau sedang mengobrol dan bercanda",
                "pesan": "Sehat selalu ya kak, jangan lupa jaga pola makan dan istirahatnya."
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "kakak terlucuuuuuu, imutttttt, baik hati dan suka membantu saya kalau adda masalah",
                "pesan": "semoga dapat jodoh yang tinggi sampai 210 cm, seorang ceo, anak tunggal, dapat mertua yang baik, disayang suami dan sebagainya"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "abangnya lucu dan enak kalau ngobrol, terus tampangnya terlihat serius",
                "pesan": "Sukses terus untuk setiap langkah dan rencana ke depannya, ya bang"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "senyumnya bikin cyandu",
                "pesan": "Jangan lupa istirahat di sela-sela kesibukannya ya, kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zNmOQ7l7AN1Z7ocF-A9e2mp71g-Benk1",#fabio
            "https://drive.google.com/uc?export=view&id=1k6nt-CqKfsnmrB0K2CYNDDGrGrv6Ey3d",#tanty
            "https://drive.google.com/uc?export=view&id=",#fadil prasetyo
            "https://drive.google.com/uc?export=view&id=1O8yaDFRuEIwPfgjGmdV4ZnrjFLOdKrCe",#manuel
            "https://drive.google.com/uc?export=view&id=1ZIpwdUkBR6_q1V22BHBHX3ScBhoiQsNQ",#ni made
            "https://drive.google.com/uc?export=view&id=1bG6vFxIe7FfSThNm6izZs5iYq_q5VQfk",#risa
            "https://drive.google.com/uc?export=view&id=1MACJ2ib0vyrklCEjY0BQhgrUYV2NIs8Y",#vannisa
            "https://drive.google.com/uc?export=view&id=1VxNd7omiz2-DatV3fzsRDUBWCdp1AcRK",#yulia
            "https://drive.google.com/uc?export=view&id=1aDxeXWyuu_IrROoOvjzZFmM6JE3KyOfG",#akeyla
            "https://drive.google.com/uc?export=view&id=1_WrhGN-8Hpl6yrlNpuK9i2lsXFc29aXd",#elsa
            "https://drive.google.com/uc?export=view&id=1spG7M5xoVXYWq5m-lQ3B1n6Szj3uXYFU",#fadya
            "https://drive.google.com/uc?export=view&id=1BgO87Pe2Vr2ZCU-P3CtJ8lIjrRRx5u1w",#lovi
            "https://drive.google.com/uc?export=view&id=1d8mevW0sSCMmbPceCnMerPAE0v0zVEBO",#alsi
            "https://drive.google.com/uc?export=view&id=1Wkxl0kzLw3X4hZPYf-xmb1k0kp7Sy8Oh",#sherena
            "https://drive.google.com/uc?export=view&id=16a9hhkUvx_bBil41hOfz3vUL5318ZHl2",#razin
            "https://drive.google.com/uc?export=view&id=15jJxgZwKMh63fdpn49pYu1nD2hni4yTV",#Faiza
            "https://drive.google.com/uc?export=view&id=19SrHnmJNSsMs1x_Oh_4cVJYw6GrtlEvk",#gathan
            "https://drive.google.com/uc?export=view&id=1lxqy7crgla5ugUeyaDrn7iKXwvD_-Jxi",#hafidz
            "https://drive.google.com/uc?export=view&id=1Tuga4rd5QHb1TEeGukUrl86SfKGx0pw9",#kaleb
            "https://drive.google.com/uc?export=view&id=1peGmgmXCiOB9u6ivVbYQ39AIPF228Myt",#melva
            "https://drive.google.com/uc?export=view&id=1YcVGfIhJxtOemYBneDt8lMEVkHeBi9BY",#falakh
            "https://drive.google.com/uc?export=view&id=10X9eJge1bQwmCIEGUFXH-ZZt3uZPdnPq",#henry

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
                "kesan": "keren, sekalinya bicara itu jelas, namun chat lama dibalesnya",
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
                "kesan": "lucuuuu, suka diajak bercanda, fast respon deh kalau ngobroll",
                "pesan": "Bahagia dan ceria selalu ya kak, semoga harinya menyenangkan"# 1
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "kagum si saya sama bang fadil, karena tetap semangat dikala capek capeknya",
                "pesan": "semoga amal ibadah abang diterima disisi tuhan"# 1
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis ",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "keren sih abangnya, perawakannya menggambarkan orang yang berwibawa",
                "pesan": "Semoga dimudahkan segala urusannya dan dijauhkan dari rasa lelah yang berlebihan"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12",
                "asal": "Bali",
                "alamat": "nusa peninda",
                "hobbi": "menghayal",
                "sosmed": "@violaadrtr_",
                "kesan": "lucu imuet dan menggemaskan dan bikin nyaman kalau ngobrol",
                "pesan": "Semangat terus mengejar mimpi dan cita-citanya, kak."# 1
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "kak risani enak aja kalau diajak ngobrol, orangnya humble",
                "pesan": "Semoga berkah selalu setiap ilmu yang kakak pelajari dan bagikan."# 1
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "1244500078",
                "umur": "19",
                "asal": "kepulauan riau",
                "alamat": "teluk betung",
                "hobbi": "nonton khw",
                "sosmed": "@vunnycaa",
                "kesan": "berwibawa banget deh pokoknya",
                "pesan": "Semoga lelahnya selama ini berbuah manis dan jadi berkat ya kakk, dan jangan mudah menyerah"# 1
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "tampang tampang serius, namun sebenarnya lucuu",
                "pesan": "Semoga semua target dan urusannya bisa beres tepat waktu, kak"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@keyashafi_",
                "kesan": "bang akeyla ini asik dan enak kalau diajak bercanda",
                "pesan": "Sehat dan sukses selalu menyertai hari-hari abang."# 1
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara ",
                "alamat": "Pemda",
                "hobbi": "Sibuk",
                "sosmed": "@_els.a",
                "kesan": "dari yang saya liat ini kakaknya ini pendiem, namun semangat teruss",
                "pesan": "Semoga dimudahkan segala urusan akademik maupun non-akademiknya, kak"# 1
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "airan",
                "hobbi": "mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "kakaknya terlihat seperti ambivert, kadang ekstrovert, kadang introvert",
                "pesan": "Semangat terus tanpa kendor menghadapi hari-hari kuliahnya kak"# 1
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "kak lovi ini dah keren, cantik, pintar lagi orangnya",
                "pesan": "pokoknya Sukses selalu untuk karier dan masa depannya ya kak!!!"# 1
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "kalianda",
                "alamat": "kota baru",
                "hobbi": "main game, tidur",
                "sosmed": "@aluccy_",
                "kesan": "bang alsi ini tipikal orang yang sedikit bicara banyak bertindak",
                "pesan": "semoga abangnya selalu diberi kemudahan"# 1
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal":"Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "kakaknya ini lucu, meski tampangnya agak menyeramkan",
                "pesan": "Semoga IP semester ini memuaskan dan sesuai harapan kakak ya kakk."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "keren sih abangnya, apalagi hobinya futsal",
                "pesan": "Semangat terus ya bangg, aura positifnya jangan luntur"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel ",
                "sosmed": "@faizaanjanii",
                "kesan": "kak faiza ini lucu, namun tidak terlalu banyak bicaranyaa",
                "pesan": "Gas terus semangatnya, jangan sampe kendor kak"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Rajabasa Raya",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "kelihataan banget abang ini berwibawa, auranya terasa",
                "pesan": "Semoga vibes-nya selalu positif dan happy terus bangg"
            },
{
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur ",
                "hobbi": "3N ( Ngoding , Ngegame, Nyibukin Diri)",
                "sosmed": "@apiszzaja",
                "kesan": "enak pake banget kalau diajak ngobrol, abangnya juga soft spoken",
                "pesan": "Semoga hari-hari abang selalu dikelilingi energi positif ya banggg!"# 1
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Campang Raya, Sukabumi",
                "hobbi": "Gym, membaca, dan bermain",
                "sosmed": "@kelelep_comberan",
                "kesan": "keren bangett, apalagi pas nutorin saya ALE, mudah mahamin materinya",
                "pesan": "Tetap keren dan kece badai ya bang, jangan kasih kendor pokoknya"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal":"Sumatera Selatan ",
                "alamat": "Sukarame ",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "kyuttt, enak diajak ngobrol, senyumannya khas gitu",
                "pesan": "Semoga hari-hari kakak bebas dari beban berat ya kakk"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syafiqui",
                "kesan": "keren pokoknya, pertama kali melihat abang ini pas fg itu langsung kagum",
                "pesan": "Semoga apa pun yang abang usahain sekarang hasilnya maksimal."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal":"Kotabumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "ngeliat abang ini pas damaskus itu kliatan keren banget, semangatnya besar",
                "pesan": "semoga semangat bang henry ga kendor kendor ya bang"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qFLHu6Zfer-tEnRHVFUXJ3xEHkRoaiZM",#ihsan
            "https://drive.google.com/uc?export=view&id=1TqmHd6LYvwg4mGNeuG6J8HzzC76JBndO",#hanifah
            "https://drive.google.com/uc?export=view&id=1g9G7-Ft8MhUwyEr0f7KkqQzIkAxLKSNs",#afifah
            "https://drive.google.com/uc?export=view&id=1Zv28YkXSaWl-MfUlzB3MDOax9rAVY19v",#hasan
            "https://drive.google.com/uc?export=view&id=116VOsVUOre6mn7DxJa1GHNiSFpt6LjUM",#layina
            "https://drive.google.com/uc?export=view&id=1Ks29QOxQEuMGNUSXsh_czGbWWsfdhTPL",#moch iqball
            "https://drive.google.com/uc?export=view&id=1ae83eAjrPA6ni27sbfQq4oe2X9L713Ew",#talitha
            "https://drive.google.com/uc?export=view&id=19zicOsKVWRH1Wj9wfgRYYcGGwCXr_Yv6",#anadia
            "https://drive.google.com/uc?export=view&id=1xOz_A3bY395mApsOh9_lhXms2mudnCi_",#abdillah
            "https://drive.google.com/uc?export=view&id=1ByURNpkPc466DbYy10krBUIhq1EKVbfb",#afdal
            "https://drive.google.com/uc?export=view&id=15QpAhu1___6mYN_sGmfwEMQM5mx0nHh-",#anggun
            "https://drive.google.com/uc?export=view&id=1zSyO851q-NaVTs72l45cr6jFRMnmexx4",#della


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
                "kesan": "ganteng, keren dan berwibawa skalihhh",
                "pesan": "semangat terus bang untuk menghasilkan uangg"# 1
            },
            {
                "nama": "hanifah inaya sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "lucu banget sih kakak ini, murah senyum, dan ternyata aku baru sadar klo kakak ini nimnya ternyata sama",
                "pesan": "Semoga keringat dan kerja kerasnya terbayar tuntas dengan hasil terbaik."# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "lucu dan imut banget, jilbab pink kakak cocok banget deh dipake sama kakak",
                "pesan": "disela sela kesibukan jangan lupa istirahat ya kakk"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "pertama kali ngeliat abang ini pas pplkk, jujur keren banget si karna bisa bikin saya tenang pas pplk",
                "pesan": "Semoga hari-hari abang adem ayem dan penuh ketenangan di hecticnya dunia ini."
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin",
                "sosmed": "@lay.inr_",
                "kesan": "mukanya itu kayak muka orang serius sih kak, tapi ternyata kakaknya lucu bingit",
                "pesan": "Semoga gak ada plan yang meleset dari target ya kak."# 1
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "abang ini keliatan imut sih ^w^",
                "pesan": "Semoga kesuksesan besar selalu membersamai setiap langkah kaki abang"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "@talljtine_",
                "kesan": "lucu dan imuet bingit kakaknyaaa",
                "pesan": "Semangat kuliahnya, semoga ilmunya berkah dan langsung nyangkut di otak ya kakk"# 1
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "mukanya kelihatan agak seram sih, ternyata lucu banget kakaknya ini",
                "pesan": "Sukses terus buat kakak, semoga semua mimpi indahnya jadi nyata."# 1
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "abang ini menerapkan konsep ganteng, imut dan keren disaat yang bersamaan",
                "pesan": "Jaga kesehatan terus ya bangg, jangan sampe drop badannya."# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "keren abangnya, kalau diajak ngobrol itu enak, suka ngelucu juga",
                "pesan": "Sehat, waras, dan sukses terus pokoknya buat abangg"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "lucu kakaknya, tudep gitu orangnya",
                "pesan": "Semoga harinya seru terus dan gak bikin emosi ya kak!"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "dari yang saya liat kakaknya ini keren dan berwibawa gitu",
                "pesan": "Semangat terus ya kak, jaga kondisi fisik dan mental baik-baik, apalagi sudah semester tinggi :)"# 1
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1S5qI9jV7PDjMUfn10zrqFyxMI6hEtf13",#nayla
            "https://drive.google.com/uc?export=view&id=1quMCA2yz81Eo5Et7E31TT8QMeSTRVKoV",#donna
            "https://drive.google.com/uc?export=view&id=1KYtSE08eRGAD6VGjFwFpVvchcCe-m-AC",#labo
            "https://drive.google.com/uc?export=view&id=1khXqY8CpJ5dP9T2WtFCAsFJL8YEmAQso",#anash
            "https://drive.google.com/uc?export=view&id=1bx1SoRcFtnBCU3ydSyP5uUGLdPE3W-Yr",#felisya
            "https://drive.google.com/uc?export=view&id=1yzr0L_x1pjdw_HUJlws40ujN-ioBocFY",#razan
            "https://drive.google.com/uc?export=view&id=1Kq8L5uaxGk6_rvuo19hBuSM7H8ekWUao",#sania
            "https://drive.google.com/uc?export=view&id=1HT8OG4P8fk4LlgpUw_9eCq8qzpqMXuHE",#allisha
            "https://drive.google.com/uc?export=view&id=1_cc6x-1EdOj7_2sWCutsRpNsh30bqhBk",#alya
            "https://drive.google.com/uc?export=view&id=1HAe6LzVRm7AswkY-b1Nmn7OhFcpPu7Ks",#bunga
            "https://drive.google.com/uc?export=view&id=1mwoafsikYskCSKocDF7pvKXT_6qlcGD_",#difanya
            "https://drive.google.com/uc?export=view&id=11ZYk2WfDjBUz_qcCVGYZ-ZZ866JbiDMv",#nazlah
            "https://drive.google.com/uc?export=view&id=1d0L0xO_h1JvOpgQGDRVKlNHj5NVrB2DI",#raihana
            "https://drive.google.com/uc?export=view&id=1gLmZITXmVsGFvbGbPz-YmrFMJ893vq79",#daffa
            "https://drive.google.com/uc?export=view&id=13KI0g25BAHrLQObqe1gecmiZK5XHZvXh",#edsel
            "https://drive.google.com/uc?export=view&id=1IFAhCWvcDbhr0QSf97rQdzwo-izubjG2",#lucia
            "https://drive.google.com/uc?export=view&id=11M7WPZlJlt2buuw3YwP38QIOE1s2e424",#shafa
            "https://drive.google.com/uc?export=view&id=1BghBusAwNuVEVXhNOWnf2oqBiydGK4Ct",#zannuba

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
                "kesan": "tampangnya agak sangar, tapi baik banget",
                "pesan": "Jangan lupa ketawa hari ini, biar hidupnya gak tegang, hehe."# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "lucu dan imut sih kakaknyaa",
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
                "kesan": "bang labo ini udah keren, pinter, baik lagi",
                "pesan": "kalau motoran malam malam jangan lupa pakai jaket ya bang, nanti masuk angin"# 1
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
                "pesan": "Sehat-sehat terus ya kak, kurang-kurangin begadang nontonnya kak, nanti sakit"
            },
            {
                "nama": "Felisya Nabila Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal": "Lampung Timur ",
                "alamat": "Kota Baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "kakaknya enak kalau diajak bercanda",
                "pesan": "Jangan jail jail terus kak, nanti mereka jailin balik :)"# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "21",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "jago motret abang ini, emang udah jiwanya di departemen inih",
                "pesan": "kapan kapan boleh kali bang fotoin saya hehehe"# 1
            },
            {
                "nama": "Sania DWi Ayu Lestari",
                "nim": "124450086",
                "umur": "21",
                "asal": "Karawang ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "pas saya ngeliat kakak ini first impressionnya itu kakaknya ini pendiem ternyata suka ngobrol",
                "pesan": "Tetap keren, humble, dan sebarkan aura positif terus ya kak!"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "kakanya cantik dan tentu saja imut",
                "pesan": "Semoga harinya seru terus dan gak bikin darah tinggi ya kakkkk!!!"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "kakaknya ini ramah banget, soft spoken jugaa",
                "pesan": "pengen deh diajak jalan jalan juga"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "kayaknya kakak ini kalau jadi visual fl di novel cocok banget kak",
                "pesan": "Semoga segala urusan yang bikin ribet lekas tuntas dengan mulus, kak."# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Alquran",
                "sosmed": "@difanyhsa_",
                "kesan": "lut pake bangettt, soft spoken jugaa",
                "pesan": "hobinya kakak ini subhanallah banget, semoga sya juga jadi lebih giat baca Alqur'an"# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@nzlhauly_",
                "kesan": "kakaknya ini udah cantik, baik dan cute lagi",
                "pesan": "kapan kapan bisa kali kak ajarin saya berenang, soalnya tenggelam terus hehe"# 1
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
                "kesan": "first impressionku itu abangnya ini kayak anak nakal gitu, ternyata beda jauh pake banget :)",
                "pesan":"Semangat terus ya bangg, jaga kondisi fisik biar tetap fit."
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "abangnya kelihatan cool, itusih yang bikin keren",
                "pesan": "Semoga selalu dilancarkan dalam hal apa pun yang sedang dikerjakan."# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "jujur awalnya takut karna keliatan galak, tapi ternyata enggak :)",
                "pesan": "Semoga hari hari kedepannya penuh kejutan seru dan hal-hal asik pake banget untuk kakak."
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis dan menulis",
                "sosmed": "@_shaazzh",
                "kesan": "kakaknya ini ramah, imut dan soft spoken banget",
                "pesan": "Semangat terus jalani aktivitas padatnya, tetap dibawa happy aja ya kak!!!!"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "kakaknya cantik, namun ga imut karena imutnya pake bangett",
                "pesan": "Tetap semangat, jangan gampang badmood apalagi mellow, ya kak!"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
# Tambahkan menu lainnya sesuai kebutuhan
