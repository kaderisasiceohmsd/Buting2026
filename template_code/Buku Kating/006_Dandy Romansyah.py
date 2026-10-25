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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hixmRQf5WkVazX2JK_uyNJDanrzN1VQ0",
                "kesan": "Bang Ginda yang pertama kali bertemu dengan Saya saat verifikasi berkas.",
                "pesan": "Semangat terus bang Ginda kuliahnya, semoga hidup akan terus berjalan ya bang.",
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qu7sYIcDplg67ekju7CS6MNIW0PYHCNm",
                "kesan": "Bang Aqil orangnya humble, fun, dan ber-aura serius banget.",
                "pesan": "Do your best bang Aqil, semoga kuliahnya lancar dan lulus tepat waktu ya bang.",
            },
            {
                "nama": "Efi Defiyati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1g2UsuQpvpC1j7pFNdjd1CqCarBuZS66k",
                "kesan": "Kak Efi selalu muncul di top of mind saya misal ditanya tentang ke Sekretariatan.",
                "pesan": "Semnagat terus kak Efi kuliahnya, semoga lulus tepat waktu ya kak.",
            },
            {
                "nama": "Qois Olifio",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_9HtA2aRZ8mqSIvTsE7ZE8OGyMeyVU0u",
                "kesan": "Bang Qois juga menjadi top of mind Saya, karena jarang Laki-Laki yang memangku jabatan Sekretaris.",
                "pesan": "Semangat terus bang Qois kuliahnya, semoga jalannya selalu dipermudahkan ya bang.",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1C5S5pUrof4y3qnsu_GoFoIYz18-cCX2o",
                "kesan": "Kak Hafsa orangnya humble, fun, dan charming banget.",
                "pesan": "Cinta banget dengan positive vibes nya, semangat terus Kak Hafsa.",
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hNRjmXOncd-hOeqc79FtxHQWIJB0yrBM",
                "kesan": "Kak Luthfia keren dan fun banget pembawaannya.",
                "pesan": "Cinta banget dengan positive vibes nya Kak Luthfia, semangat terus ya Kak!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        kating_data = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SaJ7ZNPVFadjwwlgPfGSsFlDiSpFRAAR",
                "kesan": "Bang Ridho humble, playfull, dan charming positive vibes banget",
                "pesan": "Semoga dipermudahkan segalanya, semangat terus bang Ridho kuliahnya",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hMYya9Olo5DcmvFcxlpNhUAjUw8jjMDI",
                "kesan": "Kak Juesi cantik, cute, dan flowy banget pembawaannya",
                "pesan": "Semangat kak Juesi Imut kuliahnya, semoga lulus tepat waktu ya kak",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AHZe-Olev2nMcFxUfXNBfGHYP5mol0a2",
                "kesan": "Bang Dharu keren banget orangnya, cheerful dan vibesnya positif banget",
                "pesan": "Semangat bang Dharu untuk segala halnya, doa yang terbaik untuk bang Dharu.",
            },
            {
                "nama": "Givaro Ananta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1gFXv2rPWE_x_RZNileT9bc2aIFmF5cSd",
                "kesan": "Bang Givaro keren, cool, dan humble banget orangnya",
                "pesan": "Semangat terus bang Givaro buat kuliahnya, semoga lulus tepat waktu ya bang",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1zGWtJ9vEGxBqucijis1fHkD29xQemH1r",
                "kesan": "Kak Monica cantik, humble, dan adem banget vibes orangnya",
                "pesan": "Semangat terus ya kak Monica kualiahnya, semoga lulus tepat waktu ya kak",
            },
            {
                "nama": "Gh Mikael Niko A S",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16a_basrR64sJNPViTR8Ye28whFfKwJTD",
                "kesan": "Bang Niko looks cool dan berwibawa banget orangnya",
                "pesan": "Selalu semangat terus kuliahnya bang Niko, semoga tantangan yang dihadapi selalu dimudahkan ya bang",
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GZOwM6sbGafcFP53AyRSKPWowcrbZvJ-",
                "kesan": "Kak Siti humble, fun, dan vibesnya positif banget",
                "pesan": "Semangat kuliahnya ya kak Siti, semoga harinya selalu seru dan lucu.",
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ERK4KMBgClCi7PYpd0Dj3uSZrmWOZvF2",
                "kesan": "Kak Nisa cute dan cantik banget.",
                "pesan": "Semangat terus ya kak Nisa kuliahnya, semoga harinya selalu menyenangkan",
            },
            {
                "nama": "Hani Qurrota Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HwsQ9006W3oyPfFkOzNrj6fjbW8RedQE",
                "kesan": "Kak Hani imut dan cantik banget",
                "pesan": "Semangat terus ya kak Hani kuliahnya, semoga dijauhkan dari rintangan yang sulit",
            },
            {
                "nama": "Jeremia Halim",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ZTbcu2psLWi_pRbrFtDzRcI3qIDDCYHj",
                "kesan": "Bang Jeremia keren banget waktu tampil di First Gathering 2025",
                "pesan": "Semangat terus Bang Jeremia kuliahnya, semoga lulus tepat waktu ya bang",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1NmTEWJ1JoyEpF6-ysm4h-rOLQtWLtVAa",
                "kesan": "Bang Jona kakak tingkat pertama kali yang mutualan di instagram",
                "pesan": "Semangat terus Bang Jona kuliahnya, semoga kalendernya selalu berwarna bang",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14Gd7ZUO2spWc3ixW5xgD4yfFHpSkfYQ0",
                "kesan": "Kak Sekar cantik dan vibesnya anggun banget",
                "pesan": "Semangat terus ya kak Sekar kuliahnya, semoga hari-harinya selalu berbunga-bunga",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_mnMLNG7YZXb0FFaenWWXxd_EwwTEtFU",
                "kesan": "Kak Nashwa cantik, imut, lucu, dan menggemaskan banget",
                "pesan": "Semangat terus ya kak Nashwa kuliahnya, semoga selalu bahagia dan terlihat seperti bunga",
            },
        ]
        display_kating(kating_data, departemen=menu)
    baleg()

