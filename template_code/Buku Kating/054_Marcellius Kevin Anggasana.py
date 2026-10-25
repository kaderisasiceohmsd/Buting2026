import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import parse_qs, urlparse

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
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#F4E7DB"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#EAD6C4",
            },
            "nav-link-selected": {"background-color": "#8A5A44"},
        },
    )
    return selected

@st.cache_data(ttl=300)
def load_image(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc in {"drive.google.com", "www.drive.google.com"}:
        file_id = parse_qs(parsed_url.query).get("id", [None])[0]
        if file_id is None:
            path_parts = parsed_url.path.split("/")
            if "d" in path_parts:
                file_id_index = path_parts.index("d") + 1
                if file_id_index < len(path_parts):
                    file_id = path_parts[file_id_index]
        if file_id:
            url = f"https://drive.google.com/uc?export=download&id={file_id}"

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
    except requests.RequestException as e:
        st.error(f"Failed to fetch image from {url}: {e}")
        return None

    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data(ttl=300)
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
            data = {key.casefold(): value for key, value in data_list[i].items()}
            for label in (
                "Nama",
                "Jabatan",
                "Nim",
                "Umur",
                "Asal",
                "Alamat",
                "Hobbi",
                "Sosmed",
                "Kesan",
                "Pesan",
            ):
                if label.casefold() in data:
                    st.write(f"{label}: {data[label.casefold()]}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")

menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yvIhkss91Cc6YBPjGwwY_DFep-QTVCTW",
            "https://drive.google.com/uc?export=view&id=1wEy1rlJ0boxS1cLWaLb4FAMWVOxMAm-B",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1htPWN67uB2p3jM6GEoxs_Ppoj0lL2qiL",
            "https://drive.google.com/uc?export=view&id=1eAoo7IpcUje0ZFKkuA6gj6uL-mwHmETt",
            "https://drive.google.com/uc?export=view&id=15N6p3clQCSFfjnW4AEh8HECtq6ZoCyIm",
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "Jabatan" : "Ketua Himpunan",
                "Nim": "123450103",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "push rank sampe imo",
                "Sosmed": "@jars_mrp",
                "Kesan": "Abangnya kalem, asik juga waktu jadi pemateri tidak kaku",  
                "Pesan":"info party ml ke imo bang"
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "Jabatan" : "Sekretaris Jenderal",
                "Nim": "123450066",
                "Umur": "22",
                "Asal":"Riau",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "Zikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Abangnya asik, lucu, suka bercanda juga, tinggi juga abangnya",  
                "Pesan":"ajarin saya zikir bang"
            },
            {
                "Nama": "Efi Defiyati",
                "Jabatan" : "Sekretaris 1",
                "Nim": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobbi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "Kakaknya verry well",  
                "Pesan":"semangat membacanya kak"
            },
            {
                "Nama": "Qois Olifio",
                "Jabatan" : "Sekretaris 2",
                "Nim": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio_ ",
                "Kesan": "Abangnya keren, kalem, lucu",  
                "Pesan":"mau dong bang suratnya"
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "Jabatan" : "Bendahara 1",
                "Nim": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Bertemu Kesekjenan",
                "Sosmed": "@hafsafadhilaa",
                "Kesan": "Kakaknya cantik, baik, kalem, asik juga",  
                "Pesan":"Semangat terus kak, sehat selalu"
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "Jabatan" : "Bendahara 2",
                "Nim": "123450004",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Airan",
                "Hobbi": "Mintain Duit",
                "Sosmed": "@luthfiaarmdhni ",
                "Kesan": "Kakaknya lucu, baik, keren, asik juga",  
                "Pesan":"semangat dah kak mintain duitnya"
            },                                                  
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()                

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IVPEWAu2rvPYXDAiWzEtDNHa6d8-9tws",
        	"https://drive.google.com/uc?export=view&id=13ES9xdRUrC0DYYG32Q8InXgZjEpPYKas",
        	"https://drive.google.com/uc?export=view&id=149zm-CpBFt9e_OmC7xZgHoSs_0I98kQx",
        	"https://drive.google.com/uc?export=view&id=15mEQw4QZVPvNqspSE6I-b86GHQeN_jXe",
        	"https://drive.google.com/uc?export=view&id=1m42L0OBkx3DGsIwZZvD7l7Zb-rR6TYin",
        	"https://drive.google.com/uc?export=view&id=1yhKUlw8AhIUIlrdjQXZrUDiqvqfHTtUx",
        	"https://drive.google.com/uc?export=view&id=17FQoyj3uc4_8vg4MJDhnj25uxK-KLHJ8",
        	"https://drive.google.com/uc?export=view&id=1HUql-G-Up-_uezRYBz4CLeG2kd6K6Jt1",
        	"https://drive.google.com/uc?export=view&id=1Uw1zQDXrhFT541hi3ROffXh_e4DjwBZA",
        	"https://drive.google.com/uc?export=view&id=1syXbBrD1ol9Pg5jQVS4aHkaL9fuPMhqz",
        	"https://drive.google.com/uc?export=view&id=1L-RUOVMGQl00gkXe_n3fWv6jQCcyaO1f",
        	"https://drive.google.com/uc?export=view&id=1ela06RiCy4pwPloedYA-qgt3Gh66t5Hg",
         	"https://drive.google.com/uc?export=view&id=1-gUhXegEe588q3S-8PUq5K3hSr6WAKNi",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Kota Manchester",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "SERU BANGETTT!!! abangnya beneran lucu terus celetukannya, beneran pabrik jargon hahaha",  
            	"pesan":"welcome bang to hana hani boys"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu semusim dari marsel",
                "sosmed": "@j__eesie",
                "kesan": "kakaknya cakep euy",  
            	"pesan":"jangan lupa makan kak"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupin api baleg di tiktok",
                "sosmed": "@exvoltas",
                "kesan": "Pinter bnaget abangg, tips and trik mapres bangg",  
            	"pesan":"gacor bwang"
            },
            {
                "nama": "Gh. Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "Lucu banget jokes jokes abangnyaa",  
            	"pesan": "Semangat terus kuliah dan organisasinya!"
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Imutt sekali kakanyaaa",  
            	"pesan":"Semangattt kaa kuliahnyaa, kaka imut balegg"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang gip chill banget orangnyaa dan seruu",  
            	"pesan":"info mabar ml bang"
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "19",
                "asal": "Kepulauan Mentawai",
                "alamat": "Owen Kost",
                "hobbi": "Ngoding",
                "sosmed": "@afghanisnt_",
                "kesan": "Public speakingnya bagus, aku dukung kaka jadi the next kadiv komisi 2 #YIPPIE",  
            	"pesan":"Semangat kaa kuliah dan organisasinyaa!!"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "CTR",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "Lucu dan gemas bangettt",  
            	"pesan":"Semangat ka menghadapi bang Ridhoo, semoga dilancarkan semua urusannya kaaa!"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Teluk",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Keren dan berwibawa",  
            	"pesan":"Semangat bang kuliahnyaaa!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Lucu, gemas, tapi tegas",  
            	"pesan":"Semangat kaa kuliah dan organisasinyaaa!"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450111",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym sama Koleksi figure, nafas manual",
                "sosmed": "@nagatseee",
                "kesan": "Lucu abangnya, jokes jokesnya juga fresh",  
            	"pesan":"Semangat abang kuliah dan organisasinyaa!"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Jajan sama nisa, putri, suci",
                "sosmed": "@sekardnwp",
                "kesan": "Tegas tapi chill juga",  
            	"pesan":"Semangat terus ka kuliah dan organisasinyaa!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Lemah lembut sekaliii",  
            	"pesan":"Semangat kaa TA dan kuliahnyaa!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14JzXXEVYnTlG5rJSwqfCZRGoJGhHX7x6",
            "https://drive.google.com/uc?export=view&id=1_Db1mRL_t0m7C97r3Ybiwoxb_0zCktbn",
            "https://drive.google.com/uc?export=view&id=1xHSXf9wPh9k7SDgmE6KVCyBU2JgwV6ys",
            "https://drive.google.com/uc?export=view&id=1PI4A4b2LME35IYSvGMSiok1nWqTU2jlg",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1j8fnVVg2hOuA2_fvm3RtyjYU02usZdzu",
            "https://drive.google.com/uc?export=view&id=1peYrAOiYLXURfuze8Sjzx-bRovVqjjbu",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "Jabatan": "Senator",
                "Nim": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobbi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kakaknya cantik, baik, kalem, keren",
                "Pesan": "Sehat selalu kak, semoga lancar skripsinya"
            },
            {
                "Nama": "Helmy Surya Pratama",
                "Jabatan": "Kepala Biro Aspirasi dan Media Komunikasi",
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
                "Jabatan": "Staff Biro Aspirasi dan Media Komunikasi",
                "Nim": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah Kamar Biwa",
                "Hobbi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Abangnya baik, asik, kalem",
                "Pesan": "Semoga selalu dimudahkan bang"
            },
            {
                "Nama": "Suci Aulia",
                "Jabatan": "Staff Biro Aspirasi dan Media Komunikasi",
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
                "Jabatan": "Staff Biro Aspirasi dan Media Komunikasi",
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
                "Jabatan": "Kepala Biro Kajian Strategis dan Propaganda",
                "Nim": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobbi": "Nonton",
                "Sosmed": "@lia,h_264",
                "Kesan": "Kakaknya lucu, asik juga",
                "Pesan": "Semoga kuliahnya lancar ya kak"
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "Jabatan": "Staff Biro Kajian Strategis dan Propaganda",
                "Nim": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobbi": "Mendokumentasi Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Kakaknya lucu, keren juga",
                "Pesan": "Semoga kelompoknya nambah gacor kak"
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "Jabatan": "Staff Biro Kajian Strategis dan Propaganda",
                "Nim": "124450114",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Lampung Timur",
                "Hobbi": "Giring Ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Abangnya keren, asik juga",
                "Pesan": "Semoga sukses bang"
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "Jabatan": "Kepala Biro Kesekretariatan",
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
                "Jabatan": "Staff Biro Kesekretariatan",
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

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rNcKQlNYCMNnKNtUWlSr15IkwoQM6GXQ",
            "https://drive.google.com/uc?export=view&id=1G02_2bW4gM9SAtJ0eBPXWsmXmcoiHkA0",
            "https://drive.google.com/uc?export=view&id=1UwRzJXD0S_5xpGtlYHJsVVLog-EyqyKg",
            "https://drive.google.com/uc?export=view&id=1BLuH3iD7bG785ycto0n0bNkpqEtHaLV0",
            "https://drive.google.com/uc?export=view&id=1cyf59UqE_JJXDymbQ1Kqy9IQLldLLg8T",
            "https://drive.google.com/uc?export=view&id=12u_PoPxg62fs8xRrHkCMu8LZKq2KR8Zk",
            "https://drive.google.com/uc?export=view&id=1ovlJYxmpNyj2NNAMgUzKXzJBO6cAG2J6",
            "https://drive.google.com/uc?export=view&id=1jZ6RyszCWGZpso7_egBmG1L9PjF3loSK",
            "https://drive.google.com/uc?export=view&id=1BXIUlVMqkkCc4WxpZSV__KSS75XfuCMt",
            "https://drive.google.com/uc?export=view&id=12bcolMqU1A620eAPnnYwdPaxlpscLfHi",
            "https://drive.google.com/uc?export=view&id=1ABebNipqyy6bCH5n9SfIjF2YAn40K6bQ",
            "https://drive.google.com/uc?export=view&id=1Q1DuMy0D-BEZOE2IDUdkN4IbNch9u5Qj",
            "https://drive.google.com/uc?export=view&id=1ZYQsrvMR_0tgC85mTUsEl2zPTklRP0P4",
            "https://drive.google.com/uc?export=view&id=1WlmnAQhSzkIrfjUGVFXAw-d3v7TsSLq7",
            "https://drive.google.com/uc?export=view&id=1n182UlK2jOBZU3R6c_ZegZI6fqVchGxj",
            "https://drive.google.com/uc?export=view&id=1u60eoBavUexPI4zSDTHOnaoPYJFgr_kK",
            "https://drive.google.com/uc?export=view&id=1K1Xhiikwf1ES4Tb1PieNX2YvKO3Sflgt",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Deket Pantai Kedu, Kalianda",
                "alamat": "Samping kos capo",
                "hobbi": "Baca jurnal",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arienta baik, keren, peduli, dan humble bangetttt",  
                "pesan":"Semoga diberi kesuksesan dan kesehatan selalu ya kak!!!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Nyanyi dan masak ayam",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany baik, berwibawa, dan disiplin banget",  
                "pesan":"Semoga selalu diberi kemudahan ya kakak!!!"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Urip",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel Berwibawa, Asik dan jago banget sulap, baik, tegas, dan keren banget",  
                "pesan":"Semogaa sukses dan berkah selalu ya bang!!!"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Teriak",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi keren, gentle, tegas, dan energik bangetttt",  
                "pesan":"Semoga selalu diberikan kesehatan dan kekuatan ya bang!!!"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadhan",
                "nim": "124450081",
                "umur": "21",
                "asal":"paninjauan 10 kota di atas solok sumatera barat",
                "alamat": "blok d 79 jl.manggis 8 perum pemda wayhui jatiagung lampung selatan",
                "hobbi": "Memasak",
                "sosmed": "@_ykeal",
                "kesan": "Bang Ayake humoris, asik, humble dan baik bangetttt",  
                "pesan":"Semoga selalu sehatt, bahagia, dan lancar rezekinya ya bang!!!"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal":"Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar Baik, keren dan imut, serta suka berbagi ilmu",  
                "pesan":"Semoga selalu diberikan kelancaran ya bang!!!"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Rahim ibu",
                "alamat": "sebrang kost yazid rizal",
                "hobbi": "ngapain aja deh",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Yudia ramah, tegas, keren, baik dan humble bangetttt",  
                "pesan":"Semoga selalu semangat dan bahagia ya kak!!!"# 1
            },            
            {
                "nama": "Haikal Saventio Tamba",
                "nim": "124450014",
                "umur": "20",
                "asal":"Sibolga",
                "alamat": "Di depan kostan bang ayake belok kanan",
                "hobbi": "Mencari pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal baik, tegas, asik, jago futsal, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan terhindar dari segala penyakit ya bang!!!"# 1
            },            
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri baik, lucu, imut, dan humble bangetttt",  
                "pesan":"Semoga selalu diberikan keselamatan dan kebahagiaan ya kak!!!"# 1
            },            
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal":"Cikajang",
                "alamat": "Tempat pemancingan",
                "hobbi": "Baking",
                "sosmed": "@queentanaabila",
                "kesan": "Kak Queenta baik, ber aura, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat, bahagia dan diberi keselamatan ya kak!!!"# 1
            },            
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450113",
                "umur": "25",
                "asal":"Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman baik, asik, humble, dan jago bangetttt deffense futsalnya",  
                "pesan":"Semoga selalu semangat dan sukses ya bang!!!"# 1
            },            
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel baik, kalem, dan humble bangetttt",  
                "pesan":"Semoga bahagia dimanapun kakak berada ya kak!!!"# 1
            },            
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal":"Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah baik, santai, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan bahagia ya kak!!!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jere humble, asik, kece, dan baik bangetttt",  
                "pesan":"Semoga selalu kuat dan sehat ya bang!!!"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila baik, santai, dan humble bangetttt",  
                "pesan":"Semoga selalu dilancarkan urusannya ya kak!!!"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Bang Rafli kece, rambutnya keren terus, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan doa nya diwujudkan ya bang!!!"# 1
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salafi baik, lucu, kalem dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan dilancarkan urusannya ya kak!!!"# 1
            },                      
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Minbak":
    def minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oqUSSv9PCROtEVEeTRSU2mNxvySFDt9U",
            "https://drive.google.com/uc?export=view&id=1FNKFsvlYbZ-j-92wGevQfn5PdRqh2dmC",
            "https://drive.google.com/uc?export=view&id=1G76dFsoImPIf2ZQkEMh4qfSX10NtRl1_",
            "https://drive.google.com/uc?export=view&id=1Ex-XTPwGrg4PBqLUhzxkaYYDs7jPBSRV",
            "https://drive.google.com/uc?export=view&id=17pP_eDA2lqRFRrQQ6wFldCXKZiHElwpt",
            "https://drive.google.com/uc?export=view&id=1-9jB4Snc4tKs7tH2KHfcpQiXyj4c8Qsp",
            "https://drive.google.com/uc?export=view&id=1IOX7hhOk_jHWD2MN-JaILvqzjnPZmdGe",
            "https://drive.google.com/uc?export=view&id=1EupCToVzDVHY4brM0GDyxaHqtWcSw-BK",
            "https://drive.google.com/uc?export=view&id=1KlBsBkvzh-W6ylbUawtMvSQXeLRbpkDp",
            "https://drive.google.com/uc?export=view&id=1AxpKNR4Fespcv6dSvExpDS4gGZUoct-F",
            "https://drive.google.com/uc?export=view&id=16qI7xFD_HvkMBNT2DZOUlMYrs0j0apOI",
            "https://drive.google.com/uc?export=view&id=1E40kFM2DwPK6reatmxgc18_A8_nPn0EM",
            "https://drive.google.com/uc?export=view&id=1KWKFy2dCl97ai5G0zGtEtfiABEx2Oktv",
            "https://drive.google.com/uc?export=view&id=1TwNCAHtEY2OrT7wFG4taCNodPmarUiq8",
            "https://drive.google.com/uc?export=view&id=1XZpTJhkCVqs2lnKAsGIilAsIvToqXoLf   ",
        ]

        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450009",
                "umur": "21",
                "asal": "Sulawesi Selatan",
                "alamat": "Panjang, Bandar Lampung",
                "hobbi": "Main gaplek",
                "sosmed": "@kevinaj_",
                "kesan": "Abangnya kalem, tapi asik, kece juga",
                "pesan": "Sehat terus bang",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki Gunung",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya baik sama ramah",
                "pesan": "Semoga skripsinya nanti lancar kak",
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya kalem sama baik",
                "pesan": "Sukses selalu ya bang",
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar",
                "sosmed": "@aayuandriani_",
                "kesan": "Kakaknya satu asal sama saya, baik kakaknya",
                "pesan": "Sehat selalu kak, semoga dimudahkan seluruh semesternya",
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450024",
                "umur": "21",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Main Futsal",
                "sosmed": "@dafaelpriza_",
                "kesan": "Keren abangnya, kalem, asik",
                "pesan": "Semoga dimudahkan segala urusan bang",
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Muter-muter",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakaknnya baik, satu daerah asal juga sama aku",
                "pesan": "Semoga kedepannya dimudahkan selalu kak",
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "JL. Pulau Damar",
                "hobbi": "Nemenin Bang Ridwan nonton tinju",
                "sosmed": "@afdall.03",
                "kesan": "Abangnya ramah, asik juga",
                "pesan": "Semoga sehat terus bang",
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang ke Metro",
                "sosmed": "@sllbnzw_",
                "kesan": "Kakaknya ramah sama baik",
                "pesan": "Sehat terus kak, semoga dilancarkan segala urusan",
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton tinju",
                "sosmed": "@mridwaan__",
                "kesan": "Abangnya baik, asik juga",
                "pesan": "Semoga skripsinya lancar bang",
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal": "Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nemenin Bryan nonton tinju",
                "sosmed": "@andra.lhm",
                "kesan": "Asik abangnya, diajak ngobrol juga asik",
                "pesan": "Semoga kuliahnya lancar terus bang",
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live TikTok",
                "sosmed": "@bryantel_",
                "kesan": "Abangnya kalem, asik juga",
                "pesan": "Sehat terus bang",
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Main beiblet",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Abangnya lucu, ngomongin ff mulu",
                "pesan": "Semangat terus bang, semoga sukses",
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakaknya baik sama ramah",
                "pesan": "Semoga dilancarkan keinginan dan kemauannya kak",
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Nusa Tenggarang Barat",
                "alamat": "Rajabasa",
                "hobbi": "Nebang Pohon",
                "sosmed": "@cacalvra",
                "kesan": "Kakaknya baik, asik juga",
                "pesan": "Sehat selalu kak",
            },
            {
                "nama": "Muhammad Rafka Fatih Al Fatih Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal": "Padang, Sumatera Barat",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abangnya baik sama kalem",
                "pesan": "Semoga kuliahnya lancar terus jadi orang sukses bang",
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    minbak()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oylYh_wJj9kJxBhycOjoUuZyQy4iwqc3",
            "https://drive.google.com/uc?export=view&id=16BWiIE1iV-372VWNEdSaTQ8SVKup8bd_",
            "https://drive.google.com/uc?export=view&id=1JEMQcNoyX-LVEehUrbE-hrOb95ItRRc-",
            "https://drive.google.com/uc?export=view&id=1Q-acwpX9cd8uYE5iLq2wvt8gCyoi5Fp0",
            "https://drive.google.com/uc?export=view&id=1OyHYAQknvgIVOlUoZNbYTLgqGd1Na1Xd",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1GShT_tr1uuiVYH8nqBADrVXMhm3KaOCw",
            "https://drive.google.com/uc?export=view&id=1kQizU0fgPq8cFqZb-LELGtMlrrZjfyqK",
            "https://drive.google.com/uc?export=view&id=1UKopTIrpxwAv4-NFKNVa8RV6o_WxevjJ",
            "https://drive.google.com/uc?export=view&id=1IGPRIC4Luh3N4hjBe2wEnTNms94-UI3T",
            "https://drive.google.com/uc?export=view&id=1IzVJIq6NhA7vOOirydLkA_Bgx0VqSnfr",
        ]
        data_list = [
            {
                "Nama": "Ihsan Maulana Yusuf",
                "Jabatan": "Kepala Departemen",
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
                "Jabatan": "Sekretaris Departemen",
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
                "Jabatan": "Kepala Divisi Kemitraan",
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
                "Jabatan": "Staff Divisi Kemitraan",
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
                "Jabatan": "Staff Divisi Kemitraan",
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
                "Jabatan": "Staff Divisi Kemitraan",
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
                "Jabatan": "Staff Divisi Kemitraan",
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
                "Jabatan": "Kepala Divisi Kewirausahaan",
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
                "Jabatan": "Staff Ahli Divisi Kewirausahaan",
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
                "Jabatan": "Staff Divisi Kewirausahaan",
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
                "Jabatan": "Staff Divisi Kewirausahaan",
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
                "Jabatan": "Staff Divisi Kewirausahaan",
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

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hEEs-2jIkvUGky_kS6feVtGbAROggwUa",
            "https://drive.google.com/uc?export=view&id=1KXqbcBAf5wIYVsgpgbAezgw8cbl_YqnW",
            "https://drive.google.com/uc?export=view&id=19ex0V-LpZvL6tvuud44sk0KonUYIJHgx",
            "https://drive.google.com/uc?export=view&id=1pLC5MFEFrPE5e5CsF80-IZCve2FrSY3P",
            "https://drive.google.com/uc?export=view&id=1DY1yIo9syJZ_11x3cmUb3UEXlz3rGnmf",
            "https://drive.google.com/uc?export=view&id=1t598cBXf4CZUV9ZN4b-KRnXYIUbaKWVD",
            "https://drive.google.com/uc?export=view&id=1VvpQJj4Su3kIBITvok7-O15YjfJhvi19",
            "https://drive.google.com/uc?export=view&id=11g7M_OwBe7cPEhUOMO7BDjs9x77G3SKQ",
            "https://drive.google.com/uc?export=view&id=1i2XTBdN1nc5s4hOkw53LvDo2KxGimVK1",
            "https://drive.google.com/uc?export=view&id=1HEyFwggNiMxCRC02ypwyqt2Iml9ILYk1",
            "https://drive.google.com/uc?export=view&id=1taDtME03l8RIHMotSwZ9XZ2swCVbK_Cl",
            "https://drive.google.com/uc?export=view&id=1LwpI7brKgmJhxzTSLXx4X5mnun6EH15B",
            "https://drive.google.com/uc?export=view&id=1PwrfKCBJ68-x9JJ7F6gQ_ea_opJoxntl",
            "https://drive.google.com/uc?export=view&id=1CWDDSGnTWlvt5VZpGIaaoOMe4-zLKX0H",
            "https://drive.google.com/uc?export=view&id=1r-dzB2KREY6ZG_g2EGHs3wYhqrBF9zHn",
            "https://drive.google.com/uc?export=view&id=1r-dzB2KREY6ZG_g2EGHs3wYhqrBF9zHn",
            "https://drive.google.com/uc?export=view&id=19gC_4VDrJA8ne_NeqPBOvfxDzdtX3B5m",
            "https://drive.google.com/uc?export=view&id=15U8JhEyurtQNZiFOsW4Dm6fGgB-9dc1s"
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kakaknya baik, ramah, asik juga",
                "pesan": "Semoga sehat selalu kak, semangat terus juga"
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakaknya asik, baik, seru",
                "pesan": "Sehat selalu kak, semoga skripsinya lancar"
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Jakarta Utara, Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Buka Tutup Laptop",
                "sosmed": "@noerruuu",
                "kesan": "Abangnya baik, ramah",
                "pesan": "Semoga sehat terus kak"
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Ballet",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakaknya baik, ramah, asik juga",
                "pesan": "Semoga sehat selalu kak, semangat kak"
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing emosi",
                "sosmed": "felisyanbl",
                "kesan": "Kakanya baik dan ramah",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Dukung silver arrow alias mercedes",
                "sosmed": "@muh_razan_",
                "kesan": "Abangnya baik, ramah",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "17",
                "asal": "Bali",
                "alamat": "Airan",
                "hobbi": "Nongkrong depan prodi",
                "sosmed": "saniayyllstr",
                "kesan": "Kakaknya ramah dan asik",
                "pesan": "Semoga kuliahnya lancar bang"
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "3 Tahun",
                "asal": "Surga",
                "alamat": "Rumah Asha",
                "hobbi": "Ice skating",
                "sosmed": "@aallishaa.aa",
                "kesan": "Kakaknya ramah dan asik",
                "pesan": "Semoga sukses terus kak"
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Mengkoding",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semoga sukses terus kak"
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "7.137 hari per hari ini",
                "asal": "Sumsel",
                "alamat": "Kafe Kali",
                "hobbi": "Bobo cantik",
                "sosmed": "@difanyhsa",
                "kesan": "Kakaknya ramah dan asik",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mimpi diatas kasur",
                "sosmed": "nzlhauly_",
                "kesan": "Kakaknya baik dan asik",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "n1tg._",
                "kesan": "Kakaknya kalem dan ramah",
                "pesan": "Semoga sukses terus kak"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "",
                "sosmed": "@daffascript_",
                "kesan": "Abangnya asik dan ramah",
                "pesan": "Semoga dimudahkan urusannya bang"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scrolling Fesbuk",
                "sosmed": "@eddel_0712",
                "kesan": "Kakaknya kalem dan ramah",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nonton Star Wars",
                "sosmed": "luciarachel_",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "Sehat terus, semangat terus kak"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Pemda",
                "hobbi": "Ngoding",
                "sosmed": "@_shaazzh",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semoga semngat dan sehat terus kak"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Unila",
                "hobbi": "Tidur",
                "sosmed": "@xifasky",
                "kesan": "Kakaknya kalem dan ramah",
                "pesan": "Semoga sehat selalu kak"
            }
        ]

        display_images_with_data(gambar_urls, data_list)

    medkraf()

