import streamlit as st
from sakura_ui import (
    render_buku_kating_header,
    render_kating_cards,
    sakura_dept_menu,
    display_kating,
)

render_buku_kating_header("118 - Halidaziyah Maritoma Hasibuan")

# Navigasi Kategori Departemen (Sakura Theme)
def streamlit_menu():
    return sakura_dept_menu()

menu = streamlit_menu()

def display_images_with_data(kating_data):
    display_kating(kating_data, departemen=menu)

if menu == "Kesekjenan":
    def kesekjenan():
        kating_data = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1eBpol26NutCHd6i7k16vbsjLDTJRpnW3",
                "kesan": "Bang ginda orangnya baik, ramah, dan juga humble",
                "pesan": "semoga urusannya dipermudah",
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=102xtzlxQbv3R1z5EwyAIwkiBZyoiAEyC",
                "kesan": "Bang Aqil orangnya ramah, bisa main basket tapi gak nyangka hobi abangnya masak",  
                "pesan":"Semoga lulus tepat waktu ya bang",
            },
            {
                "nama": "Efi Defiyati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17Uiht7sKETwoC99CnqlPm7jJhKv88n2t",
                "kesan": "Kak efi murah senyum, ramah, baik",  
                "pesan":"Semoga segera lulus ya kak",
            },
            {
                "nama": "Qois Olifio",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1RwWESx05tiBontM--1p1DnHt-flydQaR",
                "kesan": "ngejelasin maaterinya terlalu cepat, tapi abangnya baikk",  
                "pesan":"jangan terlalu cepat ya bang jelasin materinya hehe",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pNngBRKwgBdFTQjuv3gvIotN9TPy9Jrh",
                "kesan": "Humble dan baik",  
                "pesan":"Semoga segera lulus ya kak",
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15CbYyV1U3JllY6HQc30rn_Yy6DTHBlV9",
                "kesan": "Kak luthfia orangnnya baikkk banget",  
                "pesan":"Semangat terus ya kak :)",
            },
        ]
        display_kating(kating_data, departemen=menu)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        kating_data = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Y0BG9uXjv_SQYSU7vNfhWUZaqAKSc0qs",
                "kesan": "Bang ridho baik sekaliii dan jugaa humble",
                "pesan": "semnagat kuliahnya bang Ridho",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mBSKkRFo16aBlikH7oIbyuzTeFutIULv",
                "kesan": "cantik banget kak jue, baik, dan memotivasi",
                "pesan": "sukses selalu ya kak jue :)",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1weyS9cZOrxlH4vh1G1-OjJxUj2QqxBiO",
                "kesan": "Bang dharu kerennnnn",
                "pesan": "Semangat terus bang",
            },
            {
                "nama": "Givaro Ananta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cCyLVqyqNpC_BWCgaGLBLz9mYId0h-L6",
                "kesan": "baik sekali, humble",
                "pesan": "semangat kuliahnya bang givaro :)",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12gGjjBeIMffNhXuiwyAEqPq0odxbqClV",
                "kesan": "Kakaknya baik, humble, dan ramah!",
                "pesan": "happy teruss kak",
            },
            {
                "nama": "Gh Mikael Niko A S",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17pUQj-rFGMY3mZu8wlbNSugPapAMrCyA",
                "kesan": "kenal abang dari daplok pplk",
                "pesan": "semangat terus bangggg:)",
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1zrG8iT6mRVDwAOxp3WiuUBorzFO3U0d5",
                "kesan": "kakanya manissss bangat, dan baik",
                "pesan": "semangat dan sukses selalu ya kak",
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SnVFHmvfWsCCBX4rNITbX51rkEr8hgDQ",
                "kesan": "kakanya kerennn dan menginspirasi",
                "pesan": "Sukses selalu ya kak",
            },
            {
                "nama": "Hani Qurrota Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=193pRZfwnEjFOYgw5vmbNw7746VNrVp_T",
                "kesan": "kak hanii cantikkk dan ramah",
                "pesan": "happy selalu kakkk",
            },
            {
                "nama": "Jeremia Halim",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TVdSKP672yhmK7FxpOI9JJEZWK5q17nj",
                "kesan": "Abangnya keren dan ramah",
                "pesan": "tutor ngoding bang hehe:)",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CGKgcQ06NT1iHBXgXsNHIWNOYFfwbth4",
                "kesan": "Bang Jona baikkkk",
                "pesan": "semangat terus bang:)",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1aHXXtJ-IZ07yGpuIZP65ts6ZpQ0xQZv6",
                "kesan": "Kak Sekar baikk dan juga tegas",
                "pesan": "sukses selalu kak sekarr!!",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1EONaylM99-mnO6pPMuKJrePkZdrSmcko",
                "kesan": "Kak Nashwa cantik, gemmes, humble",
                "pesan": "Happy selalu kakak :)",
            },
        ]
        display_kating(kating_data, departemen=menu)
    baleg()

