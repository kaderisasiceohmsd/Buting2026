import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
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
            "Departemen Minbak"
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
            "nav-link-selected": {"background-color": "#606060"},
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
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hSXYw6ZGNp_7Y-A15BS7eR5YwP2HJ5qA",
            "https://drive.google.com/uc?export=view&id=1fP95YaSjhAvkBQ3ELbbE48ybTAiMSkiI",
            "https://drive.google.com/uc?export=view&id=1KVpeBiIKfCVyftM5FEK8V9WRVYR0WOc_",
            "https://drive.google.com/uc?export=view&id=1sMP2My5JlKwoVNTEAnCUQYk37MCfwohm",
            "https://drive.google.com/uc?export=view&id=109zbLVgztc65bJ7WHYyy7ln8Kv1gIILJ",
            "https://drive.google.com/uc?export=view&id=1DOqOekXeeT2pZ80fv3vhDccnQuzwLOuf",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Tinggal Sekretariat HMSD",
                "hobbi": "Push Rank Sampai imo",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Fajar baik, ramah, aura kepemimpinannya tinggi jadi agak segan sama bang fajar",  
                "pesan":"Semangat jadi kahimnya bang semoga lancar perkuliahannya"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "21",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Tahajud",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Baik dan pintar, keliatannya taat agama gitu",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak baik, ramah, dan cantik",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang Qois kelihatan pinter dan baik ",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Basket",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakak ini asik baik dan cantik",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Lutfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nemuin Pak Tirta",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kak Lutfia baik ramah dan cantik",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1obfVrNnPv9PJVA8nzqaRLkhBf2JNAyNs",
            "https://drive.google.com/uc?export=view&id=1fSLfPZGsC7jhHCCQjta6hdsY6YORIR_Y",
            "https://drive.google.com/uc?export=view&id=1UQbYlSOIfej2lLM2TJYkTB0BNUU74ePq",
            "https://drive.google.com/uc?export=view&id=1K8sKAvn-SynJv3wG1efFD-yC1qLogldr",
            "https://drive.google.com/uc?export=view&id=1KJt4KRZn4OdK7SC5HEChjEfvf3kQSe60",
            "https://drive.google.com/uc?export=view&id=1ECpiwzZ2VQTzQfmKetSFF7wVExHVqj6x",
            "https://drive.google.com/uc?export=view&id=1Mgn6nEhBTwecVpviV_6vipM7j9zxVEtX",
            "https://drive.google.com/uc?export=view&id=1ZXvOuTrW0Y8VTItDmYdl2RVKDyn6ZmJR",
            "https://drive.google.com/uc?export=view&id=1lxJ5BK_uzPSQG5nkKwi9q19rrFEU7lCf",
            "https://drive.google.com/uc?export=view&id=14AuQmBliZWxOR3ijzl6M1rWjBi2NHhwJ",
            "https://drive.google.com/uc?export=view&id=1rX9lUpaBnBPn5PKTdAflWRksc1anoCFe",
            "https://drive.google.com/uc?export=view&id=1tA0i3Q2e2s8R0wiS-Tk3gpUe7Mfpdc-B",          
            "https://drive.google.com/uc?export=view&id=13sj5P7Vf9TdAb8zviumy6pfg8n7UbzRb"
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Bali",
                "alamat": "GH",
                "hobbi": "Menonton Seminar",
                "sosmed": "@iamridhomanik",
                "kesan": "Abang ini asik parah dan yapping ",  
                "pesan":"Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Repeat lagu if only by skyline setiap hari di jam 8",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya gemas dan cantik bangett",  
                "pesan":"Semangat terus kuliahnya kak.Jangan lupa istirahat"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "124450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya aktif dan keren banget,",  
                "pesan":"semangat terus dan aktif terus bang kuliahnya.Jangan lupa istirahat"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Abangnya asik dan baik",
                "pesan":"Semangat terus belajar dan kuliahnya bang.Sukses selalu!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "124",
                "umur": "20",
                "asal":"Kupang",
                "alamat": "Jatiagung",
                "hobbi": "Main PS",
                "sosmed": "@me._kael",
                "kesan": "kak Monica baik banget, cantik dan ramah",  
                "pesan":"Semangat selalu kakk,dilancarkan semua urusannya"# 1
            },
            {
                "nama": "Gh Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal":"Kupang",
                "alamat": "Jatiagung",
                "hobbi": "Main PS",
                "sosmed": "@me._kael",
                "kesan": "Abangnya asik dan baik banget",  
                "pesan":"Semoga sukses selalu, dilancarkan semua urusannya"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal":"Jatiasih",
                "alamat": "Kedaton",
                "hobbi": "Nonton Boboiboy",
                "sosmed": "@syt.rifa",
                "kesan": "Kakaknya cantik, lucu, dan baik banget",  
                "pesan":"Semangat terus kuliahnya kak, jangan lupa istirahat"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Indarum",
                "alamat": "Awen kost",
                "hobbi": "Photobooth",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semoga semua yang kk usahankan tercapai, semangat selalu"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal":"Kotabumi",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",                
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Sidoarjo",
                "alamat": "Teluk",
                "hobbi": "Konten Mainfullness",                
                "sosmed": "@jeremia_hm",
                "kesan": "Abangnya aktif dan sibuk banget ternyata, tapi baik dan humble  banget",  
                "pesan":"Semangat terus belajar dan kuliahnya bang, semoga langkah kedepannya dipermudah."# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan koleksi figure",                
                "sosmed": "@nagatseee",
                "kesan": "Abangnya asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya bang,semoga selalu bertemu dengan hal baikk"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Membaca buku",                
                "sosmed": "@sekardnwp",
                "kesan": "Kakaknya mukanya kaya galak gitu, tapi waktu wawancara baik banget dan ramah",  
                "pesan":"Semangat terus belajar dan kuliahnya kak, sukses selalu!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "124450077",
                "umur": "20",
                "asal":"Pasoy",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",                
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya lucu, cantik, dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak, jangan lupa istirahat!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cP3GVgpQWxzCGGdUlFjAuVvKTCrAdDrM",
            "https://drive.google.com/uc?export=view&id=1gBldU2bKLPf51bECau0kuHABzGCkUIMj",
            "https://drive.google.com/uc?export=view&id=1-9szMhCsvwWdPvceyz4_H3UbPY7r30hO",
            "https://drive.google.com/uc?export=view&id=1ErQZRRAVrQVBBpvumJ2Td8lnAd9AvpRp",
            "https://drive.google.com/uc?export=view&id=1f8bCo1WUIpan0P00sdE2SdJV1CAxe0Tb",
            "https://drive.google.com/uc?export=view&id=1LBYtVZzOvBHvbyyu7m201CwSI9CVF0JM",
            "https://drive.google.com/uc?export=view&id=1dwKnyU28WapJcfic-_ftIjxJgFdexQpX",
            "https://drive.google.com/uc?export=view&id=1943JkGYsNq5yGp8k-ZpiIrFotTDN4wuH",
            "https://drive.google.com/uc?export=view&id=1bTkv-DXn07OWxDnWbvcJ_4-_32EIudbi",
            "https://drive.google.com/uc?export=view&id=1_w6gQgKdJDKFvif2X43atRCP_uYfD5tH",
            "https://drive.google.com/uc?export=view&id=14aDXfdNyfbe7Wf9qvSZBzdE035hxRjaA",
            "https://drive.google.com/uc?export=view&id=1S4uK11ACm1-PInaxyaoUd_j-GbqwHX5u",
            "https://drive.google.com/uc?export=view&id=1fG07CGt4z5xhrOqePGq22LLO-fvVbz1g",
            "https://drive.google.com/uc?export=view&id=1OA4y9nhtnZ-tUrTT0g3iFibMESiX3EjH",
            "https://drive.google.com/uc?export=view&id=164qrgywUhZygWTw8wj3mErnBGsOY44PR",
            "https://drive.google.com/uc?export=view&id=1CVNP4I6STzqV-DPDXjrVLeJM0w38ZEAw",
            "https://drive.google.com/uc?export=view&id=11htXNOyJO_diRlpJpumopdYwp3qWcJ50",
            "https://drive.google.com/uc?export=view&id=1NfnZSeV9IAXqgC5gUiLVLxOOGRM58R4Q",
            "https://drive.google.com/uc?export=view&id=1C4vEoFFTBKDY5kmcDrVH97AyBJz0Yh2-",
            "https://drive.google.com/uc?export=view&id=14ag_CDYFnPxJGjKAqKOuxzmQRTbk1ucd",
            "https://drive.google.com/uc?export=view&id=1u-5vjvQ6NpYhecNKxdYBhtzrHAJHFmdF",
            "https://drive.google.com/uc?export=view&id=1YsSwgcR14kUvbjYIMmtFiVtrBkqZ5caG"
        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "21",
                "asal": "LAMPUNG!!!",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ini pembawaannya positif vibes bgt dan baik",  
                "pesan": "semangat terus kuliahnya kakak,sukses selalu"  # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak ini baik dan ramah,",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing Keributan",
                "sosmed": "@adityatfq",
                "kesan": "Bang aditya ini orangnya kelihatan asik dan menyenangkan",  
                "pesan":"semangat terus kuliahnya, semoga semua urisannya dipermudah"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak ini baik dan menyenangkan",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupa istirahat!"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kakak ini baik dan menyenangkan",  
                "pesan":"semangat terus kuliahnya kak, tetap jaga kesehatan!"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh Pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakak ini terlihat baik dan positif vibes",  
                "pesan":"semangat terus kuliahnya kakak, sukses selalu"# 1
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakak ini keliatan asik dan mudah bergaul",  
                "pesan":"semangat terus kuliahnya kakak, jaga kesehatan selalu"# 1
            }, 
            { 
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Abangnya baik dan ramah banget",  
                "pesan":"semangat terus kuliahnya bg, semoga tercapai yang diharapkan"# 1
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat-lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Abangnya baik dan ramah banget",  
                "pesan":"semangat terus kuliahnya bg"# 1
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Love Earth",
                "hobbi": "Jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakak ini asik, baik, dan cantik",  
                "pesan":"semangat terus kuliahnya kakak, sukses selalu"# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakak ini asik, pintar, dan aktif banget",  
                "pesan":"semangat terus kuliahnya kakak, sukses selalu"# 1
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kakak ini cantik dan imut",  
                "pesan":"semangat terus kuliahnya kak, jangan lupa makan"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak ini baik dan ramah banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },             
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakak ini baik dan menyenangkan walau belum terlalu sering interaksi",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Abangnya asik, ramah, dan supel bgtt",  
                "pesan":"semangat terus kuliahnya bg, tetap jadi orang yang ceria"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Abangnya ini asik, menyenangkan, dan ramah ",  
                "pesan":"semangat selalu, sukses akademiknya"# 1
            }, 
            { 
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "Pohon mulia",
                "hobbi": "Nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Abangnya terlihat menyenangkan dan baik",  
                "pesan":"Semoga perkuliahannya lancar selalu dan sukses yang sedang dikerjakan"# 1
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Abangnya asik, ramah, dan aktif bgtt",  
                "pesan":"semangat terus kuliahnya bg, sukses selalu"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "-",
                "sosmed": "@jaldii._",
                "kesan": "Abangnya asik, ramah, dan aktif bgtt",  
                "pesan":"semangat terus kuliahnya bg, semoga tercapai semua impian"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakaknya baik, menyenangkan, dan positif aura ",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupa istirahat "# 1
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakak ini asik, baik, dan ramah.",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupa istirahat "# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "124450050",
                "umur": "21 Tahun ini alhamdulillah",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Abangnya aktif banget, keren, dan sangat berpikir kritis",  
                "pesan":"semangat terus bang, lancar semua yang sedang dikerjakan dan jangan lupa jaga kesehatan"# 1
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mrID04Jxww7Y55VuEAzSf4jIzlPrZsdB",
            "https://drive.google.com/uc?export=view&id=1iNZtuohSvo0VONuK0WQ0Gp0DUDp0HJ9i",
            "https://drive.google.com/uc?export=view&id=1rgq_y0a6cyPOZJNcoxmZjg5WM5ZOYDNp",
            "https://drive.google.com/uc?export=view&id=12ugC55IwShpQjQRgzPBxtHjw2xFKj9sU",
            "https://drive.google.com/uc?export=view&id=1N-cE6lJfgju3QsoRi5FcijqQ_XZlaqy2",
            "https://drive.google.com/uc?export=view&id=1mESp4BH7loxrAi01yn5qyYAP8gYxwLYZ",
            "https://drive.google.com/uc?export=view&id=1fbSYnpkQnOKXVKIo-v76sbj_mv56EQtd",
            "https://drive.google.com/uc?export=view&id=1wWjlyTx6MvrkSLDE-XKhy5z5v_A3ZV0i",
            "https://drive.google.com/uc?export=view&id=1WeokYvlSKxKHwl7dyld1KAMiKEI4c8gC",
            "https://drive.google.com/uc?export=view&id=1dvD6XvrblMMLwCOYadX8Od7c7QsGyU0W",
            "https://drive.google.com/uc?export=view&id=1QaQgkoyJvi1ZwlNpPX612QrlwUlpN0uJ",
            "https://drive.google.com/uc?export=view&id=1FxYIqGA2VzxDrGvMRcHovNpzr-yj6mqj"
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21 Tahun",
                "asal":"Sumbar",
                "alamat": "Belwis",
                "hobbi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abangnya asik, ramah,dan baik",  
                "pesan":"semangat terus kuliahnya bang, semoga lancar semua urusannya"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini baik, ramah, dan cantik",  
                "pesan":"Semoga semua impian kakak tercapai, jaga kesehatan selalu"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik, baik, dan menyenangkan",  
                "pesan":"semangat selalu kakak, jangan lupa makan"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya baik, ramah, dan cantik",  
                "pesan":"semangat terus kuliahnya, semoga lancar semua urusannya"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "Abangnya asik, ramah, humble, dan baik",  
                "pesan":"semangat terus kuliahnya bang, sukses selalu"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "Muka abangnya kaya galak gitu, tapi ternyata baik",  
                "pesan":"semangat terus kuliahnya, semoga sukses selalu"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Abangnya baik, ramah, dan asik",  
                "pesan":"semangat kuliahnya bang, jangan lupa istirahat"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "Kakaknya baik, ramah, dan cantik",  
                "pesan":"semangat selalu kakak, semoga lancar semua urusannya"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakak ini asik, baik, ramah, dan cantik",  
                "pesan":"Semoga lancar semua urusannya, sukses selalu"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakak ini asik, baik, ramah, dan cantik",  
                "pesan":"semangat terus kuliahnya kak, jangan lupa istirahat"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "Abangnya baik, dan menyenangkan",  
                "pesan":"Semoga semakin sukses dan tercapai semua yang diimpikan"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupa istirahat"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()


if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15LR_pw_sZqkEs3Nl3NMlEB0Sd_6SxkxX",
            "https://drive.google.com/uc?export=view&id=1dcR8YX5ox_cYpPSX5dtRKCPC2pQ2OACI",
            "https://drive.google.com/uc?export=view&id=1eYqUz-wC-1BE5f9BvpSW9pQ4-So0Uf4Z",
            "https://drive.google.com/uc?export=view&id=1G6UWF9SrX5h2tGR6pCgh3BrQgsIZKIkD",
            "https://drive.google.com/uc?export=view&id=1Po184T9YdLag-fs14HXblZZk8FUXLqkR",
            "https://drive.google.com/uc?export=view&id=1LHstWQPQegIo6o3PtUFDORads6eWQdcK",
            "https://drive.google.com/uc?export=view&id=1LUDgNE3ae1FbTc9bhg3XyoWl5rkWgu2N",
            "https://drive.google.com/uc?export=view&id=1kV_ovwUnbw8bYQwIsjQTCKqxxzOQnfSa",
            "https://drive.google.com/uc?export=view&id=1epTOihUOesb_FaQ74FvB3kMQ8RLAxdJ_",
            "https://drive.google.com/uc?export=view&id=1quQu80_e9tZ3qBZsZmEC9vmeDrvCFOv5",
            "https://drive.google.com/uc?export=view&id=1zGwqK1ir0tftQrGKu6apNeiVBeolCzXC",
            "https://drive.google.com/uc?export=view&id=1W5bgkGCWDm3Irc-TLpAdxsQJEz6Ma2If",
            "https://drive.google.com/uc?export=view&id=1FulFDR7f-sTyDA7Ngd2i9xtg_Wg_QFwW",
            "https://drive.google.com/uc?export=view&id=13wnd652IczxBmy_YZ7jWHEY1BrtOS4kE",
            "https://drive.google.com/uc?export=view&id=1rekkK-OAp29D0eY1qxiY2gqWh06IFZhI",
            "https://drive.google.com/uc?export=view&id=1n-OeTvt-s6jAgYbEQccmuiUxvLuMVRRx",
            "https://drive.google.com/uc?export=view&id=1v-hXMJAfM8PajpVpWhzAJOFHaEA-13ui",
            "https://drive.google.com/uc?export=view&id=1FSm38QPZRh1Z81TxbqvJaHF9UnoFOobo"
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kakak baik, asik, dan cantik",  
                "pesan": "semangat terus kuliahnya kakak, tetap jaga kesehatan"# 1
            },
            {
                "nama": " Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": " Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini pintar dan aktif",  
                "pesan": "semangat terus kuliahnya kakak,semoga selalu lancar perkuliahannya"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": " Way Huwi",
                "hobbi": " Tong setan",
                "sosmed": "@noerruuu",
                "kesan": "Abangnya baik, pinter dan aktif banget",  
                "pesan": "semangat terus kuliahnya, lancar terus kuliahnya"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"karawang",
                "alamat": "Airan",
                "hobbi": "nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak cantik, baik, dan asik",  
                "pesan": "semangat terus kuliahnya kakak, jangan lupa istirahat"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kakak ini asik dan baik",  
                "pesan": "semangat terus kuliahnya kk"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakak ini asik dan baik",  
                "pesan": "semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": " 124450043",
                "umur": "Gada yang tau",
                "asal": "Rumah bapak ",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakak baik dan humble",  
                "pesan": "semangat terus kuliahnya kak lancar selalu yg sedang dikerjakan"# 1
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": " 124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@ felisyanbl__",
                "kesan": "Kakak ini baik, ramah, dan aktif",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": " Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "Abangnya baik, ramah dan aktif tiap kegiatan",  
                "pesan":"semangat terus kuliahnya bg, tetap ingat istirahat"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "bobo",
                "sosmed": "@Xifasky",
                "kesan": "Kakaknya baik",  
                "pesan":"semangat terus kuliahnya kk"# 1
            },
            {
                "nama": " Lucia Advencia Rachel Nainggolan",
                "nim": " 124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": " Mencintai Andrew Garfield",
                "sosmed": "@ luciarachel_",
                "kesan": "Kakak ini cantik dan baik",  
                "pesan": "semangat terus kuliahnya kakak, jangan lupa istirahat"# 1
            },
            {
                "nama": " Edsel Adya Pradipta",
                "nim": " 124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll fesnuk",
                "sosmed": "@edsel_0712",
                "kesan": "Abgnya baik tapi masih jarang interaksi",  
                "pesan": "semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "nyuluh manuk",
                "sosmed": "@daffascript_",
                "kesan": "Abngnya baik dan menyenangkan",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@ alya.rmdhnti",
                "kesan": "Kakak baik dan menyenangkan",  
                "pesan": "semangat terus kuliahnya kak, jangan lupa makan"# 1
            },
            {
                "nama": "Bunga Clarissa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya semoga sehat selallu"# 1
            },
            {
                "nama": "Nazlah Aulia",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memanah",
                "sosmed": "@nzlhauly",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "shafa delaila azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Pemda",
                "hobbi": "Ngoding",
                "sosmed": "@_shaazzh",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan": "semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukabumi",
                "hobbi": "Gebuk Snare",
                "sosmed": "@aallishaa.a",
                "kesan": "Kakak ini cantik dan keren",  
                "pesan":"semangat terus kuliahnya kak, kk keren bgt ngegebuk snare"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cgZ7IU224hTH9VxheYXWrq4TpCHJV2NJ",
            "https://drive.google.com/uc?export=view&id=1UHQ1Nf2EGbtQ1IQnhHIDxxSCZleUQgnI",
            "https://drive.google.com/uc?export=view&id=1rX3XfPt74SduEWnjoup9uUC5fn0FI74J",
            "https://drive.google.com/uc?export=view&id=1ka2bnDl6MdhUdLt4l-Tf9Ggx4figzgrD",
            "https://drive.google.com/uc?export=view&id=1ho2KmfhD8wN7KPeG6Sb_E9F3PThEGp2Z",
            "https://drive.google.com/uc?export=view&id=1lQAllB3eds-iFg20HYwygQClND1kPx0I",
            "https://drive.google.com/uc?export=view&id=17DF5SkKNlCbtYnesTN4vlRqnZEbydrFw",
            "https://drive.google.com/uc?export=view&id=17fvVZnwNZz9ADQ7sNbKlPw8uUkrsBQa0",
            "https://drive.google.com/uc?export=view&id=1etlPh0dMEDXQME52sPIk-esRZ1ZR5aG6",
            "https://drive.google.com/uc?export=view&id=1GBSMrnM1Y4owA-1Z0sLQxOHdZfqfPUGI"
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21 Tahun",
                "asal":"Jakarta",
                "alamat": "Airan",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini baik, pintar tapi tidak sombong, dan asikS",  
                "pesan":"semangat terus kuliahnya kakak dan semoga sukses selalu!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21 tahun",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengar lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini baik dan cantik, dan asik",  
                "pesan":"Jangan lupa istirahat ya kk"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21 tahun",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "beres beres",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik, mudah senyum dn baik",  
                "pesan":"semangat terus kuliahnya, sukses selalu"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20 Tahun",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "ngesen kiri",
                "sosmed": "@helmy.inst",
                "kesan": "Baik, kocak dan hoby melet",  
                "pesan":"semangat terus bg, mau foto kami yg bertiga itu siih"# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21 Tahun",
                "asal":"Tangerang kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Main Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Baik dan kayanya receh bgt hoby ngelawak",  
                "pesan":"Jangan lupa makan bg"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19 Tahun",
                "asal":"Pesisir Barat",
                "alamat": "Kobar",
                "hobbi": "Dokum hal tidak penting",
                "sosmed": "@sciia__",
                "kesan": "Kakak ini baik, pintar tapi tidak sombong, dan asik",  
                "pesan":"semangat terus kuliahnya kakak dan semoga sukses selalu!"# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Abg ini pinter dan aktif bgt kayanya",  
                "pesan":"semangat selalu sempga lancar semuanyaa"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19 tahun",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasi Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakak ini cantik, dan aktif",  
                "pesan":"semangat terus kuliahnya kakak dan semoga sukses selalu!"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "19 Tahun",
                "asal":"Lamtim timur",
                "alamat": "Gunter terang",
                "hobbi": "Cinematic Datavora",
                "sosmed": "@hazelhandhaka",
                "kesan": "Bg Hazel baik tapi kaya susah senyum gitu ",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupa makan ya!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1n1qjNkBQipukGrqBNlzdwW_R8CP22O-i",
            "https://drive.google.com/uc?export=view&id=1k5FMeNVWYT0obhm5PlAZY2JIs_LHAhyx",
            "https://drive.google.com/uc?export=view&id=1lQ0AmT8SuLDHejsdN8pwqBVeORom_SBx",
            "https://drive.google.com/uc?export=view&id=1y29gN3iyEw1zdZsVF58SOTP_9kFDXqmN",
            "https://drive.google.com/uc?export=view&id=1x_M94BTQ1uiCyASVUOm0hotYh3W55Gtp",
            "https://drive.google.com/uc?export=view&id=1YRonuwGjSF4Yj3xSFJRpJcw0U-SnnZHB",
            "https://drive.google.com/uc?export=view&id=101LuVzhMhs1U4pAcjPIKD8X_vJN71yZq",
            "https://drive.google.com/uc?export=view&id=1MfEUr-CgbQCbEGMc6WVZabKtFOpZjXzV",
            "https://drive.google.com/uc?export=view&id=1x9TTc0QVOFNbGrKdi__zM0h_ARI_dy1U",
            "https://drive.google.com/uc?export=view&id=1PF10nsTpVxqR7up_a_6SXflEMxS91bRl",
            "https://drive.google.com/uc?export=view&id=1mfuh9haZyXpSdEvqS1K9n1xcgRip1crb",
            "https://drive.google.com/uc?export=view&id=1j4DEIxzyn1syfPsFxHRiymhJCeminWRz",
            "https://drive.google.com/uc?export=view&id=1ao6VEqprf3vnTp3jGHys90YJZ95SPSiy",
            "https://drive.google.com/uc?export=view&id=1-hQCyuSa5OYUqWDuD0wdEG5OzYloyHaY",
            "https://drive.google.com/uc?export=view&id=1qw4UCUU4ox99ILj0T50gFXOV_QannG04"
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Sulawesi Tengah",
                "alamat": "Panjang, Bandar Lampung",
                "hobbi": "Masak",
                "sosmed": "@kevinaj__",
                "kesan": "namanya keren, abgnya baik dan humble",  
                "pesan": "semangat terus kuliahnya, semoga cepat selesai"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": " Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya cantik dan imut bgtt",  
                "pesan": "semangat terus menjalani semuanya, semoga sukses selalu"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Main badminton sama Yosep",
                "sosmed": "@mridwaan_22",
                "kesan": "Kayanya baik tapi masih jarang interaksi",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton f1",
                "sosmed": "@ali_parisi3",
                "kesan": "Bg Ali baik dan humble",  
                "pesan": "semangat terus kuliahnya bg, jangan lupa istirahat"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "123450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Rajabasa",
                "hobbi": "Nguras kolam lele",
                "sosmed": "@cacalvra",
                "kesan": "Kakak ini cantik dan imutt",  
                "pesan": "semangat terus kuliahnya kak, tetap jadi orang yg murah senyum"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Ternak ayam",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Kayanya baik tapi masih jarang interaksi",  
                "pesan": "semangat terus kuliahnya"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": " 124450089",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Kotabaru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Kayanya baik tapi masih jarang interaksi",  
                "pesan": "semangat terus kuliahnya bg, jangan lupa istirahat"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": " 124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live Tiktok",
                "sosmed": "@bryantel_",
                "kesan": "Abangnya baik, tapi kayanya adalah org yg tidak enakan",  
                "pesan":"semangat terus kuliahnya bg, sukses selalu yang dikerjakan"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": " Live tiktok bareng Bryan",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Jl. Pulau Damar",
                "hobbi": "Diving",
                "sosmed": "@afdall.03",
                "kesan": "bg afdal baik, dan ramah",  
                "pesan":"semangat terus kuliahnya bg, jangan lupa istirahat"# 1
            },
            {
                "nama": "Dafa Elpriza",
                "nim": " 124450131",
                "umur": "21",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Persis",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abangnya asik, ramah bgtt, dan baik",  
                "pesan": "semangat terus kuliahnya bg"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": " 124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat selalu kakk"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Lari",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Sukses selalu kakak, lancar semua perkuliahan "# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@andra.lhm",
                "kesan": "Abangnya asik, ramah bgtt, dan baik",  
                "pesan": "semangat selalu bang, semoga selalu diberkahi"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@aayuandriani_",
                "kesan": "Kakak ini asik, baik, dan ramah",  
                "pesan":"semangat selalu kk, semoga ketemu hal baik selalu"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen PSDA":
    def PSDA():
        gambar_urls= [
            "https://drive.google.com/uc?export=view&id=1838vP5VamJwoh5tKUWFk7sFL5qCF1aDs",
            "https://drive.google.com/uc?export=view&id=1a1Q7p3uembCCOHkUmtpepbTmCrtR66UG",
            "https://drive.google.com/uc?export=view&id=1r6k-yBZFozEYOMpE-Doz-TBWnIymSV-8",
            "https://drive.google.com/uc?export=view&id=1Rhdqrgi7HLoqLcIyOEOZWZWfG3zHhmCF",
            "https://drive.google.com/uc?export=view&id=17i4HhxCCuTLxZ2sdpVUBvGGEmHCsC6Kr",
            "https://drive.google.com/uc?export=view&id=1c0rFw1fH1OQh82tVQsQ3WNrh6y2t65vd",
            "https://drive.google.com/uc?export=view&id=1pUsIrKxVLdyrZSThU8XebEdhou2bnSNH",
            "https://drive.google.com/uc?export=view&id=1zFo_RiQzvGJ0a56BCZmFp5Wmubo1dH_F",
            "https://drive.google.com/uc?export=view&id=1YRfqSyRPVKzMIWWnALCXATsFGR__BGwa",
            "https://drive.google.com/uc?export=view&id=1xmyBSYcZz2g06MUnoIDnf_Zc_JkAc2fV",
            "https://drive.google.com/uc?export=view&id=1De35_xHZ3w1BueNx8uH3GWUV9ecs4TDf",
            "https://drive.google.com/uc?export=view&id=1hFcPDEPGsFoXdZhLFNKaRYig_zZfwxr6",
            "https://drive.google.com/uc?export=view&id=1DaCuG3t1YbsC0SqiOnzG9UZ2QnWly3Ql",
            "https://drive.google.com/uc?export=view&id=1_3rGhFO2Yh6QBX4ESuDjl3YxWkHoV-v_",
            "https://drive.google.com/uc?export=view&id=1Ge1ddegopcZnVLlsIbT7sCFBJjw4Ou6D",
            "https://drive.google.com/uc?export=view&id=1aoawbnQYwtL0fff25H4_HltJx2_wOxx8",
            "https://drive.google.com/uc?export=view&id=1g_N0KpTQR6_rHqZCtz76zp9mbd7W661m"
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21 Tahun",
                "asal" :"Kalianda",
                "alamat": "Samping kost bang haikal",
                "hobbi": "Ngerjain TA",
                "sosmed": "@arientakhsnl",
                "kesan": "Kakak ini cantik, trus soft spoken bgt ",  
                "pesan":"semangat terus kuliahnya kakak semoga cepat lulus!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "21,5 tahun",
                "asal": "Kuala Lumpur",
                "alamat": "Samping kost kak arienta",
                "hobbi": "Pacaran",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini cantik, bestie kak arienta deh kayanya kak vany baik",  
                "pesan":"semangat terus kuliahnya kakak, semoga sukses selalu"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "30 Tahun",
                "asal": "Rumah Sakit",
                "alamat": "Belakang Wardat",
                "hobbi": "Kayak irfan",
                "sosmed": "@nobelnizam",
                "kesan": "Bg Nobel baik, tapi rada takut gitu karna masih jarang interaksi",  
                "pesan":"semangat terus kuliahnya bang, semoga secepatnya sidang"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "17 tahun",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Ngejek Orang",
                "sosmed": "@desmanhal",
                "kesan": "Bg Desman baik, humble, dan asik.Tapi aku sempet sebel karna wktu panit di asrama beliau sering bgtt terlalu kritik divisi aku",  
                "pesan":"semangat kuliahnya bang, semoga selalu diberkati Tuhan dan secepatnya S.Si.D"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20 Tahun",
                "asal":"Lampung Tengah",
                "alamat": "Sebelah kost jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bg Azmi overaktif bgt, agak kget wktu pertama kali liat waktu damaskus",  
                "pesan":"semangat terus kuliahnya bg, jangan lupa makan"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450008",
                "umur": "10 Tahun",
                "asal":"Di Bandung",
                "alamat": "Kamar haikal",
                "hobbi": "Goreng ayam",
                "sosmed": "@ykeall",
                "kesan": "Bg Ayake baik dan lucu awal kenal, tapi agak takut kalo ketemu sekarang kaya segan gitu",  
                "pesan":"semangat terus kuliahnya ya bg, fun fact aku dan jauza tidak tau abg terjatuh waktu riuh november 2025 itu, kami ketawa karna abg lucu aja jadi jangan salah paham lagi"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21 Tahun",
                "asal": "Rahim ibu",
                "alamat": "Diatas kost jemar",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Baik tapi kaya keliatan bgt tegasnya jadi segan tapi aku jujur senang kalo abgnya ngomong adek awak karna aku sebnarnya oengen punya abg hehee",  
                "pesan":"semangat terus kuliahnya bg, jangan lupa istirahat"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "20 tahun",
                "asal": "Debu Tanah",
                "alamat": "Sebelah pasar",
                "hobbi": "Ngegiring anak ayam",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kakak baik tapi fist impression aku kaya kk galak bgt waktu pplk jadi kebawa sampe sekarang",  
                "pesan":"semangat terus kuliahnya kakak, semoga lancar semua kerjaannya.Btw blush on kk lucu bgtt"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "17 Tahun",
                "asal": "Batam",
                "alamat": "Sebelah kost jemar atau kak arienta",
                "hobbi": "Ngurus pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal baik, ramah tapi ttp kaya agak canggung karna jarang interaksi",  
                "pesan":"semangat terus kuliahnya bg, jangan lupa makan"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18 Tahun",
                "asal": "Kampung Orang",
                "alamat": "Nomaden",
                "hobbi": "Duduk sebelah henry",
                "sosmed": "@dellaansaftr",
                "kesan": "Kak Putri baik bgt, aku kenal waktu panit paskah SD kak putri cantik",  
                "pesan":"semangat terus kuliahnya kak, maaf aku sering salfok rambut kk lucu bgtt"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Depan Pemancingan",
                "hobbi": "Ngoleksi ayam warna warni",
                "sosmed": "@queentanaabila",
                "kesan": "Kakaknya baik dan ramah juga mudah senyum",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupa tetap jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19 Tahun",
                "asal": "Lampung",
                "alamat": "Teluk",
                "hobbi": "Main game",
                "sosmed": "@azzelytn",
                "kesan": "Kakak ini baik dan lucuu",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21 Tahun",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charr baik bgtt, fast respon dan humble",  
                "pesan":"semangat terus kuliahnya kak, makasih udh mau direpotin buat foto ulang"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "18 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sebelah kost haikal",
                "hobbi": "Gembala",
                "sosmed": "@jemarrro",
                "kesan": "Muka abgnya lucu bgt, bg jemar baik dan lawak",  
                "pesan":"semangat terus kuliahnya bg, semoga kalau dikemudian hari kita ketemu dan aku nyapa abg tidak buang muka lagi hehee"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "19 tahun",
                "asal": "Lampung tengah",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kakak ini baik dan lucu",  
                "pesan":"semangat terus kuliahnya kak, jaga kesehatan selalu"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20 Tahun",
                "asal": "Sibolga",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@dearfkvmfl",
                "kesan": "Bg rafly baik kayanya tapi jujur sebenarnya agak jarang liat jdi kurang tau jugaa",
                "pesan":"semangat terus kuliahnya bg, semoga sukses selalu"# 1
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20 Tahun",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Tidur",
                "sosmed": "@avi.nhr",
                "kesan": "kk Salavi baik, ramah dan humble bgt",   
                "pesan":"semangat terus kuliahnya kak, btw kk imut bgtt lucuu"# 1
            }      
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TY7TBe2l8BSeAkBz0DTRbfyObhMOWuKT",
            "https://drive.google.com/uc?export=view&id=15CjGmfKeb_e4pbFLx0315puTt8rl-_lx",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1HVix5Ou7lzB-vD747-6-53RZAs7iW14Q",
            "https://drive.google.com/uc?export=view&id=15Vy5p8PuuMCZcPjKtxfLCKvMpg45d2OF",
            "https://drive.google.com/uc?export=view&id=1S-BZuakBsBUefP0qJmEHH6Gz1Z4AEgK0",
            "https://drive.google.com/uc?export=view&id=1pj8-Zl0rszdEUybMk_6LD-x_Rt5ffn5E",
            "https://drive.google.com/uc?export=view&id=1vI4n6-OvPQIyZIMPGQcXrmRfRh20Ml_x",
            "https://drive.google.com/uc?export=view&id=1f_Af5pjc5Yy-kw3Xg7LzZZ4wCnCgOTw1",
            "https://drive.google.com/uc?export=view&id=1Q-XUPAKPX5g4yX0ScIu0j6ognzgcHU3X",
            "https://drive.google.com/uc?export=view&id=1QMG1ATBLKeb0wydj4v0kHyCKWtx2ET_I",
            "https://drive.google.com/uc?export=view&id=1KhFlO0uzxYxirbk-yeBYAYZsMljpk8Rm",
            "https://drive.google.com/uc?export=view&id=1akWWLPKZ5CD2huCg8AfhrCTfPDFWHN_9",
            "https://drive.google.com/uc?export=view&id=1bq2ZVCB_9pP-Sd7xctQDjJqlpbhZFyKD",
            "https://drive.google.com/uc?export=view&id=1qUY26XRcee_rY1i8zvxFJfcsR2rSVmbj",
            "https://drive.google.com/uc?export=view&id=1e64rPvGkJbBt9_ETEvVzxbzuzsbg73oO",
            "https://drive.google.com/uc?export=view&id=1X25pm9e_59b1h4O7jjJR_wd0o5InT-tB",
            "https://drive.google.com/uc?export=view&id=1ZBxh34o0ogv9TKcKvrhgiGcq-ZnaSu0O",
            "https://drive.google.com/uc?export=view&id=1isA1QlgkA6UlbPfsrc5IVaoO5SXqd8E_",
            "https://drive.google.com/uc?export=view&id=1zG8cNSFBHxUcQFsrGbtIsePmwMXjwp_7",
            "https://drive.google.com/uc?export=view&id=1Kd5F9EnCW96VjUYJzD_8wmGS_4x_01V8",
            "https://drive.google.com/uc?export=view&id=1YUJkSoeHBveXBL70oaUFnZOCzDxk_65f"
        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Main game & travel",
                "sosmed": "@biyokcb",
                "kesan": "JUJUR KEREN BANGETTTT, pinter, aktif dan baik.",
                "pesan": "Semangatt kuliahnya ya banggg, Aku berharap bisa lebih banyak belajar dri bg fabio"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@tvnty_",
                "kesan": "First impression ku ke kaka, kaka ceria banget, aktif jugaa",
                "pesan": "Semangatt menjalani hari-hari menyenangkannya, jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "Inspiratif bangett",
                "pesan": "Masih ga nyangka secepat itu abang kembali ke pangkuan-Nya, tapi sekarang abang udah ga sakit lagi ya.. Doa terbaik untuk mu bang Fadil, fly high and rest in peace a good soul"
            },
            {
                "nama": "Akeyla Fairus Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandara Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Jujur keren keren bangg, pintar dan aktif",
                "pesan": "Semangat kuliah nya bangg, semoga dipermudah jalan dan urusannyaa!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Pinter bangett, aktif jugaa",
                "pesan": "Semangattt buat TA-nya bg, semoga lulus secepatnya"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way kandis",
                "hobbi": "Katama",
                "sosmed": "manuelfdk_",
                "kesan": "Keliatan pinter tapi baik dan tidak pelit ilmu",
                "pesan": "Abang keren bangett, jangan lupa jaga pola tidur dan makan nya!"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Travelling",
                "sosmed": "@violaadrtr_",
                "kesan": "Kaka cantik dan baik",
                "pesan": "Kaka semangat kuliahnya yaa, sukses selaluu"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Cantik dan baik",
                "pesan": "Semangat menjalani perkuliahan dan berbagai kegiatan kk,tetap jaga kesehatan kaa!"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Telung Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "Kknya baik dan cantikk",
                "pesan": "Semangat selalu kk, semoga bertemu hal baik selalu"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "Ceria dan ekstrovet banget, ",
                "pesan": "Semangat selalu kk, senang pernah satu panit sama kk waktu paskah SD!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Gemassss dan ceria bangett",
                "pesan": "Semangat selalu kk, yg terbaik menghampirii"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Jl. Kebon Jeruk",
                "hobbi": "Nonton Film",
                "sosmed": "@lovianora_s",
                "kesan": "Kakaknya baik banget, kenalnya waktu kak lopii jadi asprak beliau asprak menyenangkan",
                "pesan": "Semangat terus belajar dan kuliahnya kak, semoga tercapai semua yang kakak kerjakan sekarang."
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@keyashafi",
                "kesan": "Abang keren, baik bgtt dan keliaatannya pinter bgt",
                "pesan": "Semangatt terus ya bang kuliahnyaa, jangan lupa jaga kesehatan jugaaa!!"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Cantik imut tapi kaya gak mirip kak jue menurut aku",
                "pesan": "Semoga lancar semua yang kk kerjakan, sukses selalu"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@faizaanjanii",
                "kesan": "Cantik, imut, dan mudah senyum",
                "pesan": "Kaka beneran keren bangetttt, jangan pernah berhenti menebar senyum manis kk yaaa..."
            },
            {
                "nama": "Gathfan Nadif ALi",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Abang baik dan keren",
                "pesan": "Semangatttt kuliahnya banggg, jangan lupa jaga kesehatan yaa.Semoga sukses selaluu!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "Keren, pinter dan lucuu",
                "pesan": "Semangatt bang kuliahnyaa, ttp jadi manusia dengan aura positif abg yaa"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450062",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Kerennn dan pinter banget, baik dan ramahh",
                "pesan": "Semoga bertemu hal baik selalu ya bg, jangan terlalu sering spin si kataku apalagi kalau biasanya abis bagus selalu aku ketunjuk hehe"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Menari",
                "sosmed": "@melva_fbrt",
                "kesan": "CUTEEE, beneran gemas bangettt",
                "pesan": "Semangatt kaa kuliahnyaaa!!"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "125450099",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Asrama",
                "hobbi": "Membaca",
                "sosmed": "@syaafiq",
                "kesan": "First time kenal wktu di asrama wktu abg mau brngkt PKM jujur keren bgt dan aktiff",
                "pesan": "Semoga semua hal yang abang kejar dan impikan tercapai dan sukses selalu"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "150 (p, mksud bg??? #kaget)",
                "asal": "Rajabasa",
                "alamat": "Balam",
                "hobbi": "Tennis Meja",
                "sosmed": "@henryferdianto",
                "kesan": "Pinter bgt, baik dan aktif ",
                "pesan": "Lancar semua urusannya ya bg, jangan lupa makan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pruo-A_5tWmhHLCN4MCvdPTRv-qAxef3",
            "https://drive.google.com/uc?export=view&id=1PeyyHraHWbd3MsONT-Sl77VqDUgsqT5d",
            "https://drive.google.com/uc?export=view&id=1qt5zcroZ42MuVde3fkATnDuzoVSTlasE",
            "https://drive.google.com/uc?export=view&id=1OKY_0RzLxRD09hj6GxpKzuJDH9SINkI1",
            "https://drive.google.com/uc?export=view&id=1yHNQtPUMyZ1nm-ovE6-14d4hNugojKKF",
            "https://drive.google.com/uc?export=view&id=1J3jSqVERa68Q6gqr2eHRQjZ4Wjlwofas",
            "https://drive.google.com/uc?export=view&id=1rqKvszSFDBSsajApvKUzncC30rQNdr_Q",
            "https://drive.google.com/uc?export=view&id=18ihtljmc3LIFADP8eAJX_S4fB868XeWZ",
            "https://drive.google.com/uc?export=view&id=1NpvvrfA6NdC5P1ekB-hVTiPrgbLtYQ90",
            "https://drive.google.com/uc?export=view&id=17rJNXfqNn4teBbj_GtosgcpIjQGeIfAh",
            "https://drive.google.com/uc?export=view&id=1tt4bpK6cvf3Z03OeVODPZkvyxkCS_8ZW",
            "https://drive.google.com/uc?export=view&id=1cvU7_XNcPVgdmc1jfANWdEFliroCOek3",
            "https://drive.google.com/uc?export=view&id=15eAp_-eu4h2y8r_BI1B02sW5TnfQPTB1",
            "https://drive.google.com/uc?export=view&id=1ZHCQBAJurtqvhNlDam2tjBpvEezjvg4J",
            "https://drive.google.com/uc?export=view&id=1zcyshcck8edFc_Yp76V230bHpKb9pX1x",
            "https://drive.google.com/uc?export=view&id=1ziW3bhfxgfTIgYsTzYaCK_IvzsNTs62a"           
        ]
        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450006",
                "umur": "20 Tahun",
                "asal":"Sidikalang, Sumut",
                "alamat": "Belwis",
                "hobbi": "Ngoding",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang ini asik parah, baik, dan yapping banget.Trus bg hekal ternyata oversharing hehee ",  
                "pesan":"Semoga cepat selesai TA nya bang, kami menunggu bc-an sidangnya "# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21 Tahun",
                "asal": "Untung suropati",
                "alamat": "..",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya gemas, cantik bangett, dan baik",  
                "pesan":"Semangat terus belajarnya kak"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "11",
                "asal": "Kisaran",
                "alamat": "Untung",
                "hobbi": "NMenyapa satpam ITERA",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kkaknya aktif dan keren banget, kak hana orangnya sangat penuh apresiasi ",  
                "pesan":"semangat terus dan aktif terus kak kuliahnya, nanti kita main uno sama karaoke yaa"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "124450064",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "Perumnas way kandis",
                "hobbi": "Ngikutin drama tiktok",                
                "sosmed": "@hnfdzky_",
                "kesan": "Abangnya asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya bg, secepatnya S.Si.D"# 1
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhanghani",
                "kesan": "Abangnya asik, baik, dan ternyata receh, baik, dan asik bangettt",
                "pesan":"Semangat terus belajar dan kuliahnya bang"# 1
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "12450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Samping kuburan belwis",
                "hobbi": "Suka eksperimen",
                "sosmed": "@aisahkhair.",
                "kesan": "kakak ini baik banget, senyumnya manis bgt",  
                "pesan":"Semangat terus dan aktif terus kk kuliahnya"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450079",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Pesisir belwis",
                "hobbi": "Suka begadang",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kakaknya asik dan baik banget",  
                "pesan":"Semangat terus dan aktif terus kk kuliahnya"# 1
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "1244500094",
                "umur": "19",
                "asal":"Kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Buat lagu",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Abangnya baik dan ramah banget,asik dan receh",  
                "pesan":"Semangat terus belajar dan kuliahnya bg, tercapai semua yang lagi dikejar"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "1244500051",
                "umur": "20 Tahun",
                "asal":"Sumbar",
                "alamat": "Belwis",
                "hobbi": "Main ML",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450",
                "umur": "18 Tahun",
                "asal":"Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin Harvin dikelas",                
                "sosmed": "@rozakramdani_",
                "kesan": "Abangnya baik, tapi sibuk bgt kayanya, chat aku blm dibales smpe sekarangg",  
                "pesan":"Semangat terus belajar dan kuliahnya bang"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Jadi asprak",                
                "sosmed": "@christiani8872",
                "kesan": "Kak Tere asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kk, ayo panit breng lagii"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20 Tahun",
                "asal": "Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Masak",                
                "sosmed": "@audina_",
                "kesan": "Kk Audina asik dan baik banget, mukanya lucuw",  
                "pesan":"Semangat terus belajar dan kuliahnya kk"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin dina ngomong bahasa minang",                
                "sosmed": "@cikamrbn",
                "kesan": "Kakaknya asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21 Tahun",
                "asal": "Toba,Sumut",
                "alamat": "Airan Raya",
                "hobbi": "nonton drakor",                
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakaknya baik tapi agak pendiem",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20 Tahun",
                "asal":"Sematera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berburu",                
                "sosmed": "@Muhvinz_",
                "kesan": "Bg Harvin baik bgtt fastrespon, dan humble poll",  
                "pesan":"Semangat terus belajar dan kuliahnya bg!"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nitip makan sama aqila",                
                "sosmed": "@snasaa._",
                "kesan": "Kakaknya baik banget, awal kenal agak canggung karena beliau agak pendiem tapi ternyata makin laam makin dekett, ibunda kecintaan anovers",  
                "pesan":"Semangat terus belajar dan kuliahnya kak,semoga tercapai semua yang kakak dambakan, kita jangan asing yaa mari tetap menjadi anovers abadi."# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()
# Tambahkan menu lainnya sesuai kebutuhan