elif menu == "Departemen Eksternal":
    def Eksternal():
        gambar_urls = [
                "https://drive.google.com/uc?export=view&id=1QiqZB4unjCTaQQ2MJEXZ9IlEiY8FZhHe",
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "https://drive.google.com/uc?export=view&id=1kvB5Y15DgL_piXzKdyyMdavFTa8PjHyT",
                "https://drive.google.com/uc?export=view&id=1fDt0AVKuws1bX0aq3EjTViSJl-KNk3-3",
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "https://drive.google.com/uc?export=view&id=1GsWcpy3pFqvIAweAorIdhAlQmuIWYlb2",
                "https://drive.google.com/uc?export=view&id=1uA_MWaO4Dd20poeZBmAYzQaxZnTZsctT",
                "https://drive.google.com/uc?export=view&id=1cTDipX2un6rJwtJ6UhvPZ8UKKaSjRuN7",
                "https://drive.google.com/uc?export=view&id=1-RMw7N6B4m4L_2FxJwb7x45yXxBTWkRU",
                "https://drive.google.com/uc?export=view&id=1RzL_cPrp1Tf7RxjvjZzmP4QBqv8OCD_W",
                "https://drive.google.com/uc?export=view&id=1mgLbAq6GyPoK1evyklNOeih0m1H98sDv",
                "https://drive.google.com/uc?export=view&id=1t-wRSQCTmqDpDIpxQ-roTbGaKnWUnR2F",
                "https://drive.google.com/uc?export=view&id=1Jvd5Z0jjnASFpqcaVlNx-DE-Mi9S2Tmv",
                "https://drive.google.com/uc?export=view&id=1prDRFj1Czovg9zbMXjphq140BUQ-KSm9",  
                "https://drive.google.com/uc?export=view&id=1q8ZhxJftYNZU-FybbsXeosCJQuBJcMgb",
                "https://drive.google.com/uc?export=view&id=1plbA6d6tuBFcp-flWVWU37wrMMLidynn",
                "https://drive.google.com/uc?export=view&id=1-H069BupSRHrIAw95zbvSKFmXn1zjWOO",
                "https://drive.google.com/uc?export=view&id=1GxR4IO7lZM3YkM-w3IFLfoIZEQlBBR9-",
                "https://drive.google.com/uc?export=view&id=1HGIXb0PMEJTX_-9ttJmwtk-UKIOq0gex",
                "https://drive.google.com/uc?export=view&id=1UyydyJuAmjFOcs6ogBqw6XL0V3YxXnzo",
                "https://drive.google.com/uc?export=view&id=1luE3tlx8PSIuzcuD5GWrx7F2VoGAVZqr"
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
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan-Jalan",
                "sosmed": "@bylaash",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Khoirul",
                "nim": "1234500",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "20",
                "asal": "Ikut kadep",
                "alamat": "Love earth",
                "hobbi": "Jadi idol cepuyuh tayun",
                "sosmed": "@adindaadma",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "Baca Wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "666 Pohon Mulia",
                "hobbi": "Nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "-",
                "asal": "Balam balam",
                "alamat": "Nelson Piquet",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "Tanyain sama yuder (beneran ditanya ya)",
                "sosmed": "@jaldii._",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton Thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "",
                "pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Eksternal()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Gy2U3xSmi2m1VZx9wqODGE6GcpWk9C4q",
            "https://drive.google.com/uc?export=view&id=1Qzl6CWj1rZM3RKMvjISN92kirnzeV9IZ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1x4MGiM80Xs1FWVO0ezWBYdipzmphQKdR",
            "https://drive.google.com/uc?export=view&id=1ZSiBh-VENDlJ-yEEPQpWDRo30gPzubKu",
            "https://drive.google.com/uc?export=view&id=1lt6S0EhGXo3v2YIV-C1lNbC4DB5TOlAj",
            "https://drive.google.com/uc?export=view&id=1ejsc2cq_eYdaJqDtVnq7OvMeO-JhKIkg",
            "https://drive.google.com/uc?export=view&id=1D-7DZ8CKqkNoxo65Z1jWS7eqmhdu5ciI",
            "https://drive.google.com/uc?export=view&id=1Gb_HQpthLbe8AQhA1W6UewelJjaaBEUN",
            "https://drive.google.com/uc?export=view&id=1mQaIKh07t5edHNE8n-PEO_h1yR2vlyP3",
            "https://drive.google.com/uc?export=view&id=1WvZF7zxS8rZHhwSZd8bS4j5DTgXonapM",
            "https://drive.google.com/uc?export=view&id=1DOYg7m5xOyqudpP3KFoU8lksM162n72a",
            "https://drive.google.com/uc?export=view&id=1iC34WkgPb5lxOMWrgyqvjuhzkmhuaP6I",
            "https://drive.google.com/uc?export=view&id=1QQGmegvyguzGoZIGW45OonxgmVvRlpVS",
            "https://drive.google.com/uc?export=view&id=1DtDKJYfOAbxJCJ3FJfvonG5yV_C6RnQy",
            "https://drive.google.com/uc?export=view&id=1AYUN5UYLlpkKlCCTsWB1SOcHX6v8Xg5n",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=11PiI2LUkfPXw87HlPlklEv6VLxO79ixj",
            "https://drive.google.com/uc?export=view&id=1rEuS7OfVs4AN17Ul39D5ZT7YjOU__krh",
            "https://drive.google.com/uc?export=view&id=1UajqpnzaAorXXqieBzA7pvb3LchSgg38",
            "https://drive.google.com/uc?export=view&id=1k50OYo8ie2nBDxSoKaLDcOhpit0Gvwxc",
            "https://drive.google.com/uc?export=view&id=14dO2vQWV31yj4VlrO3AvATajzoDh_Fne",    
        ]

        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "124450104",
                "umur": "21",
                "asal": "Balam",
                "alamat": "-5.386541,105.262255",
                "hobbi": "Nyapu wico lantai 2, lantai 3, lantai 4, lantai 5 gedung F",
                "sosmed": "@biyokcb",
                "kesan": "Kece abangnya, kalau jadi pemateri asik, mirip mamasku di kampung",
                "pesan": "Sehat selalu bang, semoga skripsinya lancar, terus jadi sukses"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@tvnty_",
                "kesan": "Kakaknya lucu, asik, baik juga",
                "pesan": "Semoga kuliahnya gampang kak"
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Abangnya keren, hebat juga",
                "pesan": "Rest in Peace bang"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis",
                "hobbi": "Tenis meja",
                "sosmed": "@manuelfdk_",
                "kesan": "Baik abangnya, keren juga",
                "pesan": "Sukses lalu bang"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "17",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@violaadrtr_",
                "kesan": "Kakaknya baik sama ramah",
                "pesan": "Semoga sehat selalu kak, dimudahkan urusannya"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling skate",
                "sosmed": "risarmdna",
                "kesan": "Kakaknya baik",
                "pesan": "Semoga kuliahnya dimudahkan kak"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Teluk Betung",
                "hobbi": "Nonton film action Tom Cruise, Liam Neeson, Jackie Chan",
                "sosmed": "@vunnycaa",
                "kesan": "Kakaknya asik, baik juga",
                "pesan": "Semoga gampang urusan kuliahnya kak"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124540119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Main alat musik",
                "sosmed": "krnylee",
                "kesan": "Kakaknya baik, ramah juga",
                "pesan": "Smeoga disehatkan terus kak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya keren",
                "pesan": "Semoga sehat terus bang"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "Kakaknya asik, dulu satu kosan sama irfan",
                "pesan": "Semoga sehat terus kak"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main ML",
                "sosmed": "fadyaizzatul_",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semoga urusan kuliahnya dimudahkan kak"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@from_loviaa",
                "kesan": "Kakaknya baik",
                "pesan": "Sehat terus ya kak"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Kotabaru",
                "hobbi": "Main game, tidur, dengerin musik",
                "sosmed": "aruccy_",
                "kesan": "Abang NIMku, baik abangnya",
                "pesan": ""
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Menunda Pekerjaan",
                "sosmed": "sher_renna",
                "kesan": "Kakaknya cantik kata zaki, kakak NIMnya soalnya",
                "pesan": "Sehat terus kak semoga kuliahnya gampang"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya asik, jadi pemateri juga",
                "pesan": ""
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Belajar",
                "sosmed": "faizaanjanii",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Gathfan Nadhif Ali",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@gathfannad",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, LamTim",
                "hobbi": "Ngoding & Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumsel",
                "alamat": "Sukarame",
                "hobbi": "Nari",
                "sosmed": "@melva_fbrt",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Stafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syaafiqui",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "2000",
                "asal": "Kota Bumi",
                "alamat": "Rajabasa",
                "hobbi": "Nongkrong",
                "sosmed": "henryferdianto",
                "kesan": "",
                "pesan": ""
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    mikfes()

