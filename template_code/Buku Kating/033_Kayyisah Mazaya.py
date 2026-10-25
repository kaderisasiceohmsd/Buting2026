from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1rQKJe_Zt68A83KD8ywHtxynzHyFWnxh3",
        "https://drive.google.com/uc?export=view&id=1UUb42OuOEfD4fel9_FVInxiU_v2YBkpK",
        "https://drive.google.com/uc?export=view&id=1Yaq6RbQMCJjCDltE8fKGnpUUsCypcuKg",
        "https://drive.google.com/uc?export=view&id=1VexjFKg4cxJvh4VboZS9Qo836WUAtnZg",
        "https://drive.google.com/uc?export=view&id=1I9O_OInTjfCaeMklmbScrIaERp8tXDEb",
        "https://drive.google.com/uc?export=view&id=1mwupEwMqo1IFeRVyyk3MX6NmfMf3tVH_",
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "20", "asal": "Medan", "alamat": "Korpri", "hobbi": "Main Game, Futsal", "sosmed": "@jars_mrp", "kesan": "Sangat seru", "pesan": "Semangat terus bang dalam menjalankan tugas dan kuliahnyaaa!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya lucuuu bisa diajak bercanda dan bisa diajak bicara serius", "pesan": "Sukses selalu bang semangat menjalankan tugas dan kuliahnya"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya imut murah senyum", "pesan": "Sukses selalu kak dan semangat kuliahnyaa!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya soft spoken dan pendiam", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum", "pesan": "Sukses selalu dan semangat kuliahnya kaaakk!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baiiik", "pesan": "Sukses selalu dan semangat kuliahnya kaakaaa!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1hVTbtc8kxw9Wojmbhew4gyMOoxh7L161",
                   "https://drive.google.com/uc?export=view&id=1QLzcWiphn8KdE4v8pm60SVUiZ-JEIpOq",
                   "https://drive.google.com/uc?export=view&id=1sYlhu5R3qMOfH4pnmi0EhrpAQzloEejr",
                   "https://drive.google.com/uc?export=view&id=1ijKwJuwSKMGKLbTohWnkPgL-PSE0RfRm",
                   "https://drive.google.com/uc?export=view&id=15FK8_JnAe3aQfNXUgZYLMehuAYhPGKHp",
                   "https://drive.google.com/uc?export=view&id=15d1k5edAzugMWb2Iiy_tNc2LbuTUyMbG",
                   "https://drive.google.com/uc?export=view&id=1rwm5gs6dyA-oQ_pDdkOGVnjkQ_52_Js3",
                   "https://drive.google.com/uc?export=view&id=1p_meLyOVdpXopypWO1W5XF6RlSTUCLFg",
                   "https://drive.google.com/uc?export=view&id=1To96TmsO9fNRgLLbId_GGygliovGzIk4",
                   "https://drive.google.com/uc?export=view&id=1Dih47_xH9Apljkfo9HiNpGKoakSt7nG6",
                   "https://drive.google.com/uc?export=view&id=1ZSFbiRIsyvcWeJ7DGlJIEEtodJPeP8zL",
                   "https://drive.google.com/uc?export=view&id=1Pm-_1tU-kqs7aTtqjVczPcHoxR-37agJ",
                   "https://drive.google.com/uc?export=view&id=1K4H3ozJQlLvghqIGkhvUPAur1eFWKcI1",
                   ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik ", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "Bang ridho keren, asik banget", "pesan": "Lancar kuliah  dan sukses selalu bangg"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim", "sosmed": "@j__eesie", "kesan": "Kak Juee lucuu baik banget", "pesan": " semoga lancar kuliahnya dan sukses selalu kak "},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Bang dharu mapress kereennn, asik bangett", "pesan": "Semangatt semoga lancar kuliahnya dan sukses selalu bangg"},
        {"nama": "Gh Mikael Niko Anthoni Setiadi", "jabatan": "Staff Komisi I", "nim": "124450022", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@me._kael", "kesan": "bang niko keren, asikk, lucuuu ", "pesan": "Semangat kuliahnya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Kak Syarifa baikk, ramah, murah senyumm", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II", "nim": "124450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum kopi", "sosmed": "@givarooo", "kesan": "Bang Givaro keren, seruuu, baik", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "Kak nisa baikk, ramah, murah senyum", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "city earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain_", "kesan": "Kak Hani baikk, ramah, imoett", "pesan": "Kak Hani semangat kuliahnya, semoga lancar dan sukses selalu kakk"},
        {"nama": "Jeremia Halim", "jabatan": "Staff Komisi II", "nim": "124450101", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@jeremia_hm", "kesan": "Bang Jeremia keren, asikk, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@monica_tjg", "kesan": "ka monicaa baikk, ramah", "pesan": "semangat kuliahnya kaakaaa, semoga lancar dan sukses selalu kakk"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "gym / koleksi figur", "sosmed": "@nagatsee", "kesan": "Bang Jona keren, asikk, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "Kak Sekar baikk, ternyata setelah kenal asikk, ramah, murah senyum", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nahaysh", "kesan": "Kak wan baikk, ramah, murah senyum", "pesan": "Semangat kuliahnya nya kakk, semoga lancar dan sukses selalu kakk"}
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1enHDKPtCOJOcop2buBK1XrKToVI4xZRu",
        "https://drive.google.com/uc?export=view&id=1sTM68iTeccY1N_HNK8-l67p0X_C-MxML",
        "https://drive.google.com/uc?export=view&id=1fOA1GgkNbl8GD90SDJ2ze3r6E74dWhea",
        "https://drive.google.com/uc?export=view&id=15yg4LkBDNLIK3vtCUcJ5nsH6Q7xXXatv",
        "https://drive.google.com/uc?export=view&id=15FK8_JnAe3aQfNXUgZYLMehuAYhPGKHp",
        "https://drive.google.com/uc?export=view&id=1kZAXlYUaPhu0uugLMid1W18_QCr9bdD0",
        "https://drive.google.com/uc?export=view&id=1eMUs2LR1894MEr5geYNnF0PLnFzu2Kdg",
        "https://drive.google.com/uc?export=view&id=1BnqiSFg1OYXtZt_qa4DcN5WY1law1NSn",
        "https://drive.google.com/uc?export=view&id=16DGXpCnk-Edumj3KBfbouhGXh698N3pQ",
        "https://drive.google.com/uc?export=view&id=10iYQkpIOJKCnkXoej6Mzc6R6VL4WAvug",
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "ka azizah kerenn jujur terpesona, baik hati ", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Kepala Biro Aspirasi dan Media Komunikasi ", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya asik, ramah, dan seru diajak ngobrol", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Abangnya asik, orangnya santai", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Suci Aulia", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "kakanya baiikk, lucuu, kerendeh", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "abangnya baik, satset", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Biro Kajian Strategis dan Propaganda", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "kaka cantik, cheerful and colorfull", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "hmm terlihat tegas, tapi baik hati ko", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Kepala Biro Kesekretariatan", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "kaka baik hati , imoet dan tidak sombong", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Staff Biro Kesekretariatan", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "ka dwi vibes kalem banget, baik ", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"}
    ]
    display_images_with_data(gambar_urls, data_list, key="senator")


