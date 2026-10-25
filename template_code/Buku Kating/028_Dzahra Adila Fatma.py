from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1bHJycPWekuNo4NTeBkwAd01NHnXCNiv7",
        "https://drive.google.com/uc?export=view&id=10xTGX5x5WLsi8NB5gMtuFLVGESC95VQ9",
        "https://drive.google.com/uc?export=view&id=1OhUSv5lsAF5HieksWaBsblEzK3StcDI7",
        "https://drive.google.com/uc?export=view&id=1OLnmPM3f1ztfBq21DtQdMsXRc6PfiHa3",
        "https://drive.google.com/uc?export=view&id=1Y5Gx9FpRu6gAu-MdWQqI1w8htvMialqe",
        "https://drive.google.com/uc?export=view&id=1I1UyEmXuqU08haxg66acTm_a82WvlxCc",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya kalemm ,sabar,dewasa,baik.", "pesan": "jangan berubah ya bang terus jadi orang baik semoga sukses selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya lucu semyumnya manis seru bisa diajak bercanda.", "pesan": "jaga kesehatan bang semoga sukses lancar urusannya!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya cantikk manis kalem suka kakanya dewasa banget, murah senyum.", "pesan": " jangan berubah ya kak Sukses selalu  dan di lancarkan semuanya kak dan semangat!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya keliatan introvet, kalem,soft spoken, lucuu.", "pesan": "   Sukses selalu dan semangat bang!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, kaka jadi asprak satu kali kakaknya enak banget baik.", "pesan": "Sukses selalu lancar terus urusannya dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru,kaka jadi asprak seruu baikk enak,ga terlalu serius jadi ga tegang lucuu, baikk.", "pesan": "Sukses selalu  ya kak semoga semuanya di lancarkan dan semangat kakkk!!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1Bu_27fy-YhLpGhzIYbFaTO2tNQ2DyNZ2",
    "https://drive.google.com/uc?export=view&id=1xPwNwe8kXNW4LGQHVKWFdcIwBTVQ5D6E",
    "https://drive.google.com/uc?export=view&id=1HeZRbAZPWlxq6YMXWn2zREhkUyxBTz6G",
    "https://drive.google.com/uc?export=view&id=1sO2cd2ilz1XmdQcSsFZRJMj9tpProeZy",
    "https://drive.google.com/uc?export=view&id=1KG5fXe6Irike8U5xH6kw5sMk60bdZk7B",
    "https://drive.google.com/uc?export=view&id=1exvtrdA_zrN4CGrb9-1CIU0jzGzOxkpW",
    "https://drive.google.com/uc?export=view&id=1QjMkbFutk3GyqxvJItiOftTIyjj4N8Jy",
    "https://drive.google.com/uc?export=view&id=1uvjPu13DSdFwAfSN55_xKz7eBOGENNNO",
    "https://drive.google.com/uc?export=view&id=1Y0roZs6AHWYTCvUoZrDUF609dCelbeI8",
    "https://drive.google.com/uc?export=view&id=1v3ITwSFS85JWwpOpjcsI6-G-iyQ9m9LY",
    "https://drive.google.com/uc?export=view&id=11r1xFIali1DCE_fsno9jVSrKJOa36l56",
    "https://drive.google.com/uc?export=view&id=1sHHsU2H-TbKriuNqk7pVj832TnqBK0wu",
    "https://drive.google.com/uc?export=view&id=1O27iY26vhFMvQdAZUbbJ9Bn3tRHNWOaH"

    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik ", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "Bang ridho kadang serem kadang baik,aslinya asik lusu senyumnya manis,keren, asik banget", "pesan": "Semangat bang, semoga lancar semua urusannya dan sukses selalu bangg"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim", "sosmed": "@j__eesie", "kesan": "Kak Juee baik banget, suka kasi kata kata affirmasi buat semangatin adik asuh tpb <3333", "pesan": "Kak Juee jangan berubah ya kakak, semoga lancar dan sukses selalu kak <3"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Bang dharu baik banget perhatian waktu itu nanyain kamu abis sakit yaa hehe,gimana biar pinternya nular mapress kereennn", "pesan": "Semangat bangg,jangan berubah bang semoga lancar dan sukses selalu bangg"},
        {"nama": "Gh Mikael Niko Anthoni Setiadi", "jabatan": "Staff Komisi I", "nim": "124450022", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@me._kael", "kesan": "bang niko aga pendiam,kalo diem aja aga serem bang ,tapi abangnya baik ga sombong", "pesan": "Semangat kuliahnya bangg , semoga lancar dan di mudahkan dan sukses selalu bangg"},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Kak Syarifa  baikk, ramah, murah senyumm", "pesan": "Semangat kuliahnya kakk,  sehat terus semoga lancar dan sukses selalu kakk"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II", "nim": "124450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum kopi", "sosmed": "@givarooo", "kesan": "Bang Givaro ternyata kita sama sama dari lambar,abangnya baik,mature ramahh bangetttt seruuuu", "pesan": "Semangat ya bangg, semoga segala urusanya di lancarkan sukses selalu bangg"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "Kak nisa cantik bangetttt kakkk baikk, ramah, murah senyum,sabarr", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "city earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain_", "kesan": "Kak Hani baikk, ramah, sama sama coer dengan bias yg sama^^", "pesan": "Kak Hani semangat kuliahnya, semoga lancar dan sukses selalu kakk"},
        {"nama": "Jeremia Halim", "jabatan": "Staff Komisi II", "nim": "124450101", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@jeremia_hm", "kesan": "Bang Jeremia,suaranya bagus, asikk, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@monica_tjg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "gym / koleksi figur", "sosmed": "@nagatsee", "kesan": "Bang Jona baikk banget ramah,ga cocok marah arah bang ", "pesan": " tetap baik terus ya bang Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "Kak Sekar baikk dari awal kenal kaka baik banget, ternyata setelah kenal asikk, ramah, murah senyum kecuali pas rangkaian", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nahaysh", "kesan": "Kak wan baikk, cantikkk,ramah, murah senyum", "pesan": "Semangat TA nya kakk, semoga lancar dan sukses selalu kakk"}

    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1iwQT9-8ZVR2UA7YuUBSteXFBrqSQFNSq",
        "https://drive.google.com/uc?export=view&id=1Ro12i6tMYvQPqpEPA3ywc6uMhrhO4vCx",
        "https://drive.google.com/uc?export=view&id=12VsbzuOcMaOXW0w9Evsg4LaYUvYzstPD",
        "https://drive.google.com/uc?export=view&id=16b80bymcbRnisOUYfouvPFJwTQswKV0z",
        "https://drive.google.com/uc?export=view&id=",
        "https://drive.google.com/uc?export=view&id=1ftzUSanZf2du4lz8Xth_g3spB7LJ2_E-",
        "https://drive.google.com/uc?export=view&id=173o3N3wR7SNCMZxcODkwn90iAhqDhjfv",
        "https://drive.google.com/uc?export=view&id=11oGiQqgjsv4gLyttlPZBFBIcc15h86D6",
        "https://drive.google.com/uc?export=view&id=160IfGFPZsvUV786ppmmUUrh6f-0sc248",
        "https://drive.google.com/uc?export=view&id=1fXxMVx1XRbi-1i7JPfX9MyF8OABWoW6q",
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator Mahasiswa", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Senator Mahasiswa", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya asik", "pesan": "Terus berkarya!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Senator Mahasiswa", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Suci Aulia", "jabatan": "Senator Mahasiswa", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Senator Mahasiswa", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Senator Mahasiswa", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Senator Mahasiswa", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Senator Mahasiswa", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Senator Mahasiswa", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Senator Mahasiswa", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="senator")
elif menu == "Departemen PSDA":
    gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1H27h99POmiWUCAlE6QYKHBAIaEVZ2Qc9",
    "https://drive.google.com/uc?export=view&id=17I9-4GEZKxZXLs6It2JVl-FqK_v-B5Od",
    "https://drive.google.com/uc?export=view&id=1pHdJR6kkFsjfaLlzWmxGQ0DhmkIlfkJE",
    "https://drive.google.com/uc?export=view&id=1MTynR9E6PxXJ3Z2f8ivGydfpYzIwhIKl",
    "https://drive.google.com/uc?export=view&id=1aq41-QLoAazWHEty7RfES0s6qzIYjBCa",
    "https://drive.google.com/uc?export=view&id=1HRMLcmVkVYxTE2eACIdQZzGJOBslssne",
    "https://drive.google.com/uc?export=view&id=1w8a9vMc81jffYg1KfwfyVdL3lb2KMBYZ",
    "https://drive.google.com/uc?export=view&id=1I4MK48AyFP_G2zRvylmQUpJYh2nQ-G-_",
    "https://drive.google.com/uc?export=view&id=1pXKrMl3yUaEf_YRehnNQduK-lSX5oynR",
    "https://drive.google.com/uc?export=view&id=15piQKzjtWlmfcK63_9INVY4_IRftb4qv",
    "https://drive.google.com/uc?export=view&id=15B7QgZKGsYpGvSzz4ywmnv-j-TfJFvfh",
    "https://drive.google.com/uc?export=view&id=1TrJwzJiYNfvF9CTBFXsKDnF_o6lgAQdv",
    "https://drive.google.com/uc?export=view&id=1oH2gcvceEveGsu49nL1q6rx8QO7XVg77",
    "https://drive.google.com/uc?export=view&id=1PWUXi2HOY71FVpbwRav5fP6tcPnbv3pa",
    "https://drive.google.com/uc?export=view&id=1qh4sVGjSNo5uMH-7nkFLSdLEJwuZdakW",
    "https://drive.google.com/uc?export=view&id=14PYyybM4L5rDx3RgZ_yeN-6lKIJYdQXR",
    "https://drive.google.com/uc?export=view&id=1ZxWQGha7gz0gRbzzFP6zkgY0XMOv2Be2"
    ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Nobel Nizam F", "jabatan": "Kepala Divisi Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Afriza Azmi", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Ayake Alfatih Ramadan", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Caesar Ozora Alrando" , "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Euodia Meiliana Friedita", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Haikal Seventino Tamba", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Putri Manna Anantama Simbolon", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Queenta Thifaal Nabila", "jabatan": "Staf Kaderisasi", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Charrlindah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Jeremi Marolop P. Situmorang", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Salavi Naharani", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1CO3rDJHPeD3WDl3alyjAx9OaTAJLPh_8",
    "https://drive.google.com/uc?export=view&id=1tfZQkbwSJMABzgl8KGAm4MeEuHLaCBgu",
    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
    "https://drive.google.com/uc?export=view&id=1pjBTN5x-vdrswJ5ipohJJmHpAuKhLr1c",
    "https://drive.google.com/uc?export=view&id=1OXwCrnNM5vRspxv4HLFf8zgsr1enP8wr",
    "https://drive.google.com/uc?export=view&id=1BSOEgKQ3eB1YawVgZfW4hNQrmfn5KSh0",
    "https://drive.google.com/uc?export=view&id=1v7VrisRwqdEQnUyeGxhBvmOM7Jtq4tNR",
    "https://drive.google.com/uc?export=view&id=1sT4_GJUHXfhZspXNuMoXv08r6YMIn4uX",
    "https://drive.google.com/uc?export=view&id=1NfbKSUDaObumY2oyhP1BnFhe2EoTDJ3E",
    "https://drive.google.com/uc?export=view&id=1fRJxvf4fsn33ZxwwP-nKdc6DKwQFFa3y",
    "https://drive.google.com/uc?export=view&id=1EQbanzRquu_xtNFbV1R2nKaXRuQKr99s",
    "https://drive.google.com/uc?export=view&id=1woDCANIr5sqJ5qJMXZiOMMDNWXVWn-B0",
    "https://drive.google.com/uc?export=view&id=19zEMpB4jxy4IxS-iPuCciTQoCTvTtxuH",
    "https://drive.google.com/uc?export=view&id=1_aDDmvZnCcOFMH38ICs35VWAEAB13xSE",
    "https://drive.google.com/uc?export=view&id=1Nitck_h9He8uW7C2SkXANATrZ8HqRk8y",
    "https://drive.google.com/uc?export=view&id=1Rvtmv_op-R-M_DyZor374Lt_vh13UA-K",
    "https://drive.google.com/uc?export=view&id=1hz5NtQENvJN4877puGmvZWFRuHYkDMUA",
    "https://drive.google.com/uc?export=view&id=1Vrvswo0jELEPwnrYNCEfE_VZLEkoQkSL",
    "https://drive.google.com/uc?export=view&id=1pUZFEO50xiSuAkpGqO_llU1tw1wfePC6",
    "https://drive.google.com/uc?export=view&id=14ph5VQqHmV10k_8SSiYkEyeoA_sOYG9y",
    "https://drive.google.com/uc?export=view&id=1zV0-nE0dqq2SKmX1FEzFa6u-vjCjmJFl",
    "https://drive.google.com/uc?export=view&id=1SPdfip78XqFLjoIjdrBooyD0pwB4x7lZ"
    ]
    data_list = [
        {"nama": "Fabio Banyu Cyto", "jabatan": "Kepala Departemen Mikfes", "nim": "12340104", "umur": "21", "asal": "Bandar Lampung", "alamat": "Kedaton", "hobbi": "Tidur", "sosmed": "@biyokcb", "kesan": "Gayanya santai dan tidak pernah ribet.", "pesan": "Tetap jadi kakak yang asyik, Kak."},
        {"nama": "Tanty Widiyastuti", "jabatan": "Sekretaris Departemen Mikfes", "nim": "123450094", "umur": "21", "asal": "Lampung", "alamat": "Airan Raya", "hobbi": "Membaca", "sosmed": "@tvnty_", "kesan": "Tenang dan suka memperhatikan hal-hal kecil.", "pesan": "Terus bagikan ketelitianmu ke kami, Kak."},
        {"nama": "Fadil Prasetyo Alfaritzi", "jabatan": "Kepala Divisi PSD", "nim": "123450048", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Gitar", "sosmed": "@fadilalfarizzii", "kesan": "Permainan gitarnya bikin suasana nyaman.", "pesan": "Sering-sering hibur kami lewat musikmu, Kak."},
        {"nama": "Manuel Frederika", "jabatan": "Staf PSD", "nim": "124450039", "umur": "20", "asal": "Batam", "alamat": "Way Kandis", "hobbi": "Tenis meja", "sosmed": "@manuelfdk_", "kesan": "Energik dan cepat akrab dengan siapa saja.", "pesan": "Tetap semangat dan jangan berubah, Kak."},
        {"nama": "Ni Made Okta Viola Darma Putri", "jabatan": "Staf PSD", "nim": "124450005", "umur": "12", "asal": "Bali", "alamat": "Nusa Penida", "hobbi": "Menghayal", "sosmed": "Violaadrtr_", "kesan": "Pembawaannya kalem dan penuh imajinasi.", "pesan": "Semoga ide-idemu terus berkembang, Kak."},
        {"nama": "Risa Romadona", "jabatan": "Staf PSD", "nim": "124450127", "umur": "20", "asal": "Natar", "alamat": "Natar", "hobbi": "Rolling skate", "sosmed": "risarmdna", "kesan": "Aktif dan berani mencoba hal baru.", "pesan": "Terus berani melangkah, Kak."},
        {"nama": "Vannisa Ramadhani", "jabatan": "Staf PSD", "nim": "124450078", "umur": "19", "asal": "Kepulauan Riau", "alamat": "Teluk Betung", "hobbi": "Nonton KHW", "sosmed": "@vunnycaa", "kesan": "Ramah dan selalu terlihat ceria.", "pesan": "Tetap jadi pribadi yang menyenangkan, Kak."},
        {"nama": "Yulia Cristine Malau", "jabatan": "Staf PSD", "nim": "124450119", "umur": "20", "asal": "Jambi", "alamat": "Sabah Balau", "hobbi": "Belajar", "sosmed": "@krnylee", "kesan": "Sopan dan menghargai orang lain.", "pesan": "Semoga selalu sukses dalam setiap kegiatan, Kak."},
        {"nama": "Akeyla Fairuz Shafi", "jabatan": "Kepala Divisi PIKA", "nim": "1234501", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Dengerin Musik", "sosmed": "@keyashafi", "kesan": "Pendengar yang baik dan tidak suka menghakimi.", "pesan": "Tetap jadi teman cerita yang nyaman, Kak."},
        {"nama": "Elsa Sitorus", "jabatan": "Staf PIKA", "nim": "124450088", "umur": "21", "asal": "Sumatera Utara", "alamat": "Pemda", "hobbi": "Rebahan", "sosmed": "@_els.a", "kesan": "Murah senyum dan enak diajak bicara.", "pesan": "Tetap jadi kakak yang hangat, ya, Kak."},
        {"nama": "Lovianora Saragih", "jabatan": "Staf PIKA", "nim": "124450105", "umur": "19", "asal": "Sumatera Utara", "alamat": "Way Huwi", "hobbi": "Dengerin Musik", "sosmed": "_loviaa", "kesan": "Kalem tapi tetap hangat saat berinteraksi.", "pesan": "Semoga selalu dimudahkan dalam studinya, Kak."},
        {"nama": "Kaleb Filbert Istel", "jabatan": "Staf RnD", "nim": "124450053", "umur": "20", "asal": "Bandar Lampung", "alamat": "Campang Raya", "hobbi": "Ngegym, baca novel", "sosmed": "@kelelep_comberan", "kesan": "Konsisten menjaga kebiasaan hidup sehat.", "pesan": "Tularkan semangat hidup sehatmu ke kami, Kak."},
        {"nama": "M. Alsi Syahrulloh", "jabatan": "Staf PIKA", "nim": "124450092", "umur": "20", "asal": "Kalianda", "alamat": "Kotabaru", "hobbi": "Main Game, Tidur", "sosmed": "@aluccy_", "kesan": "Humoris dan gampang bikin tawa.", "pesan": "Jangan lupa tetap fokus kuliah juga, Kak."},
        {"nama": "Sherena Florencia", "jabatan": "Staf PIKA", "nim": "124450027", "umur": "19", "asal": "Bengkulu Selatan", "alamat": "Belwis", "hobbi": "Make up", "sosmed": "@sher_renna", "kesan": "Rapi dan selalu tampil percaya diri.", "pesan": "Tetap jadi inspirasi bagi adik tingkat, Kak."},
        {"nama": "Razin Hafid Hamdi", "jabatan": "Kepala Divisi RnD", "nim": "123450096", "umur": "21", "asal": "Padang", "alamat": "Belwis", "hobbi": "Futsal", "sosmed": "@razyn.hfd", "kesan": "Sportif dan semangat kerja samanya tinggi.", "pesan": "Terus ajak kami aktif bersama, Kak."},
        {"nama": "Faiza Try Anjani", "jabatan": "Staf RnD", "nim": "124450075", "umur": "19", "asal": "Padang", "alamat": "Belwis", "hobbi": "Membaca Novel", "sosmed": "@Faizaanjanii", "kesan": "Tutur katanya sopan dan penuh pertimbangan.", "pesan": "Tetap jadi kakak yang bijak, Kak."},
        {"nama": "Gathfan Nadif Ali", "jabatan": "Staf RnD", "nim": "124450001", "umur": "20", "asal": "Bandar Lampung", "alamat": "Rajabasa", "hobbi": "Main game", "sosmed": "@gathfannadif", "kesan": "Santai tapi tetap bertanggung jawab.", "pesan": "Terus jaga keseimbangan itu, Kak."},
        {"nama": "Hafidz Wahdiansyah", "jabatan": "Staf RnD", "nim": "124450064", "umur": "20", "asal": "Metro", "alamat": "Metro Kibang, Lampung Timur", "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)", "sosmed": "@apiszzaja_", "kesan": "Cekatan soal teknis dan mau berbagi ilmu.", "pesan": "Ajari kami ngoding dengan sabar, Kak."},
        {"nama": "Kaleb Filbert Istel", "jabatan": "Staf RnD", "nim": "124450053", "umur": "20", "asal": "Bandar Lampung", "alamat": "Campang Raya", "hobbi": "Ngegym, baca novel", "sosmed": "@kelelep_comberan", "kesan": "Konsisten menjaga kebiasaan hidup sehat.", "pesan": "Tularkan semangat hidup sehatmu ke kami, Kak."},
        {"nama": "Melva Shaprina Febrianti", "jabatan": "Staf RnD", "nim": "124450087", "umur": "19", "asal": "Sumsel", "alamat": "Sukarame", "hobbi": "Scroll", "sosmed": "@melva_fbrt", "kesan": "Ceria dan mudah menyesuaikan diri.", "pesan": "Tetap jadi pribadi yang ramah, Kak."},
        {"nama": "Muhammad Syafiqul Falakh", "jabatan": "Staf RnD", "nim": "124450099", "umur": "20", "asal": "Lampung Utara", "alamat": "Asrama TB 3", "hobbi": "Membaca", "sosmed": "@syafiqui", "kesan": "Pendiam tapi diam-diam bisa diandalkan.", "pesan": "Jangan sungkan berbagi pendapat ke kami, Kak."},
        {"nama": "Rifky Henry Ferdianto", "jabatan": "Staf RnD", "nim": "124450115", "umur": "28", "asal": "Kobum", "alamat": "Rajabasa", "hobbi": "Lari dari kenyataan", "sosmed": "@henryferdianto", "kesan": "Humornya unik dan bikin suasana cair.", "pesan": "Semoga kenyataan selalu ramah padamu, Kak."},
        
    ]

    display_images_with_data(gambar_urls, data_list, key="Mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1psGKm9crnYoYn1KjoJd94iWwQVfSiCwJ",
        "https://drive.google.com/uc?export=view&id=1m4Hl-GjgwQgRR6tF85kFqttp2WOjG0KL",
        "https://drive.google.com/uc?export=view&id=1MGu3zb_jDtR-WTbplKUfoRHOGpt7pSee",
        "https://drive.google.com/uc?export=view&id=1zxUZZFISEd7vedmL5eneQY77aCd6Iyi5",
        "https://drive.google.com/uc?export=view&id=1ZpgytYftNQKdZaGz9FZ8PS2S9XipH2sq",
        "https://drive.google.com/uc?export=view&id=1fY-zf2R-S7gL-ULxBm_RVHpLqNZROFD8",
        "https://drive.google.com/uc?export=view&id=12jfrGj_1US6xJsJgdFSLrxpV3Rcmevqv",
        "https://drive.google.com/uc?export=view&id=1BdNN51XB4gpQc18kh6hAdWvM8SHRjjon",
        "https://drive.google.com/uc?export=view&id=1cpulGvAF9s6An2gKrXNw2X9FusUbf60u",
        "https://drive.google.com/uc?export=view&id=1e_paz-yv1uy9jtVjBwkDm65RntQfqDcd",
        "https://drive.google.com/uc?export=view&id=1k3PoCDNxkhhwcKFgq44fONy26UW7OgTK",
        "https://drive.google.com/uc?export=view&id=1K7aAb7a3okD4u8qUbgHToVAGgD4Ki51_",
        "https://drive.google.com/uc?export=view&id=1KJ2QNu9Y665f5AdnoIfA5c71P8u6EifL",
        "https://drive.google.com/uc?export=view&id=1Y2JSujvP1QVPQ9ptlVzRXuDGZ-3E3fhJ",
        "https://drive.google.com/uc?export=view&id=19aNnniiJ-N8N6KqbaCW6p9TX8BdtPm1D",
        "https://drive.google.com/uc?export=view&id=1ZgMsw0QQbOEiOiYmCyBlt_7q58tlydPL",
        "https://drive.google.com/uc?export=view&id=1CRR9trxM8ZTeQmVPW2W6ZLBZ-L40ZRZC",
        "https://drive.google.com/uc?export=view&id=1KnxdRbTBAeWzL6eeZ1GWhZ7YJmlzWdJ0",
        "https://drive.google.com/uc?export=view&id=15FIBd70Ylc6UFiv8b4SdLgP_QHfH5koU",
        "https://drive.google.com/uc?export=view&id=1zffJEe33QPWdfe_S3dZSt9Wwf3kCQcl9",
        "https://drive.google.com/uc?export=view&id=1zAYBj3mATgQz6A2FbZIJPxmdCF7An4RG",
        "https://drive.google.com/uc?export=view&id=1TTDqNP8zkeTfCy-LraEcCmP7O3Xi_fZn"
    ]
    data_list =[
        {"nama": "Arini Puteri Elandra", "jabatan": "Kepala Departemen Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Murah Senyum", "pesan": "Selalu jadi orang baik ya kak"},
        {"nama": "Nabyla Sharfina", "jabatan": "Sekretaris Departemen Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "Ramah", "pesan": "Selalu jadi orang baik"},
        {"nama": "Khoirul Muttoharoh", "jabatan": "Kepala Divisi Hubungan Luar", "nim": "1234500", "umur": "-", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Main", "sosmed": "@khoirul_muttoharoh", "kesan": "Enak diajak ngobrol", "pesan": "Semangat terus bangg"},
        {"nama": "Ahmad Rizky", "jabatan": "Staf Ahli Hubungan Luar", "nim": "123450050", "umur": "21 Tahun ini Alhamdulillah", "asal": "Tangerang Selatan", "alamat": "GH", "hobbi": "Ngga ngapa ngapain", "sosmed": "@ahmad.rizky__", "kesan": "Kerenn bangett bang", "pesan": "Selalu jadi orang yang kritis"},
        {"nama": "Adinda Deswita Maharani", "jabatan": "Staf Hubungan Luar", "nim": "124450083", "umur": "10", "asal": "Lampung", "alamat": "Sukabumi", "hobbi": "Jadi idol", "sosmed": "@adindaadma", "kesan": "kakaknya asik", "pesan": "selalu asik ya kakk"},
        {"nama": "Ahmad Bimo Akbar Arkana", "jabatan": "Staf Hubungan Luar", "nim": "124450113", "umur": "-", "asal": "Tanggamus", "alamat": "Bandar lampung", "hobbi": "Lihat lihat perumahan", "sosmed": "@bimo_arkana", "kesan": "Ramah", "pesan": "Selalu jadi orang yang ramah tamah"},
        {"nama": "Alfaya Abiyyi", "jabatan": "Staf Hubungan Luar", "nim": "124450006", "umur": "nelson piquet", "asal": "Balam", "alamat": "Balam", "hobbi": "Makan yang manis biar manis", "sosmed": "@alfabiyi", "kesan": "Keren", "pesan": "Semangat terus"},
        {"nama": "Asri Meilani", "jabatan": "Staf Hubungan Luar", "nim": "124450010", "umur": "20", "asal": "Lampung barat", "alamat": "Korpri raya", "hobbi": "Nonton film", "sosmed": "@asrmeilani", "kesan": "Sangat ramah", "pesan": "Terus jadi orang ramah kak"},
        {"nama": "Bima Ekayasa", "jabatan": "Staf Hubungan Luar", "nim": "124450106", "umur": "-", "asal": "Lampung", "alamat": "Bandar lampung", "hobbi": "Berlaku humoris dan manis", "sosmed": "@bimayasa_", "kesan": "Ramah", "pesan": "Selalu jadi orang yang ramah tamah"},
        {"nama": "Indah Khairunnisa", "jabatan": "Staf Hubungan Luar", "nim": "124450077", "umur": "20", "asal": "Ampera", "alamat": "Disini aja", "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang", "sosmed": "@khaindaa_", "kesan": "kakaknya asik", "pesan": "selalu asik ya kakk"},
        {"nama": "Riska Erlis Dayu Tiara", "jabatan": "Staf Hubungan Luar", "nim": "124450022", "umur": "20", "asal": "Palembang", "alamat": "Bebas", "hobbi": "Ngefollow-up chat", "sosmed": "@erlsriska", "kesan": "Cantik banget", "pesan": "selalu ramah ya"},
        {"nama": "Yollanda Agustina", "jabatan": "Staf Hubungan Luar", "nim": "124450024", "umur": "-", "asal": "Kerangka bawang sebelah barat", "alamat": "Kayu mulya", "hobbi": "Tanya bang henry", "sosmed": "@yollanda_agustina16", "kesan": "aktif banget", "pesan": "inget istirahat kak"},
        {"nama": "Aditya Taufiqurrohman", "jabatan": "Kepala Divisi Pengabdian Masyarakat", "nim": "123450032", "umur": "-", "asal": "Tetangga kadep", "alamat": "Belwis", "hobbi": "Memancing keributan", "sosmed": "@adityatfq", "kesan": "Jail", "pesan": "jangan sering mancing keributan bang"},
        {"nama": "Fathya Intami Gusda", "jabatan": "Staf Ahli Pengabdian Masyarakat", "nim": "123450095", "umur": "-", "asal": "Tangsel", "alamat": "Sukarame", "hobbi": "Baca wattpad", "sosmed": "@fatthyaa_", "kesan": "Lucuu", "pesan": "selalu lucuu kak"},
        {"nama": "Tarisya Hidayatul Rahmi", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450052", "umur": "-", "asal": "Luhak tanah data", "alamat": "gerbar", "hobbi": "Jadi orang baik", "sosmed": "-", "kesan": "kakaknya lucuu", "pesan": "tetep jadi asprak yang keren ya kak"},
        {"nama": "Ashila Islamisahfa Vanisha", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450028", "umur": "20", "asal": "Sini", "alamat": "Jauh pokoknya", "hobbi": "Tidur", "sosmed": "@kshigf", "kesan": "kocak", "pesan": "Selalu tertawa terus kak"},
        {"nama": "Danil N Fadillah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450103", "umur": "-", "asal": "Karawang", "alamat": "belakang polda", "hobbi": "Ngasi makan ikan cupang", "sosmed": "@d4niel_fdlh", "kesan": "softboy", "pesan": "Selalu kalcer bang"},
        {"nama": "Favian Arkaanda", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450021", "umur": "-", "asal": "Swiss", "alamat": "Tanya bapas", "hobbi": "Ngesen kanan", "sosmed": "@fvnnn05", "kesan": "Keren", "pesan": "Semangat terus dan humoriss bang"},
        {"nama": "Muhammad Fathiy Zumar Yazid", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450081", "umur": "20", "asal": "Situlah", "alamat": "Pohon mulya", "hobbi": "Nyari hobi", "sosmed": "@zydddddd__", "kesan": "Hebat dan tegas", "pesan": "selalu jadi orang keren dan ramah tamah"},
        {"nama": "Muhammad Rizaldi", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450093", "umur": "masih mudalah", "asal": "Rahim ibu", "alamat": "Pasar lantai 3.5", "hobbi": "Gambarr", "sosmed": "@jaldii._", "kesan": "keren jadi mc pplk 2025", "pesan": "selalu ramah ya bang"},
        {"nama": "Saskia Nova Magdalena", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450074", "umur": "20", "asal": "Banyak begal", "alamat": "Pinggir jalan", "hobbi": "Nonton Tinkerbell", "sosmed": "@snova.19", "kesan": "kakaknya lucu", "pesan": "Terus jadi orang ramah kak"},
        {"nama": "Selma Siti Aisyah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450044", "umur": "20", "asal": "Lampung", "alamat": "Balam", "hobbi": "Jalan jalan", "sosmed": "@selmasiti_aisyah", "kesan": "Kerenn banget", "pesan": "Selalu jadi orang baik"}
    ]
    display_images_with_data(gambar_urls, data_list, key="eksternal")


elif menu == "Departemen Internal":
    gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1sZojUVXo_Q2ksD64lc3tHsDLujNe9xpv",
    "https://drive.google.com/uc?export=view&id=1hJ1uJLGLJpu7Ywr7J5pZcuU7yGSQuoC3",
    "https://drive.google.com/uc?export=view&id=1pmPykUmXPzvR7x047gRcH0TvcgscFdKL",
    "https://drive.google.com/uc?export=view&id=1MivL5Gs1XhR3VzGVj2LFlVA2xcLSMRCz",
    "https://drive.google.com/uc?export=view&id=18FHhZWcrrsfA_x5TqyVySk9UeMlaAIWD",
    "https://drive.google.com/uc?export=view&id=11ImahIvG7r1LiTkK-DIAxuLaLCmz_teN",
    "https://drive.google.com/uc?export=view&id=179PZp_vpq8ILPivVv-GDO25IPbCl9-_l",
    "https://drive.google.com/uc?export=view&id=1bApjL0rXsX0RUl1YCH06pZ4qmjhxfCzZ",
    "https://drive.google.com/uc?export=view&id=15IfCPUFU4BbIgDUqgJlTasJgJcOzZBtA",
    "https://drive.google.com/uc?export=view&id=",
    "https://drive.google.com/uc?export=view&id=1PH6y6dv9vPKhxfM7BgVx1giwhHWtXEGi",
    "https://drive.google.com/uc?export=view&id=12vdTMHHqPone3CvUTBmOXHcN8I03fz1t",
    "https://drive.google.com/uc?export=view&id=1J1bvcHe4h_xg9EbphL2KfpUC4jPdXSnT",
    "https://drive.google.com/uc?export=view&id=1lXMLoLsBAZuMUA4-V6E9almPjVU9PZV5",
    "https://drive.google.com/uc?export=view&id=1VEH3Sc1jqiUM2hcvAaGM-xgMCJwyNoGv",
    "https://drive.google.com/uc?export=view&id=1mhstR0pCKEq-LDHypRDvCZzN9qgIfbyh"

    
    ]
    data_list = [
        {"nama": "Haikal Fransisko Simbolon", "jabatan": "Kepala Departemen Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Kharisma Mustika Sari", "jabatan": "Sekretaris Departemen Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Hanna Gresia Sinaga", "jabatan": "Kepala Divisi Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "A Farhan Ghani", "jabatan": "Staf Ahli Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Aisyah Khairun Nisa", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Cerine Sihotang", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Jaya Saputra Tamba", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Najla Nursyifa", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Rozak Ramdani", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Teresa Christiani Purba", "jabatan": "Staf Keharmonisasian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Muhammad Hanif Dzaky Arifin", "jabatan": "Kepala Divisi Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Audina Fitria", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Cika Adelia Br Marbun", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Gustin H. Tampubolon", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Muhammad Harvinsyah", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
        {"nama": "Rafa Sabina Fahimah", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"}
    
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1ERRnfaaLA4hmMMkfzRasqDTcJSM6CUrI",
        "https://drive.google.com/uc?export=view&id=1IEiVXggdT_PQUJ0Z1-eR6ADv8oLbJ9mw",
        "https://drive.google.com/uc?export=view&id=1gmAlqbm_PZ3ajz10X_D2RdfxEDbbl7Gc",
        "https://drive.google.com/uc?export=view&id=1GIQ8OOfiuSVKG2FbPOJPX5lB3oJQ0WiP",
        "https://drive.google.com/uc?export=view&id=1B9xSMc3EbXXvcQEi4UhpB6xhGP1vNuSa",
        "https://drive.google.com/uc?export=view&id=1T7mrGt-q1LwUlFxP1oHMmMVV8lkmKOyo",
        "https://drive.google.com/uc?export=view&id=1yENXWeEJd1gYl0ztk0ZaKAliNk-C0cMs",
        "https://drive.google.com/uc?export=view&id=1J7Kq1c0WUQFg-vrhvL_LOY4-s7HdQDTY",
        "https://drive.google.com/uc?export=view&id=1VewqNE3HsmcL2oJczg7gKc28ru3K-Rbk",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1W3SHZAYr2Ze8i30J03TwrpezCUhwnODB",
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Staf SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Staf SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Afifah Fauziah", "jabatan": "Staf SSD", "nim": "12345002", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Staf SSD", "nim": "1234500", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@hasan.ramadhan08", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Layina Ropiqo", "jabatan": "Staf SSD", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Moch. Iqbal Az-Zahir", "jabatan": "Staf SSD", "nim": "122450052", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@iqbalazzahir_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Talitha Justine", "jabatan": "Staf SSD", "nim": "122450076", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anadia Carana", "jabatan": "Staf SSD", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Abdillah Fikri Al pome", "jabatan": "Staf SSD", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Staf SSD", "nim": "124450008", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@dhal_setiawan", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggun Nita", "jabatan": "Staf SSD", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Della Anisa Fitri", "jabatan": "Staf SSD", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1Ue31RlZYSZgm9l_OWTsGDuNNLRzg2ntd",
        "https://drive.google.com/uc?export=view&id=1TbFgQYzbLWaIyGGpazuuuTbWAnFSoD95",
        "https://drive.google.com/uc?export=view&id=1dl6Tr71HdtgInMtQ-LP0FeKjOkcj3Jwx",
        "https://drive.google.com/uc?export=view&id=16gmBKhdiF6VSFEdZHkfp7kj00GtTOD7z",
        "https://drive.google.com/uc?export=view&id=1WAIML80Kaw4pmCiTBeEKyLGUSXX9WQI3",
        "https://drive.google.com/uc?export=view&id=1_QhJj-g1BEIAUO1rXbq57MQa43WCN2pi",
        "https://drive.google.com/uc?export=view&id=17sFARgmLTALx5-JlCvh5YgbdkQORtx1V",
        "https://drive.google.com/uc?export=view&id=1LbL72OMG3b9bp9F-hqKLuqlX1xUgTXN7",
        "https://drive.google.com/uc?export=view&id=1VIRMZuJEQMBrT_ffACk0ra1yInsS_UNz",
        "https://drive.google.com/uc?export=view&id=1uK1eSEGFCHBacH-1bQuu1Qq4JT82Fdl0",
        "https://drive.google.com/uc?export=view&id=1m0LW6PxChLu4ikHVqVxGHd2SSU7FiZNd",
        "https://drive.google.com/uc?export=view&id=1YHfXY0zzbL3RwwyZrCqrar9wlwtVRCrO",
        "https://drive.google.com/uc?export=view&id=183prjg4UbgWRI1_0cjfCLjOk_cxZbIDN",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1ggfQxOGhgw7tNjK-t56bkmJARW_tlgSR",
        "https://drive.google.com/uc?export=view&id=1ATCPWdkLwWtCMlz49j7gyuypsD1kHCK9",
        "https://drive.google.com/uc?export=view&id=1PaSfCj8UMMs9Lzyp72SigsCnat0NXNmd",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
    ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Staf Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Donna Maya Puspita", "jabatan": "Staf Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Labo John Noel Napitupulu", "jabatan": "Staf Medkraf", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anash Tasya Ausyaqila", "jabatan": "Staf Medkraf", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Felisya Nabila Putri Nugroho", "jabatan": "Staf Medkraf", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Razan Maulana Pratama", "jabatan": "Staf Medkraf", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Sania Dwi Ayu Lestari", "jabatan": "Staf Medkraf", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Allisha", "jabatan": "Staf Medkraf", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Alya Ramadhanti", "jabatan": "Staf Medkraf", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Bunga Clarisa Sefa", "jabatan": "Staf Medkraf", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Difanya Husakina", "jabatan": "Staf Medkraf", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Nazlah Auliya", "jabatan": "Staf Medkraf", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Raihana Adelia Putri", "jabatan": "Staf Medkraf", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Medkraf", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Medkraf", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="medkraf")
elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1QKjEiAHI-7R4G6nARAwtpwznSDRBGeEf",
        "https://drive.google.com/uc?export=view&id=1IewuyR9D75wCBJQzBuQUPeDnqVRDsg7N",
        "https://drive.google.com/uc?export=view&id=1F3RoEv4bH1Y9NZM0UF4UTGj71NXVXuXR",
        "https://drive.google.com/uc?export=view&id=11rdKCjab6sMMfeOCAXMJ8qsv1doiDNLV",
        "https://drive.google.com/uc?export=view&id=14hnFO2ipm2R2-bAqCh60Zl7bWsKd47Kv",
        "https://drive.google.com/uc?export=view&id=1kry0RNispEYkrAEjclO7AI9q5YgHjNvW",
        "https://drive.google.com/uc?export=view&id=16Vb0PPgm4leFhs-UHi_y3d2HbJ1umATO",
        "https://drive.google.com/uc?export=view&id=1wcpGjwXBm3vAhMm-2MaFHGwRDZDGTyON",
        "https://drive.google.com/uc?export=view&id=1zSfVTWOy6ETHmkJyuIYBzLdf00_Jbcos",
        "https://drive.google.com/uc?export=view&id=1fzsbNQEaVGtVt2W-NjzPV98YE_qoeMWC",
        "https://drive.google.com/uc?export=view&id=1eQ1bdtP-9Gn5GOw42Z-CRHLHHCIqzqp9",
        "https://drive.google.com/uc?export=view&id=1jaKvv_kWCJHeO9sDrIzgJpK_ZStMuUWA",
        "https://drive.google.com/uc?export=view&id=1An7ve2IwlPkpSlNLXqzJNrxTJB3JOh2j",
        "https://drive.google.com/uc?export=view&id=1nKBXMxPmi-JkKAw-vFoyp2kCLv-wlHsY",
        "https://drive.google.com/uc?export=view&id=11B2Jk2UTmfzG6u9qVbPYMsmW2psQ7c2D"
    ]
    data_list = [
        {"nama": "Kevin Antonio Junior", "jabatan": "Kepala Departemen Minbak", "nim": "123450109", "umur": "21", "asal": "Bandar Lampung", "alamat": "Panjang, Bandar Lampung", "hobbi": "Balap", "sosmed": "@kevinaj__", "kesan": "Sosoknya santai tapi tetap bisa diandalkan.", "pesan": "Tetap jadi kakak yang asyik diajak ngobrol, Kak."},
        {"nama": "Gusti Putu Ferazka Dhiyamika", "jabatan": "Sekretaris Departemen Minbak", "nim": "123450046", "umur": "21", "asal": "Lampung Utara", "alamat": "Way Halim", "hobbi": "Baca", "sosmed": "@ferazkaa", "kesan": "Tutur katanya tenang dan enak didengar.", "pesan": "Terus bagikan wawasan dari bacaanmu ke kami, Kak."},
        {"nama": "Ari Aristo Muthahari Parisi", "jabatan": "Kepala Divisi Manajemen Aktivitas dan Kompetisi", "nim": "123450088", "umur": "21", "asal": "Lampung Timur", "alamat": "Gang Sakum, Belwis", "hobbi": "Nonton F1", "sosmed": "@ali_parisi3", "kesan": "Orangnya kalem dan tidak banyak menuntut.", "pesan": "Tetap jadi pribadi yang rendah hati, Kak."},
        {"nama": "Ayu Andriani Parlina Wati", "jabatan": "Staf Ahli Manajemen Aktivitas dan Kompetisi", "nim": "124450058", "umur": "20", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Belajar", "sosmed": "@aayuandrianni_", "kesan": "Rajin dan selalu bersungguh-sungguh dalam bekerja.", "pesan": "Semoga semangat belajarnya menular ke kami, Kak."},
        {"nama": "Dafa Elpriza", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450131", "umur": "21", "asal": "Bekasi", "alamat": "Way Kandis", "hobbi": "Nemenin Bryan live TikTok", "sosmed": "@dafaelpriza_", "kesan": "Setia kawan dan gampang bikin suasana ramai.", "pesan": "Jangan berubah, tetap jadi teman yang seru, Kak."},
        {"nama": "Juwita Sari", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450066", "umur": "19", "asal": "Lampung Barat", "alamat": "Pemda", "hobbi": "Lihat bulan", "sosmed": "@ju.juwitaaa_", "kesan": "Sikapnya lembut dan menenangkan.", "pesan": "Tetap jadi tempat bercerita yang nyaman, Kak."},
        {"nama": "Muhammad Afdal Lutfi", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450047", "umur": "19", "asal": "Lampung Tengah", "alamat": "Jl Pulau Damar", "hobbi": "Taptap layar kalo Bryan live", "sosmed": "@afdall.03", "kesan": "Ceria dan selalu kompak dengan teman-temannya.", "pesan": "Terus jaga kekompakan itu, Kak."},
        {"nama": "Salsabila Nazwa Putri", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450002", "umur": "20", "asal": "Metro", "alamat": "Korpri", "hobbi": "Nongkrong di Kopken", "sosmed": "@slbnzw_", "kesan": "Mudah akrab dan enak diajak berdiskusi.", "pesan": "Tetap jadi kakak yang terbuka ke adik tingkat, ya, Kak."},
        {"nama": "Muhammad Ridwan", "jabatan": "Kepala Divisi Manajemen Minat dan Bakat", "nim": "123450091", "umur": "21", "asal": "Lampung Tengah", "alamat": "Belwis", "hobbi": "Nganterin Datasena ke gedung F", "sosmed": "@mridwaan_22", "kesan": "Bertanggung jawab dan siap membantu kapan saja.", "pesan": "Jangan lelah jadi tumpuan kami, Kak."},
        {"nama": "Andra Ilham Bintang", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450060", "umur": "18", "asal": "Sumatera Selatan", "alamat": "Kota Baru", "hobbi": "Ngitungin kelopak bunga di kebun", "sosmed": "@andra.lhm", "kesan": "Teliti dan sabar dalam mengerjakan sesuatu.", "pesan": "Tetap semangat dan jangan ragu bertanya ke kami, Kak."},
        {"nama": "Bryan Paskah Telaumbanua", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450003", "umur": "22", "asal": "Nias", "alamat": "Belwis", "hobbi": "Live TikTok", "sosmed": "@bryantel_", "kesan": "Percaya dirinya tinggi dan bikin suasana hidup.", "pesan": "Tetap jadi pribadi yang menghibur, Kak."},
        {"nama": "Ghiyats Thabularasa Meardhy", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450067", "umur": "17", "asal": "Bekasi", "alamat": "Korpri", "hobbi": "Ngegift live Bryan", "sosmed": "@meardhy_ghiyats", "kesan": "Royal ke teman dan murah hati.", "pesan": "Semoga kebaikanmu selalu dibalas, Kak."},
        {"nama": "Indah Julia Mawar Pratiwi", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450055", "umur": "20", "asal": "Pringsewu", "alamat": "Airan", "hobbi": "Bengong", "sosmed": "@indahjuliaa", "kesan": "Pembawaannya adem dan tidak neko-neko.", "pesan": "Tetap jadi pribadi yang apa adanya, Kak."},
        {"nama": "Jacinda Kesya Alvara", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450023", "umur": "18", "asal": "Kalimantan Barat", "alamat": "Korpri", "hobbi": "Nyapu depan gacoan", "sosmed": "@cacalvra", "kesan": "Ceria dan punya selera humor yang unik.", "pesan": "Terus tebar keceriaan ke sekitar, Kak."},
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450089", "umur": "20", "asal": "Padang", "alamat": "Kota Baru", "hobbi": "Bangun pagi", "sosmed": "@muhammdrafka_", "kesan": "Disiplin dan selalu memulai hari lebih awal.", "pesan": "Ajari kami cara menjaga konsistensi, Kak."}
    ]

    display_images_with_data(gambar_urls, data_list, key="minbak")
