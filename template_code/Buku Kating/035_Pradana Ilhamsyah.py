import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
            "Departemen Minbak",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#8D4C06"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"NIM: {data_list[i]['Nim']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobbi: {data_list[i]['Hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['Sosmed']}")
            st.write(f"Kesan: {data_list[i]['Kesan']}")
            st.write(f"Pesan: {data_list[i]['Pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")

menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jeqH0Z7W_JS6vlWK9ki8LTvsWGGVdiUD",
            "https://drive.google.com/uc?export=view&id=1RmPw8ctkawpUuO-QA6UUKpaOx_VHQqYD",
            "https://drive.google.com/uc?export=view&id=1Oe6QiOfr1Tgj8JTWG30af7IzCCUF7AHy",
            "https://drive.google.com/uc?export=view&id=1gDIopz-t-gUs5v7tcNs7QbAnNjKSYECN",
            "https://drive.google.com/uc?export=view&id=1ApobNKjzIwdzM5GRajQe068QNF6PhVNb",
            "https://drive.google.com/uc?export=view&id=16-J9fycfkd28V2ERSOm7nUmgNaNbJRJ3",
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "Nim": "123450103",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "push rank sampe imo",
                "Sosmed": "@jars_mrp",
                "Kesan": "Abangnya keren, asik waktu jadi pemateri",  
                "Pesan":"Semangat terus bang semoga skripsinya dimudahkan"
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "Nim": "123450066",
                "Umur": "22",
                "Asal":"Riau",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "Zikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Abangnya asik banget",  
                "Pesan":"Semangat bang semoga dimudahkan segala urusan"
            },
            {
                "Nama": "Efi Defiyati",
                "Nim": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobbi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "Kakaknya baik dan asik",  
                "Pesan":"Semangat terus kak"
            },
            {
                "Nama": "Qois Olifio",
                "Nim": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio_ ",
                "Kesan": "Abangnya keren dan kalem",  
                "Pesan":"Semangat bikin bikin proposal atau surat bang"
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "Nim": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Bertemu Kesekjenan",
                "Sosmed": "@hafsafadhilaa",
                "Kesan": "Kakaknya baik, kalem, asik",  
                "Pesan":"Semangat terus kak"
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "Nim": "123450004",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Airan",
                "Hobbi": "Mintain Duit",
                "Sosmed": "@luthfiaarmdhni ",
                "Kesan": "Kakaknya lucu, baik, keren, asik juga",  
                "Pesan":"Semoga dimudahkan selalu ya kak segala urusannya"
            },                                     
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YWxjnvF0O4t7fb0xjbGmRBAlazHk2TBa",
            "https://drive.google.com/uc?export=view&id=1YrSpM3NSbRDH9wePa4BBh9WDldRZzr7g",
            "https://drive.google.com/uc?export=view&id=1jKL-dGXaIhmgRwDV7vO42SL3Wn4umsdg",
            "https://drive.google.com/uc?export=view&id=18elEeTvoHTgKnytV-0DrNnPcGuFiNYKZ",
            "https://drive.google.com/uc?export=view&id=1cVgnjPgY-L-GfettMvkwPIz58FvA0tz4",
            "https://drive.google.com/uc?export=view&id=188BGrTzXSwKsWJh0PUQcwXRu5bQpwQuq",
            "https://drive.google.com/uc?export=view&id=1wdIQKzGuL2GVGrY_Z9Motg4F-FBO-APB",
            "https://drive.google.com/uc?export=view&id=1N6wlbj852GpqKvlUJkSkglJt7hQWTCg5",
            "https://drive.google.com/uc?export=view&id=1OZC9wZy_baV9GGj6dzGENk7bEnVU2bMw",
            "https://drive.google.com/uc?export=view&id=1ovEvA8vPoRXTg6BYur8Fb100cH7qAGJc",
        ]
        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "Nim": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobbi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kakaknya cantik, baik, kalem",
                "Pesan": "Sehat selalu kak, semoga lancar skripsinya"
            },
            {
                "Nama": "Helmy Surya Pratama",
                "Nim": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobbi": "Ngesen kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "Abangnya seru, asik, lucu",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "Nim": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah Kamar Biwa",
                "Hobbi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Abangnya baik, asik",
                "Pesan": "Semoga selalu dimudahkan bang"
            },
            {
                "Nama": "Suci Aulia",
                "Nim": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota Baru",
                "Hobbi": "Mancing",
                "Sosmed": "@sciia_",
                "Kesan": "Kakaknya kalem dan baik",
                "Pesan": "Sehat selalu kak"
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "Nim": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Abangnya asik, keren, pinter juga",
                "Pesan": "Sehat selalu bang, semangat terus juga"
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "Nim": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobbi": "Nonton",
                "Sosmed": "@lia,h_264",
                "Kesan": "Kakaknya lucu, asik banget",
                "Pesan": "Semoga kuliahnya lancar ya kak"
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "Nim": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobbi": "Mendokumentasi Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Kakaknya lucu, keren banget",
                "Pesan": "Semoga bahagia terus kak"
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "Nim": "124450114",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Lampung Timur",
                "Hobbi": "Giring Ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Abangnya keren, asik dan ramah",
                "Pesan": "Semoga sukses bang"
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "Nim": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobbi": "Membaca",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Kakaknya cantik, ramah, baik",
                "Pesan": "Semangat terus kak, semoga kuliahnya lancar"
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "Nim": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobbi": "Baca Buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu dan semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Vzdn1ByxCGfHnaAu9L6BKO6Td8Xo34aG",
            "https://drive.google.com/uc?export=view&id=1C7Ml6rptyTyXvxYnoZ2nSQvSnvig4Cag",
            "https://drive.google.com/uc?export=view&id=1MwGM-Wu9kuUWUBh5Q9VkCBNONkcCKEon",
            "https://drive.google.com/uc?export=view&id=12UjmPRU4eHVs12zcUshB-hlWgJD66G2Q",
            "https://drive.google.com/uc?export=view&id=1TyPSvGXkHL5pWpN9h1etDEHKUMA0nqnc",
            "https://drive.google.com/uc?export=view&id=1lR0X5udbhAsTaIk8KWdzN7n2scoNTPNq",
            "https://drive.google.com/uc?export=view&id=1GkpUMLYG1GO3O22KoPD88zo3d0CTKAi7",
            "https://drive.google.com/uc?export=view&id=1Eub1924ILdQ6MaXjZgrML8yN5vR3X6s4",
            "https://drive.google.com/uc?export=view&id=1TmPYlIMksDlYWfXFM4rtPUa-AKWAv2K1",
            "https://drive.google.com/uc?export=view&id=1JPR1CGfBaZIl2C-iZLiAizHi2JS251sY",
            "https://drive.google.com/uc?export=view&id=1_cgs6SJLLcFk_yGsu5ScycMuC1Fbb01g",
            "https://drive.google.com/uc?export=view&id=1hEXa0nmiQvhRfPySNoDe-z9dAurgxY2T",
        ]
        data_list = [
            {
                "Nama": "Ihsan Maulana Yusuf",
                "Nim": "123450110",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Belwis",
                "Hobbi": "Mencari dan membaca jurnal, 2 minggu mewawancarai anak kader angkatan 25 Datavora tercinta, mencari pak Luki",
                "Sosmed": "@ihsan.myusuf",
                "Kesan": "Abangnya lucu dan asik",
                "Pesan": "Semangat skripsinya lancar bang"
            },
            {
                "Nama": "Hanifah Inaya Sani",
                "Nim": "123450123",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Memasak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu, semangat terus kak"
            },
            {
                "Nama": "Afifah Fauziah",
                "Nim": "123450002",
                "Umur": "19",
                "Asal": "Depok",
                "Alamat": "Belakang PB",
                "Hobbi": "Ngumpulin data sama nonton Marvel",
                "Sosmed": "@fifah.zy",
                "Kesan": "Kakaknya baik dan asik",
                "Pesan": "Semangat terus ya kak"
            },
            {
                "Nama": "Hasan Nur Ramadhan",
                "Nim": "124550012",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sebelah kost Ayake",
                "Hobbi": "Scroll Facebook",
                "Sosmed": "@hasan.ramadhan08",
                "Kesan": "Abangnya baik dan santai",
                "Pesan": "Semoga sukses bang"
            },
            {
                "Nama": "Layina Ropiqo",
                "Nim": "124550016",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Menonton Film",
                "Sosmed": "@lay.inr_",
                "Kesan": "Kakaknya ramah dan baik",
                "Pesan": "Semangat terus ya kak"
            },
            {
                "Nama": "Moch. Iqbal Az-Zahir",
                "Nim": "124450052",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Natar",
                "Hobbi": "Nonton Drakor",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Abangnya kalem dan baik",
                "Pesan": "Sehat terus bang"
            },
            {
                "Nama": "Talitha Justine",
                "Nim": "124450076",
                "Umur": "19",
                "Asal": "Padang, Sumatera Barat",
                "Alamat": "Pemda",
                "Hobbi": "Nonton",
                "Sosmed": "@talljtine_",
                "Kesan": "Kakaknya ramah dan baik",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Anadia Carana",
                "Nim": "123450019",
                "Umur": "21",
                "Asal": "Palembang",
                "Alamat": "Kost The Icon",
                "Hobbi": "Belajar",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakaknya pinter dan ramah",
                "Pesan": "Sukses terus kak, semoga kuliahnya lancar"
            },
            {
                "Nama": "Abdillah Fikri Al Pome",
                "Nim": "123450062",
                "Umur": "21",
                "Asal": "Oku, Sumatera Selatan",
                "Alamat": "Airan",
                "Hobbi": "Godain cewe bang Homey",
                "Sosmed": "@pomest_",
                "Kesan": "Abangnya lucu, asik dan seru",
                "Pesan": "Semangat terus bang, semoga skripsinya lancar"
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "Nim": "124550008",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Samping Kost Rafli",
                "Hobbi": "Fishing",
                "Sosmed": "@dhal_setiawan",
                "Kesan": "Abangnya baik dan asik",
                "Pesan": "Semoga sehat terus bang"
            },
            {
                "Nama": "Anggun Nita",
                "Nim": "124550009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobbi": "Menonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakaknya ramah dan baik",
                "Pesan": "Sehat selalu dan semangat terus kak"
            },
            {
                "Nama": "Della Anisa Fitri",
                "Nim": "124450095",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Margo Lestari",
                "Hobbi": "Lagi suka olahraga",
                "Sosmed": "@dellaansaftr",
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()


if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1haph1yjgTt4zMjBR_Fi1HXnQSRAWKNyo",
            "https://drive.google.com/uc?export=view&id=102MlvkZl8D12jmBeLNGU48NHtmeqhqsy",
            "https://drive.google.com/uc?export=view&id=16faGTeUC_8JB2eBQxT4VGAptIkaYe5tk",
            "https://drive.google.com/uc?export=view&id=1MbR9UFJ1jqiDAmwQn2Q4JpzCHfqtZcSG",
            "https://drive.google.com/uc?export=view&id=1KhvFeVfTPK6cngwdvOuwuA9G7dO4q1LB",
            "https://drive.google.com/uc?export=view&id=1R7mgyOfAA7vk3UQdJhPsodhjN9KPMlpR",
            "https://drive.google.com/uc?export=view&id=1cdbFn6KGCI4e7hhrXC6oBfg0nsg9RmUt",
            "https://drive.google.com/uc?export=view&id=18qlcr6JLfLH_RsOgRe_uzi5OfToEY3Eu",
            "https://drive.google.com/uc?export=view&id=10lXW-7cUNsz0GJXdNxRkkImxnTda5O8M",
            "https://drive.google.com/uc?export=view&id=1LlPgxZDgCpH5WkRrVdhYioPUwmyQnvx9",
            "https://drive.google.com/uc?export=view&id=1-3k7_F1E03TK-O5HGcMKd4H7PrMP4SiV",
            "https://drive.google.com/uc?export=view&id=1667yAukBh5t4wnCB58XRWHPwsNca2r4y",
            "https://drive.google.com/uc?export=view&id=1O0hCwksFjf8yrdLb6ZdjU9Bn3w9Tnzz_",
            "https://drive.google.com/uc?export=view&id=1PqvgDCX3_hTZQW8PpWnc0vyLRXCBZH6f",
            "https://drive.google.com/uc?export=view&id=1pnVI80APkEXGigHK3RyrGcFWFHZhIIeS",
            "https://drive.google.com/uc?export=view&id=1TsJpwz5F3znAeNdEKVgcE9JGi_GC1AuV",
        ]

        data_list = [
            {
                "Nama": "Haikal Fransisko Simbolon",
                "Nim": "123450106",
                "Umur": "20",
                "Asal": "Tangerang Kota",
                "Alamat": "Gerbang Barat",
                "Hobbi": "Begadang",
                "Sosmed": "@haikalsbln_",
                "Kesan": "Abangnya asik, seru di ajak diskusi",
                "Pesan": "Semangat di semester akhir ini bang"
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "Nim": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "Untung Suropati",
                "Hobbi": "Suka Menolong orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Ramah kakaknya, seru diajak diskusi",
                "Pesan": "Semangat menjalani kuliah kak"
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "Nim": "123450038",
                "Umur": "21",
                "Asal": "Kisaran",
                "Alamat": "Sukarame",
                "Hobbi": "Membaca Novel",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Asik banget kakanya",
                "Pesan": "Semangat untuk meraih mimpi"
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "Nim": "124450021",
                "Umur": "21",
                "Asal": "Kemiling",
                "Alamat": "Kemiling",
                "Hobbi": "Supporteran",
                "Sosmed": "@farhnghnii.",
                "Kesan": "Abangnya keren jago main alat musik",
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "Nim": "124450096",
                "Umur": "18",
                "Asal": "Indragirihulu",
                "Alamat": "Samping Kuburan",
                "Hobbi": "Sleep Call",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "kakaknya asik di ajak ngobrol",
                "Pesan": "Semangat kuliah kak"
            },
            {
                "Nama": "Cerine Sihotang",
                "Nim": "124450049",
                "Umur": "19",
                "Asal": "Semarang",
                "Alamat": "Belwis",
                "Hobbi": "Manjat Pohon Kelapa",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "Kakanya keren dan selalu semangat",
                "Pesan": "Semangat menjalani kuliah"
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "Nim": "124450094",
                "Umur": "21",
                "Asal": "Kisaran",
                "Alamat": "Pemda",
                "Hobbi": "Main Biola",
                "Sosmed": "@jay.saputra.tmb",
                "Kesan": "Abangnya asik, seru sekali kalo diajak ngobrol",
                "Pesan": "Semangat menjalani kuliah"
            },
            {
                "Nama": "Najla Nursyifa",
                "Nim": "124450051",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Belwis",
                "Hobbi": "Nonton asmr",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Ramah dan asik",
                "Pesan": "Semangat menjalani kuliah"
            },
            {
                "Nama": "Rozak Ramdani",
                "Nim": "124450100",
                "Umur": "19",
                "Asal": "Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobbi": "Badminton",
                "Sosmed": "@rozakramdani_",
                "Kesan": "Kalem seru diajak ngobrol",
                "Pesan": ""
            },
            {
                "Nama": "Teresa Christiani Purba",
                "Nim": "124450046",
                "Umur": "19",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobbi": "Memasak",
                "Sosmed": "@christiani8872",
                "Kesan": "Asik kakaknya",
                "Pesan": "Semangat nutorin RA kak"
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "Nim": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobbi": "Nonton MU",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Kalem dan keren",
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Audina Fitria",
                "Nim": "124450038",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobbi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Ramah kakaknya san seru",
                "Pesan": "Selalu semangat mengejar mimpi"
            },
            {
                "Nama": "Cika Adelia BR Marbun",
                "Nim": "124450107",
                "Umur": "20",
                "Asal": "Riau",
                "Alamat": "Samping Kuburan",
                "Hobbi": "Scroll tiktok",
                "Sosmed": "@cikambrn",
                "Kesan": "Asik dan seru kalo ngobrol",
                "Pesan": "Semangat terus kuliah"
            },
            {
                "Nama": "Gustin H Tampubolon",
                "Nim": "124450068",
                "Umur": "21",
                "Asal": "Sumut",
                "Alamat": "Airan",
                "Hobbi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "Asik dan seru kakanya",
                "Pesan": "Semangat mengejar mimpi"
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "Nim": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobbi": "Nangkap lele",
                "Sosmed": "@muhvinz_",
                "Kesan": "Keren abangnya dan seru",
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "Nim": "124450036",
                "Umur": "21",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobbi": "Main game di HP temen",
                "Sosmed": "@snasaa._",
                "Kesan": "kakaknya kalem dan asik",
                "Pesan": "Selalu semangat menjalani kuliah"
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    internal()


if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CFpXUfnTedITy-ap16RrJ7_DmEw_Ym_U",
            "https://drive.google.com/uc?export=view&id=1xBj_sVDPd9HlrczR8XkESe-p2d0SnLhE",
            "https://drive.google.com/uc?export=view&id=1bTj0_kyy0T9vl41j4JFLu84m1z038u9Z",
            "https://drive.google.com/uc?export=view&id=1QyYrEM7TaeKeNlLKwtnJ1l3Im2e3zsMv",
            "https://drive.google.com/uc?export=view&id=1QofZ_VgH4sO1aKq_bzkn-6cewH5l3XHL",
            "https://drive.google.com/uc?export=view&id=1iS4IVOzDwOGst2pXhjZh5blAVG7slaDm",
            "https://drive.google.com/uc?export=view&id=1WsJ8e-9kLlLkqXQSQ5tSeO0fkSG6x8nE",
            "https://drive.google.com/uc?export=view&id=1e-xIhBCEHm-zQBRBMfPCrygY5fmfzvd5",
            "https://drive.google.com/uc?export=view&id=1spvXvsQA9SR4ArLZyuXknnQ40I_Q4Go-",
            "https://drive.google.com/uc?export=view&id=1soxQ5Z71vFY8w0K43rM0zaQYo88ka1Os",
            "https://drive.google.com/uc?export=view&id=1HWstDQONJHEyy5dmxbISZrY1oLcdtiYD",
            "https://drive.google.com/uc?export=view&id=1AnzOQ2_fopyntaVtPFAZ8Q6amfgXKwts",
            "https://drive.google.com/uc?export=view&id=1TTUiL2eT7B1Jn3w_2q8hsWXK_783jDj4",
            "https://drive.google.com/uc?export=view&id=1YV77F0EVZjFIpGmILkodByfmWX553h0O",
            "https://drive.google.com/uc?export=view&id=11cJD3c4cPKpIgbZRQitkS89qf96AAAHB",
            "https://drive.google.com/uc?export=view&id=1YeoiQVFX3KGiyMIEymSiyAs9DihJZbz2",
            "https://drive.google.com/uc?export=view&id=1rXL5k09w0tU5WcJOAG3MuinrRiDGwpr2",
            "https://drive.google.com/uc?export=view&id=1AKyKJYJ89CJWFcjJPQlQyxTTv9PWf-bT",
        ]

        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "Nim": "123450082",
                "Umur": "20",
                "Asal": "Payakumbuh, Sumatera Barat",
                "Alamat": "Way Huwu",
                "Hobbi": "Musingin TA",
                "Sosmed": "@naylasalsabilaa._",
                "Kesan": "Keran kakaknya jago dalam media konten",
                "Pesan": "Semangat terus kuliahnya kak"
            },
            {
                "Nama": "Donna Maya Puspita",
                "Nim": "123450028",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Way Huwi",
                "Hobbi": "Berenang",
                "Sosmed": "@donnamaya.p",
                "Kesan": "Asik seru banget",
                "Pesan": ""
            },
            {
                "Nama": "Labo John Noel Napitupulu",
                "Nim": "123450037",
                "Umur": "20",
                "Asal": "Medan, Jakarta Utara, Palembang",
                "Alamat": "Way Huwi",
                "Hobbi": "Buka Tutup Laptop",
                "Sosmed": "@noerruuu",
                "Kesan": "Keren baik banget",
                "Pesan": "Selalu diberi kesahatan terus bang"
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "Nim": "124450050",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobbi": "Ballet",
                "Sosmed": "@anshtsyaaql",
                "Kesan": "Kakaknya asik banget",
                "Pesan": "Tetap semangat mengejar mimpi"
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "Nim": "124450104",
                "Umur": "18",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobbi": "Mancing emosi",
                "Sosmed": "felisyanbl",
                "Kesan": "Keren banget kakaknya dan asik",
                "Pesan": "Selalu semangat kak"
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "Nim": "124450031",
                "Umur": "18",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobbi": "Dukung silver arrow alias mercedes",
                "Sosmed": "@muh_razan_",
                "Kesan": "Asik banget kalo ngobrol",
                "Pesan": "tetap semangat untuk kuliah"
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "Nim": "123450086",
                "Umur": "17",
                "Asal": "Bali",
                "Alamat": "Airan",
                "Hobbi": "Nongkrong depan prodi",
                "Sosmed": "saniayyllstr",
                "Kesan": "asik di ajak diskusi keren banget",
                "Pesan": "Selalu tersenyum kak"
            },
            {
                "Nama": "Allisha",
                "Nim": "124450019",
                "Umur": "3 Tahun",
                "Asal": "Surga",
                "Alamat": "Rumah Asha",
                "Hobbi": "Ice skating",
                "Sosmed": "@aallishaa.aa",
                "Kesan": "kakanya asik banget",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Alya Ramadhanti",
                "Nim": "124450091",
                "Umur": "19",
                "Asal": "Jambi",
                "Alamat": "Airan",
                "Hobbi": "Jalan jalan dengan sepatu rodaku",
                "Sosmed": "@alya.rmdhnti",
                "Kesan": "Keren banget dan asik diajak ngobrol",
                "Pesan": "Selalu semnagat"
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "Nim": "124450097",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Pemda",
                "Hobbi": "Mengkoding",
                "Sosmed": "@bungaclrssf",
                "Kesan": "Asik kakanya, seru banget",
                "Pesan": "tetap happy terus kak"
            },
            {
                "Nama": "Difanya Husakina",
                "Nim": "124450043",
                "Umur": "7.137 hari per hari ini",
                "Asal": "Sumsel",
                "Alamat": "Kafe Kali",
                "Hobbi": "Bobo cantik",
                "Sosmed": "@difanyhsa",
                "Kesan": "Keren dalam mengambil gambar",
                "Pesan": "Tetap semangat terus ya kak"
            },
            {
                "Nama": "Nazlah Auliya",
                "Nim": "124450054",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Mimpi diatas kasur",
                "Sosmed": "nzlhauly_",
                "Kesan": "Selalu semangat kakanya",
                "Pesan": "Tetap jaga terus semangatnya"
            },
            {
                "Nama": "Raihana Adelia Putri",
                "Nim": "123450041",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Airan Raya 1",
                "Hobbi": "Menulis, membaca",
                "Sosmed": "n1tg._",
                "Kesan": "kakanya keren banget",
                "Pesan": "Selalu semangat"
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "Nim": "124450061",
                "Umur": "21",
                "Asal": "surabaya",
                "Alamat": "Sukarame",
                "Hobbi": "-",
                "Sosmed": "@daffascript_",
                "Kesan": "Abangya kalem tapi asik banget",
                "Pesan": "selalu semangat kuliah bang"
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "Nim": "124450098",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobbi": "Scrolling Fesbuk",
                "Sosmed": "@eddel_0712",
                "Kesan": "selalu semangat kakanya",
                "Pesan": "Semangat untuk menggapai mimpi kak"
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan",
                "Nim": "124450085",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobbi": "Nonton Star Wars",
                "Sosmed": "luciarachel_",
                "Kesan": "kakaknya asik banget",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "Nim": "124450124",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobbi": "Ngoding",
                "Sosmed": "@_shaazzh",
                "Kesan": "Jago banget ngoding",
                "Pesan": "Semangat untuk kuliah"
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "Nim": "124450112",
                "Umur": "19",
                "Asal": "Jabung",
                "Alamat": "Unila",
                "Hobbi": "Tidur",
                "Sosmed": "@xifasky",
                "Kesan": "Keren kakaknya",
                "Pesan": "Selalu semangat terus kak"
            }
        ]

        display_images_with_data(gambar_urls, data_list)

    medkraf()

