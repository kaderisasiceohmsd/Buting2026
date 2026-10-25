# 008_Egia Ninta Pepayosa Ketaren.py
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
        "https://drive.google.com/uc?export=view&id=1OZ90dYQxs9qhwjS1IPjwAI8hPVZ3JZD-",
        "https://drive.google.com/uc?export=view&id=1PhDbGoXVKxccssC8wPlA61diRd4pNgf_",
        "https://drive.google.com/uc?export=view&id=1yuqzTRWDLty1-ujD5pVts539JmAU1ARo",
        "https://drive.google.com/uc?export=view&id=1OVtrdQ9DYO5r6LoJuapZb67S55IKmYXk",
        "https://drive.google.com/uc?export=view&id=1gPzMBXa36KLARfOs2jXYK4y_eozaEUbt",
        "https://drive.google.com/uc?export=view&id=1xXPJnwo_MRQhECTUKrncNcwc5vFvLvE6"
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya kahim kece,seru dan santai banget kalau diajak ngobrol", "pesan": "Semangat dan sukses selalu yaa bangg!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jendral", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya tinggi bangett, pertama kali liat abangnya main basket ga nyangka ternyata sekjen", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya lucu dan baik bangett", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya asik banget", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik dan murah senyum", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk", "pesan": "Sukses selalu dan semangat kakkk!!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="kesekjenan")