elif menu == "Senator":
    def senator():
        kating_data = [
            {
                "nama": "Fathinah Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1EaHKTe-wJQvNpBTaBl8UB_bzlozOFHnO",
                "kesan": "Kakaknya baikkkkk dan kerennn",
                "pesan": "tutorin jadi orang keren kak",
            },
            {
                "nama": "Helmy Surya Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1J8RSflnAwotl4EoK7rwSUB-thd1AM31B",
                "kesan": "Bang Helmy baikk dan Ramah",
                "pesan": "Sukses terus bang:)",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rAC5TmUFT5UQb907nfvb_Z4edQgy5LfC",
                "kesan": "Kak Lia Ramahh dan humble",
                "pesan": "Semangat terus kak",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WM3NEnOX35tfHWCpDarhUbAApXlQrHQt",
                "kesan": "Kakaknya cantikk dan menginspirasi",
                "pesan": "Sukses selalu kak:)",
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CqF5ymprQyDJaXHxqgTGr4M7tx8DVlH4",
                "kesan": "baik sekali",
                "pesan": "Semangat terus bang",
            },
            {
                "nama": "Suci Aulia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1D3jLMdj03ThFq1zRtQ1J6ErMuFDRgYfk",
                "kesan": "kak suci sangat ramah dan baikk",
                "pesan": "happy terus kakakk:)",
            },
            {
                "nama": "Wielman Itolo Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WBBh19TGl9IP3kLCewwopi3i0OypNtJB",
                "kesan": "Bang Wielman sangat baikk",
                "pesan": "sukses selalu ya bang wielman",
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1STKorr_kHJFgswz3HUStmdfS_vjFkWY7",
                "kesan": "kakaknya cantikk sekaliii",
                "pesan": "happy terus ya kakkk",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OxhYCZdr78BnfNgPvGXpDtK0MPP-QQ4l",
                "kesan": "Bang Hazel sangat tegas, dan baik",
                "pesan": "Sukses teruss abanggg",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JeKGfMEN0N19j78BTQbvtWXDOsSqPm7-",
                "kesan": "Kakaknya kereen dan baikk ",
                "pesan": "semnagtt terus kuliahnya kak dwii",
            },
        ]
        display_kating(kating_data, departemen=menu)
    senator()

