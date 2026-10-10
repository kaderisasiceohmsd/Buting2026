# =========================================================
# BAGIAN SINI YANG HANYA BOLEH DIUBAH
# =========================================================
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

menu = streamlit_menu()
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RPRXY1_sjMuAcDhD0A46aDYlfkQ2CnXW",
            "https://drive.google.com/uc?export=view&id=1jdVwET2zp7CHeChA-vVKx9gtzMfUdivU",
            "https://drive.google.com/uc?export=1fuD4xooOTLVZdFMz7hiojychS2CrjbGQ",
            "https://drive.google.com/uc?export=view&id=1xi8ilNCyKhE5IACbKCcjI2XC7mxcGpjU",
            "https://drive.google.com/uc?export=view&id=1wiWYI_oP_P6Ih95sQ1ANvnG9lfnLA448",
            "https://drive.google.com/uc?export=view&id=1-6X5KDbE1W1WC8jKiNFuWCByUKE_Il48",
        ]
        data_list = [
            {
                "nama": "Muhammad Aqil",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Qois Alfio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoidalfio_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "1234500fadil",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push Rank sampe IMO",
                "sosmed": "@gars_mrp",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Evi defiani",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lamtim",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffifi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Hafsa Fadzilah Arraadhila",
                "nim": "079",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Berenang",
                "sosmed": "@hafsafadhilaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu pak tirta",
                "sosmed": "@lutfiaarmdhn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1f54XEKLV5-_iY0Ke1Amy_8n2lsuTpWrB",
            "https://drive.google.com/uc?export=view&id=1Npve-crpQRsbSWWEiarHjDlkXz2v5uMy",
            "https://drive.google.com/uc?export=view&id=1SXlqNcP7PFbzx62UCp6dmh7LCh0or6Ul",
            "https://drive.google.com/uc?export=view&id=1NFnxXH1iKWic5Mp4dbGtTP9Xx4DC68Xh",
            "https://drive.google.com/uc?export=view&id=1C7TLf81OCP5CfwY7wy6O25kc616G6IjH",
            "https://drive.google.com/uc?export=view&id=17dBnXowQY4puKAesvwkom0NmHYtjQOFS",
            "https://drive.google.com/uc?export=view&id=15DoGub_MvMZN1CO6gb_8hOv6lGIgPvu6",
            "https://drive.google.com/uc?export=view&id=1h_syNDUTRwE9yEntGLAMWhtP1A36c5ga",
            "https://drive.google.com/uc?export=view&id=1UvXJs9C6bqp_N9_2Bak2VJxgRj5SrtY8",
            "https://drive.google.com/uc?export=view&id=1MkYZ6i_A643S8bgQmQ8534gt8A5qpvi9",
            "https://drive.google.com/uc?export=view&id=1VLxmWTsL2RbVgRgKKn_WZ0u0lhHyCpMf",
            "https://drive.google.com/uc?export=view&id=1MLgWgxGJy7rWdIox6yUiJ9dgKbpnpkPW",
            "https://drive.google.com/uc?export=view&id=1_ze0SXyd0BWT4qSr5q3RF1DLeARrWyAV",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal": "Kota Manchester",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu semusim dari marsel",
                "sosmed": "@j__eesie",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupin api baleg di tiktok",
                "sosmed": "@exvoltas",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Gh. Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "19",
                "asal": "Kepulauan Mentawai",
                "alamat": "Owen Kost",
                "hobbi": "Ngoding",
                "sosmed": "@afghanisnt_",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "CTR",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Teluk",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450111",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym sama Koleksi figure, nafas manual",
                "sosmed": "@nagatseee",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Jajan sama nisa, putri, suci",
                "sosmed": "@sekardnwp",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "...",
                "pesan": "..."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DB2rHAmkffUqkrya8F8oZcQ5ky-E7IpU",
            "https://drive.google.com/uc?export=view&id=1A9TvLPFQtnaq0BzwKE6JVH1XeyX7bgp-",
            "https://drive.google.com/uc?export=view&id=1OJ7DriS--Ewwl3ZyG0xt4sMTC5quS4r-",
            "https://drive.google.com/uc?export=view&id=1Tybx2D5I_98OnxxCWinZnjk0b8-CO7S5",
            "https://drive.google.com/uc?export=view&id=1eoPRNOiqrHN13VNiao9jjQ0IuEqrIguS",
            "https://drive.google.com/uc?export=view&id=1LNwmAbHuLnCXLpEq8wxWNh40Sz-rLBCA",
            "https://drive.google.com/uc?export=view&id=1CI2P4dAFMDPRsrYErYKJPZP330WA3ORF",
            "https://drive.google.com/uc?export=view&id=1qOmHUqzqldal4GPoOGrFKMXIgXoU_yEm",
            "https://drive.google.com/uc?export=view&id=1dlDTw7hOo-XTSc1X94HK97YtOcmFutm5",
            "https://drive.google.com/uc?export=view&id=1sLE-dVR8G7XK4_y3fAEeF4QfK2BydGKT",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Airan",
                "hobbi": "Nulis Medium",
                "sosmed": "@fathinahnaazh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tanggerang kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia___",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Nyari jurnal",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "1244500114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik dan nonton film",
                "sosmed": "@dwi_rahmstlnii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen MIKFES":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TgtXdkKN21D8kaL59ZLYa_WPTVIMvavc",
            "https://drive.google.com/uc?export=view&id=1ejIuqpeZ3YK0rpsnmTZylEqPDG6HEIY6",
            "https://drive.google.com/uc?export=view&id=1YVYo_zYWkUh07Tk9pd1F6rzKw3O9c3xC",
            "https://drive.google.com/uc?export=view&id=1MB_IOXFtarTlJ0SIgj5MsnNi4JGXMQs0",
            "https://drive.google.com/uc?export=view&id=16AL3b3SQHurK5FOcuoLv0r1jMOc0Toi2",
            "https://drive.google.com/uc?export=view&id=1P2fzMf_3xo9lvFRPVg674h-EKA6CVTMn",
            "https://drive.google.com/uc?export=view&id=1kIpKvWxQCQrOvpl_hUASNzdu_GSElfXZ",
            "https://drive.google.com/uc?export=view&id=1Kb14SD8UVGHnhFDSKO5iinla8rvfcZbY",
            "https://drive.google.com/uc?export=view&id=1wmMZmcM1kPF05EDQlyT0eGUyQoyLKgCi",
            "https://drive.google.com/uc?export=view&id=1ro19Btx7EGDTDKsWAqK23gZQuI652_Pp",
            "https://drive.google.com/uc?export=view&id=1dT6PlN_zoyfKC--gUCKEChxcmiXE6l0x",
            "https://drive.google.com/uc?export=view&id=1z3TuXBj-8ZCY-D3GNtjwKXbBEL7ePWNm",
            "https://drive.google.com/uc?export=view&id=1P2fzMf_3xo9lvFRPVg674h-EKA6CVTMn",
            "https://drive.google.com/uc?export=view&id=1iy0fTja0KZaqe4v1jWV4TOz9_2oRkAFK",
            "https://drive.google.com/uc?export=view&id=1XZN5UPDIFtDKVjTg74unQGiOF8j4SEFb",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "23",
                "asal": "Sulawesi Tengah",
                "alamat": "Panjang",
                "hobbi": "Mancing",
                "sosmed": "@kevinaja__",
                "kesan": "Sangat menginspirasi dan memimpin dengan baik",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Sangat rapi dan cekatan dalam mengelola administrasi",
                "pesan": "Sukses selalu kak!"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Keren dan selalu memberikan arahan yang jelas",
                "pesan": "Semangat menjalankan tugasnya kak!"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar + menghitung uang",
                "sosmed": "@aayuandriani_",
                "kesan": "Sangat ramah dan aktif berkontribusi",
                "pesan": "Tetap semangat dan sukses terus!"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Jogging",
                "sosmed": "@dafaelpriza_",
                "kesan": "Sangat menyenangkan dan mudah diajak kerja sama",
                "pesan": "Sukses terus perkuliahan dan aktivitasnya!"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Mancing",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Sangat baik dan murah senyum",
                "pesan": "Semangat terus kuliahnya!"
            },
            {
                "nama": "Muhammad Afdal Luthfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Jl. Pulau Damar",
                "hobbi": "Memantau dl tugas",
                "sosmed": "@afdall.03",
                "kesan": "Sangat bertanggung jawab dan fokus",
                "pesan": "Semangat terus kakak!"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Nongkrong di kopken",
                "sosmed": "@slbnzw_",
                "kesan": "Sangat asik dan ceria",
                "pesan": "Tetap semangat kuliahnya ya kak!"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Sangat mengayomi dan membimbing dengan sabar",
                "pesan": "Semangat terus memimpin divisinya kak!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal": "Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Main rubik",
                "sosmed": "@andra.lhm",
                "kesan": "Sangat kreatif dan pintar",
                "pesan": "Sukses selalu kuliahnya!"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live tiktok",
                "sosmed": "@bryantel_",
                "kesan": "Sangat menghibur dan ramah",
                "pesan": "Semangat terus berkarya kak!"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Sangat unik dan bersemangat",
                "pesan": "Tetap semangat dan sukses selalu!"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "Sangat baik dan bersahabat",
                "pesan": "Sukses terus perkuliahannya kak!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Sangat ceria dan menyenangkan",
                "pesan": "Semangat terus ya kak!"
            },
            {
                "nama": "Muhammad Rafka",
                "nim": "124450089",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Kotabaru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Sangat disiplin dan dapat diandalkan",
                "pesan": "Sukses selalu buat perkuliahannya!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aMv9qlfsOuyoPiS2R8NTcgAxozaNZqou",
            "https://drive.google.com/uc?export=view&id=1UqjrZcNLpl09Tz_nF4TAHmhMpYAhXKtz",
            "https://drive.google.com/uc?export=view&id=1hn4PgTaL24skiwubJiRXN8FMc_9vrKno",
            "https://drive.google.com/uc?export=view&id=17d-nP_G08HsSbs60e_Z7fwzLlsQ38dA2",
            "https://drive.google.com/uc?export=view&id=1k2DniopsMXjCT6-kWZOVtWyeb2l9drGn",
            "https://drive.google.com/uc?export=view&id=18r-fmfLgTw20T_3VrkT5S81c57TBtZy3",
            "https://drive.google.com/uc?export=view&id=1X1f9zdjDGzs8bxpmaAyerdTKjY3fQN7g",
            "https://drive.google.com/uc?export=view&id=1idD0yxRZ26xBhd2WjUYvs9moCSU0yEAj",
            "https://drive.google.com/uc?export=view&id=1z6mzgHPVOaHUuHgn2NFf5QtgvIhdqmfk",
            "https://drive.google.com/uc?export=view&id=1Zl7FrDBs1q_1u5ETnETkn5J25Ra5Lrdq",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Baca jurnal, cari jurnal yang berhubungan ta",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450000",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "18",
                "asal": "Padang",
                "alamat": "Hasan 4",
                "hobbi": "Baca jurnal, nonton Marvel",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lamteng",
                "alamat": "Pemda",
                "hobbi": "Nonton yutub",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "20",
                "asal": "Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton dracin",
                "sosmed": "@layinr_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Sumbar",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "124450062",
                "umur": "21",
                "asal": "Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Fishing and game",
                "sosmed": "@Afdhal",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lamutara",
                "alamat": "-",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lamtim",
                "alamat": "Kotabaru",
                "hobbi": "Olahraga",
                "sosmed": "@delaanisafitri",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()
