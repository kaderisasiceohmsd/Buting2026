from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=12cWhixrwVc5uEATnocwRJHw5nhRFxCHv",
        "https://drive.google.com/uc?export=view&id=1sv9FBDEIaKNUNrIBN4OJTc6Ovk85jgVP",
        "https://drive.google.com/uc?export=view&id=1uLNAVgSX8A7F_n7IMQBu6KknNouVoF8d",
        "https://drive.google.com/uc?export=view&id=18Bm8mmUYqE7daRUSPf4xEB5JWTY8YEyt",
        "https://drive.google.com/uc?export=view&id=1mMMKw-5pKfFuazXUGLYs2r46INZzCyco",
        "https://drive.google.com/uc?export=view&id=1D6lgpdAEXhaT7OnZ_yv4a606zIIY0NI5",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, asik saat interaksi dan sefrekuensi.", "pesan": "Semangat dan semoga IMO bang!!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya asik dan suka bercanda serta interaktif", "pesan": "Sukses selalu dan sehat selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya baik dan lembut", "pesan": "Sukses selalu kak dan perbanyak senyum!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya pintar dan beaura", "pesan": "Sukses selalu dan semangat bang!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, lucu, dan suka duit", "pesan": "Sukses selalu dan semangat kakk!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, suka dinamikanya sama bang aqil", "pesan": "Sukses selalu dan semangat kakkk!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1HKsNmHfGze7dIj7T48qIRyfOtRWXhIaZ",
                   "https://drive.google.com/uc?export=view&id=1ixPG42J7k632zIwYADoO36NcNEMtY7il",
                   "https://drive.google.com/uc?export=view&id=1IBv3QdnuBtGSv7j9_A9iGMt_cPRcK3KD",
                   "https://drive.google.com/uc?export=view&id=1XqIZomFZJxrFf6WmhCyDKXW5OJtjtfjw",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1lWnX4wENmGrdKNF3t2xUJnSVk1slRArO",
                   "https://drive.google.com/uc?export=view&id=1L1l1zpB1ojTzgGm_n2y338jTnk7A7b06",
                   "https://drive.google.com/uc?export=view&id=1aIwFMlSNlh58verZVqV-4-yU-q4MUlMT",
                   "https://drive.google.com/uc?export=view&id=1hvzTrF73R4pwPxhFR6DGPU5vKo3lVqNz",
                   "https://drive.google.com/uc?export=view&id=1WUhzhJTMKvZ3aMGL6d59B0VGVlN3a5Pn",
                   "https://drive.google.com/uc?export=view&id=1aGe6QzbSDP6tcnjcRs6TMrV_4peG5ETf",
                   "https://drive.google.com/uc?export=view&id=1P8MaxGiJ4kwet55oHITTkFwOJ6fU1uYx",
                   "https://drive.google.com/uc?export=view&id=1VhQe5WxjiT05EKrnBTVFJtOoeiE7LEV6",
    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik ", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "Bang ridho aura nya komedi tapi bisa serius, my idol", "pesan": "Semangat TA nya bang, semoga cepat IMO"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim", "sosmed": "@j__eesie", "kesan": "Kak Jue baik, jail, sama slow respon hehe", "pesan": "Kak Juee semangat TA nya, semoga lancar dan sukses selalu, sama fast respond <3"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Bang dharu mapres keren, fashionable", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Gh Mikael Niko Anthoni Setiadi", "jabatan": "Staff Komisi I", "nim": "124450022", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@me._kael", "kesan": "bang niko asikk, lucu, dan detail saat menjelaskan", "pesan": "Semangat kuliahnya bangg, makin keren"},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Kak Syarifa baik dan ramah", "pesan": "Semangat kuliahnya kakk, semoga sehat dan sukses selalu kakk"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II", "nim": "124450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum kopi", "sosmed": "@givarooo", "kesan": "Bang Givaro keren, kritis, kachoww", "pesan": "Semangat TA nya bangg, semoga dilancarkan dan sehat selalu"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "Kak nisa baikk, beauty with brain, cantikk", "pesan": "Semangat kuliahnya kakk, perbanyak senyumm"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "city earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain_", "kesan": "Kak Hani baikk, ramah, sama sama coer martin > keonho", "pesan": "Kak Hani semangat kuliahnya, semoga lancar dan sehat selalu kakk"},
        {"nama": "Jeremia Halim", "jabatan": "Staff Komisi II", "nim": "124450101", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@jeremia_hm", "kesan": "Bang Jeremia keren, panutann", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sehat selalu bangg"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@monica_tjg", "kesan": "kakaknya pintar dan pendengar yang baik, jail", "pesan": "semoga kuliahnya lancar dan sehat selalu"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "gym / koleksi figur", "sosmed": "@nagatsee", "kesan": "Bang Jona keren, asikk, chill guy, jail", "pesan": "Semangat kuliah nya bangg, semoga koleksi action figurenya lengkap"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "Kak Sekar baikk, ternyata setelah kenal asikk, ramah, murah senyum", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nahaysh", "kesan": "Kak wan baikk, ramah, murah senyum", "pesan": "Semangat TA nya kakk, semoga lancar dan sukses selalu kakk"},
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1hPcj_YllCfMYzTLQhkN4bXO2qe-Rc4Rz",
        "https://drive.google.com/uc?export=view&id=1HABxHUNRQFtuxVkO4cLuxQCSOzSWtjXL",
        "https://drive.google.com/uc?export=view&id=10bcB3fYazfhpa1mGYTJqV7BlbhIsakWS",
        "https://drive.google.com/uc?export=view&id=1TdkaU4mCH3yWhhh7bncOwz5qFlJ-PE4f",
        "https://drive.google.com/uc?export=view&id=1JpYMX2nyOZf9SZ9kEVsYOWDBaIAeDyX6",
        "https://drive.google.com/uc?export=view&id=1mMvmNoSVq0TFxxy0Kl2E0Tar0DvUa4SC",
        "https://drive.google.com/uc?export=view&id=13UB5SEJ4lL-fcZ0_7EpTOCbueAN4YW1v",
        "https://drive.google.com/uc?export=view&id=1ALNb5xUYkND2oKReqOJJOoebu1i9G1Rb",
        "https://drive.google.com/uc?export=view&id=1r51B2mv1ylvCCTPLlKDRRDsdFSAqabcD",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Senator Mahasiswa", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="senator")

