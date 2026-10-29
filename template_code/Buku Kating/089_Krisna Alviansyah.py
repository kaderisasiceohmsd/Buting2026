import streamlit as st
from sakura_ui import (
    render_buku_kating_header,
    render_kating_cards,
    sakura_dept_menu,
    display_kating,
)

render_buku_kating_header("089 - Krisna Alviansyah")

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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1J-rsWHF5zwQ_-_xqxt7DYWF-5P5ymzKv",
                "kesan": "Bang ginda ramahnya gak ketolongan, humble, adem liat bang ginda rasanya",
                "pesan": "gass cumlaude bang",
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=137c5EKVfSQvxD8cQ_htbjel-yHPUU_M5",
                "kesan": "Keren berkharisma",
                "pesan": "Lulus tepat waktu ya bang",
            },
            {
                "nama": "Efi Defiyati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18Tfshe_-1nTp82E9psDJK0f4nk2r0Ke3",
                "kesan": "humble, ramah, baik",
                "pesan": "Kak, senyum selalu ya kak",
            },
            {
                "nama": "Qois Olifio",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1IvA_nI4wpruLlaCVw1ZL-JnDiMi1K03R",
                "kesan": "Cool, dan keliatan orang yang Sistematis",
                "pesan": "Bang waktu presentasi jangan terlalu cepat ya bang hehe",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1K3sEk-WQWh1kF9zRNe4ajtM_QR37NRiT",
                "kesan": "humble dan baik",
                "pesan": "Selalu happy ya kak :)",
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1709lIORxWXXRmt_r0Bk0GcYqI55IYWgy",
                "kesan": "humble dan baik",
                "pesan": "Jangan mudah patah semangat kak :)",
            },
        ]
        display_kating(kating_data, departemen=menu)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        kating_data = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1gZ9IggX8rjxaw7nwxKiSjKkP0o8y6ren",
                "kesan": "Bang ridho ramahnya gak ketolongan, humble, adem liat bang ridho rasanya",
                "pesan": "gass cumlaude bang",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1d9JaEJeah1TzGC4HdXt8eNj87PFg4KkZ",
                "kesan": "Kakaknya imut",
                "pesan": "Semangat ya kak kuliahnya, cumlaude ya :)",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Z_UCc5jFbbzHqU3OqiTqtKW4k7Y0dcnN",
                "kesan": "Abangnya keren banget waktu liat perjalanan selama kuliahnya",
                "pesan": "Lulus tepat waktu ya bang dan Akademiknya juga selalu bagus",
            },
            {
                "nama": "Givaro Ananta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1NzfunTqYdz5-O1ZobEl9JCkEWblIGhuo",
                "kesan": "Abangnya terlihat cool",
                "pesan": "Selalu semangat kuliahnya bang Givaro",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ZBSQuhGe4eM1eb0XFJCkxoXhDH6D56WR",
                "kesan": "kak monica pembaik",
                "pesan": "Semangat kuliahnya ya kak maap gak ada kata kata selain ini :)",
            },
            {
                "nama": "Gh Mikael Niko A S",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1N8aKdak_CfVFQz2qH7qRE9NJLEbP35O-",
                "kesan": "Abangnya asik",
                "pesan": "Semangat bang kuliahnya",
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1nFN_M_5_iIgw-X4sgSHgV4qMbmTnJk3i",
                "kesan": "kak sarifa lucu",
                "pesan": "Semangat kuliahnya ya kak, maap kak template hehe",
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Ny_wiQ4fd0wJjzD1ArIEdMElfC4afcD5",
                "kesan": "Kakaknya pembaik",
                "pesan": "Semangat terus ya kak kuliahnya",
            },
            {
                "nama": "Hani Qurrota Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fp0Gwk12mCGzPIksEs_xN9wlxJlub57e",
                "kesan": "Kakaknya cantik banget",
                "pesan": "Semangat ya kak kuliahnya",
            },
            {
                "nama": "Jeremia Halim",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1LmJ0_dAkId8hUOrW-Mk6cHFT8lhFIiXh",
                "kesan": "bang jeremi algoritma video ignya sama",
                "pesan": "Semangat terus ya bang jeremi kuliahnya",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1B1WA0AXP8HMhnpqi8E2gIrcgk5wTjns9",
                "kesan": "Bang jona unik, gak bisa di tebak dan lucu",
                "pesan": "Semangat terus ya bang sama akademiknya",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HHEGZO_liqOpOewXUzzpXkvrN-2j1ibh",
                "kesan": "Kakaknya humble",
                "pesan": "Semangat ya kak kuliahnya",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16pSZ1MbbV_LKplFMEl7JhU1sylWRcVxz",
                "kesan": "Kakaknya cantik dan lucu banget",
                "pesan": "Semangat selalu ya kak sama kuliahnya :)",
            },
        ]
        display_kating(kating_data, departemen=menu)
    baleg()