elif menu == "Senator":
    def senator():
        kating_data = [
            {
                "nama": "Fathinah Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1b-VFO15OiVXSRw8guOH6iRrWmM9G-BIL",
                "kesan": "Kak Azizah looks independent women dan strong women",
                "pesan": "Semangat ya kak Azizah kuliahnya, semoga selalu dipermudah dan menyenangkan ya kak",
            },
            {
                "nama": "Helmy Surya Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wzG0IJ0zFsFOsC3M7vqqUqOhF7RpbkBX",
                "kesan": "Bang Helmy salah satu kakak tingkat yang lucu dan asik banget orangnya",
                "pesan": "Semangat terus ya bang Helmy kuliahnya, semoga hari kamu selalu lucu dan menyenangkan ya bang",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1J5nyEzVI2jAVaXKkYVHRhlY1cdF_yjlM",
                "kesan": "Kak Hana cute, baik, lucu, dan humble banget",
                "pesan": "Semangat terus kuliahnya ya kak Hana, semoga selalu bahagia dan menyenangkan ya kak",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VSxbHmqRPTYXQuACbqG9BLLyxKGQQ4c4",
                "kesan": "Kak Nadya mudah banget di ajak bicara dan friendly banget orangnya",
                "pesan": "Semangat terus kuliahnya kak Nadya, energi positifnya jangan padam ya kak",
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1o_o9ab-Zr9Pnh5MsihwZvFgJ33GB2FYi",
                "kesan": "Bang Fernando asik, humble, dan easy going banget orangnya",
                "pesan": "Semangat kuliahnya ya bang Fernando, semoga harinya selalu menyenangkan dan jangan menyerah!",
            },
            {
                "nama": "Suci Aulia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QA2wUuruSx2FkziSLLis6ztG-bSiiray",
                "kesan": "Kak Suci fun banget kalo bicara bareng, dan humble banget orangnya",
                "pesan": "Semangat kuliahnya ya kak Suci, semoga selalu bahagia dan menyenangkan ya kak",
            },
            {
                "nama": "Wielman Itolo Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1B0IZ3HJn_0u5pW1rc76xgHTDFtOnhNHw",
                "kesan": "Bang Wielman terlihat chill secara pembawaaan dan easy going banget orangnya",
                "pesan": "Semangat kuliahnya ya bang wielman, semoga harinya selalu menyenangkan dan jangan menyerah!",
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_yvvQ2MpHvHdbvl-V5LPWws1HsnAhx7h",
                "kesan": "Kak Aqila lucu, imut, baik, dan energi positifnya selalu terpancar banget",
                "pesan": "Semangat terus ya kuliahnya kak Aqila dan selalu tunjukkan energi positif kakak",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WFjXfxrNRhFRjbQwaFG8IG6_G_sLB0gW",
                "kesan": "Bang Hazel terlihat mirip seperti rapper underground dari JXL namanya Nozok",
                "pesan": "Semangat terus kuliahnya bang Hazel, semoga harinya selalu berseri-seri ya bang",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YVu_pc9y6Q_il5ASWPVCobULp7SJRLzE",
                "kesan": "Kak Dwi ramah, humble, dan easy going banget orangnya",
                "pesan": "Semangat terus kuliahnya kak Dwi, semoga harinya selalu menyenangkan",
            },
        ]
        display_kating(kating_data, departemen=menu)
    senator()

