from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1CxIZrD4d0ndKYYsU5BiLO3dSUujkpGo0",
        "https://drive.google.com/uc?export=view&id=1KABZHicsQhrbKk9Rn-4R7ZnaOv1ERWyK",
        "https://drive.google.com/uc?export=view&id=1cxBQGTmEKr9m4gnUzJUT4qPLaTIKANHy",
        "https://drive.google.com/uc?export=view&id=1SDvdHICaO1zicBACVnFCM4QprM3ho4xQ",
        "https://drive.google.com/uc?export=view&id=1aXFVEo72vZQsK9Jq6wNsSohvOZCPbiMH",
        "https://drive.google.com/uc?export=view&id=1aLJM0YHPVfNX-sYdbhuV0Ao0pB6O8BPw",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abang KAHIM kerenn, baik, keliatan asik tapi tetep serius", "pesan": "Semangat kuliahnya bang, sehat selalu dan dilancarkan segala sesuatunya"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Zikir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya tinggi banget, baik dan keliatan asikk", "pesan": "Semangat kuliahnya bang, sehat dan sukses selaluu"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakak asprak ADS, baik dan murah senyumm", "pesan": "Semangat ngasprak dan kuliahnya kak, semoga sealalu dikelilingi orang baik!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya baik dan softspoken", "pesan": "Semangat kuliahnya bang!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik dan murah senyumm", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya baik, seru dan murah senyum", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1sgjaunK9jvDRQLBLqU1MZGNV2dH0brvl",
                  "https://drive.google.com/uc?export=view&id=1FZ1r0dgqeWMuqJixnQiL8FgLH--az6Lt",
                  "https://drive.google.com/uc?export=view&id=1p9zBVMLBVLJ8jpmsgxQALlVoau-RYqtS",
                  "https://drive.google.com/uc?export=view&id=1iwhdyUuWBUktB2HSohiK12y0MbCph1td",
                  "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                  "https://drive.google.com/uc?export=view&id=1BSlFHyegAlfxzr1pK2_By0DmE1a45Wzb",
                  "https://drive.google.com/uc?export=view&id=1MjiNDGsq4fjbxIgKRlFOHB5slnDzRp0v",
                  "https://drive.google.com/uc?export=view&id=1m0SPV3EXTBfNWif3lkaXlYO4x9D32zZZ",
                  "https://drive.google.com/uc?export=view&id=1rGfu4ApUnhCg0axTDiQxk5yJ2eudoXJS",
                  "https://drive.google.com/uc?export=view&id=1AHW6FGGdlA6t9Wo67AINH-jx-2ONGUha",
                  "https://drive.google.com/uc?export=view&id=1_X0MM61QIrR5ajfBmua58ONXJB9uxxB9",
                  "https://drive.google.com/uc?export=view&id=1IdC3Fh3ScYXQUU7-rtA5w7QA5DKINnwa",
                  "https://drive.google.com/uc?export=view&id=1sgWx1hWUtsSu7EjA1hxOhOw7c2gOK1nJ",
    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik ", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "Abangnya keren banget, baik, murah senyum, keliatan asikk", "pesan": "Semangat TA nya ya bang, semoga dilancarkan dan sehat selalu!"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim", "sosmed": "@j__eesie", "kesan": "Kak jue cangtip, baik, murah senyum dan humblee bangett", "pesan": "Kakak semangatt ya TA nya, semoga dilancarkan dan sukses selalu kak <3"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Abang MAPRES kerennn, baik, dan asikk", "pesan": "Semangat TA nya bangg, semoga dilancarkan dan sehat selalu!"},
        {"nama": "Gh Mikael Niko Anthoni Setiadi", "jabatan": "Staff Komisi I", "nim": "124450022", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@me._kael", "kesan": "Abangnya keliatan galak tapi aslinyaa engga hehe", "pesan": "Semangat kuliahnya bangg, sehat dan sukses selalu!"},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Kakaknya baik dan murah senyumm", "pesan": "Semangat ya kak kuliahnya, sehat selalu!"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II", "nim": "124450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum kopi", "sosmed": "@givarooo", "kesan": "Abangnya keren banget, baik, dan positif vibesss", "pesan": "Semangat TA nya bangg, semoga dilancarkan dan sukses selalu!"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "Kak Afganis, baik banget, ramah, dan asikk", "pesan": "Semangat ya kak kuliahnyaa, always happy!"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "city earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain_", "kesan": "Kakak kelas waktu SMP dan sekarang kakak NIM aku whehhe, baik bangett, ramahh dan murah senyum bangett", "pesan": "Semangat ya kak kuliahnyaa, keep shining kakk!!"},
        {"nama": "Jeremia Halim", "jabatan": "Staff Komisi II", "nim": "124450101", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@jeremia_hm", "kesan": "Abangnya keren banget, pernah nyanyi di acara DATAPUDI suaranya mirip kaya penyanyi aslinya", "pesan": "Semangat kuliah nya bang, semoga lancar dan sukses selalu!"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@monica_tjg", "kesan": "Kakaknya baik, asik, dan murah senyumm", "pesan": "Semangat kuliahnya kakk, sehat dan sukses selaluu!"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "gym / koleksi figur", "sosmed": "@nagatsee", "kesan": "Abangnya baik, asikk, sosok yang suka fotoin kalau ada yang tidur pas rangkaian T_T", "pesan": "Semangat kuliah nya bang!, sehat selaluu"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "Kak sekar, keliatan galak tapi aslinya baik bangeett, ramah dan murah senyum jugaa", "pesan": "Semangat kuliahnya kakk!, btw terima kasih yaa kak udah jagain kita pas rangkaian, apalagi yang suka ke toilet hehe"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nahaysh", "kesan": "Kakaknya baik, asik, dan murah senyum bangett", "pesan": "Semangat TA nya kakk, semoga dilancarkan dan sukses selaluu!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1DETQnJqFwGbXP6iy1b1qmrrRkqFUcaVo",
        "https://drive.google.com/uc?export=view&id=11ffq8OLtrk1AP2Gu4I2uvmJVJ-EF_7Ox",
        "https://drive.google.com/uc?export=view&id=1acT3EJxDF8coGEDmghOpmxY7wr5xI7Jn",
        "https://drive.google.com/uc?export=view&id=1e_R4fjRJDmv7N7GcVb-suR3nUAEBEHN0",
        "https://drive.google.com/uc?export=view&id=1kcnzxpSgt3E9ie2dik2UzMtP6hpWa73j",
        "https://drive.google.com/uc?export=view&id=1xp9EL9gvNrq1qlMxGpH_e-EktG-IsHd0",
        "https://drive.google.com/uc?export=view&id=1h3nZYbLt2tvSZ5ykbtqze1cdypQBaeEp",
        "https://drive.google.com/uc?export=view&id=1bgy1WnHxZ2xbbrB9Lufl7hBPjQFAR2LX",
        "https://drive.google.com/uc?export=view&id=1kJC2xhzIoNqAyR0wxLUS-qB_8l4vfRoe",
        "https://drive.google.com/uc?export=view&id=1U8x2-hxZtBQv9Oj1JR-XNil7WdgU1rUD",
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator Mahasiswa", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Kakaknya KEREN banget, baik dan murah senyumm ", "pesan": "Keep shining kakk dan jaga kesehatan!"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Senator Mahasiswa", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya baik, asik", "pesan": "Semangat kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Senator Mahasiswa", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Abangnya kaya ga asing, baik dan asik", "pesan": "semangat kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Suci Aulia", "jabatan": "Senator Mahasiswa", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Kakaknya keliatan judes tapi aslinya baik banget dan seru poll", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Senator Mahasiswa", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Abangnya baik dan asik", "pesan": "Semangat kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Senator Mahasiswa", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Kakak asprak ADS, baik, soft dan murah senyumm", "pesan": "Semangat ya kak ngasprak dan kuliahnya, semoga lancar dan sukses selalu!"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Senator Mahasiswa", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Kak Aqila Mentor MPLS waktu SMP hehe, baik, murah senyum dan asik bangett", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Senator Mahasiswa", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Abangnya keliatan galak tapi aslinya baik dan seruu", "pesan": "Semangat kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Senator Mahasiswa", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Kakaknya cantik, baik, murah senyum dan soft bangett", "pesan": "Semangat kuliahnya kak, sukses selalu dan jaga kesehatan!"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Senator Mahasiswa", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Kakaknya baik dan murah senyum", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="senator")

elif menu == "Departemen PSDA":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1xLbfVREwCK44RGkYqCnL7QvFnWkvXjcu",
                  "https://drive.google.com/uc?export=view&id=1Xm5AhoCj8PYpHhlK3pCYhvQCm2D92GcD",
                  "https://drive.google.com/uc?export=view&id=1Ny3OeKP61APOGUYDFirgB1-0fi8Hp9P7",
                  "https://drive.google.com/uc?export=view&id=1Z3JcQ3-D9YbF0WwkjG0H0trbF8qioHVI",
                  "https://drive.google.com/uc?export=view&id=1TyWKKDLXxI5o1YW5hirjAjzZgd1HC0gt",
                  "https://drive.google.com/uc?export=view&id=1Qn9QDFtkWykdQ6SILTsH1CZ4UtwY3DoH",
                  "https://drive.google.com/uc?export=view&id=1lHe9tL_UUjqEMAExJTYVS1r2jXA8WitH",
                  "https://drive.google.com/uc?export=view&id=1veZlfxydMvYJ28Qg3yRP_stHODX3UVBU",
                  "https://drive.google.com/uc?export=view&id=16j3ATXaGZuvoSlH1iOieoqQhT2ft66Kr",
                  "https://drive.google.com/uc?export=view&id=1-y0wQrahrngBunp8Ez6uroimBn7G4mQP",
                  "https://drive.google.com/uc?export=view&id=1tDLDCzeLcx_nenPKBqebkFUwXqeuBK1r",
                  "https://drive.google.com/uc?export=view&id=1cXyPVj7QWxTjxd51Moxfew0X8AnK658_",
                  "https://drive.google.com/uc?export=view&id=1Pip7eZSAvGlDrXTonnA4Mual7_cspZqh",
                  "https://drive.google.com/uc?export=view&id=1qT2bvrPbsVSXGV6tFOLOaV4zviZ9yLR2",
                  "https://drive.google.com/uc?export=view&id=1Nss6Sf07xm6vaOns77nOd2SjScJh_TIz",
                  "https://drive.google.com/uc?export=view&id=1lDitxeVxnoz7Hr-b635rSth_aHcrZwrY",
                  "https://drive.google.com/uc?export=view&id=1E2Z_VyAUZjqSNPReAhvTtMEKNdvSrNCO",
    ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "123450097", "umur": "21", "asal": "Kalianda", "alamat": "Samping kost Haikal", "hobbi": "Naksir cowo cakep", "sosmed": "@arientakhsnl_", "kesan": "Kak arien cantik, kaya boneka hidup, kakaknya baik dan ramahh", "pesan": "Semangat kuliahnya kakk, sehat dan sukses selalu!"},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "123450022", "umur": "20", "asal": "Palembang", "alamat": "Pudan Kost", "hobbi": "Pacaran", "sosmed": "@vany.salsabilaa", "kesan": "Banyak yang miripin sama kak Vany hehe, kakak keliatan judes tapi aslinya baikk banget", "pesan": "Semangat terus ya kak kuliahnyaa, sehat dan sukses selaluu!"},
        {"nama": "Nobel Nizam Fathirizki", "jabatan": "Kepala Divisi Kaderisasi", "nim": "123450117", "umur": "21", "asal": "Bandar Lampung", "alamat": "Urip", "hobbi": "-", "sosmed": "@nobelnizam", "kesan": "Bang Nobel, pernah satu kelompok matkul ALE, keliatannya galakk tapi aslinya baik, dan santai bangett", "pesan": "Semangat kuliahnya bangg, Tips jago ngodingnya bangg..."},
        {"nama": "Afriza Azmi", "jabatan": "Staf Kaderisasi", "nim": "124450110", "umur": "20", "asal": "Lamteng", "alamat": "Sebelah kost Haikal", "hobbi": "Nyebar beras", "sosmed": "@friezazmi", "kesan": "Abangnya baik, murah senyum dan keliatan soft", "pesan": "Semangat kuliahnya bangg, jaga kesehatan dan sukses selaluu!"},
        {"nama": "Ayake Alfatih Ramadan", "jabatan": "Staf Kaderisasi", "nim": "124450108", "umur": "20", "asal": "Solo", "alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung", "hobbi": "Goreng ayam", "sosmed": "@ykeall", "kesan": "Abangnya baik bangett, keliatan seru dan asikk", "pesan": "Semangat terus kuliahnya bang, Sehat dan sukses selalu!"},
        {"nama": "Caesar Ozora Alrando", "jabatan": "Staf Kaderisasi", "nim": "124450017", "umur": "21", "asal": "Rahim ibu", "alamat": "Gedung F", "hobbi": "Pengembala anak ayam", "sosmed": "@caesar.oriza", "kesan": "Vibes nya komdis bangett, keliatan galak, tapi aslinya baik dan santaii", "pesan": "Semangat kuliahnya bangg, try to smile more ya bang!"},
        {"nama": "Euodia Meiliana Friedita", "jabatan": "Staf Kaderisasi", "nim": "124450029", "umur": "20", "asal": "Asal asalan", "alamat": "Diatas tanjakan", "hobbi": "Ngekader", "sosmed": "@yudiameilianaa_", "kesan": "Kakaknya baik banget waktu TPB pernah ngorol rame rame, ceria, asikk dan seruu bangett", "pesan": "Semangat kuliahnya ya kakk, sukses selalu dan jaga kesehatan yaa!"},
        {"nama": "Haikal Seventino Tamba", "jabatan": "Staf Kaderisasi", "nim": "124450012", "umur": "25", "asal": "Jambi", "alamat": "Sebelah kontrakan Jemar", "hobbi": "Ngurusin pakan anak ayam", "sosmed": "@_haikaaalll", "kesan": "Abangnya keliatan galak, tapi aslinya baikk bangett, soft jugaa ", "pesan": "Semangat kuliahnya bangg, sehat dan sukses selaluu!"},
        {"nama": "Putri Manna Anantama Simbolon", "jabatan": "Staf Kaderisasi", "nim": "124450065", "umur": "18", "asal": "Depok", "alamat": "Nomandenl", "hobbi": "Mancing emosi", "sosmed": "@putrimannaa", "kesan": "Kak Putri baikkk bangett, ramahh murah senyum dan asikk", "pesan": "Semangat terus kuliahnya kakk, sukses dan jaga kesehatan ya kakk!"},
        {"nama": "Queenta Thifaal Nabila", "jabatan": "Staf Kaderisasi", "nim": "124450059", "umur": "21", "asal": "Lamteng", "alamat": "Depan pemancingan", "hobbi": "Nyuapin anak ayam", "sosmed": "@queentanaabila", "kesan": "Kakaknya baikk bangettt, ramah, dan murah senyum bangett", "pesan": "Semangat kuliahnya kakk, jaga kesehatan dan happy selalu ya kak!"},
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi PMA", "nim": "123450114", "umur": "18", "asal": "Palembang Sekayu", "alamat": "Asrama TB 3", "hobbi": "Ngejek orang", "sosmed": "@dsmanhl", "kesan": "Abangnya baik dan suka bercanda tapi serius jugaa", "pesan": "Semangat kuliahnya bangg, sukses selalu dan keep shining bangg!"},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf PMA", "nim": "124450041", "umur": "19", "asal": "Teluk", "alamat": "Bandar Lampung", "hobbi": "Pilates", "sosmed": "@azzelytn", "kesan": "Kakaknya cantikk dan baik bangett", "pesan": "Semangat kak kuliahnyaa, sukses dan happy selauu kakak!"},
        {"nama": "Charrlindah", "jabatan": "Staf PMA", "nim": "124450037", "umur": "21", "asal": "Jakarta Pusat", "alamat": "Cenderawasih 1", "hobbi": "Ngurus peternakan", "sosmed": "@charrlnn", "kesan": "Kakaknya baikk, santai, dan seruu", "pesan": "Semangat terus kuliahnya kakk, happy selalu yaa!"},
        {"nama": "Jeremi Marolop Partogi Situmorang", "jabatan": "Staf PMA", "nim": "124450111", "umur": "16", "asal": "Berlin", "alamat": "Samping kos Rafli", "hobbi": "Mengembala anak ayam", "sosmed": "@jemarrro", "kesan": "Pernah satu kelompok waktu firts gathering, baik, dan seru bangett", "pesan": "Semangat kuliahnya bangg, sehat dan sukses selaluu!"},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf PMA", "nim": "124450048", "umur": "18", "asal": "Lampung", "alamat": "Barokah", "hobbi": "Main sama Azel", "sosmed": "@n.bila_a", "kesan": "Kakaknya baikk, positif vibes dan soft bangett", "pesan": "Semoga kuliahnya lancar dan sehat selalu ya kakk!!"},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf PMA", "nim": "124450007", "umur": "20", "asal": "Sibolga", "alamat": "Samping kos Haikal", "hobbi": "Nonton", "sosmed": "@dearfkvmfl", "kesan": "Abangnya baik, dan keliatan asikk banget", "pesan": "Semangat kulihanya bangg, sukses selaluu dan jaga kesehatan!"},
        {"nama": "Salavi Naharani", "jabatan": "Staf PMA", "nim": "124450090", "umur": "20", "asal": "Lampung Timur", "alamat": "Jatimulyo", "hobbi": "Minum air putih", "sosmed": "@avi.nhr", "kesan": "Kakaknya baik bangett, lucu, dan keliatan kalem", "pesan": "Semangat kak kuliahnyaa, sukses selalu dan jaga kesehatan yaa!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=13f3sr_5K2L5BYlUxPV8NRWbiEMEWxNLw",
                   "https://drive.google.com/uc?export=view&id=1eq9VZNqw-_14G0nD1WwgvRGIyQxZCJHF",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1M8EQoqiAjIdGV5amkvBcQCNmrmovI8Hb",
                   "https://drive.google.com/uc?export=view&id=18qQbxq93JNbfoU-x4jlH4SatjVs1NRDs",
                   "https://drive.google.com/uc?export=view&id=15X92GaumkcVYEC9VnqaYDVGPVxkBdmUC",
                   "https://drive.google.com/uc?export=view&id=1NVkgQ6A0X5LTnS8n9MH-pb1-J2t47pzt",
                   "https://drive.google.com/uc?export=view&id=1hGlXdE6OyPgM-Ta2O0C5Nj42rkaGT0c7",
                   "https://drive.google.com/uc?export=view&id=1lYK66JEChrj_B71M_vS4ifu_nkVpyp4W",
                   "https://drive.google.com/uc?export=view&id=1KWQFMJgDuQ0Wijx3fe_knmxbxcsj45RH",
                   "https://drive.google.com/uc?export=view&id=1_bOPyUlbJL26ZPlMPFfkbbXe_LHBWrAA",
                   "https://drive.google.com/uc?export=view&id=1hdlYvrLGfaFwDnRVR8G6rcAlfh0LPSzV",
                   "https://drive.google.com/uc?export=view&id=15qDJH5UaQWMqx97dzgC9JJ2aVQH6yJY4",
                   "https://drive.google.com/uc?export=view&id=1qVf7Gt0Z2ZgYEBRbjy9tDtkBgHXsUg42",
                   "https://drive.google.com/uc?export=view&id=1FNXE7bP4k5WGRihFCj991Od_mboExAbl",
                   "https://drive.google.com/uc?export=view&id=1whwBrcWNsxdB4EKKHX8Cnc6dbcFavUFA",
                   "https://drive.google.com/uc?export=view&id=1lt1-ouSXmiX6juUGBx4k7Yc-hwSyC0e2",
                   "https://drive.google.com/uc?export=view&id=19Sv1clOJjyJZ6a6RCEQ8bCHZ9fF7ZnaS",
                   "https://drive.google.com/uc?export=view&id=1Z_OpsWQpmgtfc0VfxfyVwU1CnuPnV6sY",
                   "https://drive.google.com/uc?export=view&id=1oxKJ8mUaPGZVc-PTv55VRyLg3haonY5h",
                   "https://drive.google.com/uc?export=view&id=14w_tPUtGzecbYK22qVAPxHwaukYJ3RPH",
                   "https://drive.google.com/uc?export=view&id=1SzIc3kd3j-mDsq-taRfiHqLGSkycFiDo"
    ]
    data_list = [
        {"nama": "Fabio Banyu Cyto", "jabatan": "Kepala Departemen Mikfes", "nim": "12340104", "umur": "21", "asal": "Bandar Lampung", "alamat": "Kedaton", "hobbi": "Tidur", "sosmed": "@biyokcb", "kesan": "Abangnya kerenn, dan keliatan asikk", "pesan": "Semangat TA nya bangg, dilancarkan dan sehat selalu!"},
        {"nama": "Tanty Widiyastuti", "jabatan": "Sekretaris Departemen Mikfes", "nim": "123450094", "umur": "21", "asal": "Lampung", "alamat": "Airan Raya", "hobbi": "Membaca", "sosmed": "@tvnty_", "kesan": "Kak tanty positif vibes bangett, kakak juga ceriaaa bangett", "pesan": "Kak Tanty semangat TA nyaa, semoga lancar dan sukses selaluu, jaga kesehatan ya kak!"},
        {"nama": "Fadil Prasetyo Alfaritzi", "jabatan": "Kepala Divisi PSD", "nim": "123450048", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Gitar", "sosmed": "@fadilalfarizzii", "kesan": "", "pesan": ""},
        {"nama": "Manuel Frederika", "jabatan": "Staf PSD", "nim": "124450039", "umur": "20", "asal": "Batam", "alamat": "Way Kandis", "hobbi": "Tenis meja", "sosmed": "@manuelfdk_", "kesan": "Abangnya keliatan pendiem tapi kayanya engga sii", "pesan": "Semangat kuliahnya bangg!"},
        {"nama": "Ni Made Okta Viola Darma Putri", "jabatan": "Staf PSD", "nim": "124450005", "umur": "12", "asal": "Bali", "alamat": "Nusa Penida", "hobbi": "Menghayal", "sosmed": "Violaadrtr_", "kesan": "Kakaknya baikk, seru dan ramahh", "pesan": "Semangat kuliahnya kakk, happy selaluu yaa!"},
        {"nama": "Risa Romadona", "jabatan": "Staf PSD", "nim": "124450127", "umur": "20", "asal": "Natar", "alamat": "Natar", "hobbi": "Rolling skate", "sosmed": "risarmdna", "kesan": "Kakaknya kaya punya banyak energi, baikk dan asik bangett", "pesan": "Semangat kuliahnya kakk, keep shining ya kak!"},
        {"nama": "Vannisa Ramadhani", "jabatan": "Staf PSD", "nim": "124450078", "umur": "19", "asal": "Kepulauan Riau", "alamat": "Teluk Betung", "hobbi": "Nonton KHW", "sosmed": "@vunnycaa", "kesan": "Kakaknya baikk, murah senyum, dan kalem jugaa", "pesan": "Semangat Kuliahnya kakk!, btw aku juga suka nonton KHW hehee"},
        {"nama": "Yulia Cristine Malau", "jabatan": "Staf PSD", "nim": "124450119", "umur": "20", "asal": "Jambi", "alamat": "Sabah Balau", "hobbi": "Belajar", "sosmed": "@krnylee", "kesan": "Kakaknya keliatan kalem banget, manis, dan baikk jugaa", "pesan": "Semangat kuliahnya kakk!, btw aku kakak sabah balau dimananyaa?"},
        {"nama": "Akeyla Fairuz Shafi", "jabatan": "Kepala Divisi PIKA", "nim": "1234501", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Dengerin Musik", "sosmed": "@keyashafi", "kesan": "Abangnya baik, murah senyum, dan keliatan seruu", "pesan": "Semangat kuliahnya bang, happy selalu ya!"},
        {"nama": "Elsa Sitorus", "jabatan": "Staf PIKA", "nim": "124450088", "umur": "21", "asal": "Sumatera Utara", "alamat": "Pemda", "hobbi": "Rebahan", "sosmed": "@_els.a", "kesan": "Kak Elsa, pernah satu kepanitiannya waktu Science Fest, kakak keren, baik dan murah senyum jugaa", "pesan": "Semangat yaa kak kuliahnyaa, jaga kesehatan kakk!!"},
        {"nama": "Lovianora Saragih", "jabatan": "Staf PIKA", "nim": "124450105", "umur": "19", "asal": "Sumatera Utara", "alamat": "Way Huwi", "hobbi": "Dengerin Musik", "sosmed": "@loviaa", "kesan": "Kakaknya baikk, ramah dan keliatan ceriaa", "pesan": "Semangat kuliahnya kakak!, sehat dan sukses selaluu"},
        {"nama": "Fadya Izzatul 'Aini", "jabatan": "Staf PIKA", "nim": "124450062", "umur": "20", "asal": "Pringsewu", "alamat": "airan", "hobbi": "mancing", "sosmed": "@fadyaizzatul_", "kesan": "Kakaknya baikk banget, ramah, seruu", "pesan": "Semangat kuliahnya kakakk, semoga harinya selalu happy ya kakk"},
        {"nama": "M. Alsi Syahrulloh", "jabatan": "Staf PIKA", "nim": "124450092", "umur": "20", "asal": "Kalianda", "alamat": "Kotabaru", "hobbi": "Main Game, Tidur", "sosmed": "@aluccy_", "kesan": "Abangnya baikk dan keliatan kalem", "pesan": "Semangat kuliahnya bangg, sehat dan sukses selaluu!"},
        {"nama": "Sherena Florencia", "jabatan": "Staf PIKA", "nim": "124450027", "umur": "19", "asal": "Bengkulu Selatan", "alamat": "Belwis", "hobbi": "Make up", "sosmed": "@sher_renna", "kesan": "Kak Serena Asprak ALPRO, kakaknya cantikk, baik bangett, dan softt", "pesan": "Semangat kuliahnyaa ya kakk, sehat dan sukses selaluu!!"},
        {"nama": "Razin Hafid Hamdi", "jabatan": "Kepala Divisi RnD", "nim": "123450096", "umur": "21", "asal": "Padang", "alamat": "Belwis", "hobbi": "Futsal", "sosmed": "@razyn.hfd", "kesan": "Abangnya baikk banget dan keliatan  seruu", "pesan": "Semangat kuliahnya bangg, jaga kesehatann!"},
        {"nama": "Faiza Try Anjani", "jabatan": "Staf RnD", "nim": "124450075", "umur": "19", "asal": "Padang", "alamat": "Belwis", "hobbi": "Membaca Novel", "sosmed": "@Faizaanjanii", "kesan": "Kak Faiza, Asprak sekaligus kakak tutor, kerenn bangett, baik bangettttt, murah senyum dan ramah bangett", "pesan": "Semangat ya kak kuliahnyaa, sehat dan sukses selalu, keep growing kakk!!"},
        {"nama": "Gathfan Nadif Ali", "jabatan": "Staf RnD", "nim": "124450001", "umur": "20", "asal": "Bandar Lampung", "alamat": "Rajabasa", "hobbi": "Main game", "sosmed": "@gathfannadif", "kesan": "Abangnya baik, dan keliatan introvert", "pesan": "Semangat kuliahnya bang, happy selaluu!"},
        {"nama": "Hafidz Wahdiansyah", "jabatan": "Staf RnD", "nim": "124450064", "umur": "20", "asal": "Metro", "alamat": "Metro Kibang, Lampung Timur", "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)", "sosmed": "@apiszzaja_", "kesan": "Bang Hafidz, mentor Poissonn, awalnya keliatan introvert dan pemalu tapi aslinyaa baik bangett, seruu dan asikk banget", "pesan": "Semangat kuliahnya bangg!, dan terima kasih juga udah selalu membersamai Poisson, btw kapan Poisson jalan-jalan banggg"},
        {"nama": "Kaleb Filbert Istel", "jabatan": "Staf RnD", "nim": "124450053", "umur": "20", "asal": "Bandar Lampung", "alamat": "Campang Raya", "hobbi": "Ngegym, baca novel", "sosmed": "@kelelep_comberan", "kesan": "Abangnya baikk, pinterr, dan asikk bangett", "pesan": "Semangat kuliahnya bangg!, Tips jago ngodingnya dong bangg"},
        {"nama": "Melva Shaprina Febrianti", "jabatan": "Staf RnD", "nim": "124450087", "umur": "19", "asal": "Sumsel", "alamat": "Sukarame", "hobbi": "Scroll", "sosmed": "@melva_fbrt", "kesan": "Kakaknya lucuu, baik banget, dan ramahh", "pesan": "Semangat kuliahnya yaa kak, happy selaluu!"},
        {"nama": "Muhammad Syafiqul Falakh", "jabatan": "Staf RnD", "nim": "124450099", "umur": "20", "asal": "Lampung Utara", "alamat": "Asrama TB 3", "hobbi": "Membaca", "sosmed": "@syafiqui", "kesan": "Bang Syafiq, abang tutor kelas RA dan ternyata temennya temen aku, abangnya baikk, seruu, dan murah senyumm", "pesan": "Semangat kuliahnya bangg, sehat dan sukses selaluu!"},
        {"nama": "Rifky Henry Ferdianto", "jabatan": "Staf RnD", "nim": "124450115", "umur": "28", "asal": "Kobum", "alamat": "Rajabasa", "hobbi": "Lari dari kenyataan", "sosmed": "@henryferdianto", "kesan": "Abangnya keliatan galak, tegass, tapi aslinyaa baik bangett, dan seru jugaa", "pesan": "Semangat kuliahnya bangg!, Tips dapetin IP 4 nyaa bangg"},
    ]
    display_images_with_data(gambar_urls, data_list, key="mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=178LB2DVG8scN41c5vjQXYK_w_juO0vKB",
        "https://drive.google.com/uc?export=view&id=1FcgLXvmHOwCygYuiC97W7hkbHNanwAVn",
        "https://drive.google.com/uc?export=view&id=1667OlZUtAfk_7e4HT3JZKXiTJXhtPTvs",
        "https://drive.google.com/uc?export=view&id=1NISYLMZhNgS-eah01Xay9o1vBMoqRPTW",
        "https://drive.google.com/uc?export=view&id=1WxLNdBh-o0Lzz12xURXFym0yyG0vd2ZR",
        "https://drive.google.com/uc?export=view&id=1LpkJS3AtufYT_fFSiLxTC85bu-Okr21l",
        "https://drive.google.com/uc?export=view&id=1qNPSsCFoOKvNGWAgL4VbLtzPjrqwKa9B",
        "https://drive.google.com/uc?export=view&id=1vQ1WwJfcbh6tO_551LmosgFpFSpp7bQh",
        "https://drive.google.com/uc?export=view&id=1gvLlRqMicevOMx9Q8VRJLE1jheaF3P06",
        "https://drive.google.com/uc?export=view&id=1OpO2kB_r4NbiESEsUUImaXJGz-e1v6nZ",
        "https://drive.google.com/uc?export=view&id=1uQu6Z89m8VllwkNeoPqZGBjV8yKTi8m0",
        "https://drive.google.com/uc?export=view&id=1gqTF8hpm9kCBIhB4eKOLkzaSaINpRAZ3",
        "https://drive.google.com/uc?export=view&id=1gJfCBhx6x5_g38k0OvQHRWx1MQ3lXClp",
        "https://drive.google.com/uc?export=view&id=1TGrX2K9khNx8jN-rKlXfpqCejj6x5rFp",
        "https://drive.google.com/uc?export=view&id=1nmjbsUX8qk8MZtWmVKpt3b7Ppl6Lhj30",
        "https://drive.google.com/uc?export=view&id=16DgO0Dp5giQpOAtOP_3ayAyLizB1IcFj",
        "https://drive.google.com/uc?export=view&id=1t-SB1BCLqv__zv1TIo5Xg_A3B33bL0ta",
        "https://drive.google.com/uc?export=view&id=1ZEG-GMSzeu7_EzovItWj9y5plvHxYBCc",
        "https://drive.google.com/uc?export=view&id=12Kg7x7VYZGE90JWUrvN0_eTc9zjCDnxZ",
        "https://drive.google.com/uc?export=view&id=1fvftKvt8X4V9xXvgh6KulTk9yvXtmG-f",
        "https://drive.google.com/uc?export=view&id=155sWMRWrgn9SZCHdNuG69PDEhokwrTqm",
        "https://drive.google.com/uc?export=view&id=1BZwXBclEc9ovMiu1j3iH2eYEPuVCEnen",
    ]
    data_list = [
        {"nama": "Arini Puteri Elandra", "jabatan": "Kepala Departemen Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Kakaknya baik, murah senyum dan asikk bangett", "pesan": "Semangat kuliahnya kakk, always happy yaa!"},
        {"nama": "Nabyla Sharfina", "jabatan": "Sekretaris Departemen Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "Kakaknya baik dan soft bangett", "pesan": "Semangat ya kak kuliahnya, sehat dan sukses selaluu!"},
        {"nama": "Khoirul Muttoharoh", "jabatan": "Kepala Divisi Hubungan Luar", "nim": "1234500", "umur": "-", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Main", "sosmed": "@khoirul_muttoharoh", "kesan": "Kakaknya baikk dan murah senyum bangettt", "pesan": "Semangat kuliahnya kakk, happy selalu yaa!"},
        {"nama": "Ahmad Rizky", "jabatan": "Staf Ahli Hubungan Luar", "nim": "123450050", "umur": "21 Tahun ini Alhamdulillah", "asal": "Tangerang Selatan", "alamat": "GH", "hobbi": "Ngga ngapa ngapain", "sosmed": "@ahmad.rizky__", "kesan": "Bang Ahmad KERENN bangett, baikk, dan asikk", "pesan": "Semangat teruss ya bangg, keep growing and keep shining, abang keren bangettt!!"},
        {"nama": "Adinda Deswita Maharani", "jabatan": "Staf Hubungan Luar", "nim": "124450083", "umur": "10", "asal": "Lampung", "alamat": "Sukabumi", "hobbi": "Jadi idol", "sosmed": "@adindaadma", "kesan": "kakaknya baik dan ramahh", "pesan": "Semangat kuliahnya kak, sehat dan sukses selaluu!"},
        {"nama": "Ahmad Bimo Akbar Arkana", "jabatan": "Staf Hubungan Luar", "nim": "124450113", "umur": "-", "asal": "Tanggamus", "alamat": "Bandar lampung", "hobbi": "Lihat lihat perumahan", "sosmed": "@bimo_arkana", "kesan": "Pernah satu divisi waktu Science Fest, abangnya baik, kalem dan soft bangett", "pesan": "Semangat terus kuliahnya bang, sukses selalu dan jaga kesehatan!"},
        {"nama": "Alfaya Abiyyi", "jabatan": "Staf Hubungan Luar", "nim": "124450006", "umur": "nelson piquet", "asal": "Balam", "alamat": "Balam", "hobbi": "Makan yang manis biar manis", "sosmed": "@alfabiyi", "kesan": "Abangnya baik banget, ramah, murah senyum positif viibes, dan keliatan asik jugaa", "pesan": "Semangat kuliahnya bangg, sukses selalu dan jaga kesehatan!"},
        {"nama": "Asri Meilani", "jabatan": "Staf Hubungan Luar", "nim": "124450010", "umur": "20", "asal": "Lampung barat", "alamat": "Korpri raya", "hobbi": "Nonton film", "sosmed": "@asrmeilani", "kesan": "Kakak cantik bangett, teduh, baikk banget, dan murah senyumm", "pesan": "Semangat ya kak kuliahnya, jaga kesehatan dan keep shining kakk!"},
        {"nama": "Bima Ekayasa", "jabatan": "Staf Hubungan Luar", "nim": "124450106", "umur": "-", "asal": "Lampung", "alamat": "Bandar lampung", "hobbi": "Berlaku humoris dan manis", "sosmed": "@bimayasa_", "kesan": "Abangnya baikk, suka bercanda dan asikk", "pesan": "Semangat kuliahnya bangg, happy selalu!"},
        {"nama": "Indah Khairunnisa", "jabatan": "Staf Hubungan Luar", "nim": "124450077", "umur": "20", "asal": "Ampera", "alamat": "Disini aja", "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang", "sosmed": "@khaindaa_", "kesan": "kakaknya baik bangett, ramah, murah senyum dan seruu bangettt", "pesan": "Semangat Kuliahnya kakk, sukses selalu dan jaga keshatan!"},
        {"nama": "Riska Erlis Dayu Tiara", "jabatan": "Staf Hubungan Luar", "nim": "124450022", "umur": "20", "asal": "Palembang", "alamat": "Bebas", "hobbi": "Ngefollow-up chat", "sosmed": "@erlsriska", "kesan": "Kembarannya mentor PPLK aku hehe, baikk, ramah, dan murah senyum", "pesan": "Semangat kuliahnya kakk!, sukses dan sehat selalu, salamin buat kakk dayuu ya kakk hehhe"},
        {"nama": "Yollanda Agustina", "jabatan": "Staf Hubungan Luar", "nim": "124450024", "umur": "-", "asal": "Kerangka bawang sebelah barat", "alamat": "Kayu mulya", "hobbi": "Tanya bang henry", "sosmed": "@yollanda_agustina16", "kesan": "Kakaknya baikk, murah senyum dan keliatan asikk bangett", "pesan": "Semangat terus kak kuliahnyaa, sehat dan sukses selaluu!!"},
        {"nama": "Aditya Taufiqurrohman", "jabatan": "Kepala Divisi Pengabdian Masyarakat", "nim": "123450032", "umur": "-", "asal": "Tetangga kadep", "alamat": "Belwis", "hobbi": "Memancing keributan", "sosmed": "@adityatfq", "kesan": "Abangnya baik, santai dan keliatan suka bercanda", "pesan": "Semangat terus bangg, sukses selalu dan jaga kesehatan!"},
        {"nama": "Fathya Intami Gusda", "jabatan": "Staf Ahli Pengabdian Masyarakat", "nim": "123450095", "umur": "-", "asal": "Tangsel", "alamat": "Sukarame", "hobbi": "Baca wattpad", "sosmed": "@fatthyaa_", "kesan": "Kakaknya baik bangett dan murah senyum", "pesan": "Semangat kuliahnya kakk, sehat dan sukses selaluu!"},
        {"nama": "Tarisya Hidayatul Rahmi", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450052", "umur": "-", "asal": "Luhak tanah data", "alamat": "gerbar", "hobbi": "Jadi orang baik", "sosmed": "-", "kesan": "kakaknya baik dan ramahh", "pesan": "Semangat kuliahnya kak, happy selalu!!"},
        {"nama": "Ashila Islamisahfa Vanisha", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450028", "umur": "20", "asal": "Sini", "alamat": "Jauh pokoknya", "hobbi": "Tidur", "sosmed": "@kshigf", "kesan": "Kakaknya baikk banget, ramah dan asik diajak ngobroll", "pesan": "Semangat kuliahnya kak, sehat dan sukses selaluu!"},
        {"nama": "Danil N Fadillah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450103", "umur": "-", "asal": "Karawang", "alamat": "belakang polda", "hobbi": "Ngasi makan ikan cupang", "sosmed": "@d4niel_fdlh", "kesan": "Abangnya baikk, murah senyum dan soft banget", "pesan": "Semangat kuliahnya bang, happy selaluu!"},
        {"nama": "Favian Arkaanda", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450021", "umur": "-", "asal": "Swiss", "alamat": "Tanya bapas", "hobbi": "Ngesen kanan", "sosmed": "@fvnnn05", "kesan": "Abangnya baikk, seru dan soft", "pesan": "Semangat terus kuliahnya bang, sukses selalu!"},
        {"nama": "Muhammad Fathiy Zumar Yazid", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450081", "umur": "20", "asal": "Situlah", "alamat": "Pohon mulya", "hobbi": "Nyari hobi", "sosmed": "@zydddddd__", "kesan": "Abangnya baikk, asik dan ceriaa", "pesan": "Semangat kuliahnya bang, happy selaluu!"},
        {"nama": "Muhammad Rizaldi", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450093", "umur": "masih mudalah", "asal": "Rahim ibu", "alamat": "Pasar lantai 3.5", "hobbi": "Gambarr", "sosmed": "@jaldii._", "kesan": "Bang jaldi kerenn banget, MC PPLK, baik bangett, ceriaa, seru dan asikk bangett", "pesan": "Semangat kuliahnya bangg, sukses selalu dan jaga kesehatan!"},
        {"nama": "Saskia Nova Magdalena", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450074", "umur": "20", "asal": "Banyak begal", "alamat": "Pinggir jalan", "hobbi": "Nonton Tinkerbell", "sosmed": "@snova.19", "kesan": "Kakaknya baik, lucu dan ramahh", "pesan": "Semangat kuliahnya kak, happy selalu yaa!"},
        {"nama": "Selma Siti Aisyah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450044", "umur": "20", "asal": "Lampung", "alamat": "Balam", "hobbi": "Jalan jalan", "sosmed": "@selmasiti_aisyah", "kesan": "Kakaknya baikk, keliatan seru dan murah senyum", "pesan": "Semangat kuliahnya kakk, happy selaluuu!!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1DYGVoGeFmPO6hU5XEFai0Q9UMrYGoMoM",
                  "https://drive.google.com/uc?export=view&id=1a-wAVnHAglqty0iJxyVajXunk3APq1hl",
                  "https://drive.google.com/uc?export=view&id=10j4ZD4s3HITL5Wo_2XzGFVafXjQjHnx5",
                  "https://drive.google.com/uc?export=view&id=1QuqsdQXROhjyv-6z2PEyRY3UoqrG2os4",
                  "https://drive.google.com/uc?export=view&id=1Qit9Ufu5WctsrS-vA-AXiimLYC6G-lZ8",
                  "https://drive.google.com/uc?export=view&id=1ci3uCjf9ripPWM27pyeD8k4xNgGTyVQv",
                  "https://drive.google.com/uc?export=view&id=1iqXTp2hBemukc0ZdRJkDq5e7T6VsP9Tq",
                  "https://drive.google.com/uc?export=view&id=1ztiNEefPlgn46RpkEpXvG4pOHn5c-yiw",
                  "https://drive.google.com/uc?export=view&id=1Lti4qpba2G8z5QInXZ3Zk-gJEpwgaI2j",
                  "https://drive.google.com/uc?export=view&id=1vsCXw1ah-rNSCCE6lGOxblwHy03uK1fs",
                  "https://drive.google.com/uc?export=view&id=1iGyzvRdRgespZjIr2loonQI38WKQvoug",
                  "https://drive.google.com/uc?export=view&id=1mYqXPeaBs4GYbJGoUgnkvJJ0LvYE71_9",
                  "https://drive.google.com/uc?export=view&id=12VNXZqd_CQrxbKoDLg78MvmOInj1rJn8",
                  "https://drive.google.com/uc?export=view&id=1fMC0Pk3wxA34x_BTPxp601hL-dTJol68",
                  "https://drive.google.com/uc?export=view&id=1-pBYEj5JtPcSGP21OmFrn4AL22jA1EqS",
                  "https://drive.google.com/uc?export=view&id=1HXLn9bsLXJtR4gL9kviDt_vpHGQFOId0"
    ]
    data_list = [
        {"nama": "Haikal Fransisko Simbolon", "jabatan": "Kepala Departemen Internal", "nim": "123450106", "umur": "20", "asal": "Jambi", "alamat": "Way Halim", "hobbi": "Ngeledek Orang", "sosmed": "@haikalsbln", "kesan": "Abangnya baik dan asikk", "pesan": "Always happy bang!"},
        {"nama": "Kharisma Mustika Sari", "jabatan": "Sekretaris Departemen Internal", "nim": "123450034", "umur": "21", "asal": "Way Kanan", "alamat": "Untung Senopati", "hobbi": "Suka Nolong Orang", "sosmed": "@rismaa.mustika_", "kesan": "Kakaknya keliatan judes tapi aslinya baik bangett, murah senyum dan ramah.", "pesan": "Semangat terus kakk, happy selalu"},
        {"nama": "Hanna Gresia Sinaga", "jabatan": "Kepala Divisi Keharmonisasian", "nim": "123450038", "umur": "21", "asal": "Sumatera Utara, kisaran city", "alamat": "Sukarame", "hobbi": "Ngabarin Orang Tua", "sosmed": "@hanna_g_sinaga", "kesan": "Positif vibes bangett, ceriaa, ramah dan murah senyum bangettt", "pesan": "Terus seperti itu yaa kakk!!"},
        {"nama": "Ahmad Farhan Ghani", "jabatan": "Staf Ahli Keharmonisasian", "nim": "123450121", "umur": "21", "asal": "Kemiling", "alamat": "Kemiling", "hobbi": "Supporteran", "sosmed": "@farhnghnii", "kesan": "Abang baik banget, senyumnya maniss dan positif vibes!", "pesan": "Semangat terus ya bangg, your smile suits u well"},
        {"nama": "Aisyah Khairun Nisa", "jabatan": "Staf Keharmonisasian", "nim": "124450096", "umur": "18", "asal": "Indragiri", "alamat": "Samping Makam Perwira 2", "hobbi": "Nyicipin Makanan", "sosmed": "@aisyahkhair._", "kesan": "Kakaknya baik dan murah senyumm", "pesan": "Semangat terus kak!"},
        {"nama": "Cerine Sihotang", "jabatan": "Staf Keharmonisasian", "nim": "124450049", "umur": "20", "asal": "Medan", "alamat": "Belwis", "hobbi": "Suka Ngoding pakai R", "sosmed": "@cerine_ipynb", "kesan": "Kakaknya baik, kalem dan soft", "pesan": "Semangat kuliahnya kak, happy selalu!"},
        {"nama": "Jaya Saputra Tamba", "jabatan": "Staf Keharmonisasian", "nim": "124450094", "umur": "18", "asal": "Medan", "alamat": "Pemda", "hobbi": "Mencari Nafkah", "sosmed": "@jay.saputra.mb", "kesan": "Abanny baik dan seru", "pesan": "Semangat kuliahnya bang!"},
        {"nama": "Najla Nursyifa", "jabatan": "Staf Keharmonisasian", "nim": "124450051", "umur": "20", "asal": "Sumatra Barat", "alamat": "Belwis", "hobbi": "Nonton ASMR", "sosmed": "@njlanursyifa", "kesan": "Kakaknya baik dan murah senyum bangett", "pesan": "Semangat kuliahnya kak, happy selalu!"},
        {"nama": "Rozak Ramdani", "jabatan": "Staf Keharmonisasian", "nim": "124450100", "umur": "19", "asal": "Kalianda, Lampung Selatan", "alamat": "Korpri Raya", "hobbi": "Berantemin Kucing", "sosmed": "@rozakrabbani__", "kesan": "Abangnya baik, dan murah senyum", "pesan": "Semangat terus bang!"},
        {"nama": "Teresa Christiani Purba", "jabatan": "Staf Keharmonisasian", "nim": "124450046", "umur": "19", "asal": "Riau", "alamat": "Belwis", "hobbi": "Masak", "sosmed": "@kristiani8872", "kesan": "Kak Tere, kakak tutor anak RA, baikk banget, murah senyum dan seruu", "pesan": "Semangat ya kak kuliah dan ngastut nyaa, sehat dan sukses selalu!"},
        {"nama": "Muhammad Hanif Dzaky Arifin", "jabatan": "Kepala Divisi Kerohanian", "nim": "123450064", "umur": "21", "asal": "Padang", "alamat": "Way Kandis", "hobbi": "Nonton F1 & MotoGP", "sosmed": "@hnfdzky_", "kesan": "Abangnya baik dan keliatan santai", "pesan": "Semangat terus bang!"},
        {"nama": "Audina Fitria", "jabatan": "Staf Kerohanian", "nim": "124450038", "umur": "20", "asal": "Sumatra Barat", "alamat": "Sukarame", "hobbi": "Masak", "sosmed": "@audinaf_03", "kesan": "Kakaknya baik, kalem dan soft", "pesan": "Semangat kuliahnya kak!"},
        {"nama": "Cika Adelia Br Marbun", "jabatan": "Staf Kerohanian", "nim": "124450107", "umur": "20", "asal": "Bagan Batu, Riau", "alamat": "Belwis", "hobbi": "Dengerin Musik", "sosmed": "@cikamrbn", "kesan": "Kakaknya baik dan murah senyum", "pesan": "Semangat kuliahnya kak!"},
        {"nama": "Gustin H Tampubolon", "jabatan": "Staf Kerohanian", "nim": "124450068", "umur": "21", "asal": "Sumatera Utara", "alamat": "Airan", "hobbi": "Nonton", "sosmed": "@gustinhaleluya", "kesan": "Kakaknya baik, keliatan kalem dan murah senyum", "pesan": "Semangat kuliahnya kak!"},
        {"nama": "Muhammad Harvinsyah", "jabatan": "Staf Kerohanian", "nim": "124450128", "umur": "20", "asal": "Sumatera Selatan", "alamat": "Belwis", "hobbi": "Ngadu Ikan Cupang", "sosmed": "@muhvinz_", "kesan": "Abangnya baik", "pesan": "Semangat terus bang!"},
        {"nama": "Rafa Sabina Fahimah", "jabatan": "Staf Kerohanian", "nim": "124450036", "umur": "20", "asal": "Natar", "alamat": "Natar", "hobbi": "Nonton Drakor", "sosmed": "@snasaa._", "kesan": "Kakaknya baik dan soft bangett", "pesan": "Semangat kuliahnya kak, happy selalu!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1BhdfxZ5MTEUPq9pDtFj8U07nSSGXLcaE",
        "https://drive.google.com/uc?export=view&id=1iLUTk8NJ9yCO5_iZSer3xfayWAw9Z4k4",
        "https://drive.google.com/uc?export=view&id=1PiE8wDcFZkLE7owHvdDy0K2QxU_152nK",
        "https://drive.google.com/uc?export=view&id=1Mzv-8XXND22Z11I_GoRdBPAm_bSllyM3",
        "https://drive.google.com/uc?export=view&id=1sPr_B0HCz5k9cl_nN6YDQZA7QqEFfOuH",
        "https://drive.google.com/uc?export=view&id=1Dpzbrpi38aldg2HM3hXKiunizhV-5zAu",
        "https://drive.google.com/uc?export=view&id=1VrNMk75wRwaxnLPHmQtqt4oM6GlJ5XPx",
        "https://drive.google.com/uc?export=view&id=1YDRhkY73wzh8JOBAZ29QfxHDiISzewJz",
        "https://drive.google.com/uc?export=view&id=1VSvp0Gd1U6T_xDZc0cV6hDHPmyDTpr0s",
        "https://drive.google.com/uc?export=view&id=1zoV9doobRoVqoZYeKGYiffNoTIsJjI-L",
        "https://drive.google.com/uc?export=view&id=1Zk0aamzxvHUOhgcqDNca7Ib5JR2AJCka",
        "https://drive.google.com/uc?export=view&id=1_W_xaP5R0DpbJVOP1Gsw2brnZZP2lqp4",
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Staf SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Abangnya baik banget, keliatan enjoy, dan murah senyum", "pesan": "Semangat Kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Staf SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Kakaknya baik, seru, dan bisa mencairkan suasa", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
        {"nama": "Afifah Fauziah", "jabatan": "Staf SSD", "nim": "12345002", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "Kakaknya baik banget, seruu, dan dan ramah", "pesan": "Semangat ya kak kuliahnyaa, sehat dan sukses selalu!"},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Staf SSD", "nim": "1234500", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@hasan.ramadhan08", "kesan": "Abangnya keliatan introvert, tapi ternyata engga juga", "pesan": "Semangat kuliahnya bang!"},
        {"nama": "Layina Ropiqo", "jabatan": "Staf SSD", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "Kakaknya baik dan murah senyum", "pesan": "Semangat kuliahnya ya kakk!"},
        {"nama": "Moch. Iqbal Az-Zahir", "jabatan": "Staf SSD", "nim": "122450052", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@iqbalazzahir_", "kesan": "Bang Iqbal asprak ALPRO, abangnya baik dan asik bangett", "pesan": "Semangat kuliahnya bang, lancar dann sukses selalu!"},
        {"nama": "Talitha Justine", "jabatan": "Staf SSD", "nim": "122450076", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Kakaknya baik dan murah senyumm", "pesan": "Semangat kuliahnya kakk, lancar dan sukses selalu!"},
        {"nama": "Anadia Carana", "jabatan": "Staf SSD", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "Kakak Asprak ALPRO, kakaknya baik dan seru poll", "pesan": "Semangat kuliahnya kak, sehat dan sukses selalu!"},
        {"nama": "Abdillah Fikri Al pome", "jabatan": "Staf SSD", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@ssd", "kesan": "Abangnya baik dan soft banget, positif vibes", "pesan": "Semangat kuliahnya bang, lancar dan sukses selalu!"},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Staf SSD", "nim": "124450008", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@dhal_setiawan", "kesan": "Abangnya baik banget", "pesan": "Semangat kuliahnya bang, sehat dan sukses selalu!"},
        {"nama": "Anggun Nita", "jabatan": "Staf SSD", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa", "kesan": "Kakanya baik dan murah senyum", "pesan": "Semangat kak kuliahnya, sehat dan sukses selalu"},
        {"nama": "Della Anisa Fitri", "jabatan": "Staf SSD", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Kakaknya keliatan jutek tapi aslinya baik banget, asik dan murah senyum", "pesan": "Semangat kak kuliahnya, lancar dan sukses selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1L6q29YL71uErYyYaiqVXr5F1gUyHoL2V",
        "https://drive.google.com/uc?export=view&id=1UFZla3EbVvVtXXRVNoJNkvivlhh5Tn2W",
        "https://drive.google.com/uc?export=view&id=1Zf3cdGtDr8z5Ppgib-BwKs8Rme0qtmsC",
        "https://drive.google.com/uc?export=view&id=1naClJRDBxvaJikDlCziPDvGQGl1W3BYZ",
        "https://drive.google.com/uc?export=view&id=1oFLAn17vPp1Vb7FZbyHmiZTOcZToH2jV",
        "https://drive.google.com/uc?export=view&id=18Se0uK_CdPI9ln8LejNrDW9UWBaauV2i",
        "https://drive.google.com/uc?export=view&id=1yrSebZrNjlm8faL6kooOqXS7DXLg1Joh",
        "https://drive.google.com/uc?export=view&id=1kJEe2TmZtmv_krPiYaFC0Fk05TSTgx3s",
        "https://drive.google.com/uc?export=view&id=1jjkDjpTRaxio1dcGpBiGbQCm1ykJ_WbY",
        "https://drive.google.com/uc?export=view&id=1QLfaIFrxUofHm3XYiI0f9Xa6jciuTafT",
        "https://drive.google.com/uc?export=view&id=1hFyr6RHpC1ZiO_TtfP1nku03WYjNYQJQ",
        "https://drive.google.com/uc?export=view&id=1Ru_F8iLPsD0ndLJKjw9UgV0BZzbBwnoq",
        "https://drive.google.com/uc?export=view&id=1lsm71YyT55uJx83BEKwiSOkf1PJO5NaL",
        "https://drive.google.com/uc?export=view&id=1kOAncxa8XK3F7wna9qd-ekHYpcxR-Yem",
        "https://drive.google.com/uc?export=view&id=1Qs9u6GjeC2dLfZPGdR0lufvMQMuCvfFv",
        "https://drive.google.com/uc?export=view&id=1lhYkERzKQ4pzjyvrCceg80TwebZsGJ1-",
        "https://drive.google.com/uc?export=view&id=1buGWtvPT6o5hoi7-AqkPAWlAsiklO9zX",
        "https://drive.google.com/uc?export=view&id=119ADDJ1GijRQPu5RV0E09bWf8mWBtNXA",
    ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Staf Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kak Nayla kerenn, baik bangettt, soft dan positif vibes!", "pesan": "Semangat yaa kak kuliahnya, terus berkembang dan jaga kesehatan!"},
        {"nama": "Donna Maya Puspita", "jabatan": "Staf Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kak Donna baik banget, ramah, dan murah senyum bangett!", "pesan": "Semangat kuliahnya kakk, stay humble!"},
        {"nama": "Labo John Noel Napitupulu", "jabatan": "Staf Medkraf", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "Bang labo baik banget, suka bercanda dan asikkk polll", "pesan": "Semangat TA nya bang, semoga dilancarkan dan sukses selaluu!"},
        {"nama": "Anash Tasya Ausyaqila", "jabatan": "Staf Medkraf", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "Kak anasss, baikk bangett, ramahh, dan seruu poll ", "pesan": "Semangat yaa kak kuliahnyaa, sehat dan sukses selalu, stay amazing kak anass!!"},
        {"nama": "Felisya Nabila Putri Nugroho", "jabatan": "Staf Medkraf", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kak felis keliatannya pemalu tapi aslinya enggaa, lucuu, baikk banget dan pastinya seru bangett", "pesan": "Semangat yaa kak kuliahnyaa, semoga selalu dikelilingi orang orang baik, keep shining kak feliss!"},
        {"nama": "Muhammad Razan Maulana Pratama", "jabatan": "Staf Medkraf", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Bang Razan semi introvert gitu, tapi aslinya asikk dan baikk bangettt", "pesan": "Semangat bang kuliahnyaa, sehat dan sukses selaluu!"},
        {"nama": "Sania Dwi Ayu Lestari", "jabatan": "Staf Medkraf", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kakaknyaa baikk dan murah senyumm", "pesan": "Semangat kuliahnya kakk, sehat dan sukses selaluu!"},
        {"nama": "Allisha", "jabatan": "Staf Medkraf", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kakaknya baikk, murah senyum dan ramah bangett", "pesan": "Semangat ya kak kulliahnyaa, happy selaluu kakk!"},
        {"nama": "Alya Ramadhanti", "jabatan": "Staf Medkraf", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kakaknya baik dan murah senyumm", "pesan": "Semangat yaa kak kuliahnyaa, sehat selaluu!"},
        {"nama": "Bunga Clarisa Sefa", "jabatan": "Staf Medkraf", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kak Bunga baikk, murah senyum dan seruu bangett", "pesan": "Semangat kuliahnya kakk, stay humblee!"},
        {"nama": "Difanya Husakina", "jabatan": "Staf Medkraf", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kakaknya baikk, murah senyumm dan keliatan asikk", "pesan": "Semangat yaa kak kuliahnya, sehatt selalu!"},
        {"nama": "Nazlah Auliya", "jabatan": "Staf Medkraf", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kakaknya lucuu, baik, dan soft bangett", "pesan": "Semangat kuliahnya kakk, happy selalu yaa!"},
        {"nama": "Raihana Adelia Putri", "jabatan": "Staf Medkraf", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "kakaknya baikk dan murah senyumm", "pesan": "Semangat kak kuliahnyaa, semoga lancar dan sukses selaluu!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Abangnya baikk dan kalem bangett", "pesan": "Semangat kuliahnya bangg, always happyy!"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Medkraf", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kakaknya baik, dan murah senyumm", "pesan": "Semangat kuliahnya kakk, sehat dan sukses selaluu!"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Medkraf", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kakaknya baik dan softt", "pesan": "Semangat kuliahnyaa kak, sehat dan sukses selaluu!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="medkraf")

elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1dBd42J97UCVyw5Ta6yercuFWykK1IbKg",
        "https://drive.google.com/uc?export=view&id=1MU79eiWTZCc1_RUk5AJQUQy6BJ53IZT2",
        "https://drive.google.com/uc?export=view&id=1p2GnOXg4Xcn38Sg3o8LNsHxT93HaJE56",
        "https://drive.google.com/uc?export=view&id=1SIs30yfbRQbAQ94OQmfbV8olfoe8FSKE",
        "https://drive.google.com/uc?export=view&id=1VboUZm7QNtv_LZMbrxeHw6U8TTO2FfFN",
        "https://drive.google.com/uc?export=view&id=1sPfwh5ePktHvUeC3b5DaTwz--X1Qirtp",
        "https://drive.google.com/uc?export=view&id=1xkIKh2rPHEDoHVM8cX9_dm6p8DyvMtjc",
        "https://drive.google.com/uc?export=view&id=1-i-hPmmaCPidslWe_Pl3KPEKnVwq_Ew_",
        "https://drive.google.com/uc?export=view&id=1pnV4AhoAVGjLmkwhxraFN7wRRT3QEEKJ",
        "https://drive.google.com/uc?export=view&id=1LPPaf2g1tZ64VOCxmj7ln4bsBOtKGUy6",
        "https://drive.google.com/uc?export=view&id=1qVVpUHZvMirJxsa5fhHdEC7CLqPTnbBQ",
        "https://drive.google.com/uc?export=view&id=1fVevUCoWTU6yuotJK_HlWEgRVJ3zQknV",
        "https://drive.google.com/uc?export=view&id=15I_qPCsbeCtPclR-t7WSXpSpdc5HWb5D",
        "https://drive.google.com/uc?export=view&id=1Zlz1hMig9YX9Ehg7P16cqwR3Fzlka0nb",
        "https://drive.google.com/uc?export=view&id=1rma7r5zxguUfvVN6RWhkqQf_RaK0UG4X"
    ]
    data_list = [
        {"nama": "Kevin Antonio Junior", "jabatan": "Kepala Departemen Minbak", "nim": "123450109", "umur": "21", "asal": "Bandar Lampung", "alamat": "Panjang, Bandar Lampung", "hobbi": "Balap", "sosmed": "@kevinaj__", "kesan": "Abangnya keliatan galak, tapi aslinya baik, chill banget", "pesan": "Semangat terus bang, sehat dan sukses selalu!"},
        {"nama": "Gusti Putu Ferazka Dhiyamika", "jabatan": "Sekretaris Departemen Minbak", "nim": "123450046", "umur": "21", "asal": "Lampung Utara", "alamat": "Way Halim", "hobbi": "Baca", "sosmed": "@ferazkaa", "kesan": "Kakaknya baik banget, cantik dan humblee", "pesan": "Semangat terus kakk, sukses selalu dan jaga kesehatan!"},
        {"nama": "Ari Aristo Muthahari Parisi", "jabatan": "Kepala Divisi Manajemen Aktivitas dan Kompetisi", "nim": "123450088", "umur": "21", "asal": "Lampung Timur", "alamat": "Gang Sakum, Belwis", "hobbi": "Nonton F1", "sosmed": "@ali_parisi3", "kesan": "Abangnya baik, dan asik", "pesan": "Semangat kuliahnya bang!"},
        {"nama": "Ayu Andriani Parlina Wati", "jabatan": "Staf Ahli Manajemen Aktivitas dan Kompetisi", "nim": "124450058", "umur": "20", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Belajar", "sosmed": "@aayuandrianni_", "kesan": "Kakaknya baik dan murah senyum", "pesan": "Semangat terus kuliahnya kak!"},
        {"nama": "Dafa Elpriza", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450131", "umur": "21", "asal": "Bekasi", "alamat": "Way Kandis", "hobbi": "Nemenin Bryan live TikTok", "sosmed": "@dafaelpriza_", "kesan": "Abangnya baik, positif vibes dan soft banget", "pesan": "Semangat kuliahnya bang, sukses selalu dan jaga kesehatan!"},
        {"nama": "Juwita Sari", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450066", "umur": "19", "asal": "Lampung Barat", "alamat": "Pemda", "hobbi": "Lihat bulan", "sosmed": "@ju.juwitaaa_", "kesan": "Kakaknya asik dan seru banget", "pesan": "Semangat kuliahnya kak, happy selalu!"},
        {"nama": "Muhammad Afdal Lutfi", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450047", "umur": "19", "asal": "Lampung Tengah", "alamat": "Jl Pulau Damar", "hobbi": "Taptap layar kalo Bryan live", "sosmed": "@afdall.03", "kesan": "Abangnya baik dan seru banget", "pesan": "Semangat kuliahnya bang, happy selalu!"},
        {"nama": "Salsabila Nazwa Putri", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450002", "umur": "20", "asal": "Metro", "alamat": "Korpri", "hobbi": "Nongkrong di Kopken", "sosmed": "@slbnzw_", "kesan": "Kakaknya baik dan murah senyum", "pesan": "Semangat kuliahnya kakk, happy selalu!"},
        {"nama": "Muhammad Ridwan", "jabatan": "Kepala Divisi Manajemen Minat dan Bakat", "nim": "123450091", "umur": "21", "asal": "Lampung Tengah", "alamat": "Belwis", "hobbi": "Nganterin Datasena ke gedung F", "sosmed": "@mridwaan_22", "kesan": "Abangnya baik, chill dan asik bangett", "pesan": "Semangat terus bang, happy selalu!"},
        {"nama": "Andra Ilham Bintang", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450060", "umur": "18", "asal": "Sumatera Selatan", "alamat": "Kota Baru", "hobbi": "Ngitungin kelopak bunga di kebun", "sosmed": "@andra.lhm", "kesan": "Abangnya baik, ramah, dan seru bangett", "pesan": "Semangat kuliahnya bang, sukses dan sehat selalu!"},
        {"nama": "Bryan Paskah Telaumbanua", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450003", "umur": "22", "asal": "Nias", "alamat": "Belwis", "hobbi": "Live TikTok", "sosmed": "@bryantel_", "kesan": "Abangnya baik dan kalem", "pesan": "Semangat kuliahnya bang, happy selalu!"},
        {"nama": "Ghiyats Thabularasa Meardhy", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450067", "umur": "17", "asal": "Bekasi", "alamat": "Korpri", "hobbi": "Ngegift live Bryan", "sosmed": "@meardhy_ghiyats", "kesan": "Abangnya baik dan seru", "pesan": "Semangat terus bang, happy selalu!"},
        {"nama": "Indah Julia Mawar Pratiwi", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450055", "umur": "20", "asal": "Pringsewu", "alamat": "Airan", "hobbi": "Bengong", "sosmed": "@indahjuliaa", "kesan": "Kakaknya baik, murah senyum dan asik bangett", "pesan": "Semangat kuliahnya kak, happy selaluu!"},
        {"nama": "Jacinda Kesya Alvara", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450023", "umur": "18", "asal": "Kalimantan Barat", "alamat": "Korpri", "hobbi": "Nyapu depan gacoan", "sosmed": "@cacalvra", "kesan": "kakaknya baik, murah senyum dan ceriaa", "pesan": "Semangat kuliahnya kak, happy selaluu!"},
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450089", "umur": "20", "asal": "Padang", "alamat": "Kota Baru", "hobbi": "Bangun pagi", "sosmed": "@muhammdrafka_", "kesan": "Abangnya baik, soft, kalem dan keliatan tenang", "pesan": "Semangat kuliahnya bang, happy selalu!"}

    ]
    display_images_with_data(gambar_urls, data_list, key="minbak")