elif menu == "Baleg":
    gambar_urls = [
         "https://drive.google.com/uc?export=view&id=1K3APaB-ogB1cG988B3FWPiHR6J4qNaT0",
         "https://drive.google.com/uc?export=view&id=1fEqWzilkD0Z2gGVvlDVkjyfkvUL2Pvi0",
         "https://drive.google.com/uc?export=view&id=1D7goVhrmAdDUtKtLvjIk4L1vvvQ4SiD3",
         "https://drive.google.com/uc?export=view&id=1IiQewwd3HBrczU5IKMbdOYF8TEjP-xKK",
         "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
         "https://drive.google.com/uc?export=view&id=1NGb8jEpFfaQWZHg6JYV01vezOk2S1cd9",
         "https://drive.google.com/uc?export=view&id=1AEIhq1wNtbHTWIOWi2a3fDDFw87rF-Ed",
         "https://drive.google.com/uc?export=view&id=10lIyjmiZzYPjepl1IYiNkt95gFSOUUMe",
         "https://drive.google.com/uc?export=view&id=1nZGRlmzbLvtOQITWaqLq92m3zZBUiYwJ",
         "https://drive.google.com/uc?export=view&id=1fMHnzEjdH9x-3slXFVpo7SIgjAUB2SiL",
         "https://drive.google.com/uc?export=view&id=1bcurpxHcBev5Hft0z3tF3i7q5YO3RFrB",
         "https://drive.google.com/uc?export=view&id=1UkJ5A_eo66m8EJMWyHfgpy2-olBMCoBv",
         "https://drive.google.com/uc?export=view&id=1HNQFtFLEF6c-1X8d9n5J7NDm7oPAEx6y",
         
    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik ", "jabatan": "Ketua Badan Legislatif", "nim": "123450060", "umur": "20", "asal": "Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@rmridhomanik", "kesan": "Abangnya kece dan asik banget", "pesan": "Semangat TA nya bangg!!"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim", "sosmed": "@j__eesie", "kesan": "Kakaknya cantik dan baik banget", "pesan": "Semangat TA nya kak!!"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@ddharu_", "kesan": "Abang lucu dan baik poll", "pesan": "Semangat TA nya bangg!!"},
        {"nama": "Gh Mikael Niko Anthoni Setiadi", "jabatan": "Staff Komisi I", "nim": "124450022", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@me._kael", "kesan": "Abangnya ramah banget", "pesan": "Semangat selalu bang!!"},
        {"nama": "Siti Sarifah", "jabatan": "Staff Komisi I", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Kakaknya baik dan ramah banget", "pesan": "Semangat selaluu yaa kakk!!"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II", "nim": "124450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum kopi", "sosmed": "@givarooo", "kesan": "Abangnya kecee dan kerenn", "pesan": "Semangat selalu bangg!!"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staff Komisi II", "nim": "124450042", "umur": "19", "asal": "Mentawai", "alamat": "Oen kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "Kakaknya baikk, ramah, murah senyum", "pesan": "Semangat kuliahnya selalu kakk!!"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staff Komisi II", "nim": "124450020", "umur": "20", "asal": "city earth", "alamat": "Sukarame", "hobbi": "Baca au", "sosmed": "@haniquratuain_", "kesan": "Kakakanyaa baik dan ramah bangett", "pesan": "semangat dan sukses selalu kakk"},
        {"nama": "Jeremia Halim", "jabatan": "Staff Komisi II", "nim": "124450101", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@jeremia_hm", "kesan": "Abangnya keren, asikk, ramah", "pesan": "Semangat selalu bang"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@monica_tjg", "kesan": "Kakaknya lucu banget dan asik", "pesan": "Semangat terus kak!"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staff Komisi III", "nim": "123450121", "umur": "20", "asal": "Depok", "alamat": "Pemda", "hobbi": "gym / koleksi figur", "sosmed": "@nagatsee", "kesan": "Abangnya asikk walaupun kemarin sempat kaget foto aku dijadiin stiker trapi abangnya baik banget", "pesan": "Semangat selalu bangg!!"},
        {"nama": "Sekardini Widya Putri", "jabatan": "Staff Komisi III", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "Kakak mentor PIK R aku, kakaknya baikk bangett dan lucuu poll", "pesan": "Semangat selalu kakk!!"},
        {"nama": "Wan Nashwa Al Hasni", "jabatan": "Staff Komisi III", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nahaysh", "kesan": "Kakaknyaa murah senyum dan baik banget", "pesan": "Semangat TA nya kakk!!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="baleg")

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1bwy4U200wjwc6YN3tumWFDSW7LunNfmu",
        "https://drive.google.com/uc?export=view&id=1EJBPN6k5XmLVB8xtMNTgo2nWPEQFUkqv",
        "https://drive.google.com/uc?export=view&id=10s33vUvU34kLCr8nyL8rNZfM1k-Z1WCK",
        "https://drive.google.com/uc?export=view&id=1R77leJE5k8iATcKwvKFiw5nCmq-Ezl8C",
        "https://drive.google.com/uc?export=view&id=1awaYdg6TEcZ2P7E2KkmswUJA4rNVyNoA",
        "https://drive.google.com/uc?export=view&id=17b9QyXuHtyBeEvGLfS-omWt02e5RfT8D",
        "https://drive.google.com/uc?export=view&id=1PQpUNK5ZcmAVQ06WLxg8UlpHGsKoPlEC",
        "https://drive.google.com/uc?export=view&id=1_-uYsuZTVLXJ-RgwHKfzpR4r0otEN3Fx",
        "https://drive.google.com/uc?export=view&id=10IDI69GEY5BwBdxi6wm5L5im0UKDLoen",
        "https://drive.google.com/uc?export=view&id=1H77_72UrtmZXICgAMQHerezZ5vIYyYrp",

    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator Mahasiswa", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Kakaknya ambis banget, lucu poll dan cantik banget", "pesan": "Semangat selalu yaa kak!!"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Kepala Biro Aspirasi dan Media Komunikasi", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya lucuuu apalagi kalo foto harus melet", "pesan": "Semangat selaluu yaa bang!!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Staff Biro", "nim": "124450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Abangnya asik banget seruu", "pesan": "Semangatt terus bang"},
        {"nama": "Suci Aulia", "jabatan": "Staff Biro", "nim": "124450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Kakaknyaa lucu banget, cantik, dan asikk banget", "pesan": "Semangatt selaluu yaa kak!!"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Staff Biro", "nim": "124450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Abangnya lucu banget dan asik", "pesan": "Semangatt selaluu yaa bang!"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Kepala Biro Kajian Strategis dan Propaganda", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Kakaknya baik bangettt", "pesan": "Semangatt teruss ya kak!!"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Staff Biro", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Kakaknyaa gemesin banget dan super aktif banget", "pesan": "Semangatt terus ya kak!!"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Staff Biro", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Abangnya keliatan galak banget tapi aslinya baik banget dan asikk poll", "pesan": "Semangat selalu ya bang!!"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Kepala Biro Kesekretariatan", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Kakaknya cantik,gemesin, dan super ramah lucuuu poll", "pesan": "Semangat terusss yaa kakk"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Staff Biro", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Kakaknyaa baik bangett dan ramahh", "pesan": "Semangat selalu kakk!!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="senator")

elif menu == "Departemen PSDA":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=11gpV6qdfhF-QweCN9rkhCIzuDy9P9waD",
        "https://drive.google.com/uc?export=view&id=1zHcgsAuRM_ssrFjUp7cWqMhzORdBjZWz",
        "https://drive.google.com/uc?export=view&id=1IxLDaIjg1y0USqbb4jxHeJ-OtDXByknW",
        "https://drive.google.com/uc?export=view&id=1XU1wxQ2LwwcGTIVG9HJdP_n1wWoQhu49",
        "https://drive.google.com/uc?export=view&id=15fCy7cH0XZQ-FystUV6Db522vY2wyXjE",
        "https://drive.google.com/uc?export=view&id=1Q3zDq_gkf-L-rNNJ1o8Z2KpaP478pBdS",
        "https://drive.google.com/uc?export=view&id=1OmD-pPuMenMVvFxwvedhpg4d7f3PUVS1",
        "https://drive.google.com/uc?export=view&id=1AjzhTBiZ98CnTjp4xLhuo8OQmtlqyAvR",
        "https://drive.google.com/uc?export=view&id=1mipAyg58x9N1gtJUgg3VDr5sNAuB_dbJ",
        "https://drive.google.com/uc?export=view&id=1NXhEpZz8Ex7NtKqliQ1MYAO3iQ1jmWSq",
        "https://drive.google.com/uc?export=view&id=1ZN73joBSJaKv8nQzOGyR3eWdKTcbJnqW",
        "https://drive.google.com/uc?export=view&id=1v3_y7uWYuiE_bE2ZxvfbVaOe6FteiBL9",
        "https://drive.google.com/uc?export=view&id=1q1VvlqdASswyOhluNkBHNeezE__Jhm0z",
        "https://drive.google.com/uc?export=view&id=1n5kcXRx7wkgNHtrDzd0r3OULxsXE2hAH",
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
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Nias Selatan", "alamat": "asrama tb 3", "hobbi": "ngejek orang", "sosmed": "@desmannal_", "kesan": "Abangnya kece banget", "pesan": "Semangat selaluu bang!"},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Charrlindah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Jeremi Marolop P. Situmorang", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
        {"nama": "Salavi Naharani", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"},
]
    display_images_with_data(gambar_urls, data_list, key="psda")

elif menu == "Departemen MIKFES":
    gambar_urls = [
         "https://drive.google.com/uc?export=view&id=1aMlbW-y2Yk6woTnUd8IINyhJwTN5EwaI",
         "https://drive.google.com/uc?export=view&id=1pi5nDGnwVW_jcznF9C6CQelcbhmJ8cXa",
         "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
         "https://drive.google.com/uc?export=view&id=1MliK-HTQGjpZ3-DSAqAspkunyfkMbObP",
         "https://drive.google.com/uc?export=view&id=1McXh_tJ8D-kjrZZWw4byoWl6JF2cx9W7",
         "https://drive.google.com/uc?export=view&id=1nDjL2DvUaduudxinJBdBnldk6PiuTgwq",
         "https://drive.google.com/uc?export=view&id=1nq1PFhp4gLle5wFwsom0FLUE98YXusFC",
         "https://drive.google.com/uc?export=view&id=1hHu5Or0psvMYnu73lxdG35ubzW22YCCD",
         "https://drive.google.com/uc?export=view&id=1rJk0qMbKl-0rGJWYADFWJpx9uZcpnmxT",
         "https://drive.google.com/uc?export=view&id=1Sa8sVuGZ_5A1t2dzp0e9KNiYjEfgL7Un",
         "https://drive.google.com/uc?export=view&id=1iM3Avpu0kr-fiCiXQasfmPrmunGve7QJ",
         "https://drive.google.com/uc?export=view&id=1vKZ26lqcXWWsBRMHr5dJQ7jRAnYEPLvU",
         "https://drive.google.com/uc?export=view&id=1rl1liYQ6SFHSBjaXfD8yKzmTb-Vy3DOh",
         "https://drive.google.com/uc?export=view&id=199x7OWNAkY7FRT1QR13kPDhGQhYWNcJ4",
         "https://drive.google.com/uc?export=view&id=1juZp3jgup49ynEjNqZkItLkJP4yBSQFk",
         "https://drive.google.com/uc?export=view&id=1_Lao8CfS6sX3hPcq0NH1IuCz67Bl9vKl",
         "https://drive.google.com/uc?export=view&id=1Zp2S_vUhHG7EXyvQweQruonqAJIbaBWS",
         "https://drive.google.com/uc?export=view&id=1HTXzPckqDeWFQ6IYY4jyNFGaO1sB28jA",
         "https://drive.google.com/uc?export=view&id=1IHN_WgoHWSfoSZhu1rvLvAbpMPV0iFFL",
         "https://drive.google.com/uc?export=view&id=198wDkdmzgpMJSrhE9lol_r9qxblqd5J9",
         "https://drive.google.com/uc?export=view&id=1nkxiz2kk9MVhiza5MGqjawo2VSQ8ZAFG",
         "https://drive.google.com/uc?export=view&id=1t61O78i6va3AG3WFWFdrgGK3DciybiTe",
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
        "https://drive.google.com/uc?export=view&id=1s2XoLDNkmd79J8wzApnNqw9wA6lk1-cv",
        "https://drive.google.com/uc?export=view&id=1p8c54qe0t-KydPSN1_njmXyec4iIxPv1",
        "https://drive.google.com/uc?export=view&id=180LnphDPRRURP6I5_axl1o8-rMvM0a7v",
        "https://drive.google.com/uc?export=view&id=1OA-b0s0HelPi3sxZVwL8ClhvTZOd6RwS",
        "https://drive.google.com/uc?export=view&id=10bAdfxrD7ocCcavQarvNOlxpMMwvDIfu",
        "https://drive.google.com/uc?export=view&id=1LGW61YoaqD33BADwm6puWEK6OF5o23ZD",
        "https://drive.google.com/uc?export=view&id=1N5N0KOx8r1e6dC48eZMDUCKbHt0wjVOb",
        "https://drive.google.com/uc?export=view&id=17gTme8LpUJXymPaVakbNlva-dI-9g-I_",
        "https://drive.google.com/uc?export=view&id=1tY19bSlTXLnJlwfmh06rgIiYNlL5MLUY",
        "https://drive.google.com/uc?export=view&id=1fxkhtAJEXXvdsLWEBLxAzJh__G8RMX0y",
        "https://drive.google.com/uc?export=view&id=1SbfGEpQvEF5JRJOr8eCiNm4fcHe6RL0Y",
        "https://drive.google.com/uc?export=view&id=1CXKxYtEPvKZ7-XB4IcGU8Lt6Meu31efF",
        "https://drive.google.com/uc?export=view&id=1iPjdXfvKW7s0ACiTHMRnV3AibnbNFM3c",
        "https://drive.google.com/uc?export=view&id=1Na9ZnS6uwX_Hq1qJVQuT7m_OeL9WPMJx",
        "https://drive.google.com/uc?export=view&id=1aphZKIhFSh1cXrDmGNNBFrW0168bQOup",
        "https://drive.google.com/uc?export=view&id=1gC-G8jGnV141twsV4142tLba2B0HlDgS",
        "https://drive.google.com/uc?export=view&id=1YU37XRd6LfGjBOCMDxhjje91ifITPXvB",
        "https://drive.google.com/uc?export=view&id=14-bA744kvqPIcYDN4fEYbDuH3SPMmaMd",
        "https://drive.google.com/uc?export=view&id=1rl91DQRXnOId12HESf4-i5g7sTtFaGX5",
        "https://drive.google.com/uc?export=view&id=1Z4-9A7vu0SoSH4V26iOOMWkWce1DiamW",
        "https://drive.google.com/uc?export=view&id=1y6G-InpEMk3i3L1lr8VIjuWy2HZoT7N6",
        "https://drive.google.com/uc?export=view&id=1BlMK8yUPvll8ifkluUTZu87WU-ycClyb",
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
        "https://drive.google.com/uc?export=view&id=10O1Caz42SEbjnXeI9gG2Y4hY_QkgSdU8",
        "https://drive.google.com/uc?export=view&id=1XGvXqgOJb22CgCi9I7HQ9AFcxpPg-IXo",
        "https://drive.google.com/uc?export=view&id=1ooethe_x7ljdmbb7bBzlAGicP2GUawi7",
        "https://drive.google.com/uc?export=view&id=1C2rw5WfpXZffwbCYMj1HvXfDmciKTcHa",
        "https://drive.google.com/uc?export=view&id=1YLIMKJnw_RKujj6JNRBsxIwAzCCwE1r0",
        "https://drive.google.com/uc?export=view&id=1BGH5nzNfUQWJlwOfDWD18NxWMsj23r5i",
        "https://drive.google.com/uc?export=view&id=1OKubH1K9FFAHwaydYatfj6kRsMSrT-Am",
        "https://drive.google.com/uc?export=view&id=1JQPthYyZfaxQMmSnsUgAr8sIJC_nIsLS",
        "https://drive.google.com/uc?export=view&id=1DWF4I9MjG-pigYN6cvamPV8SE044UsSy",
        "https://drive.google.com/uc?export=view&id=16yATY5lIAG_R6SOPDSwI4ESL85i1oEkJ",
        "https://drive.google.com/uc?export=view&id=1UApvD-3wAmTP78jmaS0HBqgJazoewXp9",
        "https://drive.google.com/uc?export=view&id=1bYlhIR1eTZDJ7q6DvhzCtM_WBAVnUhOL",
        "https://drive.google.com/uc?export=view&id=10AQRs6idn65qdb0dRSs5FNZiMAvWDnAe",
        "https://drive.google.com/uc?export=view&id=1SRbQ_POWNIvr75UQCV9ITtzWdNulxY6I",
        "https://drive.google.com/uc?export=view&id=1CGK_JAnrzMLBIsZ8aA4Q-RkOcC8TkAsz",
        "https://drive.google.com/uc?export=view&id=1sW9wnx_3pZyYTBhczlL5mnOepLeG4Fvf",
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
        "https://drive.google.com/uc?export=view&id=1XMls4kh0QcWMIDiVzqaJX1kqhkOVWSzQ",
        "https://drive.google.com/uc?export=view&id=1EEZwTqaefUkPSoAnzgNig0A2nqn3zlaw",
        "https://drive.google.com/uc?export=view&id=1rU8FhlY3OoVrBAzlOyAaaxQ1MQhpmj0O",
        "https://drive.google.com/uc?export=view&id=1z91dbs7Sru4gLs8kP-ExLbWDQ7Ws6cD6",
        "https://drive.google.com/uc?export=view&id=1q_k2LJHBu9tsUNbtGJot6XAVoHGt0h7r",
        "https://drive.google.com/uc?export=view&id=1_Kf5fNwcsxG1oVEJvGDTZvdsGhHXFE0J",
        "https://drive.google.com/uc?export=view&id=1ry-WzKXg9EmgLjPwYH8BhXXe8gpokdjo",
        "https://drive.google.com/uc?export=view&id=18d4v1U8gLpdCA8VWmNIch_OpCwTOirNL",
        "https://drive.google.com/uc?export=view&id=1tzn97c-1KiRhIahSxkP4kSt5kGoe8crl",
        "https://drive.google.com/uc?export=view&id=10m29TXmNnHql0sowOmnuNqGz0WPKt2_P",
        "https://drive.google.com/uc?export=view&id=1a2DLQdH5tqfYSm1k9MMx39i4hmx836pD",
        "https://drive.google.com/uc?export=view&id=1g2nAwUtylUht0-LAByTVUYJ0SrwFtd2o",
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Kepala Departemen SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Abangnya ramah banget dan jugaa santai banget jadii bawaannya asik", "pesan": "Semangat TAnya bang, lancar terus!"},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Sekretaris SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Kakaknya super cantik, ramah, dan informatiff bangett", "pesan": "SemangatTA-nya kakk, moga cepat dapat gelar!"},
        {"nama": "Afifah Fauziah", "jabatan": "Kepala Divisi Kemitraan", "nim": "12345002", "umur": "19", "asal": "Sumatera Barat", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "Kakaknya tersweet, selalu senyum dan nyapa pas ketemu di kampus", "pesan": "Semangat TAnya kakkk, stay happy!"},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Staf Kemitraan", "nim": "123450013", "umur": "20", "asal": "Lampung Tengah", "alamat": "Sebelah Kosan Ayake", "hobbi": "Nonton Youtube", "sosmed": "@hasan.ramadhan08", "kesan": "Abangnya tenang dan asik banget diajak ngobrol", "pesan": "Semangat selaluu yaa bang!!"},
        {"nama": "Layina Ropiqo", "jabatan": "Staf Kemitraan", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "Kakaknya asik diajak ngobrol, pembawaannya ceria dan bikin nyaman", "pesan": "Semangat kuliahnya kak, sehat-sehat terus!"},
        {"nama": "Moch. Iqbal Az-Zahir", "jabatan": "Staf Kemitraan", "nim": "124450052", "umur": "20", "asal": "Bekasi", "alamat": "Natar", "hobbi": "Nonton Drakor", "sosmed": "@iqbalazzahir_", "kesan": "Abang asdosnya baik poll, penyabar pas bimbing praktikum dari awal", "pesan": "Semangat dan sukses selalu yaa kak!"},
        {"nama": "Talitha Justine", "jabatan": "Staf Kemitraan", "nim": "122450076", "umur": "19", "asal": "Jakarta", "alamat": "Pemda", "hobbi": "Nonton", "sosmed": "-", "kesan": "Kakaknya positive energy banget, ngeliatnya bikin tambah semangat", "pesan": "Semangat terus ya kak, bahagia selalu!"},
        {"nama": "Anadia Carana", "jabatan": "Kepala Divisi Kewirausahaan", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "Kakaknya kece, humble, dan cara bicaranya santai", "pesan": "Semangat selalu kak, sukses terus!"},
        {"nama": "Abdillah Fikri Al pome", "jabatan": "Staf Kewirausahaan", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@pomest__", "kesan": "Abangnya murah senyum dan asikk", "pesan": "Semangat selaluu ya bangg!"},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Staf Kewirausahaan", "nim": "124450008", "umur": "20", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Fishing", "sosmed": "@dhal_setiawan", "kesan": "Abang NIM yang super kerenn dan jugaa baik bangettt", "pesan": "Semangat selaluu ya bangg!"},
        {"nama": "Anggun Nita", "jabatan": "Staf Kewirausahaan", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa", "kesan": "Kakaknya manis, murah senyum, dan baik banget", "pesan": "Semangat kuliahnya kak, moga lancar urusannya!"},
        {"nama": "Della Anisa Fitri", "jabatan": "Staf Kewirausahaan", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Kakaknya cantik, baik poll, dan ramahh bangett", "pesan": "Semangat kuliahnya kak, sukses selalu!"},
    ]
    display_images_with_data(gambar_urls, data_list, key="ssd")

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1ulGIf34qaoBzEOYvhPCB6uSvBrz0F9pW",
        "https://drive.google.com/uc?export=view&id=1h8dcFbYl9P8Eo0xmIQtdHPjjXIrgkasq",
        "https://drive.google.com/uc?export=view&id=1MWtuNt7cLjzoqVyIQnJcgQjhC6sruQLR",
        "https://drive.google.com/uc?export=view&id=1pdIVt6ZbCmfYMGMWa0wwrUbjhypQLC9F",
        "https://drive.google.com/uc?export=view&id=1d9ycgjc2PJqjmEt3bw7HorlX0Ma84Rek",
        "https://drive.google.com/uc?export=view&id=1EVU9KZqngak_sG_jW0roDyxBTXkHnAQy",
        "https://drive.google.com/uc?export=view&id=1XRFM0IuJEOLBHofYh5rbEL9OeeWHT4jB",
        "https://drive.google.com/uc?export=view&id=1Ne_GdGDiUeHu4cT4ameZpkjtNfVjcObi",
        "https://drive.google.com/uc?export=view&id=17t6Fk5wpCKhWHRJTijuKBHDeHf1hooFf",
        "https://drive.google.com/uc?export=view&id=1i943gu9P0Hn-4iX3Ff_xs5267MzrNro7",
        "https://drive.google.com/uc?export=view&id=1zxtRxWrcSCuWE1n6UlYl-mVe7jLtEA5y",
        "https://drive.google.com/uc?export=view&id=14SuvEak83yiR3YdQfmtI7W_mSbxL5p9_",
        "https://drive.google.com/uc?export=view&id=1AwlD3RESR9TVy-mKCm3Sc4-U9JRuO8lQ",
        "https://drive.google.com/uc?export=view&id=1FukwdS0qWoZV48NsuvHvJSI36PTsmtF_",
        "https://drive.google.com/uc?export=view&id=1Vnhfi110gNpl3qKW-VfwdXjGjmg54aB6",
        "https://drive.google.com/uc?export=view&id=1MDkamNb-fcmJTpYtGqvCWs-l90BHVmQq",
        "https://drive.google.com/uc?export=view&id=1Pjv83uV75agH_7TtIForfU156O7W8jR9",
        "https://drive.google.com/uc?export=view&id=1m6mewOwuNMcAbijrIln-TAvqfOcGpq_b",
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
        "https://drive.google.com/uc?export=view&id=1silR0Ryhzbsq39uwHuKolYsfgaGyhv6u",
        "https://drive.google.com/uc?export=view&id=1GCdyZhntF9j9E9Fs_9Keev2JTvy7PJyx",
        "https://drive.google.com/uc?export=view&id=18QXf1YlRrk2Ro7yDZik34PIe7elAqbqR",
        "https://drive.google.com/uc?export=view&id=1MAcuTYtIDoH8Fn1Vcmu_VSOXO4ZIdiay",
        "https://drive.google.com/uc?export=view&id=1TbwAFdq0MhsYEqeESeINOcuV6FDMnhBQ",
        "https://drive.google.com/uc?export=view&id=1Tas_IO7W_IWBDhIGghLpodKui88Tbddi",
        "https://drive.google.com/uc?export=view&id=14NvxlhWKdUmu0fi0MrDeddiLA2UTrWBw",
        "https://drive.google.com/uc?export=view&id=1Ub-5L059GFHU1SocfHnst1bWULKDZiAe",
        "https://drive.google.com/uc?export=view&id=13L_9-3DMghSI54YnLgt9_YKJxdmvPApM",
        "https://drive.google.com/uc?export=view&id=1U67liSEUH3ah3llGmySNWwirKIw_Zw3P",
        "https://drive.google.com/uc?export=view&id=1v1K34TXTE_fPDkdFca5LY2sVV48PZZ0_",
        "https://drive.google.com/uc?export=view&id=1biJbOOmJ4pOZWhhDRTXc7oSsJqYECzZB",
        "https://drive.google.com/uc?export=view&id=1VUrn0Ns8lO10h1jSG6VuQl8VG9vsQmHF",
        "https://drive.google.com/uc?export=view&id=1ED7Q3ErtdA6W4RARR7wHX9aGsKKVDukC",
        "https://drive.google.com/uc?export=view&id=1EoQKQ-v5HEB_nM2i0kKxd_eMXfezDHAN"
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
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Staf Medkraf", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"}
    ]
    display_images_with_data(gambar_urls, data_list, key="minbak")

