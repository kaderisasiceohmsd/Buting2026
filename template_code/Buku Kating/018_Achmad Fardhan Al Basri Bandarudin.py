from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

# ============================================================
# MENU CONTENT
# ============================================================
if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=12QdXjuDnQDgFjZ53SQuKa14r1KlfZdtC",
        "https://drive.google.com/uc?export=view&id=1dCRWi5V03bDmaN8EXzTquEh56RbmzWH5",
        "https://drive.google.com/uc?export=view&id=1Nl37phlxmCYNGC8fQiEWGBngxmdTYWrS",
        "https://drive.google.com/uc?export=view&id=1-RHonktea6ug0hMHWJb075mq8lUfSxVo",
        "https://drive.google.com/uc?export=view&id=1tPhSsXlKDmI0HV1lXhVVXZ3pj-SlX6-1",
        "https://drive.google.com/uc?export=view&id=1J_tlUQwAwRqlkmQ1ctjO6VxpS9syNjG6",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "menyala selalu bang", "pesan": "Semangat TA nya banggg, semoga lancar dan sukses selaluu"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Bang aqil keren gayanya", "pesan": "semangat dan keren terus ya bang"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakk efi adalah wanita yang hebatt", "pesan": "semakin hebat dan keren selalu kak"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Bang qois postive vibes banget", "pesan": "selalu jadi orang baik bang"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kak hafsa cantikk dan keren ", "pesan": "semangat dan terus keren kak"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya cantikk nan baik hatii, penyabarr", "pesan": "Sukses dan selalu baik kesemua orangg yaa kak"},
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1nb6wQCMKYJ-qpm_JJX5mf3ZNLK-J_H3i",
                   "https://drive.google.com/uc?export=view&id=17OL5MYhd-mPGuqd3MQUn-GEt3F0BzWdV",
                   "https://drive.google.com/uc?export=view&id=1PwKjv3GE4YpyIHMxbgZuSV0X6DOnCKPm",
                   "https://drive.google.com/uc?export=view&id=13r76KMeRBGdgw_T1BS1qSyZop0qHoUir",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1asiSAi8307nYlUj6NELCI7r3VXVlVE3q",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1kLwtXjx2olEgmOaEKgusg7kVCJUBDHFe",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1IagjaSmKoMlNQuKstWP2TbyQVig0eUZe",
                   "https://drive.google.com/uc?export=view&id=1IVbitzGVgyhbI1W3YRlHSdMaHfyqDmWG",
                   "https://drive.google.com/uc?export=view&id=1WFD00bxXLtyJKy2gBjM1N_Hsd38ainaa",
                   "https://drive.google.com/uc?export=view&id=1IlzmNGNYQx6UilONk2kXu0NQqyXjeNsv",
    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik ", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "gabisa berkata kata hebatnyoo", "pesan": "Semangat TA nya bangg, semoga lancar dansukses selalu bangg"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim", "sosmed": "@j__eesie", "kesan": "Kak Juee baik banget", "pesan": "semangat kak jangan patah semangat"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Bang dharu keren banget jadii mapresssss idamann", "pesan": "selalu bersinar ditiap harinya bang"},
       {"nama": "Gh Mikael Nico Antoni Setiadi", "jabatan": "Staf Eksternal", "nim": "124450025", "umur": "20", "asal": "Lamtim", "alamat": "Jati agung", "hobbi": "Main mcgg", "sosmed": "@me._kael", "kesan": "Santai dan seru.", "pesan": "semangat terus abangnyaa"},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Kakak yang baikk, ramah, murah senyumm", "pesan": "sehat semangat kuliahnya kak"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II", "nim": "124450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum kopi", "sosmed": "@givarooo", "kesan": "Bang Givaro keren, seruuu, baik", "pesan": "udah minum kopi bang ?"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "Kak nisa baikk", "pesan": "keren keren hebat kak wow"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "city earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain_", "kesan": "Kak Hani baikk, ramah", "pesan": "p, kak, ……"},
        {"nama": "Jeremia Halim", "jabatan": "Staf Eksternal", "nim": "124450101", "umur": "20", "asal": "Tangerang", "alamat": "Teluk Betung", "hobbi": "Nyanyi, olahraga", "sosmed": "@jeremia_hm", "kesan": "Ramah dan seru", "pesan": "semakin menyalaa kedepannya bangg"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Departemen Eksternal", "nim": "123450073", "umur": "21", "asal": "Sumut", "alamat": "Kota baru", "hobbi": "Merajut", "sosmed": "@monica_tjg", "kesan": "Sabar dan telaten", "pesan": "semoga selalu berbunga bunga tiap harinya kak"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "gym / koleksi figur", "sosmed": "@nagatsee", "kesan": "Bang Jona keren, asikk, ramah", "pesan": "abangnya pengertian ya bangg"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "Kak Sekar baikk", "pesan": "senyum kakanya mahal ya kak"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nahaysh", "kesan": "Kak wan baikk, ramah, imutt", "pesan": "kalem kalem keren banget kakanyaa"},

    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1adDzBL83GRxrkpCHbabR-KGkHvdDaDLw",
                   "https://drive.google.com/uc?export=view&id=1h6knY8DO-nKuqMLUGbB0WiP_vZ2hnXxl",
                   "https://drive.google.com/uc?export=view&id=1OzMDgEK9aGkBknqyE7YTUvZisSXt9vvX",
                   "https://drive.google.com/uc?export=view&id=1sT6F4idooVcQzZEOlpZFD5uZhVlTs4dQ",
                   "https://drive.google.com/uc?export=view&id=1yYdbKWsiGJwdy2BLhuUw3Knv8nYBUCup",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1uUf8cobIcp275cg1nhdsgv4u8028adTF",
                   "https://drive.google.com/uc?export=view&id=1dpucSmlYuZfVW9W3tPnpmAxQsctbXr63",
                   "https://drive.google.com/uc?export=view&id=13tfR7Wt7bwXk6pAv6KzyRxoIniUn2xbr",
                   "https://drive.google.com/uc?export=view&id=1kdFTZEnPYkuNpJG0jHDK1qz9ImbP4LE8",
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "kakaknya bagus publik speakingnya", "pesan": "ga bisa berkata kata hebat banget kak"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Kepala Biro Aspirasi dan Media Komunikasi ", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "keliatannya serem abangnya ternyata sehelokity itu", "pesan": "GOKIL!!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Abangnya kaya serem tapi ternyata baikkk", "pesan": "keren selalu setiap hari bang"},
        {"nama": "Suci Aulia", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Kak Suci baikkk", "pesan": "semoga hari hari kakaknya selalu cerah"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Bang Wielman soft spoken", "pesan": "semangat terus mengarungi hidup bang"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Biro Kajian Strategis dan Propaganda", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Kakaknya keren", "pesan": "terimakasih selalu jadi yang terbaik kak"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Kakaknya gabisa diem selalu ketawaa tapi lucuuk", "pesan": "tabikpun, jangan lupa pulang kekobum ya kak"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Bang Hazel kaya seram gitu, rambutnya bikin baddaass tapi ternyata baikkk", "pesan": "semoga selalu dalam lindungan allah ya bang"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Kerennnn kaakakknyaaa", "pesan": "diam diam menyala kakaknya keren deh"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Kakaknya lucuuu", "pesan": "keren keren selalu kakanya"},
    ]

