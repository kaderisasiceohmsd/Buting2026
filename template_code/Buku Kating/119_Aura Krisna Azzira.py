import streamlit as st
from sakura_ui import (
    render_buku_kating_header,
    render_kating_cards,
    sakura_dept_menu,
    display_kating,
)

render_buku_kating_header("119 - Aura Krisna Azzira")

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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bZ_xsql6N9tEc9GICgZnbxH5SLuIOi_z",
                "kesan": "bang ginda sangat pembaik, humble sekali, best pokoknya bang him",
                "pesan": "terimakasih banyak ya bang, keren terus bang ginda #1",
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1u_pc0wsPKMzpLWBxcL8hGeXGsp_Q_rLn",
                "kesan": "Keren baget, humble, ga seseram yang dikira",
                "pesan": "sukses selalu bang aqil",
            },
            {
                "nama": "Efi Defiyati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UyBqB5j3JygoQiE2PWJoncvmEKb6xQD0",
                "kesan": "baik sekali, keren bangat asprak",
                "pesan": "sukses selalu ya kak,selamatkan ads ku kakk",
            },
            {
                "nama": "Qois Olifio",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Dlwb4YNyEfnFSI7RTW9wxWV3RVcrlLju",
                "kesan": "baik sekali, terlihat kalem, keliatan suart menyurat ini sudah diluar kepala",
                "pesan": "sukses selalu yaa bang qois",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1B1f8IpWM7ph6eFoInAYMfyokqeFf_iCD",
                "kesan": "baik banget, humble, cantik sekali",
                "pesan": "mau belajar banyak soal kebendaharaannn. oiya senyum terus kak soalnya keliatan galak....",
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Z1VIi2sd9fW0bptDTn7Jn_wXZipAsgeZ",
                "kesan": "keliatan paling gemesss, humble sekalii, seru",
                "pesan": "suksess selalu yaa kak luthfiaa, semangatt semester ini dan selanjut selanjutnya ",
            },
        ]
        display_kating(kating_data, departemen=menu)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        kating_data = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Lnni0Xtz9kp1xPa0oqXraV16CHMF8381",
                "kesan": "baik sekaliii dan jugaa sangat ramah",
                "pesan": "semnagat kuliahnya bang, suksess semlalu bang ridho",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11d-q2YCTGhzrLmSFLZLOfNIv3_QtYzJw",
                "kesan": "cantik banget kak jue, baik, humble, kreatif",
                "pesan": "terimakasih banyak kak!!! sukses selalu ya kak jue, semoga kebaikan selalu mengelilingi kak jue,",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mN8qt17K_C6vJfJ9e2MPh07JbiMKSRLy",
                "kesan": "baik, kerenn banget skill komunikasinya, humble jugaa",
                "pesan": "terus mengudara bang dharu, mau banget sekeren bang dharu",
            },
            {
                "nama": "Givaro Ananta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1t4x9Acs4lR9yIvNLQykwAuADf8ijet0u",
                "kesan": "baik sekali, cute jujur",
                "pesan": "semangat kuliahnya bang givaro, sukses selalu",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15W4jiLEiEjB5-aiees_8D-5H6vb9I1hD",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gh Mikael Niko A S",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1T4tw5drFW0JMz1V6yxyCI9J13iURv7Ai",
                "kesan": "cool banget",
                "pesan": "pasang muka cute terus ya bang, imut soalnya",
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cl7s3vBGuXGfHHsRHd9JxJUEnMI5arS3",
                "kesan": "baik, humble",
                "pesan": "semangat dan sukse selalu ya kak",
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1i28JUY__A94Y2GdPrNq87QLI7zrHUk3c",
                "kesan": "baik sekali, kerenn banget, berkharisma, menginspirasii",
                "pesan": "Semangat terus kuliahnya kak, sukses selalu ya kak",
            },
            {
                "nama": "Hani Qurrota Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lyhlzP2UtTSU5Ngyt1-sV0Vd4nVGSlWc",
                "kesan": "kak hanii sangat ramah, baikkk sekali kakak acara ini hehe",
                "pesan": "sukses selalu ya kak hani, kakak acara baik! semngat terus kuliahnya kak hani",
            },
            {
                "nama": "Jeremia Halim",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PK8T0EXsw7q9MHg55WTYL8VPbNfcHaTw",
                "kesan": "baik, keren banget, humble dan menginspirasi!",
                "pesan": "mau hobi ngoding juga dong bang",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Naqzm2OyDySyGVtJrbcoBvvjAXqJ_b8q",
                "kesan": "ramahh sekali dan pembaik",
                "pesan": "jangan marah marah bang, kaget",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1oR2wtz9yzcq1TzqpcEjpRuI6NrWuzQg5",
                "kesan": "baik sekali, humble, tidak segalak yang dikira, ternyataa smansaa juga hehehe (happy)",
                "pesan": "sukses selalu ya kak sekarr, semangat kuliahnyaa #1 !!",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qUEH9FjhYrJCM3J8rwPRCr0kjvv5B7uw",
                "kesan": "cantik sekali, gemmes, humble",
                "pesan": "sukses selalu ya kakak, semangat kuliahnya kakak",
            },
        ]
        display_kating(kating_data, departemen=menu)
    baleg()