elif menu == "Departemen PSDA":
    gambar_urls = [
                  "https://drive.google.com/uc?export=view&id=1cGX3eDB71U4iLOCKYpXuwT-qC0G3zP4I",
                  "https://drive.google.com/uc?export=view&id=1Vu1gtjmT8SrmM001PCLdjhfoGmZemViJ",
                  "https://drive.google.com/uc?export=view&id=1ovBzIURl16CoroaVHmbHiuajcqKf0e8K",
                  "https://drive.google.com/uc?export=view&id=1LFhdxO9rjdZwi7PbfRgIheKdVjqRpnqI",
                  "https://drive.google.com/uc?export=view&id=1x7mD_o38wQ7vEGsWqyvXZAmFQ1QsqdiW",
                  "https://drive.google.com/uc?export=view&id=1ApNi4UvHxzBGczXiW5DomoCyWtuYMgxT",
                  "https://drive.google.com/uc?export=view&id=1jA4itM1L7M-rkr1NykK9XLiemvxNe0nP",
                  "https://drive.google.com/uc?export=view&id=1ymBd-hl_T7t0wCIxZOUP6br-4fgxhP9D",
                  "https://drive.google.com/uc?export=view&id=1VoyIGs1T9R1bOpP9ZlpaQB5E_29Zzu-9",
                  "https://drive.google.com/uc?export=view&id=1nfWU3toEZhh_TXRqNabbQsaocn9jjDUv",
                  "https://drive.google.com/uc?export=view&id=1ji4YqMmcLJoxJQqfO2tiIrmIbfvDScej",
                  "https://drive.google.com/uc?export=view&id=1cPXJDmNEvfE81Y5XF0hrHTzajTE73CDf",
                  "https://drive.google.com/uc?export=view&id=1Rpsy-28X8q2ztDRAiwkppvi3Spj7TlRm",
                  "https://drive.google.com/uc?export=view&id=14MpPTC0OGshW7Bheqd4W59C5TbFjsgZY",
                  "https://drive.google.com/uc?export=view&id=1cCkCWGNcqL5k-0sBIhBqX-06LTgSJ6CJ",
                  "https://drive.google.com/uc?export=view&id=1LFzuOb3T-I0d_op9bUx_BbLP8s6PgKR2",
                  "https://drive.google.com/uc?export=view&id=16adcHj9xr4lkZH0cIQrBHqnh6Vr5k14l",
    ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "123450097", "umur": "21", "asal": "Kalianda", "alamat": "Samping kost Haikal", "hobbi": "Naksir cowo cakep", "sosmed": "@arientakhsnl_", "kesan": "Ramah dan mudah akrab sama perhatian.", "pesan": "Tetap semangat kuliahnya dan jaga kesehatan kak."},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "123450022", "umur": "20", "asal": "Palembang", "alamat": "Pudan Kost", "hobbi": "Pacaran", "sosmed": "@vany.salsabilaa", "kesan": "Kak vany ramah banget ternyata, walaupun keliatan judes", "pesan": "Semangat terus ya kak, lancar terus kuliahnya."},
        {"nama": "Nobel Nizam Fathirizki", "jabatan": "Kepala Divisi Kaderisasi", "nim": "123450117", "umur": "21", "asal": "Bandar Lampung", "alamat": "Urip", "hobbi": "Sulap", "sosmed": "@nobelnizam", "kesan": "abangnya tegas dan punya aura pemimpin, peduli dan jago komputasi.", "pesan": "semangat terus bang, stay hard stay humble."},
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
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1ps0ozgETucwKCgAgBTQNDtDFx5YUme44",
                   "https://drive.google.com/uc?export=view&id=18081aFXmtKNqwz29uVA02GRIrx0qy-rZ",
                   "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                   "https://drive.google.com/uc?export=view&id=1Xtdt9ehyg0K8zQr4X-viWodJ1ZI98XiV",
                   "https://drive.google.com/uc?export=view&id=1pYtZvPXJJRomtM9atfmObngkOOlYGwye",
                   "https://drive.google.com/uc?export=view&id=1CEdigOXGT-32HMDcQEpDlqqshj_Gbgly",
                   "https://drive.google.com/uc?export=view&id=1nJV6LHzVK0dKbFnK98zlSPzya93KnN-M",
                   "https://drive.google.com/uc?export=view&id=1G7w_Na_JO_fQTZRV1Iv8a4eN-KS3miDR",
                   "https://drive.google.com/uc?export=view&id=1x0z4zGYaS8CK_KG6wPtlvfkFVLd-mbak",
                   "https://drive.google.com/uc?export=view&id=16cK8In5kzaSbNImmkFrGNFvPRiiSkvl0",
                   "https://drive.google.com/uc?export=view&id=16c1AmflL2qlSpYkRgH8pGiUK_dBlG3JI",
                   "https://drive.google.com/uc?export=view&id=1qZsF9BKlxXmqu5lH1BZQ9LUQ2Mrgxx-O",
                   "https://drive.google.com/uc?export=view&id=1ZFh9AawKevhggTuupjGM38r62ZzObEZV",
                   "https://drive.google.com/uc?export=view&id=1rZTIP8OeqBF-f19bMxi1g4AOPxgSgVJg",
                   "https://drive.google.com/uc?export=view&id=1fj7X-QzQa4oVHySYoj6-gzAmJQnUzV7O",
                   "https://drive.google.com/uc?export=view&id=1RsjOwoeb-krYU4s67EgYkzKkkeEFNQX0",
                   "https://drive.google.com/uc?export=view&id=1D_NPpOx77rAuTCHl9dg4IMWk15waLL4a",
                   "https://drive.google.com/uc?export=view&id=1wVn5MINc8WyQGTwpjmBj97jOzSnfM7fY",
                   "https://drive.google.com/uc?export=view&id=1QsQ5pvqN6Yg4m9x5o-lCPpLWiy-V95FO",
                   "https://drive.google.com/uc?export=view&id=1G_eIVycTv4zi8llz1Waeb2QdEnsEks-h",
                   "https://drive.google.com/uc?export=view&id=1jGPsyVkKYXCR_3afwUBb5nUME6deGSK1",
                   "https://drive.google.com/uc?export=view&id=1FXxRmSe61aP8unDkCzZ_9b3GIZC9sZGw",
    ]
    data_list = [
        {"nama": "Fabio Banyu Cyto", "jabatan": "Kepala Departemen Mikfes", "nim": "12340104", "umur": "21", "asal": "Bandar Lampung", "alamat": "Kedaton", "hobbi": "Tidur", "sosmed": "@biyokcb", "kesan": "Gayanya santai dan tidak pernah ribet.", "pesan": "Tetap jadi abang yang asyik."},
        {"nama": "Tanty Widiyastuti", "jabatan": "Sekretaris Departemen Mikfes", "nim": "123450094", "umur": "21", "asal": "Lampung", "alamat": "Airan Raya", "hobbi": "Membaca", "sosmed": "@tvnty_", "kesan": "kakaknya lucu cerewet perhatian.", "pesan": "Terus bagikan ketelitianmu ke kami"},
        {"nama": "Fadil Prasetyo Alfaritzi", "jabatan": "Kepala Divisi PSD", "nim": "123450048", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Gitar", "sosmed": "@fadilalfarizzii", "kesan": "Permainan gitarnya bikin suasana nyaman.", "pesan": "Sering-sering hibur kami lewat musikmu, Kak."},
        {"nama": "Manuel Frederika", "jabatan": "Staf PSD", "nim": "124450039", "umur": "20", "asal": "Batam", "alamat": "Way Kandis", "hobbi": "Tenis meja", "sosmed": "@manuelfdk_", "kesan": "Energik dan cepat akrab dengan siapa saja.", "pesan": "Tetap semangat dan jangan berubah, Kak."},
        {"nama": "Ni Made Okta Viola Darma Putri", "jabatan": "Staf PSD", "nim": "124450005", "umur": "12", "asal": "Bali", "alamat": "Nusa Penida", "hobbi": "Menghayal", "sosmed": "Violaadrtr_", "kesan": "Pembawaannya kalem dan penuh imajinasi.", "pesan": "Semoga ide-idemu terus berkembang, Kak."},
        {"nama": "Risa Romadona", "jabatan": "Staf PSD", "nim": "124450127", "umur": "20", "asal": "Natar", "alamat": "Natar", "hobbi": "Rolling skate", "sosmed": "risarmdna", "kesan": "Aktif dan berani mencoba hal baru.", "pesan": "Terus berani melangkah, Kak."},
        {"nama": "Vannisa Ramadhani", "jabatan": "Staf PSD", "nim": "124450078", "umur": "19", "asal": "Kepulauan Riau", "alamat": "Teluk Betung", "hobbi": "Nonton KHW", "sosmed": "@vunnycaa", "kesan": "Ramah dan selalu terlihat ceria.", "pesan": "Tetap jadi pribadi yang menyenangkan, Kak."},
        {"nama": "Yulia Cristine Malau", "jabatan": "Staf PSD", "nim": "124450119", "umur": "20", "asal": "Jambi", "alamat": "Sabah Balau", "hobbi": "Belajar", "sosmed": "@krnylee", "kesan": "Sopan dan menghargai orang lain.", "pesan": "Semoga selalu sukses dalam setiap kegiatan, Kak."},
        {"nama": "Akeyla Fairuz Shafi", "jabatan": "Kepala Divisi PIKA", "nim": "1234501", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Dengerin Musik", "sosmed": "@keyashafi", "kesan": "Pendengar yang baik dan tidak suka menghakimi.", "pesan": "Tetap jadi teman cerita yang nyaman, Kak."},
        {"nama": "Elsa Sitorus", "jabatan": "Staf PIKA", "nim": "124450088", "umur": "21", "asal": "Sumatera Utara", "alamat": "Pemda", "hobbi": "Rebahan", "sosmed": "@_els.a", "kesan": "Murah senyum dan enak diajak bicara.", "pesan": "Tetap jadi kakak yang hangat, ya, Kak."},
        {"nama": "Lovianora Saragih", "jabatan": "Staf PIKA", "nim": "124450105", "umur": "19", "asal": "Sumatera Utara", "alamat": "Way Huwi", "hobbi": "Dengerin Musik", "sosmed": "_loviaa", "kesan": "Kalem tapi tetap hangat saat berinteraksi.", "pesan": "Semoga selalu dimudahkan dalam studinya, Kak."},
        {"nama": "Kaleb Filbert Istel", "jabatan": "Staf RnD", "nim": "124450053", "umur": "20", "asal": "Bandar Lampung", "alamat": "Campang Raya", "hobbi": "Ngegym, baca novel", "sosmed": "@kelelep_comberan", "kesan": "Kerenn, my idol my role model.", "pesan": "Tularkan dan tutorkan saya bangg kalebabb, awas khaleed bang."},
        {"nama": "M. Alsi Syahrulloh", "jabatan": "Staf PIKA", "nim": "124450092", "umur": "20", "asal": "Kalianda", "alamat": "Kotabaru", "hobbi": "Main Game, Tidur", "sosmed": "@aluccy_", "kesan": "Humoris dan gampang bikin tawa.", "pesan": "Jangan lupa tetap fokus kuliah juga, Kak."},
        {"nama": "Sherena Florencia", "jabatan": "Staf PIKA", "nim": "124450027", "umur": "19", "asal": "Bengkulu Selatan", "alamat": "Belwis", "hobbi": "Make up", "sosmed": "@sher_renna", "kesan": "Rapi dan selalu tampil percaya diri.", "pesan": "Tetap jadi inspirasi bagi adik tingkat, Kak."},
        {"nama": "Razin Hafid Hamdi", "jabatan": "Kepala Divisi RnD", "nim": "123450096", "umur": "21", "asal": "Padang", "alamat": "Belwis", "hobbi": "Futsal", "sosmed": "@razyn.hfd", "kesan": "Sportif dan semangat kerja samanya tinggi.", "pesan": "Terus ajak kami aktif bersama, Kak."},
        {"nama": "Faiza Try Anjani", "jabatan": "Staf RnD", "nim": "124450075", "umur": "19", "asal": "Padang", "alamat": "Belwis", "hobbi": "Membaca Novel", "sosmed": "@Faizaanjanii", "kesan": "Tutur kata kakaknya sopan my kanimmm.", "pesan": "Tetap jadi kakak yang bijak"},
        {"nama": "Gathfan Nadif Ali", "jabatan": "Staf RnD", "nim": "124450001", "umur": "20", "asal": "Bandar Lampung", "alamat": "Rajabasa", "hobbi": "Main game", "sosmed": "@gathfannadif", "kesan": "Santai tapi tetap bertanggung jawab.", "pesan": "Terus jaga keseimbangan itu, Kak."},
        {"nama": "Hafidz Wahdiansyah", "jabatan": "Staf RnD", "nim": "124450064", "umur": "20", "asal": "Metro", "alamat": "Metro Kibang, Lampung Timur", "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)", "sosmed": "@apiszzaja_", "kesan": "Cekatan soal teknis dan mau berbagi ilmu.", "pesan": "Ajari kami ngoding dengan sabar"},
        {"nama": "Kaleb Filbert Istel", "jabatan": "Staf RnD", "nim": "124450053", "umur": "20", "asal": "Bandar Lampung", "alamat": "Campang Raya", "hobbi": "Ngegym, baca novel", "sosmed": "@kelelep_comberan", "kesan": "Kerenn, my idol my role model.", "pesan": "Tularkan dan tutorkan saya bangg kalebabb, awas khaleed bang"},
        {"nama": "Melva Shaprina Febrianti", "jabatan": "Staf RnD", "nim": "124450087", "umur": "19", "asal": "Sumsel", "alamat": "Sukarame", "hobbi": "Scroll", "sosmed": "@melva_fbrt", "kesan": "Ceria dan mudah menyesuaikan diri.", "pesan": "Tetap jadi pribadi yang ramah, Kak."},
        {"nama": "Muhammad Syafiqul Falakh", "jabatan": "Staf RnD", "nim": "124450099", "umur": "20", "asal": "Lampung Utara", "alamat": "Asrama TB 3", "hobbi": "Membaca", "sosmed": "@syafiqui", "kesan": "Pendiam tapi diam-diam bisa diandalkan.", "pesan": "Jangan sungkan berbagi pendapat ke kami, Kak."},
        {"nama": "Rifky Henry Ferdianto", "jabatan": "Staf RnD", "nim": "124450115", "umur": "28", "asal": "Kobum", "alamat": "Rajabasa", "hobbi": "Lari dari kenyataan", "sosmed": "@henryferdianto", "kesan": "Humornya unik dan bikin suasana cair.", "pesan": "Semoga kenyataan selalu ramah padamu, Kak."},
    ]
    display_images_with_data(gambar_urls, data_list, key="mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1jKDOs48NUIKGq1A8Z0xngUZTr1crDCbX",
        "https://drive.google.com/uc?export=view&id=1IflEF9UfvFXL2iyAl2giEARM3Hacf6KG",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1vlyn4P2jCVepwf9Jk4HqcdGDDYWgB_B_",
        "https://drive.google.com/uc?export=view&id=18uWA7YLZ6xz3HcTtI06jZFrh6qYtsLuS",
        "https://drive.google.com/uc?export=view&id=1Q1MVOnXJp8ClRZnaXSvbl_qCZpyy4A48",
        "https://drive.google.com/uc?export=view&id=1VjqstZK3FzFIDp5jtp4S_2Qxq0v19etm",
        "https://drive.google.com/uc?export=view&id=1vXh_tDR2A5EvEp8z07lwVPYVn_LQK5Af",
        "https://drive.google.com/uc?export=view&id=1Nw489fRsyGd-63NoSgFKaRDIonyizgwg",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1Kjk1-T1hsYNlcMCJcyVQ2SF2w0qkvqka",
        "https://drive.google.com/uc?export=view&id=1Lj_vIIpVHEZ8tk1sXXTGCg-qX07c_0fW",
        "https://drive.google.com/uc?export=view&id=1axs_QMZ7UZbBaqhTp_JTY9gvdxJcEUB6",
        "https://drive.google.com/uc?export=view&id=19n9kDdp_kWpFFdU4qpYz1DVVO3-fjlbm",
        "https://drive.google.com/uc?export=view&id=1YoLCZA_w9h2t6Lr9w0KKRplgHh0pKvZK",
        "https://drive.google.com/uc?export=view&id=12kzNFYkrUgfPBuOh88dmhgnzrcO0Tp2s",
        "https://drive.google.com/uc?export=view&id=1h5w-XXVSVMOw6lA-RQWOW5ZAXAcy8p8I",
        "https://drive.google.com/uc?export=view&id=1rZMYltF9fVjeEfLvNq2SJeV4XROlMKmx",
        "https://drive.google.com/uc?export=view&id=1SwIXsRxz10A6iuWGPVwb3TxVgha77dhV",
        "https://drive.google.com/uc?export=view&id=1YshCV-3Y01ZA_VkMKjQ55NuAta6ssuuz",
        "https://drive.google.com/uc?export=view&id=1Aaoq3XxCWHAZ1CENfeDTHaZ9Hvo-rFMa",
        "https://drive.google.com/uc?export=view&id=1JIlO5g2WvnVKUWfjhtUeHQXKa2pJLc_5",
    ]
    data_list = [
        {"nama": "Arini Puteri Elandra", "jabatan": "Staf Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "kakaknya kocak pernah sekelompok di kdp gacor", "pesan": "semoga makin kerenn, tutorr kakk"},
        {"nama": "Nabyla Sharfina", "jabatan": "Staf Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "kakaknya Ramah dan perhatian", "pesan": "Selalu jadi orang baik ya kak"},
        {"nama": "Khoirul Muttoharoh", "jabatan": "Staf Eksternal", "nim": "1234500", "umur": "-", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Main", "sosmed": "@khoirul_muttoharoh", "kesan": "Enak diajak ngobrol", "pesan": "Semangat terus bangg"},
        {"nama": "Ahmad Rizky", "jabatan": "Staf Eksternal", "nim": "123450050", "umur": "21 Tahun ini Alhamdulillah", "asal": "Tangerang Selatan", "alamat": "GH", "hobbi": "Ngga ngapa ngapain", "sosmed": "@ahmad.rizky__", "kesan": "Kerenn bangett bang, gacor, role model", "pesan": "Selalu jadi orang yang kritis dan perbanyak senyum bang"},
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
    ] * 22
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1eyEq2i1K-5zHOuDZTku2ZmuUvOLVqA39",
                   "https://drive.google.com/uc?export=view&id=1IO5VmRR1zmkI0VlVXbEVeIChXDlA-ajS",
                   "https://drive.google.com/uc?export=view&id=1bpEkbl47K2N2Dp09NxGjcZSkhDE4w9o_",
                   "https://drive.google.com/uc?export=view&id=1AD-hSjaKlGiVNz3EHemcpzhChv66sHV8",
                   "https://drive.google.com/uc?export=view&id=1k97cNHFdCcJD5l_oEEf0eKTrIjSOhcft",
                   "https://drive.google.com/uc?export=view&id=1oMj9-110iZ-hCEdQGL544k8PVH4O6MaW",
                   "https://drive.google.com/uc?export=view&id=1RYzsIJ3xYqeuFF-1jRhOchI1C1j8dP_Q",
                   "https://drive.google.com/uc?export=view&id=1hNPSkMYC15KMneoBWTMen6agAYiFCEWr",
                   "https://drive.google.com/uc?export=view&id=1clZ_QQNZQousMUe4Glbd33X1fKSF8Kob",
                   "https://drive.google.com/uc?export=view&id=16Be-N8A0X68n-VAUEzwplT3Y_u0f28Xo",
                   "https://drive.google.com/uc?export=view&id=1NakM6Vn6KTmJdycbrz1j9137IxJRnxKF",
                   "https://drive.google.com/uc?export=view&id=1UM2S-buMlcOspDX7yzY5Uw64ww4K56RX",
                   "https://drive.google.com/uc?export=view&id=1pSD85RA2UUz4PteWuF7nRE93yLZau80i",
                   "https://drive.google.com/uc?export=view&id=1amPeK5x9aW09HeLEt0P3Dx4xvc5Xg-_t",
                   "https://drive.google.com/uc?export=view&id=17x8KA1eURlVaIAQz5n7vb4XwWCzwpROq",
                   "https://drive.google.com/uc?export=view&id=1aVtXDrojjgVln1mmayaXRrGHnf6VxAZk",
    ]
    data_list = [
        {"nama": "Haikal Fransisko Simbolon", "jabatan": "Kepala Departemen Internal", "nim": "123450106", "umur": "20", "asal": "Jambi", "alamat": "Way Halim", "hobbi": "Ngeledek Orang", "sosmed": "@haikalsbln", "kesan": "Humornya receh dan kocak tapi bikin akrab.", "pesan": "Jaga suasana cair tanpa berlebihan."},
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
        "https://drive.google.com/uc?export=view&id=1QrRxujgmVfZ92lno4la7wxqEyJMvAIt3",
        "https://drive.google.com/uc?export=view&id=1WRK48UMhbQAyWgFJrAzvkl4kM2dVPgeA",
        "https://drive.google.com/uc?export=view&id=1AcPhhoZ9Et2UJS-lIrmhJ2-jPOMvQnpp",
        "https://drive.google.com/uc?export=view&id=1HbqyPODWJS_Tv3TrHXvq9R-JBQi5CfsL",
        "https://drive.google.com/uc?export=view&id=13EKDQxiPgx1riA82sggBf8uO8FQxkZKR",
        "https://drive.google.com/uc?export=view&id=1_Qa8DvVGkjg-4Z7GZ8sFOPa2AaxyuoZH",
        "https://drive.google.com/uc?export=view&id=1yRYAIwml08qlW0ba8IXi1jImunNTbK2u",
        "https://drive.google.com/uc?export=view&id=1tF3x11LnMtJwzjA1nsFj7bWwYxdEQW_9",
        "https://drive.google.com/uc?export=view&id=1IbYZQ-ZRZkN_zMVhrVBXoYJB3NNLcWB-",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=198d96uuot_tGHCiNPq9Mogko-SY3L_4g",
        "https://drive.google.com/uc?export=view&id=1Rw_5EofMIqGr-RsAB9fjNUrsZAH8ixLT",
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Staf SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "abangnya kocak, kalem tapi cerdas", "pesan": "semoga makin keren dan cepat IMO!"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Staf SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "kakaknya serem tapi perhatian", "pesan": "perbanyak senyum kak!"},
        {"nama": "Afifah Fauziah", "jabatan": "Staf SSD", "nim": "12345002", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "kakaknya lucu dan ketawa teruss", "pesan": "stay humble kak!"},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Staf SSD", "nim": "1234500", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@hasan.ramadhan08", "kesan": "abangnya kalem", "pesan": "sehat selalu bang"},
        {"nama": "Layina Ropiqo", "jabatan": "Staf SSD", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "kakaknya kalem", "pesan": "semangat selalu kak!"},
        {"nama": "Moch. Iqbal Az-Zahir", "jabatan": "Staf SSD", "nim": "122450052", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@iqbalazzahir_", "kesan": "abangnya kalem tapi pintar", "pesan": "semoga semanagat dan sehat selalu!"},
        {"nama": "Talitha Justine", "jabatan": "Staf SSD", "nim": "122450076", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "kakaknya kalem dan baik", "pesan": "perbanyak senyum kak!"},
        {"nama": "Anadia Carana", "jabatan": "Staf SSD", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "kakak nya baik dan ramah", "pesan": "perbanyak senyum kak!"},
        {"nama": "Abdillah Fikri Al pome", "jabatan": "Staf SSD", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@ssd", "kesan": "abangnya baik dan hebat", "pesan": "sehat selalu bang!"},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Staf SSD", "nim": "124450008", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@dhal_setiawan", "kesan": "abangnya baik dan kerenn", "pesan": "makin kecee bangg!"},
        {"nama": "Anggun Nita", "jabatan": "Staf SSD", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa", "kesan": "kakaknya baik dan perhatian", "pesan": "stay humble kak!"},
        {"nama": "Della Anisa Fitri", "jabatan": "Staf SSD", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "kakaknya hebat dan perhatian", "pesan": "sehat dan semangat terus kak!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1tQtKPE33XvtHYFFH9E-JgyNVfJJGs8Oq",
        "https://drive.google.com/uc?export=view&id=1vfm__BjVsYZ2iJ2xYYgAd4js3uT6FWiE",
        "https://drive.google.com/uc?export=view&id=1gCwVluHER9zwNxeRkVS-NwtAOXXh1YPo",
        "https://drive.google.com/uc?export=view&id=1vnBvhaDAaclYUfNZW0CYYOqJrjNMsgtU",
        "https://drive.google.com/uc?export=view&id=1VnZZ0elxkLWc3H4o2M8F0rMjfTjXZMJd",
        "https://drive.google.com/uc?export=view&id=1QZkwiLD3Ogw6CZIfkFXDLjzp5LOoyR-R",
        "https://drive.google.com/uc?export=view&id=1y_EKN7304sdXsA_pcM3C-evtR63tEUQ6",
        "https://drive.google.com/uc?export=view&id=1OS6SbsMIl8rU5aH7k7Po-8oXHSfrmf5J",
        "https://drive.google.com/uc?export=view&id=12UFotzHaPvL2B5bpzxBOhqD2Z7vqg_ka",
        "https://drive.google.com/uc?export=view&id=1Q1fuPrZ0JlRxdQVElfaZt_Z5OKlLysKy",
        "https://drive.google.com/uc?export=view&id=1uldvmHPpTo7KuAq6WxMwvnPH7gyK0n_4",
        "https://drive.google.com/uc?export=view&id=1GtoH93BH3oO8eB5Lcab6g71BhT89nGH3",
        "https://drive.google.com/uc?export=view&id=1c_xEQ_0edrA9TEdpBwM-RckaKoLwJMNP",
        "https://drive.google.com/uc?export=view&id=1kCGCN9nuJNOS5FyNm5VeootRboL-YawC",
        "https://drive.google.com/uc?export=view&id=1TXczhSAV1e0DFdQ7rBtQ6XwLtOHVaX5M",
        "https://drive.google.com/uc?export=view&id=1jqpe5nWNyJ5HwsJ4ihHdoizx8bkcwEI0",
        "https://drive.google.com/uc?export=view&id=1UKkwqBsLFl62XaN69frWNrLdqYu9OY3p",
        "https://drive.google.com/uc?export=view&id=1Zm0HGc0sTXtUaa8KEKFgHTmKh0Km6atF",
    ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Staf Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "baik dan perhatian", "pesan": "perbanyak senyum kakkk"},
        {"nama": "Donna Maya Puspita", "jabatan": "Staf Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "senyum kakaknya manis", "pesan": "terus jadi orang baik kak"},
        {"nama": "Labo John Noel Napitupulu", "jabatan": "Staf Medkraf", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "Abangku paling kerennn multitalent, sigma", "pesan": "semangat terus abangkuu, ajarinlah adekmu ini bangg"},
        {"nama": "Anash Tasya Ausyaqila", "jabatan": "Staf Medkraf", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "kakaknya baik dan Kreatif", "pesan": "perbanyak senyum dan terus semangat kak"},
        {"nama": "Felisya Nabila Putri Nugroho", "jabatan": "Staf Medkraf", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "kakaknya hebat", "pesan": "semoga sehat selalau dan makin bisa diandalakan, ajarin mancing emosi kak!"},
        {"nama": "Muhammad Razan Maulana Pratama", "jabatan": "Staf Medkraf", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "abangnya punya aura yang elegan", "pesan": "semoga terus jadi abang yang baik dan kalem!"},
        {"nama": "Sania Dwi Ayu Lestari", "jabatan": "Staf Medkraf", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kakaknya stylish gacor", "pesan": "semangat selalu kak!"},
        {"nama": "Allisha", "jabatan": "Staf Medkraf", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kakaknya ketcee parah, aktif banget", "pesan": "stay humble kak!"},
        {"nama": "Alya Ramadhanti", "jabatan": "Staf Medkraf", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kakaknya baik dan ketcee", "pesan": "tetap jadi orang baik kak!"},
        {"nama": "Bunga Clarisa Sefa", "jabatan": "Staf Medkraf", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kakaknya baik dan wangi", "pesan": "semangat teruss kak stay humble!"},
        {"nama": "Difanya Husakina", "jabatan": "Staf Medkraf", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "kakaknya baik dan lucu", "pesan": "ajarin mancing kak!"},
        {"nama": "Nazlah Auliya", "jabatan": "Staf Medkraf", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "kakaknya lucu, agak cerewet dikit", "pesan": "stay humble kak!"},
        {"nama": "Raihana Adelia Putri", "jabatan": "Staf Medkraf", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "kakaknya baik dan kalem saat ngomong", "pesan": "perbanyak senyum kak!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "abangnya baik dan hebat", "pesan": "makin ketcee bang!"},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "abangnya pendiem dan kalem", "pesan": "terus berkarya bang!"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Medkraf", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kakaknya baik dan hebat", "pesan": "semangat terus kak!"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Medkraf", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kakaknya baik dan elegan", "pesan": "perbanyak senyum kakk!"},
        {"nama": "Anggota Medkraf", "jabatan": "Staf Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kakaknya baik dan perhatian", "pesan": "terus berkarya kak!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="medkraf")


elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1PIQ2Ab6JIg_Ry0AFKRmQXE7W1RERlgeB",
        "https://drive.google.com/uc?export=view&id=1NRU_oYuBNR8jgcjI6gafRNUfMjIGuYo7",
        "https://drive.google.com/uc?export=view&id=1TmBqyg4Z5XeSWad_vluosrznEVsJBpef",
        "https://drive.google.com/uc?export=view&id=1d00Ks5JtvCW_vJOqP4a_40xeMg0bxOGF",
        "https://drive.google.com/uc?export=view&id=1lR9SLQdZxpw9-vfIZynF1CuawBRhwNaO",
        "https://drive.google.com/uc?export=view&id=1RqymcFgnIpCjmOoeIEzon--nZUUwSMER",
        "https://drive.google.com/uc?export=view&id=1kWJ0EdVQCXwq-7gAkZg2wLL8DezpSrl6",
        "https://drive.google.com/uc?export=view&id=1sKIJuwumNtdpVTt2pwsHyfUN86H-fo3d",
        "https://drive.google.com/uc?export=view&id=1ngzaGagn-eS5POLEXdzZPJqd7DdX7YEj",
        "https://drive.google.com/uc?export=view&id=17uH_07R33C-zHfQqQz_-BUrADoK4R7Do",
        "https://drive.google.com/uc?export=view&id=1tghaHvLXdpANViBEsQU7cgt_ZepkFwcJ",
        "https://drive.google.com/uc?export=view&id=1AfJEXxugAyBTZmOXK7M0NKntOjWP9blO",
        "https://drive.google.com/uc?export=view&id=1iRdjFXHrpw7iofibOY12O3TZWLxXktpu",
        "https://drive.google.com/uc?export=view&id=1UCoi2ow3SDkc_ma-2ao4OfYBpjpUxQsk",
        "https://drive.google.com/uc?export=view&id=1o7JwjE2HV1alzPOE75Ig6_TzX_X5d2Xq",
    ]
    data_list = [
        {"nama": "Kevin Antonio Junior", "jabatan": "Kepala Departemen Minbak", "nim": "123450109", "umur": "21", "asal": "Bandar Lampung", "alamat": "Panjang, Bandar Lampung", "hobbi": "Balap", "sosmed": "@kevinaj__", "kesan": "Aura pemimpin dan bisa diandalkan.", "pesan": "Tetap jadi abang yang asyik pas diajak ngobrol, bang."},
        {"nama": "Gusti Putu Ferazka Dhiyamika", "jabatan": "Sekretaris Departemen Minbak", "nim": "123450046", "umur": "21", "asal": "Lampung Utara", "alamat": "Way Halim", "hobbi": "Baca", "sosmed": "@ferazkaa", "kesan": "kakaknya baik dan murah senyum.", "pesan": "Terus berkembang menjadi orang baik, Kak."},
        {"nama": "Ari Aristo Muthahari Parisi", "jabatan": "Kepala Divisi Manajemen Aktivitas dan Kompetisi", "nim": "123450088", "umur": "21", "asal": "Lampung Timur", "alamat": "Gang Sakum, Belwis", "hobbi": "Nonton F1", "sosmed": "@ali_parisi3", "kesan": "abangnya kalem, baik, dan dapat diandalkan.", "pesan": "Tetap jadi pribadi yang rendah hati, bang."},
        {"nama": "Ayu Andriani Parlina Wati", "jabatan": "Staf Ahli Manajemen Aktivitas dan Kompetisi", "nim": "124450058", "umur": "20", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Belajar", "sosmed": "@aayuandrianni_", "kesan": "kakaknya baik dan kalem saat ngobrol.", "pesan": "Semoga kakaknya semangat terus."},
        {"nama": "Dafa Elpriza", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450131", "umur": "21", "asal": "Bekasi", "alamat": "Way Kandis", "hobbi": "Nemenin Bryan live TikTok", "sosmed": "@dafaelpriza_", "kesan": "abang nya tenang dan ngomong yang penting aja.", "pesan": "semoga semangat dan sehat selalu abangggg."},
        {"nama": "Juwita Sari", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450066", "umur": "19", "asal": "Lampung Barat", "alamat": "Pemda", "hobbi": "Lihat bulan", "sosmed": "@ju.juwitaaa_", "kesan": "Sikap kakaknya lembut.", "pesan": "perbanyak senyum Kak."},
        {"nama": "Muhammad Afdal Lutfi", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450047", "umur": "19", "asal": "Lampung Tengah", "alamat": "Jl Pulau Damar", "hobbi": "Taptap layar kalo Bryan live", "sosmed": "@afdall.03", "kesan": "abangnya baik dan asyik saat ngobrol.", "pesan": "selalu senyum bangg."},
        {"nama": "Salsabila Nazwa Putri", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450002", "umur": "20", "asal": "Metro", "alamat": "Korpri", "hobbi": "Nongkrong di Kopken", "sosmed": "@slbnzw_", "kesan": "kakaknya manis dan baik saat ngobrol.", "pesan": "perbanyak senyum sama ke metro yo Kak."},
        {"nama": "Muhammad Ridwan", "jabatan": "Kepala Divisi Manajemen Minat dan Bakat", "nim": "123450091", "umur": "21", "asal": "Lampung Tengah", "alamat": "Belwis", "hobbi": "Nganterin Datasena ke gedung F", "sosmed": "@mridwaan_22", "kesan": "aura nya sigma abiss.", "pesan": "Semangat terus bang dan makin ketcee, Kak."},
        {"nama": "Andra Ilham Bintang", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450060", "umur": "18", "asal": "Sumatera Selatan", "alamat": "Kota Baru", "hobbi": "Ngitungin kelopak bunga di kebun", "sosmed": "@andra.lhm", "kesan": "abangnya asik banget, ketcee parah.", "pesan": "Tetap jadi bintang dengan gaya enjoymu itu bangg."},
        {"nama": "Bryan Paskah Telaumbanua", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450003", "umur": "22", "asal": "Nias", "alamat": "Belwis", "hobbi": "Live TikTok", "sosmed": "@bryantel_", "kesan": "abangnya keren bisa banyak musik.", "pesan": "semangat terus bang ajarin bolee kali."},
        {"nama": "Ghiyats Thabularasa Meardhy", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450067", "umur": "17", "asal": "Bekasi", "alamat": "Korpri", "hobbi": "Ngegift live Bryan", "sosmed": "@meardhy_ghiyats", "kesan": "abangnya kalem dan elegan.", "pesan": "Semoga sehat dan stay sigma."},
        {"nama": "Indah Julia Mawar Pratiwi", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450055", "umur": "20", "asal": "Pringsewu", "alamat": "Airan", "hobbi": "Bengong", "sosmed": "@indahjuliaa", "kesan": "kakaknya baik dan asik saat ngobrol.", "pesan": "semoga kakaknya sehat teruss dan makin aktiff."},
        {"nama": "Jacinda Kesya Alvara", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450023", "umur": "18", "asal": "Kalimantan Barat", "alamat": "Korpri", "hobbi": "Nyapu depan gacoan", "sosmed": "@cacalvra", "kesan": "kakaknya kalem dan hebat.", "pesan": "perbanyak senyum kak."},
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450089", "umur": "20", "asal": "Padang", "alamat": "Kota Baru", "hobbi": "Bangun pagi", "sosmed": "@muhammdrafka_", "kesan": "abangnya bisa lucu dan tegas serius tergantung situasi.", "pesan": "stay hard stay humble bang."}
    ]
    display_images_with_data(gambar_urls, data_list, key="minbak")