elif menu == "Departemen PSDA":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=11tpMUgeQ_vl04gbwsC-KOdRdepvBhTQ_",
                   "https://drive.google.com/uc?export=view&id=1GYLSetdOG8A_Rv2sw1_xHofFaKpD2_xK",
                   "https://drive.google.com/uc?export=view&id=15kzEo6__8qV6Ar4nVyAvPc3kGCs7C8iD",
                   "https://drive.google.com/uc?export=view&id=1_YQyIRR67NYKIYRMoBWJsYo3TNtiiCFu",
                   "https://drive.google.com/uc?export=view&id=1uCswG5vGa7W_3fsk5jGogfziNA9QsB4I",
                   "https://drive.google.com/uc?export=view&id=1OFJfzVUFnvngs2ICjHR73kkZc9qU-p1h",
                   "https://drive.google.com/uc?export=view&id=1WQh5nEIMzvSyG_bxsXWyepQm5TP5dyGL",
                   "https://drive.google.com/uc?export=view&id=1n9dbx_NwB5cHjUyKTLt5Cak1pKSQFHO5",
                   "https://drive.google.com/uc?export=view&id=1Gh8HUAnpj48Lm1c6grpsxPT1tCfo_3YN",
                   "https://drive.google.com/uc?export=view&id=18TOrQOq8kFFdqSOerre1AVbOw6W6egLu",
                   "https://drive.google.com/uc?export=view&id=1lvn8oJJ3HWZ9vHEX7JOR4ixHjjIRALXd",
                   "https://drive.google.com/uc?export=view&id=1KZGnmMyC1L3XLtQKpuHLlzlzUHtJbHKs",
                   "https://drive.google.com/uc?export=view&id=1m3sUncrGWmkm0bPTCGfbRtssZhc1ZzGA",
                   "https://drive.google.com/uc?export=view&id=1vkwiWDQD2AHlxZh6ZNAA-Oewb6xSJGdk",
                   "https://drive.google.com/uc?export=view&id=1YTgvkol2Ghm0vxWUY6AN13Cetn64ttKj",
                   "https://drive.google.com/uc?export=view&id=15b-h28pE2mT0_i-6tu4cPAwtYFrtvURR",
                   "https://drive.google.com/uc?export=view&id=1fU1qz-EjlZGfLWokFb8f13sJ7YRVrx5Q",
                   ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "123450097", "umur": "21", "asal": "Kalianda", "alamat": "Samping kost Haikal", "hobbi": "Naksir cowo cakep", "sosmed": "@arientakhsnl_", "kesan": "Ramah lucuuu pipinya merah seperti apel", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Vany Salsabila", "jabatan": "Sekretaris Departemen PSDA", "nim": "124450022", "umur": "21", "asal": "Sibolga", "alamat": "Cenderawasih 1", "hobbi": "Ngurus peternakan", "sosmed": "@charrlnn", "kesan": "ka vany baik, ramah, humble", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Nobel Nizam Fathirizki", "jabatan": "Kepala Divisi Kaderisasi", "nim": "123450117", "umur": "21", "asal": "Bandar Lampung", "alamat": "Urip", "hobbi": "-", "sosmed": "@nobelnizam", "kesan": "Bang nobel keren,baik", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Afriza Azmi", "jabatan": "Staf Kaderisasi", "nim": "124450110", "umur": "20", "asal": "Lamteng", "alamat": "Sebelah kost Haikal", "hobbi": "Nyebar beras", "sosmed": "@friezazmi", "kesan": "Bang azmi baik, kerenn","pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Ayake Alfatih Ramadan", "jabatan": "Staf Kaderisasi", "nim": "124450108", "umur": "20", "asal": "Solo", "alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung", "hobbi": "Goreng ayam", "sosmed": "@ykeall", "kesan": "bang yake lucu, kerenn, baik", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Caesar Ozora Alrando", "jabatan": "Staf Kaderisasi", "nim": "124450017", "umur": "21", "asal": "Rahim ibu", "alamat": "Gedung F", "hobbi": "Pengembala anak ayam", "sosmed": "@caesar.oriza", "kesan": "bang caesar humble, baik, kerenn", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Euodia Meiliana Friedita", "jabatan": "Staf Kaderisasi", "nim": "124450029", "umur": "20", "asal": "Asal asalan", "alamat": "Diatas tanjakan", "hobbi": "Ngekader", "sosmed": "@yudiameilianaa_", "kesan": "ka yudiaa baik, humoris dan maniess", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Haikal Seventino Tamba", "jabatan": "Staf Kaderisasi", "nim": "124450012", "umur": "25", "asal": "Jambi", "alamat": "Sebelah kontrakan Jemar", "hobbi": "Ngurusin pakan anak ayam", "sosmed": "@_haikaaalll", "kesan": "Bang Haikal kerenn, baikk, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Putri Manna Anantama Simbolon", "jabatan": "Staf Kaderisasi", "nim": "124450065", "umur": "18", "asal": "Depok", "alamat": "Nomandenl", "hobbi": "Mancing emosi", "sosmed": "@putrimannaa", "kesan": "ka putrii cheerful, baik, ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Queenta Thifaal Nabila", "jabatan": "Staf Kaderisasi", "nim": "124450059", "umur": "21", "asal": "Lamteng", "alamat": "Depan pemancingan", "hobbi": "Nyuapin anak ayam", "sosmed": "@queentanaabila", "kesan": "Kak Queenta lucu, maniess dan juga baikk", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi PMA", "nim": "123450114", "umur": "18", "asal": "Palembang Sekayu", "alamat": "Asrama TB 3", "hobbi": "Ngejek orang", "sosmed": "@dsmanhl", "kesan": "bang desman orangnya humoris dan bikin suasana cair.", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf PMA", "nim": "124450041", "umur": "19", "asal": "Teluk", "alamat": "Bandar Lampung", "hobbi": "Pilates", "sosmed": "@azzelytn", "kesan": "kakanya cantikk imoet", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Charrlindah", "jabatan": "Staf PMA", "nim": "124450037", "umur": "21", "asal": "Jakarta Pusat", "alamat": "Cenderawasih 1", "hobbi": "Ngurus peternakan", "sosmed": "@charrlnn", "kesan": "Kak Charrlindah baikk, dan juga ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Jeremi Marolop Partogi Situmorang", "jabatan": "Staf PMA", "nim": "124450111", "umur": "16", "asal": "Berlin", "alamat": "Samping kos Rafli", "hobbi": "Mengembala anak ayam", "sosmed": "@jemarrro", "kesan": "bang jemarr keren, humoris, baik ", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf PMA", "nim": "124450048", "umur": "18", "asal": "Lampung", "alamat": "Barokah", "hobbi": "Main sama Azel", "sosmed": "@n.bila_a", "kesan": "Kak Nabila maniss, dan juga baik, ramah juga", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf PMA", "nim": "124450007", "umur": "20", "asal": "Sibolga", "alamat": "Samping kos Haikal", "hobbi": "Nonton", "sosmed": "@dearfkvmfl", "kesan": "Bang Rafli baik, dan juga ramah.", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Salavi Naharani", "jabatan": "Staf PMA", "nim": "124450090", "umur": "20", "asal": "Lampung Timur", "alamat": "Jatimulyo", "hobbi": "Minum air putih", "sosmed": "@avi.nhr", "kesan": "Kak Salavi lucuu, dan juga baik, ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"}
    ]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
        
    gambar_urls = [ "https://drive.google.com/uc?export=view&id=1eiHCZwFLGaKSUQ71kJ6bNlD6IBRYgyms",
                    "https://drive.google.com/uc?export=view&id=1pfkugvxkEytldAsU5zyl5eJUVVnWbhmb",
                    "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                    "https://drive.google.com/uc?export=view&id=1a6EmcdDBU1Vg70Xqk_HTyyhGB5Hi8e_Z",
                    "https://drive.google.com/uc?export=view&id=1h6NB1TQzeKoKWR8fDDDJYhsmcTXaHf-V",
                    "https://drive.google.com/uc?export=view&id=1CmZ4Ju3Skc1M2ry7s5wxQ8zX6rFGSpep",
                    "https://drive.google.com/uc?export=view&id=1mnx7dXFCTLOIee3K32VL3xCeCqjQAt7i",
                    "https://drive.google.com/uc?export=view&id=1MhHjlBBVySFhf4ADSozuqGKnpm65VBkv",
                    "https://drive.google.com/uc?export=view&id=1yW9BG_JUkHeED8KlY2oPjwR0FOK6Zbyi",
                    "https://drive.google.com/uc?export=view&id=1WQDW2Eyn_uUqy2i0SsO49ISH7lcOX27J",
                    "https://drive.google.com/uc?export=view&id=1S9RPwlAImXiNDsH_DCL6tqSbNnyqA9Vj",
                    "https://drive.google.com/uc?export=view&id=18gJQkoLePmGSpWn3bUiqvYuwjyFKRPL7",
                    "https://drive.google.com/uc?export=view&id=12xpdZXGLwJ5znJR2ZjsqG5hwJZkqMUTW",
                    "https://drive.google.com/uc?export=view&id=1vd7KCN4haTB907ES2ul7NsQbKUEL7WAh",
                    "https://drive.google.com/uc?export=view&id=1QHURH9SjESnT6y6Vvj4_K6v_Ic8EI_Xe",
                    "https://drive.google.com/uc?export=view&id=1GGEXvBqkZqRxscHlDU9XHz_5SmExLMyU",
                    "https://drive.google.com/uc?export=view&id=1uSUMlpc4ZgIyogBuIXbgvGT28fKusXj3",
                    "https://drive.google.com/uc?export=view&id=1r1GUMEBmPAQHjMh5vCn8h6plZGLyMg6z",
                    "https://drive.google.com/uc?export=view&id=1CoyIcInCYGfa4J6KwqKlJciMwsqVgvpZ",
                    "https://drive.google.com/uc?export=view&id=13HGSEzcaxFBjpkGEhOeDJdRJb2mOMR_W",
                    "https://drive.google.com/uc?export=view&id=1nTUre1Am-KSU-eLGSbAzLLCnaIaSLEGT",
                    "https://drive.google.com/uc?export=view&id=1Fubjccc-h1EDsRbdvUclCcnSQANzIGaw",
                     ]
        
    
    data_list = [
        {"nama": "Fabio Banyu Cyto", "jabatan": "Kepala Departemen Mikfes", "nim": "12340104", "umur": "21", "asal": "Bandar Lampung", "alamat": "Kedaton", "hobbi": "Tidur", "sosmed": "@biyokcb", "kesan": "bang fabio baik, asik, helpful kalo ngasprak ", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Tanty Widiyastuti", "jabatan": "Sekretaris Departemen Mikfes", "nim": "123450094", "umur": "21", "asal": "Lampung", "alamat": "Airan Raya", "hobbi": "Membaca", "sosmed": "@tvnty_", "kesan": "ka tantyyy cheerful sekali humoris", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Fadil Prasetyo Alfaritzi", "jabatan": "Kepala Divisi PSD", "nim": "123450048", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Gitar", "sosmed": "@fadilalfarizzii", "kesan": "Permainan gitarnya bikin suasana nyaman.", "pesan": "Sering-sering hibur kami lewat musikmu, Kak."},
        {"nama": "Manuel Frederika", "jabatan": "Staf PSD", "nim": "124450039", "umur": "20", "asal": "Batam", "alamat": "Way Kandis", "hobbi": "Tenis meja", "sosmed": "@manuelfdk_", "kesan": "Bang Manuel baik, ramahh, dan juga asik", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Ni Made Okta Viola Darma Putri", "jabatan": "Staf PSD", "nim": "124450005", "umur": "12", "asal": "Bali", "alamat": "Nusa Penida", "hobbi": "Menghayal", "sosmed": "Violaadrtr_", "kesan": "ka violaa baikk, cantik ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Risa Romadona", "jabatan": "Staf PSD", "nim": "124450127", "umur": "20", "asal": "Natar", "alamat": "Natar", "hobbi": "Rolling skate", "sosmed": "risarmdna", "kesan": "kakanya baik, manies, imoutt", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Vannisa Ramadhani", "jabatan": "Staf PSD", "nim": "124450078", "umur": "19", "asal": "Kepulauan Riau", "alamat": "Teluk Betung", "hobbi": "Nonton KHW", "sosmed": "@vunnycaa", "kesan": "ka vanissa baikk,ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Yulia Cristine Malau", "jabatan": "Staf PSD", "nim": "124450119", "umur": "20", "asal": "Jambi", "alamat": "Sabah Balau", "hobbi": "Belajar", "sosmed": "@krnylee", "kesan": "ka yulia baikk, kalem", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Akeyla Fairuz Shafi", "jabatan": "Kepala Divisi PIKA", "nim": "1234501", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Dengerin Musik", "sosmed": "@keyashafi", "kesan": "Bang Akeyla baikk, dan juga ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Elsa Sitorus", "jabatan": "Staf PIKA", "nim": "124450088", "umur": "21", "asal": "Sumatera Utara", "alamat": "Pemda", "hobbi": "Rebahan", "sosmed": "@_els.a", "kesan": "ka elsa baikk, ramah, Murah senyum ", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Lovianora Saragih", "jabatan": "Staf PIKA", "nim": "124450105", "umur": "19", "asal": "Sumatera Utara", "alamat": "Way Huwi", "hobbi": "Dengerin Musik", "sosmed": "_loviaa", "kesan": "ka loviaa baik,ramah,kalem", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "M. Alsi Syahrulloh", "jabatan": "Staf PIKA", "nim": "124450092", "umur": "20", "asal": "Kalianda", "alamat": "Kotabaru", "hobbi": "Main Game, Tidur", "sosmed": "@aluccy_", "kesan": "Bang Alsi baikk, dan ramahh", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Sherena Florencia", "jabatan": "Staf PIKA", "nim": "124450027", "umur": "19", "asal": "Bengkulu Selatan", "alamat": "Belwis", "hobbi": "Make up", "sosmed": "@sher_renna", "kesan": "ka sheren baik, rapih bangett, cheerful", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Razin Hafid Hamdi", "jabatan": "Kepala Divisi RnD", "nim": "123450096", "umur": "21", "asal": "Padang", "alamat": "Belwis", "hobbi": "Futsal", "sosmed": "@razyn.hfd", "kesan": "abangnya baik dan ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Faiza Try Anjani", "jabatan": "Staf RnD", "nim": "124450075", "umur": "19", "asal": "Padang", "alamat": "Belwis", "hobbi": "Membaca Novel", "sosmed": "@Faizaanjanii", "kesan": "kakanya manis,baik,dan ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Gathfan Nadif Ali", "jabatan": "Staf RnD", "nim": "124450001", "umur": "20", "asal": "Bandar Lampung", "alamat": "Rajabasa", "hobbi": "Main game", "sosmed": "@gathfannadif", "kesan": "bang gaftan baik dan ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Hafidz Wahdiansyah", "jabatan": "Staf RnD", "nim": "124450064", "umur": "20", "asal": "Metro", "alamat": "Metro Kibang, Lampung Timur", "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)", "sosmed": "@apiszzaja_", "kesan": "bang hafidz baik, peduli, kerendeh pokoknya", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Kaleb Filbert Istel", "jabatan": "Staf RnD", "nim": "124450053", "umur": "20", "asal": "Bandar Lampung", "alamat": "Campang Raya", "hobbi": "Ngegym, baca novel", "sosmed": "@kelelep_comberan", "kesan": "bang kaleb kerenn, pintar nyooo, humoris", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Melva Shaprina Febrianti", "jabatan": "Staf RnD", "nim": "124450087", "umur": "19", "asal": "Sumsel", "alamat": "Sukarame", "hobbi": "Scroll", "sosmed": "@melva_fbrt", "kesan": "Ka melva baik, imoett", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Muhammad Syafiqul Falakh", "jabatan": "Staf RnD", "nim": "124450099", "umur": "20", "asal": "Lampung Utara", "alamat": "Asrama TB 3", "hobbi": "Membaca", "sosmed": "@syafiqui", "kesan": "bang syafiq, baik, ramah, kerenn", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Rifky Henry Ferdianto", "jabatan": "Staf RnD", "nim": "124450115", "umur": "28", "asal": "Kobum", "alamat": "Rajabasa", "hobbi": "Lari dari kenyataan", "sosmed": "@henryferdianto", "kesan": "bang henry, baik, lucu, humoris", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
    ]
    display_images_with_data(gambar_urls, data_list, key="mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1nBgLRiaIw9HHjM4X1iJ8bAJFknr4xqSS",
        "https://drive.google.com/uc?export=view&id=163qgyzrWISiEhRRSAC6bD9XwJR1zYAq5",
        "https://drive.google.com/uc?export=view&id=1dfRSs0BjMiXKFI4pluvi7pMKW467s5MQ",
        "https://drive.google.com/uc?export=view&id=1_BnmumkHSgvb52Q2WSzeaLaN5OY25_BZ",
        "https://drive.google.com/uc?export=view&id=1VvAgehftFcbgfMCXXrQ7b8tJiBJpczrl",
        "https://drive.google.com/uc?export=view&id=1EQFGvE0KBRvikwBcY-vzMAHxN9_l5UC3",
        "https://drive.google.com/uc?export=view&id=1rFJy2hRQxpoqC4v0cjfCnEYzQ3_Pfg4I",
        "https://drive.google.com/uc?export=view&id=1Hj0x16wRE9p1HKHBd_f7lmuU8H3x5G9s",
        "https://drive.google.com/uc?export=view&id=1HuvPh-rcPfpZbIshComYyQBSuLq66N2L",
        "https://drive.google.com/uc?export=view&id=1PoQL9uRZmAWRchGHa0cWigYhecVv0LX3",
        "https://drive.google.com/uc?export=view&id=1HO5XYAGzBZ9XiDVa0j5S82s31dBoLsXW",
        "https://drive.google.com/uc?export=view&id=1debXmEkqbMc90mUiMCXKFAFqkaruDtVv",
        "https://drive.google.com/uc?export=view&id=17Ec_HDubmMD4v13Hd4xg0Bp19t8zDHPD",
        "https://drive.google.com/uc?export=view&id=1_ZUoy6n8_pL5lI7iWHVU17pcdmd1OKUl",
        "https://drive.google.com/uc?export=view&id=1chH4Ykv6-yfM-Zg9Qe1VU4KtBGweHneU",
        "https://drive.google.com/uc?export=view&id=1gHn_Qu9N-fahwtXkVfZfuHpXjf5gUCDT",
        "https://drive.google.com/uc?export=view&id=1_ga069Zy0JZExhaclkcNZHkDsaHKiDNf",
        "https://drive.google.com/uc?export=view&id=1h9i8zxq8MTeyQovBL8ztIOcpcOOUB2jo",
        "https://drive.google.com/uc?export=view&id=1r-d0gPCHn6cEQb70YPiSCifB9q3OSCWj",
        "https://drive.google.com/uc?export=view&id=1DoDAEgPCQSvA7hxh-InwWAINe5oYsR60",
        "https://drive.google.com/uc?export=view&id=1RNA9Reg6EkvXzXB8HVzlGXALtCJ5cqzD",
        "https://drive.google.com/uc?export=view&id=15bGwYV3FSBkXi5GJskpuXT7iyMq0i1mP",
    ]
    data_list = [
        {"nama": "Arini Puteri Elandra", "jabatan": "Kepala Departemen Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "ka arini terlihat tegas, tapi baikk humoris", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Nabyla Sharfina", "jabatan": "Sekretaris Departemen Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "ka nabyla baik, maniess,ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Khoirul Muttoharoh", "jabatan": "Kepala Divisi Hubungan Luar", "nim": "1234500", "umur": "-", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Main", "sosmed": "@khoirul_muttoharoh", "kesan": "kakanya baik dan imoett", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Ahmad Rizky", "jabatan": "Staf Ahli Hubungan Luar", "nim": "123450050", "umur": "21 Tahun ini Alhamdulillah", "asal": "Tangerang Selatan", "alamat": "GH", "hobbi": "Ngga ngapa ngapain", "sosmed": "@ahmad.rizky__", "kesan": "bang ahmad kerenn, baik, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Adinda Deswita Maharani", "jabatan": "Staf Hubungan Luar", "nim": "124450083", "umur": "10", "asal": "Lampung", "alamat": "Sukabumi", "hobbi": "Jadi idol", "sosmed": "@adindaadma", "kesan": "kakaknya asik,baik,ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Ahmad Bimo Akbar Arkana", "jabatan": "Staf Hubungan Luar", "nim": "124450113", "umur": "-", "asal": "Tanggamus", "alamat": "Bandar lampung", "hobbi": "Lihat lihat perumahan", "sosmed": "@bimo_arkana", "kesan": "abangnya kerenn, baik", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Alfaya Abiyyi", "jabatan": "Staf Hubungan Luar", "nim": "124450006", "umur": "nelson piquet", "asal": "Balam", "alamat": "Balam", "hobbi": "Makan yang manis biar manis", "sosmed": "@alfabiyi", "kesan": "abangnya baik, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Asri Meilani", "jabatan": "Staf Hubungan Luar", "nim": "124450010", "umur": "20", "asal": "Lampung barat", "alamat": "Korpri raya", "hobbi": "Nonton film", "sosmed": "@asrmeilani", "kesan": "ka asri,baik, ramah,lucuu", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Bima Ekayasa", "jabatan": "Staf Hubungan Luar", "nim": "124450106", "umur": "-", "asal": "Lampung", "alamat": "Bandar lampung", "hobbi": "Berlaku humoris dan manis", "sosmed": "@bimayasa_", "kesan": "bang bima kerenn, baik", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Indah Khairunnisa", "jabatan": "Staf Hubungan Luar", "nim": "124450077", "umur": "20", "asal": "Ampera", "alamat": "Disini aja", "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang", "sosmed": "@khaindaa_", "kesan": "kakaknya asik,humoris, lucuu,baik juga", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Riska Erlis Dayu Tiara", "jabatan": "Staf Hubungan Luar", "nim": "124450022", "umur": "20", "asal": "Palembang", "alamat": "Bebas", "hobbi": "Ngefollow-up chat", "sosmed": "@erlsriska", "kesan": "ka rika baikk, maniesss", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Yollanda Agustina", "jabatan": "Staf Hubungan Luar", "nim": "124450024", "umur": "-", "asal": "Kerangka bawang sebelah barat", "alamat": "Kayu mulya", "hobbi": "Tanya bang henry", "sosmed": "@yollanda_agustina16", "kesan": "ka yoland baikk, humoriss", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Aditya Taufiqurrohman", "jabatan": "Kepala Divisi Pengabdian Masyarakat", "nim": "123450032", "umur": "-", "asal": "Tetangga kadep", "alamat": "Belwis", "hobbi": "Memancing keributan", "sosmed": "@adityatfq", "kesan": "abangnya baikk, ramah,terlihat lucu", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Fathya Intami Gusda", "jabatan": "Staf Ahli Pengabdian Masyarakat", "nim": "123450095", "umur": "-", "asal": "Tangsel", "alamat": "Sukarame", "hobbi": "Baca wattpad", "sosmed": "@fatthyaa_", "kesan": "kakanya baikkk, cantik maniess", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Tarisya Hidayatul Rahmi", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450052", "umur": "-", "asal": "Luhak tanah data", "alamat": "gerbar", "hobbi": "Jadi orang baik", "sosmed": "-", "kesan": "kakaknya baikk, lucuuu", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Ashila Islamisahfa Vanisha", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450028", "umur": "20", "asal": "Sini", "alamat": "Jauh pokoknya", "hobbi": "Tidur", "sosmed": "@kshigf", "kesan": "ka ashila baikk, ramah, imoet", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Danil N Fadillah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450103", "umur": "-", "asal": "Karawang", "alamat": "belakang polda", "hobbi": "Ngasi makan ikan cupang", "sosmed": "@d4niel_fdlh", "kesan": "bang daniel baikk, asik jugaa", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Favian Arkaanda", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450021", "umur": "-", "asal": "Swiss", "alamat": "Tanya bapas", "hobbi": "Ngesen kanan", "sosmed": "@fvnnn05", "kesan": "abangnya kerenn, baik, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Muhammad Fathiy Zumar Yazid", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450081", "umur": "20", "asal": "Situlah", "alamat": "Pohon mulya", "hobbi": "Nyari hobi", "sosmed": "@zydddddd__", "kesan": "abamgnya bisa tegas, tapi baik dan asik", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Muhammad Rizaldi", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450093", "umur": "masih mudalah", "asal": "Rahim ibu", "alamat": "Pasar lantai 3.5", "hobbi": "Gambarr", "sosmed": "@jaldii._", "kesan": "bang ajldi asikk,keren jadi mc pplk", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Saskia Nova Magdalena", "jabatan": "Staf Pengabdian Masyarakat", "nim": "124450074", "umur": "20", "asal": "Banyak begal", "alamat": "Pinggir jalan", "hobbi": "Nonton Tinkerbell", "sosmed": "@snova.19", "kesan": "kaka saskii lucu, baik, ramah sekalii", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Selma Siti Aisyah", "jabatan": "Staf Pengabdian Masyarakat", "nim": "123450044", "umur": "20", "asal": "Lampung", "alamat": "Balam", "hobbi": "Jalan jalan", "sosmed": "@selmasiti_aisyah", "kesan": "Ka selmaa baikk humoris", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"}
   ] 
    display_images_with_data(gambar_urls, data_list, key="eksternal")

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1KlKkrnmmZ_9dS_wCGgkRzTY5pxYZVCIY",
                   "https://drive.google.com/uc?export=view&id=1R9QFp-9tbJqTDI986iIrrUhq3unlXla9",
                   "https://drive.google.com/uc?export=view&id=1736RbGf88-66Px7ZJ64OwLk361cfs8ww",
                   "https://drive.google.com/uc?export=view&id=1czhydq4Tm-hbi4zH2mHEKJVfc2pbAXim",
                   "https://drive.google.com/uc?export=view&id=1ZR5m-RtT2JjAk3kV1dfbxs5Ulmd7tXgu",
                   "https://drive.google.com/uc?export=view&id=1RareLD4cr8a-vm_m6cFKGzEZtDVrroel",
                   "https://drive.google.com/uc?export=view&id=19Cb8nwxFzLjZEglEbpxYYFjCpx7h-Jxr",
                   "https://drive.google.com/uc?export=view&id=1qJcyKcJ4sw1ogRJFI6-FoRkHmYqF19EX",
                   "https://drive.google.com/uc?export=view&id=1mDgxoklSY1hnEjNfJVdoQhR5SecKHmME",
                   "https://drive.google.com/uc?export=view&id=193Xq42QzoIZveK1GvbQkWi0lmEZJ792K",
                   "https://drive.google.com/uc?export=view&id=1784UFSVcpYaM89irHYxPKAtc2UTW9Src",
                   "https://drive.google.com/uc?export=view&id=1DxmqrliHExnWCs_ULR8rVlSSDhU1eVlb",
                   "https://drive.google.com/uc?export=view&id=1RctflSRm9ZUscuR2PAIoCS69hsQXGlVx",
                   "https://drive.google.com/uc?export=view&id=1eQ6tLmn56Jj12XzFELmoQGM0FVG4-_2J",
                   "https://drive.google.com/uc?export=view&id=1unAXyNHdCIP3XctzGqlpny75iKPi2FDF",
                   "https://drive.google.com/uc?export=view&id=1GJSQrrgENRo_oQgJWii7WtHhs2dI5CSp",
                   ]
    data_list = [
        {"nama": "Haikal Fransisko Simbolon", "jabatan": "Kepala Departemen Internal", "nim": "123450106", "umur": "20", "asal": "Jambi", "alamat": "Way Halim", "hobbi": "Ngeledek Orang", "sosmed": "@haikalsbln", "kesan": "bang haikal kerenn, baik, enak diajak bicaranya", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Kharisma Mustika Sari", "jabatan": "Sekretaris Departemen Internal", "nim": "123450034", "umur": "21", "asal": "Way Kanan", "alamat": "Untung Senopati", "hobbi": "Suka Nolong Orang", "sosmed": "@rismaa.mustika_", "kesan": "Kak Kharisma lucuu, imutt, baikk, dan juga ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Hanna Gresia Sinaga", "jabatan": "Kepala Divisi Keharmonisasian", "nim": "123450038", "umur": "21", "asal": "Sumatera Utara, kisaran city", "alamat": "Sukarame", "hobbi": "Ngabarin Orang Tua", "sosmed": "@hanna_g_sinaga", "kesan": "ka hanna baikk full senyum teruss", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Ahmad Farhan Ghani", "jabatan": "Staf Ahli Keharmonisasian", "nim": "123450121", "umur": "21", "asal": "Kemiling", "alamat": "Kemiling", "hobbi": "Supporteran", "sosmed": "@farhanghani", "kesan": "bang farhan baikk, keren, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Aisyah Khairun Nisa", "jabatan": "Staf Keharmonisasian", "nim": "124450096", "umur": "18", "asal": "Indragiri", "alamat": "Samping Makam Perwira 2", "hobbi": "Nyicipin Makanan", "sosmed": "@aisyahkhair._", "kesan": "ka aisyah baikk dan ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Cerine Sihotang", "jabatan": "Staf Keharmonisasian", "nim": "124450049", "umur": "20", "asal": "Medan", "alamat": "Belwis", "hobbi": "Suka Ngoding pakai R", "sosmed": "@cerine_ipynb", "kesan": "ka cerine baikk imutt humoris", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Jaya Saputra Tamba", "jabatan": "Staf Keharmonisasian", "nim": "124450094", "umur": "18", "asal": "Medan", "alamat": "Pemda", "hobbi": "Mencari Nafkah", "sosmed": "@jay.saputra.mb", "kesan": "bang jaya kerenn,baik dan asikk", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Najla Nursyifa", "jabatan": "Staf Keharmonisasian", "nim": "124450051", "umur": "20", "asal": "Sumatra Barat", "alamat": "Belwis", "hobbi": "Nonton ASMR", "sosmed": "@njlanursyifa", "kesan": "ka najla baikk dan ramah sekalii", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Rozak Ramdani", "jabatan": "Staf Keharmonisasian", "nim": "124450100", "umur": "19", "asal": "Kalianda, Lampung Selatan", "alamat": "Korpri Raya", "hobbi": "Berantemin Kucing", "sosmed": "@rozakrabbani__", "kesan": "bang rozak baikk murah senyumm", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Teresa Christiani Purba", "jabatan": "Staf Keharmonisasian", "nim": "124450046", "umur": "19", "asal": "Riau", "alamat": "Belwis", "hobbi": "Masak", "sosmed": "@kristiani8872", "kesan": "ka teresaa baik sekalii dan sabar", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Muhammad Hanif Dzaky Arifin", "jabatan": "Kepala Divisi Kerohanian", "nim": "123450064", "umur": "21", "asal": "Padang", "alamat": "Way Kandis", "hobbi": "Nonton F1 & MotoGP", "sosmed": "@hnfdzky_", "kesan": "abangnya kerenn baik, lucuu", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Audina Fitria", "jabatan": "Staf Kerohanian", "nim": "124450038", "umur": "20", "asal": "Sumatra Barat", "alamat": "Sukarame", "hobbi": "Masak", "sosmed": "@audinaf_03", "kesan": "kakanya baikkk dan ramah sekalii", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Cika Adelia Br Marbun", "jabatan": "Staf Kerohanian", "nim": "124450107", "umur": "20", "asal": "Bagan Batu, Riau", "alamat": "Belwis", "hobbi": "Dengerin Musik", "sosmed": "@cikamrbn", "kesan": "ka cikaa baik sekalii, ramaahh murah senyum ", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Gustin H Tampubolon", "jabatan": "Staf Kerohanian", "nim": "124450068", "umur": "21", "asal": "Sumatera Utara", "alamat": "Airan", "hobbi": "Nonton", "sosmed": "@gustinhaleluya", "kesan": "ka gustinn baik dan ramahhh", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Muhammad Harvinsyah", "jabatan": "Staf Kerohanian", "nim": "124450128", "umur": "20", "asal": "Sumatera Selatan", "alamat": "Belwis", "hobbi": "Ngadu Ikan Cupang", "sosmed": "@muhvinz_", "kesan": "bang harvin agak pendiam yah, tapi baikk koo", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Rafa Sabina Fahimah", "jabatan": "Staf Kerohanian", "nim": "124450036", "umur": "20", "asal": "Natar", "alamat": "Natar", "hobbi": "Nonton Drakor", "sosmed": "@snasaa._", "kesan": "ka binaa baikk imut kalemmm", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"}
       
    ]
    display_images_with_data(gambar_urls, data_list, key="internal")

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=192FNfcYuc5q9OsvORkkWWordUqZSqapl",
        "https://drive.google.com/uc?export=view&id=1pclsgM1sJtOcQLA1-DWX1mjKbuw0u4LE",
        "https://drive.google.com/uc?export=view&id=1aR1jv-4z698LHJzCXtSYfip_IEnj83pM",
        "https://drive.google.com/uc?export=view&id=1pJ1l5lKpaB5qaYd99mHBanldCHu6i_wX",
        "https://drive.google.com/uc?export=view&id=1w8q9B9qMhdESsjqIYa0ET0tlrNDJjZ9f",
        "https://drive.google.com/uc?export=view&id=1XioMqKOay16dTBS7ocrfioj9IChE31dK",
        "https://drive.google.com/uc?export=view&id=1qs7jkIZ2XlmG2hqm2ubP4h-5EV4Z67Ft",
        "https://drive.google.com/uc?export=view&id=1CSQKtNQ5GDGDmAji4EJASXHZMh-YWsH8",
        "https://drive.google.com/uc?export=view&id=1whS3EDf9omJIiUUO4oiUVNsNPpP8nvqJ",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1OsZsT1gdVWiL-nRavT_bG7m_CzOyj_Ot",
        "https://drive.google.com/uc?export=view&id=1R-pUvNb3vBVWHkIeeRMEXyD9H65j7b0h",
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Staf SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "bang ihsan lucuu, humoris, kerenlah pokoknya ", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Staf SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "kakany baikk, lucu banget ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Afifah Fauziah", "jabatan": "Staf SSD", "nim": "12345002", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "ka afifah baikk kalem", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Staf SSD", "nim": "1234500", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@hasan.ramadhan08", "kesan": "bang hasann kerenn, baik ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Layina Ropiqo", "jabatan": "Staf SSD", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "ka layinaa baik ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Moch. Iqbal Az-Zahir", "jabatan": "Staf Kemitraan", "nim": "122450052", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@iqbalazzahir_", "kesan": "bang iqbal kerenn, baik dan ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Talitha Justine", "jabatan": "Staf SSD", "nim": "122450076", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "kakanya baik dan kerenn, imoett", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Anadia Carana", "jabatan": "Staf SSD", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "kakanya kereeenn, baik ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Abdillah Fikri Al pome", "jabatan": "Staf SSD", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@ssd", "kesan": "abangnya kereenn, baikk", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Staf SSD", "nim": "124450008", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@dhal_setiawan", "kesan": "bang afdhal baikkk imoed kerenlah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Anggun Nita", "jabatan": "Staf SSD", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa","kesan" :"kaka anggun baikk dan ramah sekalii", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Della Anisa Fitri", "jabatan": "Staf SSD", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "ka dellaa cantik baik, humoris", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
    ]
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=181RDGn_iiBENpZJ3iZS9nr3yjrYWps9m",
        "https://drive.google.com/uc?export=view&id=1ov6ukwiBHW2Qjmuh-tIghJCrBfa6I9gN",
        "https://drive.google.com/uc?export=view&id=13UhbqTV9aQt0v7e0cbzGGmVwEeGMHhfp",
        "https://drive.google.com/uc?export=view&id=1l7bYUZYJ-Y8lUzI1Qy6m6x7qlvmTNk7d",
        "https://drive.google.com/uc?export=view&id=16Iol9OOCg7Os0lLjzrel6mePSUns7U9Z",
        "https://drive.google.com/uc?export=view&id=112xLxPZvc6k6KyfJ45AjEtYtq-GCz77O",
        "https://drive.google.com/uc?export=view&id=1VRT1vrrPRgDmctNb1WRQDdx70t81PiBM",
        "https://drive.google.com/uc?export=view&id=1zuSoxDmbkZVw_1fsd_xgA0fd0Zy-ucxy",
        "https://drive.google.com/uc?export=view&id=1ahGBJGBoV8jHfCXMc38IM9yCtURp46ox",
        "https://drive.google.com/uc?export=view&id=1BKnHIuctPE7U52BMiaCe-82R717hDqN4",
        "https://drive.google.com/uc?export=view&id=1LFrxdbHgoSdfY7DyjS9y7gOyIo5XPpC3",
        "https://drive.google.com/uc?export=view&id=1i6ga_nRectbsFAejWQvglEclL3Vqt3go",
        "https://drive.google.com/uc?export=view&id=1S333-oDtAWEbSJpGwmC5uhA4zygR-8KA",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1fF9FEg710knxXzQ1Ws8ddLIHsdQgBFB3",
        "https://drive.google.com/uc?export=view&id=1jOyXAqVy64N9UomdGIacImSIpP7tlQ4v",
        "https://drive.google.com/uc?export=view&id=1d89zyNcITNAjpI6ASmPwVBBd1EA6__CW",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
    ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Staf Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "ka nayla cantikk manies baik, dan ramah sekalii", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Donna Maya Puspita", "jabatan": "Staf Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kak Donna asik, lucuu, dan juga baikk", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Labo John Noel Napitupulu", "jabatan": "Staf Medkraf", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "bang labo baikk kerenn", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Anash Tasya Ausyaqila", "jabatan": "Staf Medkraf", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "kak Anash lucuu, imutt, baikk, dan jugaa ramahh", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Felisya Nabila Putri Nugroho", "jabatan": "Staf Medkraf", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Ka felii cantik maniesss dan baik hati", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Muhammad Razan Maulana Pratama", "jabatan": "Staf Medkraf", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "bang razan baikk dan ramah sekalii kerenn", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Sania Dwi Ayu Lestari", "jabatan": "Staf Medkraf", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Ka saniii lucuu cantikk baik sekalii", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Allisha", "jabatan": "Staf Medkraf", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "ka alishaaa ramah sekalii humoris", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Alya Ramadhanti", "jabatan": "Staf Medkraf", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "ka alyaa lucuu imutt, baikk", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Bunga Clarisa Sefa", "jabatan": "Staf Medkraf", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "ka bungaa cantik baik dan ramah sekalii", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Difanya Husakina", "jabatan": "Staf Medkraf", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "ka difanyaa maniess baik dan humble", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Nazlah Auliya", "jabatan": "Staf Medkraf", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Ka nazlah imuttt baik sekaliii dan ramah", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Raihana Adelia Putri", "jabatan": "Staf Medkraf", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "Ka raihanaa imutt maniss ramah sekalii dan baik hati", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Daffa Kharisma Adzana", "jabatan": "Staf Visual Design", "nim": "124450061", "umur": "21", "asal": "Surabaya", "alamat": "Sukarame", "hobbi": "-", "sosmed": "@daffascript", "kesan": "Bang dafa baik dan ramah sekalii", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "bang edsell kerenn baik dan ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Staf Medkraf", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "ka luciaa cantik manis baik sekalii", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Staf Medkraf", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Ka shafaa cantikkk calm baik sekalii", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Zannuba Arifah Ilman", "jabatan": "Staf Visual Design", "nim": "124450112", "umur": "18", "asal": "Lampung Timur", "alamat": "Rajabasa", "hobbi": "Begong", "sosmed": "@xifasky", "kesan": "ka zannuba baik maniess ramah sekalii", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"}
        ]
    display_images_with_data(gambar_urls, data_list, key="medkraf")

