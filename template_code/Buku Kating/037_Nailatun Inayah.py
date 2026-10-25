from utils import (
    setup_buku_kating_page,
    streamlit_menu,
    display_images_with_data,
)

setup_buku_kating_page()
menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1MF33XGfLl-7sYejlox9Dh1lDBbKNyhBH",
        "https://drive.google.com/uc?export=view&id=1Y_IZ9qqnKXlG55F2UtC_SukySaPw66xg",
        "https://drive.google.com/uc?export=view&id=1t1k47hpLRxpzZm-KAvKzmLXB1YGVq3l-",
        "https://drive.google.com/uc?export=view&id=1zriJA0JQx7GLlS_xuNeyzcUiFPkJlrYe",
        "https://drive.google.com/uc?export=view&id=1oQ9vqAU1oiwHts0FKNy_Wz5m3KMIJINQ",
        "https://drive.google.com/uc?export=view&id=18oFNquLlj00f1LcRm3-axyFNfdtr-T3u"
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abang kahim kaciww, bijakk, humble", "pesan": "Semangat TA nya banggg, semoga lancar dan sukses selaluu"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Bang aqil vibesnya religius banget, lucuu, humoris", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selaluu"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakk efi cantikk nan baik hatii makasii banyak bimbingannyaa kakk, selalu sabar ngajarin adik adik magang yg amatir ini.", "pesan": "Semangat TA nya kakk, semoga lancar dan sukses selaluu"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Bang qois soft spoken bangett, makasii banyak bimbinganyaa bangg", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selaluu"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kak hafsa humblee, asik deh sharing session bareng kak hafsa ", "pesan": "Semangat TA nya kakk, semoga lancar dan sukses selaluu"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kak lulu cantikk nan baik hatii, penyabarr, makasii banyakk bimbingan ads nya kakk", "pesan": "Semangat Ta nya kakk, semoga lancar dan sukses selaluu"}
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1C10gN2PYRz4ZRpj3sonblSyJFitJrkFg",
    "https://drive.google.com/uc?export=view&id=17IbT5INbX6KtpbzMEgunt9nue_0rxePc",
    "https://drive.google.com/uc?export=view&id=19X9lPgcp4N5SXWi2alhA0rXEk9HLuaxF",
    "https://drive.google.com/uc?export=view&id=1wnsFRcimuIzXstWSB-KhszQ1IZs-wy8R",
    "https://drive.google.com/uc?export=view&id=1KG5fXe6Irike8U5xH6kw5sMk60bdZk7B",
    "https://drive.google.com/uc?export=view&id=1CArdPFmSdiv_cb5lW0JBHCYW8WVVfc58",
    "https://drive.google.com/uc?export=view&id=1TjYMtcuOFAp3RoolaqYoZknxtirdaXEd",
    "https://drive.google.com/uc?export=view&id=1L-MBzn4QhgjZgMI8LbgVPUhPQpu2-pt5",
    "https://drive.google.com/uc?export=view&id=13n6E8YuWbRV_G7udmfvu5LJt_IgeEDuU",
    "https://drive.google.com/uc?export=view&id=19UveBU3fOGPrH2ObqD_Zk1a1tGVRL6E9",
    "https://drive.google.com/uc?export=view&id=19AfRxOVnFY9hqfcFa2x-hV-mbQ-WXaBi",
    "https://drive.google.com/uc?export=view&id=1V_czWPQPHVMdeXjNa0Q7CIPSaqn5XPbl",
    "https://drive.google.com/uc?export=view&id=1WDpyvup3UTsi4g6DHO6UUyVor1AqUrat"

    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik ", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "Bang ridho keren, asik banget", "pesan": "Semangat TA nya bangg, semoga lancar dansukses selalu bangg"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim", "sosmed": "@j__eesie", "kesan": "Kak Juee baik banget, suka kasi kata kata affirmasi buat semangatin adik asuh tpb <3333", "pesan": "Kak Juee semangat TA nya, semoga lancar dan sukses selalu kak <3"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Bang dharu mapress kereennn,, aduhh when yahh", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Gh Mikael Niko Antoni Setiadi", "jabatan": "Staf Komisi I", "nim": "124450025", "umur": "20", "asal": "Lamtim", "alamat": "Jati agung", "hobbi": "Main mcgg", "sosmed": "@me._kael", "kesan": "Santai dan seru, asyik diajak main bareng.", "pesan": "Tetap semangat, dan semoga rank-nya naik terus tanpa lupa kuliah."},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Kak Syarifa baikk, ramah, murah senyumm", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II", "nim": "124450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum kopi", "sosmed": "@givarooo", "kesan": "Bang Givaro keren, seruuu, baik", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "Kak nisa baikk, ramah, murah senyum", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "city earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain_", "kesan": "Kak Hani baikk, ramah, coer dengan bias yg sama, btw aku juga suka au kak", "pesan": "Kak Hani semangat kuliahnya, semoga lancar dan sukses selalu kakk"},
        {"nama": "Jeremia Halim", "jabatan": "Staf Komisi II", "nim": "124450101", "umur": "20", "asal": "Tangerang", "alamat": "Teluk Betung", "hobbi": "Nyanyi, olahraga", "sosmed": "@jeremia_hm", "kesan": "Ramah dan seru, enak diajak ngobrol.", "pesan": "Tetap semangat, dan semoga suaranya makin merdu serta badannya selalu sehat."},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III", "nim": "123450073", "umur": "21", "asal": "Sumut", "alamat": "Kota baru", "hobbi": "Merajut", "sosmed": "@monica_tjg", "kesan": "Sabar dan telaten, orangnya menyenangkan.", "pesan": "Tetap semangat dan semoga rajutannya makin bagus."},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "gym / koleksi figur", "sosmed": "@nagatsee", "kesan": "Bang Jona keren, asikk, ramah", "pesan": "Semangat kuliah nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "Kak Sekar baikk, ternyata setelah kenal asikk, ramah, murah senyum", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nahaysh", "kesan": "Kak wan baikk, ramah, murah senyum", "pesan": "Semangat TA nya kakk, semoga lancar dan sukses selalu kakk"}

    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=11VzVt8f9Qx4fFk1skcRHAOywZRWCXlAM",
        "https://drive.google.com/uc?export=view&id=1pz2q8IMx_DkVHCrt48A_8R2ZKDaVTs04",
        "https://drive.google.com/uc?export=view&id=1ifwRBz_hKORHzsfGGIwIPNjmI4vEs0S6",
        "https://drive.google.com/uc?export=view&id=17VznsQr9AORlXVIRaCIZ2wmlDl9ZL8Y5",
        "https://drive.google.com/uc?export=view&id=1uOYFvMB5TWhmw7_Fj7YuPz3tnVvh4ogP",
        "https://drive.google.com/uc?export=view&id=1DQJecL12ZqLClrXPhBhPj_uEHDxO4dSM",
        "https://drive.google.com/uc?export=view&id=1A2_ewNtso7qwtbE8ffNisYMTlWAGDJbv",
        "https://drive.google.com/uc?export=view&id=1pcCONjNIecw6rIWKf4tyuuvM-OipZ70_",
        "https://drive.google.com/uc?export=view&id=1PEn0CzWfyMbTY7wdAdXPKN37-ScAZsxn",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Kakak vibesnya BA wardah bangett kakk, kerennn, kritiss", "pesan": "kakak semangat TA nya kakk, semoga "},
        {"nama": "Helmy Surya Pratama", "jabatan": "Kepala Biro Aspirasi dan Media Komunikasi ", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya humoriss, isengg, asikk", "pesan": "bang semangat kuliahnya bang, semoga lancar dan sukses selalu bangg"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Pembawaannya tenang, ramah ", "pesan": "Tetap semangat bangg kuliahnya, semoga sukses dan lancarselalu bang"},
        {"nama": "Suci Aulia", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Kak suci baikk, ramah, ceriaa", "Pesan": "Selalu semangat kakk kuliahnya, semoga lancar dan sukses selalu kakk"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Abang kalem, maap bang mirip bapaknya elzard dikitt", "pesan": "Semangat bangg kuliahnya, semoga lancar dan sukses selalu bangg"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Biro Kajian Strategis dan Propaganda", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Kak lia humblee, Open minded, kritis", "pesan": "selalu semangat kak, semoga TA nya lancar dan sukses selalu kakk"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Kak ceriaa bangett, beneran kaya bunga matahari vibesnya", "pesan": "Tetap semgat kuliahnya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Bang hazel ternyata baikk, walaupun agak serem", "pesan": "Semangat kuliahnya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Kepala Biro Kesekretariatan", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Kak nadya cantikk, baik, ramahh", "pesan": "Semangat TA nya kakk, semoga lancar dan sukses selalu kakk"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Staff Biro Kesekretariatan", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Kak dwi baik, ramah, dan ceriaa ", "pesan": "Semangat kuliahnya kakk, semoga lancar dan sukses selalu kakk"}
    ]
    display_images_with_data(gambar_urls, data_list, key="senator")

