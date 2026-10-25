 from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1O8Hdk8gKy-_C0kCpfuSv9X019Mvrb4QE",
        "https://drive.google.com/uc?export=view&id=1StyofloEs_iOq9Zje0CJIyXzhylLPksd",
        "https://drive.google.com/uc?export=view&id=1EwD0V_6O62f4DT85HapgYpXDw-HxwFwn",
        "https://drive.google.com/uc?export=view&id=1bHaikGXHPSiM32Urd8nHtH4IT6uWr92x",
        "https://drive.google.com/uc?export=view&id=1qqBsuTQPn0rlRaxQdF2VeCAwlvJ-xQAX",
        "https://drive.google.com/uc?export=view&id=1fkYTfgRpyAGaUqAlm_IKhBI2h-uxHFAg",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, dlu pernah jadi kadiv op pas natal SD25 bisa diajak serius dan bercanda.", "pesan": "Semangat dan sukses selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya seru bisa diajak bercanda dan bisa diajak bicara serius.", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya murah senyum.", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya soft spoken, lucuu.", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, dan suka duit.", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk.", "pesan": "Sukses selalu dan semangat kakkk!!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1Gq721WJrTyFsywgM3BSRAjnGGaaxzO9y",
        "https://drive.google.com/uc?export=view&id=1oiBDEvD0PT8yvcS17k9gY-qqVvchF4zC",
        "https://drive.google.com/uc?export=view&id=12QNxmLbfb7MmkyrH_HjDgT4Gmk-GwcfD",
        "https://drive.google.com/uc?export=view&id=16xwz9_Ow1xNG61kDid-w7f9of4dw4f4O",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  # ← placeholder (ID kosong)
        "https://drive.google.com/uc?export=view&id=17dGzcViYFmqfUyVeis6UDYP3nU6dPwz8",
        "https://drive.google.com/uc?export=view&id=1zs_XV54xixTDdvIfq2EDZBhaOdnA0OI8",
        "https://drive.google.com/uc?export=view&id=191UTZmimVAelyNiHq9kJrsYZ4gr1tijQ",
        "https://drive.google.com/uc?export=view&id=1iw5DhwUhI8hyo9N1DNE3gPIHjj1zqlZA",
        "https://drive.google.com/uc?export=view&id=1eIFzF5EXywwKbiNg6_d56DJ1l-CKzP-x",
        "https://drive.google.com/uc?export=view&id=1mRDZgRu_bxEv6uQNkmhf6Byfljzm-g1q",
        "https://drive.google.com/uc?export=view&id=15gx_6z3bTDo2ukpG7xwX9Iq04NbMkxYm",
        "https://drive.google.com/uc?export=view&id=13nR5eXGPrWe_VPyOxSLyNeJ8wZWW4239",
    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Kuala lumpur", "alamat": "GH", "hobbi": "Bernyanyi", "sosmed": "@iamridhomanik", "kesan": "Abangnya asikk bangettt", "pesan": "Semogaa dilancarkan TA nya"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Repeat lagu lover by taylor swift", "sosmed": "@j__eesie", "kesan": "Cantik dan kerenn banget kakaknyaa dari awal jadi kakak asuh", "pesan": "Semangat teruss untuk menyebar kebaikan"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I Legislasi", "nim": "123450023", "umur": "19", "asal": "Lampung", "alamat": "BAndar Lampung", "hobbi": "Suka Nonton AGZ", "sosmed": "@ddharu_", "kesan": "Public speaking nya keren banget pas pilmapres", "pesan": "Semangat teruss bang"},
        {"nama": "Gh Mikael Niko A S", "jabatan": "Staf Komisi I Legislasi", "nim": "123450025", "umur": "20", "asal": "Jombang", "alamat": "Jati agung", "hobbi": "Cari mangsa", "sosmed": "@me._kael", "kesan": "Abangnya kerenn, suka sama mindsetnya", "pesan": "Sukses selalu bang"},
        {"nama": "Siti Sarifah Sumamah", "jabatan": "Staf Komisi I Legislasi", "nim": "124450015", "umur": "18", "asal": "Palembang", "alamat": "Kedaton", "hobbi": "Buat pempek", "sosmed": "@syt.sarifa", "kesan": "Keren kak", "pesan": "Semoga selalu jadi orang baik"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II Pengawasan", "nim": "123450078", "umur": "20", "asal": "Gn. pesagi", "alamat": "Sukabumi", "hobbi": "Minum kopi", "sosmed": "@givarooo", "kesan": "Abangnya mirip temen saya namanya afdhi", "pesan": "Semangat trus bang mengawasnya"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staf Komisi II Pengawasan", "nim": "124450042", "umur": "20", "asal": "Krui", "alamat": "Jatimulyo", "hobbi": "Memancing", "sosmed": "@afghanisnt_", "kesan": "Masyaallah cantik dan pintar sekali", "pesan": "Semoga garde metnum nyaa nular"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staf Komisi II Pengawasan", "nim": "124450020", "umur": "19", "asal": "City Earth", "alamat": "Sukarame", "hobbi": "Baca AU", "sosmed": "@haniquratuain_", "kesan": "Masyaallah kakaknya cantik", "pesan": "Semoga sukses selalu"},
        {"nama": "Jeremia Halim", "jabatan": "Staf Komisi II Pengawasan", "nim": "124450101", "umur": "20", "asal": "Beijing", "alamat": "Teluk", "hobbi": "Olahraga", "sosmed": "@jeremia_hm", "kesan": "Abangnya keren", "pesan": "Sukses selalu!"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III Aspirasi dan Media Informasi", "nim": "123450073", "umur": "21", "asal": "Sumatera Utara", "alamat": "Kota Baru", "hobbi": "Tidur", "sosmed": "@monica_tjg", "kesan": "Kakaknya kalem", "pesan": "Semoga dilancarkan semester akhirnya!"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staf Komisi III Aspirasi dan Media Informasi", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda Raya", "hobbi": "Ngegym dan koleksi figure", "sosmed": "@nagatseee", "kesan": "Abangnya baik dan asik", "pesan": "Semoga selalu dikelilingi orang baik"},
        {"nama": "Sekar Dini Widya Putri", "jabatan": "Staf Komisi III Aspirasi dan Media Informasi", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "main", "sosmed": "@sekardnwp", "kesan": "Kakaknyaa ku kira jutek tapi ternyata baikk poll", "pesan": "Semangat terus kak"},
        {"nama": "Wan Nashwa Alhasni Yuska", "jabatan": "Staf Komisi III Aspirasi dan Media Informasi", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa", "sosmed": "@nshaysk", "kesan": "Kakak kerenn", "pesan": "Semoga suksess selalu kak"},
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1wwWGsW-AO44wdQmH2qVQ7L-m4-P7wAXn",
        "https://drive.google.com/uc?export=view&id=1HSvFRlzHJiZ0n3dt_P1dkfge-1wO95lS",
        "https://drive.google.com/uc?export=view&id=17VdkMgHGub3cmKXuP98zSPDcfUwgPMIr",
        "https://drive.google.com/uc?export=view&id=1u2frj_YYoOrS_Cfay0MzlNEJEacAoi6h",
        "https://drive.google.com/uc?export=view&id=1KGVJBJlRPwwDLqxlsJCQZMTdbbUp5fX0",
        "https://drive.google.com/uc?export=view&id=1K6A4YkdwH9MnteDhRvQW_Tqca9_0TBLR",
        "https://drive.google.com/uc?export=view&id=1f3b0xdrOUuH8E795sBK_QxpVYrUY0HaR",
        "https://drive.google.com/uc?export=view&id=1rpOYIpdKf15cTD2O82ePy4Cyr0_A_MUX",
        "https://drive.google.com/uc?export=view&id=1__HMT-dabPEY3s6znKGMQcXLpZ4uCwwb",
        "https://drive.google.com/uc?export=view&id=1r0WwnROfsy2432-5l_bivtDlXi978e5f",
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator Mahasiswa", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Kepala Biro Aspirasi dan Media Komunikasi", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya asik", "pesan": "Terus berkarya!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Suci Aulia", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Kepala Biro Kajian Strategis dan Propaganda", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Kepala Biro Kesekretariatan", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Staff Biro Kesekretariatan", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="senator")

elif menu == "Departemen PSDA":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1ugRy9I-IThSGyshDV40ZZCj5Ij0zA_dM",
        "https://drive.google.com/uc?export=view&id=1XL5MVecX_5eBy_qYPQSHipW7_NM3YC6u",
        "https://drive.google.com/uc?export=view&id=1oDy2uDWrLDhJKXWoKncsTHvLcS6uoBYb",
        "https://drive.google.com/uc?export=view&id=1ubIf8n1wNXmS1mSg5XEecHUg5flXufBz",
        "https://drive.google.com/uc?export=view&id=1m--jD9dD3qj7en8icFLz4X0WD8A3WDbt",
        "https://drive.google.com/uc?export=view&id=1byXG-3ZAOu55VsJu6gMxcowDlhESJF8T",
        "https://drive.google.com/uc?export=view&id=17a0GCKlbImpkVqwRJyNJht1N9UwDRcuH",
        "https://drive.google.com/uc?export=view&id=1-DL-YEtkYoOdmMG74Jv_IiSJrXJCC8A_",
        "https://drive.google.com/uc?export=view&id=1HJbCosZONLYJ6F2H3T4Ep5LeXRUV73ir",
        "https://drive.google.com/uc?export=view&id=1tLwohSuK2xfdrCpX9I6yJbtGFzy9YMlR",
        "https://drive.google.com/uc?export=view&id=1ITrIaHsNGIYrLBeFjKaqmNqekWH0pV8C",
        "https://drive.google.com/uc?export=view&id=1AVbyN636abRPwg26jT3Q1Pqe9cp37OFg",
        "https://drive.google.com/uc?export=view&id=1VDgB7thn0EFUarebPi-mgOl5JGuNE4-C",
        "https://drive.google.com/uc?export=view&id=16PnYv63FMdmq-gQ5VlBrLVuuuZ0K22GJ",
        "https://drive.google.com/uc?export=view&id=1E4hWGT1PdW0kbULKbGmeEI-wdph84SMe",
        "https://drive.google.com/uc?export=view&id=13aI1RPyvr1xLgDwM8qc_QtZDWZM_67IH",
        "https://drive.google.com/uc?export=view&id=1u8mLN491Z3DCf95uaIjX82zeMTsazbu1",
    ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "123450097", "umur": "21", "asal": "Pinggir pantai", "alamat": "Samping kost kapo", "hobbi": "Ngerjain anak kader", "sosmed": "@arientakhsnl_", "kesan": "Cantikk banget kak, makeupnya flawless", "pesan": "Semangat jadi kadep psda, dan selalu keren kak"},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "123450022", "umur": "20", "asal": "palembang", "alamat": "Pudan kost", "hobbi": "Pacaran", "sosmed": "@vany.salsabilaa", "kesan": "kakanya lucuu", "pesan": "semangatt kak sekdep"},
        {"nama": "Nobel Nizam F", "jabatan": "Kepala Divisi Kaderisasi", "nim": "123450023", "umur": "21", "asal": "Bandar lampung", "alamat": "Bandar lampung", "hobbi": "Banyak", "sosmed": "@nobelnizam", "kesan": "Keren main sulap kartunya", "pesan": "semoga semakin banyak trik sulapnyaa bang"},
        {"nama": "Afriza Azmi", "jabatan": "Staf Kaderisasi", "nim": "124450110", "umur": "20", "asal": "Malang", "alamat": "Lapangan", "hobbi": "Berantem", "sosmed": "@friezazmi", "kesan": "enerjik banget pas damaskusan", "pesan": "semangatt terus bangg"},
        {"nama": "Ayake Alfatih Ramadan", "jabatan": "Staf Kaderisasi", "nim": "124450059", "umur": "21", "asal": "Kota diatas solok, Sumatera Barat", "alamat": "Pemda", "hobbi": "Cekek ayam", "sosmed": "@ykeall", "kesan": "Abangnya super duper baik", "pesan": "Tetap semangat menjalani perkuliahannya bang"},
        {"nama": "Caesar Ozora Alrando", "jabatan": "Staf Kaderisasi", "nim": "124450017", "umur": "20", "asal": "Metro", "alamat": "Korpri", "hobbi": "Pulang kampung", "sosmed": "@caesar.oriza", "kesan": "Abangnya galak pas jadi komdis pplk", "pesan": "Semoga sukses selalu bang"},
        {"nama": "Euodia Meiliana Friedita", "jabatan": "Staf Kaderisasi", "nim": "124450029", "umur": "18", "asal": "Dari mana aja boleh", "alamat": "Dalam kamar dibalik pintu", "hobbi": "Surving", "sosmed": "@yudiameilanaa_", "kesan": "tau kak yudia pas jadi komdis pplk, galakk", "pesan": "Selalu menjadi orang yang asik"},
        {"nama": "Haikal Seventino Tamba", "jabatan": "Staf Kaderisasi", "nim": "124450032", "umur": "20", "asal": "Jambi", "alamat": "Belakang pemancingan", "hobbi": "Tidur", "sosmed": "@_haikaaall", "kesan": "Abangnya keliatan agak jarang ngomong", "pesan": "Semoga dikelilingi orang baik"},
        {"nama": "Putri Manna Anantama Simbolon", "jabatan": "Staf Kaderisasi", "nim": "124450056", "umur": "18", "asal": "Depok", "alamat": "Oiya cafe", "hobbi": "Jalan kaki gaboleh naik gojek", "sosmed": "@putrimannaa", "kesan": "Energi kak putri gapernah abis", "pesan": "Jaga kesehatan biar full energy trus kak"},
        {"nama": "Queenta Thifaal Nabila", "jabatan": "Staf Kaderisasi", "nim": "124450059", "umur": "19", "asal": "Rumah Sakit", "alamat": "Depan pemancingan", "hobbi": "Makanin anak ayam", "sosmed": "@queentanaabila", "kesan": "Keliatan galak ternyata engga", "pesan": "Selalu jadi orang baik"},
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi Peningkatan Mutu Anggota", "nim": "123450114", "umur": "25", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Ngejek orang", "sosmed": "@desmannal_", "kesan": "Abangnya asik", "pesan": "Semoga selalu menjadi asik dimanapun"},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450041", "umur": "19", "asal": "Bandar lampung", "alamat": "Sukarame", "hobbi": "Makan aice", "sosmed": "@azzelytn", "kesan": "Kakaknyaa seruu", "pesan": "Semangat selalu kak"},
        {"nama": "Charrlindah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450037", "umur": "21", "asal": "Jakpus", "alamat": "Cendrawasih 1", "hobbi": "Ngurus peternakan", "sosmed": "@charrlln", "kesan": "Masyaallah kakaknya biutipul bangettt", "pesan": "Semangatt yaa kak menjalani semester ini"},
        {"nama": "Jeremi Marolop P. Situmorang", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450111", "umur": "16", "asal": "Bandung", "alamat": "RS Airan", "hobbi": "Mengembala anak ayam", "sosmed": "@jemarro", "kesan": "Semangat kali pas damaskus", "pesan": "Semoga semangat nya terjaga terus"},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450048", "umur": "18", "asal": "Lamteng", "alamat": "Belwis", "hobbi": "Padel sama azel", "sosmed": "@n.bila_a", "kesan": "Kakaknyaa seru", "pesan": "Semangat main padelnya kak"},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450007", "umur": "20", "asal": "Sumatera Utara", "alamat": "Disamping kos zemar", "hobbi": "Mancing", "sosmed": "@dearfkvml", "kesan": "Story ig abangnya estetik", "pesan": "Semangat bangg, semoga menjadi apa yang diinginkan"},
        {"nama": "Salavi Naharani", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450090", "umur": "20", "asal": "Lampung timur", "alamat": "Jatimulyo", "hobbi": "Minum air putih", "sosmed": "@afi.nhr", "kesan": "kakaknya asik uhuyyy", "pesan": "Stay hydrated kak"},
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1DdlTvhV_IHRp2pLnFOg9_R6hwifUdAi3",
                   "https://drive.google.com/uc?export=view&id=1uu3WVTgThmdb5IGJTLUDvTAxc5UPZetz",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1Hg-at84TY5BZNS7T7dYRT2plzrzjN1d-",
                   "https://drive.google.com/uc?export=view&id=1Cagmb4GkTWg43p-sZC62wLzhgmo4pw3r",
                   "https://drive.google.com/uc?export=view&id=1c4ygQVJNbGSGi_YPmj2VxJQFkNpz-vO-",
                   "https://drive.google.com/uc?export=view&id=1ZUFTw-Syj0dmb3tHqXaHxKEl4aDiPjq6",
                   "https://drive.google.com/uc?export=view&id=1RE7jBZjEZSHZf-YrP1bYUj8RLhPDJnNX",
                   "https://drive.google.com/uc?export=view&id=1UU1Inom3VJbG25CqFIFbxyfZK96BU7rq",
                   "https://drive.google.com/uc?export=view&id=1eQzTKCvMpPc2Vidkz5beKKeA0F76p8Pq",
                   "https://drive.google.com/uc?export=view&id=13R7sRXGwDfTEmXcKMRT8_crO7VBWrd5Y",
                   "https://drive.google.com/uc?export=view&id=1eF9KUOWAKDcqJRWtxGlnfUv9mpqA8Bct",
                   "https://drive.google.com/uc?export=view&id=1HrLEKsv7LruhLUOa-4CNAh-_JS0loETp",
                   "https://drive.google.com/uc?export=view&id=1R6jZnyi2EoXGrWCcl5vjBqsNMEaHGLtK",
                   "https://drive.google.com/uc?export=view&id=1G2TWxewZ1yj5Vk_IId9hM9rzHrTeooAQ",
                   "https://drive.google.com/uc?export=view&id=1IuxevFNdf0zqdKrCaTwmAV3RcAC3iXtn",
                   "https://drive.google.com/uc?export=view&id=1-ocXOWd-gRrOiC2vzqlnBIOAFEH0Fnqa",
                   "https://drive.google.com/uc?export=view&id=1uEy3YfhYAC78Bgm9dGaHVFn6Rck2rkCQ",
                   "https://drive.google.com/uc?export=view&id=1jYa5mYZipzPqL4TubMbxesUdO7HoSqT1",
                   "https://drive.google.com/uc?export=view&id=1pH2wJDpzDW5KXt-j2O3vcW0RfpRR6zOv",
                   "https://drive.google.com/uc?export=view&id=1GAAqX8Dq2NaCL_vWSprnhjSluEPXPiDp",
                   "https://drive.google.com/uc?export=view&id=1MLUlRflJsLn68fa0YSCujidsqdiDP7Md",
    ]
    data_list = [
        {"nama": "Fabio Banyu Cyto", "jabatan": "Kepala Departemen MIKFES", "nim": "123450104", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
        {"nama": "Anggota MIKFES", "jabatan": "Staf MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1edYLLL1u3UZrqblLBKBmStDBf5Tay6ca",
        "https://drive.google.com/uc?export=view&id=1PFQzdEMoiWxNo-lUjnhCWydRhO4urgyR",
        "https://drive.google.com/uc?export=view&id=13o7QW1yOQb_2E2NiroMZInXtK9HqR4xO",
        "https://drive.google.com/uc?export=view&id=1eSUZWOJYeRdQ3_tQmdoCI5F0ICfKErfP",
        "https://drive.google.com/uc?export=view&id=1cRMRgofZQTOLk_tHLp31YogsPu7ZyYgv",
        "https://drive.google.com/uc?export=view&id=1aWF7m2zsNuhWAUA8H5qwBwaqO8fCHKXr",
        "https://drive.google.com/uc?export=view&id=1PpC-gYxAopgXYU6xmDhOwvn7sAPrbejK",
        "https://drive.google.com/uc?export=view&id=10lA64ZlPVk_THaKnPcVBqq_MZ_GwxVCG",
        "https://drive.google.com/uc?export=view&id=1o3sOSrrs9jyX_gwig1ZOZg7w2FTQPHze",
        "https://drive.google.com/uc?export=view&id=19iciQLziMHfq7t5KQTD_xbLXAXgCk95v",
        "https://drive.google.com/uc?export=view&id=1GY8mLHw3xop7c10KYetk25Widy6HvDKT",
        "https://drive.google.com/uc?export=view&id=1C8-tBGwFMkuwBYAiSKjJTgSDr0k_cbYg",
        "https://drive.google.com/uc?export=view&id=1lecKqZn8l3FuZana5s4F3Sa-CkEfyDWn",
        "https://drive.google.com/uc?export=view&id=1b2NmSV_pUhYatJqYvRgpDdpaMLvyCQyh",
        "https://drive.google.com/uc?export=view&id=1DeciTlNBj11XT5ts7HKgQzz8aqVwGnF-",
        "https://drive.google.com/uc?export=view&id=1vNVDXzqiTdjFgh1jltrkK-2EixDmiC0r",
        "https://drive.google.com/uc?export=view&id=1MpOnt7sgxvg-97ZD0JKsDv_CeAZ9MhPo",
        "https://drive.google.com/uc?export=view&id=12JVqNQaSWS8D6rBPUocrhfs8YrHfSKol",
        "https://drive.google.com/uc?export=view&id=1V6GG2d2PwAWdnXbIMedzK8ABTQch1Fst",
        "https://drive.google.com/uc?export=view&id=1iSJK_e3egg7XxxDYj2HzerIRefCPJG2-",
        "https://drive.google.com/uc?export=view&id=1U8fAoCtmsu-hp8fZF5MTBfICMJUrFo1b",
        "https://drive.google.com/uc?export=view&id=1E7uWK9r2_EnAvJNvMc22X3jEE51mZd0k",
    ]
    data_list = [
        {"nama": "Arini Puteri Elandra", "jabatan": "Staf Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Murah Senyum", "pesan": "Selalu jadi orang baik ya kak"},
        {"nama": "Nabyla Sharfina", "jabatan": "Staf Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "Ramah", "pesan": "Selalu jadi orang baik"},
        {"nama": "Khoirul Muttoharoh", "jabatan": "Staf Eksternal", "nim": "1234500", "umur": "-", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Main", "sosmed": "@khoirul_muttoharoh", "kesan": "Enak diajak ngobrol", "pesan": "Semangat terus bangg"},
        {"nama": "Ahmad Rizky", "jabatan": "Staf Eksternal", "nim": "123450050", "umur": "21 Tahun ini Alhamdulillah", "asal": "Tangerang Selatan", "alamat": "GH", "hobbi": "Ngga ngapa ngapain", "sosmed": "@ahmad.rizky__", "kesan": "Kerenn bangett bang", "pesan": "Selalu jadi orang yang kritis"},
        {"nama": "Adinda Deswita Maharani", "jabatan": "Staf Eksternal", "nim": "124450083", "umur": "10", "asal": "Lampung", "alamat": "Sukabumi", "hobbi": "Jadi idol", "sosmed": "@adindaadma", "kesan": "kakaknya asik", "pesan": "selalu asik ya kakk"},
        {"nama": "Ahmad Bimo Akbar Arkana", "jabatan": "Staf Eksternal", "nim": "124450113", "umur": "-", "asal": "Tanggamus", "alamat": "Bandar lampung", "hobbi": "Lihat lihat perumahan", "sosmed": "@bimo_arkana", "kesan": "Ramah", "pesan": "Selalu jadi orang yang ramah tamah"},
        {"nama": "Alfaya Abiyyi", "jabatan": "Staf Eksternal", "nim": "124450006", "umur": "nelson piquet", "asal": "Balam", "alamat": "Balam", "hobbi": "Makan yang manis biar manis", "sosmed": "@alfabiyi", "kesan": "Keren", "pesan": "Semangat terus"},
        {"nama": "Asri Meilani", "jabatan": "Staf Eksternal", "nim": "124450010", "umur": "20", "asal": "Lampung barat", "alamat": "Korpri raya", "hobbi": "Nonton film", "sosmed": "@asrmeilani", "kesan": "Sangat ramah", "pesan": "Terus jadi orang ramah kak"},
        {"nama": "Bima Ekayasa", "jabatan": "Staf Eksternal", "nim": "124450106", "umur": "-", "asal": "Lampung", "alamat": "Bandar lampung", "hobbi": "Berlaku humoris dan manis", "sosmed": "@bimayasa_", "kesan": "Ramah", "pesan": "Selalu jadi orang yang ramah tamah"},
        {"nama": "Indah Khairunnisa", "jabatan": "Staf Eksternal", "nim": "124450077", "umur": "20", "asal": "Ampera", "alamat": "Disini aja", "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang", "sosmed": "@khaindaa_", "kesan": "kakaknya asik", "pesan": "selalu asik ya kakk"},
        {"nama": "Riska Erlis Dayu Tiara", "jabatan": "Staf Eksternal", "nim": "124450022", "umur": "20", "asal": "Palembang", "alamat": "Bebas", "hobbi": "Ngefollow-up chat", "sosmed": "@erlsriska", "kesan": "Cantik banget", "pesan": "selalu ramah ya"},
        {"nama": "Yollanda Agustina", "jabatan": "Staf Eksternal", "nim": "124450024", "umur": "-", "asal": "Kerangka bawang sebelah barat", "alamat": "Kayu mulya", "hobbi": "Tanya bang henry", "sosmed": "@yollanda_agustina16", "kesan": "aktif banget", "pesan": "inget istirahat kak"},
        {"nama": "Aditya Taufiqurrohman", "jabatan": "Staf Eksternal", "nim": "123450032", "umur": "-", "asal": "Tetangga kadep", "alamat": "Belwis", "hobbi": "Memancing keributan", "sosmed": "@adityatfq", "kesan": "Jail", "pesan": "jangan sering mancing keributan bang"},
        {"nama": "Fathya Intami Gusda", "jabatan": "Staf Eksternal", "nim": "123450095", "umur": "-", "asal": "Tangsel", "alamat": "Sukarame", "hobbi": "Baca wattpad", "sosmed": "@fatthyaa_", "kesan": "Lucuu", "pesan": "selalu lucuu kak"},
        {"nama": "Tarisya Hidayatul Rahmi", "jabatan": "Staf Eksternal", "nim": "123450052", "umur": "-", "asal": "Luhak tanah data", "alamat": "gerbar", "hobbi": "Jadi orang baik", "sosmed": "-", "kesan": "kakaknya lucuu", "pesan": "tetep jadi asprak yang keren ya kak"},
        {"nama": "Ashila Islamisahfa Vanisha", "jabatan": "Staf Eksternal", "nim": "124450028", "umur": "20", "asal": "Sini", "alamat": "Jauh pokoknya", "hobbi": "Tidur", "sosmed": "@kshigf", "kesan": "kocak", "pesan": "Selalu tertawa terus kak"},
        {"nama": "Danil N Fadillah", "jabatan": "Staf Eksternal", "nim": "124450103", "umur": "-", "asal": "Karawang", "alamat": "belakang polda", "hobbi": "Ngasi makan ikan cupang", "sosmed": "@d4niel_fdlh", "kesan": "softboy", "pesan": "Selalu kalcer bang"},
        {"nama": "Favian Arkaanda", "jabatan": "Staf Eksternal", "nim": "124450021", "umur": "-", "asal": "Swiss", "alamat": "Tanya bapas", "hobbi": "Ngesen kanan", "sosmed": "@fvnnn05", "kesan": "Keren", "pesan": "Semangat terus dan humoriss bang"},
        {"nama": "Muhammad Fathiy Zumar Yazid", "jabatan": "Staf Eksternal", "nim": "124450081", "umur": "20", "asal": "Situlah", "alamat": "Pohon mulya", "hobbi": "Nyari hobi", "sosmed": "@zydddddd__", "kesan": "Hebat dan tegas", "pesan": "selalu jadi orang keren dan ramah tamah"},
        {"nama": "Muhammad Rizaldi", "jabatan": "Staf Eksternal", "nim": "124450093", "umur": "masih mudalah", "asal": "Rahim ibu", "alamat": "Pasar lantai 3.5", "hobbi": "Gambarr", "sosmed": "@jaldii._", "kesan": "keren jadi mc pplk 2025", "pesan": "selalu ramah ya bang"},
        {"nama": "Saskia Nova Magdalena", "jabatan": "Staf Eksternal", "nim": "124450074", "umur": "20", "asal": "Banyak begal", "alamat": "Pinggir jalan", "hobbi": "Nonton Tinkerbell", "sosmed": "@snova.19", "kesan": "kakaknya lucu", "pesan": "Terus jadi orang ramah kak"},
        {"nama": "Selma Siti Aisyah", "jabatan": "Staf Eksternal", "nim": "123450044", "umur": "20", "asal": "Lampung", "alamat": "Balam", "hobbi": "Jalan jalan", "sosmed": "@selmasiti_aisyah", "kesan": "Kerenn banget", "pesan": "Selalu jadi orang baik"},
    ]
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1n_PnSsF4BaBwk5Yubcr4YwrtwgvVQ_AP",
                   "https://drive.google.com/uc?export=view&id=1rbUfBqtkcx4V1IQPR707FbJDdt77F4qn",
                   "https://drive.google.com/uc?export=view&id=1YTazUOb799jV1jQly5ObYpoPf15q_30O",
                   "https://drive.google.com/uc?export=view&id=13X3TF2z2678-CLp0XWBtazaEnYxZ-GZB",
                   "https://drive.google.com/uc?export=view&id=1ZCQ4X4xE16OcrZThORC6JltKcFNvDSr8",
                   "https://drive.google.com/uc?export=view&id=1PzRzluaM14nkCFUBK3ZP5sza2I0-IUb8",
                   "https://drive.google.com/uc?export=view&id=1DIkWCmeTsXJYGjmMNIGqpBb6FIZJ7L9e",
                   "https://drive.google.com/uc?export=view&id=1xkS7pAsoSmEMPQUN66EPzP7zKJY_avDK",
                   "https://drive.google.com/uc?export=view&id=10RG54r4iIUd6fjjqE849eXMg9wCgn5Sq",
                   "https://drive.google.com/uc?export=view&id=1RtsPaV6uz7GMNpzRqwXkTtH2yvv91Hiy",
                   "https://drive.google.com/uc?export=view&id=1elAIy2diXFK-zbd37iF24CFi28ChxWPl",
                   "https://drive.google.com/uc?export=view&id=1ueR_DPLcWwgJjn5-kKOzUsyCznVvGdpB",
                   "https://drive.google.com/uc?export=view&id=1UvN0gTDwkEEQzJc9rHy8Eg5fGw9q6EVf",
                   "https://drive.google.com/uc?export=view&id=1ROAG3lly5nA6qQSKIeAQeaZTn5wnztB9",
                   "https://drive.google.com/uc?export=view&id=194BrrFTusOJnJLdX0kfgPqR0kFGXvykh",
                   "https://drive.google.com/uc?export=view&id=18VwyRlmM3U6Qn0-6sSJDPfG4av9W6VKw",
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
        {"nama": "Rafa Sabina Fahimah", "jabatan": "Staf Kerohanian", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"},
    
    
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1a9Gya_3s0X00vuVczeODWXraOCptHSDs",
        "https://drive.google.com/uc?export=view&id=105y95kRrqa90iJYLw2bQ0VD84SehYXvG",
        "https://drive.google.com/uc?export=view&id=1hblbMgfhyrh3yh51kbcMnvBDEE-emctL",
        "https://drive.google.com/uc?export=view&id=1COH5q8IwCdhYBTiRuYe2OEqYOlXlGAUE",
        "https://drive.google.com/uc?export=view&id=1KBfMWAvUhj3LlAy7LL29axIkRSyAmoU_",
        "https://drive.google.com/uc?export=view&id=1eKwX58lyZnDEDPJ100i8CfxWvzcDwLnh",
        "https://drive.google.com/uc?export=view&id=1pWzu1KdYVmtplwUmaBSn540d9Mk8MpG2",
        "https://drive.google.com/uc?export=view&id=1atEe31izGMh-lAkXxir1VmENEmuGxiVI",
        "https://drive.google.com/uc?export=view&id=16Kr195WuVpeJnxyPcFah7onZwgEs3mgT",
        "https://drive.google.com/uc?export=view&id=1kxmuQxbaShMxXIKvXuO-oT7Zvoppoxzj",
        "https://drive.google.com/uc?export=view&id=1uLF9AUII7Ijn-QV4uqgoY4GbWwA2W3L3",
        "https://drive.google.com/uc?export=view&id=15eiWYVqhjpgaxf4L8HOU0Hhubb9M_6LZ",
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
        "https://drive.google.com/uc?export=view&id=1Q9gSTbuaxL_N-SbunBTdFshUH9jpOk7v",
        "https://drive.google.com/uc?export=view&id=1Z-8_6GPJo1i8dJ1rhsO6JReuUMJc-tI8",
        "https://drive.google.com/uc?export=view&id=1wK69K5p7Pldi8mSCG-QQQ7RLcrCzeRar",
        "https://drive.google.com/uc?export=view&id=1rPobh6QZzAm6U0EI0dTlxFT-KojZOUug",
        "https://drive.google.com/uc?export=view&id=16TyEPdtxYK5NkNRymzOlR43ViTG4Gx0i",
        "https://drive.google.com/uc?export=view&id=1xFnI-sayHDOZvt4TUTgeOnFQ9xTxh07m",
        "https://drive.google.com/uc?export=view&id=14o4hC0pJxmKPDzGzhUZgf5XLmPuXw2xm",
        "https://drive.google.com/uc?export=view&id=1sTjC3qNi0s35dXiF4bLFk03fvTIk-U8P",
        "https://drive.google.com/uc?export=view&id=1okhooJvH-85zUE77SlFU5wNQNqoVydzl",
        "https://drive.google.com/uc?export=view&id=1E0R_kJ1zjc3VKxxEfmY53VH_3lZrXOFG",
        "https://drive.google.com/uc?export=view&id=1FVWxV8X-hbPrbk7B5DmsiSdYhdUm9M7U",
        "https://drive.google.com/uc?export=view&id=1MbciBqfSHgktO6LeB5PEuPMYhJJvx5qb",
        "https://drive.google.com/uc?export=view&id=1Mf_J3-DB_6RZs5L3BUDbazglGR_FoNkQ",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1ocMLYApTBFrrr4ZkyfJsehfKG6w4spX8",
        "https://drive.google.com/uc?export=view&id=1oJ-QZdYzp2CYVyhteIduj_bTzUn8NupF",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
        "https://drive.google.com/uc?export=view&id=1HavlRHDaYhTSRr1F9Eacco8fLP2zDtqz",
        "https://drive.google.com/uc?export=view&id=1qV6ac2jjHaRqmk3xiUvSCmc4PbQ4UOyL",
        "https://drive.google.com/uc?export=view&id=1wghRlJLYc9_d0Sa6BCwW7V0dIRzqIqxS",
        "https://drive.google.com/uc?export=view&id=1r01Iqd4XyQkAuVycd4DOWNo1d7wCYYe9",
        "https://drive.google.com/uc?export=view&id=1GqYJbj-Cp9pJT_ALC_iwhTdpfvujsQK-",
        "https://drive.google.com/uc?export=view&id=1dtsPgVfx3Ul1fHEVzqnmxtaeX_Mk5X85",
        "https://drive.google.com/uc?export=view&id=1VuOCBalZ3wYVMTg98r9p0qd-mPKbvT6U",
        "https://drive.google.com/uc?export=view&id=188H2McPgeQ72AJN8yAoXUOIgVdAepciW",
        "https://drive.google.com/uc?export=view&id=13hTfR8X8yu_qIAw7RMhw1EQ-o23gcns6",
        "https://drive.google.com/uc?export=view&id=1m_pXMQUn40DbCt5MA-JkZ8YEB5dWMHLz",
        "https://drive.google.com/uc?export=view&id=1xMY_oMT06VncooHyXjpz_6FLswT4FCuy",
        "https://drive.google.com/uc?export=view&id=1qEOWMuxZJQ2JKYzgCfiSdxQuvHrNf27r",
        "https://drive.google.com/uc?export=view&id=10wEJl3O6tah5Zm2Ht5wO_llDnGOmHB8W",
        "https://drive.google.com/uc?export=view&id=1l9Pw6v2N3nh_FfWHjWqEeE_O0oE4kGUS",
        "https://drive.google.com/uc?export=view&id=1SV1YhjwuQsY9ZVvzFEkqIGinMRUhDvZO",
    ]
    data_list = [
        {"nama": "Kevin Antonio Junior", "jabatan": "Staf Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Gusti Putu Ferazka D.", "jabatan": "Staf Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Ali Aristo Muthahhari Parisi", "jabatan": "Staf Medkraf", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Ayu Andriani Parlina Wati", "jabatan": "Staf Medkraf", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Dafa Elpriza", "jabatan": "Staf Medkraf", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Juwita Sari", "jabatan": "Staf Medkraf", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Afdal Lutfi", "jabatan": "Staf Medkraf", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Salsabila Nazwa Putri", "jabatan": "Staf Medkraf", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Ridwan", "jabatan": "Staf Medkraf", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Andra Ilham Bintang", "jabatan": "Staf Medkraf", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Bryan Paskah Telaumbanua", "jabatan": "Staf Medkraf", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Ghiyats Thabularasa Meardhy", "jabatan": "Staf Medkraf", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Indah Julia Mawar Pratiwi", "jabatan": "Staf Medkraf", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Jacinda Kesya Alvara", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},

    ]
    display_images_with_data(gambar_urls, data_list, key="minbak")