elif menu == "Departemen MINBAK":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1iX48Jv1O_PM3mDsHjpdResGZFrOLU1m3",
        "https://drive.google.com/uc?export=view&id=10MsM9aUHFy1_XAPIQ89kZy3aIzMXC86_",
        "https://drive.google.com/uc?export=view&id=1eD7jvI3pmGdRMkeWkeThL5cchBR3GRr5",
        "https://drive.google.com/uc?export=view&id=1P2Bs_jCfh43nggKeymP44EIBKnRiYltw",
        "https://drive.google.com/uc?export=view&id=1I2soGlW1H5BOnpRXvGEQGGODvUThLYzg",
        "https://drive.google.com/uc?export=view&id=15d6ev0lrTz9BG_6Ue6ZQO3mCp6pFgD_Z",
        "https://drive.google.com/uc?export=view&id=11Uu1WEZfXFqTZAuJOl4g3_Mn1VrZOfo7",
        "https://drive.google.com/uc?export=view&id=1_83Im8l8gnYGhnDAerTMzLFlxLH-zJGc",
        "https://drive.google.com/uc?export=view&id=1lYANfo6kNAJwi0L3A0QgdlP8k8yeFP8Q",
        "https://drive.google.com/uc?export=view&id=1EFb899j5VB6FzA1mkqyOLEAIW2wTsnrN",
        "https://drive.google.com/uc?export=view&id=13KTlv-c0maoAcabcw3MZSuYTv7WTdHAT",
        "https://drive.google.com/uc?export=view&id=1SoebLwSqbcoiwuJLqJCkg6AU_4SB7DwV",
        "https://drive.google.com/uc?export=view&id=13ls7-19xz5hXX70m6AiwoJ5FullZy8CO",
        "https://drive.google.com/uc?export=view&id=1KVaJFMyBi_Gz0jh2CJW8cedX_KsH30GC",
        "https://drive.google.com/uc?export=view&id=1bBxCM7eV62Vkg0bQ2vVhhwkfOddA2lSd"
    ]
    data_list = [
        {"nama": "Kevin Antonio Junior", "jabatan": "Kepala Departemen Minbak", "nim": "123450109", "umur": "21", "asal": "Bandar Lampung", "alamat": "Panjang, Bandar Lampung", "hobbi": "Balap", "sosmed": "@kevinaj__", "kesan": "bang kevin kerenn abies baik dan juga ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Gusti Putu Ferazka Dhiyamika", "jabatan": "Sekretaris Departemen Minbak", "nim": "123450046", "umur": "21", "asal": "Lampung Utara", "alamat": "Way Halim", "hobbi": "Baca", "sosmed": "@ferazkaa", "kesan": "ka ferazka baik sekalii, ramah dan asikk", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Ari Aristo Muthahari Parisi", "jabatan": "Kepala Divisi Manajemen Aktivitas dan Kompetisi", "nim": "123450088", "umur": "21", "asal": "Lampung Timur", "alamat": "Gang Sakum, Belwis", "hobbi": "Nonton F1", "sosmed": "@ali_parisi3", "kesan": "bang ali baik, ramahh, keren ", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Ayu Andriani Parlina Wati", "jabatan": "Staf Ahli Manajemen Aktivitas dan Kompetisi", "nim": "124450058", "umur": "20", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Belajar", "sosmed": "@aayuandrianni_", "kesan": "ka ayuu baik, humoris", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Dafa Elpriza", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450131", "umur": "21", "asal": "Bekasi", "alamat": "Way Kandis", "hobbi": "Nemenin Bryan live TikTok", "sosmed": "@dafaelpriza_", "kesan": "bang dafa baik apalagi pas ngasprak", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Juwita Sari", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450066", "umur": "19", "asal": "Lampung Barat", "alamat": "Pemda", "hobbi": "Lihat bulan", "sosmed": "@ju.juwitaaa_", "kesan": "ka juwitaa baik dan ramah ", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Muhammad Afdal Lutfi", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450047", "umur": "19", "asal": "Lampung Tengah", "alamat": "Jl Pulau Damar", "hobbi": "Taptap layar kalo Bryan live", "sosmed": "@afdall.03", "kesan": "bang afdal lucuu banget, baikk", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Salsabila Nazwa Putri", "jabatan": "Staf Manajemen Aktivitas dan Kompetisi", "nim": "124450002", "umur": "20", "asal": "Metro", "alamat": "Korpri", "hobbi": "Nongkrong di Kopken", "sosmed": "@slbnzw_", "kesan": "kaka salsa baikk dan ramahhh", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Muhammad Ridwan", "jabatan": "Kepala Divisi Manajemen Minat dan Bakat", "nim": "123450091", "umur": "21", "asal": "Lampung Tengah", "alamat": "Belwis", "hobbi": "Nganterin Datasena ke gedung F", "sosmed": "@mridwaan_22", "kesan": "bang ridwan kren dan baikk", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Andra Ilham Bintang", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450060", "umur": "18", "asal": "Sumatera Selatan", "alamat": "Kota Baru", "hobbi": "Ngitungin kelopak bunga di kebun", "sosmed": "@andra.lhm", "kesan": "bang andra baik sekalii dan keren", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Bryan Paskah Telaumbanua", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450003", "umur": "22", "asal": "Nias", "alamat": "Belwis", "hobbi": "Live TikTok", "sosmed": "@bryantel_", "kesan": "bang bryan imut baik,ramahh", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Ghiyats Thabularasa Meardhy", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450067", "umur": "17", "asal": "Bekasi", "alamat": "Korpri", "hobbi": "Ngegift live Bryan", "sosmed": "@meardhy_ghiyats", "kesan": "bang gyatss keren dan baikk", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Indah Julia Mawar Pratiwi", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450055", "umur": "20", "asal": "Pringsewu", "alamat": "Airan", "hobbi": "Bengong", "sosmed": "@indahjuliaa", "kesan": "ka indah baikk dan ramah jugaa", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Jacinda Kesya Alvara", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450023", "umur": "18", "asal": "Kalimantan Barat", "alamat": "Korpri", "hobbi": "Nyapu depan gacoan", "sosmed": "@cacalvra", "kesan": "ka caca cantikk, imoett", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Manajemen Minat dan Bakat", "nim": "124450089", "umur": "20", "asal": "Padang", "alamat": "Kota Baru", "hobbi": "Bangun pagi", "sosmed": "@muhammdrafka_", "kesan": "abangnya kerenn cool", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"}
    ]
    display_images_with_data(gambar_urls, data_list, key="minbak")
