import streamlit as st
from sakura_ui import (
    render_buku_kating_header,
    render_kating_cards,
    sakura_dept_menu,
    display_kating,
)

render_buku_kating_header("087 - M.Ramadhan Bagus Ar-Rahman")

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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JW5Q6J0-l32PUXZ4fmDbIwv-z8uJD-aw",
                "kesan": "tegas dan berwibawa pokoknyaa bang gindaa",
                "pesan": "jadi kahim berat bang, semangat menjalankan amanahnya",
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YTvvbaOeLVFGR4bLLUJkXcla2nfTf27z",
                "kesan": "tegas dan berwibawa juga si bang aqil itu",
                "pesan": "Semangat yowww banggg dengan amanahnya",
            },
            {
                "nama": "Efi Defiyati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=10Rypx3s2TdPakzSFRB-Mfs4j7lzXZ7we",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangatloh kakak dengan jabatannyaa",
            },
            {
                "nama": "Qois Olifio",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Ki9fTDAJ0yYwBCSDVJXEnJ0FkBPsWNwJ",
                "kesan": "keliatannya berwibawa banggg",
                "pesan": "semangat yaa banggg dengan tugas tugas nyaa",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1NiN9gdOMSWZqPHM5BBoCd-K6wr7a8ESY",
                "kesan": "lucuuuuu",
                "pesan": "semangat trs kakkk",
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ca25_WajQEIdSeWyBUY8wcFlBwPIktRL",
                "kesan": "friendlyyyyyyy",
                "pesan": "semangat kak dengan tugasnyaa",
            },
        ]
        display_kating(kating_data, departemen=menu)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        kating_data = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1XNSXzeYpf8dhblsV8pFvjT1yYG18MFhn",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1i8wsWgHJnUyUvkKDC1tqEzGnEQ82FlmT",
                "kesan": "lucuuuuu bgtttt",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CN3B8cT4CHIFU4RDGQbvTJ7osGg-yPzH",
                "kesan": "lucu suka nonton agssss",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Givaro Ananta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Fjq65rzSjIOrQ9QKlwVUyA3zyMX62gsj",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VJHORmrZM1NbJmDwTxUtAuLJQrJeRmJn",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
            {
                "nama": "Gh Mikael Niko A S",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1DVIWHiNruGq7mzPlTwF-GWQvCVK38lDF",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1kLzuln39ncDIwiCh-KMUHv8Mtm31ytYx",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Cxvy9NgLhTx1JG4GugzjQwYwt2W54xwp",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Hani Qurrota Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lz9cuT5sq1qIU-jAHOCyRysaQB50LeTv",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Jeremia Halim",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GR7rcXMVJjBRlD9H0OATbzO8gPng7fy-",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1P7CN9dF8V_-iKQgd2X3VzXS4PDAFbgW9",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1KG-TG2-t8Yd7qRJm17GpRc53b8qQh4cr",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GiBU6W-U9flBGhClMuEM9el3VxQboR0o",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
        ]
        display_kating(kating_data, departemen=menu)
    baleg()

