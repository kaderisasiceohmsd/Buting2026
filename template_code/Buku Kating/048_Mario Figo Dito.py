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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Jl3TRqARa03G7sfnjmMp5Ic2WUMTrmXI",
            "https://drive.google.com/uc?export=view&id=10JdGKbS-sy0Q-WODYIiq-RHdxOgIoQdA",
            "https://drive.google.com/uc?export=view&id=1Y9gqqft8Q-1O2XTpIn1SLSwKE0Ww6Cza",
            "https://drive.google.com/uc?export=view&id=1_DhgtFl73HGdnTt_cFRGie75GBwmfEGk",
            "https://drive.google.com/uc?export=view&id=1CAfB_4CI6SRxThyXOIgRXsY7J7GU9-8m",
            "https://drive.google.com/uc?export=view&id=1xSa9_YEbEIISrjwqyd1SijZNJW7N81ph"
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
                "kesan": "Bang Fajar humble, baik, dan punya auranya sendiri",
                "pesan": "Sukses terus kuliahnya dan lancar segalanya bang"
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil santai, ramah, dan mudah dipahami",
                "pesan": "Sehat selalu dan makin sukses ke depannya bang"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi baik banget penjelasannya bikin pengen masuk sekre",
                "pesan": "Semoga urusannya selalu dipermudah dan berbuat baik kak"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Tenang dan kelihatan menikmati banget di sekre",
                "pesan": "Semangat terus bang semoga selalu sehat dan sukses"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa ramah dan asik diajak ngobrol",
                "pesan": "Semoga selalu diberi kesehatan dan kelancaran ya kak"
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Orangnya ceria, aktif, dan mudah dimengerti",
                "pesan": "Lancar terus buat tugas dan amanahnya ya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lC3FWUt7p7CmmMCoGMACpHHNmyEMA7aS",
            "https://drive.google.com/uc?export=view&id=1jb5VY8k-pautrECcBiPxqhMvqmcluejD",
            "https://drive.google.com/uc?export=view&id=1GDcRO5vZrQg4sHzOJtyjihQpvISlc8IG",
            "https://drive.google.com/uc?export=view&id=1MTBV8RdtqTv2LYvtFocW6KUsgn2kdt8A",
            "https://drive.google.com/uc?export=view&id=1Y3RXg2UjBiYK2UFfOez1TFzzFRFC4zpD",
            "https://drive.google.com/uc?export=view&id=1H6uBb8MdRtVgd64vTAxQp-20PGVI9BGg",
            "https://drive.google.com/uc?export=view&id=1mv6MwjD8B-JTZcs2XENOAL6FTF-0_dnO",
            "https://drive.google.com/uc?export=view&id=1XUDGdVLBdlzS4SY0s4prXPZQlhLoaGYw",
            "https://drive.google.com/uc?export=view&id=1TfUx-1y0I5Apqs3U95EdHQbNIBMIDAft",
            "https://drive.google.com/uc?export=view&id=1c5BCtvvKOYLRNdkyNtRoH7ZEFV_ogV4L",
            "https://drive.google.com/uc?export=view&id=1h1GYlKkaRGsgxGLLDFV8w8AkO2Ya4UVY",
            "https://drive.google.com/uc?export=view&id=13SOqbRPnPykp29OWhxT687aPq-DdctGb",
            "https://drive.google.com/uc?export=view&id=1mTlzLtUFrCNyj9Y9fo5TBTOacV74TCcy"
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
                "kesan": "Bang Ridho random tapi to the point",
                "pesan": "Semoga sehat selalu dan diberi kemudahan dalam segala hal bang"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue seru dan ramah bangett",
                "pesan": "Sukses terus kuliahnya dan selalu sehat ya kak"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Asik banget dan bikin nyaman",
                "pesan": "Semangat kuliahnya bang semoga tugas lancar dan IPK aman"
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Auranya beda ini keliatan, tapi bang niko tetep santai dan humble",
                "pesan": "Lancar terus kuliahnya dan sehat selalu bang"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Orangnya ramah dan seru banget",
                "pesan": "Kuliahnya lancar terus ya kak"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro asik dan asikk",
                "pesan": "Semoga terhindar dari tugas dadakan dan hidupnyanya makin nikmat bang"
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak Nisa baik, ramah, dan terlihat punya rasa tanggung jawab yang tinggi",
                "pesan": "Semoga segala langkahnya dipermudah ya kak"
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Orangnya lembut, sopan, dan enak diajak ngobrol",
                "pesan": "Sehat selalu dan sukses terus kuliahnya kak"
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremia orangnya asik dan gampang diajak ngomong",
                "pesan": "Semoga selalu sehat dan lancar semua kegiatannya bang"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica murah senyum, baiik, dan asik",
                "pesan": "Semangat terus kuliahnya dan sukses selalu kak"
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jona suka bercanda dan random",
                "pesan": "Semangat terus kuliahnya bang"
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Sekar tegas tapi tetep perhatian",
                "pesan": "Sehat selalu dan lancar urusan  kak"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakak satu ini sangat friendly dan baik",
                "pesan": "Semangat terus kuliahnya dan sukses selalu ya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Vm3Nd6Tinyp6efLMmi9YsJ2NIajq8qyw",
            "https://drive.google.com/uc?export=view&id=1IvqFmpJKcLawOJNgZyj6w207YqopfcGI",
            "https://drive.google.com/uc?export=view&id=1fZAnwPHYQyH-claqtow-yvEE9lFJPqnN",
            "https://drive.google.com/uc?export=view&id=1Onr5OF0X_xVIsfiCnrke9oFHbuoAFmuo",
            "https://drive.google.com/uc?export=view&id=1M2CS-Hk_gxBi9EUI2NJL7hx54NJdPr8Q",
            "https://drive.google.com/uc?export=view&id=1Da46NCZ-oXjk4Vhhg20cX0vhfEHFHlCk",
            "https://drive.google.com/uc?export=view&id=1EFFBwUCDN1SCPzyy12LOXa6vbnRXf39Q",
            "https://drive.google.com/uc?export=view&id=1uac_LVx74QJp95Y2C4aH49U1CKd3CarK",
            "https://drive.google.com/uc?export=view&id=1LDjzg_DMC365CujWm0Hlc2_GsMi8_Xqi",
            "https://drive.google.com/uc?export=view&id=1RQ7LGKcKK4AxUWLN4vv9Iqf1vy909IJU",
            "https://drive.google.com/uc?export=view&id=1h3jNg8SzuYNlTC_TouOqGQTmT3ojO20M",
            "https://drive.google.com/uc?export=view&id=1zvaz2s0MyQ9nt-ljAU911qKW5Cuh02IY",
            "https://drive.google.com/uc?export=view&id=1l6PmSlTzRmf0YSB8YIcaRl6T1ELY_DyP",
            "https://drive.google.com/uc?export=view&id=10l0Je27RNMoLUijI4pWp21Qt0ufno2X4",
            "https://drive.google.com/uc?export=view&id=1GmBpG1o-HtgIHhk5OxyRfdDa7M02Ihc9"
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
                "kesan": "Bang Kevin lucu dan seru banget",
                "pesan": "Semangat terus kuliahnya dan sehat selalu bang"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kak Ferazka kocak dan hobi banget ngajak muncak",
                "pesan": "Semoga ada sehat dan semangat terus kak"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Bang Ali orangnya baik, pendiem, dan baik",
                "pesan": "Semangat terus buat kuliahnya ya bang"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kak Ayu asik dan gampang ngobrol sama siapa aja",
                "pesan": "Sukses dan semangat terus kuliahnya kak"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Dafa asik dan baik banget",
                "pesan": "Sehat selalu dan lancar kuliahnya bang"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kak Nazwa orangnya lembut dan selalu ramah",
                "pesan": "Semoga urusannya selalu dilancarkan ya kak"
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Bang Afdal kocak, seru, dan asikkk",
                "pesan": "Tetap semangat dan jaga kesehatan selalu bang"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak Juwita baik dan ramahhh",
                "pesan": "Semoga kuliah dan kegiatannya lancar terus kak"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang Ridwan asik dan seru",
                "pesan": "Semangat terus kuliahnya bang"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Bang Andra kocak, dan seru banget kalo becanda",
                "pesan": "Semangat kuliahnya dan lancar terus ya bang"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang Bryan orangnya ramah dan kalem",
                "pesan": "Sukses terus buat kuliahnya ya bang"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17 tahun",
                "asal":"Jati Asih",
                "alamat": "Korpri",
                "hobbi": "Nyawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Aktif abangnya dan seru saat ngobrol",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Indah sangat asik diajak ngobroldan baik",
                "pesan": "Lancar terus kuliahnya ya kak"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri ",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Asik dan lucu kakaknya",
                "pesan": "Semangat terus kuliahnya ya kak"
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Bang Rafka humble dan seru",
                "pesan": "Sehat selalu dan sukses buat kuliahnya bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13TYX3n6gfgWEVAhYtfR_RSXChAIV6GMG",
            "https://drive.google.com/uc?export=view&id=1jj19Xu38t4CImU0ORsXxpErmZyBZggoT",
            "https://drive.google.com/uc?export=view&id=1CeEy4gNHQyGV2FBtwvLhq-gECG5u0lGB",
            "https://drive.google.com/uc?export=view&id=1xJXrFYxahSb5WTxFOe_74ej_MaCcZ3Bb",
            "https://drive.google.com/uc?export=view&id=1yMNvCADGXoOLseH3jmOEsc0pai54PxCI",
            "https://drive.google.com/uc?export=view&id=1Ijlra46Fc0Ur-uz3TusMaWVz4rcWyn_a",
            "https://drive.google.com/uc?export=view&id=1Jx_9RdD5oK7dx-234jhBw3TybpT0Kqet",
            "https://drive.google.com/uc?export=view&id=1U0JT9IQ8JeY3rpQgEdKqsi94FPJu8gs1",
            "https://drive.google.com/uc?export=view&id=1vuB0sHxCnJgbz4AJjFXOR9rD2lcxCt0W",
            "https://drive.google.com/uc?export=view&id=1oLFAPBP89lhgwOgM6pvzb208w3ngNoE8",
            "https://drive.google.com/uc?export=view&id=1zeI4yFV9XiAeoygRvQQJP7x_fhnYqzbP",
            "https://drive.google.com/uc?export=view&id=1Jj51ZVmL-Jt4MaQrheqqYfzzRGHAUcq8",
            "https://drive.google.com/uc?export=view&id=1mEfGOdFMsnC-sGLA-9Gk-a6YLemdHmy0",
            "https://drive.google.com/uc?export=view&id=1DzIevEoLp5uvNNlbfbHMUYUwMVIE06gR",
            "https://drive.google.com/uc?export=view&id=16j0vqEwdaiHAUmKOfQSjiR-pI2D4TSJZ",
            "https://drive.google.com/uc?export=view&id=1aYAv0j_8_Pkqep6PDKx1cYbItnYl1rl3"
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
                "kesan": "Bang Haikal orangnya santai dan asik",
                "pesan": "Semoga segala urusannya selalu dipermudah bang"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma ramah, lucu, dan selalu ceria",
                "pesan": "Semoga selalu dikelilingi kebaikan ya kak"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna seru, baik hati, dan humblee",
                "pesan": "Semoga impian dan cita-citanya cepat terwujud kak"
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan keren dan keliatan mantap mantep banget damaskus",
                "pesan": "Semoga diberikan kesehatan dan kelancaran terus bang"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak Aisyah lucu dan baik dari dulu",
                "pesan": "Semoga langkah dan tujuan Kakak selalu lancar"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kak Cerine sangat humble, seru, dan baik hati",
                "pesan": "Semoga selalu dikelilingi orang-orang baik kak"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya keren, asik, dan baik",
                "pesan": "Sehat selalu dan lancar di setiap kegiatan bang"
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kak Najla baik banget dan sangat ramah disapa",
                "pesan": "Semoga apa yang diimpikan segera tercapai ya kak"
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"lampung selatan",
                "alamat": "korpri raya",
                "hobbi": "isengin harvin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "Bang Rozak santai dan murah senyum kalau ketemu",
                "pesan": "Semoga selalu didekatkan dengan hal-hal positif bang"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"riau",
                "alamat": "belwis",
                "hobbi": "masak",
                "sosmed": "@christiani8872",
                "kesan": "Kak Teresa lucu, baik, dan asik",
                "pesan": "Semoga target-targetnya segera terwujud ya kak"
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Bang Hanif asik dan seru kelihatannya",
                "pesan": "Semoga terus jadi yang terbaik di setiap langkah bang"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"sumbar",
                "alamat": "sukarame",
                "hobbi": "main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kak Audina sangat ramah, lucu, dan baik hati",
                "pesan": "Semoga senantiasa berada di lingkungan yang positif kak"
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kak Cika seru, lucu, dan baik banget",
                "pesan": "Semoga harapan dan rencananya segera tercapai kak"
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara ",
                "alamat": "airan",
                "hobbi": "nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kak Gustin ramah dan lucu",
                "pesan": "Semoga hari-harinya selalu dikelilingi kebaikan ya kak"
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Bang Harvin orangnya lembut dan baik banget",
                "pesan": "Semoga semua impiannya bisa terwujud secepatnya bang"
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "nginep di rumah kak yollanda",
                "sosmed": "@snasha._",
                "kesan": "Kak Sabina ramah banget dan enak diajak komunikasi",
                "pesan": "Semoga hal-hal baik selalu menyertai Kakak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EtM17goe2HHL04LkI8XrKiy9H-Wobfl-",
            "https://drive.google.com/uc?export=view&id=1g8lpc7bRe4vLHvZNXYn6dlNhKuqWO-Wk",
            "https://drive.google.com/uc?export=view&id=1wPXz8WeN-NMdhXSPQHmdvwyRPoQbEeJE",
            "https://drive.google.com/uc?export=view&id=1f1rX29ld7E66FD7-CBDswAT7-6erwCNd",
            "https://drive.google.com/uc?export=view&id=1f8P1QX-TwPcAojsV8W3breCtMYCyZ1KB",
            "https://drive.google.com/uc?export=view&id=1KbECDCCiFmBhiILtgy00dnEaLnBGL2bL",
            "https://drive.google.com/uc?export=view&id=1a6KlieOPJLYTLMvOXQzZaay0cML9SSaB",
            "https://drive.google.com/uc?export=view&id=14AMEQ2ReqiSrlJTkxjfPJEFYGyUPktox",
            "https://drive.google.com/uc?export=view&id=19ZnM3deOhNrPZp9Tf67gteVBLFa-BaZq",
            "https://drive.google.com/uc?export=view&id=1rJ2X70qAKI3Dkibf477sjzKLvqCUXsac",
            "https://drive.google.com/uc?export=view&id=1kMtq37xTjmunbnIUFOxe6vXofxL9Kci7",
            "https://drive.google.com/uc?export=view&id=1zj7FqC3-50fQzl5H-8_UVliIp5SJe9eY",
            "https://drive.google.com/uc?export=view&id=1yfF5VhdWtKiN_7y7Id7_LI65ZHIbV7GS",
            "https://drive.google.com/uc?export=view&id=1lbVIMOa-9da5ivrs0dnosRNPJYwNLYHb",
            "https://drive.google.com/uc?export=view&id=1oP01q7RKATO5p40R85bJYy1Ry373-SdS",
            "https://drive.google.com/uc?export=view&id=1o70JXDiPgFQrsxaJEn7Nyt9QZ5afx1t6",
            "https://drive.google.com/uc?export=view&id=1pRxV_pBKOXJsmX5A3WHhU1Q-0fgD7DRr"
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
                "kesan": "Kak Arienta ramah dan baik orangnya",
                "pesan": "Semoga cita-cita Kakak cepat terwujud ya"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany humble dan sangat baik hati",
                "pesan": "Semoga tujuannya cepat tercapai dan terus sehat"
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel keliatan tegas tapi tetep keren dan baik baik",
                "pesan": "Semoga selalu diberi kelancaran di segala sesuatu bang"
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi keren, to the point, dan baik",
                "pesan": "Semoga semua harapan abang cepat terkabul dan tetap sehat bang"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang Ayake humble banget, asik dan keren lah",
                "pesan": "Sehat selalu dan dipermudah segala urusannya bang"
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar tegas dan kelihatan keren banget pokoknya",
                "pesan": "Semoga selalu diberikan kesehatan dan kelancaran bang"
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Euodia seru, tegas, tapi tetep ramah dan baik",
                "pesan": "Semoga selalu dipertemukan dengan hal hal baik kak"
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal keren, misterius dan baik",
                "pesan": "Semoga sukses menggapai hal yang diimpikan bang"
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri ramah, humble, profesional dan baik banget",
                "pesan": "Semoga sehat selalu dan sukses selalu ya kak"
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@queentanaabila",
                "kesan": "Kak Queenta seru, ramah, dan baik",
                "pesan": "Semoga selalu lancar menggapai keinginannya kak"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman asik, baik, dan keren",
                "pesan": "Semoga selalu bertemu hal-hal baik bang"
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel humble dan baik banget orangnya",
                "pesan": "Semoga semua harapan Kakak bisa terwujud"
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah ramah dan seru diajak bicaranya",
                "pesan": "Semoga dikelilingi kebahagiaan dan kebaikan terus kak"
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jemar keliatan keren apalagi waktu damaskus jadi capo",
                "pesan": "Semoga impian-impian Abang bisa tercapai semuanya"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila ramah, baik, dan kakak nim ku",
                "pesan": "Semoga hal yang diinginkan bisa segera terwujud"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Bang Rafli humble, ramah, dan baik ke siapapun",
                "pesan": "Semoga sukses menggapai target-targetnya bang"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salavi seru, ramah, dan seru",
                "pesan": "Semoga selalu dipermudah dan dilindungi kebaikan ya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19nBw0l0j8MPBEn_hsfdoRBs7rVS71pfI",
            "https://drive.google.com/uc?export=view&id=12SY6nQe9msP6Fl1T5vklC_W4wUOoQLBR",
            "https://drive.google.com/uc?export=view&id=1a-_pMqKddzdKRM5Ao93xmMbdMz80kwFK",
            "https://drive.google.com/uc?export=view&id=18Lg4dGWduYlDt1u2akl-tAEQzbJe-DN8",
            "https://drive.google.com/uc?export=view&id=1OZZIUizPcIt3H0StjZ7Aqki4qdPo5gEn",
            "https://drive.google.com/uc?export=view&id=189YDwjpDabWXjYoez1JEa5kW-4ViRyPX",
            "https://drive.google.com/uc?export=view&id=1IwyArfd9Owk0v8DwyMw1Brcd_6bFXH9u",
            "https://drive.google.com/uc?export=view&id=1YxHQhAb3FC7Krz_D_djS8WztVCHe-fKD",
            "https://drive.google.com/uc?export=view&id=1hJa7uwFQgF4c0j3Ko3iWJ73Garvpviwr",
            "https://drive.google.com/uc?export=view&id=1_2jNCbe8TGQHQaQ6xNbEtXJzY1ncE-L1"
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
                "kesan": "Kak Fathinah seru dan baik banget pas ngobrol",
                "pesan": "Semangat terus menjalankan tugas Senat KM-ITERA ya kak"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak Nadya nadanya lembut, baik, dan seru",
                "pesan": "Semoga dipermudah segala urusan dan sehat selalu kak"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kak Dwi seru dan baik banget orangnya",
                "pesan": "Semoga harapan yang diinginkan bisa cepat tercapai ya kak"
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen Kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Bang Helmy lucu dan asikk",
                "pesan": "Lancar terus di setiap urusannya ya bang"
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tanggerang Kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Bang Nando orangnya humble dan baik banget diajak ngomong",
                "pesan": "Semoga selalu sehat dan lancar urusannya bang"
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Kota Baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia__",
                "kesan": "Kak Suci seru dan aktif banget",
                "pesan": "Semangat terus dan semoga lancar jalannya kak"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Bang Wielman humble parah dan sangat ramah",
                "pesan": "Semoga diberi kemudahan di setiap situasi bang"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jaarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Hana murah senyum dan baik banget",
                "pesan": "Semangat terus kak semoga segala usahanya dipermudah"
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "18",
                "asal":"lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kak Aqila aktif banget, seru, dan kocak",
                "pesan": "Tetap semangat dan lancar jalannya ya kak"
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "Giring Ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Bang Hazel fashionable dan keren banget",
                "pesan": "Semoga sehat selalu bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cgDT6xE10cCIOvRXxZ1384zAhyEoHrjI",
            "https://drive.google.com/uc?export=view&id=1cnBb62R_dd6D0Pxjmap-xrl0oIP1hl_f",
            "https://drive.google.com/uc?export=view&id=15eshsJMrAPJIzAaWGgA-mFSNHKuTuocr",
            "https://drive.google.com/uc?export=view&id=1sSYmw7KyQOnwZxtSMJ7M3rswjgJhbGSN",
            "https://drive.google.com/uc?export=view&id=1RJIoSJAHkCKUS6-GMN6kSjultA5QbAI9",
            "https://drive.google.com/uc?export=view&id=1kIIKtNx5QaC0uEHIgBNvEvtRVUzLxqKJ",
            "https://drive.google.com/uc?export=view&id=1UIHHl4IUiI7b1h3hUR3CcSaeIfkZJrCB",
            "https://drive.google.com/uc?export=view&id=17czWEBFYey_0VuLfkF2sn1H2euFWWOkQ",
            "https://drive.google.com/uc?export=view&id=1VkC3CPkNqZPRMwc2da8QQ3HfAfYvDPF1",
            "https://drive.google.com/uc?export=view&id=1aeIyGpP9Gt6GEmStQfHE44kS7D9-uhI1",
            "https://drive.google.com/uc?export=view&id=10OxmpkGXsFaj2XCA1_Z-rz--rMRJ2YM9",
            "https://drive.google.com/uc?export=view&id=1PgAqJQmAAsQOFCGg4kDSjVmEV3BGSBuZ",
            "https://drive.google.com/uc?export=view&id=1txUISIXKiX5so0zudjzXDJwbRJNQNV1X",
            "https://drive.google.com/uc?export=view&id=1ztXllb3XHH0zwWpUcB_tmCNEeaYBz2XU",
            "https://drive.google.com/uc?export=view&id=1o9NAljysi3LKp7wsUovDQXGBhpwTBQ15",
            "https://drive.google.com/uc?export=view&id=1TUHjyRHkYI9WYPIDH5Ic_RCTF6Yp3JnY",
            "https://drive.google.com/uc?export=view&id=18x22K4jyid8uhxC-QOV4vjREt_dFVfYM",
            "https://drive.google.com/uc?export=view&id=18Lg4dGWduYlDt1u2akl-tAEQzbJe-DN8",
            "https://drive.google.com/uc?export=view&id=1Q8M-RJrR_cD4oC9IRGsTImUswzQseoIu",
            "https://drive.google.com/uc?export=view&id=1GIk-MIU5_jV2BNry9XcYLuE9Opv-FmO9",
            "https://drive.google.com/uc?export=view&id=1yHipkLZ_yAf0FTkQN1sMxTF2lRV_BqKm",
            "https://drive.google.com/uc?export=view&id=11E-vaoa77D8hZboNsFpx6uOFUa3zoL83"
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
                "kesan": "Kak Arini murah senyum dan baik orangnya",
                "pesan": "Semoga lancar dan sehat selalu dalam segala hal kak"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla humble dan baik",
                "pesan": "Semoga hal-hal baik selalu menyertai dan sukses terus kak"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "Bang Adit asik, ramai, dan bikin nyaman",
                "pesan": "Semoga impian Abang cepat tercapai dan sehat selalu"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya seru dan ramah diajak ngobrol",
                "pesan": "Semoga sehat selalu dan dilancarkan semua urusannya kak"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "-",
                "asal": "Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kak Tarisya baik banget",
                "pesan": "Semoga selalu dikelilingi hal baik dan lancar kumpulannya kak"
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kak Selma baik, ramah, dan asik",
                "pesan": "Sukses dan bahagia selalu dalam setiap hal ya kak"
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "sini",
                "alamat": "jauh pokoknya",
                "hobbi": "tidur",
                "sosmed": "@kshigf",
                "kesan": "Kak Shila gampang tersenyum dan friendly sama orang",
                "pesan": "Semoga apa yang dicita-citakan berjalan lancar kak"
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Bang Danil berprestasi banget, keren, dan tetep humble",
                "pesan": "Semangat selalu dan tambah sukses ke depannya bang"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Bang Vian kocak banget dan ramah banget",
                "pesan": "Semoga selalu diberi kebahagiaan dan sukses terus bang"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "((15≪1) & 31) ⊕ 10",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Bang Yazid baik dan asik banget",
                "pesan": "Semoga dipermudah segala langkahnya dan sehat selalu bang"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah ",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "tanyain sama yuder",
                "sosmed": "@jaldii._",
                "kesan": "Bang Zaldi lucu dan selalu bikin ketawa",
                "pesan": "Lancar urusannya dan sukses terus ya bang"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kak Saskia ramah dan gampang senyum",
                "pesan": "Semoga dilancarkan semua urusannya dan semangat terus kak"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak Mut tenang, sopan, dan pinter",
                "pesan": "Semangat terus berjuangnya dan sukses selalu kak"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang Ahmad orangnya berani bersuara dan punya kepedulian tinggi keren banget pokoknya",
                "pesan": "Semoga perjuangannya berdampak baik dan sukses selalu bang"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kak Indah kelihatannya pendiem tapi ternyata asik diajak bercanda",
                "pesan": "Sehat selalu dan semangat dalam menjalani kuliah kak"
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung ",
                "alamat": "Balam",
                "hobbi": "berlaku lucu dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Bang Bima asik dan humble banget",
                "pesan": "Semoga langkah-langkahnya dimudahkan terus ya bang"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus ",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Bang Bimo terlihat dewasa dan ramah",
                "pesan": "Semoga dilancarkan semua urusannya ya bang"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "21",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kak Adinda kelihatan tenang, ramah, dan murah senyum",
                "pesan": "Semoga dipermudah setiap urusan yang dijalani kak"
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kak Yollanda sangat aktif dan gampang bergaul",
                "pesan": "Semoga sehat selalu dan lancar urusannya kak"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kak Ipin ternyata perhatian, tulus, dan penyabar banget membimbing dan mengajar anak anaknya ini",
                "pesan": "Terima kasih banyak ya Kak, semoga selalu sehat dan bahagia"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Bang Alfaya ramah dan asikk",
                "pesan": "Semoga makin sukses dan berkembang terus bang"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kak Mei lucu, seru, dan ramah",
                "pesan": "Semoga sehat selalu dan sukses kuliahnya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1omCuyOT4oC7XDdHjqxvqrhCO5oWjeZ1t",
            "https://drive.google.com/uc?export=view&id=1gY02GV_kFnKM4UvKB9l81T2Zg4JVxWo7",
            "https://drive.google.com/uc?export=view&id=1RcuyO0knEj-zjt0hSxTJxk-SkEpfWT4H",
            "https://drive.google.com/uc?export=view&id=1uA-JDoAqNTf3Fi2mUIBlZm5MTn1-d3GS",
            "https://drive.google.com/uc?export=view&id=1g0I-BTpeHDKE-MZNU1LbcuTega2qJQAZ",
            "https://drive.google.com/uc?export=view&id=1Z8NA3t18CgPwsNrJ7BL3o6BdIks_1W3O",
            "https://drive.google.com/uc?export=view&id=1kdOqnKj4Cff7F32HqyA85YLgI90FRfiM",
            "https://drive.google.com/uc?export=view&id=1-IUk2_LnqV4kaHI8lMveDWPMBS0M4OAE",
            "https://drive.google.com/uc?export=view&id=1uiq8FOvQo_7hyE6R5A6CFMVPzBY7kHc2",
            "https://drive.google.com/uc?export=view&id=1Dx4gr9VX9SIh9aI8jDeuTE9tlA6fisKm",
            "https://drive.google.com/uc?export=view&id=1FeSrFD1u4E8u27xbI6jPzrCEMIswQ9Uk",
            "https://drive.google.com/uc?export=view&id=1Qa4PZZczHqI176PtlPlzswUMDYArq_Ak",
            "https://drive.google.com/uc?export=view&id=1eGzA-HgShCOl5tCeOldmIqlMLzmGzcCq",
            "https://drive.google.com/uc?export=view&id=1CVDU93mOm-PWUjKv3Bynp_a_fu7gH-U4",
            "https://drive.google.com/uc?export=view&id=1GXF_UKhzzplSQPv0w-kXHEpcldYPXryZ",
            "https://drive.google.com/uc?export=view&id=1kEC3Zlt_RhXEss8cDIOM4QLu28tk9244",
            "https://drive.google.com/uc?export=view&id=16vfWzUTxisab8ZEn--Y09HBxIoiiC7SO",
            "https://drive.google.com/uc?export=view&id=1S0E43Qf4fdryJLiotmpIcCNxpeuaU3NC",
            "https://drive.google.com/uc?export=view&id=1dsfowjXFmcAtQmLAd3Sq6D6nioCNsweM",
            "https://drive.google.com/uc?export=view&id=1QS3PSIkzDSRx0W_tyCPBLIPap9n5J7mS",
            "https://drive.google.com/uc?export=view&id=1gtieOtwGBU92zWzuPSalqbhWkwprbiSJ",
            "https://drive.google.com/uc?export=view&id=1w3DfI3cDv6kmEDfg2Hmpt1iPKIMGOaoQ"
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
                "kesan": "Bang Fabio pinter, asik diajak ngobrol, dan asik",
                "pesan": "Semoga terus bermanfaat dan sukses terus bang"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Nonton film",
                "sosmed": "@tvnty_",
                "kesan": "Kak Tanty ramah. baik bangettt, ceria, dan selalu bikin suasana heboh",
                "pesan": "Tetap jadi sosok yang ceria dan sehat selalu kak"
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Bang Fadil sangat baik, rendah hati, dan berprestasi",
                "pesan": "Semoga amal ibadahnya diterima dan diberikan tempat terbaik di sisi-Nya"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis ",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "Bang Manuel baik, to the point, dan seru",
                "pesan": "Lancar terus kuliahnya dan sukses selalu ya bang"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12",
                "asal": "Bali",
                "alamat": "nusa peninda",
                "hobbi": "menghayal",
                "sosmed": "@violaadrtr_",
                "kesan": "Kak Viola murah senyum, ramah, dan seru",
                "pesan": "Semoga harinya dikelilingi kebaikan terus ya kak"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Kak Risa humble, santun, dan asik",
                "pesan": "Semoga selalu diberikan kebahagiaan dan kelancaran kak"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "1244500078",
                "umur": "19",
                "asal": "kepulauan riau",
                "alamat": "teluk betung",
                "hobbi": "nonton khw",
                "sosmed": "@vunnycaa",
                "kesan": "Kak Vannisa kalem tapi pinter banget kelihatannya",
                "pesan": "Semoga sukses dan berkembang terus kuliahnya kak"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Kak Yulia tenang, baik hati, dan sangat ramah",
                "pesan": "Sehat dan dilancarkan selalu urusannya ya kak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@keyashafi_",
                "kesan": "Bang Keya kalem, ramah, dan pintar",
                "pesan": "Semoga ilmunya terus berguna dan makin sukses bang"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara ",
                "alamat": "Pemda",
                "hobbi": "Sibuk",
                "sosmed": "@_els.a",
                "kesan": "Kak Elsa aktif banget seru, dan hobi muncak",
                "pesan": "Semoga rasa lelahnya terbayar dengan hasil terbaik kak"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "airan",
                "hobbi": "mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kak Fadya ramah dan baik bangett",
                "pesan": "Semoga harinya seru dan lancar urusannya kak"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "Kak Lovi baik, aktif dan keren banget pas jadi MC",
                "pesan": "Public speaking-nya makin mantap terus ya kak"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "kalianda",
                "alamat": "kota baru",
                "hobbi": "main game, tidur",
                "sosmed": "@aluccy_",
                "kesan": "Bang Alsi pinter, kalem, tapi tetep santai menjadi prince of pika",
                "pesan": "Semoga selalu diberikan kemudahan dan kesehatan bang"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kak Sherena ramah, murah senyum dan lucu",
                "pesan": "Sehat selalu dan tetap jadi sosok yang baik kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Bang Razin kalem, ramah, dan baik",
                "pesan": "Sukses terus kuliahnya dan selalu sehat bang"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel ",
                "sosmed": "@faizaanjanii",
                "kesan": "Kak Faiza humble dan ramah banget pas disapa",
                "pesan": "Semoga dipermudah segala langkah kegiatannya ya kak"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Rajabasa Raya",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Bang Gathfan pendiam tapi kelihatan baik orangnya",
                "pesan": "Semoga selalu diberikan kelancaran dalam berproses bang"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur ",
                "hobbi": "3N ( Ngoding , Ngegame, Nyibukin Diri)",
                "sosmed": "@apiszzaja",
                "kesan": "Bang Hafidz kocak, ramah, dan bikin suasana seru",
                "pesan": "Bahagia selalu dan lancar terus kuliahnya ya bang"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Campang Raya, Sukabumi",
                "hobbi": "Gym, membaca, dan bermain",
                "sosmed": "@kelelep_comberan",
                "kesan": "Bang Kaleb berwawasan luas serta pintar tapi tetep rendah hati",
                "pesan": "Terus menginspirasi dan sukses dalam kuliahnya bang"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal":"Sumatera Selatan ",
                "alamat": "Sukarame ",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kak Melva pinter ngoding dan baik",
                "pesan": "Semoga makin jago kodingnya dan sukses selalu kak"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syafiqui",
                "kesan": "Bang Syafiq pintar, berprestasi, dan inspiratif",
                "pesan": "Semangat terus berjuangnya di PIMNAS ya bang"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal":"Kotabumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "Bang Henry sosok yang bisa diandalkan dan baik banget",
                "pesan": "Tetap jadi pemimpin yang mengayomi dan sukses selalu bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WAwtA5fEL51nuW85WYaAiVLSUuy7u5EJ",
            "https://drive.google.com/uc?export=view&id=18jVApqi1e9paAOLSIKvea6LnD_FswRF0",
            "https://drive.google.com/uc?export=view&id=11jlbX4zAjp5iQmBjndMRleZdDEfdSFbb",
            "https://drive.google.com/uc?export=view&id=12MzRitqvDz5dJ-GnqLXYjX76YGgPJBMk",
            "https://drive.google.com/uc?export=view&id=1FpioGbmQLmbY1f9Q17TCOpNjZ-LIQESl",
            "https://drive.google.com/uc?export=view&id=1gSVip-VeskNYxK_fX69qYbIZRbs261yk",
            "https://drive.google.com/uc?export=view&id=1F-Ift-W6V-os2uB2Xds2zKzphuIl1sHK",
            "https://drive.google.com/uc?export=view&id=1czE7WkcOA_8fOwt2yM2C6146ANap3YoT",
            "https://drive.google.com/uc?export=view&id=1DuVeRUg3C5Pz7Y0bxFaqSktYF9Z1Jj3f",
            "https://drive.google.com/uc?export=view&id=19Aq-1liZCTHzoGEq7TZI7T-cTQxum8k3",
            "https://drive.google.com/uc?export=view&id=11V3QvKyySX2t2JcKoknAWLx5eu1hq74S",
            "https://drive.google.com/uc?export=view&id=1LS7Sm5127N1u0WoGKw2v8LIHcuiSkrM4"
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
                "kesan": "Bang Ihsan kocak, suka ngelawak, dan rame orangnya",
                "pesan": "Semoga dipermudah segala usahanya ya bang"
            },
            {
                "nama": "hanifah inaya sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak Hanifah ramah, lucu, dan baik banget",
                "pesan": "Sehat dan bahagia selalu ya kak"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah asik dan ramah",
                "pesan": "Sukses terus kuliahnya dan sehat selalu kak"
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Bang Hasan orangnya pendiem tapi seru dan asik",
                "pesan": "Semoga cita-citanya lancar dan tercapai bang"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin",
                "sosmed": "@lay.inr_",
                "kesan": "Kak Layina sederhana dan ramah disapa",
                "pesan": "Lancar terus jalannya dan sehat selalu ya kak"
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Bang Iqbal baik bagnet dan ramah sekali",
                "pesan": "Sukses terus dan dikelilingi hal baik bang"
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "@alljtine_",
                "kesan": "Kak Talitha humble dan seru orangnya",
                "pesan": "Semoga semua rencananya berjalan mulus kak"
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kak Nadia orangnya positif sekali dan ceria",
                "pesan": "Sukses selalu ya kak dan sehat selalu"
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "Bang Pome terampil main basket dan humble",
                "pesan": "Makin jago basketnya dan sukses kuliahnya bang"
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "Bang Afdhal orangnya tenang dan humble banget",
                "pesan": "Sehat terus dan lancar segala urusannya bang"
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kak Anggun ramah dan sangat asikkk",
                "pesan": "Sukses terus dan bahagia selalu ya kak"
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "Kak Della ramah dan asik",
                "pesan": "Lancar urusannya dan sehat selalu ya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UjeTqdtemb_pCc6d0CWVbFmFECIEcsMg",
            "https://drive.google.com/uc?export=view&id=12maynSJTERwffZ4k2Lyo6b7CxC5hvY5z",
            "https://drive.google.com/uc?export=view&id=1ijeX0orFVru1BAA04j6NkYqgSZUfvfrA",
            "https://drive.google.com/uc?export=view&id=17aH688j9-UCEfGAt6C70NYTiX21Z8RPA",
            "https://drive.google.com/uc?export=view&id=1krGl5rLMqvTPdsrciyYqOR6CtQA3plh3",
            "https://drive.google.com/uc?export=view&id=13BMNPZz8ZdekJSOmoX3aVpoyljPXgiw9",
            "https://drive.google.com/uc?export=view&id=1bTLSWtKKTtcLsalYdSPGl-4Ky4ciFHqR",
            "https://drive.google.com/uc?export=view&id=1DtqPBsU8MXsKaSAGMKWyXhSizyqGndJj",
            "https://drive.google.com/uc?export=view&id=13Fzal24rCltraW9W-2EGfbT8MP1BOQHX",
            "https://drive.google.com/uc?export=view&id=1-PG_ZR4Vwr4X4tzcSfYZ0lPOieXrYL_5",
            "https://drive.google.com/uc?export=view&id=1PJdaSAK3Z4ufrnC4hujU6J09pUhkevDZ",
            "https://drive.google.com/uc?export=view&id=13aqR6-bIMkIBJ2iJmaWVGOpp8m5HDYCV",
            "https://drive.google.com/uc?export=view&id=1-c3yuozjIpyhWlbKpYj7toOiwgPT00Dq",
            "https://drive.google.com/uc?export=view&id=1yRjuO64V97orH2TsE4ukQkTHG-8jrYcq",
            "https://drive.google.com/uc?export=view&id=151abb06UdlkJdsENrn7k1_Y4IuywOXDl",
            "https://drive.google.com/uc?export=view&id=1zKEwv5rakzSyeEXCXVqWrIth2xAVw9OF",
            "https://drive.google.com/uc?export=view&id=18Lg4dGWduYlDt1u2akl-tAEQzbJe-DN8",
            "https://drive.google.com/uc?export=view&id=1JX8zPKLju6eYz_BJ1yXK110RpBPpx5VK"
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
                "kesan": "Kak Nayla humble, ramah, dan gak kaku diajak interaksi",
                "pesan": "Semangat terus memimpin Medkraf dan sukses selalu ya kak"
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Dona sangat membantu dan baik bangett",
                "pesan": "Semoga amanah di Medkraf dan kuliahnya lancar terus kak"
            },
            {
                "nama": "Labo John Noel Napitupulu ",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran ",
                "sosmed": "@noerruuu",
                "kesan": "Bang Labo ramah dan mudah diajak ngobrol",
                "pesan": "Sehat selalu dan sukses jalannya ya bang"
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Way Halim ",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kak Tasya selalu ceria dan penuh energi positif",
                "pesan": "Semoga hal-hal seru selalu datang ya kak"
            },
            {
                "nama": "Felisya Nabila Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal": "Lampung Timur ",
                "alamat": "Kota Baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "Kak Felisya lucu dan cukup santai",
                "pesan": "Semoga semua target dan cita-citanya lancar kak"
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "21",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "Bang Razan lumayan kalem tapi jago badminton",
                "pesan": "Lancar urusannya dan makin jago bang"
            },
            {
                "nama": "Sania DWi Ayu Lestari",
                "nim": "124450086",
                "umur": "21",
                "asal": "Karawang ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania ramah dan mantap banget pokoknya",
                "pesan": "Makin sukses menghasilkan deisgn design ya kak"
            },
            {
                "nama": "Allisha",
                "nim": "12445019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "Kak Allisha seru, multitalent, dan banyak skillnya",
                "pesan": "Terus berkarya dan mengasah bakatnya ya kak"
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kak Alya seru dan ramah orangnya",
                "pesan": "Semoga selalu semangat dalam menghasilkan ide-ide baru kak"
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kak Bunga ramah, kocak, dan asik",
                "pesan": "Tetap jadi sosok yang seru dan sukses terus ya kak"
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Alquran",
                "sosmed": "@difanyhsa_",
                "kesan": "Kak Difa ramah, baik, dan seru",
                "pesan": "Sehat selalu dan sukses kuliahnya kak"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@nzlhauly_",
                "kesan": "Kak Nazla lucu dan baik banget",
                "pesan": "Semoga dipermudah dalam segala urusan ya kak"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Aira Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kak Raihana baik dan sangat ramah",
                "pesan": "Makin kreatif dan sukses buat kepemimpinannya kak"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame ",
                "hobbi": "-",
                "sosmed": "@daffascript",
                "kesan": "Bang Daffa kocak, ramah, dan seru kalo bercanda",
                "pesan": "Semoga sukses terus kuliahnya ya bang"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "Bang Edsel baik dan murah senyum",
                "pesan": "Sehat selalu dan dipermudah urusannya ya bang"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Kak Rachel sangat baik dan ramah",
                "pesan": "Semoga rencananya berjalan mulus dan sukses selalu kak"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis dan menulis",
                "sosmed": "@_shaazzh",
                "kesan": "Kak Shafa ramah, dan baik banget",
                "pesan": "Semoga diberi kesabaran dan kesehatan selalu ya kak"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "Kak Zannuba humble dan seru",
                "pesan": "Lancar jalannya dan selalu bahagia ya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
# Tambahkan menu lainnya sesuai kebutuhan
