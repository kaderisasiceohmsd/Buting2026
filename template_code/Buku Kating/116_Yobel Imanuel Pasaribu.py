from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1bqXtM-rTMLvszUEkFpqcxIq0FBJsf9p3",
        "https://drive.google.com/uc?export=view&id=1OFg-hsUhscQ1XPzNMkkab_-HjsuxzLPW",
        "https://drive.google.com/uc?export=view&id=1lBh7UOm5nnCiacs38HPw-hZQoZ84HmA5",
        "https://drive.google.com/uc?export=view&id=1foBWtpEaWvBvqKnJDf3B0XRTd5TMLSNC",
        "https://drive.google.com/uc?export=view&id=1zgdkpfDkJdzK6C6BrdexyCzM7iUhSIeq",
        "https://drive.google.com/uc?export=view&id=1fmy2tQh77tGdd9GUuD2XQzLaIsPDC2XI",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abang kahim kaciww, keren banget bang", "pesan": "Semangat TA nya banggg, semoga lancar dan sukses selaluu"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Bang aqil vibesnya religius banget, lucuu, humoris", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selaluu"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakk efi cantikk nan baik hatii makasii banyak bimbingannyaa kakk, selalu sabar ngajarin adik adik magang yg amatir ini.", "pesan": "Semangat TA nya kakk, semoga lancar dan sukses selaluu"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Bang qois soft spoken bangett, makasii banyak bimbinganyaa bangg", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selaluu"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kak hafsa cantikk nan baik hatii, asik deh sharing session bareng kak hafsa ", "pesan": "Semangat TA nya kakk, semoga lancar dan sukses selaluu"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kak lulu cantikk nan baik hatii, penyabarr, makasii banyakk bimbingan ads nya kakk", "pesan": "Semangat Ta nya kakk, semoga lancar dan sukses selaluu"}
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1o0LwimGHeuFSr3GuxFnvUWGOtgZ5k3oz",
                   "https://drive.google.com/uc?export=view&id=1RqdHYAcKK5bpsnIBUQ-cQjlSXheE01Io",
                   "https://drive.google.com/uc?export=view&id=1osQudtQ-bB-ntAXY4O-cLLla4PMPuXgl",
                   "https://drive.google.com/uc?export=view&id=1roKQ9B1Pt1utpYidZbtPuzxRkhtRHtmt",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1xkSxMsmc26qcL7Uiuh2XIeQaMUIkxvkl",
                   "https://drive.google.com/uc?export=view&id=1VIaENMRrdfjUfZZOa0FouE81JI6e3y6K",
                   "https://drive.google.com/uc?export=view&id=1NiIVf3vCweCyHaw9V3JvND2HlBX5wp5c",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1hlsH2LRcvV5q-bE3kwZtVgxMS8CiomhD",
                   "https://drive.google.com/uc?export=view&id=1iiH8epf6N_MBhLoLZ19927wRzRgrbeau",
                   "https://drive.google.com/uc?export=view&id=1AKx9Q-lkGvwTAfgwups8xmvhcyNv-ykO",
                   "https://drive.google.com/uc?export=view&id=16ABXMvt1jI_W96Leq5hlcQRtG2eHSRJL",
    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik ", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "Bang ridho keren, asik banget", "pesan": "Semangat TA nya bangg, semoga lancar dansukses selalu bangg"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim", "sosmed": "@j__eesie", "kesan": "Kak Juee baik banget, suka kasi kata kata affirmasi buat semangatin adik asuh tpb <3333", "pesan": "Kak Juee semangat TA nya, semoga lancar dan sukses selalu kak <3"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Bang dharu mapress kereennn,, aduhh when yahh", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Gh Mikael Niko Antoni Setiadi", "jabatan": "Staf Komisi I", "nim": "124450025", "umur": "20", "asal": "Lamtim", "alamat": "Jati agung", "hobbi": "Main mcgg", "sosmed": "@me._kael", "kesan": "Santai dan seru, asyik diajak main bareng.", "pesan": "Tetap semangat, dan semoga rank-nya naik terus tanpa lupa kuliah."},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Kak Syarifa baikk, ramah, murah senyumm", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II", "nim": "124450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum kopi", "sosmed": "@givarooo", "kesan": "Bang Givaro keren, seruuu, baik", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "Kak nisa baikk, ramah, murah senyum", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "city earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain_", "kesan": "Kak Hani baikk, ramah, sama sama coer dengan bias yg sama^^", "pesan": "Kak Hani semangat kuliahnya, semoga lancar dan sukses selalu kakk"},
        {"nama": "Jeremia Halim", "jabatan": "Staf Komisi II", "nim": "124450101", "umur": "20", "asal": "Tangerang", "alamat": "Teluk Betung", "hobbi": "Nyanyi, olahraga", "sosmed": "@jeremia_hm", "kesan": "Ramah dan seru, enak diajak ngobrol.", "pesan": "Tetap semangat, dan semoga suaranya makin merdu serta badannya selalu sehat."},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III", "nim": "123450073", "umur": "21", "asal": "Sumut", "alamat": "Kota baru", "hobbi": "Merajut", "sosmed": "@monica_tjg", "kesan": "Sabar dan telaten, orangnya menyenangkan.", "pesan": "Tetap semangat dan semoga rajutannya makin bagus."},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "gym / koleksi figur", "sosmed": "@nagatsee", "kesan": "Bang Jona keren, asikk, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "Kak Sekar baikk, ternyata setelah kenal asikk, ramah, murah senyum", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nahaysh", "kesan": "Kak wan baikk, ramah, murah senyum", "pesan": "Semangat TA nya kakk, semoga lancar dan sukses selalu kakk"}
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1hn-Ky0zPUqblDniW0Y6E6xSCHEXBm7se",
        "https://drive.google.com/uc?export=view&id=1T1UBnQciFWOss5ME-Nvaqh2lxe7cPjc1",
        "https://drive.google.com/uc?export=view&id=1PJzx5OsOKAFkdt61DNgyx_0q9Y1ALgkw",
        "https://drive.google.com/uc?export=view&id=1FHq0jJZtMLkGctgtNahEVsHoPKn1U58o",
        "https://drive.google.com/uc?export=view&id=1HUI9a-zUFCkZoHJ1QXo3uGEvSAeGs5oY",
        "https://drive.google.com/uc?export=view&id=1-hPhfyPTwdwbJgM01qti0bxOHlapC7xB",
        "https://drive.google.com/uc?export=view&id=1-JZkq53ZsVjGpXKOWzhmS4qBvhHHI8y0",
        "https://drive.google.com/uc?export=view&id=1FhWChvx0s1WcEQvvLFTtwu5rp0Lpj5a1",
        "https://drive.google.com/uc?export=view&id=1f7g5Ddh7jL2l5yJEaACG09G8p3aMvH0e",
        "https://drive.google.com/uc?export=view&id=1RJ8uqQZScWoUZbuGxCRcCklj6kCui-5C",
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Kakak vibesnya wardah bangett kakk, kerennn, kritiss", "pesan": "kakak semangat TA nya kakk, semoga "},
        {"nama": "Helmy Surya Pratama", "jabatan": "Kepala Biro Aspirasi dan Media Komunikasi ", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya humoriss", "pesan": "Terus berkarya!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Suci Aulia", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Biro Kajian Strategis dan Propaganda", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Kepala Biro Kesekretariatan", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Staff Biro Kesekretariatan", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="senator")