if menu == "Departemen Minbak":
    def minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-4XBVKbYSNsDLXVz8ehir5IwBjla8pnP",
            "https://drive.google.com/uc?export=view&id=1RwDprjcSEUbCw3sArS6UbmzbdjvmXCRD",
            "https://drive.google.com/uc?export=view&id=1STT8aQ_eGBzdD5rRwT9kuWHDLvIkNmje",
            "https://drive.google.com/uc?export=view&id=1JmdcXS1lnde3rym9550YdCnBy1WA2_sL",
            "https://drive.google.com/uc?export=view&id=17nv29fxy3ZBu0vjqHg4pQoe1OXeCQLHs",
            "https://drive.google.com/uc?export=view&id=1NEFAxbar4d7gz0zbhVdtadqgfGkJTbxW",
            "https://drive.google.com/uc?export=view&id=1n-uPtCt5tcqfYtcVPtutriSKtlLkNgxP",
            "https://drive.google.com/uc?export=view&id=1d7ZJUlbKa2xRbUPH_Vgube-7zya7k0eC",
            "https://drive.google.com/uc?export=view&id=1HpBrSAOX4GFKUi6TUFIc73Hh81cJ72re",
            "https://drive.google.com/uc?export=view&id=1eGG5qCvCF8WrPiQ9JubQKRqqunl1q7BR",
            "https://drive.google.com/uc?export=view&id=1zT18veUoLB7gOCw_ouR1NKflm5ZO8wR8",
            "https://drive.google.com/uc?export=view&id=1hPxzzzZu5Eaibx4qpSYHLzHFFu05lfW-",
            "https://drive.google.com/uc?export=view&id=1BfqUDBLLT7gn6_9rqST68JeC1g87r7N-",
            "https://drive.google.com/uc?export=view&id=1XiW-1KFpwNzl3gLlb_1q-P4ARvXk-L3J",
            "https://drive.google.com/uc?export=view&id=1BtJsngFwofyO7vtMuHOafI2T4yJtdRfQ",
        ]
        data_list = [
            {
                "Nama": "Kevin Antonio Junior",
                "Nim": "123450009",
                "Umur": "21",
                "Asal": "Sulawesi Selatan",
                "Alamat": "Panjang, Bandar Lampung",
                "Hobbi": "Main gaplek",
                "Sosmed": "@kevinaj_",
                "Kesan": "Abangnya keren dan seru",
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "Nim": "123450046",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Way Dadi",
                "Hobbi": "Mendaki Gunung",
                "Sosmed": "@ferazkaa",
                "Kesan": "kakaknya ramah dan asik",
                "Pesan": "Selalu semangat mengejar mimpi kak"
            },
            {
                "Nama": "Ali Aristo Muthahhari Parisi",
                "Nim": "123450088",
                "Umur": "21",
                "Asal": "Lampung Timur",
                "Alamat": "Gang Sakum Belwis",
                "Hobbi": "Nonton F1",
                "Sosmed": "@ali_parisi3",
                "Kesan": "Abangnya keren dan pecinta F1",
                "Pesan": "Semoga jagoannya di F1 selalu menang bang"
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "Nim": "124450058",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Airan",
                "Hobbi": "Belajar",
                "Sosmed": "@aayuandriani_",
                "Kesan": "Asik kakaknya seruu",
                "Pesan": "Tetap semangat kuliah kak"
            },
            {
                "Nama": "Dafa Elpriza",
                "Nim": "124450024",
                "Umur": "21",
                "Asal": "Bandung",
                "Alamat": "Way Kandis",
                "Hobbi": "Main Futsal",
                "Sosmed": "@dafaelpriza_",
                "Kesan": "Abangnya jago futsal",
                "Pesan": "Selalu juaraa bang"
            },
            {
                "Nama": "Juwita Sari",
                "Nim": "124450066",
                "Umur": "19",
                "Asal": "Lampung Barat",
                "Alamat": "Pemda",
                "Hobbi": "Muter-muter",
                "Sosmed": "@ju.juwitaaa_",
                "Kesan": "Kakaknya kalem dan asik",
                "Pesan": "Semangat trus ya kak"
            },
            {
                "Nama": "Muhammad Afdal Lutfi",
                "Nim": "124450047",
                "Umur": "19",
                "Asal": "Lampung Tengah",
                "Alamat": "JL. Pulau Damar",
                "Hobbi": "Nemenin Bang Ridwan nonton tinju",
                "Sosmed": "@afdall.03",
                "Kesan": "Abangnya ramah dan seru",
                "Pesan": "Tetap semangat teruss"
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "Nim": "124550002",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Korpri",
                "Hobbi": "Pulang ke Metro",
                "Sosmed": "@sllbnzw_",
                "Kesan": "Kakaknya baik dan seru",
                "Pesan": "Tetap optimis kakk"
            },
            {
                "Nama": "Muhammad Ridwan",
                "Nim": "123450091",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Belwis",
                "Hobbi": "Nonton tinju",
                "Sosmed": "@mridwaan__",
                "Kesan": "Abangnya asik sekali di ajak diskusi",
                "Pesan": "Selalu sukses bang"
            },
            {
                "Nama": "Andra Ilham Bintang",
                "Nim": "124550060",
                "Umur": "18",
                "Asal": "Sumatera Selatan",
                "Alamat": "Kota Baru",
                "Hobbi": "Nemenin Bryan nonton tinju",
                "Sosmed": "@andra.lhm",
                "Kesan": "Abangnya baik dan ramah sekali",
                "Pesan": "Selalu semangat futsal bang"
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "Nim": "124550003",
                "Umur": "20",
                "Asal": "Nias",
                "Alamat": "Belwis",
                "Hobbi": "Live TikTok",
                "Sosmed": "@bryantel_",
                "Kesan": "Abangnya kalem baik dan jago musik",
                "Pesan": "Semangat musiknya bang"
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "Nim": "124550067",
                "Umur": "17",
                "Asal": "Surabaya",
                "Alamat": "Kemiling",
                "Hobbi": "Main beiblet",
                "Sosmed": "@meardhy_ghiyats",
                "Kesan": "Asik bangett",
                "Pesan": "semangat menggapai mimpi"
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "Nim": "124550055",
                "Umur": "20",
                "Asal": "Pringsewu",
                "Alamat": "Airan",
                "Hobbi": "Memasak",
                "Sosmed": "@indahjuliaa",
                "Kesan": "Selalu aktif dan baik kakaknya",
                "Pesan": "Semangat untuk meraih apa yang dimau kak"
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "Nim": "124550023",
                "Umur": "18",
                "Asal": "Nusa Tenggarang Barat",
                "Alamat": "Rajabasa",
                "Hobbi": "Nebang Pohon",
                "Sosmed": "@cacalvra",
                "Kesan": "Kakaknya asik dan baik",
                "Pesan": "Semangat terus dan sukses"
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "Nim": "124550089",
                "Umur": "20",
                "Asal": "Padang, Sumatera Barat",
                "Alamat": "Kota Baru",
                "Hobbi": "Bangun Pagi",
                "Sosmed": "@muhammdrafka_",
                "Kesan": "Abangnya kalem tapi asik",
                "Pesan": "Semangat futsalnya bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    minbak()

if menu == "Baleg":
    def legislatif():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BAJZq_nnGU8zvPdPHHo_ftDF2OFxSazL",
            "https://drive.google.com/uc?export=view&id=1-_ZRvTr2yLO1bvjSvE0mZEh4E6V1C41i",
            "https://drive.google.com/uc?export=view&id=1LpLN9qsDnMm3FKtJUCBYVM2XHNtQ0JSq",
            "https://drive.google.com/uc?export=view&id=1jzOMlsyetyTz1LPM_CFRg-ND7l2j3Oon",
            "https://drive.google.com/uc?export=view&id=1UJrwWkGE_wDot3Xq8hLpNkayn-h455-I",
            "https://drive.google.com/uc?export=view&id=19dkWLk5lm5PgL0oCJn7ZKa9pWl8lF6V7",
            "https://drive.google.com/uc?export=view&id=1hpv7IQtEISXAPpKjj3-vhVcsr3xkl5aQ",
            "https://drive.google.com/uc?export=view&id=1h40aquSzJYx8r_vXEnjS4z4rOQHA9p78",
            "https://drive.google.com/uc?export=view&id=1Uq5ltI69TfLGZFJGYWi0Fb3j77fxyjtF",
            "https://drive.google.com/uc?export=view&id=1vmjjQOsC9CoPjI7o93rL3k49rHOC2VIS",
            "https://drive.google.com/uc?export=view&id=1zuTpXSwNRljp1uO87CJczcQN6clXcQGT",
            "https://drive.google.com/uc?export=view&id=1X6Dbuee6WutfIKUfV_upSjpPqEX-Am3H",
        ]
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "Nim": "123450060",
                "Umur": "20",
                "Asal": "Kuala Lumpur",
                "Alamat": "GH",
                "Hobbi": "Ke Cafe",
                "Sosmed": "@iamridhomanik",
                "Kesan": "Abangnya keren banget, apalagi pas menyampaikan materi",
                "Pesan": "Semangat terus ketika kuliah"
            },
            {
                "Nama": "Juesi Apridelia Saragih",
                "Nim": "123450085",
                "Umur": "19",
                "Asal": "Sikawang",
                "Alamat": "Pelangi",
                "Hobbi": "Dengerin Lagu Pilihlah Aku dari Krisdayanti",
                "Sosmed": "@j_eesie",
                "Kesan": "Kakaknya baik dan asik",
                "Pesan": "Semangat kakk"
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "Nim": "123450023",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Ngidupin api Baleg di tiktok",
                "Sosmed": "@ddharu_",
                "Kesan": "Abangnya keren bangett",
                "Pesan": "Semangat menggapai mimpi bang"
            },
            {
                "Nama": "GH Mikael Niko AS",
                "Nim": "124450025",
                "Umur": "20",
                "Asal": "Pasir Sakti",
                "Alamat": "Jati Agung",
                "Hobbi": "Tidur",
                "Sosmed": "@me._kael",
                "Kesan": "Abangnya asik banget",
                "Pesan": "Semangat kuliah nya bang"
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "Nim": "124450015",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kedaton",
                "Hobbi": "Mancing",
                "Sosmed": "@syt.rifa",
                "Kesan": "Seru kakaknya",
                "Pesan": "Semnagat yaa kakk untuk menjadi apa yang di impikan"
            },
            {
                "Nama": "Givaro Ananta",
                "Nim": "123450078",
                "Umur": "21",
                "Asal": "Lampung Barat",
                "Alamat": "Sukabumi",
                "Hobbi": "minum kopi",
                "Sosmed": "@givarooo",
                "Kesan": "Abangnya keren, baik dan ramah",
                "Pesan": "Seamngat terus bang "
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "Nim": "124450042",
                "Umur": "18",
                "Asal": "kepulauan mentawai, lampung",
                "Alamat": "kadang di kos sekar kadang di kos putri",
                "Hobbi": "memanjat",
                "Sosmed": "@afghanisnt_",
                "Kesan": "kakaknya baik asik dan seru",
                "Pesan": "Semangat terus membimbing pandas kakkk"
            },
            {
                "Nama": "Hani Qurrota Aini",
                "Nim": "124450020",
                "Umur": "20",
                "Asal": "City Earth",
                "Alamat": "Sukarame",
                "Hobbi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "Kakaknya asik dan seru",
                "Pesan": "Selalu optimis kakk"
            },
            {
                "Nama": "Jeremia Halim",
                "Nim": "124450101",
                "Umur": "20",
                "Asal": "Cibaduyut",
                "Alamat": "Teluk",
                "Hobbi": "Bernyanyi",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Abangnya seru banget dan ramah",
                "Pesan": "Selalu menjadi ramah terus bang"
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "Nim": "123450073",
                "Umur": "21",
                "Asal": "jabar",
                "Alamat": "kotabaru",
                "Hobbi": "Lari",
                "Sosmed": "@monica_tjg",
                "Kesan": "Asik banget kakaknya",
                "Pesan": "Selalu semangat ya kakk"
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "Nim": "124450121",
                "Umur": "20",
                "Asal": "depok",
                "Alamat": "pemda raya",
                "Hobbi": "nge gym dan koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "Abangnya asik seru kalo di ajak diskusi seru",
                "Pesan": "Semangat menunggu one piece tamat bang"
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "Nim": "124450082",
                "Umur": "20",
                "Asal": "metro",
                "Alamat": "pemda",
                "Hobbi": "main sama kak nisa",
                "Sosmed": "@sekardnwp",
                "Kesan": "Kakaknya ramah dan asik",
                "Pesan": "selalu semangat dan optimmis kak"
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "Nim": "123450077",
                "Umur": "20",
                "Asal": "Pasay",
                "Alamat": "Belwis",
                "Hobbi": "nyapa angin",
                "Sosmed": "@nshaysk",
                "Kesan": "selalu happy kakaknnya",
                "Pesan": "happy terus ya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    legislatif()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qHcMVq9eWDEZRINfZJcrms54hwQFDgF4",
            "https://drive.google.com/uc?export=view&id=1ZM--44loMB_rZSQlxraNP4ZnAo6dlluQ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1o3koJ8lKalgglR-ooZtQ07ox4hoSgGJY",
            "https://drive.google.com/uc?export=view&id=1z_vjQTqDVCdzlmt1JaLqlaQDt05orIIP",
            "https://drive.google.com/uc?export=view&id=1CZe37if9TZOUqWWE3XHokAsyd1XwngQW",
            "https://drive.google.com/uc?export=view&id=1akv4gYbURW6RxKEYf9iHsHYvSbnAzf7h",
            "https://drive.google.com/uc?export=view&id=1pQCbAxfHcrySbR_tZYUVql_5qU4J6JaW",
            "https://drive.google.com/uc?export=view&id=1W0GVTz5bvqlf36DXwpAVanZQYZuyMujB",
            "https://drive.google.com/uc?export=view&id=1-oyJqoXTIEj4G1F4iCnzskq6-hhDiNRb",
            "https://drive.google.com/uc?export=view&id=1LnBr_tExFkh3yvd9fG0CvVZeMxQb_3Hl",
            "https://drive.google.com/uc?export=view&id=1h6v5DBwcyK1ttyoelJt05jEY83HnuCaL",
            "https://drive.google.com/uc?export=view&id=15oiZ28XLuXHSs_-M0kVfP0Y9F1AsHD_O",
            "https://drive.google.com/uc?export=view&id=1BaeLmneMQfO6u37CdrJ6oeQIRkIk2Fnv",
            "https://drive.google.com/uc?export=view&id=1_qN_AHjdzKfmP0-vgQ7rG4qkbhje0O9_",
            "https://drive.google.com/uc?export=view&id=1dTdJ1XECe1Wr0uaZ4MCwFew0_MqAxx96",
            "https://drive.google.com/uc?export=view&id=1551UlCa4q9qDSvs5pAw-DlwM6CZHNz5q",
            "https://drive.google.com/uc?export=view&id=1KMFyIsm8xYycGgFJhVSP9kFO-vej12zx",
            "https://drive.google.com/uc?export=view&id=1ow6-YzI3pD71QC2NaPasz1-OmeiQEXGL",
            "https://drive.google.com/uc?export=view&id=1PLUnrFbSYwNBJrl514k_f6_ZhjOS4ip7",
            "https://drive.google.com/uc?export=view&id=1mCIV-0sPlGA3WPs1g47U1HRPjyAyVZpD",
            "https://drive.google.com/uc?export=view&id=1CG2Tr8ggRPk6JlVgd5MQbK1wzt_lDuSe",
        ]
        data_list = [
            {
                "Nama": "Fabio Banyu Cyto",
                "Nim": "124450104",
                "Umur": "21",
                "Asal": "Balam",
                "Alamat": "-5.386541,105.262255",
                "Hobbi": "Nyapu wico lantai 2, lantai 3, lantai 4, lantai 5 gedung F",
                "Sosmed": "@biyokcb",
                "Kesan": "Abangnya Asik dan seru dan keren",
                "Pesan": "Semangat kuliahnya bang dan TA"
            },
            {
                "Nama": "Tanty widiyastuti",
                "Nim": "123450094",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Airan",
                "Hobbi": "membaca",
                "Sosmed": "IG @tvnty_",
                "Kesan": "Kakaknya Lucuu",
                "Pesan": "Semangat TA kak"
            },
            {
                "Nama": "Fadil Prasetyo",
                "Nim": "123450048",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "IG @fadilalfarizzii",
                "Kesan": "Abangnya keren dan sangat menginspirasi",
                "Pesan": "Selalu semangat ya bangg"
            },
            {
                "Nama": "Manuel Frederika",
                "Nim": "124450039",
                "Umur": "20",
                "Asal": "batam",
                "Alamat": "way kandis",
                "Hobbi": "tenis meja",
                "Sosmed": "@manuelfdk_",
                "Kesan": "Abangnya keren dan mantap",
                "Pesan": "Selalu manggat menggapai mimpi"
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "Nim": "124450005",
                "Umur": "17",
                "Asal": "Lampung Tengah",
                "Alamat": "Korpri",
                "Hobbi": "Tidur",
                "Sosmed": "@violaadrtr_",
                "Kesan": "Kakaknya asik dan baik",
                "Pesan": "Happy terus kak"
            },
            {
                "Nama": "Risa Romadona",
                "Nim": "124450127",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobbi": "Rolling skate",
                "Sosmed": "risarmdna",
                "Kesan": "Selalu bahagia kakaknya",
                "Pesan": "Selalu tersenyum kak"
            },
            {
                "Nama": "Vannisa Ramadhani",
                "Nim": "124450078",
                "Umur": "19",
                "Asal": "Kepulaun Riau",
                "Alamat": "Teluk Betung",
                "Hobbi": "Nonton film action tom cruise liam nesson jackie chan",
                "Sosmed": "@vunnycaa",
                "Kesan": "Kakaknya asik dan seru walaupun kalem",
                "Pesan": "Semngat kuliah kak"
            },
            {
                "Nama": "Yulia Kristine Malau",
                "Nim": "12440119",
                "Umur": "20",
                "Asal": "jambi",
                "Alamat": "sabah balau",
                "Hobbi": "main alat musik",
                "Sosmed": "krnylee",
                "Kesan": "Kakaknya murah senyum",
                "Pesan": "Selalu happy kak"
            },
            {
                "Nama": "Akeyla Fairuz Shafi",
                "Nim": "123450119",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Dengerin Musik",
                "Sosmed": "IG @keyashafi_",
                "Kesan": "Abangnya keren banget",
                "Pesan": "Semangat untuk gapai imoian bang"
            },
            {
                "Nama": "Elsa Sitorus",
                "Nim": "124450088",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Pemda",
                "Hobbi": "Rebahan",
                "Sosmed": "_els.a",
                "Kesan": "Kakaknya asik banget",
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Fadya Izzatul 'Aini",
                "Nim": "124450062",
                "Umur": "20",
                "Asal": "Pringsewu",
                "Alamat": "Airan",
                "Hobbi": "Main ML",
                "Sosmed": "fadyaizzatul_",
                "Kesan": "Kakaknya ramah banget",
                "Pesan": "Selalu di kelilingi orang baik kak"
            },
            {
                "Nama": "Lovianora Saragih",
                "Nim": "124450105",
                "Umur": "19",
                "Asal": "Sumut",
                "Alamat": "Way huwi",
                "Hobbi": "badminton",
                "Sosmed": "IG @from_loviaa",
                "Kesan": "Kakaknya seru bangett",
                "Pesan": "Semangat kakak MC"
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "Nim": "124450092",
                "Umur": "20",
                "Asal": "Kalianda",
                "Alamat": "Kotabaru",
                "Hobbi": "Main game, tidur, dengerin musik",
                "Sosmed": "ig: aruccy_",
                "Kesan": "Semngat terus abangnya",
                "Pesan": "NIM nya sama kaya punya ridho datavora bang"
            },
            {
                "Nama": "Sherena Florencia",
                "Nim": "124450027",
                "Umur": "19",
                "Asal": "Bengkulu Selatan",
                "Alamat": "Belwis",
                "Hobbi": "Menunda Pekerjaan",
                "Sosmed": "sher_renna",
                "Kesan": "Kakaknya Asik",
                "Pesan": "Semangat ya kak"
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "Nim": "123450096",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "belwis",
                "Hobbi": "futsal",
                "Sosmed": "IG @razyn.hfd",
                "Kesan": "Abangnya keren jago coding",
                "Pesan": "Selalu jago abangnya"
            },
            {
                "Nama": "Faiza Try Anjani",
                "Nim": "124450075",
                "Umur": "19",
                "Asal": "Padang",
                "Alamat": "Belwis",
                "Hobbi": "Belajar",
                "Sosmed": "faizaanjanii",
                "Kesan": "Kakaknya baik banget",
                "Pesan": "Semangat kakak kakak"
            },
            {
                "Nama": "Gathfan Nadhif Ali",
                "Nim": "124450001",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasah",
                "Hobbi": "Main Game",
                "Sosmed": "@gathfannad",
                "Kesan": "Abangnya kalem dan asik",
                "Pesan": "Semangat kulaihnya bang"
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "Nim": "124450064",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Metro Kibang, LamTim",
                "Hobbi": "Ngoding & Ngegame",
                "Sosmed": "@apiszzaja_",
                "Kesan": "Abangnya asik sekali inii",
                "Pesan": "Semangat mementori bang"
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "Nim": "124450053",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Campang Raya",
                "Hobbi": "nge-gym, baca novel",
                "Sosmed": "IG @kelelep_comberan",
                "Kesan": "ABangnya jago ALE",
                "Pesan": "Selalu jago bang"
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "Nim": "124450087",
                "Umur": "19",
                "Asal": "Sumsel",
                "Alamat": "Sukarame",
                "Hobbi": "Nari",
                "Sosmed": "@melva_fbrt",
                "Kesan": "Kakaknya baik dan semangat banget",
                "Pesan": "Happy terus kak"
            },
            {
                "Nama": "Muhammad Stafiqul Falakh",
                "Nim": "124450099",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Membaca",
                "Sosmed": "@syaafiqui",
                "Kesan": "Abangya seru dan keren suaranya",
                "Pesan": "semangat terus menjadi astut RA bang"
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "Nim": "124450115",
                "Umur": "2000",
                "Asal": "Kota Bumi",
                "Alamat": "Rajabasa",
                "Hobbi": "Nongkrong",
                "Sosmed": "henryferdianto",
                "Kesan": "Abangnya keren baik dan ramah",
                "Pesan": "Semangat ya bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    mikfes()


if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FqPbyKwEy1tXyP36l_momR3kkySPlUyh",
            "https://drive.google.com/uc?export=view&id=1vMErfqvCBFvZmoPC9gMf_-aXV7hjCYgC",
            "https://drive.google.com/uc?export=view&id=19SBt5UEQf0KvSH-StPBP2T9UXNoJimeq",
            "https://drive.google.com/uc?export=view&id=1BU-XEpb5PVBSb7Wwh6u-w0224N6lXs44",
            "https://drive.google.com/uc?export=view&id=1nAZxGzZ9Z8hJwMWXib41ca9GQattsvxJ",
            "https://drive.google.com/uc?export=view&id=1YOqFE9QvEmbzRUqodzSpC9Ex0B-OrHrO",
            "https://drive.google.com/uc?export=view&id=1OMFKKVwS5ySSRSjxIhvHKxyaTVU16hzg",
            "https://drive.google.com/uc?export=view&id=1ICrRAA8O3ow0Y0tZb-WsMOaMmVHZw4Hm",
            "https://drive.google.com/uc?export=view&id=1cSSS2W905gdeb820-svdHflhCSHJW0NH",
            "https://drive.google.com/uc?export=view&id=1K0Cz55unmB7tR0dDyfzbsv5-7ZVmG7jx",
            "https://drive.google.com/uc?export=view&id=1JtvK65murY_Npp3em0soCnWCEUU1DHiu",
            "https://drive.google.com/uc?export=view&id=1rgBY4n5w6y9n4IlacGeIUb3DeEuxjyPM",
            "https://drive.google.com/uc?export=view&id=1l5S_TJpvOWbI_5NgRPg2MdWYNxWZ95zf",
            "https://drive.google.com/uc?export=view&id=1yz48FidNElSVAVL-GHfCWoapspg5kwXr",
            "https://drive.google.com/uc?export=view&id=1W_4TMpjkk179_lf9eCMVuhkasjeYBWJN",
            "https://drive.google.com/uc?export=view&id=1ldgLUtywXpYKBLoTxT-YnEJtzaARcnsm",
            "https://drive.google.com/uc?export=view&id=1w-rFL2XSr4NtS5_62CsUQVMjD0MHNPY-",
        ]

        data_list = [
            {
                "Nama": "Arienta Khusnul Ananda",
                "Nim": "123450097",
                "Umur": "21",
                "Asal": "Kalianda",
                "Alamat": "Samping kos bang Haikal",
                "Hobbi": "Ngerjain TA",
                "Sosmed": "@arientakhsnl",
                "Kesan": "Kakaknya baik banget",
                "Pesan": "Selalu bahagia kak"
            },
            {
                "Nama": "Vany Salsabila Putri",
                "Nim": "123450022",
                "Umur": "21",
                "Asal": "Sibologa",
                "Alamat": "Pudan Kos",
                "Hobbi": "Berduaan sama pacar",
                "Sosmed": "vany.salsabilaa",
                "Kesan": "Kakaknya Ramah banget",
                "Pesan": "Selalu di kelilingi orang baik kak"
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "Nim": "123450117",
                "Umur": "21",
                "Asal": "Tanah Indonesia",
                "Alamat": "Samping Rumah Henry",
                "Hobbi": "Banyak",
                "Sosmed": "@nobelnizam",
                "Kesan": "Abangnya keren, apalgi pas menyampaikan materi",
                "Pesan": "Selalu semangat bang"
            },
            {
                "Nama": "Afriza Azmi",
                "Nim": "124450110",
                "Umur": "20",
                "Asal": "Malang",
                "Alamat": "Dalam pasar",
                "Hobbi": "Teriak",
                "Sosmed": "Tanya Reno",
                "Kesan": "Abangnya Keren dan tegas",
                "Pesan": "Selalu semangat untuk kuliah bang"
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "Nim": "124450108",
                "Umur": "21",
                "Asal": "Paninjauan Solok, Sepuluh Kota di Atas, Sumatera Barat, Indonesia",
                "Alamat": "Blok D 77, Jalan Manggis Delapan, Pemda, Jatiagung, Lampung Selatan, Lampung, Indonesia",
                "Hobbi": "Mancing",
                "Sosmed": "@ykeall",
                "Kesan": "Abangnya Keren dan seru",
                "Pesan": "Selalu Semangat untuk meraaih mimpi bang"
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "Nim": "124450017",
                "Umur": "21",
                "Asal": "Tanya Biwa",
                "Alamat": "Kontrakan Hijau",
                "Hobbi": "Mandiin anak ayam",
                "Sosmed": "@caesarozora",
                "Kesan": "Abangnya seru banget",
                "Pesan": "Selalu menjadi panutan bang"
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "Nim": "124450029",
                "Umur": "18",
                "Asal": "Kampung lama",
                "Alamat": "Dibawah turunan",
                "Hobbi": "Makan gorengan",
                "Sosmed": "yudiameilianaa_",
                "Kesan": "Kakaknya asik dan seru",
                "Pesan": "Selalu semangat menggapai apa yang diinginkan"
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "Nim": "124450016",
                "Umur": "21",
                "Asal": "Palembang",
                "Alamat": "Sebelah kanan rumah Henry",
                "Hobbi": "Ngecek makan ayam",
                "Sosmed": "_haikaaall",
                "Kesan": "Abangnya keren sekaali",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "Nim": "125450056",
                "Umur": "18",
                "Asal": "Kos Owen",
                "Alamat": "Kost Owen",
                "Hobbi": "Belajar naik motor ke Bandung 94",
                "Sosmed": "putrimannaa",
                "Kesan": "Kakaknya asik dan ramah",
                "Pesan": "Selalu semangat ya kak"
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "Nim": "124450059",
                "Umur": "21",
                "Asal": "Johor Baru",
                "Alamat": "Depan Mie Gacoan",
                "Hobbi": "Main gitar",
                "Sosmed": "queentanaabila",
                "Kesan": "Selalu ramah kakaknya",
                "Pesan": "Semangat terus untuk apa yang di kejar kak"
            },
            {
                "Nama": "Desman Velius Halawa",
                "Nim": "123450114",
                "Umur": "19",
                "Asal": "Nias",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Ngejek orang",
                "Sosmed": "desmanhall_",
                "Kesan": "Abangnya seru dan asik",
                "Pesan": "Semangat TA nya bang"
            },
            {
                "Nama": "Azzelya Thianandry",
                "Nim": "123450041",
                "Umur": "19",
                "Asal": "Sukarame",
                "Alamat": "Lampung",
                "Hobbi": "Makan Ice",
                "Sosmed": "azzelytn",
                "Kesan": "Semangat terus kakakknya",
                "Pesan": "Selalu tersenyum terus kak"
            },
            {
                "Nama": "Charrlindah",
                "Nim": "37",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cenderawasih 1",
                "Hobbi": "Ngurus Peternakan",
                "Sosmed": "charrlnn",
                "Kesan": "kakaknya ramah banget",
                "Pesan": "Selalu di beri kemudahan kak"
            },
            {
                "Nama": "Jeremi Marolop P. Situmorang",
                "Nim": "124450111",
                "Umur": "17",
                "Asal": "Sidingkalang",
                "Alamat": "Di sebelah kost Haikal",
                "Hobbi": "Jadi nelayan",
                "Sosmed": "jemarrro",
                "Kesan": "Abangnya seru apalagi pas DAMASKUS",
                "Pesan": "Selalu semangat bernyanyi bang"
            },
            {
                "Nama": "Nabila Nur Azizah",
                "Nim": "48",
                "Umur": "18",
                "Asal": "Lampung",
                "Alamat": "Barokah",
                "Hobbi": "Main Roblox",
                "Sosmed": "n.bila_a",
                "Kesan": "Kakaknya baik banget",
                "Pesan": "Selalu semngat kak"
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "Nim": "124450007",
                "Umur": "20",
                "Asal": "Kota Ikan",
                "Alamat": "Di samping Kost Afdal",
                "Hobbi": "Memancing",
                "Sosmed": "dearfkvmfl",
                "Kesan": "Abangnya keren",
                "Pesan": "Semngat kuliahnya bang"
            },
            {
                "Nama": "Salavi Naharani",
                "Nim": "124450090",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobbi": "Minum air putih",
                "Sosmed": "avi.nhr",
                "Kesan": "kakaknya selalu happy",
                "Pesan": "selalu happy terus kak "
            }
        ]

        display_images_with_data(gambar_urls, data_list)

    psda()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wjjFy5eBaLVtFox7cLu0mqNOSPiEW-_t",
            "https://drive.google.com/uc?export=view&id=1u_soqD_eS458WSe0fw_oeDCgLbeD9A-K",
            "https://drive.google.com/uc?export=view&id=17_wk9kmEupbInZ26B0jlNeNjwNIGnqbf",
            "https://drive.google.com/uc?export=view&id=11f2cv2mOVkB9Xe-LedCfXUwEfNg7f2-l",
            "https://drive.google.com/uc?export=view&id=1uiM4nUXHaCDI-BjWabRcWm6DxQ7XDe2l",
            "https://drive.google.com/uc?export=view&id=1aFwGOXN2v4bRuJ2YNVkll1-mc_jlqR2b",
            "https://drive.google.com/uc?export=view&id=1O9YVLzJtXt4J20fqFUTUkb4KVJ32l8Gb",
            "https://drive.google.com/uc?export=view&id=1Iprl-VwsiwApumUnwiyZ9kSn6w7JLAPX",
            "https://drive.google.com/uc?export=view&id=14uHDuyUcuwNtlLXHcXMC2ndUvwUBufMA",
            "https://drive.google.com/uc?export=view&id=1kd0OdfJfT8vWr08KkOgXdSAMPwAZhOqZ",
            "https://drive.google.com/uc?export=view&id=1p7hRgFe1tHukbsOjFNDbzvh91fDCP-sh",
            "https://drive.google.com/uc?export=view&id=15mgKzfSRFNsD9mzQBPdA23BW60IJuozX",
            "https://drive.google.com/uc?export=view&id=1jzorN9OviJXsxR3IsxP_U9GK3qNVGrVU",
            "https://drive.google.com/uc?export=view&id=1xnRd7JwZo-Px95Dw2WlefBozpldJJFuh",
            "https://drive.google.com/uc?export=view&id=1Zff-cXU7KNo_oGeRHpuTAolD2_QYQ9Wv",
            "https://drive.google.com/uc?export=view&id=1zMHz55WFiGIpNnrVjyTpQZ2goYt45QDA",
            "https://drive.google.com/uc?export=view&id=1VcGyz7-qqweNt7u-Q8SzxqnHGcHFSUjl",
            "https://drive.google.com/uc?export=view&id=1iwHQ0fGAFmTEkswsjCP3d4SfS8UOBQCZ",
            "https://drive.google.com/uc?export=view&id=1GQ26D2Lwf5xm4c-iOvoL_cuk8zzjGerd",
            "https://drive.google.com/uc?export=view&id=1t46UPutTeKl3tpFfI2K94SZyIRyPPhfP",
            "https://drive.google.com/uc?export=view&id=1bs5yhdXn4I4Y0lRRayXjPjmzF7_Oo9k5",
            "https://drive.google.com/uc?export=view&id=1popS-_qru4CItyMi2IdbzYf7Pw2mHZAz"
        ]

        data_list = [
            {
                "Nama": "Arini Puteri Elandra",
                "Nim": "123450069",
                "Umur": "21",
                "Asal": "LAMPUNG!!!",
                "Alamat": "Teluk Betung Selatan",
                "Hobbi": "Nonton Kartun",
                "Sosmed": "@elandraa_",
                "Kesan": "Kakaknya asik dan seru banget",
                "Pesan": "Semangat menjalankan kuliah"
            },
            {
                "Nama": "Nabyla Sharfina",
                "Nim": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobbi": "Jalan - Jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Kakaknya ramah dan kerenn",
                "Pesan": "Semangat mengejar mimpi"
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "Nim": "123450032",
                "Umur": "22",
                "Asal": "tetangga kadep",
                "Alamat": "belwis",
                "Hobbi": "memancing keributan",
                "Sosmed": "@adityatfq",
                "Kesan": "Abangnya keren dan jago",
                "Pesan": "Selalu semangat  bang"
            },
            {
                "Nama": "Khoirul Muttoharoh",
                "Nim": "1234500",
                "Umur": "21",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobbi": "main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "kakaknya ramah dan rame",
                "Pesan": "Selalu bersama orang-orang baik kak"
            },
            {
                "Nama": "Selma Siti Aisyah",
                "Nim": "123450044",
                "Umur": "20",
                "Asal": "lampung",
                "Alamat": "balam",
                "Hobbi": "jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Kalem dan seru",
                "Pesan": "Selalu di beri kesehatan kak"
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "Nim": "124450028",
                "Umur": "20",
                "Asal": "sini",
                "Alamat": "jauh pokoknya",
                "Hobbi": "tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Seru banget kakaknya",
                "Pesan": "Sehat selalu kak"
            },
            {
                "Nama": "Indah Khairunnisa",
                "Nim": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Kakaknya jago mancing",
                "Pesan": "Semangat mancingnya kak"
            },
            {
                "Nama": "Bima Ekayasa",
                "Nim": "124450106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobbi": "berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "Abangnya keren",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "Nim": "124450113",
                "Umur": "20",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobbi": "lihat lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "Abangnya seru dan kalem",
                "Pesan": "Selalu di beri kesahatan bang"
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "Nim": "124450083",
                "Umur": "20",
                "Asal": "ikut kadep",
                "Alamat": "love earth",
                "Hobbi": "hobi jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Semangat banget kakaknya",
                "Pesan": "Selalu semangat dan tersenyum kak"
            },
            {
                "Nama": "Yollanda Agustina",
                "Nim": "124450024",
                "Umur": "",
                "Asal": "Sebelah Barat",
                "Alamat": "Kayu Mulya Kerangka Bawang",
                "Hobbi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Kakaknya asik dan  rame",
                "Pesan": "Tetap semnagat kuliah kak"
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "Nim": "124450022",
                "Umur": "20",
                "Asal": "palembang",
                "Alamat": "bebas",
                "Hobbi": "ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Kakaknya ramah dan baik",
                "Pesan": "Selalu semangat kak"
            },
            {
                "Nama": "Fathya Intami Gusda",
                "Nim": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobbi": "baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Semangat banget kakaknya dan seru",
                "Pesan": "Selalu semangat dimanapun kak"
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "Nim": "123450052",
                "Umur": "",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobbi": "Jadi orang baik",
                "Sosmed": "-",
                "Kesan": "Kkakaknya baik seperti hobinya",
                "Pesan": "Selalu baik ya kak"
            },
            {
                "Nama": "Danil N Fadillah",
                "Nim": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobbi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Asik abangnya",
                "Pesan": "Selalu semangat memeberi asupan makanan ke cupang bang"
            },
            {
                "Nama": "Favian Arkaanda",
                "Nim": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobbi": "ngesen kanan",
                "Sosmed": "@fvnnn05",
                "Kesan": "Selalu semangat  bang",
                "Pesan": "nim 21 datavora sepupu saya bang"
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "Nim": "124450081",
                "Umur": "20",
                "Asal": "situlah",
                "Alamat": "pohon mulia",
                "Hobbi": "nyari hobi",
                "Sosmed": "@zydddddd__",
                "Kesan": "Abangnya seru dan keren",
                "Pesan": "Keren hobi abangnya nyari hobi"
            },
            {
                "Nama": "Alfaya Abiyyi",
                "Nim": "124450006",
                "Umur": "20",
                "Asal": "balam",
                "Alamat": "balam",
                "Hobbi": "makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "Abangnya kalem dan ramah",
                "Pesan": "selalu bahagia dan terseyum bang"
            },
            {
                "Nama": "Muhammad Rizaldi",
                "Nim": "124450093",
                "Umur": "Masih muda lah",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobbi": "Tanyain sama yuder (beneran ditanya ya)",
                "Sosmed": "@jaldii._",
                "Kesan": "Abangya asik seru dan keren",
                "Pesan": "Selalu semngat untuk menggapai mimpi bang"
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "Nim": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobbi": "nonton thinkerbell",
                "Sosmed": "@snova.19",
                "Kesan": "Kakaknya kalem dan selalu semangat",
                "Pesan": "Jaga semangat terus kak"
            },
            {
                "Nama": "Asri Meilani",
                "Nim": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobbi": "menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "kakaknya asik dan seru dan kalem",
                "Pesan": "Tetap semangat kak"
            },
            {
                "Nama": "Ahmad Rizky",
                "Nim": "123450050",
                "Umur": "21",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobbi": "ga ngapa ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Selalu semangat dan selalu menginspirasi",
                "Pesan": "Semangat terus banggg"
            }
        ]

        display_images_with_data(gambar_urls, data_list)

    eksternal()