elif menu == "Departemen PSDA":
    def departemen_psda():
        kating_data = [
            {
                "nama": "Arienta Khusnul Ananda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1e5iCAjErIUOkEJgGmZTwoGsMWbOrerWM",
                "kesan": "Kenal kakak dari kelompok KDP",
                "pesan": "Semangat terus kuliah kakk:)",
            },
            {
                "nama": "Vany Salsabila Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15LGp2u2nrrKcdj3ee_9v0l2qL1JcD4dF",
                "kesan": "Kakaknya sangat Tegas, dan baik ",
                "pesan": "Happy teruss kakkk",
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qQmEZjqA3tW3hTZ4Mmmboim2hM6hr2wJ",
                "kesan": "Abangnya sangat Tegas, dan menginspirasi!",
                "pesan": "Sukses teruss bang",
            },
            {
                "nama": "Desman Velius Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1EPkMxVcR3W59Yl_-3xombKNbVsQG65mq",
                "kesan": "Abangnya baikk, ramah, dan humble",
                "pesan": "Semangat kuliahnya bangg:)",
            },
            {
                "nama": "Afriza Azmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MytKvf-6_P3k9RneNS1WdS0uRIq4rhJZ",
                "kesan": "Abangnya tegass, dan baikk",
                "pesan": "Sukses terus bangg",
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1KjkmG81Ss8_v4Ccf4b7nDe0yZ6v9R-9_",
                "kesan": "Abangnya sangat baikkk",
                "pesan": "semangat teruss abangg",
            },
            {
                "nama": "Caesar Ozora Alrando",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1IUuNKh4phLj_fGmT6yxt6DOjdLrhcAMa",
                "kesan": "Abangnya tegas, dan ramahh",
                "pesan": "Sukses selalu bangg",
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pfe-g3S0o-vDCF7--hJGKEwSxVQfEQUB",
                "kesan": "Kakaknya Tegas dan profesional",
                "pesan": "Happy terus kakkk:)",
            },
            {
                "nama": "Haikal Seventino Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Lfe06G5OLYa81WzjD-0pfKmXHcoAP6Fu",
                "kesan": "Abangnya tegas dan baik",
                "pesan": "Sukses selalu bangg",
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OzmeXrj2JOQfX-5wxeG6xyk28hBmIUlY",
                "kesan": "Kakaknya ramah, tegas dan profesional",
                "pesan": "Semangat terus kak Putrii",
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13wbNA5W5MicyZUw3VdtRMeOs0Qa-INgV",
                "kesan": "Kakaknya baik dan tegas",
                "pesan": "Happy terus kakk",
            },
            {
                "nama": "Azzelya Thianandry",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ULo-XPKIssvLG5WOMoMjtKhoHrBGyE77",
                "kesan": "Kakaknya cantikk dan baik",
                "pesan": "Semangat terus kuliahnya kakk:)",
            },
            {
                "nama": "Charrlindah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1H528dvrmVBvKkgdsw2YD0Eg5za_iJtJU",
                "kesan": "Kakaknya sangat ramah, humble, dan baik",
                "pesan": "Sukses teru kak",
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JRHRtraWAeNrA1T7b3UYsclRmdeqg9B7",
                "kesan": "Kakaknya sangat baikkkk",
                "pesan": "Happy selalu ya banggg",
            },
            {
                "nama": "Nabila Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17-nHG_R-MfSg9C-G0H_7B_jyzFtoBOd9",
                "kesan": "Kakaknya cantikk dan ramah",
                "pesan": "Semangat terus kak Nabila",
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=138ThlKAakcXHsGsbA7pkInDADibFvlW4",
                "kesan": "Abangnya baikk dan ramahh",
                "pesan": "Sukses terus bang",
            },
            {
                "nama": "Salavia Naharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1q4cbV2MQ_3wM1ZRdvB26UX3r6I2PX6ex",
                "kesan": "Kakaknya sangat ramah, humble, dan baikkkk",
                "pesan": "Happy terus kak",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_psda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        kating_data = [
            {
                "nama": "Fabio Banyu Cyto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=166qpK9lPW8hN3-kEtoewHPiTBg56oOlt",
                "kesan": "Kakaknya sangat baik, dan menginspirasi!",
                "pesan": "Jangan bosan ngarin kami ya bang",
            },
            {
                "nama": "Tanty Widiyastuti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18mgQKDXJlrlXWSiJfsJdrz9ZLSAulZBi",
                "kesan": "Kakaknya sangat humble, dan baikk",
                "pesan": "Happy terus kak",
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bvacSPaIBpbsHDot8M-qHRGKS5PsmsJw",
                "kesan": "Abangnya baikk dan ramahh",
                "pesan": "Sukses terus bangg",
            },
            {
                "nama": "Razin Hafid Hamdi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1FSS-rpjkXW0tD8jh8ZhhHv1rAUKzHDrI",
                "kesan": "Abangnya sangat menginspirasi!",
                "pesan": "Semangat terus kuliahnya kak",
            },
            {
                "nama": "Manuel Frederika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=10cm7PDzqP_4ayZofScxecQrxuRH2LI12",
                "kesan": "Abangnya sangat ramah",
                "pesan": "Semangat terus bangg",
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17UHfwZa5XTkH2YcZDPlYBiHhcSnT-Z3n",
                "kesan": "Kakaknya sangat ramah, humble, dan bikk",
                "pesan": "Happy terus kakakkk",
            },
            {
                "nama": "Risa Romadona",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1NjtpWVxWqjBks4tnV3KvszVvyCnsyG_f",
                "kesan": "Kakaknya sangat ramahhh",
                "pesan": "Semangat terus kakak",
            },
            {
                "nama": "Vannisa Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Xl_MdO3x-sbaMzPF4yTxRjjEHGnwH15_",
                "kesan": "Kakaknya sangat humble, dan baikk",
                "pesan": "Sukses terus kak",
            },
            {
                "nama": "Yulia Kristine Malau",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dphA7utRsPHKVKywbYnW4uLBhNV7Pttj",
                "kesan": "Kakaknya sangat ramah dan baikkk!",
                "pesan": "Semangat terus kuliah kak",
            },
            {
                "nama": "Elsa Sitorus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bkZvpkOxEm7hMOJqEfzoZ01_w0CHRrB3",
                "kesan": "kakaknya ramahhhh",
                "pesan": "Happy terus kakk",
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1T485vNqtRA50hZlzsupHlzLxZYkQalqX",
                "kesan": "Kakaknya sangat ramah, dan baikk",
                "pesan": "Semangat terus kakak",
            },
            {
                "nama": "Lovianora Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UglmaV97qC0RrrnT4IxbZdWLo-astGz_",
                "kesan": "Kakaknya kereenn",
                "pesan": "Semangat terus kuliahnya kak",
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dDcEm4NDaPTVvEXvI-6vkh7bc5R4QtIH",
                "kesan": "Kakaknya sangat ramah, humble, dan baikk",
                "pesan": "Happy terus banggg",
            },
            {
                "nama": "Sherena Florencia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11OX0L76AXFMUexMV7evb3OKaXa_LBWSD",
                "kesan": "Kakaknya sangat ramahhh",
                "pesan": "Semangat terus kuliahnya kak",
            },
            {
                "nama": "Faiza Try Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vaIo_WNVtfig3YUwNl8mv3gchCtEe7M-",
                "kesan": "Kakaknya sangat baikk, humble, dan menginspirasi!",
                "pesan": "Happy terus kakkk",
            },
            {
                "nama": "Gathfan Nadif Ali",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1iiTSmutoWE5S4l8Ck7gwkgaaeSR-Qpan",
                "kesan": "Abangnya sangat baikk, dan humble",
                "pesan": "Semangat terus abanggg!",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1elgV3c0kK_TrFyDdvq6iWugSSjRy0x9z",
                "kesan": "Kakaknya sangat ramah dan baikk",
                "pesan": "Happy terus kakak",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bguXyjMwVrCYrQEOnNhP3USq2Uurcvbm",
                "kesan": "Abangnya sangat menginspirasii",
                "pesan": "Sukses terus banggg",
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1J3I6rJQL5UEE8nMDLTKgy3d9YvDnvpJJ",
                "kesan": "Kakaknya sangat baikkk",
                "pesan": "Semangat terus kuliahnya kakkk",
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1r7FrEQGDm0atVA6mB7QyS2MV4rtEgKpw",
                "kesan": "Abangnya sangat menginspirasi!",
                "pesan": "Happy terus bangg",
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CmF89rp_fr1-g3vx2M7H9k73BWiR_Wty",
                "kesan": "Abangnya sangat ramah, tegass, dan baikk",
                "pesan": "Sukses terus bang",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemen_eksternal():
        kating_data = [
            {
                "nama": "Arini Puteri Elandra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_r05sgRgZQL2_l7gRTu6fqu-X71V0cJ9",
                "kesan": "Kakaknya sangat ramah, dan menginspirasi!",
                "pesan": "Semangat terus kuliahny kak",
            },
            {
                "nama": "Nabyla Sharfina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11ljHJAgCd0K3zP9LksJ5wZ-_ydCY3oUV",
                "kesan": "Kakaknya baikk bangett",
                "pesan": "Happy terus kak",
            },
            {
                "nama": "Khoirul Muttoharoh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1eXNEtZHWZfS2Vq7WMFjySAUXUeaNcEma",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15FGmhcz5rKEs4xhiAFCdbu8G6wK9jG7Z",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Indah Khairunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=144Y_PfoYY9g9Xpv74r7TDx6X3nvlA5B6",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bima Ekayasa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VSLAxbSRrNf3prJZAEOqbtnzZtKo-vbM",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1i-QsDnJSKE-RDorzG_AYYtVxjVE9txKU",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Adinda Deswita Maharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Afg9q4wJgWrNw8fACNwOH60AxyNjjhtw",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Yollanda Agustina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ZuyaoLvYnzD_oOOb-wh2eOkqfqc_9LgT",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rr3SJKFe-9-iJ2NRZLQAv-oID07KeF11",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Alfaya Abiyyi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UN3qtQtic-ryFDVs5fVQ_ETJO7pSBVTw",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Asri Meilani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13Xd-lrX026izRXXACqNm-HxFm68eX2en",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ahmad Rizky",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1otnreGPnkmABUjLxxl-neWSZtq3HNkzL",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Selma Siti Aisyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AGQcLOoCSUwUf0RWsfYWWeRMUjUEnnZw",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1D79nPfWiFDydtLlhs6iI_uDNUdO_kObP",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Fathya Intami Gusda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rfS6ncMQTHe9YaL4rWPz8FrzdPwPuoyS",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1sJndG6nkOIDbnhWtgGsZD6NKqA0yILe4",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Danil N Fadillah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1konmstD9YJuPRC7u5MOFsiAkj7Ykfmqc",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Favian Arkaanda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1APrMjcO_S0c4vgWTDIXniWvv6szGk0Sv",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MrqDIvZrTxxUCRFrxMHl5xFJuzf4FYlZ",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Rizaldi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rNSTW-_Qf2EjutFBTMpdhwzfDcckIiU-",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Saskia Nova Magdalena",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1eXSsJBysMTD1jQtrABvae6_WJiaXFnoJ",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_eksternal()

elif menu == "Departemen Internal":
    def departemen_internal():
        kating_data = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jrauAVlslerzPEZ96onfxAeWD_8hNMWU",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Kharisma Mustika Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Gd1XWCx1BxkWSpvbRd_YOR9gzwS0sz5a",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UfxvTiVQRB7dY7HR64Rh0uTwpjFadCNR",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1KFz_TqEh_wmHXIEe9tGyEyn17GUu56yg",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Of1i_fg759OS2roUMjE-CsetcPeujzcR",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13b7Eyh5Luh63CVZpA2f-Jl-x6DAsXEfn",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Cerine Sihotang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1W6nDwzUWm05ZBy-HFs6t19zFm4KayNCp",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Jaya Saputra Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wXe1JCO-o_NorRSgJMHZ8O-1rTbG5gPu",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Najla Nursyifa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yCNukeiHv_lt_ag_bFqhN91IVFKhZN_U",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rozak Ramdani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Opri17OaRCxFdBg2cGxeTq8Xr4b6QjtN",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Teresa Christiani Purba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MXia_nz247uAQvOpFU2DXHVXLQWLS23S",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Audina Fitria",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ZRlyOpBqwg1twqKwn9YLAYPyjhxKrJmd",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Z6XfYDBrYzyNficKQfgO9bVVPjBEy8Dl",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1BMUcZkCVcXadkOzjugsIIbuihMOlmiKp",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Harvinsyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YAIHSk9AUlLrzSazNLqfZwk2ippEpKpo",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ycF4zZAA0GCS7AuzdzDgeF1y1KYXQED9",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_internal()

elif menu == "Departemen SSD":
    def departemen_ssd():
        kating_data = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pyfpSjBXtriIPlF27ul2r0EhEsphCEqU",
                "kesan": "Abangnya sangat ramah, humble, dan baikk",
                "pesan": "Semangat terus kuliahnya banggg!",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_5YXPG3wQMaTsBpITYzguHpbsl4HPNhv",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Afifah Fauziah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wKhSGVLtYBNBqJ3CEhGqQNQCHjit9jik",
                "kesan": "Kakaknya sangat humble, dan ramahh",
                "pesan": "Happy terus kakkk",
            },
            {
                "nama": "Anadia Carana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14SVUiIF4t-SkA5tmG1Za6cwk-HoiB940",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14b4utMUsnyLyNI6dOZXEpCP5UYF7CmQc",
                "kesan": "Abangnya sangat ramah, humble, dan baikk",
                "pesan": "Semangat terus bang Hasannn",
            },
            {
                "nama": "Layina Ropiqo",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1RclD8g7p_txgQyo9Z1DDZDi6cKiICsjx",
                "kesan": "Kakaknya sangat baikkkk",
                "pesan": "Hppy terus kakk",
            },
            {
                "nama": "Mochammad Iqbal Az-Zahir",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1aJLmu_vVcuWtwE_FSmdzz7ZUpMWT1VoO",
                "kesan": "Abangnya sangat ramah, dan tegas!",
                "pesan": "Semangat terus kuliahnya bangg",
            },
            {
                "nama": "Talitha Justine",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QlqkMIEeP3uAqaJ5jD81Af73T9hnk3SH",
                "kesan": "Kakaknya sangat humblee",
                "pesan": "Semangat terus kakakkk",
            },
            {
                "nama": "Abdillah Fikri Al Pome",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1kZKDWfLOFyaw2dVGuhspUkaiehFwMe83",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya bang",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Tbga_i0IMNJsxbMBdaM_L-3E-pMp5Q8U",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anggun Nita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16BuaJVSaULCUYHJDiq9LU0A8TiF51liu",
                "kesan": "Kakaknya  humble, dan baikk",
                "pesan": "Semangat terus kakkk!",
            },
            {
                "nama": "Della Anisa Fitri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1O3P_0oh0A7ezJxJ8s6gQNovhpYCOEdCF",
                "kesan": "Kakaknya sangat ramahhh",
                "pesan": "Happy terus kakkk",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_ssd()

elif menu == "Departemen Medkraf":
    def departemen_medkraf():
        kating_data = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Z3rimOl9qVQ0BxcmOvTsQeBzPPf9lHIS",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Donna Maya Puspita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1oXJifgviy3my1JcyhCoCXhVYYm6zc9UN",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1je0yIapM7CVuWQm3paS3nbExWwLWWqNs",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UNzoKzTQ4kX_SvWmomAyABys8ZdOMMeq",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Raihana Adelia Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1aqSv-kgMIScGZAfJ0-58Bh12a8lj8PG2",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18LTnYA5AYawlG-ZDbKNmucyTD58NYnzt",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VNTAkkGOMEBOwN3RBCpNyU7gC-gmjwTx",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SzaSBhsnSSOKy2rVxjvD4MsB6GHSDBvJ",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Allisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OOyy03pP5dKfuhmxDYjdN3M-5RH0x4Bb",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Alya Ramadhanti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1nRDQ07t-e5pfMadPqqZm-ikvVkA2DWRg",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_iuBYzwcxShyp--ZkTucq3A2q_am_w1s",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Difanya Husakina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1a79o8jYhsIX_VAm9vtVWAklCOc0xY_MA",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Nazlah Auliya",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1D_0xqJQ10zUW6gBN9zQmi6oZ5Hp1s4TT",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1DmR9V9EwCymzL1mkHEY9BHd8IqWYx_wX",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Edsel Adya Pradipta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bB8YWu2CepGK6FiKJrheWtPGiJVY7bQs",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WOFqkXva-4SyOapOZAOsOCg6o42pZS3L",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=10ywZLpqAPf0cJwE4wC5YVutPsSAKJW-A",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SLRx59xf6Ht65eWvejqU6E4Cdmt7MXPc",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_medkraf()

elif menu == "Departemen MINBAK":
    def departemen_minbak():
        kating_data = [
            {
                "nama": "Kevin Antonio Junior",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UaD2hqPKV9xrrpaSu4b_k7CChdT-rhJ2",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17nGG3qkOn9TUtkPJeg9bT8ExYIFial0u",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WzOI-xNJxmOqtviNF9Zl4_5cMzRNCIbR",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Ridwan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wuBL-f6pgxypbsx-mN-arHGayIlcmZg4",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YwEgabh7jyAVhF6_p6ojqcczv233dqRN",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Dafa Elpriza",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yC6Xm-GNF2bcXnYPsFTkPxIL2B7A_tRH",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=112UvAFoq4D_aD7kcEL_YNN4s6nTdq0ck",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17bOcFFqT4o4X7YW3klIBlYVG4HhPDFPg",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Juwita Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1IroBw2fh0NztQwxwkjLBgCSy6ZGv9rsu",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Andra Ilham Bintang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Yhf2nK0Cip19xQrP4SwYXX9lFIvrv2MW",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_3shdG_4bdDWGtkjFsFZzx6ibnAQj3wG",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Dat7wIm0-7JkcP60rHmxszLmHmNiktvu",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1s-Zah817iT_tkNZzqS0JVG3qfrb5fdrc",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ucpVvhqGd5rXopXieJxltoRRV3z8FSls",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1zhldbN4q63Titqu3P8mGutRg_0z5NfvL",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_minbak()