elif menu == "Senator":
    def senator():
        kating_data = [
            {
                "nama": "Fathinah Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1zi4CDG7tcn0uTFzmJpVN8BccYFBdHOJB",
                "kesan": "baik sekali, energinya posotif banget, berwibawa, menginspirasi",
                "pesan": "kok bisa sekeren ini kak, keren terus kak zizah! semoga bisa sekeren kak zizah",
            },
            {
                "nama": "Helmy Surya Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MoSXu0GYxZku6F916uY5jCRTjgkW6kyE",
                "kesan": "seru, humble sekali, ramah, ternyataa #JACOBI jugaa",
                "pesan": "JACOBI gangg, sukses terus bang. jangan buat jacobi#02 yelyel terus bang....",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1kvGDPpmXi92XMeC0PQDIq8zF9M-8CX82",
                "kesan": "baikkk sekali, ceria sekali kakak asprak",
                "pesan": "sukses selalu ya kak,selamatkan ads ku kakk",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1sQW7Gaw86mZyDyAVvZsFQn7lQVHB_WO_",
                "kesan": "cantik banget, humble, energi positif sekalii, keren banget deh pokoknya",
                "pesan": "terimakasih ya kak!! semoga kebaikan selalu mengelilingi kakakk, sukses selalu",
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QIULwOK6sH4QEKFhjTzosb94dVsCKEfv",
                "kesan": "baik sekali",
                "pesan": "sukse selalu bangg",
            },
            {
                "nama": "Suci Aulia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15PahVjeszBExeCQl6jD4jmYAwkxxZYCZ",
                "kesan": "kak suci sangat ramah,baik sekali, ceria banget",
                "pesan": "terimakasih ya kak sucii sudah menemani saat sedih waktu itu wkwkw, sukses selalu kak suci",
            },
            {
                "nama": "Wielman Itolo Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Zy5cl6HKaG8XS2iwkCgsdNspzfBUzA2l",
                "kesan": "pembaik seklaii, terlihat ramahh",
                "pesan": "sukses selalu ya bang wielman",
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14OxN-nbrs2Rj-HmVhw2NR1sKnj4d8eDW",
                "kesan": "baik sekali belio ini, energinya seperti tidak pernah habis, keren banget banget",
                "pesan": "keren terus yaa, semoga dikelilingi kebakan selaluuUuu",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11eHZpcGwYrFtzmIFx6WgsTBcKI8ot8C0",
                "kesan": "humble sekali, wajahnya sangat tegas yap",
                "pesan": "akhirnya foto sama abang gondrong, korlap, capo, ketuplak sf, motor xsr, celana denim",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Sb9q9bypjNXycUhh7bMafKe9YcR5xImK",
                "kesan": "tidak sekalem yang dikira, lucuu, bener bener pembaikk, dan seperti tidak pernah marah gitu....",
                "pesan": "semnagtt terus kuliahnya dan sukses selalu ya kak dwii",
            },
        ]
        display_kating(kating_data, departemen=menu)
    senator()

