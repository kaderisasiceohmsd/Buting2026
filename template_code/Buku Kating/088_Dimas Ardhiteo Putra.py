import streamlit as st
from sakura_ui import (
    render_buku_kating_header,
    render_kating_cards,
    sakura_dept_menu,
    display_kating,
)

render_buku_kating_header("088 - Dimas Ardhiteo Putra")

# Navigasi Kategori Departemen (Sakura Theme)
def streamlit_menu():
    return sakura_dept_menu()

menu = streamlit_menu()

def display_images_with_data(kating_data):
    display_kating(kating_data, departemen=menu)

if menu == "Kesekjenan":
    def kesekjenan():
        kating_data = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-O0PYQwKLb2hemdBhjrnMgFoPYatlw6T",
                "kesan": "Kesan yang aku dapat dari Kak Ginda, sosoknya ramah dan membuat suasana terasa nyaman.",
                "pesan": "Teruslah menjadi pribadi yang baik dan rendah hati. Semoga langkah Kak Ginda selalu dimudahkan.",
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1H15DQzaSmo78aU2gWrfysKoOQOsO4zgh",
                 "kesan": "pembawaannya yang hangat dan enak diajak berinteraksi.",
                "pesan": "Semoga perjalanan ke depan dipenuhi kesempatan baik, kesehatan, dan keberhasilan.",
            },
            {
                "nama": "Efi Defiyati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ln04DGU0Lc9sXhoyppviS9UvKupvRiCO",
                "kesan": "Kak Efi baik karena sikapnya sederhana, terbuka, dan menyenangkan.",
                "pesan": "Jaga diri baik-baik, dan semoga hari-hari Kak Efi selalu menyenangkan.",
            },
            {
                "nama": "Qois Olifio",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=178yDYLTucGPL5HwwL-D0tzeVJlcSq7iO",
                "kesan": "Aku melihat abangnya sebagai pribadi yang rendah hati dan selalu membawa energi positif.",
                "pesan": "Semoga masa depan bang qois dipenuhi pengalaman baik, orang-orang tulus, dan kebahagiaan sederhana.",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TbqjmnrsOH8MwkMrLaiaCIrRJjLucOPk",
                "kesan": "Orangnya lucu dan ramah; cara senyumnya manis juga mudah menular.",
                "pesan": "Semoga selalu dikelilingi orang-orang baik dan tetap mempertahankan senyumnya.",
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1frdlrJLufW0eP7gO05YjR2jHaOJx5tuM",
                "kesan": "Dari cara bercerita dan berbagi pengalaman, saya mendapat banyak insight baru tentang dunia perkuliahan.",
                "pesan": "Semoga kuliahnya lancar; saya masih ingin mendengar banyak cerita dan pengalaman lainnya.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        kating_data = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1zh4M-Em2lwM-CmePV3GbnEiicK8zL9af",
                "kesan": "Abangnya keren, ramah, suka mengayomi, dan bijaksana saat diajak berinteraksi.",
                "pesan": "Semoga selalu sehat, sukses, dan lancar menjalani kuliahnya.",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1j_56jjUXFplAfwI6MsZT_2hRZMPUHM9C",
                "kesan": "Mentor TPB yang keren, berprestasi, dan banyak memberi motivasi.",
                "pesan": "Semoga kuliahnya lancar, tetap ceria, dan jangan pernah kehilangan senyumnya.",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tyAFkhHMUanbHCvNarJsojELU9S_PpDL",
                "kesan": "Abangnya keren banget, pinter, baik juga.",
                "pesan": "Semangat terus dan sehat selalu abang, semoga bisa menjadi teladan atau contoh yang baik untuk adik tingkatnya ya abang.",
            },
            {
                "nama": "Givaro Ananta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17RXB64pOkzQlnQsbiR9OoJGRhgCkTk4P",
                 "kesan": "Orangnya seru dan sering membuat suasana lebih santai dengan candaan-candaan random.",
                "pesan": "Semoga kuliahnya lancar dan jangan lupa tetap menjaga kesehatan.",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1FajHLFg1Adloc9Qj5KoPmQ97DDAmvDxF",
                "kesan": "Orangnya baik, ramah, dan punya pembawaan yang menyenangkan.",
                "pesan": "Semoga semua keinginan baiknya segera tercapai dan kuliahnya berjalan lancar.",
            },
            {
                "nama": "Gh Mikael Niko A S",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lm9RQDR0eqeYvkLDkze_AsKqhiEMD7ga",
                "kesan": "Abangnya baik, asik, ramah, kirain pendiam",
                "pesan": "Sehat selalu dan sukses selalu Abang",
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13_D_X0D_4dQVIV0FmQRKCtPtos3IDftB",
                "kesan": "Orangnya baik hati tapi suka isengin saya.",
                "pesan": "Tetap tebarkan senyum yang bisa membuat orang lain ikut bahagia.",
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1hO1376B7sn8zdd5lQYuXgHNpyQTQd2jL",
                "kesan": "kakak tutor Metnum saya, ngajarnyasangat jelas dan mudah dipahami.",
                "pesan": "Semoga tetap semangat berbagi ilmu, kalau ada kesempatan, saya ingin belajar lagi.",
            },
            {
                "nama": "Hani Qurrota Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jkv3ySQFjBP3uKNQmZ7_gBqCBmW87sCg",
                "kesan": "Orangnya lucu, ramah, dan enak diajak ngobrol, tapi suka isengin saya juga",
                "pesan": "Semoga selalu dikelilingi hal-hal baik dan kuliahnya berjalan lancar.",
            },
            {
                "nama": "Jeremia Halim",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1aZuCI5tlg6Mr5WGSrkp2pZ0hgthbiOOc",
                "kesan": "Penyanyi handal dan asik abangnya",
                "pesan": "Sukses terus dan semangat kuliahnya bang",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18piDxtnMPi26UDyawQxA_3oDqHyRr8wU",
                "kesan": "Awalnya saya kira orangnya dari bidang medis, ternyata aktif di Baleg dan sangat keren saat bertugas.",
                "pesan": "Semoga tidak terlalu sering membuat kaget saat memberi arahan di lapangan.",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1e8EXbqpnZ9BxLcUjJwRV86WeeMcpGPpM",
                "kesan": "Orangnya baik, manis, dan ternyata asik setelah diajak berinteraksi.",
                "pesan": "Semoga selalu dikelilingi hal-hal baik dan dimudahkan dalam kuliahnya.",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pqDKflXiYiV1mYWjA9IY0IcD2sR6dn_E",
                "kesan": "Kakaknya lucu, terkesan dari nama awalnya \"wan\" seperti suku melayu",
                "pesan": "Semangat kuliahnya kak, semoga apa yang dicitakan terwujud.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    baleg()

elif menu == "Senator":
    def senator():
        kating_data = [
            {
                "nama": "Fathinah Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1yJEP8VtnOKOoHAWxugbBaz2VAwq-sN4d",
                 "kesan": "kakaknya hebat banyak menampung aspirasi massa.",
                "pesan": "Semoga semua keinginan baiknya segera tercapai dan kuliahnya lancar.",
            },
            {
                "nama": "Helmy Surya Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1UlQC9CZxyzIp1MNRvvrOsap_cE6GxQbh",
                "kesan": "Bang Helmy orangnya asik suka ngajakin melet.",
                "pesan": "Semoga kuliahnya selalu lancar, dimudahkan dalam setiap urusan, dan semua cita-cita serta keinginannya bisa tercapai.",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ijEzT2vPZjJO3UWJ9wRJI-OqLPbE64V4",
                 "kesan": "Aku suka banget melihat kakak pas membawakan materi",
                "pesan": "Semangat kuliahnya kak! terbang setinggi mungkin",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qAByI5DpNQ24VpC3GU8s-cFU2ejs4KjI",
                "kesan": "Orangnya manis, baik, dan sangat ramah ketika diajak ngobrol.",
                "pesan": "Semoga semua keinginan baiknya segera tercapai.",
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1NdGByRdXQe7Tz6yOQZllRlLrqMf0Vbl8",
                "kesan": "Orangnya asik, keren, dan punya hobi yang menarik.",
                "pesan": "Semoga semua urusan dan rencana ke depannya diberi kelancaran.",
            },
            {
                "nama": "Suci Aulia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16Yk2N2Bow7hbgLcMLEvu9xZ1VrtzLrEd",
                "kesan": "Orangnya asik, keren, dan pembawaannya membuat suasana menjadi lebih hidup.",
                "pesan": "Semoga kuliahnya lancar dan terus dan selalu menginspirasi banyak orang."
            },
            {
                "nama": "Wielman Itolo Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Xy5Iyco90lB-FCW79oKYTPJu4enb7WyP",
                "kesan": "Cara bicaranya khas dan selalu terdengar seperti seorang jago public speaking.",
                "pesan": "Semoga semua keinginan baiknya segera terwujud.",
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=159ad2J0fyx3r7LLxajURH2q_-UORO_uH",
                "kesan": "Kakaknya asik, fashionable, dan ramah. tetap jadi mentor yang baik untuk partner saya",
                "pesan": "Semangat terus, dan semoga selalu dikelilingi orang baik ya kak",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1C4Io47YeEZLSoc7uhVtQLRt6l5AGaJjn",
                 "kesan": "Keren sekali saat dipercaya menjadi ketuplak, gacor acaranya bang",
                "pesan": "Semoga kuliahnya lancar dan semakin sukses ke depannya.",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JMYsZD-7HIprA-G9gLP6A1R6AJ2ZokCd",
                "kesan": "Kakak lucu, sangat baik, dan juga ramah sekalii",
                "pesan": "Semoga Kakak selalu dikelilingi hal-hal baik di mana pun",
            },
        ]
        display_kating(kating_data, departemen=menu)
    senator()

elif menu == "Departemen PSDA":
    def departemen_psda():
        kating_data = [
            {
                "nama": "Arienta Khusnul Ananda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1xUaeuOqs5vzalvExE_wU0YGdHPLRoAGZ",
                "kesan": "Awalnya terlihat agak serius, tetapi ternyata baik dan banyak membantu.",
                "pesan": "Terima kasih sudah menjadi salah satu orang yang ikut membantu saya berkembang."
            },
            {
                "nama": "Vany Salsabila Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14XA-XztqL0_QI4SzAf1or8_S6cw0HSoV",
                "kesan": "Orangnya baik, tegas, dan terlihat sangat sigap saat di lapangan.",
                "pesan": "Semoga kuliahnya lancar sampai lulus dan semua urusannya dimudahkan."
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Y7vMobzUDUBo0Ubpz3iHheQPrHMPm-t7",
                "kesan": "Sosoknya berwibawa, tegas, banyak pengalaman juga.",
                "pesan": "Semoga selalu sukses, berkah, dan terus menjadi pribadi yang menginspirasi.",
            },
            {
                "nama": "Desman Velius Halawa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11dVDrci8gQ16-PsbA9Sm1cS3h9lpPHjF",
                "kesan": "Orangnya baik, asik, humble, dan selalu membawa energi positif dalam tim.",
                "pesan": "Semoga sukses dan semua cita-citanya dapat tercapai.",
            },
            {
                "nama": "Afriza Azmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lrbfqb9cL8NFcwK2Ohpp0pv6_dOgM629",
                "kesan": "Orangnya tegas, keren, dan punya aura percaya diri yang kuat.",
                "pesan": "Semoga selalu diberi kesehatan, kekuatan, dan kelancaran.",
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1-zGUfaSbnoyPToAEdVKFJFZxYUQIRZmC",
                "kesan": "Awalnya terlihat agak serius, tetapi ternyata perhatian dan baik saat sudah diajak ngobrol.",
                "pesan": "Semoga selalu sehat, sukses, dan dimudahkan dalam mencapai cita-cita.",
            },
            {
                "nama": "Caesar Ozora Alrando",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1V30-8WvPjdBoAj4lf6_W1H7eTfNXvcuR",
                "kesan": "Orangnya baik, tegas, dan sangat terlihat jiwa kepemimpinannya saat menjadi korlap.",
                "pesan": "Semoga selalu diberi kelancaran dalam setiap amanah dan kegiatannya.",
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Tb0BOlsk16X-QnbWiRJ0Ew079EUxTXWb",
                "kesan": "Saat pertama bertemu di PPLK sempat terlihat tegas, tetapi ternyata baik dan perhatian.",
                "pesan": "Semoga selalu sehat, bahagia, dan dimudahkan dalam semua urusan."
            },
            {
                "nama": "Haikal Seventino Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1iYmVqzDdbNCKQHRx3bmpCVNMSBm04H8D",
                "kesan": "orangnya ga banyak bicara, tapi aura nya membawa ketegasan",
                "pesan": "Sehat selalu dan sukses buat kakaknya",
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1XY_zMSWz7LjOuaRZPq697aOACzEIsQHn",
                "kesan": "kakaknya cantik dan baik, pas di lapangan tegas juga",
                "pesan": "sehat selalu kak putri dan selalu tersenyum ",
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=150nFVrEm0MUxW3a3-Ib5Mb2Ck5y8KGny",
                "kesan": "Orangnya baik, manis, cantik, dan punya semangat yang menyala.",
                "pesan": "Semoga selalu sehat, bahagia, dan terus menjadi pribadi yang membawa semangat positif.",
            },
            {
                "nama": "Azzelya Thianandry",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Kih5BdBO4ZHdVe1AmUUVGPgCaYQIyWqQ",
                 "kesan": "Orangnya kalem, baik, dan ramah sehingga nyaman diajak berinteraksi.",
                "pesan": "Semoga bahagia dan selalu dikelilingi hal-hal baik di mana pun berada.",
            },
            {
                "nama": "Charrlindah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1zLChJEiREbMEtKYIe7XimUhXX3vw9CNV",
                "kesan": "Orangnya santai, baik, dan keren saat diajak bekerja sama.",
                "pesan": "Semoga selalu sehat dan kebahagiaan menyertai setiap langkahnya.",
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GXOue82J1A1-RSOYllCSk3r9CGNmjdv-",
                "kesan": "Abang Jemar humble, asik, kece, dan calon capo Damaskus yang menyala",
                "pesan": "Semoga selalu kuat dan dapat mencapai cita-citanya ya abang!!",
            },
            {
                "nama": "Nabila Nur Azizah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1i4K-xQ3rkZzUGa8Qf0VIGrkj3ov1ayVr",
                "kesan": "Baik dan ramah kakaknya",
                "pesan": "Dipermudah segala urusan dan makin sukses buat kakaknya",
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14A__D6QGDWrG8v3ped4-5xKPNvD9ceW1",
                "kesan": "Orangnya keren, baik, dan ramah saat diajak berinteraksi.",
                "pesan": "Semoga selalu sehat dan semua yang sedang diusahakan dapat tercapai.",
            },
            {
                "nama": "Salavia Naharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1q3nSJ6ulwfHiFgkGk2Zg3KgB8SdkewMf",
                "kesan": "Baik dan ramah dan lucu banget kakaknya",
                "pesan": "Semoga selalu sehat dan sukses menjalani kuliah.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_psda()

elif menu == "Departemen MIKFES":
    def departemen_mikfes():
        kating_data = [
           {
                "nama": "Fabio Banyu Cyto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13wg2DFr1Ue0NkPsy88IRaJZAW7l654xq",
                "kesan": "Keren banget ketika melihat prestasi Abang",
                "pesan": "Tetap semangat menginspirasi banyak orang ya abang, semoga sukses selalu menyertai abang.",
            },
            {
                "nama": "Tanty Widiyastuti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1M5wovbfYyipq5y2pnDhkU4yf97Towa3G",
                "kesan": "Orangnya lucu, heboh, ceria, dan punya senyum yang manis.",
                "pesan": "Semoga ilmu serta kebaikan yang dibagikan menjadi berkah untuk perjalanan ke depannya.",
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "belum pernah ketemu, tapi pasti abangnya sangat baik",
                "pesan": "Semoga amal ibadah dan ilmu yang dibagikan menjadi berkah untuk perjalanan ke depannya.",
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=11VCDFystpavf5Jf9wxaGcyHMRNLJD_ts",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Tetap semangat menginspirasi banyak orang ya abang, semoga sukses selalu menyertai abang.",
            },
            {
                "nama": "Razin Hafid Hamdi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1AckjDHh4XSEzulV0N11ZqMkdMjsNou51",
                "kesan": "Abang keren banget waktu ngejelasin materi WWC tentang mikfes",
                "pesan": "Tetap semangat menginspirasi banyak orang ya abang, semoga sukses selalu menyertai abang.",
            },
            {
                "nama": "Manuel Frederika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=15CGuyGGki_2AmSWtCia1yx3xt-UtkTxS",
                "kesan": "Abangnya baik dan humble banget",
                "pesan": "Tetap semangat menginspirasi banyak orang ya abang, semoga sukses selalu menyertai abang.",
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VeE6Uqa1xosn-oWESkS0iva1qAu_UFm9",
                "kesan": "Orangnya baik hati, cantik, dan punya pembawaan yang lembut.",
                "pesan": "Semoga selalu dikelilingi orang-orang baik dan sukses dalam kuliahnya.",
            },
            {
                "nama": "Risa Romadona",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tFaajXX_pRoiXCzKWaC73M_aZlMD1_i1",
                "kesan": "Orangnya baik, ramah, dan mudah membuat suasana terasa nyaman.",
                "pesan": "Semoga kuliahnya lancar dan selalu diberi kebahagiaan.",
            },
            {
                "nama": "Vannisa Ramadhani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1b6cga-iTXqBQvyMtDi5r_VrP-R1F24uR",
                "kesan": "Orangnya cantik, baik, dan ramah ketika diajak berkomunikasi.",
                "pesan": "Semoga selalu sehat, bahagia, dan sukses menjalani kuliahnya.",
            },
            {
                "nama": "Yulia Kristine Malau",
                "link_gdrive": "https://drive.google.com/uc?export=1T-kf9WRc9YsjQx2vXWln5mcHJgUDZBxC",
                "kesan": "Orangnya cantik, baik, dan ramah pembawaannya juga menyenangkan.",
                "pesan": "Semoga semua urusannya dilancarkan dan kuliahnya sukses.",
            },
            {
                "nama": "Elsa Sitorus",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13pVjExeGQye-BMChGkNw8Z3S7tRKUk79",
                "kesan": "Orangnya baik dan keren saat berorganisasi semangatnya juga mengagumkan.",
                "pesan": "Semoga terus berkembang dan sukses dalam setiap langkahnya.",
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1pOYYVmobTdvt8fNASHqHVeINfgWWCKuy",
                "kesan": "kakaknya ramah keliatan pendiam mungkin banyak yang mau dibicarakan",
                "pesan": "semangat terus kak, dan teruslah menjadi versi terbaik dari dirimu.",
            },
            {
                "nama": "Lovianora Saragih",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1jaUexuBEgH-upuPM-FLJIZQUZXS1bR48",
                "kesan": "Orangnya cantik, baik, dan ramah.",
                "pesan": "Semoga selalu dikelilingi hal-hal baik dan sukses dalam kuliahnya.",
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Orangnya ramah, humoris, dan mudah membuat suasana menjadi lebih santai.",
                "pesan": "Semoga kuliahnya lancar, tetap bisa menikmati waktu istirahat, dan semua cita-citanya tercapai.",
            },
            {
                "nama": "Sherena Florencia",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=18jr33J_anrQnt7ZPFGoQ7299P_M9QTWn",
                "kesan": "Kakaknya cantik, baik dan ramah",
                "pesan": "Semoga terus percaya diri mengembangkan kemampuan, kuliahnya lancar, dan selalu dikelilingi hal-hal baik.",
            },
            {
                "nama": "Faiza Try Anjani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OCUMDMDY6G3M8Vd3khymHZalsZnHMvel",
                "kesan": "Kakaknya cantik, baik dan ramah",
                "pesan": "Semoga selalu semangat menjalani kuliah, banyak hal baik datang, dan semua harapannya tercapai.",
            },
            {
                "nama": "Gathfan Nadif Ali",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1FGOiFG-LQ1JHTC8sqZx9NzTBgwyBheRS",
                "kesan": "Pertama bertemu saat WWC, kesannya ramah dan mudah diajak berinteraksi.",
                "pesan": "Semoga sukses dan terus menginspirasi banyak orang.",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ihsvyMogIEjNiDRgYShx_qbKITAhagOf",
                "kesan": "Mentor yang keren, baik, dan lucu",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qzpFa9WroJ6r_y6nVMADs2UaupXQsbMn",
                "kesan": "Abangnya baik dan keren banget dengan prestasinya",
                "pesan": "Semoga terus berkembang, semakin sukses, dan semua target akademik maupun organisasi dapat tercapai.",
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=12KQ8AskB-mHUHwCpfgN4b71bSDkgO9yh",
                "kesan": "Kakaknya cantik, baik dan ramah",
                "pesan": "Semoga selalu bahagia, kuliahnya lancar, dan semua rencana baiknya berjalan sesuai harapan.",
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VUPKQ84sBNJKudJSRGccH9PJ8PCH4VxM",
                "kesan": "Orangnya keren dan baik saat diajak berinteraksi.",
                "pesan": "Semoga kuliahnya lancar dan sukses dalam setiap langkah.",
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1nX3D42DsXrliwL-oZBvgLzYOMY8x-ow6",
                "kesan": "Abangnya tegas dan baik",
                "pesan": "Tetap semangat menginspirasi banyak orang ya abang, semoga sukses selalu menyertai abang.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_mikfes()

elif menu == "Departemen Eksternal":
    def departemen_eksternal():
        kating_data = [
              {
                "nama": "Arini Puteri Elandra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1vxR2-e9zp22OreCgUQGRKPtKqyyy-Kh1",
                "kesan": "Sosok yang terlihat seperti wanita karier: berprestasi, tegas, dan punya jiwa kepemimpinan.",
                "pesan": "Semoga tugas akhirnya lancar dan semua rencana ke depannya dimudahkan.",
            },
            {
                "nama": "Nabyla Sharfina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1nMCr_rGuh22xU5BF3HTOfHc6Xtfji4xC",
                "kesan": "Orangnya manis dan sangat membantu saat mengasisteni praktikum.",
                "pesan": "Semoga semua keinginan baiknya segera terwujud.",
            },
            {
                "nama": "Khoirul Muttoharoh",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=14DxNrIeUtsacPVxvHZEFPKqJOKB30U8V",
                "kesan": "Orangnya lucu, gemas, dan keren karena berhasil lolos PIMNAS.",
                "pesan": "Semoga perjuangan di PIMNAS berjalan lancar dan membawa hasil terbaik.",
            },
             {
                "nama": "Aditya Taufiqurrohman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Orangnya seru dan asik, terutama saat kegiatan PPLK.",
                "pesan": "Semoga selalu dikelilingi hal-hal baik dan sukses dalam kuliahnya.",
            },
            {
                "nama": "Indah Khairunnisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VJAQ1KuK_lY8_9hlLgKeOZlNsyjXUnTF",
                "kesan": "orang indah seperti namanya, senang bisa mengenal sosok yang aktif di Hublu.",
                "pesan": "Semoga energinya selalu terjaga dan tugas-tugasnya diselesaikan dengan lancar.",
            },
            {
                "nama": "Bima Ekayasa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CKCsPp4GZ2vpvILAdYYjc-p4St_Z9rwK",
                "kesan": "banyak pengalaman dan ilmu yang bisa dipelajari dari abangnya.",
                "pesan": "suskes terus setiap hal yang dilakukan dan semoga selalu dikelilingi hal-hal baik.",
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1LwUuhiEQJuwDRrw0U02z0e02Gkxw5Vlu",
                "kesan": "Hobinya unik dan menunjukkan bahwa orangnya punya banyak ide menarik.",
                "pesan": "Semoga semua urusan kuliahnya lancar dan rencana-rencananya berjalan baik.",
            },
            {
                "nama": "Adinda Deswita Maharani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1iTcx4gS_jJSlhYJ3k_XTp8vWqPcRgHVy",
                "kesan": "Orangnya cantik dan punya aura yang menyenangkan saat dilihat.",
                "pesan": "Semoga urusan akademik, organisasi, dan skripsinya dilancarkan sampai selesai.",
            },
            {
                "nama": "Yollanda Agustina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fFgMAIxXnOn6PLQrAYkF4wKxwnq_cqSW",
                "kesan": "Mentor yang baik, ceria, dan mampu membuat suasana belajar terasa menyenangkan.",
                "pesan": "Semoga urusan kuliah dan skripsinya dilancarkan sampai selesai.",
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1OiiYgBwABGaTKs675dG5Mg6hr1QB_ePg",
                "kesan": "keren banget kakaknya bisa jadi mentor tensor yang sangat baik",
                "pesan": "sehat terus kak dan semoga tetap menjadi orang yang menginspirasi",
            },
            {
                "nama": "Alfaya Abiyyi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1USivi188vD2xFXLK8-42NIvU6c-nED1F",
                "kesan": "Hobinya unik dan cukup mengundang selera untuk ikut mencoba.",
                "pesan": "Semoga tugas-tugas kuliahnya lancar dan selalu diberi semangat.",
            },
            {
                "nama": "Asri Meilani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PAertu6h93MyrNAMj9-yr1SDVLvH0B0d",
                "kesan": "Orangnya cantik, baik hati, dan punya aura yang menyenangkan.",
                "pesan": "Semoga selalu bahagia, ceria, dan lancar menyelesaikan tugas-tugasnya.",
            },
            {
                "nama": "Ahmad Rizky",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1eAWEGnIqZWue2IPnPDTSj06VpDCa7qD3",
                "kesan": "Keren Abang dengan segala prestasinya",
                "pesan": "Tetap semangat untuk Abang dalam menyelesaikan tugas-tugas kuliahnya",
            },
            {
                "nama": "Selma Siti Aisyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1BfXc4wG3mwN6JGNIctKWGn_XJAAB3OoN",
                "kesan": "Orangnya cantik dan punya senyum yang manis.",
                "pesan": "Semoga semester akhirnya lancar dan tidak terlalu banyak revisi.",
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1xRRTzUR4eBdVcrYzXUUOHo54I8k0P3ud",
                "kesan": "Orangnya lucu, ramah, dan menggemaskan.",
                "pesan": "Semoga tugas-tugas kuliahnya lancar dan selalu diberi semangat.",
            },
            {
                "nama": "Fathya Intami Gusda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=16NW22awio1qnU9JfH4pUaDcv8YC2bkg3",
                "kesan": "Orangnya ceria dan energinya terasa saat diajak berbicara.",
                "pesan": "Semoga selalu bahagia dan semangat menjalani hari-harinya.",
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Ue1YMgA7TELYLudkbRvP7M1ITB1Okc1c",
                "kesan": "Orangnya baik, ramah, dan hobinya bisa menjadi motivasi.",
                "pesan": "Semoga semester akhirnya lancar tanpa kendala.",
            },
            {
                "nama": "Danil N Fadillah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WJpcMaU9tmXgJD3nV9L5wXJxYBApN_YK",
                "kesan": "Ternyata sosok yang berprestasi dan menarik untuk diajak berbicara.",
                "pesan": "Semoga selalu sehat, termasuk menjaga ikan cupangnya, dan sukses dalam kuliahnya.",
            },
            {
                "nama": "Favian Arkaanda",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JTUM6ff4pxcISoHDHVt0bl12ZYd62KZZ",
                "kesan": "Orangnya cepat tanggap dan selalu membantu ketika ada yang sakit selama rangkaian.",
                "pesan": "Semoga selalu bahagia dan bisa bermain badminton lagi bersama keluarga kecil Tensor.",
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1JEl_rdCEuiweoltl0E1iNpYGz0KwaXU7",
                "kesan": "Awalnya terlihat galak, tetapi ternyata asik saat diajak mengobrol.",
                "pesan": "semoga dilancarkan setiap rencananya dan tetap semangat menjalani kuliah.",
            },
            {
                "nama": "Muhammad Rizaldi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=156EUsu_083tb8mj7q____qkDAfqQpM7W",
                "kesan": "Orangnya asik dan selalu punya lelucon untuk mencairkan suasana.",
                "pesan": "Semoga selalu bahagia dan sukses menjalankan tugas sebagai MC.",
            },
            {
                "nama": "Saskia Nova Magdalena",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1WL6vDge8jIdcFf7KTES7pzccGVkle6Ix",
                "kesan": "Orangnya cantik, lucu, dan ramah.",
                "pesan": "Semoga tugas-tugas kuliahnya lancar dan selalu diberi semangat.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_eksternal()

elif menu == "Departemen Internal":
    def departemen_internal():
        kating_data = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1MVzFHc7rqqdicj2dIu9kB6harzvOL46B",
                "kesan": "Abang adalah sosok yang hangat, merangkul, dan peduli dalam menjaga keharmonisan serta hubungan di internal Himpunan",
                "pesan": "Semoga sukses selalu, baik dalam akademik maupun organisasinya.",
            },
            {
                "nama": "Kharisma Mustika Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Orangnya cantik, lucu, dan menyenangkan.",
                "pesan": "Semoga kuliahnya lancar; kelulusan sudah semakin dekat.",
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YFpottMplvXmejq6ZTYPCYULuKpLidF2",
                "kesan": "Orangnya ekstrovert, ceria, dan punya senyum yang manis.",
                "pesan": "Semoga selalu dikelilingi hal-hal yang membuatnya bahagia.",
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HaVGrEpYuh7D6ouArjB2wGpoHgQPG6Cj",
                "kesan": "Orangnya baik, asik, dan ramah saat diajak berinteraksi.",
                "pesan": "Semoga terus menjadi versi terbaik dari diri sendiri.",
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Bb-6WWhPkbmRxHjQAqwx4EcruiremB9c",
                "kesan": "Orangnya santai, keren, dan terlihat percaya diri, terutama saat kegiatan Damaskus.",
                "pesan": "Semoga kuliahnya lancar, sehat selalu, dan semakin sukses ke depannya.",
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1B7wtLJ1JLUlcqAoFxAnHMga8il_yyAvs",
                "kesan": "Orangnya kalem, ramah, dan mudah berbaur dengan siapa saja.",
                "pesan": "Semoga selalu sehat, dikelilingi orang baik, dan semua urusannya dimudahkan.",
            },
            {
                "nama": "Cerine Sihotang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1KWGDWQ9Lu90pimSPSey4ySJ2yI7NrXrm",
                "kesan": "kakaknya baik dan ceria asik setiap kali diajak ngobrol",
                "pesan": "ceria terus kakak dan semoga selalu sehat dan sukses kuliahnaya",
            },
            {
                "nama": "Jaya Saputra Tamba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Bkajl0ojszLyUcSCOkRvjl8igGZlR5Q5",
                "kesan": "Orangnya seru dan jago bermain basket.",
                "pesan": "Semoga semakin sukses dan kemampuan basketnya terus berkembang.",
            },
            {
                "nama": "Najla Nursyifa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Tk8J-WZAV68kP68W62m6baMApy7YBrnz",
                "kesan": "Orangnya baik, ramah, dan mudah membuat suasana nyaman.",
                "pesan": "Semoga semua keinginan baiknya segera tercapai.",
            },
            {
                "nama": "Rozak Ramdani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1_Py8tyQnweuWrRkeFqPEbb-9zF8XHNLX",
                "kesan": "Orangnya asik, baik, dan punya senyum yang menenangkan.",
                "pesan": "Semoga selalu dikelilingi hal-hal baik.",
            },
            {
                "nama": "Teresa Christiani Purba",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1eR5HPivFpO3BQrAvqBZefpvFnzPZWZp8",
                "kesan": "Orangnya cantik, gemas, dan seru diajak bercerita.",
                "pesan": "Semoga lulus tepat waktu dan selalu diberi kelancaran.",
            },
            {
                "nama": "Audina Fitria",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Orangnya lucu, baik, dan sangat ramah.",
                "pesan": "Semoga selalu berada di lingkungan yang baik dan menyenangkan.",
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=19V56sUKM2tQovmLtM5zYeiaH5oqu3MZD",
                "kesan": "Kakaknya baik dan asik sekali",
                "pesan": "Semangat terus, semoga makin sukses dan selalu sehat.",
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Orangnya lucu, baik, dan ramah.",
                "pesan": "Semoga terus berkembang, sukses, dan sehat selalu.",
            },
            {
                "nama": "Muhammad Harvinsyah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SfnupAYZDDgJ9kV-d196Rlay8uuj12uy",
                "kesan": "Orangnya baik dan sedikit pendiam, tetapi tetap menyenangkan saat diajak berbicara.",
                "pesan": "Semoga semua keinginan baiknya segera tercapai.",
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QdvJ4Nb6oWtyoRxAZUWfmbz_B-sypcLL",
                "kesan": "Wajahnya membawa kesan teduh dan menyenangkan.",
                "pesan": "Semoga kuliahnya lancar dan bisa terbang setinggi mungkin.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_internal()

elif menu == "Departemen SSD":
    def departemen_ssd():
        kating_data = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1R8Wy7cE9xUy-AMRdH0IIt9-79a_i-65R",
                "kesan": "Abangnya baik dan humoris sangat super percaya diri",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Orangnya cantik, baik, humoris, dan ramah saat diajak berinteraksi.",
                "pesan": "Semoga kuliahnya lancar dan bisa lulus dengan hasil yang membanggakan.",
            },
            {
                "nama": "Afifah Fauziah",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lF9LdQhbbJTYMMvysWqv1PiL2mfCYJYc",
                "kesan": "Orangnya baik banyak memberi ilmu.",
                "pesan": "Semoga kuliahnya lancar hingga lulus.",
            },
            {
                "nama": "Anadia Carana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1fKDMK8NirJLg1l0N1l7SJJwk9c_pFHRY",
                "kesan": "Orangnya cantik, baik, dan ramah sehingga nyaman diajak berkomunikasi.",
                "pesan": "Semoga kuliahnya lancar dan semua rencana baiknya dimudahkan.",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1NjuVnrFPvjfev7VGG158MDmvimszNI4W",
                "kesan": "Orangnya baik dan tenang saat diajak berinteraksi.",
                "pesan": "Semoga urusan akademik, organisasi, dan skripsinya dilancarkan hingga lulus.",
            },
            {
                "nama": "Layina Ropiqo",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Gj2hkxcn2ug-veMcbEUrFl02NzoM1zQh",
                "kesan": "Kakaknya lucu bestie banget sama kak talitha",
                "pesan": "Semangat buat kuliahnya, sampai lulus",
            },
            {
                "nama": "Mochammad Iqbal Az-Zahir",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=157GSfwfZkuVkSBT9bwoRhuo_bkOzj0Nx",
                "kesan": "Orangnya ramah, humoris, dan mudah membuat suasana menjadi lebih santai.",
                "pesan": "Semoga kuliahnya lancar dan semua targetnya bisa tercapai.",
            },
            {
                "nama": "Talitha Justine",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1ecn-_o864h6AXhb-6VcA0wmupO7Qo-Im",
                "kesan": "kakaknya imut, dan lucu pas banget jadi bestie sama kak layina",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus",
            },
            {
                "nama": "Abdillah Fikri Al Pome",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1O8NA8kxOEErJhQsaB8fTo2B8eKwZ8o3L",
                "kesan": "Orangnya keren dan sangat percaya diri.",
                "pesan": "semoga keterima di bloomberg ya bang.",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dd23QJNHZPt4DVRNCtwGK4cbuCpr66Wm",
                "kesan": "orangnya juga baik dan ramah, suka bercanda.",
                "pesan": "Semoga urusan akademik dan kuliahnya dilancarkan hingga lulus.",
            },
            {
                "nama": "Anggun Nita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HmSGwQfn6RLLv1FpaQ1hKk6itxQXn5kX",
                "kesan": "Kakaknya cantik dan manis",
                "pesan": "Semangat buat kuliahnya, sampai lulus",
            },
            {
                "nama": "Della Anisa Fitri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1zB4AxmLRfov0Zxo1ylNB9wn6VXB2VB1P",
                "kesan": "orangnya lucu kirain judes ternyata asik dan ramah",
                "pesan": "Semangat terus kak jualannya semoga jadi entrepreneur",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_ssd()

elif menu == "Departemen Medkraf":
    def departemen_medkraf():
        kating_data = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1lzH2VKDjgjP3N_QrdFwA5c_5lo4gQMul",
                "kesan": "Orangnya lembut, tenang, dan punya pembawaan yang nyaman. ",
                "pesan": "Semoga selalu dikelilingi hal-hal baik, kuliahnya diberi kelancaran, dan setiap langkah yang dipilih membawa ke tempat yang diinginkan.",
            },
            {
                "nama": "Donna Maya Puspita",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Z3peEyRLbIu4MwIEwwcMPuwg7cbhbq3M",
                "kesan": "Tutor LMD yang keren; cara menjelaskan materinya mudah dipahami.",
                "pesan": "terus semangat berbagi ilmu dan lancar terus kuliahnya",
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1PfKB9wdjwrKEwg2iSuoGbg4ZOb2oTlUk",
                "kesan": "orangnya kelihatan pendiam dan berwibawa, dan ternyata memang begitu",
                "pesan": "semangat kuliahnya sampai wisuda dan lancar dan semua perjuangannya segera berbuah hasil.",
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Pertama kali melihatnya saat PPLK, pembawaanya manis, santai, dan mudah membuat orang tertarik.",
                "pesan": "Semoga hari-harinya selalu dipenuhi hal yang disukai, kuliahnya lancar, dan semua impian kecil maupun besarnya bisa tercapai.",
            },
            {
                "nama": "Raihana Adelia Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13_IDzBCC65we1oJPNu75Gl53GRLXYlf1",
                "kesan": "Orangnya cantik, manis, dan ramah.",
                "pesan": "Semoga seluruh urusan akademik, organisasi, dan skripsinya dilancarkan hingga lulus.",
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Nrxa-cXqvlvx4txMitCKPmiRb6NMv4Oh",
                "kesan": "Kakaknya cantik dan manis",
                "pesan": "Semoga selalu punya alasan untuk tersenyum, dimudahkan dalam setiap urusan, dan terus berkembang menjadi versi terbaik dirinya.",
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1NGItYm37OnJ4oVogKZSvTHjiAdi_fbLe",
                "kesan": "Orangnya mudah akrab dan seru, spontan, agak jahil juga biar gak sepi.",
                "pesan": "Semoga tetap menjadi diri sendiri, selalu bertanggung jawab, dan semua rencana baiknya berjalan dengan lancar.",
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1dJtchK-bdRWLsdWODxqaf0ac56PWF0wF",
                "kesan": "Orangnya keren dan ramah banyak yang suka.",
                "pesan": "tetap ceria bang jangan lupa jaga kesehatan.",
            },
            {
                "nama": "Allisha",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1rDG7cQGfGJPjr8Cljx4Cb-gaVs5iKgh9",
                "kesan": "Kakaknya cantik dan manis, pembawaannya santai dan unik.",
                "pesan": "Semoga selalu diberi ketenangan, banyak pengalaman seru, dan keberanian untuk mencoba hal-hal baru yang membawa kebahagiaan.",
            },
            {
                "nama": "Alya Ramadhanti",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17bWEIIr6R3fiS6vUxCBatRyTPzGjVnP2",
                "kesan": "Kakaknya cantik, ramah dan manis",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus.",
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qUYUQ8F50FcMm9eS1RpNDQlTStyXJtvE",
                "kesan": "Orangnya cantik dan punya aura yang menyenangkan dan keliatan ambis juga.",
                "pesan": "Semoga kerja kerasnya selalu membuahkan hasil, tetap diberi semangat saat menghadapi kesulitan, dan sukses dalam setiap langkahnya.",
            },
            {
                "nama": "Difanya Husakina",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1Vn1uCdEWNbcjKegulErVidotkiBNYzoO",
                "kesan": "Orangnya memiliki pembawaan yang adem dan menenangkan, kakaknya juga ceria.",
                "pesan": "Semoga selalu diberi ketenangan hati, dikuatkan dalam setiap proses, dan dipertemukan dengan banyak kebaikan.",
            },
            {
                "nama": "Nazlah Auliya",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1J8cISb-Jg0FB_4U5gG1zJ0b8p3MlfwCw",
                "kesan": "Orangnya terlihat ceria, aktif, dan punya energi yang menyenangkan.",
                "pesan": "Semoga selalu sehat, semakin percaya diri, dan semua target yang sedang dikejar dapat tercapai dengan hasil yang membanggakan.",
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Abangnya baik, humoris, dan ramah",
                "pesan": "semangat terus hari-harinya dan banyak makin banyak melakukan kegiatan lagi",
            },
            {
                "nama": "Edsel Adya Pradipta",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1CPV6OJJQdQpgjfCYLe7NAA4AVRnty0ai",
                "kesan": "orangnya kelihatan santai dan asik, dan gagah juga ",
                "pesan": "semangat terus bang dan lancarnya terus kuliahnya bang dan semoga selalu sehat",
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17uHVMbU4dFUREfGH7kpOfT2hjxgFjul4",
                "kesan": "Orangnya manis, lembut, dan punya aura yang membuat orang gampang merasa nyaman.",
                "pesan": "Semoga selalu punya waktu untuk beristirahat tanpa kehilangan semangat mengejar impian, dan semua urusannya dimudahkan.",
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1QAMPxiQd3NZATApP7thrxyqz0eLEb0J2",
                "kesan": "Orangnya kreatif, tenang, dan punya banyak cara untuk mengekspresikan diri.",
                "pesan": "Semoga ide-idenya terus mengalir, karyanya semakin berkembang.",
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1e1hGT22hIFVgxfxM0L8Mj9msD4S0I1Ou",
                "kesan": "Orangnya cantik, ramah, dan baik.",
                "pesan": "Semoga urusan akademik dan skripsinya lancar sampai selesai.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_medkraf()

elif menu == "Departemen MINBAK":
    def departemen_minbak():
        kating_data = [
            {
                "nama": "Kevin Antonio Junior",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1nPAxn1C9gjV9h6AsgXdCebN3gkLbrW5a",
                "kesan": "Tidak menyangka kepala departemen Minbak ternyata sekeren itu.",
                "pesan": "Semoga kuliahnya lancar dan tidak ada mata kuliah yang harus diulang.",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=13w3rjFhDeCD9EGHxXtVmb-_FFX_Z-3D1",
                "kesan": "Orangnya asik dan punya pembawaan yang membuat orang mudah terkesan.",
                "pesan": "Semoga selalu berhati-hati, sehat, dan dimudahkan dalam setiap urusan.",
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "kesan": "Orangnya baik dan mudah berbaur dengan siapa saja.",
                "pesan": "Semoga selalu dikelilingi hal-hal baik dan sukses dalam kuliahnya.",
            },
            {
                "nama": "Muhammad Ridwan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1TPiyWB8b5BRgti8sy7zPcjFyl4KpsJ_r",
                "kesan": "Orangnya asik, baik, dan ramah.",
                "pesan": "Semoga selalu dikelilingi hal-hal baik.",
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1YbDHbOj5H9taraAlhYrJ7o9CFqEW_R7l",
                "kesan": "Orangnya baik dan sangat ramah.",
                "pesan": "Semoga semua keinginan baiknya segera tercapai.",
            },
            {
                "nama": "Dafa Elpriza",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1VWGaStk9tHfIidxaM7ZaL_YmVRXAKRuX",
                "kesan": "Sering terlihat di Damaskus dan ternyata aktif di Minbak, keren juga.",
                "pesan": "Semoga tetap semangat menjalankan amanah dan menjadi tenaga medis yang hebat.",
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1E2rcu9WkEIjc1s351clJA4czRV1k3eE0",
                "kesan": "Orangnya manis dan punya aura yang menyenangkan.",
                "pesan": "Semoga kuat menjalani setiap proses dan rintangan ke depannya.",
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=17HezUEPcI6cJu_e8a-GU0KmYP2xzP3wi",
                "kesan": "Abangnya keren, baik hati, sangat membantu pemahaman ketika praktikum Alpro.",
                "pesan": "Semoga sukses terus dan suatu hari nanti bisa menjadi asisten praktikum yang menginspirasi banyak orang.",
            },
            {
                "nama": "Juwita Sari",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1uw7I6LSbudqCcxhuEAZ451bvx0X4aude",
                "kesan": "Orangnya manis, cantik, dan sering berbagi cerita yang bisa dipelajari.",
                "pesan": "Semoga tetap kuat menghadapi setiap proses dan selalu bahagia.",
            },
            {
                "nama": "Andra Ilham Bintang",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1HzIWQ92WijpFedIyz3XBHhcval8-mpnt",
                "kesan": "Coach basket yang seru dan asik; selalu membuat latihan terasa menyenangkan.",
                "pesan": "Semoga semakin sukses dan kemampuan bermain basketnya terus berkembang.",
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1c4nFhCM-6XXXta9neo30GW8LhYnwIztU",
                "kesan": "Orangnya kocak, baik, dan mudah membuat suasana menjadi cair.",
                "pesan": "Semoga selalu dikelilingi hal-hal baik dan sukses dalam kuliahnya.",
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1qYqOPavgV3qBUqd_DiYZMkAAFjGuZ8sH",
                "kesan": "orangnya kelihatan pintar dan rajin, ceria juga ternyata.",
                "pesan": "Semoga tugas di Minbak lancar dan cita-cita besarnya bisa tercapai.",
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1SLUNCloleZKxBCSl7ofi8riWtexSyHLa",
                "kesan": "Orangnya kalem, baik, dan humble.",
                "pesan": "Semoga selalu sehat dan kuliahnya berjalan lancar.",
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1GObS3qxJtXPn0waG235Q8hql75xyn1Or",
                "kesan": "Pertama kali lihat saat tampil menari, bagus banget kak gerakannya seindah itu.",
                "pesan": "Semoga terus mengembangkan kemampuan menari dan tetap percaya diri.",
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "link_gdrive": "https://drive.google.com/uc?export=view&id=1tdaj4rZGtQKor7y0EEycXlg28rzqTBC1",
                "kesan": "Orangnya keren dan terlihat punya semangat kuat saat menjalankan tugas di Minbak.",
                "pesan": "Semoga selalu sehat, kuliahnya lancar, dan terus berkembang dalam menjalankan amanah.",
            },
        ]
        display_kating(kating_data, departemen=menu)
    departemen_minbak() 