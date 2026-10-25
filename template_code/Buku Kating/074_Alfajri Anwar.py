from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1fVbdcNtDL9EnqIOj_mgNN44LK8k7bcBo",
        "https://drive.google.com/uc?export=view&id=1h5eAUDPuBkfK5B2wPaIiGl5tJyoVnJeH",
        "https://drive.google.com/uc?export=view&id=12EPPbJo4eqKPPGcCGeDTkaDcJuoy524g",
        "https://drive.google.com/uc?export=view&id=1l3_Y7sxDN3fww3K1Bd4xK3Me0IeF46e5",
        "https://drive.google.com/uc?export=view&id=1HpFYt0K8iMSx-CS6yJi_WrFfujRdIiOv",
        "https://drive.google.com/uc?export=view&id=1JtuaMMWi0pW6-pX2X1wNGl2W9f-B6227",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya keliatan tenang meskipun jadi ketua himpunan dan udah semester 7", "pesan": "Semangat dan semoga amanah selalu bang"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya religius, rajin dzikir dan selalu bawa tasbih", "pesan": "Keren bang jarang banget mahasiswa disini yang hobinya dzikir"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya gampang banget senyum dan ramah", "pesan": "semoga pahalanya banyak kak karena kakak murah senyum banget"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya keliatan kalem dan lemah lembut gitu", "pesan": "jangan lupa istirahat ya bang jangan keseringan mainin surat juga"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya ramah dan baik juga", "pesan": "semoga lulus tepat waktu kak"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya murah senyum dan gampang ketawa", "pesan": "sudah mau semester akhir kak, jaadi semangat ya"},
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1O9sLac8Jr5gmmjLM7nwNX4rq0-L0Caeu",
        "https://drive.google.com/uc?export=view&id=1b5liNx6c5vaHlW9siu_GbCzPJ2pHQT5j",
        "https://drive.google.com/uc?export=view&id=1gSqLICQv6JrSLT4bQI1z1OROP-Zi1CEX",
        "https://drive.google.com/uc?export=view&id=1TqkuimLvIKpMOetoKtnmMw4f4UFSpxsJ",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1hLDsKBT8gTYk40oK-iUmbsNoITqfXylm",
        "https://drive.google.com/uc?export=view&id=1Vtiuy0lfHpLrc3BIfRhtLbrReVMsbeS1",
        "https://drive.google.com/uc?export=view&id=1duG5OJhw34J-g6E6fn_NDXekj3bR028Q",
        "https://drive.google.com/uc?export=view&id=1S7gJPfWM78mlS0KLa08V85j7IVekvxKg",
        "https://drive.google.com/uc?export=view&id=12Gkcnl6yQMw_tYqWAEPEHmav51vRjc73",
        "https://drive.google.com/uc?export=view&id=1AE7gha77N1NTg1vh927w_jRn7yPYSSwr",
        "https://drive.google.com/uc?export=view&id=1Frabe4ucvCGxGP7ahBT_vI_mRauoBQsM",
        "https://drive.google.com/uc?export=view&id=1YV3sqsc316u8go2QlHPNXquhNb5eJ4vY",
    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "abangnya suka banget becanda dan kadang buat jokes jokes", "pesan": "semoga di permudah di semester akhir ini bang"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "12345085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin Lagu Semusim", "sosmed": "@j__eesie", "kesan": "kakaknya aktif banget dan gampang ketawa", "pesan": "Tetap jadi orang yang murah senyum ya kak"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Abang nya pintar banget sampai jadi mapres", "pesan": "Semoga ilmu yang abang miliki bermanfaat ya bang"},
        {"nama": "Gh Mikael Niko Anthoni Setiadi", "jabatan": "Staff Komisi I", "nim": "124450022", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@me._kael", "kesan": "abang nya baik, kece dan agak mirip vocalis band", "pesan": "semoga di beri kelancaran dalam kuliah dan organisasinya"},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Kakaknya baik", "pesan": "sudah mau semester 6, jadi jangan terlalu keseringan mancing ya kak"},
        {"nama": "Givaro Ananta","jabatan": "Kepala Komisi II", "nim": "123450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum Kopi", "sosmed": "@givarooo", "kesan": "Abangnya keren dari segi penampilan dan pola fikirnya", "pesan": "semoga jadi orang yang sukses bang"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen Kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt", "kesan": "Kakaknya baik, ramah dan suka goding", "pesan": "Jangan lupa istirahat ya kak"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "City Earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain", "kesan": "kakaknya rapih dalam berpakaian", "pesan": "tetap jadi pribadi yang selalu berpenampilan baik ya kak, baik di kampus maupun di luar"},
        {"nama": "Jeremia Halim", "jabatan": "Staff Komisi II", "nim": "124450101", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@jeremia_hm", "kesan": "keren banget bang suaranya waktu nyanyi di acara FG", "pesan": "Semoga menjadi penyayi top bang"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@monica_tjg", "kesan": "kakaknya baik banget", "pesan": "semoga menjadi orang yang selalu baik kak"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "Gym / Koleksi Figur", "sosmed": "@nagatsee", "kesan": "abangnya baik dan maskulin banget", "pesan": "lancar selalu bang urusannya"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa,putri,suci", "sosmed": "@sekardnwp", "kesan": "tampang kakaknya agak garang tapi aslinya baik kok", "pesan": "lebih murah senyum lagi ya kak"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa Angin", "sosmed": "@nahaysh", "kesan": "kakaknya baik kok bisa keliatan dari wajahnya", "pesan": "semangat selalu kakak"},
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1orLImq551nHraZ0X4AAOAPZTM9rL5Z-V",
        "https://drive.google.com/uc?export=view&id=1nrDS8IP8A5HoO05xYB4uyhY4Dvbn4R4r",
        "https://drive.google.com/uc?export=view&id=1671S6yjjHBDnfCvGEN9d5CF7GKmMfZV5",
        "https://drive.google.com/uc?export=view&id=1j9CkpEJdOSqdSjg4rK6QDlB93oMpoveD",
        "https://drive.google.com/uc?export=view&id=1gBB7ZZueTgIWA7GZ7xHlmu1Cg-yf7ZCq",
        "https://drive.google.com/uc?export=view&id=1OXsekTpgD8RC5bnRiYrse_PNFvx-k2P4",
        "https://drive.google.com/uc?export=view&id=1Hx97FsSOMD11sTICLZBPqFdnmxdqmHIo",
        "https://drive.google.com/uc?export=view&id=1UgVoMefovNv7B2cQGgndy8zG_8JAwLim",
        "https://drive.google.com/uc?export=view&id=17FiNMgKcw8_-nSKVQosy10XopH6C7R2h",
        "https://drive.google.com/uc?export=view&id=1pMRQWN1UpXrM2ZIGFkRP3R6Z9NfyFmZI",
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "kakaknya Aktif dan suka nampung aspirasi", "pesan": "Makasih kakak dan tim yang sudah mengalirkan aspirasi"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Kepala Biro Aspirasi dan Komunikasi", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya Gaul dan asik", "pesan": "Jangan ngesen kiri kalau mau belok kanan bang"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Staf Biro Aspirasi dan Komunikasi", "nim": "124450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Abang baik, ramah dan Seru", "pesan": "Terus jdi orang yang asik bang"},
        {"nama": "Suci Aulia", "jabatan": "Staf Biro Aspirasi dan Komunikasi", "nim": "124450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Kakaknya ceria dan aktif banget", "pesan": "Semoga dapat Ikan yang besar saat mancing kak"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Biro Aspirasi dan Komunikasi", "nim": "124450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Abangnya Keren penampilannya", "pesan": "Tetaplah dibonceng bang"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Kepala Biro Kajian Strategis dan Propaganda", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Kakaknya punya suara yang imut", "pesan": "Keren kak suaranya"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Staf Biro Kajian Strategis dan Propaganda", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Kakaknya punya energik yang gak abis abis", "pesan": "keren kak, selalu energik setiap saat"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Staf Biro Kajian Strategis dan Propaganda", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "tampang abangnya lumayan garang tapi keliatan gagah juga", "pesan": "Perbanyak senyum ya bang"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Biro Kesekretariatan", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Kakaknya ramah banget", "pesan": "selalu ramah ya kak setiap saat"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Staf Biro Kesekretariatan", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "kakaknya produktif bisa diliat dari hobinya", "pesan": "Terus Produktif dalam hal apa pun kak"},
    ] 
    display_images_with_data(gambar_urls, data_list, key="senator")

elif menu == "Departemen PSDA":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1_LaGRBuUgTJOT9T0zBdeBHyF6msZbaHV",
        "https://drive.google.com/uc?export=view&id=1Qh_48LGHS3R_Az31JRQVcjpTdhb-jJdn",
        "https://drive.google.com/uc?export=view&id=1IFOYEs4gfA5VX5E7gjV2NOEgCX5nK1yF",
        "https://drive.google.com/uc?export=view&id=18DquKiwmaLetQsXaWmsCmpiGQDOVpJZb",
        "https://drive.google.com/uc?export=view&id=1fJyi-RIP7xvBvy5kQHM3baknCu1KdoMA",
        "https://drive.google.com/uc?export=view&id=1zD2NS6YbBX-boYSERjvG_3CMzj6nmOus",
        "https://drive.google.com/uc?export=view&id=1B7NXVqsoDcvWvzHnQebAVw4--DcQ3HwV",
        "https://drive.google.com/uc?export=view&id=1Aapb8JmfykOuQpbeZgLlUd977EiZoHBQ",
        "https://drive.google.com/uc?export=view&id=1ScQc817uB_RvnSJmiYGCL8rqcnGsS-6G",
        "https://drive.google.com/uc?export=view&id=1w-fkHkB3sVAtXiNN5dVhSOCprLvb2Iy-",
        "https://drive.google.com/uc?export=view&id=10wZTJWb5inqC8iuZEaH2fMDpL0lRuhT9",
        "https://drive.google.com/uc?export=view&id=1SLw0z6kqLKP_No8tg0Ih9vlXre-uivK6",
        "https://drive.google.com/uc?export=view&id=19lmiBeWoFiOx8GMAVXY2TOCsweZ0oM6S",
        "https://drive.google.com/uc?export=view&id=1tm0PM2oQ23KvmzSpOGhUSAZ4I7-wh_cS",
        "https://drive.google.com/uc?export=view&id=1qj2Uqsd-yx0SeAHe51_7ab-6U0xeHMUI",
        "https://drive.google.com/uc?export=view&id=152xyIO1wvVB6q063wP8UgzJSSOlc84WV",
        "https://drive.google.com/uc?export=view&id=1PYxrVse-acDNec6GHf4D_lwVHw8G_e-5",
    ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "123450097", "umur": "21", "asal": "Kalianda", "alamat": "Samping kost Haikal", "hobbi": "Naksir cowo cakep", "sosmed": "@arientakhsnl_", "kesan": "Kakaknya punya aura kepemimpinan yang kuat", "pesan": "Lancar selalu ya kak kegiatannya"},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "123450022", "umur": "20", "asal": "Palembang", "alamat": "Pudan Kost", "hobbi": "Pacaran", "sosmed": "@vany.salsabilaa", "kesan": "Kakaknya baik kok", "pesan": "semangat terus kak dalam segala hal"},
        {"nama": "Nobel Nizam Fathirizki", "jabatan": "Kepala Divisi Kaderisasi", "nim": "123450117", "umur": "21", "asal": "Bandar Lampung", "alamat": "Urip", "hobbi": "Sulap", "sosmed": "@nobelnizam", "kesan": "Abangnya keren, rapih dan kece penampilannya jago sulap juga", "pesan": "Semoga Ilmu yang diberikan oleh abang bermanfaat"},
        {"nama": "Afriza Azmi", "jabatan": "Staf Kaderisasi", "nim": "124450110", "umur": "20", "asal": "Lamteng", "alamat": "Sebelah kost Haikal", "hobbi": "Nyebar beras", "sosmed": "@friezazmi", "kesan": "Abangnya heboh banget kalau lagi supporteran", "pesan": "Keren bang energinya kalau lagi supporteran"},
        {"nama": "Ayake Alfatih Ramadan", "jabatan": "Staf Kaderisasi", "nim": "124450108", "umur": "20", "asal": "Solo", "alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung", "hobbi": "Goreng ayam", "sosmed": "@ykeall", "kesan": "Abangnya tegas tapi baik dan gak sombong", "pesan": "semoga apa yang disemogakan tersemogakan bang"},
        {"nama": "Caesar Ozora Alrando", "jabatan": "Staf Kaderisasi", "nim": "124450017", "umur": "21", "asal": "Rahim ibu", "alamat": "Gedung F", "hobbi": "Pengembala anak ayam", "sosmed": "@caesar.oriza", "kesan": "Abangnya agak garang tampangnya tai baik kok aslinya", "pesan": "Perbanyak senyum ya bang"},
        {"nama": "Euodia Meiliana Friedita", "jabatan": "Staf Kaderisasi", "nim": "124450029", "umur": "20", "asal": "Asal asalan", "alamat": "Diatas tanjakan", "hobbi": "Ngekader", "sosmed": "@yudiameilianaa_", "kesan": "Kakaknya punya sifat profesionalitas yang tinggi", "pesan": "Sukses selalu kak hari harinya"},
        {"nama": "Haikal Seventino Tamba", "jabatan": "Staf Kaderisasi", "nim": "124450012", "umur": "25", "asal": "Jambi", "alamat": "Sebelah kontrakan Jemar", "hobbi": "Ngurusin pakan anak ayam", "sosmed": "@_haikaaalll", "kesan": "Abangnya keren, kece dalam berpenampilan", "pesan": "semangat terus bang kuliahnya"},
        {"nama": "Putri Manna Anantama Simbolon", "jabatan": "Staf Kaderisasi", "nim": "124450065", "umur": "18", "asal": "Depok", "alamat": "Nomandenl", "hobbi": "Mancing emosi", "sosmed": "@putrimannaa", "kesan": "Kakaknya baik kok", "pesan": "Lancar terus urusannya"},
        {"nama": "Queenta Thifaal Nabila", "jabatan": "Staf Kaderisasi", "nim": "124450059", "umur": "21", "asal": "Lamteng", "alamat": "Depan pemancingan", "hobbi": "Nyuapin anak ayam", "sosmed": "@queentanaabila", "kesan": "Kakaknya baik", "pesan": "Sukses selalu kuliahnya"},
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi PMA", "nim": "123450114", "umur": "18", "asal": "Palembang Sekayu", "alamat": "Asrama TB 3", "hobbi": "Ngejek orang", "sosmed": "@dsmanhl", "kesan": "Abangnya humoris dan humble banget", "pesan": "Semangat bang dan teruslah humble"},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf PMA", "nim": "124450041", "umur": "19", "asal": "Teluk", "alamat": "Bandar Lampung", "hobbi": "Pilates", "sosmed": "@azzelytn", "kesan": "Kakaknya baik dan ramah", "pesan": "Semoga selalu dipermudah urusannya kak"},
        {"nama": "Charrlindah", "jabatan": "Staf PMA", "nim": "124450037", "umur": "21", "asal": "Jakarta Pusat", "alamat": "Cenderawasih 1", "hobbi": "Ngurus peternakan", "sosmed": "@charrlnn", "kesan": "Pekerja keras dan bertanggung jawab.", "pesan": "Semangat terus dan jangan lupa luangkan waktu untuk diri sendiri."},
        {"nama": "Jeremi Marolop Partogi Situmorang", "jabatan": "Staf PMA", "nim": "124450111", "umur": "16", "asal": "Berlin", "alamat": "Samping kos Rafli", "hobbi": "Mengembala anak ayam", "sosmed": "@jemarrro", "kesan": "Santai dan mudah bergaul.", "pesan": "Tetap semangat dan terus belajar hal baru."},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf PMA", "nim": "124450048", "umur": "18", "asal": "Lampung", "alamat": "Barokah", "hobbi": "Main sama Azel", "sosmed": "@n.bila_a", "kesan": "Ramah dan menyenangkan diajak berteman.", "pesan": "Semoga kuliahnya lancar dan selalu diberi kesehatan."},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf PMA", "nim": "124450007", "umur": "20", "asal": "Sibolga", "alamat": "Samping kos Haikal", "hobbi": "Nonton", "sosmed": "@dearfkvmfl", "kesan": "Kalem dan enak diajak ngobrol.", "pesan": "Tetap semangat dan terus jadi pribadi yang baik."},
        {"nama": "Salavi Naharani", "jabatan": "Staf PMA", "nim": "124450090", "umur": "20", "asal": "Lampung Timur", "alamat": "Jatimulyo", "hobbi": "Minum air putih", "sosmed": "@avi.nhr", "kesan": "Tenang dan apa adanya.", "pesan": "Semangat terus dan tetap jaga kesehatan."}
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1GkDmPwPuCOcrh9rdxRru46n4I9K_p45D",
        "https://drive.google.com/uc?export=view&id=19xOFTy_4sH8rHikkvBwojL6XVsKBnEjW",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1JrUW6LiSm9fp1p0tEsyyvVv_0riGsJTC",
        "https://drive.google.com/uc?export=view&id=1UuMEF3oE4ApRe3JlZQm5wvFsvQ6g8cau",
        "https://drive.google.com/uc?export=view&id=1qHFEjQPEF_M4L4tO8Mh77zEnxq2WqXVE",
        "https://drive.google.com/uc?export=view&id=1Jk6zW99DGwmFJSijVvGgdeSNf1Ldjoih",
        "https://drive.google.com/uc?export=view&id=1FC1Pq2kAxzfoMK97NYRNG2fY8EfsntbO",
        "https://drive.google.com/uc?export=view&id=1w26kbJ1NXEE0DAPFHXmIHmiKSIDToTzH",
        "https://drive.google.com/uc?export=view&id=1nR7gOcXS-SJcSEjA3xm7hgjo0J-33vV2",
        "https://drive.google.com/uc?export=view&id=1jcHJCz6pfkpJ2dCW6UBU5MdszbAXo_pf",
        "https://drive.google.com/uc?export=view&id=1aVJGtf9Y6DyklDgplQdIPFxhrKKbMBLj",
        "https://drive.google.com/uc?export=view&id=1cjWfkHRe4OTVg0IpZ2PSFlSRk1IU7LG_",
        "https://drive.google.com/uc?export=view&id=1Z00qpZi7alGUIMQ-pXcjZ0SA8o9lFfc1",
        "https://drive.google.com/uc?export=view&id=1ZhacuK_MlZGpbQOjmtEfnzr2pQ5x15Hk",
        "https://drive.google.com/uc?export=view&id=1nK8-letlsIefUIDqY5BozWfkcqGlZyxp",
        "https://drive.google.com/uc?export=view&id=1zEl7TGcp2qTR64C3HplEWtQcvNQTvO7b",
        "https://drive.google.com/uc?export=view&id=139gqZ6DlhTJrY1J-VhF8z3ATpRzwAb0Q",
        "https://drive.google.com/uc?export=view&id=1DaoqBbB8T1wg1oaKYLcbrshOvc_sLbC_",
        "https://drive.google.com/uc?export=view&id=1np7Jo873sq3CcGvckBfge23lK1Gk8uc0",
        "https://drive.google.com/uc?export=view&id=1Q8_kk-s_vEpJDVzZl4u0mqM0KzuoWn0d",
        "https://drive.google.com/uc?export=view&id=1Cslt_o6sjlnuuVY75FiTsI-4Xr3PDGDJ",
    ]
    data_list = [
        {"nama": "Fabio Banyu Cyto", "jabatan": "Kepala Departemen", "nim": "123450104", "umur": "21", "asal": "Kedaton", "alamat": "Kedaton", "hobbi": "Ngerjain TA, main game, jalan jalan","sosmed": "@biyokcb", "kesan": "Abangnyaa lucu banget dan nyantai, abangnya juga soft spoken  bangettt ", "pesan": "Semangatt bang TA nyaa!"},
        {"nama": "Tanty Widiyastuti","jabatan": "Sekretaris Departemen MIKFES","nim": "123450094","umur": "21","asal": "Lampung Tengah","alamat": "Airan","hobbi": "Ngelakuin semuanya","sosmed": "@tvnty_","kesan": "Kaka nyaa ceria bangett, lucuuu polll","pesan": "Semangatt TA nya kaa, semoga diberikan kelancaran dalam mengerjakan TA!"},
        {"nama": "Fadil Prasetyo Alfarizzi","jabatan": "Kepala Divisi Professional Skill Development","nim": "123450048.","umur": "21","asal": "Bandar Lampung","alamat": "Bandar Lampung","hobbi": "Gitar","sosmed": "@fadilalfarizzii","kesan": "Abangnya baik poll, pertama kali ketemu abangnya di PIK R jadi salah satu pemateri yang kerenn","pesan": "..."},
        {"nama": "Manuel Frederika","jabatan": "Staf Professional Skill Development","nim": "124450039","umur": "20","asal": "Batam","alamat": "Way kandis","hobbi": "Katama","sosmed": "manuelfdk_","kesan": "Abangnya santai dan seruu bangett diajak ngobrol","pesan": "Semangat selalu ya bang!!"},
        {"nama": "Ni Made Okta Viola Darma Putri","jabatan": "Staf Professional Skill Development","nim": "124450005","umur": "20","asal": "Lampung Tengah","alamat": "Korpri","hobbi": "Travelling","sosmed": "@violaadrtr_","kesan": "Kakanya cantikk banget dan jugaa lucuu","pesan": "Semangat kuliahnyaaa kak, sukses selaluu!!"},
        {"nama": "Risa Romadona","jabatan": "Staf Professional Skill Development","nim": "124450127","umur": "20","asal": "Natar","alamat": "Natar","hobbi": "rolling skate","sosmed": "@risarmdna","kesan": "Kakaknyaa baik dan ramahh bangett","pesan": "Semangatt kuliah dan tugas tugasnyaa yaa kak!"},
        {"nama": "Vannisa Ramadhani","jabatan": "Staf Professional Skill Development","nim": "124450078","umur": "19","asal": "Kepulauan Riau","alamat": "Telung Betung","hobbi": "Nonton KHW","sosmed": "@vunnycaa","kesan": "Kakanyaa baikk bangett lucuu dann ramahh poll","pesan": "Semangat dan sukses teruss kakkk!"},
        {"nama": "Yulia Kristine Malau","jabatan": "Staf Professional Skill Development","nim": "124450119","umur": "20","asal": "Jambi","alamat": "Sabah Balau","hobbi": "Belajar","sosmed": "@krnylee","kesan": "Kakaknyaa lucuuu bangett","pesan": "Semangatt yaa kak kuliahnyaa!!"},
        {"nama": "Akeyla Fairus Shafi","jabatan": "Kepala Divisi Pusat Inovasi dan Kajian Akademik","nim": "123450119","umur": "21","asal": "Bandar Lampung","alamat": "Bandara Lampung","hobbi": "Dengerin Musik","sosmed": "@keyashafi_","kesan": "Abangnyaa kecee dan jugaa asik banget diajak ngobroll","pesan": "Semangat nanti TA nya bangg!"},
        {"nama": "Elsa Sitorus","jabatan": "Staf Pusat Inovasi dan Kajian Akademik","nim": "124450088","umur": "21","asal": "Sumatera Utara","alamat": "Pemda","hobbi": "Gaada hobi karena gaada waktu","sosmed": "_els.a","kesan": "Kakaknyaa ceriaa bangettt","pesan": "semangatt kuliahnyaa yaa kaa!"},
        {"nama": "Fadya Izzatul 'Aini","jabatan": "Staf Pusat Inovasi dan Kajian Akademik","nim": "124450062","umur": "20","asal": "Pringsewu","alamat": "Airan","hobbi": "Makan","sosmed": "@fadyaizzatul_","kesan": "Kakaknyaaa lucuuu bangett, gemesinnnn","pesan": "Semangattt selaluuuu ya kakakk!!"},
        {"nama": "Lovianora Saragih","jabatan": "Staf Pusat Inovasi dan Kajian Akademik","nim": "124450105","umur": "19","asal": "Sumatera Utara","alamat": "Way Huwi","hobbi": "Scroll Tiktok","sosmed": "_loviaa","kesan": "Kakaknya lucuu, gemesin bangett","pesan": "Semangatt selaluu yaa kakk!!"},
        {"nama": "M. Alsi Syahrulloh","jabatan": "Staf Pusat Inovasi dan Kajian Akademik","nim": "124450092","umur": "20","asal": "Kalianda","alamat": "Gedung Harapan","hobbi": "Main Game","sosmed": "@keyashafi","kesan": "Abangnya seru banget kalo lagi ngejelasin, ga bikin ngantuk", "pesan": "Semangat terus bang, sukses selalu!"},
        {"nama": "Sherena Florencia","jabatan": "Staf Pusat Inovasi dan Kajian Akademik","nim": "124450027","umur": "19","asal": "Bengkulu Selatan","alamat": "Belwis","hobbi": "Make up","sosmed": "@sher_renna","kesan": "Kakaknya anggun, murah senyum, dan lucuuu bangett","pesan": "semangattt kuliahnyaa kaa!!"},
        {"nama": "Razin Hafid Hamdi","jabatan": "Kepala Divisi Research & Development","nim": "123450096","umur": "21","asal": "Padang","alamat": "Belwis","hobbi": "Futsal","sosmed": "@razyn.hfd","kesan": "Abangnya keren banget pas ngejelasin, panutan deh", "pesan": "Semangat terus bang, sukses karirnya nanti!"},
        {"nama": "Faiza Try Anjani","jabatan": "Staf Research & Development","nim": "124450075","umur": "19","asal": "Padang","alamat": "Belwis","hobbi": "Baca","sosmed": "@faizaanjanii","kesan": "Kakaknya humble banget padahal ambiss parah", "pesan": "Semangat kuliah dan tugas-tugasnya ya kak!"},
        {"nama": "Gathfan Nadif ALi","jabatan": "Staf Research & Development","nim": "124450001","umur": "20","asal": "Bandar Lampung","alamat": "Rajabasa","hobbi": "Main game","sosmed": "@gathfannadif","kesan": "Abangnya kece, humble, dan gampang diajak ngobrol", "pesan": "Semangat terus bang!"},
        {"nama": "Hafidz Wahdiansyah","jabatan": "Staf Research & Development","nim": "124450064","umur": "20","asal": "Metro","alamat": "Metro Kibang","hobbi": "Ngegame","sosmed": "@apiszzaja_","kesan": "bang mentor tersabar menghadapi kerandoman kelompok kita", "pesan": "Semangat terus bangg, sukses selalu!"},
        {"nama": "Kaleb Filbert Istel","jabatan": "Staf Research & Development","nim": "124450062","umur": "20","asal": "Bandar Lampung","alamat": "Campang Raya","hobbi": "Nge-gym, baca novel","sosmed": "@kelelep_comberan","kesan":"Abangnya penyabar banget pas kita banyak tanya hal sepele, btw innes ngefans banget samaa abangnyaa", "pesan": "Semangat kuliahnya bang, moga berkah ilmunya!"},
        {"nama": "Melva Shaprina Febrianti","jabatan": "Staf Research & Development","nim": "124450087","umur": "19","asal":  "Sumatera Selatan","alamat": "Sukarame","hobbi": "Menari","sosmed": "@melva_fbrt","kesan": "Kakaknya manis banget pas senyum, baik dan asik diajak ngobrol", "pesan": "Semangat kuliahnya kakk"},
        {"nama": "Muhammad Syafiqul Falakh","jabatan": "Staf Research & Development","nim": "124450099","umur": "20","asal": "Lampung Selatan","alamat": "Asrama","hobbi": "Membaca","sosmed": "@syaafiq","kesan": "Abangnya rapi, teliti, dan selalu senyum tiap ketemu", "pesan": "Semangat selalu ya bang, bahagia terus!"},
        {"nama": "Rifky Henry Ferdianto","jabatan": "Staf Research & Development","nim": "124450115","umur": "28","asal": "Rajabasa","alamat": "Balam","hobbi": "Tennis Meja","sosmed": "@henryferdianto","kesan": "Abangnya wibawa tapi gokil, seru banget kalau berdiskusi", "pesan": "Semangat kuliahnya bang, lancar jaya"},
    ]
    display_images_with_data(gambar_urls, data_list, key="mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=12gltKb0u47SSXS0AdybpTW8gsgT-PJJ7",
        "https://drive.google.com/uc?export=view&id=1lKLds4z1vjwe7Vi5CxS496W8asrxsA8N",
        "https://drive.google.com/uc?export=view&id=1X0LFmPLuHFFpC9YvabA7yqX8higuMaxH",
        "https://drive.google.com/uc?export=view&id=1yNVj4PUy4IjllMMoTL2iBgoQpwkB07GE",
        "https://drive.google.com/uc?export=view&id=1enSvuub0CvSkA9AcDczoEjwRYji244U5",
        "https://drive.google.com/uc?export=view&id=1Krq4AaG1RYRvQfMpzJKYn8eFhJ2U9Qhg",
        "https://drive.google.com/uc?export=view&id=1kMB9sFOC9iUewwf3g1eqyPFcdInZ7iHl",
        "https://drive.google.com/uc?export=view&id=1WlGL_3JBoGKfvaJ1YpDhGhhk_ERvOb9F",
        "https://drive.google.com/uc?export=view&id=1WiPRZhlIFAFXZ0ANa5EjSUZwbQ932uWe",
        "https://drive.google.com/uc?export=view&id=1TMBqCe-jDE9bzheeVHLOg03LA4h-ahlM",
        "https://drive.google.com/uc?export=view&id=1K03xYUbFS2H0wPceTPIsU8dmUGkb6cIy",
        "https://drive.google.com/uc?export=view&id=1zRYV33hR4IyUB6f6IidO9nsFxKPzJ5Ew",
        "https://drive.google.com/uc?export=view&id=1MD5UVO9m-tv2UB0fJP1nI-PnrQKHzedP",
        "https://drive.google.com/uc?export=view&id=1-sZTRl503zi5uxv7VaSmIaicniZ0y3gQ",
        "https://drive.google.com/uc?export=view&id=17wRsf488SsSgX4y4uaH7sc-FEG5_SfAb",
        "https://drive.google.com/uc?export=view&id=1GbJddaGIbazKoGDbjeboQa-erGo7EtGk",
        "https://drive.google.com/uc?export=view&id=1JxAD3i-UAVGnpeTVafzaWLWIGBpm4phB",
        "https://drive.google.com/uc?export=view&id=12FIKj2LHvh-wF_73K6pQzSKJG0aSIlP6",
        "https://drive.google.com/uc?export=view&id=10apMk99cPTt5xRKzcHRAxozyoumGrIzR",
        "https://drive.google.com/uc?export=view&id=1z_GJHeWW7LHy3iaNyB-8sxeqA49k-M3q",
        "https://drive.google.com/uc?export=view&id=1aXUBI_O2xlkBooDPS9FEyEeDgS4ABAmO",
        "https://drive.google.com/uc?export=view&id=1PwgN6MoB47GwYwfAT--wknoszLzoAKsD",
    ] 
    data_list = [
        {"nama": "Arini Puteri Elandra", "jabatan": "Kepala Departemen Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Kakaknya imut dan murah senyum banget, bikin adem", "pesan": "Semangat TAnya kak, sukses terus!"},
        {"nama": "Nabyla Sharfina", "jabatan": "Sekretaris Departemen Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "Kakaknya friendly parah, serasa ngobrol sama temen sebaya", "pesan": "Semangat TA nya kak!"},
        {"nama": "Khoirul Muttoharoh", "jabatan": "Kepala Divisi Hubungan Luar", "nim": "1234500", "umur": "-", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Main", "sosmed": "@khoirul_muttoharoh", "kesan": "Kakaknya pandai mencairkan suasana pas lagi pada pusing", "pesan": "Semangat TA-nya kak, cepat nyusul wisuda!"},
        {"nama": "Ahmad Rizky", "jabatan": "Staf Ahli Hubungan Luar", "nim": "123450050", "umur": "21 Tahun ini Alhamdulillah", "asal": "Tangerang Selatan", "alamat": "GH", "hobbi": "Ngga ngapa ngapain", "sosmed": "@ahmad.rizky__", "kesan": "Abangnya charismatic banget pas ngomong di depan publik, keren sekaligus jadi panutan!", "pesan": "Semangat dan sukses selalu ya bang!"},
        {"nama": "Adinda Deswita Maharani", "jabatan": "Staf Hubungan Luar", "nim": "124450083", "umur": "10", "asal": "Lampung", "alamat": "Sukabumi", "hobbi": "Jadi idol", "sosmed": "@adindaadma", "kesan": "Kakaknya positive energy banget, selalu bikin suasana jadi ceria", "pesan": "Semangat kuliahnya kakkk!!"},
        {"nama": "Ahmad Bimo Akbar Arkana", "jabatan": "Staf Hubungan Luar", "nim": "124450113", "umur": "-", "asal": "Tanggamus", "alamat": "Bandar lampung", "hobbi": "Lihat lihat perumahan", "sosmed": "@bimo_arkana", "kesan": "Kaget abangnyaa tinggi bangettt", "pesan": "Semangatt selaluu yaa bangg!"},
        {"nama": "Alfaya Abiyyi", "jabatan": "Staf Hubungan Luar", "nim": "124450006", "umur": "nelson piquet", "asal": "Balam", "alamat": "Balam", "hobbi": "Makan yang manis biar manis", "sosmed": "@alfabiyi", "kesan": "Abangnya asik diajak diskusi, pembawaannya tenang dan solutif", "pesan": "Semangat terus bangg, sukses selalu!"},
        {"nama": "Asri Meilani", "jabatan": "Staf Hubungan Luar", "nim": "124450010", "umur": "20", "asal": "Lampung barat", "alamat": "Korpri raya", "hobbi": "Nonton film", "sosmed": "@asrmeilani", "kesan": "Kakaknya adalah kating pertama dari sains data yang akuu temuinn dan ketemunyaa di kolo garden(kebetulan yang sangat kebetulann <3), kakaknya gemesin, lucuu, dan baik beneran, ga pernah keliatan marah atau cemberut", "pesan": "Semangat kuliahnya kak, stay happy!"},
        {"nama": "Bima Ekayasa", "jabatan": "Staf Hubungan Luar", "nim": "124450106", "umur": "-", "asal": "Lampung", "alamat": "Bandar lampung", "hobbi": "Berlaku humoris dan manis", "sosmed": "@bimayasa_", "kesan": "Abangnya keliataan cool tapi asik bangett diajak ngobroll", "pesan": "Semangat terus bangg!"},
        {"nama": "Indah Khairunnisa", "jabatan": "Staf Hubungan Luar", "nim": "124450077", "umur": "20", "asal": "Ampera", "alamat": "Disini aja", "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang", "sosmed": "@khaindaa_", "kesan": "Kakak nya random bangett, lucuuu poll", "pesan": "Semangat selalu yaaa kakk!!"},
        {"nama": "Riska Erlis Dayu Tiara", "jabatan": "Staf Hubungan Luar", "nim": "124450022", "umur": "20", "asal": "Palembang", "alamat": "Bebas", "hobbi": "Ngefollow-up chat", "sosmed": "@erlsriska", "kesan": "Kakaknya positive vibes banget, selalu nularin semangat ke kita", "pesan": "Semangat terus kakk, stay humble and happy!"},
        {"nama": "Yollanda Agustina", "jabatan": "Staf Hubungan Luar", "nim": "124450024", "umur": "-", "asal": "Kerangka bawang sebelah barat", "alamat": "Kayu mulya", "hobbi": "Tanya bang henry", "sosmed": "@yollanda_agustina16", "kesan": "Kakak nya baikk banget, sering ngasih semangat dan motivasi", "pesan": "Semangat selalu kak, makasih banyak bantuannya!"},
        {"nama": "Aditya Taufiqurrohman", "jabatan": "Kepala Divisi Pengabdian Masyarakat", "nim": "123450032", "umur": "-", "asal": "Tetangga kadep", "alamat": "Belwis", "hobbi": "Memancing keributan", "sosmed": "@adityatfq", "kesan": "Abangnya humoris, ada aja candaannya pas lagi wawancara", "pesan": "Semangat selalu bang"},
        {"nama": "Fathya Intami Gusda", "jabatan": "Staf Ahli Pengabdian Masyarakat", "nim": "123450095", "umur": "-", "asal": "Tangsel", "alamat": "Sukarame", "hobbi": "Baca wattpad", "sosmed": "@fatthyaa_", "kesan": "Kakaknya manis banget pas senyum, baik dan asik diajak ngobrol", "pesan": "Semangat kuliahnyaa kakk"},
        {"nama": "Tarisya Hidayatul Rahmi", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450052", "umur": "-", "asal": "Luhak tanah data", "alamat": "gerbar", "hobbi": "Jadi orang baik", "sosmed": "-", "kesan": "kakaknya lucuu", "pesan": "tetep jadi asprak yang keren ya kak"},
        {"nama": "Ashila Islamisahfa Vanisha", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450028", "umur": "20", "asal": "Sini", "alamat": "Jauh pokoknya", "hobbi": "Tidur", "sosmed": "@kshigf", "kesan": "Kakaknya murah senyum dan cantikk bangett", "pesan": "Semangat kuliahnya kak, moga dipermudah urusannya!"},
        {"nama": "Danil N Fadillah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450103", "umur": "-", "asal": "Karawang", "alamat": "belakang polda", "hobbi": "Ngasi makan ikan cupang", "sosmed": "@d4niel_fdlh", "kesan": "Abangnya vibenya abangable banget, seruu banget diajak ngobrol", "pesan": "Semangat terus bang, sukses selalu kedepannya!"},
        {"nama": "Favian Arkaanda", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450021", "umur": "-", "asal": "Swiss", "alamat": "Tanya bapas", "hobbi": "Ngesen kanan", "sosmed": "@fvnnn05", "kesan": "Abangnya lucu dan solutif, dan juga soft spoken", "pesan": "Semangat dan sukses selalu bang!"},
        {"nama": "Muhammad Fathiy Zumar Yazid", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450081", "umur": "20", "asal": "Situlah", "alamat": "Pohon mulya", "hobbi": "Nyari hobi", "sosmed": "@zydddddd__", "kesan": "Hebat dan tegas", "pesan": "selalu jadi orang keren dan ramah tamah"},
        {"nama": "Muhammad Rizaldi", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450093", "umur": "masih mudalah", "asal": "Rahim ibu", "alamat": "Pasar lantai 3.5", "hobbi": "Gambarr", "sosmed": "@jaldii._", "kesan": "abang mc pplk 2025, abangnya kocak banget, bikin suasana wawancara jadi cair", "pesan": "Semangat selalu bangg, sukses terus ya!"},
        {"nama": "Saskia Nova Magdalena", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450074", "umur": "20", "asal": "Banyak begal", "alamat": "Pinggir jalan", "hobbi": "Nonton Tinkerbell", "sosmed": "@snova.19", "kesan": "Kakaknya positive vibes dan orangnyaa lucuu", "pesan": "Semangat selalu kak, moga makin bersinar!"},
        {"nama": "Selma Siti Aisyah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450044", "umur": "20", "asal": "Lampung", "alamat": "Balam", "hobbi": "Jalan jalan", "sosmed": "@selmasiti_aisyah", "kesan": "Kakaknya manis, murah senyum, dan lucuu banget", "pesan": "Semangat kuliahnya kak, moga lancar urusannya!"},
    ] 
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1jPeN_evGbdLn57baXWnzuh7PE0ndbjOp",
        "https://drive.google.com/uc?export=view&id=1ruhlJAoITApJXBmfzOouKyEZbcLrGr1a",
        "https://drive.google.com/uc?export=view&id=11xkVLH44BIbI-jGBRWpvmn41r2pjEH9M",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1xgC1SHX5OkCAjXjoH7WtCaYL98MHr1_T",
        "https://drive.google.com/uc?export=view&id=1xSPT55idf0TIlwZegAsRiBUPiZJliREa",
        "https://drive.google.com/uc?export=view&id=1EzXI_JlohfhDghLRPVK0Tfr4T7ZYdaf7",
        "https://drive.google.com/uc?export=view&id=1coginEB51EMcRpWXHozBNQ5rAGkXjxOY",
        "https://drive.google.com/uc?export=view&id=1-tqf_KAjuPJsZVc_dgSf7UvN2FeRA881",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1urI1RZH3NLqvgf0hUMWW3by9Tg4lNPvG",
        "https://drive.google.com/uc?export=view&id=1BKF-MEFLeYSJHElB2jdG57FTLaKAl2OU",
        "https://drive.google.com/uc?export=view&id=1jqbpBPbwlcnZcVcs9WJlZGE1W2Jr1L5S",
        "https://drive.google.com/uc?export=view&id=1JSBdDGSFCk-rPQSZZeBD6U828hwj0R4p",
        "https://drive.google.com/uc?export=view&id=1-pa4mws5yadAjdVtISU6jZbGWD30cPed",
        "https://drive.google.com/uc?export=view&id=1sE8MJVefRvSpJMtyMVPZjnMv2mx32h07",
    ]
    data_list = [
        {"nama": "Haikal Fransisko Simbolon", "jabatan": "Kepala Departemen Internal", "nim": "123450106", "umur": "20", "asal": "Jambi", "alamat": "Way Halim", "hobbi": "Ngeledek Orang", "sosmed": "@haikalsbln", "kesan": "Abangnya simpel, keren dan baik banget", "pesan": "waduh untuk hobi ngeledek orangnya agak kurangi ya bang"},
        {"nama": "Kharisma Mustika Sari", "jabatan": "Sekretaris Departemen Internal", "nim": "123450034", "umur": "21", "asal": "Way Kanan", "alamat": "Untung Senopati", "hobbi": "Suka Nolong Orang", "sosmed": "@rismaa.mustika_", "kesan": "Kakaknya Baik dan suka menolong", "pesan": "tetap menjadi penolong yang tanpa pamrih ya kak"},
        {"nama": "Hanna Gresia Sinaga", "jabatan": "Kepala Divisi Keharmonisasian", "nim": "123450038", "umur": "21", "asal": "Sumatera Utara, kisaran city", "alamat": "Sukarame", "hobbi": "Ngabarin Orang Tua", "sosmed": "@hanna_g_sinaga", "kesan": "Kakaknya Aura Positif Banget serius, asik, baik dan ramah", "pesan": "Semoga kakak sehat selalu dan dilingungi oleh tuhan"},
        {"nama": "Ahmad Farhan Ghani", "jabatan": "Staf Ahli Keharmonisasian", "nim": "123450121", "umur": "21", "asal": "Kemiling", "alamat": "Kemiling", "hobbi": "Supporteran", "sosmed": "@farhanghani", "kesan": "Abangnya jago banget main bas", "pesan": "semoga jadi drumber profesional dan terkenal bang"},
        {"nama": "Aisyah Khairun Nisa", "jabatan": "Staf Keharmonisasian", "nim": "124450096", "umur": "18", "asal": "Indragiri", "alamat": "Samping Makam Perwira 2", "hobbi": "Nyicipin Makanan", "sosmed": "@aisyahkhair._", "kesan": "Kakaknya baik dan lemah lembut", "pesan": "Selalu lemah lembut jika dibutuhkan kak"},
        {"nama": "Cerine Sihotang", "jabatan": "Staf Keharmonisasian", "nim": "124450049", "umur": "20", "asal": "Medan", "alamat": "Belwis", "hobbi": "Suka Ngoding pakai R", "sosmed": "@cerine_ipynb", "kesan": "Kakaknya Aktif dan selalu ceria", "pesan": "Terus jadi orang yang ceria dan membawa aura positif untuk orang lain kak"},
        {"nama": "Jaya Saputra Tamba", "jabatan": "Staf Keharmonisasian", "nim": "124450094", "umur": "18", "asal": "Medan", "alamat": "Pemda", "hobbi": "Mencari Nafkah", "sosmed": "@jay.saputra.mb", "kesan": "Abangnya asik dan kece gitu", "pesan": "Semoga Lancar bang nyari nafkah nya dan jangan lupa pulang"},
        {"nama": "Najla Nursyifa", "jabatan": "Staf Keharmonisasian", "nim": "124450051", "umur": "20", "asal": "Sumatra Barat", "alamat": "Belwis", "hobbi": "Nonton ASMR", "sosmed": "@njlanursyifa", "kesan": "Kakaknya Kalem dan ramah", "pesan": "selalu baik dimanapun dan kapan pun ya kak"},
        {"nama": "Rozak Ramdani", "jabatan": "Staf Keharmonisasian", "nim": "124450100", "umur": "19", "asal": "Kalianda, Lampung Selatan", "alamat": "Korpri Raya", "hobbi": "Berantemin Kucing", "sosmed": "@rozakrabbani__", "kesan": "Abangnya asik dan suka becanda", "pesan": "Jangan ngadu kucing lagi bang"},
        {"nama": "Teresa Christiani Purba", "jabatan": "Staf Keharmonisasian", "nim": "124450046", "umur": "19", "asal": "Riau", "alamat": "Belwis", "hobbi": "Masak", "sosmed": "@kristiani8872", "kesan": "Kakaknya pintar dan sering banget jadi asprak atau gak astut", "pesan": "Semoga manfaat ilmunya ya kak"},
        {"nama": "Muhammad Hanif Dzaky Arifin", "jabatan": "Kepala Divisi Kerohanian", "nim": "123450064", "umur": "21", "asal": "Padang", "alamat": "Way Kandis", "hobbi": "Nonton F1 & MotoGP", "sosmed": "@hnfdzky_", "kesan": "Abangnya santai kalem dan tenang", "pesan": "sukses selalu bang hanif"},
        {"nama": "Audina Fitria", "jabatan": "Staf Kerohanian", "nim": "124450038", "umur": "20", "asal": "Sumatra Barat", "alamat": "Sukarame", "hobbi": "Masak", "sosmed": "@audinaf_03", "kesan": "Kakaknya baik dan ramah", "pesan": "Sehat sehat orang baik"},
        {"nama": "Cika Adelia Br Marbun", "jabatan": "Staf Kerohanian", "nim": "124450107", "umur": "20", "asal": "Bagan Batu, Riau", "alamat": "Belwis", "hobbi": "Dengerin Musik", "sosmed": "@cikamrbn", "kesan": "Kakaknya murah senyum banget liat aja di foto", "pesan": "Semoga selalu menjadi orang yang murah senyum kak"},
        {"nama": "Gustin H Tampubolon", "jabatan": "Staf Kerohanian", "nim": "124450068", "umur": "21", "asal": "Sumatera Utara", "alamat": "Airan", "hobbi": "Nonton", "sosmed": "@gustinhaleluya", "kesan": "Kakaknya Ramah kok", "pesan": "Lanacar lancar ya kak kuliahnya"},
        {"nama": "Muhammad Harvinsyah", "jabatan": "Staf Kerohanian", "nim": "124450128", "umur": "20", "asal": "Sumatera Selatan", "alamat": "Belwis", "hobbi": "Ngadu Ikan Cupang", "sosmed": "@muhvinz_", "kesan": "Abangnya simpel dan kalem juga", "pesan": "waduh jangan ngadu cupang lag bang kesian cupangnya"},
        {"nama": "Rafa Sabina Fahimah", "jabatan": "Staf Kerohanian", "nim": "124450036", "umur": "20", "asal": "Natar", "alamat": "Natar", "hobbi": "Nonton Drakor", "sosmed": "@snasaa._", "kesan": "Kakaknya baik dan ramah", "pesan": "ramah selalu ya kak"}
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=14hcL8FhtwwqBQfkM9B5YZQJGqqLb8D-S",
        "https://drive.google.com/uc?export=view&id=1rjhAWLRLAhtn1DJFyChOW-w0gVbDNJdz",
        "https://drive.google.com/uc?export=view&id=1JuDaB8f6ypNAey0_RH8X4aW7TKBBG3fl",
        "https://drive.google.com/uc?export=view&id=1x-Vxo9k_fqZBOSCcK1C44EgpbOywa4Gg",
        "https://drive.google.com/uc?export=view&id=1wrwo39xhMDWyZS22SR6yUR3P2F-MtQgO",
        "https://drive.google.com/uc?export=view&id=10FauwZ8w62Uf2ICNgxi8gZVjsXVnN3vN",
        "https://drive.google.com/uc?export=view&id=1oZHVrvfsoxEpKFXcdkNew_Za6fX5aHTZ",
        "https://drive.google.com/uc?export=view&id=1mo5kbI30uTnxNsqu24RaBcfgxGakDsm9",
        "https://drive.google.com/uc?export=view&id=15Oba8SQ5vqA5pfV7EJcIld5ZePLEe8sz",
        "https://drive.google.com/uc?export=view&id=1cDh7BJEOpzfEkv0lP9zyILk1p7rvg5d5",
        "https://drive.google.com/uc?export=view&id=1NjG9jhrTbZBnkseLVLPQhuVy-yJP6Skn",
        "https://drive.google.com/uc?export=view&id=1qAtFg84Mbmj_ZJNVLt-400ggYtD1fln-",
    ] 
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Kepala Departemen SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Abangnya ramah, asik dan suka banget becanda", "pesan": "Semangat bang semoga jualannya laris manis"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Sekretaris SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Kakaknya suka becanda kayak marah marah dan tensi gitu", "pesan": "Lancar selalu urusannya kak"},
        {"nama": "Afifah Fauziah", "jabatan": "Kepala Divisi Kemitraan", "nim": "12345002", "umur": "19", "asal": "Sumatera Barat", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "Kakaknya ramah baik dan tidak sombong", "pesan": "Semoga tamat nonton marvelnya kak!"},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Staf Kemitraan", "nim": "124450013", "umur": "20", "asal": "Lampung Tengah", "alamat": "Sebelah Kosan Ayake", "hobbi": "Nonton Youtube", "sosmed": "@hasan.ramadhan08", "kesan": "Abangnya kalem dan soft spoken gitu", "pesan": "Soft spoken selalu ya bang"},
        {"nama": "Layina Ropiqo", "jabatan": "Staf Kemitraan", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "Kakaknya asik dan ramah", "pesan": "Semangat selalu kak di setiap aktivitasnya"},
        {"nama": "Moch. Iqbal Az-Zahir", "jabatan": "Staf Kemitraan", "nim": "124450052", "umur": "20", "asal": "Bekasi", "alamat": "Natar", "hobbi": "Nonton Drakor", "sosmed": "@iqbalazzahir_", "kesan": "Abang jago ngoding banget dan jadi asdos dulu di prak alpro", "pesan": "Semoga manfaat ilmunya bang"},
        {"nama": "Talitha Justine", "jabatan": "Staf Kemitraan", "nim": "122450076", "umur": "19", "asal": "Jakarta", "alamat": "Pemda", "hobbi": "Nonton", "sosmed": "-", "kesan": "Kakaknya lucu dan baik banget", "pesan": "lancar dan sukses selalu ya kak"},
        {"nama": "Anadia Carana", "jabatan": "Kepala Divisi Kewirausahaan", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "Kakaknya pekerja keras bisa diliat dari hobinya", "pesan": "Semangat kak nyari duitnya"},
        {"nama": "Abdillah Fikri Al pome", "jabatan": "Staf Kewirausahaan", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@pomest__", "kesan": "Abangnya kece dan jago basket", "pesan": "keren bang kece selalu bang"},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Staf Kewirausahaan", "nim": "124450008", "umur": "20", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Fishing", "sosmed": "@dhal_setiawan", "kesan": "Abangnya simpel dan apa adanya", "pesan": "Semangat bang semester 5 nya"},
        {"nama": "Anggun Nita", "jabatan": "Staf Kewirausahaan", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa", "kesan": "Kakaknya murah senyum dan baik banget", "pesan": "keren kak masih menjaga kebiasaan waktu kecil yaitu nonton kartun"},
        {"nama": "Della Anisa Fitri", "jabatan": "Staf Kewirausahaan", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Kakaknya baik dan ramahh banget", "pesan": "Semoga cepat ketemu hobinya kak"},
    ] 
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1Dwc_wTvKyiNZGs8zr5PaFaq13TJodwP_",
        "https://drive.google.com/uc?export=view&id=1yJ3rK3Sk67MlxzxFtnticSMfXMfMSO0f",
        "https://drive.google.com/uc?export=view&id=1FMgfIziI6s_eHdPhAvcz4KXNRdIMNAdA",
        "https://drive.google.com/uc?export=view&id=1PkJKppQTOfrSQxXOdirqs-1ZppTW85bp",
        "https://drive.google.com/uc?export=view&id=1pc-hFmULGT_Mm4lwV06anerlPDEgf5Wd",
        "https://drive.google.com/uc?export=view&id=1Qkd1wvcA4GZQLyrLrhRyKy3fUcHsvpAW",
        "https://drive.google.com/uc?export=view&id=1KEVZNBNwc2l_WA5rIkQ-3c1OiD67ZM6g",
        "https://drive.google.com/uc?export=view&id=1o9qCmQLOhGAdCSKXeeruEj5RhAWUmNTC",
        "https://drive.google.com/uc?export=view&id=1RQOcsXdD-kFYOYE9bdMR1EOsh69VRz9g",
        "https://drive.google.com/uc?export=view&id=1lXzPqbD9WSV4zhfVeqQESdCUMakW0-ky",
        "https://drive.google.com/uc?export=view&id=1V1Og56j1hLWclP0i2ejvAU_OpZOsHcxN",
        "https://drive.google.com/uc?export=view&id=1HzatuJUprH-pEYcOM1OdNwubhxnSmfX3",
        "https://drive.google.com/uc?export=view&id=1r_Ki_IqYCBgD6Im3aUuzvkiKbv-KKs4T",
        "https://drive.google.com/uc?export=view&id=1hfVRRVwvASqOeOx-U1ISic5YZkqQ2RWs",
        "https://drive.google.com/uc?export=view&id=1jRD4vuZKTI-48jW3tZCzLxul3QETXOxA",
        "https://drive.google.com/uc?export=view&id=1qfAhxaNh2zGah9AQF35JLOjplJB4qxXQ",
        "https://drive.google.com/uc?export=view&id=1__yIZ-MbRX1TiWLK1uqerEU92WbvPBHh",
        "https://drive.google.com/uc?export=view&id=1loJIhnxwnh8QaKUMLtXeDf8D8I_N4FY5"
    ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Kepala Departemen Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kakaknya ramah dan lucu", "pesan": "Semangat TA nya kak"},
        {"nama": "Donna Maya Puspita", "jabatan": "Sekretaris Departemen Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kakaknya baik dan ramah", "pesan": "semangat selalu kak di setiap kondisi"},
        {"nama": "Labo John Noel Napitupulu", "jabatan": "Kepala Divisi Dokumentasi", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "abangnya simpel tapi kece dan gaul banget", "pesan": "semoga di permudah kuliahnya bang"},
        {"nama": "Anash Tasya Ausyaqila", "jabatan": "Staf Dokumentasi", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "Kakaknya murah senyum banget", "pesan": "tetap jadi orang yang murah senyum ya kak"},
        {"nama": "Felisya Nabila Putri Nugroho", "jabatan": "Staf Dokumentasi", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kakaknya imut dan lucu", "pesan": "Jangan keseringan mancing emosi orang ya kak"},
        {"nama": "Muhammad Razan Maulana Pratama", "jabatan": "Staf Dokumentasi", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Abangnya jago fotografi dan main panah", "pesan": "keren bang semoga jadi fotografer profesional"},
        {"nama": "Sania Dwi Ayu Lestari", "jabatan": "Kepala Divisi Media dan Konten Spesialis", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kakaknya produktif dan rajin", "pesan": "semoga lancar kegiatannnya kak"},
        {"nama": "Allisha", "jabatan": "Staf Media dan Konten Spesialis", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kakaknya mudah banget ketawa dan asik", "pesan": "Selalu jadi orang yang asik ya kak"},
        {"nama": "Alya Ramadhanti", "jabatan": "Staf Media dan Konten Spesialis", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kakaknya energetik banget pantes hobinya main futsal", "pesan": "Keren kak aku baru nemu perempun main futsal"},
        {"nama": "Bunga Clarisa Sefa", "jabatan": "Staf Media dan Konten Spesialis", "nim": "124450097", "umur": "20", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kakaknya positif vibes kayak namanya", "pesan": "semoga positive vibesnya gak pudar"},
        {"nama": "Difanya Husakina", "jabatan": "Staf Media dan Konten Spesialis", "nim": "124450043", "umur": "20", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kakaknya the real perantau", "pesan": "Semoga apa yang diusahakan terwujud ya kak"},
        {"nama": "Nazlah Auliya", "jabatan": "Staf Media dan Konten Spesialis", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kakaknya Imut dan lucu", "pesan": "Lancar selalu urusannya kak"},
        {"nama": "Raihana Adelia Putri", "jabatan": "Kepala Divisi Visual Design", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "Kakaknya produktif banget bisa diliat dari hobinya", "pesan": "semoga selalu produktif kak"},
        {"nama": "Daffa Kharisma Adzana", "jabatan": "Staf Visual Design", "nim": "124450061", "umur": "21", "asal": "Surabaya", "alamat": "Sukarame", "hobbi": "Editing & Foto", "sosmed": "@daffascript", "kesan": "abangnya super sibuk dan serba bisa", "pesan": "Keren bang walaupun sibuk tapi gak pernah ngeluh"},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Visual Design", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Abangnya mirip sama temen SMA ku dulu", "pesan": "Kurangi Scrolling ya bang"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Visual Design", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kakaknya ramah banget", "pesan": "Tetap jadi orang yang ramah selalu kak"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Visual Design", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kakaknya punya aura yang bagus", "pesan": "semoga auaranya menular ke orang lain"},
        {"nama": "Zannuba Arifah Ilman", "jabatan": "Staf Visual Design", "nim": "124450112", "umur": "18", "asal": "Lampung Timur", "alamat": "Rajabasa", "hobbi": "Bengong", "sosmed": "@xifasky", "kesan": "Kakaknya baik banget", "pesan": "Jangan keseringan bengong ya kak"},
    ] 
    display_images_with_data(gambar_urls, data_list, key="medkraf")

elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1vR91vzjU2omTqVhtKP72-HovGkFTdrTG",
        "https://drive.google.com/uc?export=view&id=1H5QGKx6l6Y-e8OWE0nVXmbuVl4Rt_dSB",
        "https://drive.google.com/uc?export=view&id=1y15WBuyGjVY7Xd2NZCECFhlU-Vm0-nkZ",
        "https://drive.google.com/uc?export=view&id=1zdAdOf8GOrSCBTiUY56_jpduvjt0rsuI",
        "https://drive.google.com/uc?export=view&id=1RMCI13NYmGVHaT3VQVfh4SL3Tk47m6CF",
        "https://drive.google.com/uc?export=view&id=1Fy4pqqKjRVE6jFcl6XRl-T92sYdTDHQM",
        "https://drive.google.com/uc?export=view&id=143oD8Py7dlZ77ssZlOA82_hCxT0DG6ym",
        "https://drive.google.com/uc?export=view&id=1nMQ-fvmI0Rp2vLvJvbWEelTFeB0snRqm",
        "https://drive.google.com/uc?export=view&id=1mgPPWEwwNx4DzSpE5gvmJj6-LKyb_iyj",
        "https://drive.google.com/uc?export=view&id=1fBT6pDA2td_9-H8c0GvvGTvcrdSO-srw",
        "https://drive.google.com/uc?export=view&id=1OJkN0JqY6tEXMtnG-r8SbMXe9d9VQQtG",
        "https://drive.google.com/uc?export=view&id=123Pve9GZmND-dRAMQDl7esXRiMEKiQeQ",
        "https://drive.google.com/uc?export=view&id=1v_Pw_sgl2g0ps7WRknO7VnHxGXJ5V3Ry",
        "https://drive.google.com/uc?export=view&id=1P3aDaDOEmZ_iNu3lx3Y060Sb3mpM1Or_",
        "https://drive.google.com/uc?export=view&id=1DLsCFea4IGFaZmdKcMftMroFr3ILqYaK",
    ]
    data_list = [
        {"nama": "Kevin Antonio Junior", "jabatan": "Kepala Departemen Minat dan Bakat", "nim": "123450109", "umur": "21", "asal": "Bandar Lampung", "alamat": "Panjang, Bandar Lampung", "hobbi": "Balap", "sosmed": "@kevinaj_", "kesan": "Abangnya atletis dan jago olahraga", "pesan": "tetap rajin olahraga agar sehat bang"},
        {"nama": "Gusti Putu Ferazka D.", "jabatan": "Sekretaris Departemen Minat dan Bakat", "nim": "123450046", "umur": "21", "asal": "Lampung Utara", "alamat": "Way Halim", "hobbi": "Baca", "sosmed": "@ferazkaa", "kesan": "Kakaknya keren dan kece", "pesan": "semoga budaya membacanya tidak hilang dimakan zaman ya kak"},
        {"nama": "Ali Aristo Muthahhari Parisi", "jabatan": "Kepala Divisi Manajemen Aktivitas dan Kompetisi", "nim": "123450088", "umur": "21", "asal": "Lampung Timur", "alamat": "Gang Sakum, Belwis", "hobbi": "Nonton F1", "sosmed": "@ali_parisi3", "kesan": "Abangnya mirip konten kreator di IG", "pesan": "Semoga bisa nonton F1 nya langsung di arenanya bang"},
        {"nama": "Ayu Andriani Parlina Wati", "jabatan": "Staf Ahli Manajemen Aktivitas dan Kompetisi", "nim": "124450058", "umur": "20", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Belajar", "sosmed": "@aayuandrianni_", "kesan": "Kakaknya keren sampai bisa jadi staf ahli", "pesan": "keren kak, kayaknya baru kakak yang hobinya belajar"},
        {"nama": "Dafa Elpriza", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450131", "umur": "21", "asal": "Bekasi", "alamat": "Way Kandis", "hobbi": "Nemenin Bryan live Tiktok", "sosmed": "@dafaelpriza", "kesan": "Abangnya kece dalam berpakaian dan penampilan", "pesan": "Tetaplah jadi orang yang selalu mendampingi kawan yang sedang live tiktok"},
        {"nama": "Juwita Sari", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450066", "umur": "19", "asal": "Lampung Barat", "alamat": "Pemda", "hobbi": "Lihat Bulan", "sosmed": "@ju.juwitaaa", "kesan": "Kakaknya baik dan ramah", "pesan": "Semoga apa yang di impikan tercapai ya kak"},
        {"nama": "Muhammad Afdal Lutfi", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450047", "umur": "19", "asal": "Lampung Tengah", "alamat": "Jl Pulau Damar", "hobbi": "Taptap layar kalo Bryan live", "sosmed": "@afdall.03", "kesan": "Abangnya simpel dan gak ribet", "pesan": "Terus menjadi orang yang selalu mendukung teman bang"},
        {"nama": "Salsabila Nazwa Putri", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450002", "umur": "20", "asal": "Metro", "alamat": "Korpri", "hobbi": "Nongkrong di kopken", "sosmed": "@slbnzw_", "kesan": "kakaknya baik, kece juga", "pesan": "sudah mau semester 6 kak, jadi nongkrongnya agak di kurangi ya"},
        {"nama": "Muhammad Ridwan", "jabatan": "Kepala Divisi Manajemen Minat dan Bakat", "nim": "123450091", "umur": "21", "asal": "Lampung Tengah", "alamat": "Belwis", "hobbi": "Nganterin Datasena ke gedung F", "sosmed": "@mridwaan_22", "kesan": "Abangnya Baik dan suka membantu", "pesan": "Tetap jadi orang yang selalu menolong orang bang"},
        {"nama": "Andra Ilham Bintang", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450060", "umur": "18", "asal": "Sumatera Selatan", "alamat": "Kota Baru", "hobbi": "Ngitungin Kelopak bunga di kebun", "sosmed": "@andra.ilham", "kesan": "Abangnya ramah, baik dan mudah bergaul", "pesan": "sekarang udah berapa kelopak bunga yang di itung bang?"},
        {"nama": "Bryan Paskah Telaumbanua", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450003", "umur": "22", "asal": "Nias", "alamat": "Belwis", "hobbi": "Live Tiktok", "sosmed": "@bryantel", "kesan": "wajah abangnya mirip artis", "pesan": "semoga jadi tiktokers terkenal bang"},
        {"nama": "Ghiyats Thabularasa Meardhy", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450067", "umur": "17", "asal": "Bekasi", "alamat": "Korpri", "hobbi": "Ngegift Live Bryan", "sosmed": "@meardhy_ghiyats", "kesan": "keren dan baik abangnya", "pesan": "tetap menjadi orang yang selalu mensupport teman bang"},
        {"nama": "Indah Julia Mawar Pratiwi", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450055", "umur": "20", "asal": "Pringsewu", "alamat": "Airan", "hobbi": "Bengong", "sosmed": "@indahjuliaa", "kesan": "Kakaknya baik dan tidak sombong", "pesan": "Jangan banya bengong ya kak takut kemasukkan"},
        {"nama": "Jacinda Kesya Alvara", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450023", "umur": "18", "asal": "Kalimantan Barat", "alamat": "Korpri", "hobbi": "Nyapu depan Gacoan", "sosmed": "@cacalvra", "kesan": "kakaknya ceria dan jago banget di bidang tari", "pesan": "semoga skill yang dimiliki bisa diajarkan ke orang lain ya kak"},
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450089", "umur": "20", "asal": "Padang", "alamat": "Kota Baru", "hobbi": "Bangun Pagi", "sosmed": "@muhammdrafka_", "kesan": "Abangnya keliatan tenang dan kalem gitu", "pesan": "Tetap jadi morning person bang"}
    ]
    display_images_with_data(gambar_urls, data_list, key="minbak")