elif menu == "Senator":
    def senator():
        kating_data = [
            {
                "nama": "Fathinah Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SvUi2X7S5FzPLDIa6D-C8taWKWxnLaT7",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Helmy Surya Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pVXXQowJfMgINjAz8xzJ3c-lqtnRZ-ND",
                "kesan": "lucuuuuu bgtttt",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-kCR7qbrTDoMI5fmJMc1_1M817boX-6z",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hZtnE3Ufye4VSN2AL08TmVeBiW82Qyzq",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1k_dim-RF2oR2_bYUvek_VkaS1gy-7gt2",
                "kesan": "Bang nando orgnya lucuuuu",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Suci Aulia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1p1dYrOozNrHl395tY_Yi4V-MA2pawlIQ",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Wielman Itolo Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AOn9Xw74XKmhPkp9dRQlf3u8FDZdJCcl",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wOIX0pm-lwcBN0yy7qnxTXk-XEB6ptsi",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1q76Q4DJj7A_B7NJ9Z0iqEPcQwQg7EAwI",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ijdv9nYdilslXMpnT5x5gyvrz_KOBd_z",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
        ]
        display_kating(kating_data, departemen=menu)
    senator()

elif menu == "Departemen PSDA":
    def departemen_psda():
        kating_data = [
            {
                "nama": "Arienta Khusnul Ananda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15bGfYVoiqTkyGIoMFODDmq_7ee86AllF",
                "kesan": "baik kok ka arienta ini tapi emang ada jabatan jadi harus jaga image",
                "pesan": "semangat menjalankan amanahnya ya kak arienta",
            },
            {
                "nama": "Vany Salsabila Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wO05b9uvAsLIlSWs8dbwJ81__pFEKG2s",
                "kesan": "baik ka vanyyyyy",
                "pesan": "semangat menjalankan amanahnya ya kakkk",
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vdhGc5xb-gpvsAhAJd_i4KekmDEz8ekG",
                "kesan": "tegas dan berwibawa bang nobel ",
                "pesan": "semangat menjalankan amanahnya yaa bang",
            },
            {
                "nama": "Desman Velius Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1DXDxXW7BQhrLdTexVII67Y2UW9vvChTy",
                "kesan": "tegas dan berwibawa bang desman",
                "pesan": "semangat menjalankan amanahnya banggg",
            },
            {
                "nama": "Afriza Azmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1uZiq2JZhlSoEuxap498rpwUUvqQJYVRa",
                "kesan": "tegas dan berwibawa bang azmi",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mHMY8LoWjXATbpsl-iPWLuNxdhhE3kO0",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Caesar Ozora Alrando",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1oQX-KuDyYFzU_me1x-a941wk26ysVbIT",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya bang",
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_X3sgHjKvC7stBiQ2OFP0uBTLqw3Jpl0",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Haikal Seventino Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=10IcvDkUL4bpDfa-0O0TTuaWw0nRTDPUP",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kak",
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1q9XtvSbuiZWLb4Opzr-1lJ7u8qoOoY0p",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kakk",
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1p1TKGd8FNwBwwZAsJmh3EcozCYZjqBUx",
                "kesan": "tegas dan berwibawa",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
            {
                "nama": "Azzelya Thianandry",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OaLPUeF7Ub-TKOEjHasVSZdu55MyoNia",
                "kesan": "baikk",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
            {
                "nama": "Charrlindah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1q2TCdcQEXFWMLyZKfs0eqzYsBYPJfi4Y",
                "kesan": "baik",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OPjbd9fsouyIZAKdU3oV4FHPOb3fsj5C",
                "kesan": "baik mengayomi",
                "pesan": "semangat menjalankan amanahnya bangg",
            },
            {
                "nama": "Nabila Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1A5gqa__vCQzrYXhF8ETqvGiqMDXLcYQt",
                "kesan": "ramah",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1DheYcOlDSOM66lq9fMSgbURJJxfVc7So",
                "kesan": "baikkk orgnyaaa",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
            {
                "nama": "Salavia Naharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1aKhDJYIQsEYhcLYCXOA2WFZrykL9mBIf",
                "kesan": "ramah",
                "pesan": "semangat menjalankan amanahnya kakkkk",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_psda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        kating_data = [
            {
                "nama": "Fabio Banyu Cyto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12ZNz8JnR0F1ZlXBg0zz7olIT9MtXgAe4",
                "kesan": "baikkk bang fabio ini",
                "pesan": "Semangat ya banggg jadi kepala departemen",
            },
            {
                "nama": "Tanty Widiyastuti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_8UqeyWHgYBbPlU0vDNG3eKiVonae0W8",
                "kesan": "lucuuu, aku salah nama manggilnya kak tantryyy",
                "pesan": "Semangat ya kakkk tanty",
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1KQbBRRXU-UUR4uLf91uOpCgqKnkH6wcP",
                "kesan": "banggg fadil yang mentorin aku dutaa iteraa",
                "pesan": "Khusnul Khotimah bang fadil, aku bersaksi bang fadil orang baik...Alfatihah",
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pMhAZLrl7c4ua5ATDVO17r7DJR9gXtdy",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah bggg",
            },
            {
                "nama": "Razin Hafid Hamdi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1BSRBRlHrxVNL2TBmMbWura1NSudeDp6a",
                "kesan": "mirip pak tirta,kalem",
                "pesan": "Semangat terus bgggg",
            },
            {
                "nama": "Manuel Frederika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1s2-JGOcyvHCjhjHFaf39NfeIIiz-zr5r",
                "kesan": "SANGARRRRRR",
                "pesan": "makasih bang bimbingannya selama magang di PSD",
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1DcLGczueC7zZY_mz-4UzEicAzESHjbQY",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "ayo ikut magang psd kak violaaa",
            },
            {
                "nama": "Risa Romadona",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1P_zyDsT0BgJewGzZAqbWYkNY0aiqZW49",
                "kesan": "aku gatau namanya waktu wwc...maafkan aku kak risa...",
                "pesan": "BAIK BANGET JOSSSLAHHHH KAK RISAAA INIII",
            },
            {
                "nama": "Vannisa Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HnOKrK85mlWJkAAQM-aXVN-hCHGyKi3S",
                "kesan": "Kakaknya baik, pengen di mentorin",
                "pesan": "Semangat terus kuliah ya kakkk",
            },
            {
                "nama": "Yulia Kristine Malau",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GZ_pLjcNl96Pfbo_UQq7iaqy1ASt4dsI",
                "kesan": "Kakaknya baikkk dan ramah",
                "pesan": "Semangat terus kuliah kakkkkk",
            },
            {
                "nama": "Elsa Sitorus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Uz97VsyJVBojNyL6Rreie2M8UsDpY63L",
                "kesan": "suka marah marah",
                "pesan": "jangan marah-marah kak elsa",
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UIggTTrBpghE8HTbmh7KUw9Yz-6dJrlW",
                "kesan": "Kakaknya sangat ramah!",
                "pesan": "Semangat terus kuliah kak",
            },
            {
                "nama": "Lovianora Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Xp5ls01cFBbNY7QRMicWBuG9WlePjkbD",
                "kesan": "Kakak asprak alprooooo",
                "pesan": "baikkkk banget kaaa loviaaa",
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Me8mtMI_Ua8po34CDfHpI3Xhvc1r0gXR",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Sherena Florencia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ZuA7fjgUfMy9wagS9UtBO4seySNFJ33k",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah kakkk",
            },
            {
                "nama": "Faiza Try Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1S4RGcZCddXxEJ0KH_FiZOEm5EsBA52MT",
                "kesan": "kakak ozt",
                "pesan": "ajarin aku dong kak matkul kuliah",
            },
            {
                "nama": "Gathfan Nadif Ali",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qJr9PH5ti_fLZsFV97uRWh9HbqIiJaWA",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dGZ_7lOe_D9JhNi5P0cjUQg1RHDyi7cr",
                "kesan": "LUCUUUU BAIK RAMAH SEMUANYALAH UNTUK BANG HAFIDZZZ INIII",
                "pesan": "AJARIN NGODING DONG BOSSS",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wKMafhJdDGWdc5lUy_apk-edEiIEnZHp",
                "kesan": "ABANG TUTOR ALE TERBAIK YANG GAMPANG DIPAHAMI",
                "pesan": "AJARIN NGODING BANG KALEBBB",
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cumnuqfMnCNl4qlNk0Qi0eKIIgHt16qP",
                "kesan": "Kakak NIM AKUUUUU",
                "pesan": "SEMANGAT KAKAK NIM",
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1gaQ_Kx6QLEUQlD1sTcQtqtksEKwc5-ia",
                "kesan": "SUARA MCNYA MANTAPPPPP",
                "pesan": "TUTOR PINTER DAN MULTITALENT DONG BANG",
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hxGhHUrGPtVytyLDBf62YS-R2cg28qqu",
                "kesan": "TEGAS DAN BERWIBAWA",
                "pesan": "AJARIN BIAR PINTER BANG",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemen_eksternal():
        kating_data = [
            {
                "nama": "Arini Puteri Elandra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1j4IulGjFcGcuxx47qb7uP3Mo2HmWlVjx",
                "kesan": "Kakaknya BAIK SIHHHH",
                "pesan": "Semangat terus kuliahnyaaa kakkk",
            },
            {
                "nama": "Nabyla Sharfina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1l59zOXqvybxBcNhN68JqjORTz3U9BSA9",
                "kesan": "Kakaknya sangat baik",
                "pesan": "Semangat terus kuliah kak",
            },
            {
                "nama": "Khoirul Muttoharoh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1b3CpAuM2YtLie7j7KNvviMOMq-0hpTWZ",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ZQ1hO6RWuPCkpCQqoMSrgE0UA4tmOx6G",
                "kesan": "lulusan pesantren juga bg adit ini",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Indah Khairunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JgnTi8imfxNQN1J3NRkn_R7946MEV5a4",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Bima Ekayasa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_gy329LpSCzWYKwdzxuEQ9D6IP5-4xue",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1nEqohawypk4KX2fLNYqusqqpi6G8-MIe",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Adinda Deswita Maharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=136u-Eqmg_pTJ9_QofeL4T12u-dJenwr0",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Yollanda Agustina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1BeNklE87WQNIi4hWh3aRal-7mpPdQIZE",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1BgV84cA5sDTjtUyK565gvLfvY53DEHQi",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Alfaya Abiyyi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1DeYFCVfaEv7e84GpvB_J0DURtyMrhTkV",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Asri Meilani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vtkgoFooIwUwu2x0nITIfF1cXv7t1qNY",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Ahmad Rizky",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ClJNJNHIhPexdNI5Xs5YnuqGJPs_RX4b",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Selma Siti Aisyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bYRQgDiR-GlWFh2cUMVHYW1X4Kys6gzR",
                "kesan": "temennya ka ashilaaa",
                "pesan": "Semangat kakkk",
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1V77zEThhWkfPmFyKDtZvhBO65Tm08-t7",
                "kesan": "KAKAK ITERA MENGAJAR YANG BAIK TIDAK SOMBONG",
                "pesan": "MAAFKAN AKU YANG TIDAK PENGMAS ITU",
            },
            {
                "nama": "Fathya Intami Gusda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16__JCTrr-pFGIXIgijjpsz2I95Tcwn8T",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1LNN5TSL9n7d9CFdvosQVNsdk3eXtWdQp",
                "kesan": "KAKAK ITERA MENGAJAR YANG BAIK HATI TIDAK SOMBONGGG",
                "pesan": "MAAFKAN AKU YANG TIDAK DAFTAR PENGMAS ITU",
            },
            {
                "nama": "Danil N Fadillah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1f84DaT9ufbCL9vaCFfX2ZHAgXqeTgtS2",
                "kesan": "MENTOR DUTAAAAA ITERAA AKUUUU",
                "pesan": "MAKASIH ARAHANNYA BANG DANIL",
            },
            {
                "nama": "Favian Arkaanda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-MNplcWlW6dj4eod__rfugZkkVpG7zIn",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UlBY88ajMduRoPK9P_GPEt-PDCA-MPMe",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Muhammad Rizaldi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CESlIZI5RC4-gtWPBJZ9YP74YiyKHZBv",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Saskia Nova Magdalena",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cgpoYu4K20qw7pUeJKcHMncy2pgV6WD9",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_eksternal()

elif menu == "Departemen Internal":
    def departemen_internal():
        kating_data = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1KV0yK92Btj_0lSzA55JDpbZFASNZBW-h",
                "kesan": "KETUPLAK FG 2025",
                "pesan": "Semangat terus kuliah bang",
            },
            {
                "nama": "Kharisma Mustika Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ztnc-Lp1Htyu5CKuhBt8LNlJkdGLb94b",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1XYBOyBvMCcEGkiHztfyvU0xlUwCAJV7D",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Bx-YKDK34okxIueH06cUZ81oAf14gkrY",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Semangat terus kuliah",
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UivFNpesbZiLcGZ3z5J_ZypoI-xueCNy",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1S4vYS197-kCyUFVvpIIxVxWBSnp9c7HH",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Cerine Sihotang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1iQwXInETHRxc1cON9kBDmF9Q8s5dejfA",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Jaya Saputra Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1V7nbbUU7cKuNzMrU9AgsrcQLlx7Kx6ju",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Najla Nursyifa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1iQ7mc3mnWhcYedDjw8_JKFFkLtPTfdNi",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rozak Ramdani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GPwC74u3NGlgeVWs7774ENmiSbjQp2Rq",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Teresa Christiani Purba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Zy03UyEMVarw46NyQmKYQIEvkzwduJWQ",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Audina Fitria",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WYeJvsH49khMXx8DYQB3Bqghc92jWn_1",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1V6p_pE0OWvo94_t89FVApTkdrWOe0h0_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1i0ADda4eym813Qec-BdOazput0NU95uc",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Harvinsyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19qfSaMoemo1obOSHggAo2slHNW1dttpK",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cGIqerrYEsfJ0uqP4YJf8oGu1otTCiu6",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MRkYiQU-OdM6l2DMU4LbdI3EDICTNhl5",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fHlF80lkiN6QFrGhMzIPGjIg6vLY4wPE",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Afifah Fauziah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1cr9XyrJQ523jilIVWAfCZSzdli46KnDb",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anadia Carana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pkkpI3MTlt26Ro_XxoxvJU74M245-ZGF",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MFP8PeEt2mODcWT0zASry3z10oEUCfK9",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Layina Ropiqo",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1oLO5Leiiis_wib-OdLHtloEs0oYwWmo0",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Mochammad Iqbal Az-Zahir",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1d40s2apoBkMYKLP6u9ZhhgTtXIjYBamW",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Talitha Justine",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1KAIzxKQvNPXAwZulLGbuKrfaLpgYCFcy",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Abdillah Fikri Al Pome",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1p_pJjihP2vwTtMwqU0dXKA3QdRlf1hcZ",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TQgXGryVawvAkSAxFhf_R3Yi6t20XGNQ",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anggun Nita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1xp0UXBeCZSz6Z5DcVOPRAmqvLQQ5Fk8k",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Della Anisa Fitri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wzkLGJ_aw0iR-EHw9ru312Ypu6_vPklT",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1n9LjJrdZGzHdC35e5-oOdOHKKQQOpffo",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Donna Maya Puspita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11Am4NBjNpyeOdwzDkIbIPjRl2KPBhrW8",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1raPp6o85LOpU39Ap1k-lw3rTjO87uRql",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1f3ysjz9IHD3Qkeb1jwWwOu2Juuy-m4Tp",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Raihana Adelia Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=10t7o98_OqlDN5KuquthtcTVtlBy7vlWL",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UCr5XjIhLSHIkeYKX4xL_qak4Ua4xQ90",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lnHjiIBUUQ2cePjebDsgvAF8ivkVpaQ1",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11Q6YUHwttLnW6Suc51379PUpvucY-YT3",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Allisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1kRfPlTpSW0Ad6NNmGxLnQv3q_ruPGLxc",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Alya Ramadhanti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vccnqZRASAFxHccmm7FuppOLIGGh_Kvu",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1DRtCwfk-UA3QRijJs4xStChCYrEbpVMa",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Difanya Husakina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TbBK-NGIZK3UodRiL_w1xQWFnPx9LO3F",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Nazlah Auliya",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jbvX73UzRaQYPgJG-kYBqRwVQCPeT6kC",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1m2NODdpPl3s_cOfR8ZngHQ_988PywUkc",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Edsel Adya Pradipta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vOe4-EnciOtq5uviZue1cRZQbmCs67GJ",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1L1boplM3nXXWPj_-vONwXZlJfSBIlJ03",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1FM83p6qPUBMehbCqOm96dr6278QAjf0u_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AFUNG-7hyPJ83eoekQcz7jkyxOHxeKPZ",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AROZ1ZksKOlTJOIb-wrIeT_kLwakBQ9Y",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Jbn7SV3XcCg_nDfNR6xxAcAvWgR2Z9Co",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rqthI7tWNH-w5ZWL_NwyyHcWXR2SLqOr",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Ridwan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1NyRHbUsr1hQtDZvpb_Qbqse1T4MyN3yU",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yEK3Vur-DrP5cwMuvnfLQKY1mBzyFf2X",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Dafa Elpriza",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1XWFr94HpzeX-EW59CKoDB3tTU7KeJiAH",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Ot_OU6yfsx3yaBf6Zch7PDodxDP_Kgac",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Z-yvjqn8xAPQFxgO10nJd7h-_zo_HQbi",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Juwita Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1uLu_5BA8b_smKxuN4qzuaHMzB1BEmcUF",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Andra Ilham Bintang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1l85jOa_F-0xbfWfC5onPuD9ywWlwYR85",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yKojXNHZk73sCU-61eq-tLVUkqqjHXuY",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1B1T25IhCGs1q1zx88EYZ0uGE3KRP1aQw",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mRjdtvYnLcZnw3IFfuSQOoRTfIU8Pgbn",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yfoBOXzwGgv-1SlhEI0dEqyXVWfweDb9",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lDvqd8ftwBLQXgCaNkXwJFe_u-Z3GFqH",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_minbak()
