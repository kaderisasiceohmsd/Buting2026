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
            "https://drive.google.com/uc?export=view&id=1NXV0ECB8OUztJJUeZKTsc6lM2VToUt34",
            "https://drive.google.com/uc?export=view&id=1G-3XKw2y4vw2NLlMY4--IJ3GXpWx6PWN",
            "https://drive.google.com/uc?export=view&id=1EMLdsxhuRocxvwX9MrnxMRvUsuRh7rZO",
            "https://drive.google.com/uc?export=view&id=1dc3IAue-NgNttcR4asAODVP60tWY91nQ",
            "https://drive.google.com/uc?export=view&id=17bkuJzulY2c8KbWtTIGg0rvF0R7fY5IS",
            "https://drive.google.com/uc?export=view&id=1KOMsigI24XhhcfD4iCyiE8XfJGnk4YRA",
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
                "pesan":"Pijarkan api semenyala mungkin bang, jangan sampai padam"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil keren banget apalagi pas ngejelasin materi",  
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
                "kesan": "Kakak efi suka banget penjelasan waktu materi, keren banget ngeliatnya.",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois orangnya unik, lucu, dan hobinya seru sepertinya.",  
                "pesan": "Semangat kuliahnya bang, semoga ga ada hambatan dalam menempul hal yang di inginkan."
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa orangnya lucu banget, dan kalo ketawa bikin nular.",  
                "pesan": "Semoga kedepannya hani bisa tumbuh seperti kakak yang keren, dan tetap senyum ya kak jangan sampai pudar"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Dari kak lutfia aku mendapatkan insight baru disunia perkulihan.",  
                "pesan": "Semoga lancar kuliahnya, karna aku pingin denger banyak cerita lagi dari kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EINzOceEaYbD2JSZvOA3p0bxtiSqBmIV",
            "https://drive.google.com/uc?export=view&id=1WLYyjiRX2RZNd-WsBsHe6D0XUCUY5D2E",
            "https://drive.google.com/uc?export=view&id=1nwovRCQ4f20QTUU5-l1Y_i2yiDjd9iJc",
            "https://drive.google.com/uc?export=view&id=1hNl1JgNO3xZEXBjiduvNhOhZL_eUmo6H",
            "https://drive.google.com/uc?export=view&id=1jL5rKV6YhnBxcdBAGA9kk073URW6bZXn",
            "https://drive.google.com/uc?export=view&id=1LKrFNBakZZZOKGnW5c5bwTpta62djJZa",
            "https://drive.google.com/uc?export=view&id=1i-U2dV72juuiXFuIrYMD74n-yoLsRVH2",
            "https://drive.google.com/uc?export=view&id=1Jl7laA_S_NkzbMZMrgBTynN9buI5Lc9B",
            "https://drive.google.com/uc?export=view&id=1EoYev3u4IKKikAt8UhE5vd3MgCMwq-6D",
            "https://drive.google.com/uc?export=view&id=1KQIyf49dnfg7hQxHN11-bmReKHEpvZMV",
            "https://drive.google.com/uc?export=view&id=1V1mVgVBvUTBi9QPs1Kxkky5isnDvUQcv",
            "https://drive.google.com/uc?export=view&id=1NDtPlQSFQ78upiz6hjY5u4h6ywxIyswD",
            "https://drive.google.com/uc?export=view&id=1fKPt9Ght0yLRG_zAjTA8UzfdXxeUPNGi",

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
                "kesan": "Bang Ridho orangnya lucu banget, banyak hal yang didapakan dari ceritanya.",  
                "pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kakak mentor TPB aku yang sangat keren dan prestasinya sangat WOWWW.",  
                "pesan": "semangat terus kuliahnya kakak !!!, tetap ceria ya kak jangan pernah pudarsenyumnya"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Bang Dharu yang punya segudang prestasi, contoh yang baik dan meningkatkan semangatku untuk mengikuti jejaknya.",  
                "pesan": "Kobarkan semangat terus bang untuk meraih prestasi yang lebih banyak lagi!!!"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Abang Asprak ALPRO aku yang humoris.",  
                "pesan": "Semangat buat jadi asprak MK lainnya bang!!!!"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kakak yang baik hati, cantik, setiap ngeliat mukanya sejuk banget bawaannya.",  
                "pesan": "Mari tebarkan senyum itu kak biar orang lain ketika melihatnya ikut happy"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro orangnya suka ngelu hal yang random banget.",  
                "pesan": "Semangat kuliahnya bang, jangan sering ngelucu perutnya sakit pas ketawa"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakak tutor metnum yang kalo ngajarin jelas banget akusuka metodenya.",  
                "pesan": "Harus jadi tutor privat aku sih kak"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "BTW nama panggilan kita sama kakkk.",  
                "pesan":"Semoga sehat terus ya kak, semangat buat meraih mimpi-mimpinyaaaa"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Aku ga bisa bedain antara bang Jeremia sama bang Kaleb semirip itu menurut aku",  
                "pesan":"Jangan sering-sering nempel sama bang jon takut ngeliatnya"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya seru dan lucuuuuu bangetttt omgg",  
                "pesan":"Semangat menjelajahi dunia bang"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Aku pikir bang jona itu medis ternyata Baleg keren banget sih, syok pas diteriakin dilapangan",  
                "pesan":"Jangan diteriakin lagi ya bang"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Keren banget waktu dilapangan ngawasinnya",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kenal pas di kelas KDP ngeliatnya aku terpesona banget ga tau kenapa",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VO4n_QWkD4Od-TSCG9_dz9SXpam3x7JP",
            "https://drive.google.com/uc?export=view&id=1HAXjISF5IYlAU7RlP5bSF5xtfbeWMXvc",
            "https://drive.google.com/uc?export=view&id=1RlxhzaT1Tzbx3WePKuBHw6SNpwexn4EA",
            "https://drive.google.com/uc?export=view&id=160M584UVgKoiF9VIa8R84Rn-T0agnSol",
            "https://drive.google.com/uc?export=view&id=1tNrjmsnFGNChpgWz1XMiRTLX_vERXvvI",
            "https://drive.google.com/uc?export=view&id=16LQ_JCws1wd9qg8At4r8_G_FfL95_qLb",
            "https://drive.google.com/uc?export=view&id=181As08N5v3dK7GP4EdycPJiMAroPLrFq",
            "https://drive.google.com/uc?export=view&id=1QliBymxCl8dqdMVS6WEEX1eyYFAt2X2O",
            "https://drive.google.com/uc?export=view&id=1OmoB5Ny19KtUGXTKnRegWZcd8jR3Gx2S",
            "https://drive.google.com/uc?export=view&id=1mZPLq-PC3uAN_43nJxC5wTRKne65qa9P",
            "https://drive.google.com/uc?export=view&id=1iwOcPKTNqMLipyBHMrHctSm5uEM6zqav",
            "https://drive.google.com/uc?export=view&id=1RvigC2eZCSi_ft_aAl3H1Db6dUi2SDLd",
            "https://drive.google.com/uc?export=view&id=1QN-TFPZw7GZm9c5ouEkbNPAnGAsRwqYw",
            "https://drive.google.com/uc?export=view&id=1yCE-J3QmD5PyeZF3kzDyKoiG8aEqIq-y",
            "https://drive.google.com/uc?export=view&id=1EhZWRi2QvmrjtUUdzb4MOJtMdJHniqMo",

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
                "kesan": "Bang Kevin ga nyangkan ternyata kadep minbak keren banget sih.",  
                "pesan": "Semangatkuliahnya bang, semoga ga ada mk yang ngulang lagi"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini asik, dan aku terpesona sama kecantikkannya sihhh omggg",  
                "pesan": "Jangan sampe kena tipu lagi ya kak"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Abangnya lucu banget",  
                "pesan": "Semangat untuk menjelajah dunia dan terbang setinggi mungkin"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakak yang cantik dan baik hati suka banget love.",  
                "pesan": "Pancarkan cahaya yang dipunya kak!!"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abang yang aku sering liat di damaskus ternyata anak minbak keren.",  
                "pesan": "Jangan pernah cape untuk jadi medis ya bang"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakaknya cute banget, suka deh ngeliatnya.",  
                "pesan": "Semangat buat kedepannya menjalani banyak rindangan di hidup ini."# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Abang asprak alpro aku yang keren banget dan baik hati.",  
                "pesan": "Semoga kedepannya hani bisa jadi asprak alpro kaya abang"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakak yang cute, cantik, dan sering cerita yang bisa aku ambil pelajran dari hidupnya.",  
                "pesan": "Jangan lelah buat menghadapi dunia ya kak"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Orangnya lucu banget",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Palu tensor 24 yang keren dan keren banget ngeliat dia bangga sama tensornya",  
                "pesan": "Kapan badminton sama tensor 25 bang!!"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "abangnya lucu banget ketika lagi cerita sering diledekin sama temennya ",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri ",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kakak yang keren banget, pasti narinya jugakeren sih",  
                "pesan": "semangat buat terus nari kak, ajarin aku buat lenturin tubuh alias nari"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abangnya keren banget",  
                "pesan": "semangat terus kuliahnya kakak !!! semangat menjalankan tugas di minbak"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal":"Surabaya ",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Abangnya keren banget, pasti punya kebon sawit berhektar-hektar",  
                "pesan": "OTW jadi CEO SAWIT!!! semangat menjalankan tugas di minbak, "# 1
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Uw5IyIYrfpIbNyxaKCYCqU98a_iQ5F8I",
            "https://drive.google.com/uc?export=view&id=1mylWhn9GSbeU7zD73Who3vQe_Rho4w8L",
            "https://drive.google.com/uc?export=view&id=1_ceWsXsTB5_BCIa_Xmxkzf7bsRPEZqVi",
            "https://drive.google.com/uc?export=view&id=1NuoNgp6bRY17k_WXyTUsZj0FbatGuhof",
            "https://drive.google.com/uc?export=view&id=1Q5viHnfgjEWNojKprcEd_xrflV1RRnt5",
            "https://drive.google.com/uc?export=view&id=1iEKrVwwVMsvwgqWjnfcmvSKH-q4KNlll",
            "https://drive.google.com/uc?export=view&id=1sR7Fh6QpSJNKQbe22m09Avl78GfprEy4",
            "https://drive.google.com/uc?export=view&id=1C_9LAPTpZTxz1wHT485djE7d_Gr0Vdn8",
            "https://drive.google.com/uc?export=view&id=13WQ4NCrJqxNg1k-1EaeELdQx5QTGq_lS",
            "https://drive.google.com/uc?export=view&id=1Qt_KU9NVao6C2v-hirCA_kOEY-GRgdkC",
            "https://drive.google.com/uc?export=view&id=1DSsbmyvuRdILHvrMzdsCs0A2XLqiMS5N",
            "https://drive.google.com/uc?export=view&id=1fT0y8mOWfzTZOceNVWjfq-6qCmQxTrfg",
            "https://drive.google.com/uc?export=view&id=1H6TDK0Fw7Htp3_F6vk6Jj9xL7_WaxwLZ",
            "https://drive.google.com/uc?export=view&id=1irHI27lpQ-CRCSAz5y4AgRlYAyKjoTi3",
            "https://drive.google.com/uc?export=view&id=1-hc7QqvYLD2bBaktmqJ5XYTuEDoHpT3D",
            "https://drive.google.com/uc?export=view&id=1sTQtwszdcy-LYAQlttqFqRAQu4FiKULl",

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
                "kesan": "Nama yang ada disetiap angkatan.",  
                "pesan": "Semangat buat menjadi kadepnya bang!!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya cantik banget dan lucu",  
                "pesan": "semangat terus kuliahnya kakak !!!, kelulusaan sudaah didepan mata kak semangat!!!"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Orangnya cerita banget kaya energinya ga pernah habis",  
                "pesan": "Terus ceria ya kak dan aku suka dengerin cerita kakak"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Keren banget bang waktu main di damaskus.",  
                "pesan": "Semoga terus membara semangatnya"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "kakanya lucu dan cantik banget suka ngeliatnya.",  
                "pesan": "Semangat terus kak, jangan sering-sering stalker takutttt"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "orangnya lucu banget apa lagi waktu dia manggil aku hey polkadot karna baju aku.",  
                "pesan": "tetep ceria ya kak"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal": "kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya mirip banget sama temen aku dari ujung rambut sampe ujung kaki.",  
                "pesan": "jangan terlalu di city city kan ya banggggg"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "kakaknya cantik dan cute.",  
                "pesan": "Semangat kuliahnya mengejar sampai ujung dunia"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpro Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "nama abang mirip banget sama abang aku yang nyebelin",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "masak",
                "sosmed": "@christiani8872",
                "kesan": "suka banget ngeliat kakaknya waktu senyum",  
                "pesan": "HIDUP ANAK ACARAAAA KAKKK SEMANGAT TERUSSS !!!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "nama kita sama bang cuman kurang huruf a aja",  
                "pesan": "semangat terus kuliahnya banggg !!!"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kakaknya cute ",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kakak asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak, walau anak rantau !!!"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara ",
                "alamat": "airan",
                "hobbi": "nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakak lucu dan cute bangettt",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Bang harvinsyah orangnya lucu banget dan unik",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Kakaknya sejuk banget ketika ngeliat mukanya masyallah",  
                "pesan": "semangat terus kuliahnya kakak !!!, terbang setinggi mungkin"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BT2ZKdb7iiP_w2zJtHC5ikdy5Wc6Rg5b",
            "https://drive.google.com/uc?export=view&id=1AZ5_QUJDvk6ZT4wWWA5RPdXS6UMSJHOd",
            "https://drive.google.com/uc?export=view&id=1e6EFAPDey5JILjdcfGBNgI8joirlvV1r",
            "https://drive.google.com/uc?export=view&id=1wIPWNQuOB1-MQYOTZzi29IsCe_YoYQ-7",
            "https://drive.google.com/uc?export=view&id=1wVfn81q09K7nQ-0GotGdVqL3kH6JKNKe",
            "https://drive.google.com/uc?export=view&id=1dcSlfvmcIzdhm7f5Tuf0PW2TAPgy5caW",
            "https://drive.google.com/uc?export=view&id=1BxA47QFbubRUeIRxVlUqtcU42Poz4zPR",
            "https://drive.google.com/uc?export=view&id=13aFQzJMW3TVznknHGnQBjuePuHoJuLWw",
            "https://drive.google.com/uc?export=view&id=1PbjGQ1DxDtuOK5x0Kr8Gz5fFzmgkhtaW",
            "https://drive.google.com/uc?export=view&id=1xB1-abMGc6dO_Uq19nO1OlbLWQwzi2zp",
            "https://drive.google.com/uc?export=view&id=18RBGXCqqIYgcOiNfXE4wfB2TFDV1AmMr",
            "https://drive.google.com/uc?export=view&id=1rl6Ttw8_qOw4wmj6uv5aGZ2-n13EvHLn",
            "https://drive.google.com/uc?export=view&id=1pPqg3-H_DY6KpNNMKOXG5GqvvfYjuMVK",
            "https://drive.google.com/uc?export=view&id=186K4K5fjSTGbESMZEsL1mnd3P7DbGQqB",
            "https://drive.google.com/uc?export=view&id=1C02Ot-V3dm_XliIZDnIDu6ilMYIKqEIt",
            "https://drive.google.com/uc?export=view&id=1nUzTVIT7m2RIruIzwbHpYkhcwyEst5t5",
            "https://drive.google.com/uc?export=view&id=1x2kee3SEzSarPAUng_UPlHqb3jCrjF5u",

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
                "kesan": "Kak arienta ternyata baikkk, walau awalnya sedikit serem",  
                "pesan": "Makasih banyak ya kak, udah jadi salah satu orang dibalik CEO HMSD yang bikin aku berkembang."# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany baikkk, tegas jugaaa apalagi waktu dilapangan",  
                "pesan": "Semangat terus ya kakaaaa semester ini, semoga lancar2 kuliahnya sampai lulus"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel tegas tapi saya rasa bang nobel jadi kaya bapak dari datavora",  
                "pesan": "Makasih banyak atas pelajaran yang telah diberikan"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal": "Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi orang yang tegas juga",  
                "pesan": "Terimakasih atas hal yang di berikan selama rangkaian"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal": "Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang ayake orang yang perhatian apalagi kalo ada yang sakit gercep banget",  
                "pesan": "Terimakasih atas perhatian yang diberikan"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Orangnya tegas banget",  
                "pesan": "Terimakasih telah membentuk mental saya semakin berani selagi tidak melakukan kesalahan"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal": "dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Keren banget apalagi waktu di lapangan, tegas dan jadi contoh buat berani dalam hal apapun",  
                "pesan": "terimakasih atass pelajaran yang di berikan"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Keren banget bang apalagi waktu day-4",  
                "pesan":"Terimakasih atas hal yang di berikan selama rangkaian, dan membuat saya berani untuk bicara di day-4"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                 "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "orangnya baik, suka banget liat kak putri waktu senyum manis bangett",  
                "pesan": "Terimakasih atas banyak hal, semangat kuliah kakk"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@andra.lhm",
                "kesan": "kakaaa cantikbanget aku suka ngeliatnya",  
                "pesan": "Terus senyum kak biar makin cantik, semangat kulahnya!!!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Keren sihhh apalagi waktu cerita cerita di wawancara",  
                "pesan": "Tetap semangat untuk kuliahnya bang"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "kakanya cantik dan cute",  
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "kakanya keren  dan cantik",  
                "pesan": "Tetap ceria dan semangat kuliah"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "keren banget bang",  
                "pesan":"semangat kuliahnya bang!!!"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                 "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "kakanya cantik dan cute",  
                "pesan":"terus ceria dan semangat kuliahnya"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "abangnya lucu gemasdan baik hati",  
                "pesan":"semangat kuliahnya bang dan terbang setinggi mungkin"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                 "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "kakaknya cantik banget suka ngeliatnya",  
                "pesan":"semangat kuliahnya kak,dan terus senyum karna buat happy orang lain"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