elif menu == "Departemen PSDA":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1Wuc4L6sgBoo0_bEfODDm4qnmhV0lb5Fs",
                   "https://drive.google.com/uc?export=view&id=1mYHpz8j3-LdffghK3--meBlWQV6S6TRE",
                   "https://drive.google.com/uc?export=view&id=1lhv5Fzb2y7vN6dKi3-iFs2kP29Opl_Wa",
                   "https://drive.google.com/uc?export=view&id=1ord9VbP1G8yKkezIjNab8CBwUPEV_q12",
                   "https://drive.google.com/uc?export=view&id=1mMekmzXyU1mld6BgK4yJVSBBfdp4LOJq",
                   "https://drive.google.com/uc?export=view&id=1rjP2j9ScK6YgzGP1FsTQJcNX5tiJwgiX",
                   "https://drive.google.com/uc?export=view&id=1HAql4KGgPOKK_NAKQr-MDrERmW_2CXre",
                   "https://drive.google.com/uc?export=view&id=19R7Y9-gHOeLnSQLBkM2KvmUhlF7UXgYm",
                   "https://drive.google.com/uc?export=view&id=1Ab96qg09_6NUt8LGb8yme7WSErzvvhEh",
                   "https://drive.google.com/uc?export=view&id=1Htn6O5u6FeCM-EgAwzdYhl0hwGcIwr2q",
                   "https://drive.google.com/uc?export=view&id=1T3En8p8NqynR7wSEqNRTtn2JVUjlLLRw",
                   "https://drive.google.com/uc?export=view&id=1ULsT6Pk7G7dSbUbjx3GFDpTRuA_uOglf",
                   "https://drive.google.com/uc?export=view&id=1WJatEYATBbA-ex6gPJKNzE-6_fHzTnKI",
                   "https://drive.google.com/uc?export=view&id=1_J8cADzoEhS_gwj9OfK--v0GtK1b8Xmn",
                   "https://drive.google.com/uc?export=view&id=1nDp-XlUNqD0CR5bHBR-9soFX16zo1nmT",
                   "https://drive.google.com/uc?export=view&id=1BhoiSznhDKNgzQPiGKd8ycLRQqWwOM6p",
                   "https://drive.google.com/uc?export=view&id=1OXFzj9MDHDtUtI_T-04-qy7uf5zsaO8w",
    ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "123450097", "umur": "21", "asal": "Kalianda", "alamat": "Samping kost Haikal", "hobbi": "Naksir cowo cakep", "sosmed": "@arientakhsnl_", "kesan": "Ramah dan mudah akrab dengan siapa saja.", "pesan": "menyala terus kakanya"},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "123450022", "umur": "20", "asal": "Palembang", "alamat": "Pudan Kost", "hobbi": "Pacaran", "sosmed": "@vany.salsabilaa", "kesan": "Kak vany baikkk, walaupun keliatan judes", "pesan": "semangat terus kakaknya"},
        {"nama": "Nobel Nizam Fathirizki", "jabatan": "Kepala Divisi Kaderisasi", "nim": "123450117", "umur": "21", "asal": "Bandar Lampung", "alamat": "Urip", "hobbi": "-", "sosmed": "@nobelnizam", "kesan": "Kalem dan sopan, nyaman diajak ngobrol.", "pesan": "keren teruss bang"},
        {"nama": "Afriza Azmi", "jabatan": "Staf Kaderisasi", "nim": "124450110", "umur": "20", "asal": "Lamteng", "alamat": "Sebelah kost Haikal", "hobbi": "Nyebar beras", "sosmed": "@friezazmi", "kesan": "Santai dan menyenangkan.", "pesan": "sehat sehat bang"},
        {"nama": "Ayake Alfatih Ramadan", "jabatan": "Staf Kaderisasi", "nim": "124450108", "umur": "20", "asal": "Solo", "alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung", "hobbi": "Goreng ayam", "sosmed": "@ykeall", "kesan": "Supel dan gampang bergaul.", "pesan": "selalu ramah ya bang "},
        {"nama": "Caesar Ozora Alrando", "jabatan": "Staf Kaderisasi", "nim": "124450017", "umur": "21", "asal": "Rahim ibu", "alamat": "Gedung F", "hobbi": "Pengembala anak ayam", "sosmed": "@caesar.oriza", "kesan": "Orangnya santai dan asyik diajak ngobrol.", "pesan": "semakin hebat setiap langkahnya bang"},
        {"nama": "Euodia Meiliana Friedita", "jabatan": "Staf Kaderisasi", "nim": "124450029", "umur": "20", "asal": "Asal asalan", "alamat": "Diatas tanjakan", "hobbi": "Ngekader", "sosmed": "@yudiameilianaa_", "kesan": "Aktif dan punya semangat yang tinggi.", "pesan": "selalu semangat semangat kak"},
        {"nama": "Haikal Seventino Tamba", "jabatan": "Staf Kaderisasi", "nim": "124450012", "umur": "25", "asal": "Jambi", "alamat": "Sebelah kontrakan Jemar", "hobbi": "Ngurusin pakan anak ayam", "sosmed": "@_haikaaalll", "kesan": "Dewasa dan bisa diandalkan.", "pesan": "gapai terus mimpimya bang"},
        {"nama": "Putri Manna Anantama Simbolon", "jabatan": "Staf Kaderisasi", "nim": "124450065", "umur": "18", "asal": "Depok", "alamat": "Nomandenl", "hobbi": "Mancing emosi", "sosmed": "@putrimannaa", "kesan": "Ceria dan seru diajak bercanda.", "pesan": "tetap semangat kak jangan nyerah"},
        {"nama": "Queenta Thifaal Nabila", "jabatan": "Staf Kaderisasi", "nim": "124450059", "umur": "21", "asal": "Lamteng", "alamat": "Depan pemancingan", "hobbi": "Nyuapin anak ayam", "sosmed": "@queentanaabila", "kesan": "Ramah dan hangat ke semua orang.", "pesan": "selalu jadi orang baik kak"},
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi PMA", "nim": "123450114", "umur": "18", "asal": "Palembang Sekayu", "alamat": "Asrama TB 3", "hobbi": "Ngejek orang", "sosmed": "@dsmanhl", "kesan": "Orangnya humoris dan bikin suasana cair.", "pesan": "selalu jadi orang asik abangku"},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf PMA", "nim": "124450041", "umur": "19", "asal": "Teluk", "alamat": "Bandar Lampung", "hobbi": "Pilates", "sosmed": "@azzelytn", "kesan": "Disiplin dan menjaga pola hidup sehat.", "pesan": "sehat sehat dan menyala terus orang baik"},
        {"nama": "Charrlindah", "jabatan": "Staf PMA", "nim": "124450037", "umur": "21", "asal": "Jakarta Pusat", "alamat": "Cenderawasih 1", "hobbi": "Ngurus peternakan", "sosmed": "@charrlnn", "kesan": "Pekerja keras dan bertanggung jawab.", "pesan": "jadi orang asik terus ya kak"},
        {"nama": "Jeremi Marolop Partogi Situmorang", "jabatan": "Staf PMA", "nim": "124450111", "umur": "16", "asal": "Berlin", "alamat": "Samping kos Rafli", "hobbi": "Mengembala anak ayam", "sosmed": "@jemarrro", "kesan": "Santai dan mudah bergaul.", "pesan": "semangat terus bang "},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf PMA", "nim": "124450048", "umur": "18", "asal": "Lampung", "alamat": "Barokah", "hobbi": "Main sama Azel", "sosmed": "@n.bila_a", "kesan": "Ramah dan menyenangkan diajak berteman.", "pesan": "tetap menyala terus kak"},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf PMA", "nim": "124450007", "umur": "20", "asal": "Sibolga", "alamat": "Samping kos Haikal", "hobbi": "Nonton", "sosmed": "@dearfkvmfl", "kesan": "Kalem dan enak diajak ngobrol.", "pesan": "selalu jadi orang murah hati bang"},
        {"nama": "Salavi Naharani", "jabatan": "Staf PMA", "nim": "124450090", "umur": "20", "asal": "Lampung Timur", "alamat": "Jatimulyo", "hobbi": "Minum air putih", "sosmed": "@avi.nhr", "kesan": "Tenang dan apa adanya.", "pesan": "sehat selalu kak"},
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1Vrf6tfghe4NB6LkTN8Oknosvx-tvjIuT",
                   "https://drive.google.com/uc?export=view&id=1DJHzP85moU2DdSX4CxJGm-_-F41UjGNy",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy",
                   "https://drive.google.com/uc?export=view&id=19TTnEGSUEpbkRYRqOHKYryECCpjv8C4R",
                   "https://drive.google.com/uc?export=view&id=1yOoxvdC9Gt64-rwPCIGI7Ewa2cNO0By3",
                   "https://drive.google.com/uc?export=view&id=1UhJh2xq3RUjmqHllYVMonwgll5fWdK-H",
                   "https://drive.google.com/uc?export=view&id=1RT0VsPQObAZZoP-JNpek2y7ebUxtD4ru",
                   "https://drive.google.com/uc?export=view&id=1dsdC6LlV7SHIZcD6_hFts6VZtBamXW1w",
                   "https://drive.google.com/uc?export=view&id=1DvKA-VfwJO5JL-evbEIcPqAyGl4d2J8d",
                   "https://drive.google.com/uc?export=view&id=1r4HNsPcYjhAg4qakI7gCZbEiyvZ3Q2KH",
                   "https://drive.google.com/uc?export=view&id=1ZXVJfjxABm470NG57wIeuO8ffBHkq-AY",
                   "https://drive.google.com/uc?export=view&id=1c82ZZAFTaTMTO_BuF5xBZabozz5Kpn-P",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1jxM3Zx3NsXFshrSiumapbCEDaDhc1OJi",
                   "https://drive.google.com/uc?export=view&id=1JlZ1I2w6r4cwtLnN1Lhz0A70vW6tBf3p",
                   "https://drive.google.com/uc?export=view&id=1XZ24oWA_GIp8ugfyixhyooo25sy8CSB1",
                   "https://drive.google.com/uc?export=view&id=1g26jRfNBn8JKtfyZ1MSzFtm3MGiTdnhb",
                   "https://drive.google.com/uc?export=view&id=1nd6kcxPIYZos6NGcGxPTYA2-GJiV6reQ",
                   "https://drive.google.com/uc?export=view&id=14SmXrXQ-mBZ7dBBBtjJRp6_PpGBuwI_X",
                   "https://drive.google.com/uc?export=view&id=1LTfRoN1EDCeTC9SdaSF_XVqZM6Y1rBMZ",
                   "https://drive.google.com/uc?export=view&id=1Dt2btj9-PSXxtbddvVMJCDaRXpo14ZoI",
                   "https://drive.google.com/uc?export=view&id=18CBehY0eqQRgc0Y1ETHMpzyo8cFdgPUE",
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
        {"nama": "Fadya Izzatul 'Aini", "jabatan": "Staf PIKA", "nim": "124450062", "umur": "20", "asal": "Pringsewu", "alamat": "airan", "hobbi": "mancing", "sosmed": "@fadyaizzatul_", "kesan": "Kakaknya baikk, ramah, seruu", "pesan": "Semangat kuliahnya kakakk, semoga lancar dan sukses selaluu"},
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
    display_images_with_data(gambar_urls, data_list, key="mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1u0GPQcg6pHKddidEpCW03MXJf09nWlIS",
                   "https://drive.google.com/uc?export=view&id=1JTz0JQx0o9-41SIRGD65asvBT12cblY4",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=19rM4QJg_4tsWzJQVcz4iQGMy3TXh2-yu",
                   "https://drive.google.com/uc?export=view&id=1dIbxHxXQppoA-M3k5EepeIBTDQUVsy3d",
                   "https://drive.google.com/uc?export=view&id=1ZnDz5dmr5l393QuVk5n_jTLGG5Vz9npw",
                   "https://drive.google.com/uc?export=view&id=1NmEcnANricdiLQHQpOMmpoTRC0Hye78q",
                   "https://drive.google.com/uc?export=view&id=1xjrIXgMNPoQ2HWIy999JwbwxAo7082Tv",
                   "https://drive.google.com/uc?export=view&id=1_naA2Pr1kaARtrUhbugRY-kCZ2YJK8au",
                   "https://drive.google.com/uc?export=view&id=1aW5YaTpcIe2qXV7T7tcHXWcJl3vWjq58",
                   "https://drive.google.com/uc?export=view&id=1f1lZjkYB4GiIoHMD_9Z_4GHE5QFK-2kN",
                   "https://drive.google.com/uc?export=view&id=1B2zO2sAjI6f1wfg6j4laPwVWBGaBcKPn",
                   "https://drive.google.com/uc?export=view&id=1dzpXZ3fCjKBS1W2zAoCvIZ0_Au2xQOQR",
                   "https://drive.google.com/uc?export=view&id=1R_vevwV9Cc9w48X4QFc01NdkzzAULZM9",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1QM_o_q09j0JHvWvTY_vTxlDQAdwrqEOP",
                   "https://drive.google.com/uc?export=view&id=1XIbGvb-weBGgRegGDou624O_JMaSEMxV",
                   "https://drive.google.com/uc?export=view&id=1NI01CC_jV1yL6PEoK0TNs187fAWD7oJD",
                   "https://drive.google.com/uc?export=view&id=1Cirzwsa96DiGo8VzurOpFQ21X8yzyDAF",
                   "https://drive.google.com/uc?export=view&id=1XhM8mEeL6RGY90UOEVNV2HUa0w81muwm",
                   "https://drive.google.com/uc?export=view&id=1ZoMYZhC_1_jndLI6bYX7PjKDj1FTSYum",
                   "https://drive.google.com/uc?export=view&id=1cbKV3XfEjp40oQfndBzi438W3I79ymLP",
    ]
    
    data_list = [
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
        {"nama": "Selma Siti Aisyah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450044", "umur": "20", "asal": "Lampung", "alamat": "Balam", "hobbi": "Jalan jalan", "sosmed": "@selmasiti_aisyah", "kesan": "Kerenn banget", "pesan": "Selalu jadi orang baik"},
    ]
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1Qg9iT4ppQ45YFIjoEoIxQ_g6MTbWnynB",
                   "https://drive.google.com/uc?export=view&id=1Y7MDaZXYo5vgq7ys0OfAPb_gnc1VyAhx",
                   "https://drive.google.com/uc?export=view&id=1SaRStJOtsNOuFmJh4KugmkB4USQi8CEq",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bg farhan
                   "https://drive.google.com/uc?export=view&id=18crJAyEqY6DyIqbpZghKkkfWQQoxBbff",
                   "https://drive.google.com/uc?export=view&id=1BsDaOvqb1cUerICtSyA34NepJFIiyzPx",
                   "https://drive.google.com/uc?export=view&id=1z2zPCwICtKXmjKXPrkHz_36WJ13VSgSk", 
                   "https://drive.google.com/uc?export=view&id=1c0M4qugAMtMNI_582UFtOFPhXZe24Znt",
                   "https://drive.google.com/uc?export=view&id=1bJ_IJg4uEXqZceG0XwIt_QPvPKZReylK",
                   "https://drive.google.com/uc?export=view&id=1q93vvZb2ymsxed7qxBO5VYLdmS7myBU5", 
                   "https://drive.google.com/uc?export=view&id=1sDRImohzil7wDem8OWoo-UEeLUkeHLSN",
                   "https://drive.google.com/uc?export=view&id=1urUksXckK29uycn-PYEr5J3tm0wmV6R7",
                   "https://drive.google.com/uc?export=view&id=1o_wExnoejzGXjp6gRfN1pINRVpVS6by8",
                   "https://drive.google.com/uc?export=view&id=1GUdEDsFa2vtasR_pqN3jfvAKbl0BNQsz",
                   "https://drive.google.com/uc?export=view&id=1YTkJwCJ33mkzrI0ZWvZCuTiadQQNesHx",
                   "https://drive.google.com/uc?export=view&id=1sbgqsVlY3R_GQi_9S5Rs-fyFgCL6_0mv",
                  
    ]
    data_list = [
        {"nama": "Haikal Fransisko Simbolon", "jabatan": "Kepala Departemen Internal", "nim": "123450106", "umur": "20", "asal": "Jambi", "alamat": "Way Halim", "hobbi": "Ngeledek Orang", "sosmed": "@haikalsbln", "kesan": "Humornya sederhana tapi bikin akrab.", "pesan": "Jaga suasana cair tanpa berlebihan."},
        {"nama": "Kharisma Mustika Sari", "jabatan": "Sekretaris Departemen Internal", "nim": "123450034", "umur": "21", "asal": "Way Kanan", "alamat": "Untung Senopati", "hobbi": "Suka Nolong Orang", "sosmed": "@rismaa.mustika_", "kesan": "Cara bicaranya lembut tapi tegas.", "pesan": "Jangan ragu terus membimbing kami dengan sabar."},
        {"nama": "Hanna Gresia Sinaga", "jabatan": "Kepala Divisi Keharmonisasian", "nim": "123450038", "umur": "21", "asal": "Sumatera Utara, kisaran city", "alamat": "Sukarame", "hobbi": "Ngabarin Orang Tua", "sosmed": "@hanna_g_sinaga", "kesan": "Perhatiannya ke adik tingkat sangat besar.", "pesan": "Semoga kebaikan Kakak selalu kembali."},
        {"nama": "Ahmad Farhan Ghani", "jabatan": "Staf Ahli Keharmonisasian", "nim": "123450121", "umur": "21", "asal": "Kemiling", "alamat": "Kemiling", "hobbi": "Supporteran", "sosmed": "@farhanghani", "kesan": "Tegas saat mengambil keputusan.", "pesan": "Tetap adil dan pertimbangkan banyak hal."},
        {"nama": "Aisyah Khairun Nisa", "jabatan": "Staf Keharmonisasian", "nim": "124450096", "umur": "18", "asal": "Indragiri", "alamat": "Samping Makam Perwira 2", "hobbi": "Nyicipin Makanan", "sosmed": "@aisyahkhair._", "kesan": "Selalu rapi dan enak dilihat.", "pesan": "Tetap jadi panutan tanpa harus menggurui."},
        {"nama": "Cerine Sihotang", "jabatan": "Staf Keharmonisasian", "nim": "124450049", "umur": "20", "asal": "Medan", "alamat": "Belwis", "hobbi": "Suka Ngoding pakai R", "sosmed": "@cerine_ipynb", "kesan": "Pintar menenangkan saat kami panik.", "pesan": "Terus jadi tempat cerita yang aman."},
        {"nama": "Jaya Saputra Tamba", "jabatan": "Staf Keharmonisasian", "nim": "124450094", "umur": "18", "asal": "Medan", "alamat": "Pemda", "hobbi": "Mencari Nafkah", "sosmed": "@jay.saputra.mb", "kesan": "Suka membantu tanpa pamrih.", "pesan": "Semoga kebaikan Kakak berbuah baik."},
        {"nama": "Najla Nursyifa", "jabatan": "Staf Keharmonisasian", "nim": "124450051", "umur": "20", "asal": "Sumatra Barat", "alamat": "Belwis", "hobbi": "Nonton ASMR", "sosmed": "@njlanursyifa", "kesan": "Humornya segar dan tidak berlebihan.", "pesan": "Jaga energi positif itu sampai kapan pun."},
        {"nama": "Rozak Ramdani", "jabatan": "Staf Keharmonisasian", "nim": "124450100", "umur": "19", "asal": "Kalianda, Lampung Selatan", "alamat": "Korpri Raya", "hobbi": "Berantemin Kucing", "sosmed": "@rozakrabbani__", "kesan": "Disiplin dan tepat waktu.", "pesan": "Tularkan kebiasaan itu ke adik tingkat."},
        {"nama": "Teresa Christiani Purba", "jabatan": "Staf Keharmonisasian", "nim": "124450046", "umur": "19", "asal": "Riau", "alamat": "Belwis", "hobbi": "Masak", "sosmed": "@kristiani8872", "kesan": "Tegas saat organisasi butuh keputusan.", "pesan": "Tetap adil dan bijak dalam memimpin."},
        {"nama": "Muhammad Hanif Dzaky Arifin", "jabatan": "Kepala Divisi Kerohanian", "nim": "123450064", "umur": "21", "asal": "Padang", "alamat": "Way Kandis", "hobbi": "Nonton F1 & MotoGP", "sosmed": "@hnfdzky_", "kesan": "Berwibawa tanpa harus marah.", "pesan": "Terus jadi panutan yang bijak."},
        {"nama": "Audina Fitria", "jabatan": "Staf Kerohanian", "nim": "124450038", "umur": "20", "asal": "Sumatra Barat", "alamat": "Sukarame", "hobbi": "Masak", "sosmed": "@audinaf_03", "kesan": "Suka menolong tanpa banyak bicara.", "pesan": "Jangan lupa istirahat, Kak."},
        {"nama": "Cika Adelia Br Marbun", "jabatan": "Staf Kerohanian", "nim": "124450107", "umur": "20", "asal": "Bagan Batu, Riau", "alamat": "Belwis", "hobbi": "Dengerin Musik", "sosmed": "@cikamrbn", "kesan": "Disiplin soal waktu.", "pesan": "Ajari kami juga cara mengatur prioritas."},
        {"nama": "Gustin H Tampubolon", "jabatan": "Staf Kerohanian", "nim": "124450068", "umur": "21", "asal": "Sumatera Utara", "alamat": "Airan", "hobbi": "Nonton", "sosmed": "@gustinhaleluya", "kesan": "Pandai memberi nasihat praktis.", "pesan": "Terus jadi kakak yang solutif."},
        {"nama": "Muhammad Harvinsyah", "jabatan": "Staf Kerohanian", "nim": "124450128", "umur": "20", "asal": "Sumatera Selatan", "alamat": "Belwis", "hobbi": "Ngadu Ikan Cupang", "sosmed": "@muhvinz_", "kesan": "Ramah ke semua orang.", "pesan": "Pertahankan sikap terbuka itu."},
        {"nama": "Rafa Sabina Fahimah", "jabatan": "Staf Kerohanian", "nim": "124450036", "umur": "20", "asal": "Natar", "alamat": "Natar", "hobbi": "Nonton Drakor", "sosmed": "@snasaa._", "kesan": "Ramah ke semua orang.", "pesan": "Pertahankan sikap rendah hati itu."},
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1e2lyEW3Tt1s_reEotgt6YgXt6QgoxFNo",
                   "https://drive.google.com/uc?export=view&id=1nvNY6Q4-bvt4oZdnnhEjGoPt3xr2baeI",
                   "https://drive.google.com/uc?export=view&id=1DFI7WURFKOXwQ1LQUR3Eu9bGW3tEVE-O",
                   "https://drive.google.com/uc?export=view&id=1n2VOosrTtoArBMyCGoDmMecLGnGnTo6W",
                   "https://drive.google.com/uc?export=view&id=1KzdXaRGL_f_W-YQcPVKeLR1GfFhAv4zQ",
                   "https://drive.google.com/uc?export=view&id=1aRXo2dZIW5Kohof94cwtpQgHCQsT7ubY",
                   "https://drive.google.com/uc?export=view&id=11V7sGDZ4w5Z6bE4TomfZUcnQPl_2fJVf",
                   "https://drive.google.com/uc?export=view&id=1uXIjyfX6Cb9bOFGFdUtcrgdMBn9NCwZF",
                   "https://drive.google.com/uc?export=view&id=1603I5xBQpFHTPm0NMgyoOats53W2WHy1",
                   "https://drive.google.com/uc?export=view&id=1r6_C9O2tuNk1U6adKEs7W8lTTMaywsz-",
                   "https://drive.google.com/uc?export=view&id=1nUDxWI0MmRglG4nvEfuUcw9wcTIX7OoS",
                   "https://drive.google.com/uc?export=view&id=1-Tf7Dh2YmI7FAmz-BnTs48AjryAnRTAW",
                  
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Kepala Departemen SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Sekretaris Departemen SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Afifah Fauziah", "jabatan": "Kepala Divisi Kemitraan", "nim": "12345002", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Staf Kemitraan", "nim": "1234500", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@hasan.ramadhan08", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Layina Ropiqo", "jabatan": "Staf Kemitraan", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Moch. Iqbal Az-Zahir", "jabatan": "Staf Kemitraan", "nim": "122450052", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@iqbalazzahir_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Talitha Justine", "jabatan": "Staf Kemitraan", "nim": "122450076", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anadia Carana", "jabatan": "Kepala Divisi Kewirausahaan", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Abdillah Fikri Al pome", "jabatan": "Staf Kewirausahaan", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Staf Kewirausahaan", "nim": "124450008", "umur": "20", "asal": "Sumatera Barat", "alamat": "Samping kamar rafli", "hobbi": "Mancing Mania", "sosmed": "@dhalsetiawan", "kesan": "Sabar dan santai, enak diajak ngobrol.", "pesan": "Semoga hasil pancingannya selalu melimpah dan kuliahnya lancar."},
        {"nama": "Anggun Nita", "jabatan": "Staf Kewirausahaan", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Della Anisa Fitri", "jabatan": "Staf Kewirausahaan", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
    ]
    
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [ "https://drive.google.com/uc?export=view&id=1gv3ZHruRvhlqjqB0J12SCNq9VCGXZtHc",
        "https://drive.google.com/uc?export=view&id=1FG-5QwmDV7R5bgK3lRgvC55ozV-T8xEc",
        "https://drive.google.com/uc?export=view&id=1_70DlvPCXP-ieUQZ9xrTGkVm5bi75qiO",
        "https://drive.google.com/uc?export=view&id=1F_fy0dfhNKc-7bsu21cYxT1UDqSKHlc9",
        "https://drive.google.com/uc?export=view&id=1qAVzBUQq_QixAItTOsaFfbZC2KbcOAm2",
        "https://drive.google.com/uc?export=view&id=1q5XbzPqW6KaNjG6XzsXXYFficU-8qKwd",
        "https://drive.google.com/uc?export=view&id=18WVqqF7nxsjJ7c7IxtmDxAJ9gdbWhLJH",
        "https://drive.google.com/uc?export=view&id=1qrAYXB3Owg7DEMd1L7-f4jFaAHSW3Igp",
        "https://drive.google.com/uc?export=view&id=13mDNYZ-qMSJlMYZanFv660qduwh_Ngvr",
        "https://drive.google.com/uc?export=view&id=1nfV7vSieHHKnSPa9pK8wzPmKlEPAXUPM",
        "https://drive.google.com/uc?export=view&id=1SQSauv4w9N0FxOM6b_6MdWskVhONcr4f",
        "https://drive.google.com/uc?export=view&id=1hcCYJ1Hmzrg3xcyMgFrRCivDLnS0L9m3",
        "https://drive.google.com/uc?export=view&id=183prjg4UbgWRI1_0cjfCLjOk_cxZbIDN",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1ggfQxOGhgw7tNjK-t56bkmJARW_tlgSR",
        "https://drive.google.com/uc?export=view&id=1ATCPWdkLwWtCMlz49j7gyuypsD1kHCK9",
        "https://drive.google.com/uc?export=view&id=1PaSfCj8UMMs9Lzyp72SigsCnat0NXNmd",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
    ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Kepala Departemen Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Donna Maya Puspita", "jabatan": "Sekretaris Departemen Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Labo John Noel Napitupulu", "jabatan": "Kepala Divisi Dokumentasi", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anash Tasya Ausyaqila", "jabatan": "Staf Dokumentasi", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Felisya Nabila Putri Nugroho", "jabatan": "Staf Dokumentasi", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Razan Maulana Pratama", "jabatan": "Staf Dokumentasi", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Sania Dwi Ayu Lestari", "jabatan": "Kepala Divisi Media dan Konten Spesialis", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Allisha", "jabatan": "Staf Media dan Konten Spesialis", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Alya Ramadhanti", "jabatan": "Staf Media dan Konten Spesialis", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Bunga Clarisa Sefa", "jabatan": "Staf Media dan Konten Spesialis", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Difanya Husakina", "jabatan": "Staf Media dan Konten Spesialis", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Nazlah Auliya", "jabatan": "Staf Media dan Konten Spesialis", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Raihana Adelia Putri", "jabatan": "Kepala Divisi Visual Design", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Daffa Kharisma Adzana", "jabatan": "Staf Visual Design", "nim": "124450061", "umur": "21", "asal": "Surabaya", "alamat": "Sukarame", "hobbi": "-", "sosmed": "@daffascript", "kesan": "Kalem dan tidak banyak bicara, tapi tulus.", "pesan": "Jangan sungkan bergabung ngobrol bareng, Kak."},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Visual Design", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Visual Design", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Visual Design", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Zannuba Arifah Ilman", "jabatan": "Staf Visual Design", "nim": "124450112", "umur": "18", "asal": "Lampung Timur", "alamat": "Rajabasa", "hobbi": "Begong", "sosmed": "@xifasky", "kesan": "Sopan dan selalu menghargai orang lain.", "pesan": "Semoga selalu dimudahkan dalam setiap urusan, Kak."},
    ]
    display_images_with_data(gambar_urls, data_list, key="medkraf")

elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1rTmyPLmmDxWdvEsGojwQjDQTovodjHXH",
        "https://drive.google.com/uc?export=view&id=1-Ul5mfV_JXU_tk4ewgtPAwNKRjDvcI_O",
        "https://drive.google.com/uc?export=view&id=1koQA-1DFOIst7QmIp8QiqEG_i0uKC6hw",
        "https://drive.google.com/uc?export=view&id=1oBwVTXUj1JzhE1SfY7AJ6HW02kQqm4r9",
        "https://drive.google.com/uc?export=view&id=1S368q3066zNocOivsVIfT3HPMacAOnwU",
        "https://drive.google.com/uc?export=view&id=1HAGEusSLz7Op2kSiqAKU3BSS5nfonb1U",
        "https://drive.google.com/uc?export=view&id=1x4xqU9dtQfgjl_PD_inA2NfDJSl_IJnG",
        "https://drive.google.com/uc?export=view&id=13FW3ZkOoZlrV3z8mmEN71GWzGeDPjnU_",
        "https://drive.google.com/uc?export=view&id=1ELAQDS9dg80CPedaIymlWZh0l5uSefp9",
        "https://drive.google.com/uc?export=view&id=1ezjw-g4sBfWNZuNWvWHfUlKpUs8qgzMG",
        "https://drive.google.com/uc?export=view&id=10dw6LaqrRzuGU9ndHKfU74mW0yxsYRqf",
        "https://drive.google.com/uc?export=view&id=1BDlk31IbbCvMF9wBAneSRfrCItNHpP-J",
        "https://drive.google.com/uc?export=view&id=1dOPlMxo4Ztv6ZAjYS0USlm18DSK6CB7c",
        "https://drive.google.com/uc?export=view&id=16-Va12Or_hc5nfa2s2GXuya756S666Mk",
        "https://drive.google.com/uc?export=view&id=13oe9JWflY4KkHze5eszVV7xJ-4uKfWXF",
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
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450089", "umur": "20", "asal": "Padang", "alamat": "Kota Baru", "hobbi": "Bangun pagi", "sosmed": "@muhammdrafka_", "kesan": "Disiplin dan selalu memulai hari lebih awal.", "pesan": "Ajari kami cara menjaga konsistensi, Kak."},

    ]

    display_images_with_data(gambar_urls, data_list, key="minbak")