elif menu == "Departemen PSDA":
    def departemen_psda():
        kating_data = [
            {
                "nama": "Arienta Khusnul Ananda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19eQgY0ljzMQc15askCjYDavxoF0Dd2Tb",
                "kesan": "pembaik dan cantikk sekaliii, banget bangety",
                "pesan": "keren banget, seperti wanita tangguh... semangat selalu kakk",
            },
            {
                "nama": "Vany Salsabila Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15I5jphPhOFFcV7x3FKYbcoiPPPFWaLfT",
                "kesan": "keren bangett kak vanny, galak",
                "pesan": "sekses selalu kak vanny, semangat kuliahnyaa",
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1RI1mGj7MjaqfhDOY_4daZW-b6r8FgMag",
                "kesan": "baik, tegass, jago ngoding",
                "pesan": "keren banget bang, semoga bisa ngoding sejago bang nobel",
            },
            {
                "nama": "Desman Velius Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14ZKHdKwe7BHm8NKmzzBM6z9jo5oVfU9M",
                "kesan": "baik sekalii, humble, humoris",
                "pesan": "abang ini sangat pembaik, udah ya bang gajah gajahannya. sukses selalu bang desmann",
            },
            {
                "nama": "Afriza Azmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Z848klTjJhbuFSYyMtTj3jg3e_l70ezu",
                "kesan": "kaget",
                "pesan": "semangat bang, lain kali posenya lebih cute dong",
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1T2Vcj1m_qJq4tyOf11PIfQpvq3yTfDyw",
                "kesan": "kaget, humble",
                "pesan": "semangat bang, sukses selalu",
            },
            {
                "nama": "Caesar Ozora Alrando",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GVCTYXuYy8CLsgJXYK_ct0I8eKITtfvT",
                "kesan": "pembaik sekalii, baik baik",
                "pesan": "sukses selalu bang, gemes posenya bang",
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MjA6MOhdrC9Rl1Hoz2ooHRaHATKbvQ2p",
                "kesan": "baikk sekali, seru",
                "pesan": "keren banget, semangat kak euodia(yudia)",
            },
            {
                "nama": "Haikal Seventino Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Y3ADlAgvMD7uNTD0VilvrOedOAkGwu1y",
                "kesan": "baikkk, cool",
                "pesan": "semangat bang mulet",
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12njSc5jLF4lHaRRgApp_G-TEQ3C3lxd5",
                "kesan": "lucu bangett, cantikk, baikk ternyata",
                "pesan": "seruu banget, jangan cemberut kak, jadi takut. sukses selalu kak putri",
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1v1pZMFlUaA1WjYiPC1hJ8_oYxVIuVWWq",
                "kesan": "baik sekalii, cantik, seru",
                "pesan": "Ssemangat dan sukses selalu kakk queenta",
            },
            {
                "nama": "Azzelya Thianandry",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PVQdvkjkLkJ8kgeJCYl-ihSKWJ9xhGlS",
                "kesan": "baik, humble",
                "pesan": "semangat kuliahnyaa, sukses selalu kak",
            },
            {
                "nama": "Charrlindah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1gHX14POZuXtuhBL3ktSzF8wliAxCAkbB",
                "kesan": "cantik, baik",
                "pesan": "semangat kuliahnyaa, sukses selalu kak",
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18oaDfpki5rLZMX7Njefroy_g2DYklLpx",
                "kesan": "capo, baikkk sekali, lucu",
                "pesan": "semangat kuliahnyaa, sukses selalu bang",
            },
            {
                "nama": "Nabila Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14uSIPLIPFj7LFm8htobOPjG8ck7eULqh",
                "kesan": "lucu, cantik, baik",
                "pesan": "semangat kuliahnyaa, sukses selalu kak",
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18JX8vDiCeP5v9XAeCTjOp9op5w3gQvAW",
                "kesan": "baik, seru, humble",
                "pesan": "semangat kuliahnyaa, sukses selalu bang",
            },
            {
                "nama": "Salavia Naharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1sVXG4EaKA75hPCRkMzEyhcWEkU2vRAvA",
                "kesan": "cantik, baik",
                "pesan": "semangat kuliahnyaa, sukses selalu kak",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_psda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        kating_data = [
            {
                "nama": "Fabio Banyu Cyto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12S3o2flbdO4i0gvLl0211fu1Cug1Rj8E",
                "kesan": "seruu bangett, kerenn dan selalu pembaik",
                "pesan": "sukses selalu bang fabioo, semoga selalu dikelilingi kebaikann",
            },
            {
                "nama": "Tanty Widiyastuti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1H3Tf3CXoOzLIGe_RqpZ3lJrrhAoL8qon",
                "kesan": "seruu bangett, lucuu banget, humble",
                "pesan": "kerenn selalu kak, suksess selaluuu",
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1LK_qZXGshSwCwVOyDQx6ipdxO_NalA-h",
                "kesan": "baikk bangettt banget bangett, menginspirasii, kerenn selalu",
                "pesan": "terimakasih banyak untuk segala bantuannyaa bang, dipermudah segala urusnnyaaa",
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1DWXHN29BEHiLXvlzYJlvOBPCfkagJC7o",
                "kesan": "kerenn bangett bang, baikkk sekali",
                "pesan": "suksess selalu bangg, kerenn teruss",
            },
            {
                "nama": "Razin Hafid Hamdi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jAZBG0JLtYdi7gmnDqzB6BCvJQgvJJAq",
                "kesan": "baikkk bangettt, humble",
                "pesan": "semangatt kuliahnyaa, sukses selalu bang",
            },
            {
                "nama": "Manuel Frederika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=10_cgYPX3wP95i33jDErkCK6Lr9gg7M4s",
                "kesan": "batak sekali mukanya, tapii ternyata sangat pembaikkk",
                "pesan": "sukses selalu bangg, semangatt teruss",
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lhWvEKTPebO33yHNm58d9GcDa9GKxaWy",
                "kesan": "cantikk bangettt, baikk sekaliii, humblee, energinya baikk sekali",
                "pesan": "semangattt teruss yaa kakak viooo, suksess teruss pokoknya, kerenn kerenn!!!",
            },
            {
                "nama": "Risa Romadona",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1obqKJKPbfixMBEYY6Hu065rJcNxp0WdS",
                "kesan": "baikk sekaliii, lucu",
                "pesan": "semangat selalu kakk, suksessss",
            },
            {
                "nama": "Vannisa Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Xe3cFAN0zTWkv_F-mSqD4JdVx4p-NhBX",
                "kesan": "baikk seklaii, humblee, terlihatt tulusss",
                "pesan": "suksesss teruss yaa kakk vaniiisaa, keren teruys pokoknyaa",
            },
            {
                "nama": "Yulia Kristine Malau",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "baikk, keren, cantikk, imut",
                "pesan": "semangattt dan sukses selalu ya kak",
            },
            {
                "nama": "Elsa Sitorus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Egmf2dLWnOdD3Cs9AbxR-Yyou9JfYWBi",
                "kesan": "baikk bangett banget, cantiikk, keren",
                "pesan": "terimakasihh ya kakk, suksess terussss!!! semangat kuliahnyaa, langgeng ya",
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bXcMLYlwY0IUOdv_s1c-JV_EW13TlVyg",
                "kesan": "keren, baikkk, cantik",
                "pesan": "pembaikkk, sukses sellau ya kakk, semangatt",
            },
            {
                "nama": "Lovianora Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13g3zZgfAHdoSu2v7_yvsE0EZbHY0fxKw",
                "kesan": "seruu banget, cantikk, pembaik sekalii",
                "pesan": "semangatt selalu kak lovia, suksesss",
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GJdvB-58W7gj6YB9mSYu_fCUf2zEOoUc",
                "kesan": "baikk, humblee, keren",
                "pesan": "semangat selalu ya bang, suksess selalu",
            },
            {
                "nama": "Sherena Florencia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UPrhjRXxSphlhK2lNHrbTL7fnijJDZ_l",
                "kesan": "keren,cantik, seru",
                "pesan": "sukses selalu kakk, semangatttt",
            },
            {
                "nama": "Faiza Try Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JLycpMNhGhfqximcako80PW_LCTYEzks",
                "kesan": "kerenn bangett asprakk inii, menginspirasi sekali, energinyaa positif sekali",
                "pesan": "semogaa bisa seencerrr kak faizaa, sukses selalu  kakk faizaa",
            },
            {
                "nama": "Gathfan Nadif Ali",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dcgqhON7g9CpTMUFfpxMSggXZwY3ttXI",
                "kesan": "keren, seru, baikk sekali",
                "pesan": "semangat terus bangg, sukses kedepannya",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1z-J69K8qjYDklIiVWHte7a3eMOiI-1y-",
                "kesan": "seruu bangett abang metrooo iniii, baikk bangettt, lucuu",
                "pesan": "semangat selalu abangg metrokk,suksess teruss, jangan bosan sama jacobi#02",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1zJaJuc9LrmxlXykAS5baoc6yhnmWsxJr",
                "kesan": "kerenn bangettt, jago bangett bangett banget ngoding",
                "pesan": "semoga bisaa sejagoo ngoding bangg kaleb, ajarkan bang....",
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1obqKJKPbfixMBEYY6Hu065rJcNxp0WdS",
                "kesan": "baikkk sekali, kerenn",
                "pesan": "suksess selalu kak, semangatt",
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cMbN6TOa4ryJUd4G3sUm2zetrCWO698N",
                "kesan": "abangg jagoo ini, baik sekalii astutt, softspokenn",
                "pesan": "selamatkann mentnumm ku banggg, kerenn terus pokoknyaa",
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dcgqhON7g9CpTMUFfpxMSggXZwY3ttXI",
                "kesan": "kalem banget, baikk sekali, jagoo",
                "pesan": "ajarkan supaya 4.0 dengan gaya kalem abangg",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemen_eksternal():
        kating_data = [
            {
                "nama": "Arini Puteri Elandra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Q5oRB0AM9Jea7hLa6XK4psU1eEUHllNo",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Nabyla Sharfina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YQUUu9-Cf6CP9e-6AafNBwMZcD530lEa",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Khoirul Muttoharoh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1FkNPabgH3jrtK-MwKvDeczonYkWgl5rj",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1xsWs_I_HXdi5JagyhACVQb5fGG7hyn_5",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Indah Khairunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wDWowL7TGQreaupXX5wMkUsYPgPIbxnU",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bima Ekayasa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lSueja10J5U4P3mzfNoray1-OVJ5OCoJ",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QUKVyWXe3TS0Ex-z3e5x8QnlvqGJaE7C",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Adinda Deswita Maharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jEJz_Oy5pOFCOcWVBun0iQm1eJxvyU1n",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Yollanda Agustina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HktVqbOCX_Qul5h-hgHmczEWA21suH7d",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TYEH8ormsFzfZoMUfCO-GuowULum8cWM",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Alfaya Abiyyi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=104KKtEilRvr2q7_YUXZtL2m0z8xBXP8A",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Asri Meilani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1z3_UuKPD6UA2qxJHwRfvbLhy6G6UaSkN",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ahmad Rizky",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16oLOyHnIHPgFQQz9n5xNn_WRJc4AlNIj",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Selma Siti Aisyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ysQejA_9VaId5iPiLdOxHBWkeQ4lL3rt",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1sUbm4lrbz8XWkw2ilJ1BX5Lbse0cJelK",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Fathya Intami Gusda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1G-urrA_bm5sBQxqQUYa9f2sCLIu5Sk3e",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jfF9paf11cOmxEWjnJEWJFo0gn30Ar-o",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Danil N Fadillah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yBzgYNDVryStKwbMsyEzoQcOGgRI_NZ0",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Favian Arkaanda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1khGI8CqufvJEgoSAjRML1ls9cGWULUa5",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hWIpLpVPnr9hUX0lMMwlcfwmUMd-bC0k",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Rizaldi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11LhXHA1sTbJvVywwp-Wn3burCdQJ4dJX",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Saskia Nova Magdalena",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HFAXPyzy3jjgw0QJ1H2Cjxsdk_6FiNQK",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PHOHE5sBChmDT6mbaw6ng4tl0VJXqT2y",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Kharisma Mustika Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1piQPrmAU1sdbKRGyx8yNTOCU9akWbmvf",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15uxfD2KSURhHMqxENFJvpYXSranvigtW",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lxOVlKh0S7B0ep3ljLR-L-XpiO9sfvn5",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1BZ1MK7JLAZ3jSuy2fRfscURzh66j0KuW",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yliJFbPKSbPm3x3FcHwkfEy6MAUT6yoV",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Cerine Sihotang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tf_Kxmkg-ueLpUjLEe58bFN1z3p9JMBz",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Jaya Saputra Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1aG27Y-7Jl2TrWitJKUd2_tflNp8fiMBo",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Najla Nursyifa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qCiBZfNuOes6UQYSoIyjnJdYtIJOVq_0",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rozak Ramdani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Teresa Christiani Purba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16JbFoajQVZ0VDerLodkZfsmqkivHyMAr",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Audina Fitria",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1KhT1dHcMw1FIukaMf2irusBYcFksvawc",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12AouunFRZKZCp2r5He74sUkRkIs-jnfw",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Harvinsyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QewT5AIj1dg85KBGadaQghUuGJ3mZ2Gi",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13AhvPtR17YAwtg_nAErtDU0HORqAWTac",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-UNtWvqLuDVbJZJ4fxxjn83R-nExwrIO",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PvFmzhrAVwDaeR2cLfDDD71EoJU1hKJ5",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Afifah Fauziah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1gZE9sKkmYqI7VAItkP0tWW6xnlOmzUUW",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anadia Carana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1uE0ncxafdpAjH7nm5N-RkAasOliQ_h7j",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qa5bxb9a-JyN3A-ao1JO0abAgc338hoT",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Layina Ropiqo",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1gbUWTTk9BJwosixa0kJRmSuetcHEzeLV",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Mochammad Iqbal Az-Zahir",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18tHY4XvY95FJ0BIAb2YPG8ZWauqJ-Uxa",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_64K7QP_mH-ajZXzTKf9xShP39UgZVw-",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anggun Nita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1D46BDJC29dggbDPU46lbzzemoUaolEnk",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Della Anisa Fitri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VWdSMr0LvAQ0Sd28BhD8PJcM1KyGGotj",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1m7jAfyuOtUhmJgVKwq_prcqqg0ls386D",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Donna Maya Puspita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11mnJzCc0vR6Q5GFfskcV4vXa4LCaU6iV",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12Z4ZKj5klKBf12Vf2uE6xtbEzpEuTRSR",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vErxhldWJJR0GK-PgLOJKoisXsOLtv-P",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Jqi5LfPAnsWPT4XCeLzxWl60-JcPdeEc",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1nJEtmCIITv8SRgOePb163Tri5AVavrRA",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TsLnuaUgEXOHVoAoTxdQN0dbiNjxb5BC",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Allisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cdH6fRmVcBDybO-OqdurXa7EKlNEUEYh",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Alya Ramadhanti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_xz7_KWQK9y5pVBp-6lMUE6Xxnb5yDz3",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1kkqXPMiWVd3TG_MpSk1Swqjxz-Lk5eVq",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Difanya Husakina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PvFVp43X_p3NPlCvX0PKYqKRs5MFqIq7",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Nazlah Auliya",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16MS2R18u9L1jb0dTmRrUmMAFIKA_VpQb",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ruehl3ohOBAapyjGs42DIKBIlhhk3Ui6",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Edsel Adya Pradipta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fnEDd00jM5D6bUQw8H4AbTkPS7g7r8k4",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=10cRPrCn1XyY2NmFpR9p8OX8H9OgbxZpu",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Yfv1lEkGYdXfrBc5ewM6IKVNsDxk0mwr",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OwAUd5V636pmW4PCVtq6w4I-0WaOGr_r",
                "kesan": "keren bangett, seru, jago basket",
                "pesan": "sukses selalu bang, semangatt kuliahnyaa",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=135Cmo8RCL0YIFJyQ1DkZWl75FgsLje_r",
                "kesan": "cantikk bangett, kecee bangett kak gustii",
                "pesan": "kerwenn bangett kak gustii, suksess selalu yaa kak gustii",
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GnwKLsIm8NjtGLt_ghp08vARZ9VTnzKL",
                "kesan": "kerenn banget bang",
                "pesan": "semangatt selalu bang, suksesss",
            },
            {
                "nama": "Muhammad Ridwan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1N2bnq4-mW_JFV24jo9kcelhuuiFSeJZm",
                "kesan": "kerenn bangg, pembaikk",
                "pesan": "semangat terus kuliah dan suksess selalu",
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MpKLhwwwHEHANgToX-hBAJa1eXsVfFV2",
                "kesan": "kerenn kakk, suksess selaluu",
                "pesan": "semangatt kak ayu, suksess selalu",
            },
            {
                "nama": "Dafa Elpriza",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1btlvYQHDz6zovapuInowv8h6o6M2fSAQ",
                "kesan": "baikk, humble, seru",
                "pesan": "semangat kuliahnya bang, sukses selalu",
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11vbYxKLrwIaqsg9bK10hm1jZxGhay30L",
                "kesan": "cantik sekalii, pembaikk dan ternyata metrookk ganggg",
                "pesan": "suksess selaluu kak salsaa cantikk, m for metrook bahagia",
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1xU0rmyNJ1z51HP_S3ezPmReyHmK9odZJ",
                "kesan": "kerenn bang, baikk sekali",
                "pesan": "happy selaluu banggg",
            },
            {
                "nama": "Juwita Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hByEznH64iFcqQYVlVMMcoto2jl_d9-r",
                "kesan": "kakaknya sangat ramah, humble",
                "pesan": "suksesss terusss kak juwitaa, semangat",
            },
            {
                "nama": "Andra Ilham Bintang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Z4AY-KBLHAQmBuIHJaJva8-zFxENvowR",
                "kesan": "kerenn bangett abangg atlet inii, humblee sekaliii",
                "pesan": "doa baik bangg, semangattt kuliahnyaa",
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vCP_QntvasXw77Wa-C2sbVtVXSRwVxd3",
                "kesan": "keren bangg, baikk",
                "pesan": "happy teruss bang, suksesss",
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1S-QT0CHPEU6SrDR5TIJa1xwegJiaE1zd",
                "kesan": "kakaknya sangat ramah, humble, pembaik",
                "pesan": "semangat terus kuliahnya bang, suksesss",
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MpKLhwwwHEHANgToX-hBAJa1eXsVfFV2",
                "kesan": "baikk sekali, humble",
                "pesan": "semangat kuliahnyaa kak, suksess",
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1IWxzk592db5SjQhQpYjBnR8dnVbhRIc2",
                "kesan": "cantikk bangett, sukaa banget liat kak caca narii",
                "pesan": "kakak pembaik semangatt teruss yaa, suksess",
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qYtnZJ18pT-B65VjZ8LZvhZv-EnDj9LS",
                "kesan": "keren, humble, baik",
                "pesan": "suksess selalu bangg, semangattt",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_minbak()