elif menu == "Departemen Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Axt58DPBwBqWrKLRH2ip_VrSwyt3gToG",
            "https://drive.google.com/uc?export=view&id=1Bd0-KNMVc0E67pYojPbKjTDdI82ZbTMr",#helmy
            "https://drive.google.com/uc?export=view&id=1BNHQiTTsgEPWh13WcIi8QA2XuLEjMNTk",
            "https://drive.google.com/uc?export=view&id=1Bb2FvMIY4Mf_ewlc8m8DFgcn3uwhHpP7",
            "https://drive.google.com/uc?export=view&id=1BtqUtJMFo4PrLwpDka-rusC5MBZqv4Cn",
            "https://drive.google.com/uc?export=view&id=1BQs5wUYsyHESkLDHt0riiXO1QG48xgfb",
            "https://drive.google.com/uc?export=view&id=1AqhkecRf9DqnbYZsxGPXoi4sodMGPoo2",
            "https://drive.google.com/uc?export=view&id=1Bs87z9WEhwsHyiiZw7Il3IVxx3WB0xzl",
            "https://drive.google.com/uc?export=view&id=1BFo66H-T2610YoULXXJ-viNcF-2TDogX",
            "https://drive.google.com/uc?export=view&id=1BbwBRwyqPCEXfmpwdW4Mk_8EGMwV74jY",
           

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
                "kesan": "Kak azizah orangnya seru bangett",  
                "pesan": "Makasih kak atas penjelasan materi tentang Kesenatoran, Semangat kuliahnya kak!!."# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "orangnya baik dan lucu banget ketika mau foto harus pake gaya handalan",  
                "pesan": "Semangat kuliahnya bang!! terbang setinggi mungkin"# 1
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Nemenin Wielman MC",
                "sosmed": "@barus.fernando",
                "kesan": "Bang fernando keren banget, hobinya sangat menyenangkan sepertinyaa",  
                "pesan": "Semangat buat selalu nemenin bang wielman nge-MC"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru ",
                "hobbi": "Baca",
                "sosmed": "@sciia__",
                "kesan": "kaa suci orangnya asik banget omgggg, keren deh",  
                "pesan": "Semangat terus kaka kuliahnya, dan selalu jadi MC ya kak karna asik banget bawainnya"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "jadi MC",
                "sosmed": "@wielhawn",
                "kesan": "Terpukau sama nada MC yang nge-MC banget keren sihhh bang omggg",  
                "pesan": "Jangan sampai suara emasnya hilang bang!!!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "main hp",
                "sosmed": "@lia.h_264",
                "kesan": "Aku suka banget ngeliat kakak pas bawain materi",  
                "pesan": "Semangat kuliahnya kak!! terbang setinggi mungkin"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Mentor bayesmup yang sering ketawa, dan identik dengan bunga mataharinya",  
                "pesan": "Semangat buat jadi mentornya kakkk, dan tetap ceriaaa"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "jadi sekjen",
                "sosmed": "@hazelhandhaka",
                "kesan": "keren banget waktu jadi ketuplak",  
                "pesan": "Semangat kuliahnya bang!!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                 "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya cute, cantik",  
                "pesan": "semoga hal-hal baik akan selalu datang ke kak nadya"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani ",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang ",
                "alamat": "Jl. Lapas",
                "hobbi": "nonton film,musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "kakanya humble, cantik dan senyumnya manis",  
                "pesan": "semangat kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19bd1LgaTN2qxlP0WnPFo_ebeo3Nu38f3",
            "https://drive.google.com/uc?export=view&id=1y-peb_TJdsz6917amHsvtp8i3iiIKAty",
            "https://drive.google.com/uc?export=view&id=1fiYcN-ZAzAWrvJh6FNUHR0s355mL0Lrh",
            "https://drive.google.com/uc?export=view&id=1KXNLI8AE21p_7nbOdlax1TSHrOyqThI_",#Fathya
            "https://drive.google.com/uc?export=view&id=11eSDc0OjUecwl4kck7HcLxa4uBECWXCe",
            "https://drive.google.com/uc?export=view&id=1Qf8jg-0O3toujQgrjhsLZ3UAm7r_yaJL",
            "https://drive.google.com/uc?export=view&id=15wTEsKtgOB8Nc1An6b4u0zL3876gvkE6",
            "https://drive.google.com/uc?export=view&id=1VB_R7gO_NaUXcwV2R3N9mJ2lV2kGzemH",
            "https://drive.google.com/uc?export=view&id=13ULS8ybLpsbpWNjJOysfNWwecgB-q-u_",
            "https://drive.google.com/uc?export=view&id=17lureBAjTM2sl54hYdOEGwyijTClDCbG",
            "https://drive.google.com/uc?export=view&id=11GwtotnBRIxLVgCtdjRz6jPkdEMl13uQ",
            "https://drive.google.com/uc?export=view&id=1tVr4SMkizf6f_5AXZrj1UZY3HjPtGoiU",
            "https://drive.google.com/uc?export=view&id=1949rdU9sLaqKizzLUuyE5Q36tdlHrDYJ",
            "https://drive.google.com/uc?export=view&id=1co6csbx1qFpsBYsAavi0Pr_zObj63_bp",
            "https://drive.google.com/uc?export=view&id=1REFa_hxUU4ijM98NIlMwlKQIe_LpUSGL",
            "https://drive.google.com/uc?export=view&id=1tt5w89L9h_tylmoacW8EqpxFFpXAjaxI",
            "https://drive.google.com/uc?export=view&id=1kLNbjiI92PwtGtajOvThAVmeRYelmIKK",
            "https://drive.google.com/uc?export=view&id=1nFZlaY2sgNDdmjbh0QBG3rj1HJFjONmR",
            "https://drive.google.com/uc?export=view&id=1WZE4Z9QV_mechyWCtsor_rdnHIHbr14o",
            "https://drive.google.com/uc?export=view&id=1pRURCQpkZyfAj9dTsGzo0LwVYWB9-uyV",
            "https://drive.google.com/uc?export=view&id=1-Tx_pdt310Cwye_6SkN6tBLd3j0pEuwg",
            "https://drive.google.com/uc?export=view&id=1ZAyWf_Ex6l6dAX9onQLlcfEEuX33W-rd",

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
                "kesan": "orangnya seruuu banget apa lagi kalo di ajakin gibahh omgg",  
                "pesan": "cerita yang waktu itu belom kelar bang, esok kalo ketemu lanjutkan ceritanya"# 1
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
                "pesan": "Terima kasih banyak ya, Kak, sudah luar biasa perhatian ke Tensor selama ini. Aku benar-benar bersyukur Kakak selalu meluangkan waktu dan mau mendengarkan semua cerita serta keluh kesahku tanpa pernah menghakimi. Semua saran terbaik yang Kakak berikan sangat berarti dan membantu aku melewati masa-masa sulit. Sebenarnya ada banyak sekali hal baik dan rasa terima kasih yang ingin aku sampaikan, tapi jujur semua itu terlalu berharga sampai tidak bisa kuungkapkan lagi lewat kata-kata. Terima kasih sudah menjadi kakak tingkat sekaligus pendengar terbaikku, Kak."
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
            "https://drive.google.com/uc?export=view&id=1P50SuWoPa77U_4InqSVgmn4U4ef35IFr",
            "https://drive.google.com/uc?export=view&id=1LR2TcFYvBsbjSyWKBS9sAct-AgPE7HzB",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#fadil prasetyo
            "https://drive.google.com/uc?export=view&id=1cWoZfqlPhQeXSOTWBYuJICkMuIlYQN0X",
            "https://drive.google.com/uc?export=view&id=1NlUlxveC8NUpZv_h9h4PGR3dxjLkFfHo",#ni made 
            "https://drive.google.com/uc?export=view&id=1Uybt_WoT2LegHmtUF_pqkhJPifoW0c3I",
            "https://drive.google.com/uc?export=view&id=1aEZjyzaJqLLXvl-7AxVxerJzNgr-cZu7",
            "https://drive.google.com/uc?export=view&id=12XLrFQqrppFEB5JP3kMaGAyPIqRVOGpo",#yulia
            "https://drive.google.com/uc?export=view&id=1Lvj5o5FKmS8QWm967Smrz_xkfBjoPIyZ",
            "https://drive.google.com/uc?export=view&id=1I4zTQZPmgy54v0UPkPytw3qpmvagtaNt",
            "https://drive.google.com/uc?export=view&id=1-dFUdWNxdY5Y9oeq2SC4QVDWqC4BbtBm",
            "https://drive.google.com/uc?export=view&id=1OPWK9aqLk3tuuF1e-TS2zzOXy5w3GEQ0",
            "https://drive.google.com/uc?export=view&id=1BDkW-GlvhrInYVd6RK9HRjyGHKItKZ-p",
            "https://drive.google.com/uc?export=view&id=1CML0YKsp58sNqP_TdkO8WKJjDV0vJGTd",#sherena
            "https://drive.google.com/uc?export=view&id=1vxJW2uZ1KhB_foAbydtmlYiWtP0abGFg",
            "https://drive.google.com/uc?export=view&id=1F5VMYOHO0D43ZeMtj48gjxZDBI6YR37d",#Faiza
            "https://drive.google.com/uc?export=view&id=1Va3n82JtOkf1Mf8HA1DMJExYzShF46i8",
            "https://drive.google.com/uc?export=view&id=13MhGn55TbkghdFiWIkWk5fFfgDfSFqIU",
            "https://drive.google.com/uc?export=view&id=1NxRXcKR1DTT-oehOidrGNSS8fbBKVuI9",
            "https://drive.google.com/uc?export=view&id=1Az3fleD8431lg1AsMft80BujQJpyhvZL",#melva
            "https://drive.google.com/uc?export=view&id=1l9imldkR1Sdqbp1DnzPukgKOfNnxIvlD",
            "https://drive.google.com/uc?export=view&id=1sdEuA36IQfr8rdaHmz7mQCj2pxUUa2Qh",

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
                "kesan": "keren banget ketika liat prestasi bang fabio",  
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
                "kesan": "kak tanty orangnya lucu, heboh, ceria banget dan senyumnya manis",  
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
                "kesan": "bang manuel orangnya baik dan humble banget",  
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
                "kesan": "kaka viola orangnya baik hati dan cantik banget",  
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
                "kesan": "kakaknya baik dan ramah",  
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
                "kesan": "kakaknya cantik, baik dan ramah",  
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
                "kesan": "kakaknya cantik, baik dan ramah",  
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
                "kesan": "bang akeyla orangnya baik dan ramah",
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
                "kesan": "kak elsa baik dan keren banget liat di organisasi, terpesonaaa",  
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
                "kesan": "kak fadya ternyata dari SMA yang sama dan terimakasih atas bantuan yang diberikan, baik banget",  
                "pesan": "Yuk bisa yuk, Kak! Semester 5 ini emang lagi seru-serunya. Tetap konsisten dan jangan kasih kendor kuliahnya!"# 1
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "kakaknya cantik, baik dan ramah",  
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
                "kesan": "abang alsi orangnya ramah, baik, dan  humoris",  
                "pesan": "Selamat melanjutkan aktivitas kuliah! Semoga IPK semester ini memuaskan dan sesuai harapan.."# 1
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal":"Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "kakaknya cantik, baik dan ramah",  
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
                "kesan": "bang razin keren banget waktu ngejelasin materi wwc tentang mikfes",  
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
                "kesan": "kakaknya cantik, baik dan ramah",  
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
                "kesan": "baru ketemu abang nim pas wwc",  
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
                "kesan": "mentor yang keren, baik, dan lucu",  
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
                "kesan": "bang kaleb orangnya baik dan keren banget dengan prestasinya",  
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
                "kesan": "kakaknya cantik, baik dan ramah",  
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
                "kesan": "bang syafiq keren, baik",  
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
                "kesan": "bang henry orangnya tegas dan baik",  
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14fLnuYH8UV1yUQaHR_0WhE85f5cfbtTS",
            "https://drive.google.com/uc?export=view&id=1xSDaRvVGQXGtKegf27YNLgkZ3BULxzF9",
            "https://drive.google.com/uc?export=view&id=1Sem9p6CpKZAbL_4cDJGS3iQ96i1HRrpa",
            "https://drive.google.com/uc?export=view&id=1yhNHMQpn-LrJKvNLkKt93a8yvafuGajj",
            "https://drive.google.com/uc?export=view&id=13UV9dDFp8Y3OBwv89VspcPMeemtNlycW",
            "https://drive.google.com/uc?export=view&id=1AZrDa18qNgPrzt_rjofqqfPIgmvJIMGD",
            "https://drive.google.com/uc?export=view&id=1xctL5PURnSrYhnSubdpai0hzv9n9ey4a",
            "https://drive.google.com/uc?export=view&id=17CUyTJWLszYFRDqrEE1b3G5beFO7rXeV",
            "https://drive.google.com/uc?export=view&id=14SU-F0EchKLnsebysBAh5oPy8AQSvgdB",
            "https://drive.google.com/uc?export=view&id=1Oqs1w0bfTwMkaf_u-FZjzfsndwjJ-8T8",
            "https://drive.google.com/uc?export=view&id=1ALVl0SWVkBpp3ML3_MGfr1dwfAQ5AbJU",#anggun
            "https://drive.google.com/uc?export=view&id=1baVtisX5dc-xOe-ShnDtB_tfUVGWYz2G",


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
                "kesan": "bang ihsan orangnya baik dan humoris",  
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
                "kesan": "kakaknya cantik, baik,humoris dan ramah",  
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
                "kesan": "kakaknya cantik, baik dan ramah",  
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
                "kesan": "bang hasan orangnya baik",  
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
                "kesan": "kakaknya cantik, baik dan ramah",  
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
                "kesan": "bang iqbal orangnya ramah, dan humoris",  
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "talljtine_",
                "kesan": "kakaknya cantik, baik dan ramah",  
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
                "kesan": "kakaknya cantik, baik dan ramah",  
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
                "kesan": "bang pome orangnya seru banget, baik dan ramahh banget",  
                "pesan": "Selamat melanjutkan aktivitas kuliah! Semoga IPK semester ini memuaskan dan sesuai harapan.."# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "bang afdhal hobinya sangat seru buat healing, orangnya baik dan ramah",  
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
            "https://drive.google.com/uc?export=view&id=1qG9QfmutWZIpSHGsyl5Hd6BwH5diQA6L",
            "https://drive.google.com/uc?export=view&id=1psWbQ4sTRMulaMqYio0SEiRrr3AVgkGw",
            "https://drive.google.com/uc?export=view&id=1T734kYH-eLCjSsSTx_0XgjKAnAZaBSfA",
            "https://drive.google.com/uc?export=view&id=1mkhwtZ9zRfNckyaP_0LDcr6nxNukBg_A",
            "https://drive.google.com/uc?export=view&id=15cx7CFbbyJ3pyxUMV65F5kPAsBBtcGU1",
            "https://drive.google.com/uc?export=view&id=1hb29SfwZp7PxrnqUTlUsIXUCvJYBRyKs",
            "https://drive.google.com/uc?export=view&id=1Vxo0RG0PSFB-9bTrwU8VuI9FgiY77T5H",
            "https://drive.google.com/uc?export=view&id=1ird1dU6Da2mgrEXTEZmTz7m89RXAi0Dn",
            "https://drive.google.com/uc?export=view&id=1Jo2Sbe3xc150YcYDFwgmg5NUKVUHhVH8",#alya
            "https://drive.google.com/uc?export=view&id=1fimdE2nQrusEPPWkMHzE24UPo26G1GUU",
            "https://drive.google.com/uc?export=view&id=1Z-xy16RQOCnwQsxFCE3X1Yn0V8I2xjzs",
            "https://drive.google.com/uc?export=view&id=1QbnDKRqTSZX_umhsLvGrlNeqrMRz8Wo_",
            "https://drive.google.com/uc?export=view&id=1j4piMZaRYxJtJ5cCtwVQrjxiLak5d4SF",
            "https://drive.google.com/uc?export=view&id=1CpUbSAR0_DHqFYrmZh1aCqDhjurWVpDs",
            "https://drive.google.com/uc?export=view&id=1kvRv2HV15KS7eaTj_jSALQeYDjAVWtLj",
            "https://drive.google.com/uc?export=view&id=1ZPpr9l_ivx99iDYgr-1upCayYJQ7Bfwx",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#shafa
            "https://drive.google.com/uc?export=view&id=1EfXP25mLhdh1-b5ZIT4ONJz6tjQ0XUnN",

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
                "kesan": "kakaknya cantik, baik,keren banget dan ramah",  
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
                "kesan": "kakak donna tutor lmd yang keren banget, penjelasannya mudah dipahami",  
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
                "kesan": "bang labo orangnya baik, ramah dan keren banget ngeliatnya di medkraf",  
                "pesan": "Satu langkah besar lagi menuju wisuda, bang. Lelahnya cuma sementara, bangganya seumur hidup. Semangat!"# 1
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
                "kesan": "bang razan orangnnya ramah dan lucu",  
                "pesan": "Yuk bisa yuk, bang! Semester 5 ini emang lagi seru-serunya. Tetap konsisten dan jangan kasih kendor kuliahnya!"# 1
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
                "kesan": "kakaknya cantik, baik dan ramah, suka banget ngeliat vibesnyaa",  
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
                "kesan": "bang daffa orangnya baik, humoris, dan ramah",  
                "pesan": "Yuk bisa yuk, bang! Semester 5 ini emang lagi seru-serunya. Tetap konsisten dan jangan kasih kendor kuliahnya!"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "bang edsel orangnya baik dan ramah",  
                "pesan": "Yuk bisa yuk, bang! Semester 5 ini emang lagi seru-serunya. Tetap konsisten dan jangan kasih kendor kuliahnya!"# 1
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