elif menu == "Departemen Internal":
    def Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BnPnJsqBmF9TmVOBtln5_zx47BQ285XL",
            "https://drive.google.com/uc?export=view&id=1-3CJYs4zF_PJjH0-C9j9Xob8A9K-rgLv",
            "https://drive.google.com/uc?export=view&id=19N6wSefPX0zonYO4j-0CCtA-Qd9QDOfS",
            "https://drive.google.com/uc?export=view&id=1d4m5lQyJl1CAHwIRUxjHr2CO_ibUDZsL",
            "https://drive.google.com/uc?export=view&id=14tTdWQOPhrxRDesjRf46fqd2X2e-6a59",
            "https://drive.google.com/uc?export=view&id=1b0GlRx0B6KnA3NiwxANQHi6Jzk5MMRIt",
            "https://drive.google.com/uc?export=view&id=1cQ-0ibO9N0x-N5qTgEDwRkN40-GNir8D",
            "https://drive.google.com/uc?export=view&id=1lFIGUhjSCOZK-o8Kz1SUys5q--9gsDXZ",
            "https://drive.google.com/uc?export=view&id=1QSWDEabNuu1iH_XgX45sfNMbNQPscjAQ",
            "https://drive.google.com/uc?export=view&id=1pomZ4l0H4Kw2oavDE2Q0cY8uZ-VsopPd",
            "https://drive.google.com/uc?export=view&id=1fJlKDOil5a117hWiTFcoms8c0KKwgoSI",
            "https://drive.google.com/uc?export=view&id=1IsVUaOMZG8H7Hj6dAJdQxFaD_rr8uN29",
            "https://drive.google.com/uc?export=view&id=1hpFA_6PubgDlYwoRGJe_AG4S33HnABnw",
            "https://drive.google.com/uc?export=view&id=1jNDL7xxWAA9m54aIDKw4JqZ4xsrfL4kz",
            "https://drive.google.com/uc?export=view&id=1T4gfq4BqNmuPG771VMZozpLDbKNma9u6",
            "https://drive.google.com/uc?export=view&id=1euqNJ0S4GVsCkGU9uXiFxl_ShC_OMr5w"
        ]
        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "20",
                "asal": "Tangerang Kota",
                "alamat": "Gerbang Barat",
                "hobbi": "Begadang",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang ini asik diajak ngobrol, baik juga",
                "pesan": "semangat abang, sehat selalu"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "Untung Suropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakaknya ramah dan baik",
                "pesan": "semangat terus kuliahnya kakak, semangat skripsi"
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Kisaran",
                "alamat": "Sukarame",
                "hobbi": "Membaca Novel",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "semangat terus kuliahnya kakak semangat skripsi"
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "nim": "123450067",
                "umur": "22",
                "asal": "Tetangga Singapore",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya asik dan seru",
                "pesan": "semangat terus kuliahnya abang"
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Indragirihulu",
                "alamat": "Samping Kuburan",
                "hobbi": "Sleep Call",
                "sosmed": "@aisyahkhair._",
                "kesan": "kakaknya asik dan ramah",
                "pesan": "semangat kakak, sehat selalu"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Semarang",
                "alamat": "Belwis",
                "hobbi": "Manjat pohon kelapa",
                "sosmed": "@cerine_ipynb",
                "kesan": "kakaknya ramah dan baik",
                "pesan": "semangat terus kuliahnya kakak"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "21",
                "asal": "Kisaran",
                "alamat": "Pemda",
                "hobbi": "Main Biola",
                "sosmed": "@jay.saputra.tmb",
                "kesan": "abangnya asik, seru orangnya",
                "pesan": "semangat terus kuliahnya bang semangat menugas"
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Nonton asmr",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "semangat terus kuliahnya kakak"
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "19",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Badminton",
                "sosmed": "@rozakramdani_",
                "kesan": "Abangnya ramah dan baik",
                "pesan": "semoga sehat selalu abang"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Memasak",
                "sosmed": "@christiani8872",
                "kesan": "kakaknya baik, seru orangnya",
                "pesan": "semoga selalu dikelilingi orang baik"
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "",
                "asal": "Padang",
                "alamat": "Way Kandis",
                "hobbi": "Nonton MU",
                "sosmed": "@hnfdzky_",
                "kesan": "Abangnya ramah dan asik",
                "pesan": "semoga sehat selalu bang"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "semangat terus kuliahnya kakak"
            },
            {
                "nama": "Cika Adelia BR Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Samping Kuburan",
                "hobbi": "Scroll tiktok",
                "sosmed": "@cikambrn",
                "kesan": "Kakaknya ramah dan baik",
                "pesan": "Jaga kesehatan kakak, semoga bahagia selalu"
            },
            {
                "nama": "Gustin H Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "kakaknya ramah dan baik",
                "pesan": "semoga selalu dikelilingi orang baik"
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Nangkap lele",
                "sosmed": "@muhvinz_",
                "kesan": "Abangnya ramah dan asik",
                "pesan": "semoga sehat selalu bang"
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Main game di HP temen",
                "sosmed": "@muhvinz_",
                "kesan": "Kakaknya baik dan asik",
                "pesan": "semoga sehat selalu bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    Internal()
# Tambahkan menu lainnya sesuai kebutuhan