elif menu == "Departemen PSDA":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1-21j54ADWi9A3LHCRkGh8x2yeCNPMZrt",
                  "https://drive.google.com/uc?export=view&id=18do8qbuf71vyD7oiQO6gvruYERza1wGf",
                  "https://drive.google.com/uc?export=view&id=1zcsRbgKWYoy1xxI_83tXdyj4jluzR46o",
                  "https://drive.google.com/uc?export=view&id=17_sVPmK8anaDrlinuXlp754MKoyx--J8",
                  "https://drive.google.com/uc?export=view&id=1nJHgim3LySSeSnBe2SHqVDS-Yq7GRF5M",
                  "https://drive.google.com/uc?export=view&id=1yryPxB39Jmh_xP9XBlfqFSPooX6Vv8P-",
                  "https://drive.google.com/uc?export=view&id=1CYgY8ViKYJ2k3VVG8mFYMAALadj5no52",
                  "https://drive.google.com/uc?export=view&id=1fKLGBxRLjf8YYvx_FyFK0czw9lsrFEm3",
                  "https://drive.google.com/uc?export=view&id=1TZJcSql29quxEZNjCENDNgxU8UQhDXQE",
                  "https://drive.google.com/uc?export=view&id=1U5q3TP-83dF3Peri66lPiwM44ibX8avK",
                  "https://drive.google.com/uc?export=view&id=1aMjTx_idpgQc6yC7DZc9xOzjbDNGJUco",
                  "https://drive.google.com/uc?export=view&id=1nRaxb6adKVKinQ75mExK6vyICrbeSgq6",
                  "https://drive.google.com/uc?export=view&id=1N6lgdHFRnKa-dmZ1UPNuaLmsH0fAiE5G",
                  "https://drive.google.com/uc?export=view&id=1cih81UoJWI73QT_OAdBkUdVOC9GjaKGZ",
                  "https://drive.google.com/uc?export=view&id=1Ou1lGn_85Qr1hHKy5I3cRVth87zX_S6h",
                  "https://drive.google.com/uc?export=view&id=1R7f4Vt9oTUJqVDpPAVF1iaP23kLAnqSb",
                  "https://drive.google.com/uc?export=view&id=1m3TvCEomhwvlq1vL3sLwvsbsdpfhAQNr",
    ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "123450097", "umur": "21", "asal": "Kalianda", "alamat": "Samping kost Haikal", "hobbi": "Naksir cowo cakep", "sosmed": "@arientakhsnl_", "kesan": "Ramah dan mudah akrab dengan siapa saja.", "pesan": "Tetap semangat kuliahnya dan jaga kesehatan ya."},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "123450022", "umur": "20", "asal": "Palembang", "alamat": "Pudan Kost", "hobbi": "Pacaran", "sosmed": "@vany.salsabilaa", "kesan": "Kak vany baikkk, walaupun keliatan judes", "pesan": "Semangat terus ya kak, lancar terus kuliahnya."},
        {"nama": "Nobel Nizam Fathirizki", "jabatan": "Kepala Divisi Kaderisasi", "nim": "123450117", "umur": "21", "asal": "Bandar Lampung", "alamat": "Urip", "hobbi": "Sulap", "sosmed": "@nobelnizam", "kesan": "Kalem dan sopan, nyaman diajak ngobrol.", "pesan": "Terus semangat dan tetap konsisten dalam belajar."},
        {"nama": "Afriza Azmi", "jabatan": "Staf Kaderisasi", "nim": "124450110", "umur": "20", "asal": "Lamteng", "alamat": "Sebelah kost Haikal", "hobbi": "Nyebar beras", "sosmed": "@friezazmi", "kesan": "Santai dan menyenangkan.", "pesan": "Tetap jadi diri sendiri dan semangat terus."},
        {"nama": "Ayake Alfatih Ramadan", "jabatan": "Staf Kaderisasi", "nim": "124450108", "umur": "20", "asal": "Solo", "alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung", "hobbi": "Goreng ayam", "sosmed": "@ykeall", "kesan": "Supel dan gampang bergaul.", "pesan": "Semangat terus kuliahnya, semoga lancar ke depannya."},
        {"nama": "Caesar Ozora Alrando", "jabatan": "Staf Kaderisasi", "nim": "124450017", "umur": "21", "asal": "Rahim ibu", "alamat": "Gedung F", "hobbi": "Pengembala anak ayam", "sosmed": "@caesar.oriza", "kesan": "Orangnya santai dan asyik diajak ngobrol.", "pesan": "Tetap semangat dan jangan lupa istirahat yang cukup."},
        {"nama": "Euodia Meiliana Friedita", "jabatan": "Staf Kaderisasi", "nim": "124450029", "umur": "20", "asal": "Asal asalan", "alamat": "Diatas tanjakan", "hobbi": "Ngekader", "sosmed": "@yudiameilianaa_", "kesan": "Aktif dan punya semangat yang tinggi.", "pesan": "Terus berkembang dan semoga selalu sukses."},
        {"nama": "Haikal Seventino Tamba", "jabatan": "Staf Kaderisasi", "nim": "124450012", "umur": "25", "asal": "Jambi", "alamat": "Sebelah kontrakan Jemar", "hobbi": "Ngurusin pakan anak ayam", "sosmed": "@_haikaaalll", "kesan": "Dewasa dan bisa diandalkan.", "pesan": "Tetap semangat dan jaga kesehatan."},
        {"nama": "Putri Manna Anantama Simbolon", "jabatan": "Staf Kaderisasi", "nim": "124450065", "umur": "18", "asal": "Depok", "alamat": "Nomandenl", "hobbi": "Mancing emosi", "sosmed": "@putrimannaa", "kesan": "Ceria dan seru diajak bercanda.", "pesan": "Semangat terus belajarnya dan tetap jadi pribadi yang positif."},
        {"nama": "Queenta Thifaal Nabila", "jabatan": "Staf Kaderisasi", "nim": "124450059", "umur": "21", "asal": "Lamteng", "alamat": "Depan pemancingan", "hobbi": "Nyuapin anak ayam", "sosmed": "@queentanaabila", "kesan": "Ramah dan hangat ke semua orang.", "pesan": "Tetap semangat dan semoga semua rencananya berjalan baik."},
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi PMA", "nim": "123450114", "umur": "18", "asal": "Palembang Sekayu", "alamat": "Asrama TB 3", "hobbi": "Ngejek orang", "sosmed": "@dsmanhl", "kesan": "Orangnya humoris dan bikin suasana cair.", "pesan": "Terus semangat dan tetap rendah hati."},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf PMA", "nim": "124450041", "umur": "19", "asal": "Teluk", "alamat": "Bandar Lampung", "hobbi": "Pilates", "sosmed": "@azzelytn", "kesan": "Disiplin dan menjaga pola hidup sehat.", "pesan": "Pertahankan semangatnya dan tetap konsisten."},
        {"nama": "Charrlindah", "jabatan": "Staf PMA", "nim": "124450037", "umur": "21", "asal": "Jakarta Pusat", "alamat": "Cenderawasih 1", "hobbi": "Ngurus peternakan", "sosmed": "@charrlnn", "kesan": "Pekerja keras dan bertanggung jawab.", "pesan": "Semangat terus dan jangan lupa luangkan waktu untuk diri sendiri."},
        {"nama": "Jeremi Marolop Partogi Situmorang", "jabatan": "Staf PMA", "nim": "124450111", "umur": "16", "asal": "Berlin", "alamat": "Samping kos Rafli", "hobbi": "Mengembala anak ayam", "sosmed": "@jemarrro", "kesan": "Santai dan mudah bergaul.", "pesan": "Tetap semangat dan terus belajar hal baru."},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf PMA", "nim": "124450048", "umur": "18", "asal": "Lampung", "alamat": "Barokah", "hobbi": "Main sama Azel", "sosmed": "@n.bila_a", "kesan": "Ramah dan menyenangkan diajak berteman.", "pesan": "Semoga kuliahnya lancar dan selalu diberi kesehatan."},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf PMA", "nim": "124450007", "umur": "20", "asal": "Sibolga", "alamat": "Samping kos Haikal", "hobbi": "Nonton", "sosmed": "@dearfkvmfl", "kesan": "Kalem dan enak diajak ngobrol.", "pesan": "Tetap semangat dan terus jadi pribadi yang baik."},
        {"nama": "Salavi Naharani", "jabatan": "Staf PMA", "nim": "124450090", "umur": "20", "asal": "Lampung Timur", "alamat": "Jatimulyo", "hobbi": "Minum air putih", "sosmed": "@avi.nhr", "kesan": "Tenang dan apa adanya.", "pesan": "Semangat terus dan tetap jaga kesehatan."}
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1b_yPOKqvmAAy-RYzp7A9mrDH5ym2UC44",
                   "https://drive.google.com/uc?export=view&id=1lWJqZWa25zn58h5ioia7xk_w8ozh46aj",
                   "https://drive.google.com/uc?export=view&id=1gXF8gheFyM0XydmQQQKbzvNp2r4NNXSS",
                   "https://drive.google.com/uc?export=view&id=1qppkDG49KHOcqHpTN8_7Kd5f66aVdFu_",
                   "https://drive.google.com/uc?export=view&id=11wBDS5HmwtkavxFVnQDZAGUkMWeLeAqp",
                   "https://drive.google.com/uc?export=view&id=1q4xreNcM3IOuE7FVOzn9-4zZfNmj8wQU",
                   "https://drive.google.com/uc?export=view&id=1LxiOwks8s07jOoL-7MhsSFQaUDTYbIUa",
                   "https://drive.google.com/uc?export=view&id=1xAfNq27dZKma8-cR90FXZL1lWLS5lmFh",
                   "https://drive.google.com/uc?export=view&id=1xy1rDH7fe4Jb1AkG6FqAdfelNwruIp34",
                   "https://drive.google.com/uc?export=view&id=1Rz3kwYrBk1oWqAbMn0U5z1tq5A51hiOK",
                   "https://drive.google.com/uc?export=view&id=1haPjkxeNSYCP7dOgV0JfvwsGipVIZV5r",
                   "https://drive.google.com/uc?export=view&id=1ynb8L9AAI5V3rzcqN2CQ9oh2K-wsbCAj",
                   "https://drive.google.com/uc?export=view&id=18oyzFGj0BW7aP0aYjNiKO-Q2yFx2k4L9",
                   "https://drive.google.com/uc?export=view&id=1HZWn3HNEk9Q-BV861B_x3QqKH7Q9Rjrn",
                   "https://drive.google.com/uc?export=view&id=14o_6hfHjPqzr4agxBMjt3wVj8IlD1Fnv",
                   "https://drive.google.com/uc?export=view&id=1xb70utJ8nVu4yP-tJJjCX6ViTxBACTCv",
                   "https://drive.google.com/uc?export=view&id=1Vu6ljqPWoqElGBwXJnVri0mRTJzZwNqi",
                   "https://drive.google.com/uc?export=view&id=1gw-RVyOUBrZOMBGlTpIQqb_5LiZ-Y6g6",
                   "https://drive.google.com/uc?export=view&id=1Rs1PwnO8MV8UchD6Sg5B_BFlF9sBxkgB",
                   "https://drive.google.com/uc?export=view&id=1KcaC0Ji6uSXORInY4wzgeqwuJ4fs9oZg",
                   "https://drive.google.com/uc?export=view&id=1d5VApEh68Yb6uEMHJ5FPjfj4EPs8ZgH0",
                   "https://drive.google.com/uc?export=view&id=1LacqEuRNaD60WxbuxP5kFPw9JjGDPHHy",
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
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1EVldkaIupq6Njvj_JOXemWuzdh4kWM2_",
        "https://drive.google.com/uc?export=view&id=1QzpzIxzCGdQihYftkrJGEb4rTASosdj8",
        "https://drive.google.com/uc?export=view&id=1aRQ1gQwKSI2S0ZqMFVqcTvhV0HaNZPy6",
        "https://drive.google.com/uc?export=view&id=1sKTiYv2ysBcpdgL8mU5AxbfL0aka448R",
        "https://drive.google.com/uc?export=view&id=1aRZJz-LTBsN-jB0nSDjzmnRTaPawQg5i",
        "https://drive.google.com/uc?export=view&id=15ZdArAGWhpXWN252qouVeblLzqjlS-Mu",
        "https://drive.google.com/uc?export=view&id=1IeyTso2rU5S0SiPA4bcAyc7VtmB5ucU8",
        "https://drive.google.com/uc?export=view&id=1tSOqo30f0LzQ4E9qVgdl0RlduLV0aDSO",
        "https://drive.google.com/uc?export=view&id=1ubhrB0TrtN0nyZhlMT9LJAXBnkzDOpzw",
        "https://drive.google.com/uc?export=view&id=1Pt3-n-CThgPm9kLuGoc5VAbn8jnvXykt",
        "https://drive.google.com/uc?export=view&id=1y50CXbnkPi6XbIalbgIFXjr7bra6w08Z",
        "https://drive.google.com/uc?export=view&id=1KvPaHLwU6TVdnzrWHWKaJ4bKhlxX9WoY",
        "https://drive.google.com/uc?export=view&id=1Bq9ArlK4gVC6kbqftC1-9OSB4La_k1lW",
        "https://drive.google.com/uc?export=view&id=1xTm4zFz7s3HK_cY5U252TqgNSDiygyVe",
        "https://drive.google.com/uc?export=view&id=1JyItxfHevYalXOtT--y3vT7RHF5pkC6V",
        "https://drive.google.com/uc?export=view&id=1ggxb3GmYcX4ODxwyI2HL9tsEEfbHRyoj",
        "https://drive.google.com/uc?export=view&id=1n2Jub9JxVdLVAgRWULOAjj8KTuuMksDj",
        "https://drive.google.com/uc?export=view&id=1ybfPhcvfEIp4sWoWi9Z4EOxlwKTOLSd2",
        "https://drive.google.com/uc?export=view&id=161mSPfo4cNnOTfMYyWGPxnd3draXDJOc",
        "https://drive.google.com/uc?export=view&id=1urajHbpiCUObVPWeuoG1AJj3znNa3r0J",
        "https://drive.google.com/uc?export=view&id=1B26KhqqwtOJcOR5MG-LssHmZPjzYp_Wb",
        "https://drive.google.com/uc?export=view&id=1-VInirVZHkc1Z9_JYJpizOTkhtErOaOb",
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
    gambar_urls = ["https://drive.google.com/uc?export=view&id=158slOazSLVnd9XEE3xnqOXs5QqZ1MO17",
                   "https://drive.google.com/uc?export=view&id=1N6eGVTvI0TcS8WCzAoR1Q572oU3kBmTy",
                   "https://drive.google.com/uc?export=view&id=1ddNQzPeowhEcAwnhlZwdYf2NbuLtxOCZ",
                   "https://drive.google.com/uc?export=view&id=1mORa3dJS_Us7epaYYcmdYlbmox_Mlz7j",
                   "https://drive.google.com/uc?export=view&id=1lqRCBTra8LLdNtf1ljWLD8AaNCNBkmVc",
                   "https://drive.google.com/uc?export=view&id=1VJT0OhTwHCInkd-KQAI-i9zlMhFnixd3",
                   "https://drive.google.com/uc?export=view&id=1eEsD4Dxn8VJQWG6hNCeXzHQVGlq8qa4T",
                   "https://drive.google.com/uc?export=view&id=1uMOwYfffPDy7anMVWb7WmYk23rmAv3QE",
                   "https://drive.google.com/uc?export=view&id=1HDuYg_j6rP62KiqUal2L4k_dSsgvBtEZ",
                   "https://drive.google.com/uc?export=view&id=10nAn0oXL3649xr9BiYssrpg9Pfz7MspV",
                   "https://drive.google.com/uc?export=view&id=1etE1uJXuWC5uT_-9NubwfgBYmZrMz9ai",
                   "https://drive.google.com/uc?export=view&id=1-jXMsQy_DEMvr296h_s9LRNEncK-S2Mm",
                   "https://drive.google.com/uc?export=view&id=1F9PVg-wo-O0MQ0i-0ZhF3C6soMIxCGRi",
                   "https://drive.google.com/uc?export=view&id=1XcbcRocVErx1EXE79GIHVHsPwFWX8z7u",
                   "https://drive.google.com/uc?export=view&id=1L1Z-s6S8VPMFGku5HwB5yxcxkaN1HNKG",
                   "https://drive.google.com/uc?export=view&id=1k6hB_wKw4C9t-HU7eW4Qy-O6WsLMoS-v",
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
        {"nama": "Rafa Sabina Fahimah", "jabatan": "Staf Kerohanian", "nim": "124450036", "umur": "20", "asal": "Natar", "alamat": "Natar", "hobbi": "Nonton Drakor", "sosmed": "@snasaa._", "kesan": "Ramah ke semua orang.", "pesan": "Pertahankan sikap rendah hati itu."}
    ]

    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1h_wt0wWbktdt_WlN4GbTfRif6oSqrKm6",
        "https://drive.google.com/uc?export=view&id=1-brd6HwBe7sgRzQcq4frtiTggK_CoXHb",
        "https://drive.google.com/uc?export=view&id=1wZEH9birpHNA6KWDaMJSiyZOVPeUMLN6",
        "https://drive.google.com/uc?export=view&id=1A1a3wb_bqn7nb0W0bGIOxwYt7n8k7kX3",
        "https://drive.google.com/uc?export=view&id=1pIFqtn_Cf3vqoLZA9wL5ggXqvpsd7zj0",
        "https://drive.google.com/uc?export=view&id=1PGniSg9uXUxuiFHklW2j4hVipmr8WSM-",
        "https://drive.google.com/uc?export=view&id=1tDypjE0Gl-2EgeuGW_WNpoIBVsg45ydP",
        "https://drive.google.com/uc?export=view&id=14HSLUcDZoAGVjEkWZJH67rDSGVrQFO1Y",
        "https://drive.google.com/uc?export=view&id=1TLor2cxMWsnNmLGU8OPFqdO0Ty0xA16u",
        "https://drive.google.com/uc?export=view&id=1qa1IuxTU7OkyVjLdbHfpieXbZUIEtIJp",
        "https://drive.google.com/uc?export=view&id=1BQSjcy9mVZgqJgHNr3cOet9jdsqR6taH",
        "https://drive.google.com/uc?export=view&id=1tq9kOwNy117xzgvauMsYD21A87d_XnfK",
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
        {"nama": "Della Anisa Fitri", "jabatan": "Staf Kewirausahaan", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1TH3en8vPgJLBZIA4OThtjc1YTXtu-etS",
        "https://drive.google.com/uc?export=view&id=1RawrK7B9uIooZ3HJu1YHTJBNPM8si51Q",
        "https://drive.google.com/uc?export=view&id=1W-WXC7hrHbu-4x4DNKcBKE7CP16cdvkS",
        "https://drive.google.com/uc?export=view&id=1n5spXZgLTRYTBpb2c6GwvcCI5O63Hgmr",
        "https://drive.google.com/uc?export=view&id=1XFubSQFxKFHL3vxK7AVmH4SCZ-x6NRF2",
        "https://drive.google.com/uc?export=view&id=1zUCE3tCkNajwWb6ILL-lz10rnffI9yNV",
        "https://drive.google.com/uc?export=view&id=1_NLwZPAYvc-UMOH2iC3NqINJy58yBVmE",
        "https://drive.google.com/uc?export=view&id=1bXF9aOlpKKMz3l-_dHEOFqt0N7PvGGNI",
        "https://drive.google.com/uc?export=view&id=174yA3PPM-0Luedj1g9XZK55gkdMwGOK3",
        "https://drive.google.com/uc?export=view&id=14gA3DroUtUUItxnqUKZK4apLVYAzeoSn",
        "https://drive.google.com/uc?export=view&id=1u4LiknrbETnnqwz0yzUBePwhvMISgPQw",
        "https://drive.google.com/uc?export=view&id=1OxygdmJdR7VfFQO7zrg3we-9qX7AEin1",
        "https://drive.google.com/uc?export=view&id=1w3e3Vg-7gUHkjOsdZTIKVIFdpgchMTdH",
        "https://drive.google.com/uc?export=view&id=1PtkS5003c3_3tMLuIJnvHpRFXgMCC0U_",
        "https://drive.google.com/uc?export=view&id=1OQcSTTTyTmj2csiFx4MbEJR5giQGu6Zm",
        "https://drive.google.com/uc?export=view&id=1AJ1w8pXRDohaI6qojEFqjbC3xD-tnjn_",
        "https://drive.google.com/uc?export=view&id=10V1YWSdm83ivyxtsjgjsUZsgo6GYISi9",
        "https://drive.google.com/uc?export=view&id=1LuBal5_0QklZhEif7nqv08mNhKIlqEXM",
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
        {"nama": "Zannuba Arifah Ilman", "jabatan": "Staf Visual Design", "nim": "124450112", "umur": "18", "asal": "Lampung Timur", "alamat": "Rajabasa", "hobbi": "Begong", "sosmed": "@xifasky", "kesan": "Sopan dan selalu menghargai orang lain.", "pesan": "Semoga selalu dimudahkan dalam setiap urusan, Kak."}
    ]
    display_images_with_data(gambar_urls, data_list, key="medkraf")


elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1fPtsYqF_0DOMxPylUfP8tHJb-4I8bclk",
        "https://drive.google.com/uc?export=view&id=1PllMuoTERH-2sD8P20iTxbJxTQm7x10d",
        "https://drive.google.com/uc?export=view&id=16YgKZ9rrGnISfnT1z5GmABdQaBPRiM0j",
        "https://drive.google.com/uc?export=view&id=1A7DCCFoX0uVRapmTROWRJ7RKB3jvSB5w",
        "https://drive.google.com/uc?export=view&id=1LmPX6jybPVwqYMwN7Avk5WeaL4O7hRLH",
        "https://drive.google.com/uc?export=view&id=1DRDiySSqt5X-ZTr2qRMKTtpvc_gyh-Hw",
        "https://drive.google.com/uc?export=view&id=1zRNtU-cFIBjdM3K9A2BYML4fnfrpz5wj",
        "https://drive.google.com/uc?export=view&id=1ZMRNL1nH5UZQdeBXAaWLojALMxH_O1si",
        "https://drive.google.com/uc?export=view&id=1KMfgOUiumRjtO2bw-cJP7BgVdfI7JViQ",
        "https://drive.google.com/uc?export=view&id=1bILja-L8BwfQZRCTOyZbWzqZlC5aMLwc",
        "https://drive.google.com/uc?export=view&id=1XPh0CoqrMMwXfQnxlc1msV5PBONGCtpF",
        "https://drive.google.com/uc?export=view&id=1TAlpvwm8csUxnCKtw2TaogQRU13gqtCH",
        "https://drive.google.com/uc?export=view&id=13JR2pVHtTboy_JtJVMGtH7wXwyP8yDS6",
        "https://drive.google.com/uc?export=view&id=1e6c6Af3c-k7-iNB5RIu4qqSynwm202Mt",
        "https://drive.google.com/uc?export=view&id=1bTmGuC1vxZQha4RbUIqJKMDURkuQnEBV",
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
