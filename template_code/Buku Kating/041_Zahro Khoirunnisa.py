import streamlit as st
from sakura_ui import (
    render_buku_kating_header,
    render_kating_cards,
    sakura_dept_menu,
    display_kating,
)

render_buku_kating_header("041 - Zahro Khoirunnisa")

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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1sVr38ZkjKRzn3GShB5X1pcP-Qt6n4xki",
                "kesan": "Bang Fajar orangnya sangat ramah dan baik, soalnya bantuin kodingan aku yang error.",
                "pesan": "Semoga kedepannya aku bisa jadi orang kaya bang fajar, terimakasih banyak bang.",
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1gV56_EjzRFeQk3OoHrHz63dPLhkgWB8p",
                "kesan": "Bang Aqil baik dan ramah jugaa.",
                "pesan": "Waktu maparin materi jangan cepet cepet bang, jujur ketinggalan materi.",
            },
            {
                "nama": "Efi Defiyati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Orrbf0_4fHQvkioLEg19YrbvCbWnbDqw",
                "kesan": "Kak Efi keliatannya kalem seteleh ku liat liat emang kalem ternyata.",
                "pesan": "Semangat nyusun TAnya Kak Efi.",
            },
            {
                "nama": "Qois Olifio",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1W84_ImFkVl34lGQLebrJ7hBYpD0GwhcM",
                "kesan": "Bang Qois keliatan kaya ada aura anak rohis gitu.",
                "pesan": "Semoga gak stres di semester ini ya bang.",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1b303jHGNOdizmZ3UNa49_wEkdP_TQGq-",
                "kesan": "Visual kakak ngingetin aku sama seseorang, tapi lupa siapa.",
                "pesan": "Kak ajarin bisa berkuda kakak.",
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UGsVnsG-Wx0_3Fr8G7eKoFvDZUVDHJ1j",
                "kesan": "Kakak cantik bangett terus visualnya gak ngebosenin..",
                "pesan": "Spil skincarenya kakak cantik.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        kating_data = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1EoTauZ4I4XddKPLf-VVvKrd6nOh7wKJc",
                "kesan": "Bang Ridho baik dan ramah, jujur sungkan mau nanya pas code aku error.",
                "pesan": "Makasih udah bantuin pas code aku error.",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ErjQ5f1pX7ET-RijIGJuClpc1MFrdXue",
                "kesan": "Kakak ini asik dan gak nyangka ignya menginspiratif.",
                "pesan": "Kakak ajarin aku biar jadi orang yg menginspirasi juga.",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1XpgdFqEo-SJf-FAfrC07RUtLqagjh1HV",
                "kesan": "Kagum banget sama Bang Dharu soalnya prestasinya banyak.",
                "pesan": "Tutor lolos KKN Kebangsaaan Bang Dharu.",
            },
            {
                "nama": "Givaro Ananta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1i6V-d7t_kd_cKCDrdKpFBlAVd4sHOzoJ",
                "kesan": "Suka sama lesung pipitnya.",
                "pesan": "Kopinya berapa shot tuh bang?",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1eAH5DG1033Ak0AMc3sZwGrscl4Qeanun",
                "kesan": "Kagum sama Kak Monika soalnya lolos magang Bank Mandiri.",
                "pesan": "Minta tutornya biar bisa magang di tempat yang sama kaya kakak.",
            },
            {
                "nama": "Gh Mikael Niko A S",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1KbEKLs2fJz8nfp4fSIu78OPhDUCITVGq",
                "kesan": "Bang Niko baikk, soalnya pas ketemu pertama kali ramah banget.",
                "pesan": "Semoga lancar di semester 5 dan semoga amanah dalam mengemban tanggung jawabnya.",
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1xzIzWw1lTCgryESEZi42mb-cxQqS6TZU",
                "kesan": "Kakaknya baik banget dan cantikk.",
                "pesan": "Ajarin bikin pempek yang enak kak.",
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1wSOFXvtQG0df1xfPLs8s6NydR74pqBZR",
                "kesan": "kak Nisa baik, aku minta foto ulang dikabulin.",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD Kakak.",
            },
            {
                "nama": "Hani Qurrota Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vIGHcZm6RxR08R7VaoOhjRXSBO8Wijug",
                "kesan": "Gak enak sama kak Hani soalnya pernah manggil jadi Kak Hana.",
                "pesan": "Semoga segala urusan kedepannya dipermudah sama Tuhan.",
            },
            {
                "nama": "Jeremia Halim",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HS4AeXqADgxCxrZkELYD5wf9D1GCJgMN",
                "kesan": "Abang ini fast respon tapi juga slow respon.",
                "pesan": "semangat terus kuliahnya abang.",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1LaRz6GACWm3DPOtgKFK6MRqPQ0P93VSo",
                "kesan": "Jujur kaget ternyata bang Jona follow ig aku duluan.",
                "pesan": "Maaf kan aku yang baru follback ini bang."",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1kLuHKvl5FRFIkMGBM5mlzRMI1YEs_7DX",
                "kesan": "Kakak Sekar keliatannya galak ternyata baikk.",
                "pesan": "Semangat terus yaa kak kuliahnya.",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TIREI8jABuDhvievgowso2A19ZamilGV",
                "kesan": "Dari awal liat web HMSD salfok sama namanya.",
                "pesan": "Semangat terus yaa kakak cantik.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    baleg()

elif menu == "Senator":
    def senator():
        kating_data = [
            {
                "nama": "Fathinah Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Z8Vd_gVXLcqaPaL4Nl3UCSSupQnvdcQI",
                "kesan": "Kak Zizah baik banget, ramah, dan rajin solat.",
                "pesan": "Bangga banget sama kakak akademin, nonakademik, dan tuhan imbang.",
            },
            {
                "nama": "Helmy Surya Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GVBCaePsAHroGJJvFAJqYdcLPqAPcLUG",
                "kesan": "Bang Helmy ternyata baik banget, jadi terharu aku.",
                "pesan": "Bang Helmy pusing enggak?",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ULgdmXLiod9K8Z64ozjpKsAcCZlNQJ0i",
                "kesan": "Kak Hana, nama Kak Hana banyak di Sains Data, jadi bingung gitu akunya.",
                "pesan": "It's okay nama Kak Hana banyak tapi Kak Hana Bason tetep kakak.",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1k4y-mcJTAEndN6sDXO4yUQFVf424f1xi",
                "kesan": "Kak Nadya cantik dan bening bangett.",
                "pesan": "Spil skincarenya dong kakakk.",
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1erTQ_pyVOkYxSXtXSe0gc78xbc3JYk0b",
                "kesan": "Bang Nando fast respon dan ramah banget.",
                "pesan": "Semoga tetap bertahan di ITERA sampe lulus yaa bang.",
            },
            {
                "nama": "Suci Aulia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1v3UfUikhfzNXQX3vYZqkm9LGG8uhsiwN",
                "kesan": "Kak Suci baik dan ramahh terus suka banget sama model jilbabnya.",
                "pesan": "Ajarin aku bikin jilbab yang bagus juga kak.",
            },
            {
                "nama": "Wielman Itolo Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1G0sVvpwqNGiTZvdOiFriLSobYyPDMZj6",
                "kesan": "Salah satu abang yang aku notice namanya, soalnya unik",
                "pesan": "Selamat menempuh dunia semester 5 bang.",
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OLmypf3uOmJCI-LWaS-VXGrG1jjhBzJ7",
                "kesan": "Kak Aqila lucu banget, imut dan kiyut, full energi terus.",
                "pesan": "Spill caranya biar energi gak abis abis kakak.",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CnYKrYnMXNGGiSKHkQaiRXgr21GwMS4S",
                "kesan": "Keliatan galak ternyata sangat baik.",
                "pesan": "Selalu semangat bang Hazel.",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=107iyUuEVqx-PEmCp50tDWbbmmLJEYfl3",
                "kesan": "Kak Dwi ramah dan baikk.",
                "pesan": "Btw umur kita sama nih kak.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    senator()

elif menu == "Departemen PSDA":
    def departemen_psda():
        kating_data = [
            {
                "nama": "Arienta Khusnul Ananda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1A_IuPe4JgyDR4QlRwGRLmEEzWcFPKs_J",
                "kesan": "Kakak Arienta manis banget waktu senyum, jadi suka deh.",
                "pesan": "Semangat terus kuliah dan semoga di lancarnya dalam ngerjain TA-nya.",
            },
            {
                "nama": "Vany Salsabila Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tvHssXw0jgoXLCSx7SxrT91K9WH4CXpF",
                "kesan": "Kak Vany tambah cantek kalo senyumm.",
                "pesan": "Good luck kak vany, kakak pasti bisa.",
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vwiUl3F1zKioSX6Gt5bMAhqgvYkRVAlC",
                "kesan": "Bang Nobel ganteng dan ramah.",
                "pesan": "Tetep jadi orang yang ramah yaa bang.",
            },
            {
                "nama": "Desman Velius Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hhoukiYesPBzDnCXcITryfr3f1D7-vs5",
                "kesan": "Bang Desman ramah, sopspoken, dan baikk.",
                "pesan": "Bang Desman, daunnya udah kering.",
            },
            {
                "nama": "Afriza Azmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Ytcrbt2bdpRFl7PHQ2U3RUXfvxFBoZ7s",
                "kesan": "Kagum banget sama Bang Azmi soalnya taat agama.",
                "pesan": "Semoga bisa jaga solat 5 waktunya yaa Bang.",
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UcDTSq47cLI2FDg9hzcmAosgyvxFGpSe",
                "kesan": "Bang Ayake ramah bangett gak sombong pas d sapa.",
                "pesan": "Semangat terus kuliah dan tetep jadi orang yang ramah yaa bang.",
            },
            {
                "nama": "Caesar Ozora Alrando",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mN0T145meYtdhHzvdKZdVFSaJoEvYJny",
                "kesan": "Abang korlap pplk 2025, gak pernah terlupakan di aku.",
                "pesan": "Semoga selalu diberi kemudahan dalam menjalankan amanah yaa bang.",
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rbnme1afJaMEUb86wQGYFjtV4qnIpxAR",
                "kesan": "Kak Euodia namanya unik bangett, terus juga ramah gituu.",
                "pesan": "Kak kapan-kapan foto berdua lagi yuk.",
            },
            {
                "nama": "Haikal Seventino Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Fya9o3d_cZAX8nTPQ9LfwYQ_vFDUfSra",
                "kesan": "Bang bakik, ramah, dan ganteng juga.",
                "pesan": "Bang Haikal pernah potong rambut pendek enggak?",
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16WUW2wpPEUzQUzxgwJ0H-HQ9y9g-baAM",
                "kesan": "Kakak Putri cantik, baik, ramah, dan perhatian.",
                "pesan": "Sukses terus untuk kedepannya Kak Putri.",
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1l3YdJIadQFTCIVT6mixbu1aI8Flp7gQV",
                "kesan": "Salfok sama nama kakak, soalnya bagus banget.",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Azzelya Thianandry",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yMaENoTt7z2gHPVT_bD4GGtwpU5lHSJP",
                "kesan": "Seneng bangett akhirnya ketemu kakak NIM akuu.",
                "pesan": "Kak kapan-kapan kita foto bertiga sama Firdha yaa kak.",
            },
            {
                "nama": "Charrlindah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1xAbFC9S_yHSRCQ6fu3XC8qdAMoU_U_-j",
                "kesan": "Kak Charrlindah cantikk terus aku suka style rambut kakak.",
                "pesan": "Kak pernah warnain rambut enggak?",
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qQ4CH0-IGrDJGE6iel6ioYIVKhkX-s4W",
                "kesan": "Abangnya kalem banget waktu wawancara.",
                "pesan": "Bang Jemar nama depannya kok bisa sama, sama Bang Jeremi Baleg.",
            },
            {
                "nama": "Nabila Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1US2rFY309daPz9V5Mj5BZGqjhymUjA72",
                "kesan": "Seneng ketemu kakak sains data yang suka main Roblox.",
                "pesan": "Kak kapan-kapan mabar Roblox yukk.",
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CDNUSaNOrEly3fcX9Zi74teBV6GE0z0m",
                "kesan": "Abang ganteng banget waktu pake kacamata.",
                "pesan": "Abang kalo ketemu aku inget gak yaa?",
            },
            {
                "nama": "Salavia Naharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1d3muAE-D5Dot3RYsiZh_cAmRuCRjqu-P",
                "kesan": "Ihh lucu deh ngeliat kakak soalnya kecil kaya aku.",
                "pesan": "Kak jangan marah yaa waktu aku bilang kecil.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_psda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        kating_data = [
            {
                "nama": "Fabio Banyu Cyto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mKf5MaxivkfvsY7yejdtXMSv-iocxKLv",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Tanty Widiyastuti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SDcg1cfe_xQgMyQV8Dw8E-54n5BmnxOv",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UzuCzO0M7H8vkdk25I-tHWkHocKkJK3A",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1k9HmZGfXPxq2mEr4Uxc20aV9z_J9SaAM",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Razin Hafid Hamdi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1LoFl6z4bPyj90R9brNG8lRmOlQyXyz11",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Manuel Frederika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dhFYC01yZN70DLT4HunH0ennq8l90egS",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1EzKDtIW4wsS-M99qB-3rT1UHS2udtADl",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Risa Romadona",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1kZ6Y7-ls5yCys4q9SsXOrAQs60bKI3hi",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Vannisa Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1eDUCSFBmoC_sVxLaDUN6TwrljTlaixq4",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Yulia Kristine Malau",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_mmtLo1ZGtmTEZphnu-u_fMd6DlCYcDd",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Elsa Sitorus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1DuAlwBLQWdqE1fOGPnqQThzHdyytOJRZ",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Kwa3AMZbERah8-CeO6FuExT4k3SgHAdw",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Lovianora Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1o1BNv3BDN-ksmKi61g0EiQYY6U8KzGtY",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1LxM2Yp8sRIES1aKc0aqbmqEJMtrTji_C",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Sherena Florencia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12yMvUz9Zacb1XzPliXacpcp5YX-NnSaH",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Faiza Try Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17aIAXDQhTgPwqDpcKq9soTbi1lUTz0DB",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gathfan Nadif Ali",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yPLii7ssG5yi8HGtffjKu12JnBHWm9vw",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12Bw_tup-6bVaYoiJPxWsEvMUr9Dqf3zN",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1IWiKEKqeMyO7i227EXR33R_nTCvVFtQr",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Kwa3AMZbERah8-CeO6FuExT4k3SgHAdw",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1W97ajCa6KiWktibT-vXSIfn9zLduZsrO",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=105H1YrHF_gTVwoR-oEgCQnKAJIPbi5G-",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OROlkRV4enAkXBsXDf2g__N7QkUg2_AX",
                "kesan": "Kakak Arini kalem, baik, ramah juga, tapi keliatan tegas gitu.",
                "pesan": "Kak gak mau 3 periode?",
            },
            {
                "nama": "Nabyla Sharfina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1sahIrAvoPAO2a3VghFOuAnNZ3azWs9kH",
                "kesan": "Lucu banget kakak Nabyla, ternyata ramahh.",
                "pesan": "Spill skincarenya dong kak Nabyla.",
            },
            {
                "nama": "Khoirul Muttoharoh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1uf0DlDxsNAtjZwAKxwVXsHboOhaFEQDP",
                "kesan": "Kagum sama Kak Mut bisa lolos Pimnas.",
                "pesan": "Tutor lolos pimnasnya dong kak mut.",
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1U5PPQPxQKafvgSPPWiq_0LRer7BAWBbB",
                "kesan": "Bang Adit sopspoken tapi ramah terus asik juga.",
                "pesan": "Bang energinya keluarin lagii.",
            },
            {
                "nama": "Indah Khairunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14naWF279dIYE695VsnbvDfE7WjC8CCAg",
                "kesan": "Aduhh kak Indah asik banget, sefrekuensi sama aku, suka deh akunya.",
                "pesan": "Ayo kapan kapan bikin jj bareng kak.",
            },
            {
                "nama": "Bima Ekayasa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_bVSql5GNzvCPkzB3ABZhEd45-LsYr-o",
                "kesan": "Bang Bima kalem gitu, bener bener jaga image.",
                "pesan": "Bang pernah teriak enggak?",
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11L3xa3qdpAMsAQF9jHudEzhLAHg08KJS",
                "kesan": "Bang Bimo ramah dan banget bangett terus tinggi juga.",
                "pesan": "Semangat terus kuliah dan lanjut 2 periode gak bang?",
            },
            {
                "nama": "Adinda Deswita Maharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JdgAfyS3ZOJCApA4QZApdlA1sGtNahml",
                "kesan": "Suka banget aku sama warna rambut kakak.",
                "pesan": "Kakak warnain rambut sendiri atau ke salon?",
            },
            {
                "nama": "Yollanda Agustina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VgibjgQenc3_m8eSRy5aEczHeXJsU923",
                "kesan": "Muka kakak gak ngbosenin, jadi suka akuu.",
                "pesan": "Semangat menjalankan tanggung jawab kak.",
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1bPTGSEwqdPmbRN6ayniczf3kqjFhxkiw",
                "kesan": "Kak riska baik dan kecill kaya aku.",
                "pesan": "Semangat menempuh semster baru kak.",
            },
            {
                "nama": "Alfaya Abiyyi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yXVs_Xj05dhtEprXEfep_2MrCh5ix0_D",
                "kesan": "Ku kira abang kalem ternyata salah besar, soalnya keliatan lemes gitu.",
                "pesan": "Emang gitu yaa bang pembawaanya?",
            },
            {
                "nama": "Asri Meilani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1BlY6r4DDgfYejsb4h1XWUHL4BTT6Y60p",
                "kesan": "Kak Mei cantik, baik, ramah, senyum terus.",
                "pesan": "Kak senyum terus yaa, tambah tambah cantik kalo senyum.",
            },
            {
                "nama": "Ahmad Rizky",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1au8o096S7zas0tfdE6iRWTWW8Q9emn1r",
                "kesan": "Bang Ahmad yang sangatt mengispirasi untuk aku.",
                "pesan": "Bang jangan patah semangat bela hak hak kita yaa bang.",
            },
            {
                "nama": "Selma Siti Aisyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tiOybDostHcgDHJSXGSQtUIlbqgokNsx",
                "kesan": "Kakak selma sopspoken, ramah, asik, gak bosen kalo ngomong sama kakak.",
                "pesan": "Kapan-kapan aku boleh main ke rumah kakak engga?",
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1BbP2NvZcq89ibdcLFjcRx-cJOA7TDRI8",
                "kesan": "Kakak ashila tuh kalem tapi tep tep tep soal tanggung jawab.",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Fathya Intami Gusda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1772q-WCK4krlu6-2cM2jpD7m9jJNww2p",
                "kesan": "Kakak ternyata lebih cantik di rlnya.",
                "pesan": "Kakak cantiknya pengmas, luv bangett. Kakak cantik gak mau lanjut 3 periode?",
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1D6rDWPJwVv9AcsTytNC40Giqi54UP7kW",
                "kesan": "Kak Tarii, ramahh, sopspoken tapi bisa bercanda juga.",
                "pesan": "Kalo sidang udang aku yaa kak.",
            },
            {
                "nama": "Danil N Fadillah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CTeXdq912RXglu2kbN7ZrSwi8VFWLBt7",
                "kesan": "Ku kira Bang Danil cool cool dan ganteng gitu, ternyata prank tapi gantengnya rill.",
                "pesan": "Bang kok bis bening perawatannya pake apa bang?",
            },
            {
                "nama": "Favian Arkaanda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1g45jFk16xElR3CI4EGrdVFLWhSpXV3Wn",
                "kesan": "Omaga Bang Pian gak nyangka ku kira imut kalem kayak mukanya, tapi ternyata prank",
                "pesan": "Bang kalo ngasih info yang seru jangan nanggung-nanggung, bikin aku greget.",
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fvlJbnOlYQM5sEWy2nxlcHL3vN03_sx9",
                "kesan": "Bang Yazid ganteng, tan manis gituu.  ",
                "pesan": "Bang tau gak rahasia ini? enggak ya?",
            },
            {
                "nama": "Muhammad Rizaldi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hKFsLiCnqymwFabEfWDB6ARPSo3Gszho",
                "kesan": "Bang Jaldi ramah bangett, terus energinya bikin nyaman gitu.",
                "pesan": "Bang Jaldi paswordnya "Bestie bestie: WELL""",
            },
            {
                "nama": "Saskia Nova Magdalena",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12nym_KId5iaTD0_95xAcwErNAEgICXX7",
                "kesan": "Kak kia kalem tapi kadang kadang bisa ngelawak juga.",
                "pesan": "Kak Kia kapan kapan ayok pulang bareng ke Lamtim.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_eksternal()

elif menu == "Departemen Internal":
    def departemen_internal():
        kating_data = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=128_Ugc-nYJPF2RceKidldo0LYxBoKEM7",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Kharisma Mustika Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1FP8iPsU_ZehX8G519knR0ed1nLoyKppS",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mGxU-6jf-pqxjJjy9fe2hTDxLKfOtixy",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1LsrTTRUJ6REhIZyKWURe9Z4ZRTuadMhC",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1p1g7qcelNcds7nfhSg7uXoLtoEEwrr7E",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ifAiPVsZPasGASnJD4qrx8OwNFXXjfYC",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Cerine Sihotang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1LwMmGUPelx3V84QjjsdN8znkp1xDqk7F",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Jaya Saputra Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19KakqRJpo-wUTOvWe_ZonO1TalU7OP5W",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Najla Nursyifa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rxiQjkAQNsS-UPqIgSov3XSpdOAW0gQJ",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rozak Ramdani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YRHLra92N0O5IQ08KKmO921-_ueO7Tml",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Teresa Christiani Purba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1R3WgjZJNHwfErHIiRQY2AyA6LRmmV1KV",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Audina Fitria",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YRHLra92N0O5IQ08KKmO921-_ueO7Tml",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1KIXk085vduI7mM5AyM55VHLOpg0JbULT",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1d2o-HM5T94XuHQUHa8CoeX_q5N5-TeM2",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Harvinsyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Gzx69N73cxssVx169u-_ZtlwGQVn-TOG",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19hRTcHtrhLy-xGtzh56EK_rmzJqAlQ38",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Zk1SyvCIxNrGdOcU6sHbpRtV-hGRvu_B",
                "kesan": "Sangat shok dan kagum dengan hobbi abang.",
                "pesan": "Semangat terus kuliah dan semoga TA-nya lancar.",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1itjvplAsSMf4WlUIfwUGmYiQB_FxiI2v",
                "kesan": "Kakak baik, cantik dan ramahhh.",
                "pesan": "Jadi pengen coba masakan kakak deh, soalnya aku lagi kangen rumah.",
            },
            {
                "nama": "Afifah Fauziah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vorhsIGACWG1_onbAzrIUG4Rvb-w5T73",
                "kesan": "Kak Afiqah keren karena suka film Marvel.",
                "pesan": "Semoga selalu lancar perjalanan hidup kakak.",
            },
            {
                "nama": "Anadia Carana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TcgHGtDEFS6EANqB1ZsE0ljH460JVpwW",
                "kesan": "Kerenn hobbinya sangat realistis, i like it.",
                "pesan": "Kalo dah jadi ceo angkat aku jadi partner kak.",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MzMMMRk3iY-3xPuUybwwR6Syusr0Nz9I",
                "kesan": "Bang Hasan kalem dan cool.",
                "pesan": "Bang just saran, rambutnya di potong pendek, ganteng rambut pendek soalnya. ",
            },
            {
                "nama": "Layina Ropiqo",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1u3AmoD7yVikd5Ci0tzsizt2KEDKKQMia",
                "kesan": "Suka banget aku sama tahi lalat kakak, lucu gituu.",
                "pesan": "Kak ramah terus yaa, soalnya tambah cantik kalo senyum.",
            },
            {
                "nama": "Mochammad Iqbal Az-Zahir",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-crTWXaKssw5AwznBIuQKXSKW-OTLT9E",
                "kesan": "Bang Iqbal waktu jadi asprak agak nyeremin.",
                "pesan": "Good luck yaa Bang Iqbal.",
            },
            {
                "nama": "Talitha Justine",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AFVE2o8eTnVdh20OOQx3XRenYIS108yJ",
                "kesan": "Baikk dan softspoken.",
                "pesan": "Kapan-kapan ayo nonton bareng kakak.",
            },
            {
                "nama": "Abdillah Fikri Al Pome",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Ot3mPNrmXY3zXcB7FgP0USV4YymBIlpK",
                "kesan": "Bang Pome baikk bangett.",
                "pesan": "Semoga gak stres di semester ini yaa bang.",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WorbTmMoGyd5FdU0q-xBb9Xec3iJSe7E",
                "kesan": "Bang Afdhal keren dan cool.",
                "pesan": "Jaga kesehatan mental dan kesehatan fisik yaa bang.",
            },
            {
                "nama": "Anggun Nita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1xSDRXRRHvicCQhfUz0Ky85ipYtd15NA3",
                "kesan": "Kagum sama proses hijrah Kak Anggun.",
                "pesan": "Semoga selalu istiqomah yaa kakak cantik.",
            },
            {
                "nama": "Della Anisa Fitri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YFUWg5v4-Sdez1XKeEv2hUzcvoCRSI6s",
                "kesan": "Ihh seneng banget soalnya sama sama Lampung Timur.",
                "pesan": "Rekomend olahraga selain lari yg cocok buat aku.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_ssd()

elif menu == "Departemen Medkraf":
    def departemen_medkraf():
        kating_data = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=121hUMhYzMiTRDQNI7YyVfSFMu3YKibAT",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Donna Maya Puspita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pMpM36v2qieZ3X9f_lhKeeh49V_v_cX1",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1R33XH84y2Bl3nq0bIwh9yuJiRdhUF1Ub",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fMrtJxFBz8AzcuQLFD8F-Kn9AQ8DKHzZ",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Raihana Adelia Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YKm7hATns9nNK1FBhP389UdakjmQZpux",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11VJWOh8yOgPRI3hX2TU0wb17FGxWCOQe",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_YNOgckZ9Tcm8CJX5FKvBFChrmOualNc",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1mCWcy-IIDEzlnxHg_i9WCGT0DEzVCGsl",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Allisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dO9S3nz9pevYlkLs-b-vPYIzQ-1Gc344",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Alya Ramadhanti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1A2yf_lpNmGW6T_4UFSG_B202IdzZWHuI",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vuXw21OspWWqjjz6GUfgyohKHUJGpbLY",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Difanya Husakina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=146CDPPRHPm6GpNRi_e7zzAt7ENR1Pgco",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Nazlah Auliya",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1G_W8Aby0wQCsrg_ELxM8dlTu8Sv3Hpqy",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13QPMrbpHHvbmYhULH8vvV6pjhVN_2awl",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Edsel Adya Pradipta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18PXCln8NKL3D88oL4IvPbLF0fhKx7VSV",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14ScLmT7FZjxmFBLGUrlM85eU1u5mdxuC",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VWP_AZIrM28PaloZSthfzJjFcFHWqqZl",
                "kesan": "Kakaknya sangat ramah, humble, dan menginspirasi!",
                "pesan": "Semangat terus kuliah dan menjalankan amanahnya di HMSD!",
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dS19ToDGjudFZd0MG03OOpVd8VLMjqYd",
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
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16Uf1QlmM-_gQXvBzpe9CYfFVSPEUwkYA",
                "kesan": "Gak espek abang dari Maluku.",
                "pesan": "Kalo balik kampung gimana tuh bang?",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1gtgcsxCHOIDawaXArO1VtL8ZrWmqdcm8",
                "kesan": "Dari awal tertuju dengan outpit kakaknya, keren bangett.",
                "pesan": "Tutor outpitnya kakak biar kalcer juga dong kakak.",
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1S5ednhk9VXeZWqjEX8dKYMfWmEnp48d_",
                "kesan": "Salfok juga sama nama abangnya di nama Parisi.",
                "pesan": ""Bang lampung timurnya mana?",
            },
            {
                "nama": "Muhammad Ridwan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-cRFDDQPK6CC5QyfjNY0JxGPFsdfdZXY",
                "kesan": "Abangnya sangat ramah, humble, dan menginspirasi!",
                "pesan": "semangat terus kuliahnya abang, soalnya masalah bakal dateng terus.",
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12Hw_0n3HKw2o_CDAavVrKQpezhlG2dgO",
                "kesan": "Kakaknya cantik dan baik bangett.",
                "pesan": "Semoga kedepannya kakak selalu semangat terus.",
            },
            {
                "nama": "Dafa Elpriza",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1trwZ-lLSAREsp6JBdxPQ1UuCTKFgw0Af",
                "kesan": "Keliatan cool awalnya, tapi ternyata enggak",
                "pesan": "Semangat bertahan d semester 5 ini bang.",
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1O0lsR5Y-TtRfXRbNzecYV42hSAJh5twC",
                "kesan": "Kakaknya ramah dan baik ke aku.",
                "pesan": "Semoga bertahan di semester ini yaa kakak.",
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1iiEuqOipJMBZr-31GKM6l4LFpZllBTmp",
                "kesan": "Abang ini ramahhh.",
                "pesan": "Bang adek NIM aku juga dari Lampung Tengah loo.",
            },
            {
                "nama": "Juwita Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1U9Zwxfpp4tJdKHsWPAwiG7O7kdK50-Ix",
                "kesan": "Kakak Juwita cantik bangett.",
                "pesan": "Spil skincarenya dong kakak.",
            },
            {
                "nama": "Andra Ilham Bintang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1oS4X2bI9O74oDiW2gnqm5fs92nuwk7ft",
                "kesan": "Lucu abangnya setiap liat mukanya senyum terus.",
                "pesan": "Bisa ngomong Bahasa Palembang enggak bang?",
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1xLQXkBxlxrnLC5N2iOPE0yg9Zi1dJ4W1",
                "kesan": "Abangnya pendiemmm bangett.",
                "pesan": "Jangan diem diem yaa bang, cobalah menjadi ekstropet.",
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1sj_HC717epkEvtqy-mIT78_WDlSUt33s",
                "kesan": "Abangnya tinggi dan kayak ada aura rohisnya gitu.",
                "pesan": "Abang pake baju koko cocok banget.",
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1F6EWlmR5Fu3OZvRh4MUJEFTfoBGkvQ9e",
                "kesan": "Kakak baik, cantik, dan ramah.",
                "pesan": "Jaga selalu keramahan kakak yaa.",
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1oXfcu82fhBvEdZujcVwuQjPvOD487eVS",
                "kesan": "Kakaknya cantik dan bening.",
                "pesan": "Suka banget aku sama lesung pipit kak Caca.",
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Yg_2r0P68p9Q5pnTsIVj9RftE3Ex6iaE",
                "kesan": "Abangnya ganteng tapi pendiem gitu.",
                "pesan": "Semoga tetap bertahan sampe lulus ITERA.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_minbak()