elif menu == "Senator":
    def senator():
        kating_data = [
            {
                "nama": "Fathinah Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1w-rCPlAlpDzDwgr0DWnzYHhV188f4RSx",
                "kesan": "Kakaknya terlihat pembawaannya santai",
                "pesan": "Semangat ya kak kuliahnya semoga lulus tepat waktu dengan cumlaude :)",
            },
            {
                "nama": "Helmy Surya Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1H0JDw9g3VuBq27LoV_ZDD2H7IoVhWRLG",
                "kesan": "Abangnya santai, asik dan humoris banget",
                "pesan": "Semangat terus ya bang helmy kuliahnya, selalu lucu ya bang",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1DToMyoJ8wKUM0fvPuz9bvFlcP3o9FKKH",
                "kesan": "Kakak humble banget",
                "pesan": "Semangat selalu ya kakak nim acu, lulus cumlaude ya :)",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1a7aHNPGQfzkJrI2ivkGGC96X-s0VeI2r",
                "kesan": "Kakaknya mudah banget di ajak bicara kerasa aku ngomong sama kakak aku",
                "pesan": "Energi positifnya jangan padam ya kak, semangat dan semoga lulus dengan cumlaude :)",
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1zIZDLXVP9JJ0OGslxMoL1d_8QgaF8jCK",
                "kesan": "Abangnya terlihat sangat pembaik",
                "pesan": "Semangat kuliahnya ya bang Fernando, jangan menyerah!",
            },
            {
                "nama": "Suci Aulia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1r-6rPWoM0CkuatUcUEQKJ2ezuojsfytq",
                "kesan": "Kak Suci terlihat berwibawa",
                "pesan": "Kuliah dengan lulus Cumlaude ya kak",
            },
            {
                "nama": "Wielman Itolo Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1F5lwFSVA9XvDRfO8qLpdMqfWwUgsmLUR",
                "kesan": "Abangnya keliatan chill guy",
                "pesan": "Semangat kuliahnya ya bang wielman, jangan menyerah!",
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1g1Q8Uqa0Oc2jGn0yxDmckjzzwYVPkMQw",
                "kesan": "Kak Aqila terlihat lucu, dan pembaik banget",
                "pesan": "Semangat terus ya kak aqila selalu tunjukkan energi positif kakak :)",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1oWYM1XQSUwTbSzM-NAqtd3rVgGzdWSIp",
                "kesan": "Pembaik visualnya",
                "pesan": "Semangat terus bang Hazel ya",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1EOlLdB7ht7Jm5yCXNVS0Wzdd01YGRpFr",
                "kesan": "Pembaik banget kakaknya",
                "pesan": "lulus tepat waktu ya kak :)",
            },
        ]
        display_kating(kating_data, departemen=menu)
    senator()

