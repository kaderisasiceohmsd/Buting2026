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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1iOtNzlP5aodOf_kIGR2XJgKSiBxSi9b8",
                "kesan": "Bang Fabio humble, inspired, dan easy going banget orangnya",
                "pesan": "Semangat terus kuliah dan terima kasih atas inspirasi & motivasi nya bang",
            },
            {
                "nama": "Tanty Widiyastuti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WWuhLvu-12_magaWKG8TYc6WJKbDWdBd",
                "kesan": "Kak Tanty sangat ramah, humble, menyenangkan, dan menginspirasi",
                "pesan": "Semangat terus kuliahnya Kak Tanty, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1anOT7U-xPwWo1bHlyDq724xb3xc6KRge",
                "kesan": "Bang Fadil yang Saya tahu sangat ramah, humble, dan menginspirasi",
                "pesan": "Terima kasih atas inspirasi & motivasi nya bang Fadil.",
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HI8l3QOw98I-xyoliGbO6SnU0JjZ6RtR",
                "kesan": "Bang Akeyla sangat ramah, humble, dan menginspirasi",
                "pesan": "Semangat terus kuliahnya bang Akeyla, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Razin Hafid Hamdi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1S9w0Zw6GuoShwbTi3ZF7M7I9Re47Yu_2",
                "kesan": "Bang Razin sangat ramah, humble, cool, dan menginspirasi",
                "pesan": "Semangat terus kuliahnya bang Razin, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Manuel Frederika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1d0WhnoFzxsRgtU3TLoyDxNfEB73NZpUJ",
                "kesan": "Bang Manuel sangat ramah, humble, dan menginspirasi",
                "pesan": "Semangat terus kuliah nya bang Manuel, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13ajkK9Z457krjI01mVJBprX5EWc0bU-o",
                "kesan": "Kak Viola cantik, anggun, dan menginspirasi",
                "pesan": "Semangat terus kuliahnya kak Viola, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Risa Romadona",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rr6b6A1VVnLNhawv9ur9xEryLqykdbJe",
                "kesan": "Kak Risa sangat ramah, imut, humble, dan menginspirasi",
                "pesan": "Semangat terus kuliahnya kak Risa, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Vannisa Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1X68pXphiqDoxY6FYVR6Ncp1q4O7B6-iP",
                "kesan": "Kak Vannisa sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya kak Vannisa, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Yulia Kristine Malau",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1NdPdBQVnsMZe1vZPfLpdJUaNFTQnGHjk",
                "kesan": "Kak Yulia sangat ramah, cantik, imut, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya kak Yulia, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Elsa Sitorus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19Frs22BfPanq84m7z3kOc65MYK1u7Od5",
                "kesan": "Kak Elsa sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya kak Elsa, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1eHXxbiIdGT-wsI9qWS-UE7YE4lok--MU",
                "kesan": "Kak Fadya sangat ramah, baik, dan menginspirasi",
                "pesan": "Semangat terus kuliahnya kak Fadya, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Lovianora Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mGhtPlkYUsUu0w2LQVMRpKTDYTB_PAG1",
                "kesan": "Kak Lovi ramah banget, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya Kak Lovi, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PDvOUdRO5zMXquJY0C4-VQozuQgUdWnk",
                "kesan": "Bang Alsi baik, ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya bang Alsi, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Sherena Florencia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1x47OAW_lItyp4jjwEM_buieZmM1PKAH_",
                "kesan": "Kak Sherena imut, ramah, cantik, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya kak Sherena, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Faiza Try Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1u8XYJwzQ6hzfN_BBvCJabrhzZOXoxWaH",
                "kesan": "Kak Faiza imut, ramah, baik, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya ka Faiza, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Gathfan Nadif Ali",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AkcWVrfvzzxdMebn4erbhkGvKJHsn57z",
                "kesan": "Bang Gathfan cool, fun, menyenangkan, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya bang Gathfan, semoga selalu menyenangkan dan menginspirasi banyak orang",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1kUwL69O45Sya6Q69gO_ouzOoLJCRP37Z",
                "kesan": "Bang Hafidz ramah, easy going, imut, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya bang Hafidz, semoga selalu menyenangkan dan terima kasih banyak atas insight yang telah diberikan",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Zg4ZBrlX1Um_XyzmhQe84_lKIKhROiFL",
                "kesan": "Bang Kaleb seorang putra kerajaan yang telah menjadi tutor Saya di Matkul ALE",
                "pesan": "Semangat terus kuliahnya bang Kaleb, semoga selalu menyenangkan dan terima kasih banyak atas insight yang telah diberikan",
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1W3tzvTMUefPfA7Lj7scdwp1alK-JlsUI",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1prMQN4asH7xE1YMNYPIjJ7Zyyy4ufSCb",
                "kesan": "Bang Syafiqul ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliahnya bang Syafiq, semoga selalu menyenangkan dan terima kasih banyak atas insight yang telah diberikan",
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15udq7oow3eS42QexQWKVF6AAL4aRF3Au",
                "kesan": "Bang Henry baik, coolest person, humble, dan menginspirasi",
                "pesan": "Semangat terus kuliahnya bang Syafiq, semoga selalu menyenangkan dan terima kasih banyak atas insight yang telah diberikan",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemen_eksternal():
        kating_data = [
            {
                "nama": "Arini Puteri Elandra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1RwPasyICvDURkl5Z5j1qLZKgYIKtKCqc",
                "kesan": "Kak Arini fun, menyenangkan, dan alpha women terkeren",
                "pesan": "Semangat terus kuliahnya kak Arini, semoga selalu menyenangkan dan memiliki hari yang indah",
            },
            {
                "nama": "Nabyla Sharfina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1v9EowBgyGfGz6ur48XQbVGtPqR8JPSyb",
                "kesan": "Kak Nabyla sangat ramah, cantik, imut dan menyenangkan",
                "pesan": "Semangat terus kuliahnya kak Nabyla, semoga harinya selalu menyenangkan dan berwarna seperti pelangi",
            },
            {
                "nama": "Khoirul Muttoharoh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-T9mGoCu4l9_hgzM7uA7N-40ViFLaykE",
                "kesan": "Kak Khoirul saat pertama kali mendengar namanya aku kira seorang lelaki, ternyata kakak cantik dan imut",
                "pesan": "Semangat terus kuliahnya kak Khoirul, semoga harimu selalu memberikan energi positif",
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ZRvOxjPlFXoaqw3aNjtUy1Q_XxSMpOO4",
                "kesan": "Bang Adit pertama kali melihat beliau di Verbek dan saya mengira beliau sesama angkatan 25 yang sedang verbek",
                "pesan": "Semangat terus kuliahnya bang Adit, semoga harimu selalu menyenangkan dan selalu menebar senyuman yang manis",
            },
            {
                "nama": "Indah Khairunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AnTiHoDq3X7svWk_jpum3QE_EM3ipJ6k",
                "kesan": "Kak Indah sangat ramah, menyenangkan, dan memiliki pancaran aura positif dari dirinya",
                "pesan": "Semangat terus kuliahnya kak Indah, semoga harimu seindah namamu",
            },
            {
                "nama": "Bima Ekayasa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1oogWBZbityhZW9wFtL6bqBVwRKoXT7zD",
                "kesan": "Bang Bima baik pake banget, humble, dan fun",
                "pesan": "Semangat terus kuliahnya bang Bima, semoga selalu menebarkan vibes positif dimanapun dan kapanpun",
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jOfMFqo0sih81-DorFBXC03WP0zX-Ea5",
                "kesan": "Bang Bimo easy talking, menyenangkan, dan ramah",
                "pesan": "Semangat terus kuliahnya bang Bimo, semoga harinya selalu menyenangkan",
            },
            {
                "nama": "Adinda Deswita Maharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1sKLmEpkhtWXvH29-iqTZQiaouDeuzjvd",
                "kesan": "Kak Adinda imut, menyenangkan, dan imut",
                "pesan": "Semangat terus kuliahnya kak Adinda, semoga harinya selalu menyenangkan dan indah",
            },
            {
                "nama": "Yollanda Agustina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JRjg0KR80_4xaZIgenyKXnRT9bmniLMl",
                "kesan": "Kak Yollanda ramah, senyumnya berkilau, dan menyenangkan",
                "pesan": "Semangat terus kuliahnya kak Yollanda, semoga harinya selalu menyenangkan dan indah",
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14i5RVM6qHjLRua0A-lyXklfa8vXds-mL",
                "kesan": "Kak Riska ramah, fun, imut dan menyenangkan",
                "pesan": "Semangat terus kuliahnya kak Riska, semoga harinya selalu menyenangkan dan indah",
            },
            {
                "nama": "Alfaya Abiyyi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rUf2vMkGbRuxtdper-GSDhHOuqa-SrQm",
                "kesan": "Bang Alfa abang nim Saya sesama nim 006",
                "pesan": "Semangat terus kuliahnya bang Alfa, semoga harimu selalu menyenangkan dan gembira",
            },
            {
                "nama": "Asri Meilani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1T2__RK4J-KcPw4QK1CEyBrhQ1DgxMvW5",
                "kesan": "Kak Asri baik, menyenangkan, dan memberikan positif vibes",
                "pesan": "Semangat terus kuliahnya kak Asri, semoga harinya selalu menyenangkan",
            },
            {
                "nama": "Ahmad Rizky",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1r5vQuQ4LHQL2nljPSU_1V3NJegWjZITt",
                "kesan": "Bang Ahmad ramah, dan menginspirasi! Satu kata yang menggambarkan bang Ahmad yaitu Bergelora",
                "pesan": "Semangat terus kuliahnya bang Ahmad, semoga harinya selalu menyenangkan dan terima kasih sudah membela banyak nya aspirasi",
            },
            {
                "nama": "Selma Siti Aisyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=198YOE9x6j3O3AslCMZ_uZAVBUgwTsZdT",
                "kesan": "Kak Selma ramah, senyumnya manis, dan menyenangkan",
                "pesan": "Semangat terus kuliahnya kak Selma, semoga harinya selalu menyenangkan",
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Evnz9wSB-gk-qkhIBEK1EfT1R4Jjenz0",
                "kesan": "Kak Ashila imut, cantik, menyenangkan, dan senyumnya manis",
                "pesan": "Semangat terus kuliahnya kak Ashila, semoga harinya manis seperti senyumannya",
            },
            {
                "nama": "Fathya Intami Gusda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bS0FIT-hWx1-LF1nvbVSOAeYA7RRBQJ0",
                "kesan": "Kak Fathya menyenangkan, ramah, dan imut",
                "pesan": "Semangat terus kuliahnya kak Fathya, semoga harinya menyenangkan dan indah",
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1v9YuP2mhPuTeDVuSxwf3BjvevUiX5UBN",
                "kesan": "Kak Tarisya ramah, humble, dan menyenangkan",
                "pesan": "Semangat terus kuliahnya kak Tarisya, semoga harinya menyenangkan dan indah",
            },
            {
                "nama": "Danil N Fadillah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16LtrSKC1AaOeKygRlLIQ1Arr_9qfjlHc",
                "kesan": "Bang Danil ganteng, ganteng, dan oppa korea",
                "pesan": "Semangat terus kuliahnya bang Danil, semoga harinya selalu ganteng kayak orangnya",
            },
            {
                "nama": "Favian Arkaanda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11JvtDIBwgWSlTEPhHUCV4OmUGqnvkOZD",
                "kesan": "Bang Favian merupakan teman dekat dari mentorku yaitu kak Farhana",
                "pesan": "Semangat terus kuliahnya bang Favian, semoga hari mu seindah bunga sakura yang sedang bersemi",
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17VPQUrkIdyfj0o2TAhLx6ItMdtayC9pv",
                "kesan": "Bang Yazid ramah, menyenangkan, dan charming",
                "pesan": "Semangat terus kuliahnya bang Yazid, semoga harinya selalu membahagiakan",
            },
            {
                "nama": "Muhammad Rizaldi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1W7irZSgbCNzpnt3sIrcS6ZC7p_dR6WnG",
                "kesan": "Bang Zaldi sangat ramah, menyenangkan, menginspirasi, dan spirit nya yang mengembara",
                "pesan": "Semangat terus kuliahnya bang Zaldi, semoga harinya selalu bersinar seperti bunga matahari",
            },
            {
                "nama": "Saskia Nova Magdalena",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PrFu2wftBk3p8GrTw9F9jC3eD86SDQ1Q",
                "kesan": "Kak Saskia senyumnya manis, menyenangkan, dan ramah",
                "pesan": "Semangat terus kuliahnya kak Saskia, semoga harinya seterang bulan purnama dimalam hari",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_eksternal()

elif menu == "Departemen Internal":
    def departemen_internal():
        kating_data = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AYk7YnabUme0BdE5Fd5zNDRjSsCs63Mk",
                "kesan": "Bang Haikal asik banget dan membuat Saya menjadi tertarik untuk bergabung kedalam departemen internal",
                "pesan": "Semangat kuliahnya bang Haikal, doa yang terbaik buat abang, dan semoga harinya selalu menyenangkan",
            },
            {
                "nama": "Kharisma Mustika Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HbQGqIbAxbryyslzkitg4WUTcTYO3dc8",
                "kesan": "Kak Kharisma cute dan imut banget",
                "pesan": "Semangat terus kuliahnya kak Kharisma, semoga harinya selalu menyenangkan dan indah",
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ZZP-fLuNHimiM1XMhstttkaE1h3vh3xj",
                "kesan": "Kak Hanna fun, menyenangkan, cantik, imut, dan positive vibes",
                "pesan": "Semangat terus kuliahnya kak Hanna, semoga selalu menyilaukan hari dengan senyumannya",
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1j--G0rhGaVIZZgdNJzGZ7e5CtdKjpvU3",
                "kesan": "Bang Hanif humble, lucu, menyenangkan, dan cool banget",
                "pesan": "Semangat terus ya bang Hanif kuliahnya, semoga harinya selalu menyenangkan kapanpun dan dimana pun",
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QhIHnH-RwmcwNhZL8ZYqQCWSP5h9_doD",
                "kesan": "Bang Farhan terlalu dingin untuk dipandang, pokoknya keren dan cool banget",
                "pesan": "Semangat terus kuliahnya bang Farhan, semoga harinya selalu menyenangkan dan menggebu-gebu",
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jv-Otn0-N1_t_kdUVsS-mxVQTCGNvj-U",
                "kesan": "Kak Aisyah lucu, imut, dan menggemaskan",
                "pesan": "Semangat terus ya kak Aisyah kuliahnya, semoga harinya selalu bersinar seperti senyuman kakak",
            },
            {
                "nama": "Cerine Sihotang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lXYg3exCKQOzmpWXJI0NkNSLXQBO3A5T",
                "kesan": "Kak Cerine baik hati, ramah, lucu, imut, dan menggemaskan",
                "pesan": "Semangat terus kuliahnya kak Cerine, semoga harimu selalu indah seperti pulau dewata",
            },
            {
                "nama": "Jaya Saputra Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SYXv5B35P8Qq9-xZTU9qr2XscNFF0xBw",
                "kesan": "Bang Jaya mirip bule ganteng dan pintar banget",
                "pesan": "Semangat ya kuliahnya bang Jaya, semoga rezeki dan kesehetan selalu menyertaimu",
            },
            {
                "nama": "Najla Nursyifa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1U7jl79j8KN9n4UgJBPnMHy3W0fDQThvN",
                "kesan": "Kak Najla cantik, imut, dan menyenangkan",
                "pesan": "Semangat terus ya kak Najla kuliahnya, semoga harinya selalu menyenangkan dan indah",
            },
            {
                "nama": "Rozak Ramdani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1v4amXtyY6k0QGdzG39Y4Q2iT_doffcYa",
                "kesan": "Bang Rozak menyenangkan, cool, dan humble",
                "pesan": "Semangat bang Rozak kuliahnya, semoga harinya selalu menyenangkan dan indah",
            },
            {
                "nama": "Teresa Christiani Purba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UjQ3LUqXWxcTn-ZVU8lLA3KPnL0Dnrav",
                "kesan": "Kak Teresa cantik, senyumannya manis, dan menyenangkan",
                "pesan": "Semangat kak Teresa kuliahnya, semoga harinya selalunya menyenangkan dan indah",
            },
            {
                "nama": "Audina Fitria",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1X-6CfWpJDrBaZAZnubu3rEboEpsXcQRe",
                "kesan": "Kak Audina imup, lucu, dan menggemaskan",
                "pesan": "Semangat kak Audina kuliahnya, semoga harimu bersinar terang seperti matahari di pagi hari",
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Ymm8K0Vp201CMpKqCHHqyNiL1bxOINYQ",
                "kesan": "Kak Cika menyenangkan, lucu, dan seru",
                "pesan": "Semangat terus kak Cika kuliahnya, semoga harimu menyenangkan dan indah selalu",
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1FUbU1OLRLNUKp0CUy7lRBAzjdyQVIsBb",
                "kesan": "Kak Gustin cantik, lucu, imut, dan menyenangkan",
                "pesan": "Semangat terus ya kak Gustin kuliahnya, semoga harimu selalu menyenangkan dan bahagia",
            },
            {
                "nama": "Muhammad Harvinsyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1o1BSZ13M1kzjSQ_Gh6LkmlXXtJytAZU8",
                "kesan": "Bang Harvin the chill guy and genius man",
                "pesan": "Semangat terus bang Harvin kuliahnya, semoga harimu selalu menyenangkan dan indah",
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jI-y-gS2gGvNHb0bp-PMBlkaVPN8hNS-",
                "kesan": "Kak Sabina baik, ramah, agamis, dan menyenangkan",
                "pesan": "Semangat kuliahnya kak Sabina, semoga harimu selalu menyilaukan seperti matahari yang sedang terbit",
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