elif menu == "Departemen PSDA":
    gambar_urls = [
    "https://drive.google.com/uc?export=view&id=14yJr_rGZ2s9lXuNCZaFyVNkrvOGTtUZc",
    "https://drive.google.com/uc?export=view&id=1QkKxp3t2wpV270TJVacUSrxDmtNAcgVf",
    "https://drive.google.com/uc?export=view&id=1mv8xU7Yk6peJ9DI13UC1fE09_wS6XZbu",
    "https://drive.google.com/uc?export=view&id=15LjKUOgMpI_3t7ZHVCUQQ_7HgtN-IwQR",
    "https://drive.google.com/uc?export=view&id=1BzTJyOnonLdkdEh9yQpB8ix1BKUmhd-r",
    "https://drive.google.com/uc?export=view&id=1XySP2PYt_h5_9ihHo2LQj0xiiMKcA_v_",
    "https://drive.google.com/uc?export=view&id=17tkY28AYY7p1x0aYYnvRq-MkUfn_4Ulw",
    "https://drive.google.com/uc?export=view&id=1yd109phc9X7V7xC89sz8e87DijyVjhS1",
    "https://drive.google.com/uc?export=view&id=10VWw0F7VwwLShVvyNQm-BXKGrC-LX1Pi",
    "https://drive.google.com/uc?export=view&id=1TW2WL_oqkH_YtvTFbKgohDzuIj6bF1mE",
    "https://drive.google.com/uc?export=view&id=17HAbsVAUstvYTx3TMJuNGGEnbvVpaWGE",
    "https://drive.google.com/uc?export=view&id=1DwBdY1NqFBZRIHfLnf_dj9ycKHyHoL1L",
    "https://drive.google.com/uc?export=view&id=1PDhuf8I0jUm9TsFMdtDuoGHeNOkJpP1D",
    "https://drive.google.com/uc?export=view&id=1Kox2fLr5u3lJTzuBoz88zB8v4I1tJ6w4",
    "https://drive.google.com/uc?export=view&id=1Gc7LkOdSz3aMx0mSxPYNc4MBoaFYsiWX",
    "https://drive.google.com/uc?export=view&id=1Z-n6ldJuBX_Qta_TOJ252YCJESSumD8S",
    "https://drive.google.com/uc?export=view&id=1iQscJd_L7yhJXYyY0UKmSt7HjVQqc5Ky"

    ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "123450097", "umur": "21", "asal": "Kalianda", "alamat": "Samping kost Haikal", "hobbi": "Naksir cowo cakep", "sosmed": "@arientakhsnl_", "kesan": "Klo liat kak arin senyumnya sekilas mirip Jisoo BP, baikk bangett ternyata", "pesan": "Kak semangat TA nya kakk, semoga lancar dan sukses selaluuu"},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "123450022", "umur": "20", "asal": "Palembang", "alamat": "Pudan Kost", "hobbi": "Pacaran", "sosmed": "@vany.salsabilaa", "kesan": "Kak vany baikkk, kakak mirip temen aku", "pesan": "Kak semnagat TA nya kakk, semoga lancar dan sukses selaluuu"},
        {"nama": "Nobel Nizam Fathirizki", "jabatan": "Kepala Divisi Kaderisasi", "nim": "123450117", "umur": "21", "asal": "Bandar Lampung", "alamat": "Urip", "hobbi": "Sulap", "sosmed": "@nobelnizam", "kesan": "bang nobel kerenn, tegas tapi humble", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
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

    display_images_with_data(gambar_urls, data_list, key="PSDA")

elif menu == "Departemen MIKFES":
    gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1KhXBVqcWPg0oi9XOKiIk_06rzeEL7roZ",
    "https://drive.google.com/uc?export=view&id=1u64R9N6uSAls5jk1XHu0innG_Ja17jkd",
    "https://drive.google.com/uc?export=view&id=11TBExLg2AaV9euzaGGOnH4-wST6jeusr",
    "https://drive.google.com/uc?export=view&id=1mIvC2NA0AcygBbVSlHqH4bYca_L6a2yT",
    "https://drive.google.com/uc?export=view&id=1n5xRq2jpENB0l2nYfqm4JcNJUmfqQGRo",
    "https://drive.google.com/uc?export=view&id=1ID4_KBx8SFYBuyVoqBSHCDj4fNodIfLi",
    "https://drive.google.com/uc?export=view&id=1t8M8zVYUWKjvo3OqaFRvqYPw8EKQ2Sip",
    "https://drive.google.com/uc?export=view&id=14jqgiQwuKU0fIVaWtM3oZGHlcUJgmssZ",
    "https://drive.google.com/uc?export=view&id=1hMEb550iM4ukh5RCLmYNwTCl5jXlgxig",
    "https://drive.google.com/uc?export=view&id=1JkQfT3nEa1zYAfCqEc01TMakBUe1cqgO",
    "https://drive.google.com/uc?export=view&id=1tvhF9OgfiJuxYyAXeZ3FJO0P7F0kgcLr",
    "https://drive.google.com/uc?export=view&id=1UdllnylQP4nN2sRYWfC1YPe38SBjgY9A",
    "https://drive.google.com/uc?export=view&id=1b9ghXDwnBuUNHLgwlJi7-z3vw803Dlcg",
    "https://drive.google.com/uc?export=view&id=1DYXqniFYq4HvcKc0hN1hV2BH1_1fwH7q",
    "https://drive.google.com/uc?export=view&id=1Fk-I4RoNV36d0fyEzYKseOKDS4CbcVat",
    "https://drive.google.com/uc?export=view&id=1HkaSR3bJ1EsZ7qprHYmwFuVBMk97AB_z",
    "https://drive.google.com/uc?export=view&id=1GW_VSLB3uA77pq6ZncQ8ggramti9YhK_",
    "https://drive.google.com/uc?export=view&id=19Zv-X4G3Doley_h8J5iWatUOqHWy2AY-",
    "https://drive.google.com/uc?export=view&id=1jbS8_9bZmARsn1TuzHESMa-4iEUVRnjQ",
    "https://drive.google.com/uc?export=view&id=1SvPgLtCI0AtrERSK3LdjpXqlTGtatS6p",
    "https://drive.google.com/uc?export=view&id=10_-leGbSPHwsdnKD_ppx6_Tw1Nzz0ZhR",
    "https://drive.google.com/uc?export=view&id=1rqSebvDIEAGQa9OXOPs_xwjNS6I6IB8M"

    ]
    data_list = [
        {"nama": "Fabio Banyu Cyto", "jabatan": "Kepala Departemen Mikfes", "nim": "12340104", "umur": "21", "asal": "Bandar Lampung", "alamat": "Kedaton", "hobbi": "Tidur", "sosmed": "@biyokcb", "kesan": "Abangnya kereenn, seruu kalau diajak ngobrol", "pesan": "Bang semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Tanty Widiyastuti", "jabatan": "Sekretaris Departemen Mikfes", "nim": "123450094", "umur": "21", "asal": "Lampung", "alamat": "Airan Raya", "hobbi": "Membaca", "sosmed": "@tvnty_", "kesan": "Kak tanty ceria bangett, kalau liat kak tanty vibesnya warna kuning ceriaa", "pesan": "Kak semangat TA nya kakk, semoga lancar dan sukses selaluuu"},
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

    display_images_with_data(gambar_urls, data_list, key="Mikfes")

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1P_YxveJIz8irx8uuo5PzHpui094Q3X1i",
        "https://drive.google.com/uc?export=view&id=1JtqLMi6pgjU3gEfS3RWZx65SPyYvDcz4",
        "https://drive.google.com/uc?export=view&id=1JNDTXm67tpoFV3AvIc8GpJ9yUcQD7kdL",
        "https://drive.google.com/uc?export=view&id=1VWBxi6veMmh81aHkkIOZwUqOEZvvIKqT",
        "https://drive.google.com/uc?export=view&id=1yi6QkI0WJ2ATXCOKehc4rK69JTHqmCFZ",
        "https://drive.google.com/uc?export=view&id=1FffMm3Kz9BmEf0tT331GfprA48PrpzFR",
        "https://drive.google.com/uc?export=view&id=18PaYPqNuolvh_edOMRJLFcrwZ-OQjrWa",
        "https://drive.google.com/uc?export=view&id=1OXlnGUKEbYXb-kPCxoK7bYqOcM1HYkAT",
        "https://drive.google.com/uc?export=view&id=1Xy2okVZv1rclkiCLERxEQo0fqGo8BlC0",
        "https://drive.google.com/uc?export=view&id=1B1uJFPEXgUkwTH3nfjI9y2hxNGAQccv7",
        "https://drive.google.com/uc?export=view&id=1z_iJogIwD_bmypmmBGJNI5SUCu0LktNI",
        "https://drive.google.com/uc?export=view&id=1mKqxyIYCdS65dDs-CxRslNt8UERoV7GF",
        "https://drive.google.com/uc?export=view&id=1v7PggWxaiOduwFLIk_Mh-_bDuqoItwbL",
        "https://drive.google.com/uc?export=view&id=1VOCDgD-QTYi4TC1XvR3yCW2iwMunThb8",
        "https://drive.google.com/uc?export=view&id=1xMWieEG3oBw01zhBsx1EqWGeMLpsM8__",
        "https://drive.google.com/uc?export=view&id=1Y-lrzJ_Q0Anc9xStNdbaUkobMwgXNj7j",
        "https://drive.google.com/uc?export=view&id=1mdLAaWzAW8BeqNNE9xMXCR_5tIKwHGc-",
        "https://drive.google.com/uc?export=view&id=1uPgiWNrjon2oauwA9tD8Yr8fiRAFAWYx",
        "https://drive.google.com/uc?export=view&id=17kZM4YEVVqjeBVgDY83XtLMGnvYIxxic",
        "https://drive.google.com/uc?export=view&id=1ejVyBOb7tnoO8A9hCYQ6PY3V0mtRCH-f",
        "https://drive.google.com/uc?export=view&id=1davruIwEPjjgf6A8fM0n6jnjpBeTZmGE",
        "https://drive.google.com/uc?export=view&id=1NGN_5qS9Rlq3DjnLrgedc-xDST-21ESL"
    ]
    data_list =[
        {"nama": "Arini Puteri Elandra", "jabatan": "Kepala Departemen Eksternal", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Baikk, ramaahh bangett, fm sama kak arini wktu fg 25 humble bangett", "pesan": "Kakk semangat TA nya kakk, semoga lancar dan sukses selaluuu"},
        {"nama": "Nabyla Sharfina", "jabatan": "Sekretaris Departemen Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jl. Lapas", "hobbi": "Jalan Jalan", "sosmed": "@bylaash", "kesan": "Baikk, ramahh, sabar membimbing adik adik tutorial ale RC", "pesan": "Selalu jadi orang baik"},
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
    "https://drive.google.com/uc?export=view&id=1zcxgDpvlGQPe8-QGO6q3x-WvbUAP9mRn",
    "https://drive.google.com/uc?export=view&id=1NqOhK-BKtXlIKmBXNidWMUwq7nLqAIly",
    "https://drive.google.com/uc?export=view&id=1gs3itM0L3_zfcUTPQB567L3vvtqPren_",
    "https://drive.google.com/uc?export=view&id=1ku1-Q6wTuKC_7qjfBL4ArrE3dIgRiXJd",
    "https://drive.google.com/uc?export=view&id=1M-PsWVbwTEqkKO7i7pdz6QdFf_TVCQdD",
    "https://drive.google.com/uc?export=view&id=1Z-6rhdVSzBhIhTnCncbOoU72xYZu5dPP",
    "https://drive.google.com/uc?export=view&id=10bXWBTh4m7fZQ4Pdv05DwNPXLl-FSCXT",
    "https://drive.google.com/uc?export=view&id=151vfX8BA8qZ6FMefypUVXfbv8HC9jEis",
    "https://drive.google.com/uc?export=view&id=1pmzMCwOe2z2gs3aTEj07wmWFFO5hFaQi",
    "https://drive.google.com/uc?export=view&id=1xeu6xkzOjF4DKavAFDYdo_HuIZvPJma0",
    "https://drive.google.com/uc?export=view&id=154zl57zyHyjpKr54OLkZixOy5KtVY7RD",
    "https://drive.google.com/uc?export=view&id=1TodYRWREUOItYngES2BPVw4LFVc1WLiU",
    "https://drive.google.com/uc?export=view&id=1bhCExK_oiXwhYQm7vZha0rvkRJFBezce",
    "https://drive.google.com/uc?export=view&id=1U4wuhey2aWD7ujBsOoZvKLtc83oxfbN7",
    "https://drive.google.com/uc?export=view&id=1Hh778yI2J1-9JuJzZldRqLtl02FtNh5O",
    "https://drive.google.com/uc?export=view&id=1MF1UB56pv6Wwn9Sii2pzwsAn0qLQ84If"

    
    ]
    data_list = [
        {"nama": "Haikal Fransisko Simbolon", "jabatan": "Kepala Departemen Internal", "nim": "123450106", "umur": "20", "asal": "Jambi", "alamat": "Way Halim", "hobbi": "Ngeledek Orang", "sosmed": "@haikalsbln", "kesan": "abangnya sangat ramah, humoris", "pesan": "Bang semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Kharisma Mustika Sari", "jabatan": "Sekretaris Departemen Internal", "nim": "123450034", "umur": "21", "asal": "Way Kanan", "alamat": "Untung Senopati", "hobbi": "Suka Nolong Orang", "sosmed": "@rismaa.mustika_", "kesan": "Kakak sangat anggun, soft spoken, baikk", "pesan": "Kak semangat TA nya kakk, semoga lancar dan sukses selaluuu"},
        {"nama": "Hanna Gresia Sinaga", "jabatan": "Kepala Divisi Keharmonisasian", "nim": "123450038", "umur": "21", "asal": "Sumatera Utara, kisaran city", "alamat": "Sukarame", "hobbi": "Ngabarin Orang Tua", "sosmed": "@hanna_g_sinaga", "kesan": "Sangat sangat supell, kak hana happy virusnya orang orang", "pesan": "Kak semangat TA nya kakk, semoga lancar dan sukses selaluuu"},
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
        "https://drive.google.com/uc?export=view&id=1jDEG-im2Qsxw0D3QYT7r-wV8ysUte12r",
        "https://drive.google.com/uc?export=view&id=1lWZ_8Z153AibwM01rkt9-o4gJiGTOZ4k",
        "https://drive.google.com/uc?export=view&id=1UwozLsSossrwwhPwtgMh4MUlhlI8qAIH",
        "https://drive.google.com/uc?export=view&id=11O0E8TNxJ3ai9MNPfZimVe-9_4nh2atM",
        "https://drive.google.com/uc?export=view&id=1ha6ULRBaN5h_SWuaNR46_8FNAGd4vcIh",
        "https://drive.google.com/uc?export=view&id=1TKjulrdydxRsXnQ4IlAXqzSDnW5-cqrf",
        "https://drive.google.com/uc?export=view&id=1EeW5h2G4YVF02qFDhJ0KvqzmJUvVqI_6",
        "https://drive.google.com/uc?export=view&id=15QVwAjAw9ikSzi6nY75zW-nT8BDb1Kn4",
        "https://drive.google.com/uc?export=view&id=1WbxOo7eagnmTHU79WClOSTgBBKFiSSeo",
        "https://drive.google.com/uc?export=view&id=1uydEUVLrBeNVIhvroRKcnSMqwNyl30pF",
        "https://drive.google.com/uc?export=view&id=1J08meeDUoQxSv6Th2tbLHWUQnb8D9YOQ",
        "https://drive.google.com/uc?export=view&id=1iWmFuGpmvSshTVO4RGuioSLbOXOWhvSW"
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Kepala Departemen SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Abang kerenn, humoris", "pesan": "Semangat TA nya bangg, semoga lancar dan sukses selalu bangg"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Sekretaris Departemen SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Kakak ramah bangett", "pesan": "Kak semangat TA nya kakk, semoga lancar dan sukses selaluuu"},
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
        "https://drive.google.com/uc?export=view&id=1-ZcGn0wV7AXDQIGv_aX34akJAd6w44hj",
        "https://drive.google.com/uc?export=view&id=17RTVW5kWVLS5ycGaHckvo6XnhKAKJJlH",
        "https://drive.google.com/uc?export=view&id=1xBjaDtComTuqY56rrAv1DOPOGFUsY2sv",
        "https://drive.google.com/uc?export=view&id=1lyOZpqKd1b9nVZstAZA4vLRTz7SeZzna",
        "https://drive.google.com/uc?export=view&id=1okhUMy1D1CzbJJTnpxswVYyNSbQz2TXc",
        "https://drive.google.com/uc?export=view&id=1IbcbkT6CkMCCuhZxDyxzQug0rU_-hNWR",
        "https://drive.google.com/uc?export=view&id=1-D_Tba9L9GLWtdXIVNVZFC2onpcuQzkp",
        "https://drive.google.com/uc?export=view&id=1q6hg0TjVawxMmbitJ_zV5tsq8yetgFjs",
        "https://drive.google.com/uc?export=view&id=11ECoEZWE-LOXHLR-5hE68rIAi-3kGoMv",
        "https://drive.google.com/uc?export=view&id=1ocd1SyELHuUxoTrIwTgqDIdy-Y6jR4gk",
        "https://drive.google.com/uc?export=view&id=1Yu988LBWpC9rq6MA-e4W_gZX7nToSDM4",
        "https://drive.google.com/uc?export=view&id=1LeVLEdGy14_V4FrucsTJj0ge2dzNRI4C",
        "https://drive.google.com/uc?export=view&id=1qh8w2pIV-z9ZMOzUfRTo_ffkBBX3-zIy",
        "https://drive.google.com/uc?export=view&id=1uydEUVLrBeNVIhvroRKcnSMqwNyl30pF",
        "https://drive.google.com/uc?export=view&id=1SbkF-ECFzzfVNMpIfgynXtgLkw_rWZ8w",
        "https://drive.google.com/uc?export=view&id=1VZ6JdtFLH3gMmoy4A0XXoc5TD-X22kI-",
        "https://drive.google.com/uc?export=view&id=18BXJqwqoBCnjDqoM2aojor4MLf8suhWf",
        "https://drive.google.com/uc?export=view&id=15yZfjmkg5Sviilj6FMTdZnYOXOj9OiZp"
    ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Kepala Departemen Medkraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kak nayy kerenn, baikk dan ramahh", "pesan": "Selalu semangatt kak, semoga TA nya lancar dan sukses selalu kak"},
        {"nama": "Donna Maya Puspita", "jabatan": "Sekretaris Departemen Medkraf", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kak dona baikkkk bangett, soft spoken, ramahh, makasii buat tutorial lmd nya kakk<3", "pesan": "Karya tanpa batas!"},
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
        "https://drive.google.com/uc?export=view&id=1mfLGXyKIio_1TC5qM6eRj8pyNJfsjwgT",
        "https://drive.google.com/uc?export=view&id=1PN8JqZ2N6f9qRjOeVOlWdCd4mnNNtI--",
        "https://drive.google.com/uc?export=view&id=1qR9qg7LSvMBVWYqNEZKiLmg7Q1jgqhM3",
        "https://drive.google.com/uc?export=view&id=1oPf8xBDFjHQAEdD9nsmXJA5ywCSsZUSm",
        "https://drive.google.com/uc?export=view&id=16toA9QDn_boIAyu5uVi3OBQLOtjEmtjx",
        "https://drive.google.com/uc?export=view&id=1cOT5AZZPuBRqoPG7zW0INLjDmTO4UI8O",
        "https://drive.google.com/uc?export=view&id=1IxcdiH-zgZhgetdBBJbWBUZJi3KdkRmM",
        "https://drive.google.com/uc?export=view&id=1bi7Vs2g-8Wk9Ab8SCsAV6Q64tZzA0XDO",
        "https://drive.google.com/uc?export=view&id=1wufJqchT8TCybPuB-t9s8A3NJj04Nqcm",
        "https://drive.google.com/uc?export=view&id=1OagoRIgcLhWt18LJPgg3-Owdg9-3zyp9",
        "https://drive.google.com/uc?export=view&id=1pEgBR4_cYue3-2zEgpyvSNyCROGTfCyM",
        "https://drive.google.com/uc?export=view&id=12vSMsCvlgNGlcMtnIZCzLu0ZBda8NwFf",
        "https://drive.google.com/uc?export=view&id=1TTdTDfg1GuSIz0Q9n3I_nG0rLf1D4Rak",
        "https://drive.google.com/uc?export=view&id=1ORvF_9EZTfnGdeoweibwbUy07y-Fd0tA",
        "https://drive.google.com/uc?export=view&id=1mPNBVYPsYcf52Bb9Q_HoJ_tticObUjXD"
    ]
    data_list = [
        {"nama": "Kevin Antonio Junior", "jabatan": "Kepala Departemen Minbak", "nim": "123450109", "umur": "21", "asal": "Bandar Lampung", "alamat": "Panjang, Bandar Lampung", "hobbi": "Balap", "sosmed": "@kevinaj__", "kesan": "Abangnya chill, ramah ", "pesan": "Semangat selalu bang, semoga TA nya lancar dan sukses selalu bangg"},
        {"nama": "Gusti Putu Ferazka Dhiyamika", "jabatan": "Sekretaris Departemen Minbak", "nim": "123450046", "umur": "21", "asal": "Lampung Utara", "alamat": "Way Halim", "hobbi": "Baca", "sosmed": "@ferazkaa", "kesan": "Kakaknya cantikkk, ceriaa, humble", "pesan": "Semangat selalu kak, semoga TA nya lancar dan sukses selalu kakk"},
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