elif menu == "Departemen PSDA":
    def departemen_psda():
        kating_data = [
            {
                "nama": "Arienta Khusnul Ananda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CAiFEwAA2WclKCO_uZhpC4n_B6XV-XU-",
                "kesan": "Kakaknya keliatan cool",
                "pesan": "Kak Arienta semangat ya sama impiannya dan lulus cepat :)",
            },
            {
                "nama": "Vany Salsabila Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AO_KAlAsru19p0xEU45mqp9NgLClr3sY",
                "kesan": "Tegas",
                "pesan": "semangat ya kak kuliahnya :)",
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cAVnAydMm311stuIXd-atswINP_HGeG7",
                "kesan": "Galak, Ramah, Pembaik",
                "pesan": "Semangat bang nobel kuliahnya pasti impiannya terwujud",
            },
            {
                "nama": "Desman Velius Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Y-FBDUoUZuEyM8VX62ds_15JEl4ttCJp",
                "kesan": "Bang Desman unik, lucu dan asik",
                "pesan": "Semangat bang milih DA/DS/DE, aku liat abang membahas itu di thread (muncul) :)",
            },
            {
                "nama": "Afriza Azmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ZuiqNNcD6o-EnrlnGId89lNAVXBXzvqg",
                "kesan": "Keliatan asik abangnya dan chill orangnya waktu wawancara",
                "pesan": "Semangat bang kuliah tetap chill ya bang",
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CJKBsQlIazwPQIzWunrE3RuzKa3JKzEu",
                "kesan": "Suka bercanda",
                "pesan": "Semangat bang ayake kuliahnya",
            },
            {
                "nama": "Caesar Ozora Alrando",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1g9GIF1lf6pTaOpBrpNOlFon6Ie3oRys0",
                "kesan": "Gemes",
                "pesan": "Semangat ya bang caesar kuliahnya selalu senyum ya bang",
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1gKa9rFIjhfHU9C2xHqTRpkpC3qKVrfJD",
                "kesan": "Tegas, Lantang",
                "pesan": "Semangat ya kak untuk kuliahnya :)",
            },
            {
                "nama": "Haikal Seventino Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_em-zIwQ6QTMvw1jedre_1op_YRJ26gG",
                "kesan": "Vokal",
                "pesan": "Semangat terus bang kuliahnya go go go",
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ckY6-MbiCEh4xJzweYhf1KA3_FB_CVke",
                "kesan": "Ramah",
                "pesan": "Semangat kak Putri kuliahnya semangat lulus cepat",
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13fxabY5a4XMZ2aa1kDw89_0yV3H6vFnX",
                "kesan": "Humble",
                "pesan": "Lulus cepat kak queenta semangat",
            },
            {
                "nama": "Azzelya Thianandry",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1nOf9tuQ1a90pesmYFXeZyRkTRHypA419",
                "kesan": "Ramah",
                "pesan": "Semangat kak kuliahnya",
            },
            {
                "nama": "Charrlindah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=10PWT3Gj3vnlIAZ8K4RAiDBdaH4v4uE_X",
                "kesan": "Cool",
                "pesan": "Semangat ya kak kuliahnya",
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fbTl9UebjN4RkX3RQP3iLEkr66OJOOf1",
                "kesan": "Energik, Semangat",
                "pesan": "Semangat bang akademiknya gass lulus cepat",
            },
            {
                "nama": "Nabila Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_es8DdvlPiDf5kPBajNaecti53zmxGHe",
                "kesan": "kakaknya keliatan humble",
                "pesan": "Semangat terus kuliahnya kak",
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1XpQ8pqyJi5Eth_Q3mH2KZye-rSU3XujP",
                "kesan": "Cool",
                "pesan": "Semangat bang kuliahnya",
            },
            {
                "nama": "Salavia Naharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GPKi0IkmZSrMZ8w_h7dHAIw2WQDC3--A",
                "kesan": "Pembaik",
                "pesan": "Semangat ya kak kuliahnya",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_psda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        kating_data = [
            {
                "nama": "Fabio Banyu Cyto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1e4mRZG0iZ2XwUd6YMMoOYB2wddIdMrrw",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah!",
            },
            {
                "nama": "Tanty Widiyastuti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fQWg5DoFSU-y_m4MS5fT2z6Dz1fLv91g",
                "kesan": "Lucu",
                "pesan": "Semangat kak kuliah go go go",
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Baik",
                "pesan": "-",
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1kJvrd-4YVmoHtEZ3GTBn9mmyTYlKdNPQ",
                "kesan": "Cool",
                "pesan": "Semangat terus kuliahnya bang",
            },
            {
                "nama": "Razin Hafid Hamdi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1a517PpssYbmMOeeb_WI5RjItrfQAuwCa",
                "kesan": "Pembaik",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Manuel Frederika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1EwkPZ3ek_Hg2uWlq7PabhXXD39VKpk5J",
                "kesan": "Pembaik",
                "pesan": "Semangat terus kuliahnya bang",
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16Du1T1SnihPg4-rpWYdq80dvnPM6Pa9W",
                "kesan": "Kakaknya sangat ramah, humble",
                "pesan": "Semangat terus kuliahnya ",
            },
            {
                "nama": "Risa Romadona",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jEdcJvh34drT4OSS_YhTfGD-BIfmqmfT",
                "kesan": "Kakaknya sangat ramah, humble,",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Vannisa Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1J0bMaBVUKBQ1aaPgJ9KOwAdESQgO3dDJ",
                "kesan": "Kakaknya sangat ramah, humble,",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Yulia Kristine Malau",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WNcLLrrMQfzEQz2Bb3Blduk6INQ1g1sC",
                "kesan": "Kakaknya sangat ramah, humble,",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Elsa Sitorus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yjqCPYEoa4UiQghRrgnHxykNFaRlXX6Z",
                "kesan": "Kakaknya sangat ramah, humble,",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-7qmH-F-mKECxPPITScuatKOL58zPbMK",
                "kesan": "Kakaknya sangat ramah, humble,",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Lovianora Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qG79Kps90ILhtZbD4ZfnbhJOnfuF2cew",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=139dVY7z6JJqlmcfO8HOS566wVQ0JJwz6",
                "kesan": "Bang semangat ya",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Sherena Florencia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1B5HpXqTLCX0zgUAsiesw8mH32iiigaAZ",
                "kesan": "Kakaknya sangat ramah, humble",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Faiza Try Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TPA311HahBn8NKcl-wuGf431pdx_vWLH",
                "kesan": "Kakaknya sangat ramah, humble, dan Astut",
                "pesan": "Semangat terus kuliah bang gas ozete",
            },
            {
                "nama": "Gathfan Nadif Ali",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VEE8za9f0K9Jp6SfMGZIrVW19iaXpqLV",
                "kesan": "Hebat",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TAAdQ0tUMFHCroe5utL06_efI-UQz6av",
                "kesan": "Lucu, baik",
                "pesan": "Semangat terus kuliahnya bang",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19ngZdIHxVT7oBo2PzPxEX-d4CNXN85we",
                "kesan": "Cerdas",
                "pesan": "Semangat terus kuliahnya bang kaleb",
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QBdvRtiTnvc_lfDwCkTj6845b5wsr-Lu",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliahnya kak",
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fYBC-Fo6IUTtRK2W8kXB4QNL2w6dkm3P",
                "kesan": "Pembaik",
                "pesan": "Semangat terus kuliahnya bang",
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jCKqOBnYOw9pUi4bJXoTRoNgSUn0cyIK",
                "kesan": "Cool",
                "pesan": "Semangat terus kuliahnya bang gas gas gas",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemen_eksternal():
        kating_data = [
            {
                "nama": "Arini Puteri Elandra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17Gye2hen1KGNmPtxlvvVKiy8wx7G0EHz",
                "kesan": "Kakaknya sangat ramah, humble!",
                "pesan": "Semangat terus kuliahnya kak",
            },
            {
                "nama": "Nabyla Sharfina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cNJgLYgBa6YjIU0ws3P7l9CW8FquBare",
                "kesan": "Kakaknya sangat ramah, humble",
                "pesan": "Semangat terus kuliahnya go go kak",
            },
            {
                "nama": "Khoirul Muttoharoh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-dVFPW8qv28FI3d6n0E8YOpN3LNjtmnJ",
                "kesan": "Lucu",
                "pesan": "Kak semangat ya hehe",
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TkSEomizmDQEVgb0TMQOKo2s8c1wTb5Z",
                "kesan": "Aktif, Positive vibes",
                "pesan": "bang semangatttt",
            },
            {
                "nama": "Indah Khairunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1BKTHkENScmbsUZMVhl0mdaX6Mav2zAIy",
                "kesan": "Humble",
                "pesan": "Kak kuliahnya cepat lulus ya",
            },
            {
                "nama": "Bima Ekayasa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1re3T-sEDE7FvYxmjxs5bfyFDZwwDJutG",
                "kesan": "Badass",
                "pesan": "Semangat ya bang hehe",
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fZXMi8dg9d3tj9LUGcQQiZ7HzPRh3Da8",
                "kesan": "Ganteng",
                "pesan": "bang kuliahnya gasskan lebih gacor",
            },
            {
                "nama": "Adinda Deswita Maharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Cp8sou7cfPhzBI0UpTjovNOa_V72LGmy",
                "kesan": "Imut",
                "pesan": "Semangat kak kuliahnya ",
            },
            {
                "nama": "Yollanda Agustina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OTn1rL6s1liA5OSxN7XlwCLvYtboZ3wh",
                "kesan": "Pembaik",
                "pesan": "Gacorkan perkuliahannya ka yolla",
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bjhY5EMVonlrpbG_SNpo2pTaGDsyYrln",
                "kesan": "Lucu",
                "pesan": "Semangat ya kak",
            },
            {
                "nama": "Alfaya rafif Abiyyi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1XaqsRAg3677vwAlS-THgqt0oErgoqwc7",
                "kesan": "Macho",
                "pesan": "Bang semangattttttt",
            },
            {
                "nama": "Asri Meilani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OMA9LVPSXawO0Hk9-dkrJsQQ1jZGtR0l",
                "kesan": "Cantik",
                "pesan": "Semangat kak gas gas",
            },
            {
                "nama": "Ahmad Rizky",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Us4fesPvE-O3azzzQIfa_hBhk9JQE7Xl",
                "kesan": "Sibuk",
                "pesan": "Semangat bang kuliahnya",
            },
            {
                "nama": "Selma Siti Aisyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1O3d5KkIJ576SerGvSGZDo4ZVoOljpqCJ",
                "kesan": "Humble",
                "pesan": "Semangat ya kak",
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19JcHCKqliOC8bwRSXFavVSZRvy5TThNi",
                "kesan": "Pembaik",
                "pesan": "Semangat kakkkk",
            },
            {
                "nama": "Fathya Intami Gusda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wIgeTPpNcuQ64zmFDWgvZUDs7yFgAEO-",
                "kesan": "Lucu",
                "pesan": "Semangat ya kak kuliahnya",
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WHFV-xjba7Zgl133JMMQBu9wGGedPRdn",
                "kesan": "Keren",
                "pesan": "Semangat kak",
            },
            {
                "nama": "Danil N Fadillah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lAewSHMuAXWL77VIJb2-mai_ld26s5jA",
                "kesan": "Gantenggg",
                "pesan": "Semangat ya kak kuliahnyaaa",
            },
            {
                "nama": "Favian Arkaanda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PL79O8yOkqhP1hPySiGjUR5qWI43FogA",
                "kesan": "Asik",
                "pesan": "Semangat ya kak kuliahnya",
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JmTlEPChTQznMOxAG6GbWKHkhNXBQ9aj",
                "kesan": "Happy",
                "pesan": "Semangat bang yazid",
            },
            {
                "nama": "Muhammad Rizaldi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WLN-RqPS1NF8jMxN9xcBgQiD4CpgESsG",
                "kesan": "Cool",
                "pesan": "Semangat banggggg",
            },
            {
                "nama": "Saskia Nova Magdalena",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19AoB4yVWEivvOW6kJ1uAkw9krL7trS-5",
                "kesan": "Imut",
                "pesan": "Semangat ya kak :)",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_eksternal()

elif menu == "Departemen Internal":
    def departemen_internal():
        kating_data = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1v-vTR0Sk5V1jGjYyOQWcsgb8XKjRMZMx",
                "kesan": "Humble, Cool, Asik",
                "pesan": "Semangat ya bang semoga semester depan Sempro",
            },
            {
                "nama": "Kharisma Mustika Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pXyMlpTvtcaQA8h5pn9h_HtD1nCLcQ5x",
                "kesan": "Pembaik",
                "pesan": "semangat kak kuliahnya",
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Lnb03ULsurSWGHiw7wP9msmrHLtoq-oI",
                "kesan": "Positif vibes, pembaik, imut, lucu, intinya mendekati sempurna",
                "pesan": "Lulus cepat ya kak Hanna bismillah tahun depan udah S2",
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1od3jRbkwpvsyIewdKuaHac1U4pUq2OCt",
                "kesan": "Abangnya humble, lucu, Pembaik, Asik, cool",
                "pesan": "Semangat terus ya bang kuliahnya, loker dong hehe",
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1n3hYnd2vt_uY-rz7JbkUBa30a2OKp147",
                "kesan": "Baik, cool",
                "pesan": "Bang Semangat kuliah ceria selalu",
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ee1BrPjkdfyhiz2rImC0O055192lFVoW",
                "kesan": "Cantik, lucu",
                "pesan": "Semangat ya kak kuliahnya :)",
            },
            {
                "nama": "Cerine Sihotang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=155LlSq96mfRYsDmBH0UlS74izKGvicbn",
                "kesan": "Lucu, Pembaik",
                "pesan": "Semangat ya kak the next kadepku",
            },
            {
                "nama": "Jaya Saputra Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ODQX0_ZElyfLPRGVcjmk-EN9-SPtaIvg",
                "kesan": "Pembaik, asik, cerdas",
                "pesan": "Semangat ya kuliahnya bang jaya pasti bisa cumlaude",
            },
            {
                "nama": "Najla Nursyifa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1is1P29Q5zz7K8x0ioPw9HYq9TBHRLtD2",
                "kesan": "Humble",
                "pesan": "Semangat terus ya kak kuliahnya",
            },
            {
                "nama": "Rozak Ramdani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fkYgH_lQxCJBz9Ufry2WH91NuYBQKrEM",
                "kesan": "Cool",
                "pesan": "Semangat bang kuliahnya",
            },
            {
                "nama": "Teresa Christiani Purba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-Z-ngKS3Fg9eEhylVn7883V6duc0IioR",
                "kesan": "Cerdas, astut, pembaik",
                "pesan": "Semangat kak kuliahnya pasti lulus cepat",
            },
            {
                "nama": "Audina Fitria",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vB6If51wjlvEwukiikZ68HuQnbKhQ2GG",
                "kesan": "Pembaik",
                "pesan": "Semangat kak kuliahnya go go go cumlaude",
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1437fixXXvq7ZTfSQOBZFAsBz7uEewVib",
                "kesan": "lucu",
                "pesan": "Semangat terus kak kuliahnya",
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1R3mi4NC-lvNcXwYLN8lDp73wYpAkKMeX",
                "kesan": "Pembaik",
                "pesan": "Semangat terus ya kak kuliahnya",
            },
            {
                "nama": "Muhammad Harvinsyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16eTVEU0rKK5_MEc3cqFqFG4otitr6lmB",
                "kesan": "Chill guy",
                "pesan": "Semangat terus bang kuliahnya :)",
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12TRVUXxc5ETdgZGyhqyHq_XGgnivAObg",
                "kesan": "Pembaik, humble",
                "pesan": "se se mangat kak kuliahnya pasti nilai tiap semester selalu ip 4",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_internal()

elif menu == "Departemen SSD":
    def departemen_ssd():
        kating_data = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cMzVQnvK7XvZJck_dZLjcRCaDM8lPZl0",
                "kesan": "Berwibawa",
                "pesan": "Semangat terus bang kuliahnya",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1eW3F2t79hxcwa2WTRTS0XH_8AFfUNkTi",
                "kesan": "Pembaik",
                "pesan": "Semangat kak kedepannya",
            },
            {
                "nama": "Afifah Fauziah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1FZkIQZy83n_Ktvy3Y2NuY60ifWPLZJFS",
                "kesan": "Cantik",
                "pesan": "Semangat ya kak kuliahnya go go go",
            },
            {
                "nama": "Anadia Carana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1J_vYi3G50umcVjew0If9vV7Cb1k1aAvR",
                "kesan": "Imut",
                "pesan": "Kak kuliahnya lulus cepat ya",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SxwHAV896iUuRD6EKG-n7_4_3hthI67O",
                "kesan": "Cool",
                "pesan": "Bang semangat ya akademiknya",
            },
            {
                "nama": "Layina Ropiqo",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1p6PKHNjXKEQ5VWskDmwMfLYXOn0WgSK7",
                "kesan": "Cantik",
                "pesan": "kak semangat ya kuliahnya hehe",
            },
            {
                "nama": "Mochammad Iqbal Az-Zahir",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1s5g9kExIOhdHa4VD1qj7ymxm7APNSQer",
                "kesan": "Ganteng",
                "pesan": "Bang akademiknya gaskan terus ya",
            },
            {
                "nama": "Talitha Justine",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CTUJgCVSXbBGaRU612Bmsi6IUww2p5Rc",
                "kesan": "imut",
                "pesan": "Kak gogo semangat kuliahnya",
            },
            {
                "nama": "Abdillah Fikri Al Pome",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MYk9zLHOasTpfVOUJ2RlYNOszLm_XZ9Q",
                "kesan": "Ganteng, Maskulin",
                "pesan": "Semangat bang kuliahnya go go go",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AguvSiBL_PsRBG-jXNuVoz-4eMOoPaxG",
                "kesan": "keren",
                "pesan": "Semangat bang kuliahnya gass",
            },
            {
                "nama": "Anggun Nita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CwqBc8wyD0Y3bKSIOZF6AOtq45g4gKhM",
                "kesan": "Cantik, Lucu",
                "pesan": "Semangat kak ngejer cumlaudenya",
            },
            {
                "nama": "Della Anisa Fitri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ZlzXg2PtTrFeA83gMg_Ea-1BDv-4yPbi",
                "kesan": "Cantik",
                "pesan": "Kak semangat kuliahnya dan nilai akademiknya",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_ssd()

elif menu == "Departemen Medkraf":
    def departemen_medkraf():
        kating_data = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1prfiJxf2DTz1-mFGsXJlZBIjzljnGwf0",
                "kesan": "Cantik, berwibawa",
                "pesan": "Semangat ya Kak",
            },
            {
                "nama": "Donna Maya Puspita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1aHGRNiHpYGOQNFsGBXNEaDKqJn-3mcS2",
                "kesan": "Lucu",
                "pesan": "Kak gass ya semangat",
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tC7dmlF_0JvvXd8Tyueoi4hGI_fsfUEs",
                "kesan": "Badass",
                "pesan": "Bang kuliahnya gass terus kasih paham",
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WKbE-g-xcyzCfx8Sxv5s7JShCsUEScu-",
                "kesan": "Cantik, lucu",
                "pesan": "Kak lulus cepat ya",
            },
            {
                "nama": "Raihana Adelia Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1zY6ARAYBn_sCBg5gfQ4u2E0iflJM0G4p",
                "kesan": "Baik",
                "pesan": "Kak.... Semangatttttt",
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UdJzeJiAijGU3w6WWz3bCheGhp_V4VV3",
                "kesan": "Pembaik",
                "pesan": "Gass cumlaude go go go :)",
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QyOcolOXG_SfPZiv9PtrhE4xdsnslBzP",
                "kesan": "Cool",
                "pesan": "Semangat kak kuliahnya",
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1M08qv9izCB-oVnd7BZMwAoRqabA_oz7-",
                "kesan": "Keren",
                "pesan": "Bang semangat ya kuliahnya",
            },
            {
                "nama": "Allisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-FJRYbDvt0vTuyQokFZAwGqbPSH2tOZV",
                "kesan": "Lucu, cantik",
                "pesan": "Semangat ya kak akdemiknya",
            },
            {
                "nama": "Alya Ramadhanti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lHS8QMLX0f2eyFfRHffOojWo38q91Tcl",
                "kesan": "Keren",
                "pesan": "Kak semangat yah",
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14XnzA5HxY2IiDfgwhKsJWcoYjmBQKx47",
                "kesan": "Pembaik",
                "pesan": "Cumlaude gak sih kak",
            },
            {
                "nama": "Difanya Husakina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1stHrURy-YzzZZVPqLajuymiVYJfyly-F",
                "kesan": "Imut",
                "pesan": "Semangat kak kuliahnya ya semoga cumlaude",
            },
            {
                "nama": "Nazlah Auliya",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1I3B1SZb592Fx7SxoFBu3-jb7MRoUuVrH",
                "kesan": "Cantik",
                "pesan": "Semangat Kak kuliahnya",
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1aQhk4z3qeJfyJN0Y8njnsx72VhN2YYjN",
                "kesan": "Lucu",
                "pesan": "Semangat bang daffa kuliahnya",
            },
            {
                "nama": "Edsel Adya Pradipta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13xQIFsoAE-INJo_h7-fKn9oCTdGM_Pvn",
                "kesan": "Hebat",
                "pesan": "Semangat bang kuliahnya",
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14A11yQlZydOSLURJ3iWgvLTDm7jY46UI",
                "kesan": "Lucu",
                "pesan": "Semangat terus kak ya semoga mimpinya terwujud",
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15mJcVlfVd4WfH0OQ-oC-CfU9j5Q_XWEh",
                "kesan": "Pembaik!",
                "pesan": "Semangat terus kuliahnya kak gas cumalude",
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15-Dj6tV-jHOTLegb7kFz1xBpNjszpmtK",
                "kesan": "Baik",
                "pesan": "Semangat terus kuliahnya kak gas lulus cepat"
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_medkraf()

elif menu == "Departemen MINBAK":
    def departemen_minbak():
        kating_data = [
            {
                "nama": "Kevin Antonio Junior",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11ZPFbEZT-_znYmtoFvllkzDmtjZZqdT6",
                "kesan": "Abangnya keliatan berwibawa",
                "pesan": "Semangat bang akademiknya",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1A3A7pyD9waaN66tz8MjOk7CNjkmQcm9j",
                "kesan": "cantik, ramah, pembaik",
                "pesan": "Semangat ya kak kuliahnya semangattttttttttttttt :)",
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16fTwSHRbmS0lSd780Pxoi20njVL3PgZT",
                "kesan": "cool, santuy",
                "pesan": "Semangat bang akademiknya pasti bisa cumlaude",
            },
            {
                "nama": "Muhammad Ridwan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1STB7xsmVyfXXaQQJ-rwWTG_haUOM8s8s",
                "kesan": "Pembaik, baik, care, hebat, humble",
                "pesan": "Semangat bang kuliahnya gass gass",
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1a-45LetmQW4smfpvnV3eo74dvBdf08Qh",
                "kesan": "humble",
                "pesan": "Semangat kak kuliahnya",
            },
            {
                "nama": "Dafa Elpriza",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=137Jr_3m5OTjNoUgvl2WH9NA_2xNeJ9me",
                "kesan": "Cool",
                "pesan": "Semangat bang kuliahnya",
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SMOG6rkJLwrFkUJoo6ee-0lEpoJSGJcd",
                "kesan": "Keren",
                "pesan": "semangat kak kuliahnya pasti lulus cepat",
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pco55fiikJLgWRTr8YWgUwdTRue-tzVQ",
                "kesan": "cool",
                "pesan": "Semangat bang kuliahnya pasti bisa cumlaude",
            },
            {
                "nama": "Juwita Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13UecXpKco2LOfCN-qCZeYBzKKFZUDzZl",
                "kesan": "pembaik",
                "pesan": "Semangat ya kak kuliah pasti bisa lulus dan menggapai impian",
            },
            {
                "nama": "Andra Ilham Bintang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lSgP7u2XxjJhJYAfwqIWJjrHPCmuHEvv",
                "kesan": "Keren, asik, pembaik, jago basket",
                "pesan": "Semangat bang, akademik juga harus gacor yakh",
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vEivQoIkyBiq14ZSAXk5HYxYU-jQXTNN",
                "kesan": "cool",
                "pesan": "Semangat bang gaskan kuliahnya",
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13Fq-XAk6vNKRcxjnX2HgGbfadJrAS1WE",
                "kesan": "baik",
                "pesan": "Semangat kak kuliahnya",
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18sci74xAan5oYpcTg_ROpw7rkVT280Cv",
                "kesan": "pembaik",
                "pesan": "Semanngat kak kuliah go go lulus tepat waktu",
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18c7IP5KuemJ_tQxGzxIyLaC9xQcygjzu",
                "kesan": "lucu, imut",
                "pesan": "Semangat kak akademiknya juga pasti bisa cumlaude",
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OAx4bEImsVtgSCg69fjSBK8Oxy34BHor",
                "kesan": "kanim, ramah",
                "pesan": "Semangat bang kanimku semoga impianmu tergapai go go go :)",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_minbak()
