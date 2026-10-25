import streamlit as st
from sakura_ui import (
    render_buku_kating_header,
    render_kating_cards,
    sakura_dept_menu,
    display_kating,
)

render_buku_kating_header("058 - Dea Febryana")

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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CEDYIqb1Y5hSkqU0fq-uEG3-NAJwfImf",
                "kesan": "Gagah gitu liatnya,pembawaannya tenang",
                "pesan": "Semangat semester akhirnya bang!",
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vzeJvdZ0fUNIX3je4ThAeIPEQtPgphB2",
                "kesan": "Keliatannya tengil",
                "pesan": "Real tengil tapi jago",
            },
            {
                "nama": "Efi Defiyati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tmWGRr-LCh6DFSZg1wAPHm2S16Q3OhTa",
                "kesan": "keliatannya kaya jutek,tapi kalo udah senyum manis",
                "pesan": "Ajarin jadi orang penting di PPLK dong kak",
            },
            {
                "nama": "Qois Olifio",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VuGyJFe7elXPwjWY7qUUUj3RLi5TmAaz",
                "kesan": "Humble dan welcome banget",
                "pesan": "Semangat selalu semester akhirnya ya bang!",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bybk-YxRUEiZGZujcym2k0EncXuOFA9C",
                "kesan": "definisi kakak2 adem",
                "pesan": "semoga harinya selalu baik ya kak<3",
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ph5pCPH4VTLZu2hdq8yCtkQTp7T_4EhE",
                "kesan": "Receh abis suka ketawa",
                "pesan": "Hepi terus ya kak<3",
            },
        ]
        display_kating(kating_data, departemen=menu)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        kating_data = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=HbWnrMGJ6UAmE96y1jHZIXK84EVmFY5T",
                "kesan": "Tengil kaya bang aqil keliatannya,real tengil tapi beneran jago",
                "pesan": "semangat semester akhirnya bang!",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wlb3e4kAbcDrCAGf6FgDGJD6DQ-jAIB2",
                "kesan": "gemuyyyy",
                "pesan": "always happy kak juee<33333",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HVn0ZPH35VzODtEdN550ERgXZA8GtLUR",
                "kesan": "humble banget suka kalo bang dharu udah ngomong,orang kerenn!",
                "pesan": "ajarin dea keren kaya abang sih bang huhu",
            },
            {
                "nama": "Givaro Ananta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1u4f24-vFZZ6LTrpbNMpxZ4UXz8mOxGUO",
                "kesan": "cool ganteng anteng",
                "pesan": "hepi terus bang!",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WR7sLgcSAS0gey4cCA_k-9tL-WfH9N7h",
                "kesan": "Baik,seru,tegas dan baru tau kalo 1 tempat kos kaget banget mana dikasih penggaris juga huhu makasih kak ",
                "pesan": "tutorin dea magang di mandiri dong kak monic hehe",
            },
            {
                "nama": "Gh Mikael Niko A S",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qw0fftr7mXk-LPPjdxo1TDg5buQBBYTb",
                "kesan": "keliatannya orangnya tegas gasuka menye menye",
                "pesan": "Semangat bangi!",
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18c_V2GLFSDEkynJFoD1A52XN2ZFpIm2r",
                "kesan": "humble dan baik",
                "pesan": "Selalu happy ya kak:)",
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_9fz8HXqKQA63caAJWd_uG-gRtJizDTb",
                "kesan": "Kakak kalem,asik suka becanda juga",
                "pesan": "semangat nutor RC nya ya kak hehehe",
            },
            {
                "nama": "Hani Qurrota Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Q-I_16dtMN_CXohV7vPuLZNnGHvYUL4U",
                "kesan": "Kakak2 manis lucu,kalem",
                "pesan": "Semangat selalu kak<3",
            },
            {
                "nama": "Jeremia Halim",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1stKavNSTJYt6ryQkdYHePNOotaDnKrxF",
                "kesan": "Real abang2 kalem,manis",
                "pesan": "Hidup baleg!",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OC7xTAX02ZttxpzriN2nC8G9srNo8Yyw",
                "kesan": "kirain medis baik, taunya pas marah serem banget",
                "pesan": "bang jona keren bisa menang dinasional!",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ehqZh_KHhC-AwwdDTWCXGPAFuhryKry-",
                "kesan": "kak sekar ternyata ga galak",
                "pesan": "sehat sehat ka sekar<#",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19Mw7pHs23uo_A_aq2ZU-V43o1pCnx--Z",
                "kesan": "suka kalo liat kakaknya senyum",
                "pesan": "Semangat selalu kak!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    baleg()

elif menu == "Senator":
    def senator():
        kating_data = [
            {
                "nama": "Fathinah Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mm2KiAgL7t_K6W7_QMZtiL1zBYs4ShEN",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Helmy Surya Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QKDIlxxC8qLrrTjuFZzlTZ-dm2hm9ATi",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1n0unC2pshzG2ZoOkldEQW35VhboyIN4z",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HULLmpjLo0o7Jn5SsMpH-jWFyINSqvdr",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1z7glZhnLK8bt0uvi8XPnjAc_u84WXHRK",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Suci Aulia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12-cnfP8ki9-u7k3CRVSCmqOgCpZkIj6x",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Wielman Itolo Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1FOTRVGhpkYKtmBb1LZ-L96eaeoTC_idU",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MEs-K3g_85QBEmPL287lUTrPzHhjW7LK",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1L6CRpxJMFf_ba5K7mcijEprRp35bHu-G",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1i_0rQ25y5CR6Ghb9AwAmQ1SCcEtH8z6L",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    senator()

elif menu == "Departemen PSDA":
    def departemen_psda():
        kating_data = [
            {
                "nama": "Arienta Khusnul Ananda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1q5Il-no2o_JYFWaNUKSaVZ-nQgOF4qtD",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Vany Salsabila Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1sHjlHmHZD2cGcBXWYXHooxBTqDn17A8x",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12BUNNzcAMl8vmIOPQsmXohFpA2SD9ZHb",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Desman Velius Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CmqZYwi_V7byAti4W6S-pCuAvkb27wG9",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Afriza Azmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yov-rIpXgUs5cqGalpXvpKJN59487hPz",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UPWOljt_CtcH3P1KXF_g5LCIusUuVsnK",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Caesar Ozora Alrando",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1L9Gz4pijteq_s_NWDjpJf_qU9965am_3",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_QNh8OoOcyoQy4l9XQo4w2xBgiShZ1x1",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Haikal Seventino Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1N6X4enfRA90pzr-HCCxd1BG7zPLZ1kYt",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11jI-hhyJu7O32JdMLJUSoaqk_1q1GSB6",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1c7_QlJsjmjgZTenA91PuEw-IhyI-kgpW",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Azzelya Thianandry",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1EeEQIuZwvQUM1Ady26bJxMFEVJF3XSLf",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Charrlindah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wGGNlBEVCMrMg3tR9YnfqShZukS_1yUX",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PO8iyV92qOaayQjWv1Tk3eZKDA2LCi-l",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Nabila Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Pv24XeeviVmk6kMdxQgUY-F2LtAvotlK",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19q1C0BE6bcpu6BZzqQQeclpF2WhASOuS",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Salavia Naharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1e4E2xFaQbXx2BkS84fj4ntVWLjB9Z6AI",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_psda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        kating_data = [
            {
                "nama": "Fabio Banyu Cyto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1G8HR2DmQNgyO85_jMRoT1-enqMDYTNBn",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Tanty Widiyastuti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1k-9BaXf_GXxbPEaxRnqhKdzvF5C30zA8",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MuxqLL0ERvifC5ZATd6vjWx45VtLnqwX",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Razin Hafid Hamdi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wWFIk2bucTxM5BQdwQR9pGUZIP3tUltl",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Manuel Frederika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1c90ZQa-Z2WJpgba54QXWHc_Bj7pU8qtc",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12J_yw0UmweWoehx74I7m-nQsF4lYkH_5",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Risa Romadona",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ItwhJKb3Sj-Frlt2p-DZ21oUHu6I-zV_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Vannisa Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1eh36sd9H0znfMmMLx_frUvJyJsQYxQbd",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Yulia Kristine Malau",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hOAR1G4YzHRBplgFSboGv_dK7Z9ecqe3",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Elsa Sitorus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16UaTh2TxEWkmxlTcsa8WRMOJGP1Jnt9Y",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jAD_C24ythyvYMIHYJwL2UME4FqMakX5",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Lovianora Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16Ma5xQli02mIGv_A3R7V1G4-TdJ-dN_l",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mHl-6ypgFCQJswI_h4n16cU112SIeEuj",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Sherena Florencia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Cz_EakbX_co7Bpq3LhWukD7FoboThGQk",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Faiza Try Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rK_oHhT0vmKgNHJ3j2646bgaZ9Rt4FA3",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gathfan Nadif Ali",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dF5if41J749OfG4-n1PDQxx6_Ae8YLFt",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1iNZujMl3yAJrfdUKbPvYi3WAoWRGQi-H",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VSLjff-K8gGny-_cfoWd6G-lLbp48RIP",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1v6CAdSsgg0mgjPi70mg2tz_3pvlQ30-p",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1p4LUpwbUGRPBXyUUrQ-JsVZZtc--3W4n",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ldo7299huLn_eKNrzLMhcrZuL_49GnkP",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Kharisma Mustika Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Cerine Sihotang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Jaya Saputra Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Najla Nursyifa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Harvinsyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Ridwan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Dafa Elpriza",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Juwita Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Andra Ilham Bintang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_minbak()