elif menu == "Departemen PSDA":
    def departemen_psda():
        kating_data = [
            {
                "nama": "Arienta Khusnul Ananda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dn23WJ_HeN97GVJ0A3DSAgV8L04VLR3q",
                "kesan": "Kak Arienta ramah, humble, dan cool banget orangnya",
                "pesan": "Semangat ya kak Arienta, semoga harinya selalu indah dan cantik seperti bunga mawar merah",
            },
            {
                "nama": "Vany Salsabila Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16B7Eba4sP2tXv4mHFJRjbl91BS6har0W",
                "kesan": "Kak vany looks cute, humble, dan seperti light fury dari how to train your dragon",
                "pesan": "Semangat terus ya kak Vany, semoga harinya selalu menyenangkan dan indah",
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1iWt3kbziynzqNN63gWiENKuDO-p_EWAU",
                "kesan": "Bang Nobel looks lone wolf, berkharisma, dan dingin tetapi tidak kejam",
                "pesan": "Semangat terus bang Nobel kuliahnya dan terima kasih banyak atas ilmunya bang, semoga harinya selalu menyenangkan",
            },
            {
                "nama": "Desman Velius Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17ozKQ_OIRjvRtxYMZzlCBHvv0PrDll--",
                "kesan": "Bang Desman unik, lucu, dan menyenangkan banget orangnya",
                "pesan": "Semangat bang Desman kuliahnya, semoga harinya selalu lucu dan menyenangkan seperti Charlie Chaplin",
            },
            {
                "nama": "Afriza Azmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14rbaYoXhzaw1PNob5khL9-Uo-YmFnFea",
                "kesan": "Bang Azmi fun, humble, dan easy going banget orangnya",
                "pesan": "Semangat bang Azmi kuliahnya, semoga harinya selalu menyenangkan",
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12-0JwBTOUpQhvRTgSEXyZkDxpnbx6Qtd",
                "kesan": "Bang Ayake humble, lovely, dan easy going banget orangnya",
                "pesan": "Semangat bang Ayake kuliahnya, semoga harinya selalu menyenangkan seperti film Up",
            },
            {
                "nama": "Caesar Ozora Alrando",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19Yh4QuJggcxwl0zf3IClrrA0pjm-KJZW",
                "kesan": "Pertama kali melihat Bang Caesar saat menjadi Komisi Kedisiplinan di PPLK 2025",
                "pesan": "Semangat kuliahnya bang Caesar, semoga harinya selalu fun dan penuh tawa",
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1RjmkMMyvMqObn5idSweakjkVRLAmjBmT",
                "kesan": "Kak Euodia 1 of independent women terkeren yang aku tahu, humble, dan anggun orangnya",
                "pesan": "Semangat kuliahnya kak Euodia, semoga harinya se-indah seperti bunga mawar merah",
            },
            {
                "nama": "Haikal Seventino Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MtiToQlK5XnDYbZI34sgEHGoWOyDchv9",
                "kesan": "Bang Haikal berkarisma, humble, dan cool banget orangnya",
                "pesan": "Semangat terus kuliahnya bang Haikal, semoga harinya selalu menyenangkan",
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AyZAXGdrSndPEY0YRGQ3OITCux8Xpx-N",
                "kesan": "Kak Putri sesuai dengan namanya seperti Tuan Putri Kerajaan",
                "pesan": "Semangat kak Putri kuliahnya, semoga harinya selalu menyenangkan dan indah seperti Tuan Putri Kerajaan di film Tangled",
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YJ7nZKTfwWzZKanV-HNBcdfo6xzN29mn",
                "kesan": "Kak Queenta humble, fun, dan easy going banget orangnya",
                "pesan": "Semangat terus kak Queenta kuliahnya, semoga harinya selalu menyenangkan",
            },
            {
                "nama": "Azzelya Thianandry",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_kcHZT763buoUlfW2cBwv38gS7qZhNy6",
                "kesan": "Kak Azzelya humble, fun, dan cute banget orangnya",
                "pesan": "Semangat kak Azzelya kuliahnya, semoga harinya selalu menyenangkan",
            },
            {
                "nama": "Charrlindah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18F6KXtfjhafkQ5Wc7mix4CduaD0An0TP",
                "kesan": "Kak Charrlindah humble, anggun, camtik, dan easy going banget orangnya",
                "pesan": "Semangat terus kak Charrlindah kuliahnya, semoga harinya selalu menyenangkan dan indah",
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SQr6knheKsa3CiLJ0MZY9VgHRq6MeCea",
                "kesan": "Bang Jeremi menyenangkan, imup, keren dan easy going banget orangnya",
                "pesan": "Semangat bang Jeremi kuliahnya, semoga harinya selalu menyenangkan dan penuh tawa",
            },
            {
                "nama": "Nabila Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1LdqJXR_VssOWSFE-0Jyo78zFx7IAMko7",
                "kesan": "Kak Nabila cute, cantik, dan anggun orangnya",
                "pesan": "Semangat terus kuliahnya kak Nabila, semoga harinya selalu menyenangkan dan indah",
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QbEYQnZ4trFMHiCYrMzJ34aetNJmV8be",
                "kesan": "Bang Rafli memiliki kesamaan dengan saya seperti menyukai banyak jenis genre musik dan film",
                "pesan": "Semangat bang Rafli kuliahnya, semoga harinya selalu menyenangkan seperti album musik Heaven or Las Vegas dari Cocteau Twins",
            },
            {
                "nama": "Salavia Naharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Jg5uHj3vvVBynbEylXgiEw1nxCouVBHQ",
                "kesan": "Kak Salavia cute, imut, camtik, dan menyenangkan banget orangnya",
                "pesan": "Semangat ya kak Salavia kuliahnya, semoga harinya selalu menyenangkan dan indah",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_psda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        kating_data = [
            {
                "nama": "Fabio Banyu Cyto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Tanty Widiyastuti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Razin Hafid Hamdi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Manuel Frederika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Risa Romadona",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Vannisa Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Yulia Kristine Malau",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Elsa Sitorus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Lovianora Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Sherena Florencia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Faiza Try Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gathfan Nadif Ali",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemen_eksternal():
        kating_data = [
            {
                "nama": "Arini Puteri Elandra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Nabyla Sharfina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Khoirul Muttoharoh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Indah Khairunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bima Ekayasa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Adinda Deswita Maharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Yollanda Agustina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Alfaya Abiyyi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Asri Meilani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ahmad Rizky",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Selma Siti Aisyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Fathya Intami Gusda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Danil N Fadillah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Favian Arkaanda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Rizaldi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Saskia Nova Magdalena",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Afifah Fauziah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anadia Carana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Layina Ropiqo",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Mochammad Iqbal Az-Zahir",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Talitha Justine",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Abdillah Fikri Al Pome",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anggun Nita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Della Anisa Fitri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_ssd()

elif menu == "Departemen Medkraf":
    def departemen_medkraf():
        kating_data = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Donna Maya Puspita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Raihana Adelia Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Allisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Alya Ramadhanti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Difanya Husakina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Nazlah Auliya",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Edsel Adya Pradipta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11ZPFbEZT-_znYmtoFvllkzDmtjZZqdT6",
                "kesan": "-",
                "pesan": "-",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1A3A7pyD9waaN66tz8MjOk7CNjkmQcm9j",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16fTwSHRbmS0lSd780Pxoi20njVL3PgZT",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Ridwan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1STB7xsmVyfXXaQQJ-rwWTG_haUOM8s8s",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1a-45LetmQW4smfpvnV3eo74dvBdf08Qh",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Dafa Elpriza",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=137Jr_3m5OTjNoUgvl2WH9NA_2xNeJ9me",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SMOG6rkJLwrFkUJoo6ee-0lEpoJSGJcd",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": ")",
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pco55fiikJLgWRTr8YWgUwdTRue-tzVQ",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Juwita Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13UecXpKco2LOfCN-qCZeYBzKKFZUDzZl",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Andra Ilham Bintang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lSgP7u2XxjJhJYAfwqIWJjrHPCmuHEvv",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vEivQoIkyBiq14ZSAXk5HYxYU-jQXTNN",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13Fq-XAk6vNKRcxjnX2HgGbfadJrAS1WE",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18sci74xAan5oYpcTg_ROpw7rkVT280Cv",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18c7IP5KuemJ_tQxGzxIyLaC9xQcygjzu",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OAx4bEImsVtgSCg69fjSBK8Oxy34BHor",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_minbak()
