import streamlit as st
from streamlit_option_menu import option_menu
import requests
import re
from PIL import Image, ImageOps
from io import BytesIO

st.set_page_config(page_title="Buku Kating", layout="wide")

st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Badan Legislatif",
            "Badan Kesenatoran",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
            "Departemen Minbak"
        ],
        icons=["people-fill"] * 10,
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
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

def get_direct_image_url(url):
    """Mengubah link berbagi Google Drive menjadi URL unduhan langsung."""
    match = re.search(r"/file/d/([^/?]+)", url)
    if match:
        file_id = match.group(1)
        return f"https://drive.google.com/uc?export=download&id={file_id}"

    match = re.search(r"[?&]id=([^&]+)", url)
    if "drive.google.com" in url and match:
        file_id = match.group(1)
        return f"https://drive.google.com/uc?export=download&id={file_id}"

    return url

def load_image(url):
    """Mengambil dan memvalidasi gambar sebelum ditampilkan."""
    direct_url = get_direct_image_url(url)
    try:
        response = requests.get(
            direct_url,
            timeout=15,
            allow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        image = ImageOps.exif_transpose(image).convert("RGB")
        image.thumbnail((600, 800))
        return image
    except Exception:
        return None

def display_images_with_data(gambar_urls, data_list):
    """Menampilkan setiap data orang dengan gambar yang sesuai secara berurutan."""
    for idx, orang in enumerate(data_list):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            if idx < len(gambar_urls):
                img = load_image(gambar_urls[idx])
                if img is not None:
                    st.image(img, use_container_width=True)
                else:
                    st.info(f"Gambar {orang.get('nama', '')} tidak dapat dimuat. Pastikan akses Google Drive diatur ke 'Public'.")
            else:
                st.info("URL gambar belum ditambahkan.")

        st.write(f"**Nama:** {orang.get('nama', '-')}")
        st.write(f"**NIM:** {orang.get('nim', '-')}")
        st.write(f"**Umur:** {orang.get('umur', '-')}")
        st.write(f"**Asal:** {orang.get('asal', '-')}")
        st.write(f"**Alamat:** {orang.get('alamat', '-')}")
        st.write(f"**Hobi:** {orang.get('hobbi', '-')}")
        st.write(f"**Sosial Media:** {orang.get('sosmed', '-')}")

        if "divisi" in orang and orang["divisi"]:
            st.write(f"**Divisi:** {orang['divisi']}")

        st.write(f"**Kesan:** {orang.get('kesan', '-')}")
        st.write(f"**Pesan:** {orang.get('pesan', '-')}")
        st.divider()

    st.success("Selesai memproses daftar anggota.")

menu = streamlit_menu()

# --- 1. KESEKJENAN ---
if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1RPRXY1_sjMuAcDhD0A46aDYlfkQ2CnXW",
        "https://drive.google.com/uc?export=view&id=1jdVwET2zp7CHeChA-vVKx9gtzMfUdivU",
        "https://drive.google.com/uc?export=view&id=1fuD4xooOTLVZdFMz7hiojychS2CrjbGQ",
        "https://drive.google.com/uc?export=view&id=1xi8ilNCyKhE5IACbKCcjI2XC7mxcGpjU",
        "https://drive.google.com/uc?export=view&id=1wiWYI_oP_P6Ih95sQ1ANvnG9lfnLA448",
        "https://drive.google.com/uc?export=view&id=1-6X5KDbE1W1WC8jKiNFuWCByUKE_Il48"
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Sekretariat HMSD", "hobbi": "Push Rank sampe IMO", "sosmed": "@jars_mrp", "kesan": "Keren dan berwibawa, keren banget manage waktunya", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Muhammad Aqil Ramadhan", "nim": "123450046", "umur": "22", "asal": "Bangkinang", "alamat": "Sekretariat HMSD", "hobbi": "Dzikir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya chill bangett, dan memperoleh banyak ilmu dari sekjen", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Efi Defiyati", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakak ini asik saya suka belajar dengan dia", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Qois Olifio", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin Surat", "sosmed": "@qoisolifio_", "kesan": "Kakak ini asik saya suka belajar dengan dia", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Hafsa Fazila Arradhi", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Berenang", "sosmed": "@hafsafazilaa", "kesan": "Kakaknya seruuuu", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Luthfia Laila Ramadhani", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Bertemu Pak Tirta", "sosmed": "@luthfiaarmdhni", "kesan": "Lucuuu kakanya, dan insight how to survive every semesternya sangat menarikk", "pesan": "semangat terus kuliahnya kakak !!!"}
    ]
    display_images_with_data(gambar_urls, data_list)

# --- 2. BADAN LEGISLATIF ---
elif menu == "Badan Legislatif":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1f54XEKLV5-_iY0Ke1Amy_8n2lsuTpWrB",
        "https://drive.google.com/uc?export=view&id=1Npve-crpQRsbSWWEiarHjDlkXz2v5uMy",
        "https://drive.google.com/uc?export=view&id=1SXlqNcP7PFbzx62UCp6dmh7LCh0or6Ul",
        "https://drive.google.com/uc?export=view&id=1NFnxXH1iKWic5Mp4dbGtTP9Xx4DC68Xh",
        "https://drive.google.com/uc?export=view&id=1C7TLf81OCP5CfwY7wy6O25kc616G6IjH",
        "https://drive.google.com/uc?export=view&id=17dBnXowQY4puKAesvwkom0NmHYtjQOFS",
        "https://drive.google.com/uc?export=view&id=15DoGub_MvMZN1CO6gb_8hOv6lGIgPvu6",
        "https://drive.google.com/uc?export=view&id=1h_syNDUTRwE9yEntGLAMWhtP1A36c5ga",
        "https://drive.google.com/uc?export=view&id=1UvXJs9C6bqp_N9_2Bak2VJxgRj5SrtY8",
        "https://drive.google.com/uc?export=view&id=1MkYZ6i_A643S8bgQmQ8534gt8A5qpvi9",
        "https://drive.google.com/uc?export=view&id=1VLxmWTsL2RbVgRgKKn_WZ0u0lhHyCpMf",
        "https://drive.google.com/uc?export=view&id=1MLgWgxGJy7rWdIox6yUiJ9dgKbpnpkPW",
        "https://drive.google.com/uc?export=view&id=1_ze0SXyd0BWT4qSr5q3RF1DLeARrWyAV"
    ]
    data_list = [
        {"nama": "Ridho Benedictus Togi Manik", "nim": "123450060", "umur": "20", "asal": "Kota Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@iamridhomanik", "kesan": "SERU BANGETTT!!! abangnya beneran lucu terus celetukannya, beneran pabrik jargon hahaha", "pesan": "Semangat bang TA nyaa, semoga dilancarkan semuanya dan lulus tepat waktu ya bangg. Anak magang baleg selalu mendoakan yang terbaik untuk ayah dido"},
        {"nama": "Juesi Apridelia Saragih", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim dari marsel", "sosmed": "@j__eesie", "kesan": "GEMASSSSS! beneran imut kakanya dan seru banget dengerin storytelling ka juee, karena kayak sivia the catchup club cara kaka ngomong", "pesan": "Semangatt terus kak kuliah dan TA nya, semoga dimudahkan segala urusannya yaa, aamiin"},
        {"nama": "Dharu Cahyoaji Sasongko", "nim": "123450023", "umur": "19", "asal": "Lampung", "alamat": "Bandar Lampung", "hobbi": "Ngidupin api baleg di tiktok", "sosmed": "@exvoltas", "kesan": "Pinter bnaget abangg, tips and trik mapres bangg", "pesan": "Semangat kuliah dan TA nya, semoga dimudahkan seluruh urusannya, aamiin!"},
        {"nama": "Gh. Mikael Niko Antoni Setiadi", "nim": "124450025", "umur": "20", "asal": "Jabung", "alamat": "Jati Agung", "hobbi": "COD Musang", "sosmed": "@me._kael", "kesan": "Lucu banget jokes jokes abangnyaa", "pesan": "Semangat terus kuliah dan organisasinya!"},
        {"nama": "Siti Sarifah Sumamah", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "Imutt sekali kakanyaaa", "pesan": "Semangattt kaa kuliahnyaa, kaka imut balegg"},
        {"nama": "Givaro Ananta", "nim": "123450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum Kopi", "sosmed": "@givarooo", "kesan": "Bang gip chill banget orangnyaa dan seruu", "pesan": "Semangat terus bang kuliahnya dan semoga dimudahkan TA nya ya banggg, Aamiin!"},
        {"nama": "Afghanis Nursholehatunnisa", "nim": "124450042", "umur": "19", "asal": "Kepulauan Mentawai", "alamat": "Owen Kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "Public speakingnya bagus, aku dukung kaka jadi the next kadiv komisi 2 #YIPPIE", "pesan": "Semangat kaa kuliah dan organisasinyaa!!"},
        {"nama": "Hani Qurrota Aini", "nim": "124450020", "umur": "20", "asal": "CTR", "alamat": "Sukarame", "hobbi": "Baca AU", "sosmed": "@haniquratuain_", "kesan": "Lucu dan gemas bangettt", "pesan": "Semangat ka menghadapi bang Ridhoo, semoga dilancarkan semua urusannya kaaa!"},
        {"nama": "Jeremia Halim", "nim": "124450101", "umur": "20", "asal": "Tanggerang", "alamat": "Teluk", "hobbi": "Nyanyi, olahraga", "sosmed": "@jeremia_hm", "kesan": "Keren dan berwibawa", "pesan": "Semangat bang kuliahnyaaa!"},
        {"nama": "Monica Patricia Tanjung", "nim": "123450073", "umur": "21", "asal": "Jakarta Barat", "alamat": "Kotabaru", "hobbi": "Lari", "sosmed": "@monica_tjg", "kesan": "Lucu, gemas, tapi tegas", "pesan": "Semangat kaa kuliah dan organisasinyaaa!"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "nim": "124450111", "umur": "20", "asal": "Depok", "alamat": "Pemda Raya", "hobbi": "Gym sama Koleksi figure, nafas manual", "sosmed": "@nagatseee", "kesan": "Lucu abangnya, jokes jokesnya juga fresh", "pesan": "Semangat abang kuliah dan organisasinyaa!"},
        {"nama": "Sekar Dini Widya Putri", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "Tegas tapi chill juga", "pesan": "Semangat terus ka kuliah dan organisasinyaa!"},
        {"nama": "Wan Nashwa Alhasni Yuska", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nshaysk", "kesan": "Lemah lembut sekaliii", "pesan": "Semangat kaa TA dan kuliahnyaa!"}
    ]
    display_images_with_data(gambar_urls, data_list)

# --- 3. BADAN KESENATORAN ---
elif menu == "Badan Kesenatoran":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1DB2rHAmkffUqkrya8F8oZcQ5ky-E7IpU",
        "https://drive.google.com/uc?export=view&id=1A9TvLPFQtnaq0BzwKE6JVH1XeyX7bgp-",
        "https://drive.google.com/uc?export=view&id=1OJ7DriS--Ewwl3ZyG0xt4sMTC5quS4r-",
        "https://drive.google.com/uc?export=view&id=1Tybx2D5I_98OnxxCWinZnjk0b8-CO7S5",
        "https://drive.google.com/uc?export=view&id=1eoPRNOiqrHN13VNiao9jjQ0IuEqrIguS",
        "https://drive.google.com/uc?export=view&id=1LNwmAbHuLnCXLpEq8wxWNh40Sz-rLBCA",
        "https://drive.google.com/uc?export=view&id=1CI2P4dAFMDPRsrYErYKJPZP330WA3ORF",
        "https://drive.google.com/uc?export=view&id=1qOmHUqzqldal4GPoOGrFKMXIgXoU_yEm",
        "https://drive.google.com/uc?export=view&id=1dlDTw7hOo-XTSc1X94HK97YtOcmFutm5",
        "https://drive.google.com/uc?export=view&id=1sLE-dVR8G7XK4_y3fAEeF4QfK2BydGKT"
    ]
    data_list = [
        {"nama": "Fathinah Nur Azizah", "nim": "123450072", "umur": "21", "asal": "Jakarta Timur", "alamat": "Airan", "hobbi": "Nulis Medium", "sosmed": "@fathinahnaazh", "kesan": "Inspired girl, beneran keren bangettttt", "pesan": "Semangat terus kak kuliahnya!"},
        {"nama": "Helmy Surya Pratama", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Kedamaian", "hobbi": "Ngesen kiri", "sosmed": "@helmy_ist", "kesan": "Duta melet, lucuuuu", "pesan": "Semangat terus kuliahnya kak!"},
        {"nama": "Fernando Dimetrius Barus", "nim": "124450063", "umur": "21", "asal": "Tangerang", "alamat": "Sebelah kamar biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Chill banget kakanyaa", "pesan": "Semanagat terus bang kuliahnya!"},
        {"nama": "Suci Aulia", "nim": "124450034", "umur": "19", "asal": "Krui", "alamat": "Kota Baru", "hobbi": "Bikin video random dan upload di second", "sosmed": "@sciia_staff", "kesan": "Sumpah style baju kakanya keren kerennn", "pesan": "Semangat terus kak kuliahnya!"},
        {"nama": "Wielman Itolo Halawa", "nim": "124450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB3", "hobbi": "Mancing", "sosmed": "@wielhawny", "kesan": "Welcome sekali abangnya, apapun pose yang diminta beneran diiyain #GEMAS", "pesan": "Semangat terus bang kuliahnya!"},
        {"nama": "Lia Hana Ichisasmita", "nim": "123450089", "umur": "21", "asal": "Jakarta Timur", "alamat": "Belwis", "hobbi": "Nyari jurnal", "sosmed": "@lia.h_264", "kesan": "Banyak ilmu mengenai Strategis dan Propaganda yg aku peroleh dari kakaaa", "pesan": "Semangat kak TA nyaa, semoga dimudahkan jalannya yaa!!"},
        {"nama": "Aqila Zayyan Salsabil", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan bayyesian", "sosmed": "@aqilazayyaan", "kesan": "Modis dan keren banget style stylenyaa, dan imup bangett", "pesan": "Semangat terus kuliahnya kaa!"},
        {"nama": "Hazel Mahesa Handhaka", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Ujung Terang", "hobbi": "Bulu Tangkis", "sosmed": "@hazelhandhaka", "kesan": "kece euyyy, style abang beneran keren bangett", "pesan": "Semangat terus bang kuliah dan organisasinya!"},
        {"nama": "Nadya Ratu Anjani", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Denger Lagu", "sosmed": "@nadyaanjaani", "kesan": "Welcome sekali kakanyaaa, dan cara penyampaian materinya juga mudah dipahami", "pesan": "Semangat terus kuliahnya kaa!!"},
        {"nama": "Dwi Rahma Fitriani", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas Belwis", "hobbi": "Dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Gemass kakanyaa", "pesan": "Semangat terus kaa kuliahnyaa!!"}
    ]
    display_images_with_data(gambar_urls, data_list)

# --- 4. DEPARTEMEN PSDA ---
elif menu == "Departemen PSDA":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=153egJP5i9qz2r7v2CKyXgsdi-UlttKIF",
        "https://drive.google.com/uc?export=view&id=1NXugTSOY-v_BtWkdKdohyXlsNxd8kCf9",
        "https://drive.google.com/uc?export=view&id=1OBBZKNv4psX_BOu0N4UIop3WBtu2WYXQ",
        "https://drive.google.com/uc?export=view&id=19nT5Io7fK6aJdvYuy_9Z1yP11znF9jCb",
        "https://drive.google.com/uc?export=view&id=1m5pMnXkV4Bpi_OyFS9E6sJKbrwmH_bty",
        "https://drive.google.com/uc?export=view&id=1rXtWe6248SSP-i9hweUM_nX19Dq88TTg",
        "https://drive.google.com/uc?export=view&id=1UHCxZ-14Caq8duvc_dR1gl37ftwMlR6I",
        "https://drive.google.com/uc?export=view&id=1oiK6KPStWdR5aWjgglM4sO9baYMsSOyj",
        "https://drive.google.com/uc?export=view&id=182mgFTgY4NAWYGRgee3jPD0E03WrCILf",
        "https://drive.google.com/uc?export=view&id=1KGrumBz2cAsB1guZPgROqOqQ8fDqRHnV",
        "https://drive.google.com/uc?export=view&id=1wjiuj_258DE8sx3970aXBjVZjAHlIVJH",
        "https://drive.google.com/uc?export=view&id=1ZouY_InyWDJVSLHgqrputpUtrZ7ifed2",
        "https://drive.google.com/uc?export=view&id=12xpJFu_Ke2EeNVlfE6RIEpaIp6eo5rXD",
        "https://drive.google.com/uc?export=view&id=19i5eLiyk7slfw10Gaje9xA7wDtphVo2B",
        "https://drive.google.com/uc?export=view&id=1p1t4oMSSYDKisRnS-wYDXe63qK62d0VQ",
        "https://drive.google.com/uc?export=view&id=1RBRpOUeX2nDd-BhrkvioRqMonxjAcpBX",
        "https://drive.google.com/uc?export=view&id=105MFnanA0MFLcvjA8FHPo8mbQEgnNhpp"
    ]
    data_list = [
        {"nama": "Arienta Khusnul Ananda", "nim": "123450097", "umur": "21", "asal": "Dekat Pantai Kedu, Kalianda", "alamat": "Samping kos capo", "hobbi": "Baca jurnal", "sosmed": "@arientakhsnl_", "kesan": "Cantik dan fashionable", "pesan": "Semangat TA nya kaa, semoga diberi kemudahan dan dilancarkan semua urusannyaa"},
        {"nama": "Vany Salsabila Putri", "nim": "123450022", "umur": "20", "asal": "Sibolga", "alamat": "Pudan Kost", "hobbi": "Pacaran", "sosmed": "@vany.salsabilaa", "kesan": "Orangnya tegas", "pesan": "Semangattt kaa untuk TA nyaa, jangan lupa jaga kesehatan ya kaa!"},
        {"nama": "Nobel Nizam Fathirizki", "nim": "123450117", "umur": "21", "asal": "Bandar Lampung", "alamat": "Urip", "hobbi": "Banyak", "sosmed": "@nobelnizam", "kesan": "Abang kalau ga marah beneran lebih berkharisma, btw materi kader yang disampaikan abang beneran ilmu daging", "pesan": "Semoga abang selalu dilingkupi oleh banyak kebaikan yaa, dan semangat nanti TA nyaa!"},
        {"nama": "Afriza Azmi", "nim": "124450110", "umur": "20", "asal": "Malang", "alamat": "Samping kos Jemar", "hobbi": "Berantem", "sosmed": "@friezazmi", "kesan": "aduhai abang nim ku timder, jujur kaget ga ekspek para abang nim ku orang-orang penting #PRESSURE", "pesan": "Jangan marah-marah mulu bang, btw sukses buat selanjutnya #salampaguyuban110"},
        {"nama": "Ayake Alfatih Ramadan", "nim": "124450108", "umur": "21", "asal": "Peninjauan, 10 kota di atas, Solok, Sumatera Barat", "alamat": "Blok D 79, Jl Manggis 8 Perum Pemda, Way Huwi Jati Agung, Lampung Selatan, Lampung", "hobbi": "Masak ayam", "sosmed": "@ykeall", "kesan": "Galak tapi kadang baik", "pesan": "Jaga kesehatan bang, kontrol emosinya biar ga jadi penyakit"},
        {"nama": "Caesar Ozora Alrando", "nim": "124450017", "umur": "21", "asal": "Painar, Sumatera Barat", "alamat": "Gedung F", "hobbi": "Mandiin anak ayam", "sosmed": "@caesar.oriza", "kesan": "Kadang galak banget, kadang galak aja", "pesan": "Jaga pola pikir bang, jangan stress-stress"},
        {"nama": "Euodia Meiliana Friedita", "nim": "124450029", "umur": "18", "asal": "Debu Tanah", "alamat": "Di sebelah pasar, di bawah turunan, di atas tanjakan, di seberang kontrakan Yazid Rizal", "hobbi": "Ngegiring anak ayam bermain di Lapangan", "sosmed": "@yudiameilianaa_", "kesan": "Ramah kalau ga marah", "pesan": "Semangat kuliahnyaa, walaupun semakin bertambah semester semakin bikin ga semangat #CRI, oh iya sama kaa kalau kaka lagi stress jangan dialihin emosinya ke orang lain ya.."},
        {"nama": "Haikal Seventino Tamba", "nim": "124450012", "umur": "18", "asal": "Rantau Perapat", "alamat": "Belakang kos Ayake", "hobbi": "Goreng ayam", "sosmed": "@_haikaaall", "kesan": "Ini anak 24 emang suka ayam ya?", "pesan": "Semangatt bang kuliahnya, semoga kebaikan selalu melingkupi abang"},
        {"nama": "Putri Manna Anantama Simbolon", "nim": "124450056", "umur": "18", "asal": "Sabang", "alamat": "Nomaden", "hobbi": "Duduk samping Henry", "sosmed": "@putrimannaa", "kesan": "Omelan kaka hinggap di mimpi saya sampe 3 hari", "pesan": "Ga ekspek ternyata di luar 'itu' kaka ternyata ramah, saya kira memang pemarah"},
        {"nama": "Queenta Thifaal Nabila", "nim": "124450059", "umur": "18", "asal": "Kota Gajah", "alamat": "Depan pemancingan", "hobbi": "Nyuapin anak ayam", "sosmed": "@queentanabila", "kesan": "Kakanya soft spoken kalau ga marah", "pesan": "Jaga kesehatan kaa, dan semangat kuliahnyaa!"},
        {"nama": "Desman Velius Halawa", "nim": "123450114", "umur": "17", "asal": "Nias", "alamat": "Airan", "hobbi": "Bermusik", "sosmed": "@desmannhal_", "kesan": "Asik dan seruu abangnya", "pesan": "Semangatt TA nya nanti bangg, semoga dilancarkan segala urusannya!"},
        {"nama": "Azzelya Thianandry", "nim": "124450041", "umur": "19", "asal": "Lampung", "alamat": "Sukarame", "hobbi": "Makan Aice", "sosmed": "@azzelytn", "kesan": "Kakanya cantik and ramah", "pesan": "Semangattt kaa kuliahnyaa! jangan lupa jaga kesehatan jugaa"},
        {"nama": "Charrlindah", "nim": "124450037", "umur": "21", "asal": "Jakarta Pusat", "alamat": "Cendrawasih 1", "hobbi": "Ngurus peternakan", "sosmed": "@charrlln", "kesan": "Kakanya baik and ramahh sekalii", "pesan": "Sehat selalu dan semangat kuliahnya kaa!"},
        {"nama": "Jeremi Marolop P. Situmorang", "nim": "124450111", "umur": "17", "asal": "Nibire, Papua", "alamat": "Sebelah kos Haikal", "hobbi": "Memahat patung", "sosmed": "@jemarrro", "kesan": "Abangnya tegas banget, tapi cukup welcome kalau di ajak ngobrol", "pesan": "Semangat kuliahnya bangg, sehat sehat!"},
        {"nama": "Nabila Nur Azizah", "nim": "124450048", "umur": "19", "asal": "Lampung Timur", "alamat": "Belwis", "hobbi": "Main Roblox", "sosmed": "@n.bila_a", "kesan": "Kakanya baik dan ramah", "pesan": "Jangan lupa jaga kesehatan dan semnangat kuliahnya kaa!"},
        {"nama": "Rafli Al Mansyah Tambunan", "nim": "124450007", "umur": "20", "asal": "Tembung", "alamat": "Belwis Tengah", "hobbi": "Mancing", "sosmed": "@dearfkvmfl", "kesan": "Baik dan asik", "pesan": "Semangattt kuliahnya bangg!"},
        {"nama": "Salavia Naharani", "nim": "124450090", "umur": "20", "asal": "Lampung Timur", "alamat": "Jatimulyo", "hobbi": "Nonton", "sosmed": "@avi.nhr", "kesan": "Imut dan lucuu", "pesan": "Semangat teruss kaa kuliahnyaa!!"}
    ]
    display_images_with_data(gambar_urls, data_list)

# --- 5. DEPARTEMEN EKSTERNAL ---
elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1nsN3TV4twKSbjBdoIzTqW6VYpgxXaJK5",
        "https://drive.google.com/uc?export=view&id=1LIlJ3cvLC3iqiRl5jszIlZgdPSUeb5Ks",
        "https://drive.google.com/uc?export=view&id=1xVBHbJxkymxCXI6MKj6DBiS4n9S51jlz",
        "https://drive.google.com/uc?export=view&id=1bOtboNzQUnQuWU3yPd5jtaOaNUUmENe8",
        "https://drive.google.com/uc?export=view&id=1I3e9ufUUa2SeQF7UeN7yezIf_l4OVQBS",
        "https://drive.google.com/uc?export=view&id=15pv1O1bhQKEGWhUkjqdTwdURzTqUF_Oo",
        "https://drive.google.com/uc?export=view&id=1Wxe1-cc8OAJitdOn4divJlNCLB7iEKP3",
        "https://drive.google.com/uc?export=view&id=1EtOAhb1iW2vi5ON5_J5UsOHDfiKRHbtX",
        "https://drive.google.com/uc?export=view&id=1Q0bfgvtRf52KGDtfg73jGykaAVcyYL5p",
        "https://drive.google.com/uc?export=view&id=16_6Hxh5BrrU6sdbhGA18ZDILJE-HleTW",
        "https://drive.google.com/uc?export=view&id=1HWpHXERG9xj-Ortt3qYfVd4LmTObYw24",
        "https://drive.google.com/uc?export=view&id=1oerpvhqKBLxrjWDAptSvaQCtiNUq4le_",
        "https://drive.google.com/uc?export=view&id=1QwtLVj7LbCImanpLeT3BjBnwNWwH2zNh",
        "https://drive.google.com/uc?export=view&id=19pYqYKE24bNxABF5c2DZN3vshDqYodK4",
        "https://drive.google.com/uc?export=view&id=1Fb2pod6Pd1kcsbe-rpyHDfz1-6nmixTr",
        "https://drive.google.com/uc?export=view&id=1-ylGqoH5ix1iXPT0OUOsTOqoGi7QkGtA",
        "https://drive.google.com/uc?export=view&id=1sq_JPdYFDoRpRK0PjT4mLNjGk5iSCoGA",
        "https://drive.google.com/uc?export=view&id=11l2tKMnP74bIQZImA8jejzO6ojY_50ja",
        "https://drive.google.com/uc?export=view&id=1zFgKAhODhHunfbxIuLM3q8RUj2zlz763",
        "https://drive.google.com/uc?export=view&id=1HC78n-R52FfVX820vhbq0to1lzalcn1z",
        "https://drive.google.com/uc?export=view&id=1vDtAWkEdxpXvoCzI_Lk6WVcIgFvbynSk",
        "https://drive.google.com/uc?export=view&id=167SM0igqIGQlquzXc_LRHi00jWtx0utO"
    ]
    data_list = [
        {"nama": "Arini Puteri Elandra", "nim": "123450069", "umur": "21", "asal": "Lampung", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Karismatik woman, baik tapi tegas", "pesan": "Sukses selalu kaa kedepannya, dan nanti semangat nyusun TA nyaa!!"},
        {"nama": "Nabyla Sharfina", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jalan lapas", "hobbi": "Jalan-jalan", "sosmed": "@bylaash", "kesan": "Cantik dan baikk", "pesan": "Semangatt kaa kuliahnyaa dan juga semangatt nyusun TA nya!!"},
        {"nama": "Khoirul Muttoharoh", "nim": "123450021", "umur": "21", "asal": "Lampung barat", "alamat": "Airan", "hobbi": "Main", "sosmed": "@khoirul_muttoharoh", "divisi": "Hubungan Luar", "kesan": "Imutt", "pesan": "Semangat kaa nanti nyusun TA nyaa, semoga diberikan kemudahan dalam segala hal. Aamiin"},
        {"nama": "Ahmad Rizky", "nim": "123450050", "umur": "21", "asal": "Tangerang Selatan", "alamat": "GH", "hobbi": "Ga ngapa ngapain", "sosmed": "@ahmad.rizky___", "divisi": "Hubungan Luar", "kesan": "KERENNNN!!! abang beneran jadi role model saya bangett", "pesan": "Jaga kesehatan bangg di negara yang ga sehat ini"},
        {"nama": "Adinda Deswita Maharani", "nim": "124450083", "umur": "cepuyuh tayun", "asal": "Ikut kadep", "alamat": "Sukabumi", "hobbi": "Mancing", "sosmed": "@khaindaa_", "divisi": "Hubungan Luar", "kesan": "Kakanya ramah dan baik", "pesan": "Jaga kesehatan kaa, dan semangatt kuliahnyaa!"},
        {"nama": "Ahmad Bimo Akbar Arkana", "nim": "124450113", "umur": "-", "asal": "Tanggamus", "alamat": "Balam", "hobbi": "Lihat-lihat perumahan", "sosmed": "@bimo_arkana", "divisi": "Hubungan Luar", "kesan": "Keren dan ramah", "pesan": "Semangat terus bang kuliahnyaa, jaga kesehatan juga!!"},
        {"nama": "Alfaya Abiyyi", "nim": "124450006", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Makan yang manis biar manis", "sosmed": "@alfayabiyi", "divisi": "Hubungan Luar", "kesan": "Kerennnn", "pesan": "Semangattt bang kuliahnyaa, jaga kesehatan jugaa!"},
        {"nama": "Asri Meilani", "nim": "124450010", "umur": "20", "asal": "Lampung Barat", "alamat": "Korpri", "hobbi": "Nonton Film", "sosmed": "@asemeilani", "divisi": "Hubungan Luar", "kesan": "Baik dan lucuu kakanyaa", "pesan": "Sukses selalu kak untuk ke depannya!!"},
        {"nama": "Bima Ekayasa", "nim": "124450106", "umur": "20", "asal": "Lampung", "alamat": "Bandar Lampung", "hobbi": "Berlaku humoris dan manis", "sosmed": "@bimayasa_", "divisi": "Hubungan Luar", "kesan": "Kerennn, baik dan ramah", "pesan": "Semangatt terus bangg kuliahnya walau makin tambah semester makin nambah juga stressnya. Jaga kesehatan jugaa!"},
        {"nama": "Indah Khairunnisa", "nim": "124450077", "umur": "20", "asal": "Ampera", "alamat": "Disini aja", "hobbi": "Mancing", "sosmed": "@khaindaa_", "divisi": "Hubungan Luar", "kesan": "Baik dan lucuu", "pesan": "Kakk jangan ikut marah-marah kaa, kaka versi medis beneran terbaik banget"},
        {"nama": "Riska Erlis Dayu Tiara", "nim": "124450022", "umur": "20", "asal": "Palembang", "alamat": "Bebas", "hobbi": "ngefollow up chat", "sosmed": "@erlsriska", "divisi": "Hubungan Luar", "kesan": "Gemass", "pesan": "Jaga kesehatan ya kaa, dan semangat juga kuliahnya!!"},
        {"nama": "Yollanda Agustina", "nim": "124450024", "umur": "20", "asal": "Kerangka Bawang Sebelah Barat", "alamat": "Jati Agung", "hobbi": "Main Futsal", "sosmed": "@yollanda_agustina16", "divisi": "Hubungan Luar", "kesan": "Semangatt terus ka yollandaaaa, kak yollanda keren hebat and kuattt", "pesan": "Jaga kesehatan ya kaa, apalagi kaka ambil banyak kepanitian. Jangan sampe drop kaa"},
        {"nama": "Aditya Taufiqurrohman", "nim": "123450032", "umur": "22", "asal": "Tetangga Kadep", "alamat": "Belwis", "hobbi": "Memancing keributan", "sosmed": "@adityatfq", "divisi": "Pengabdian Masyarakat", "kesan": "Baik, ramah, dan welcome bangett", "pesan": "Semangatt bang ngerjain TA nya, semoga selalu dipermudah langkah selanjutnyaa, Aamiin!"},
        {"nama": "Fathya Intami Gusda", "nim": "123450095", "umur": "25", "asal": "Tangerang Selatan", "alamat": "Sukarame", "hobbi": "Baca wattpad", "sosmed": "@fatthyaa_", "divisi": "Pengabdian Masyarakat", "kesan": "Keren banget kakanyaa", "pesan": "Jaga kesehatan ya kaa, dan capai imppian kaka satu persatu!"},
        {"nama": "Tarisya Hidayatul Rahmi", "nim": "123450052", "umur": "25", "asal": "Luhak tanah data", "alamat": "Gerbang barat", "hobbi": "Jadi orang baik", "sosmed": "-", "divisi": "Pengabdian Masyarakat", "kesan": "Manis dan imutt", "pesan": "Sukses selalu kaa untuk kedepannya, raih goals kaka satu persatu!"},
        {"nama": "Ashila Islamisahfa Vanisha", "nim": "124450028", "umur": "20", "asal": "Sini", "alamat": "Jauh pokoknya", "hobbi": "Tidur", "sosmed": "@kshigf", "divisi": "Pengabdian Masyarakat", "kesan": "Cantik dan ramah", "pesan": "Jangan lupa untuk berbahagia ya kaa!"},
        {"nama": "Danil N Fadillah", "nim": "124450103", "umur": "19", "asal": "Karawang", "alamat": "Belakang Polda", "hobbi": "Ngasih makan ikan cupang", "sosmed": "@d4niel_fdlh", "divisi": "Pengabdian Masyarakat", "kesan": "Keren dan baik", "pesan": "Semangat kuliahnya dan jaga kesehatannya bangg!"},
        {"nama": "Favian Arkaanda", "nim": "124450021", "umur": "19", "asal": "Swiss", "alamat": "Way Halim", "hobbi": "Ngesen kanan", "sosmed": "@fvnnn05", "divisi": "Pengabdian Masyarakat", "kesan": "Mirip influencer si itu siapa namanya", "pesan": "Kerenn banggg, semangatt menjalani perkuliahan dan kehidupan #salambinjai"},
        {"nama": "Muhammad Fathiy Zumar Yazid", "nim": "124450081", "umur": "20", "asal": "situlah", "alamat": "pohon mulia", "hobbi": "nyari hobi", "sosmed": "@zydddddd__", "divisi": "Pengabdian Masyarakat", "kesan": "Abang keren kalau ga marah-marah", "pesan": "Panjang umur sehat selalu bang, tetep semangat kuliah walau setiap semesternya bikin asam lambung naik"},
        {"nama": "Muhammad Rizaldi", "nim": "124450093", "umur": "Masih muda lah", "asal": "Rahim Ibu", "alamat": "Pasar lantai 3.5", "hobbi": "Membantu Yudia", "sosmed": "@jaldii._", "divisi": "Pengabdian Masyarakat", "kesan": "KERENNN, jujur inspiring bangett", "pesan": "Semangattt terus bang jaldi gapai impian satu persatu!!"},
        {"nama": "Saskia Nova Magdalena", "nim": "124450074", "umur": "...", "asal": "Banyak Begal", "alamat": "Pinggir Jalan", "hobbi": "nonton thinkerbell", "sosmed": "@snova.19", "divisi": "Pengabdian Masyarakat", "kesan": "Kakanya imut dan ramah", "pesan": "Semangatttttt kaa kuliahnyaaa! GO GOO!!"},
        {"nama": "Selma Siti Aisyah", "nim": "123450044", "umur": "20", "asal": "Lampung", "alamat": "Bandara Lampung", "hobbi": "Jalan-jalan", "sosmed": "@selmasiti_aisyah", "divisi": "Pengabdian Masyarakat", "kesan": "Ramah dan cantikk", "pesan": "Vibes kakanya ceria dan positif bangett"}
    ]
    display_images_with_data(gambar_urls, data_list)

# --- 6. DEPARTEMEN INTERNAL ---
elif menu == "Departemen Internal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1yY0UcwW0OGe_wjFslLfXidx_p4gdgLtM",
        "https://drive.google.com/uc?export=view&id=1iMWWQ-gfJ9Js44b-4WAN1X8jUt0MqhgO",
        "https://drive.google.com/uc?export=view&id=14qKtE3QEiRqY0jIFfdDtCSJ40uLRf3LR",
        "https://drive.google.com/uc?export=view&id=1kSzlnSY5d-sk13sjDAJJgCGxb53ZLWog",
        "https://drive.google.com/uc?export=view&id=1zZjq_bHdB3TPOYicpBQwfpv7-TTPoDmV",
        "https://drive.google.com/uc?export=view&id=1mPpQTVwD8gHg3EWuKGhXrm3r6wZB8st5",
        "https://drive.google.com/uc?export=view&id=19Ha4jsx1tN59eAYslpGxJ3HLVLtSjTNu",
        "https://drive.google.com/uc?export=view&id=1ulrI05TtdAZL09sCYfN8AguuPDnwMoOI",
        "https://drive.google.com/uc?export=view&id=14gSC9XO8GLBYL9fp0QRkAafgY0h_XPxy",
        "https://drive.google.com/uc?export=view&id=1vFJx5bFIWHeD-YB6nNOm8IGqXet75nTQ"
    ]
    data_list = [
        {"nama": "Haikal Fransisko Simbolon", "nim": "123450106", "umur": "20", "asal": "Sidikalang", "alamat": "Belwis", "hobbi": "Ngoding", "sosmed": "@haikalsbln_", "kesan": "Kerenn", "pesan": "Semangat TA nya bangg, semoga diberi kemudahan dan dilancarkan semua urusannyaa"},
        {"nama": "Kharisma Mustika Sari", "nim": "123450034", "umur": "21", "asal": "Way Kanan", "alamat": "Untung Senopati", "hobbi": "Menolong orang", "sosmed": "@rismaa.mustika_", "kesan": "Cantik dan ramah", "pesan": "Semangattt kaa untuk TA nyaa, jangan lupa jaga kesehatan yaa!"},
        {"nama": "Hanna Gresia Sinaga", "nim": "123450038", "umur": "21", "asal": "Kisaran City", "alamat": "Sukarame", "hobbi": "Menyapa satpam ITERA", "sosmed": "@hanna_g_sinaga", "kesan": "Positig energy bangettt", "pesan": "Semoga kaka selalu dilingkupi oleh banyak kebaikan yaa, dan semangat nanti TA nyaa!"},
        {"nama": "Ahmad Farhan Ghani", "nim": "123450121", "umur": "20", "asal": "Kemiling", "alamat": "Kemiling", "hobbi": "Olahraga menembak", "sosmed": "@farhnghnii", "kesan": "Skill perkusi nya kerenn bangg", "pesan": "Sehat selalu bangg dan semangat TA nyaa!"},
        {"nama": "Aisyah Khairun Nisa", "nim": "124450096", "umur": "20", "asal": "Riau", "alamat": "Belwis", "hobbi": "Menulis wishlist", "sosmed": "@aisyahkhair", "kesan": "Kakanya gemas bangett dan ramahh", "pesan": "Sehat-sehat ya kaaa!"},
        {"nama": "Cerine Sihotang", "nim": "124450049", "umur": "19", "asal": "Medan", "alamat": "Belwis", "hobbi": "Balap Liar", "sosmed": "@cerine_ipynb", "kesan": "Lucuuu", "pesan": "Sehat selalu kaa, dan semangat kuliahnyaa!"},
        {"nama": "Jaya Saputra Tamba", "nim": "124450094", "umur": "22", "asal": "Kisaran City", "alamat": "Pemda", "hobbi": "Kick Boxing", "sosmed": "@jay.saputratmb", "kesan": "Asik dan ramah", "pesan": "Semangatt kuliahnya bangg, semoga plan abang bisa tercapai satu-persatu"},
        {"nama": "Najla Nursyifa", "nim": "124450051", "umur": "20", "asal": "Aceh", "alamat": "Belwis", "hobbi": "Nonton ASMR", "sosmed": "@njlanursyifa", "kesan": "Kakanya gemass bangett", "pesan": "Semangatt terus ka kuliahnyaa"},
        {"nama": "Rozak Ramdani", "nim": "124450100", "umur": "18", "asal": "Lampung Selatan", "alamat": "Korpri Raya", "hobbi": "Isengin Harvin di kelas", "sosmed": "@rozakramdani__", "kesan": "Abang keren dan ramah", "pesan": "Semangatt bang menjalani perkuliahan dan proker himpunannya!"},
        {"nama": "Teresa Christiani Purba", "nim": "124450046", "umur": "19", "asal": "Riau", "alamat": "Belwis", "hobbi": "Masak", "sosmed": "@christiani8872", "kesan": "My kaka tutorr", "pesan": "Sumpah terimakasih banyak kaaa udah ngambil kesempatan untuk jadi astut LMD. Saya merasa terbantu bangettt. Maaf juga kemarin aku banyak diamnya pas tutor karena kebetulan waktunya berbarengan dengan wwc dan hal lainnya"}
    ]
    display_images_with_data(gambar_urls, data_list)

# --- 7. DEPARTEMEN SSD ---
elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1aMv9qlfsOuyoPiS2R8NTcgAxozaNZqou",
        "https://drive.google.com/uc?export=view&id=1PT6ipJ2f-hCrUjXJeNx4DjWaudZuIVvx",
        "https://drive.google.com/uc?export=view&id=1UqjrZcNLpl09Tz_nF4TAHmhMpYAhXKtz",
        "https://drive.google.com/uc?export=view&id=1hn4PgTaL24skiwubJiRXN8FMc_9vrKno",
        "https://drive.google.com/uc?export=view&id=17d-nP_G08HsSbs60e_Z7fwzLlsQ38dA2",
        "https://drive.google.com/uc?export=view&id=1k2DniopsMXjCT6-kWZOVtWyeb2l9drGn",
        "https://drive.google.com/uc?export=view&id=1gJOc_kFxHewv61AhgdEjwXIm4ZWeYS5W",
        "https://drive.google.com/uc?export=view&id=18r-fmfLgTw20T_3VrkT5S81c57TBtZy3",
        "https://drive.google.com/uc?export=view&id=1X1f9zdjDGzs8bxpmaAyerdTKjY3fQN7g",
        "https://drive.google.com/uc?export=view&id=1idD0yxRZ26xBhd2WjUYvs9moCSU0yEAj",
        "https://drive.google.com/uc?export=view&id=1z6mzgHPVOaHUuHgn2NFf5QtgvIhdqmfk",
        "https://drive.google.com/uc?export=view&id=1Zl7FrDBs1q_1u5ETnETkn5J25Ra5Lrdq"
    ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "nim": "123450110", "umur": "21", "asal": "Sumbar", "alamat": "Belwis", "hobbi": "Baca jurnal, cari jurnal yang berhubungan ta", "sosmed": "@ihsan.myusuf", "kesan": "Kakak ini asik saya suka belajar dengan dia", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Hanifah Inaya Sani", "nim": "123450009", "umur": "21", "asal": "Balam", "alamat": "Korpri", "hobbi": "Memasak", "sosmed": "@_inayasani", "kesan": "Kakak ini asik saya suka belajar dengan dia", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Afifah Fauziah", "nim": "123450002", "umur": "18", "asal": "Padang", "alamat": "Hasan 4", "hobbi": "Baca jurnal, nonton Marvel", "sosmed": "-", "kesan": "Kakak ini asik saya suka belajar dengan dia", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Hasan Nur Ramadhan", "nim": "124450013", "umur": "25", "asal": "Lamteng", "alamat": "Pemda", "hobbi": "Nonton yutub", "sosmed": "-", "kesan": "Kakak ini asik saya suka belajar dengan dia", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Layina Ropiqo", "nim": "124450016", "umur": "20", "asal": "Semarang", "alamat": "Balam", "hobbi": "Nonton dracin", "sosmed": "@layinr_", "kesan": "Kakak ini asik saya suka belajar dengan dia", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Talitha Justine", "nim": "124450076", "umur": "19", "asal": "Sumbar", "alamat": "Pemda", "hobbi": "Nonton", "sosmed": "@talljtine_", "kesan": "Kakak ini asik saya suka belajar dengan dia", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Mochammad Iqbal Az-zahir", "nim": "124450052", "umur": "20", "asal": "Bekasi", "alamat": "Natar", "hobbi": "Nonton Drakor", "sosmed": "@iqbalazzahir_", "kesan": "Kakak ini asik saya suka belajar dengan dia", "pesan": "semangat terus kuliahnya kakak !!!"}
    ]
    display_images_with_data(gambar_urls, data_list)

# --- 8. DEPARTEMEN MINBAK ---
elif menu == "Departemen Minbak":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1Udk2xpvnZx6fPqH0f9wwTJN980Bz1TkV",
        "https://drive.google.com/uc?export=view&id=15Yw6OAHvR23TlQWly2hcYUanBIOinm8K",
        "https://drive.google.com/uc?export=view&id=1LAJkUbx8KooEozXE57nFs0fWwWtw2aIP",
        "https://drive.google.com/uc?export=view&id=1ycj9bzqvPwFxuGZBljR6lo3qUM8UVrib",
        "https://drive.google.com/uc?export=view&id=1bmq4huEEg36soPANR5uIcqpw-PPk38x2",
        "https://drive.google.com/uc?export=view&id=10dndlb7oI4Iu3gjolRIzTLtk5cAeTpQF",
        "https://drive.google.com/uc?export=view&id=17KZMQOw0MuSyUy28i0J71aVIFCwrPtNf",
        "https://drive.google.com/uc?export=view&id=1CadH0SDhfRZiE9V3cehnGvRk7UDupoYm",
        "https://drive.google.com/uc?export=view&id=1BUjU9oqJxp17o_Rn-Wg-QGqDnkfIZvyX",
        "https://drive.google.com/uc?export=view&id=1Ic-k9SPonBkbgOwesBrmyK__ne-o-rvv",
        "https://drive.google.com/uc?export=view&id=1Yruir4LTmRioWy3eogCH8peS6sw14xg2",
        "https://drive.google.com/uc?export=view&id=1l6WFa-Obnwn1x7t9BQf3L7cAFL9iPss5",
        "https://drive.google.com/uc?export=view&id=13yIUWXRoArqanTVyR5a4I_jGqslJ8J0o",
        "https://drive.google.com/uc?export=view&id=13yIUWXRoArqanTVyR5a4I_jGqslJ8J0o",
        "https://drive.google.com/uc?export=view&id=1cMHzTwL_osj4CvaWdPCSfrrpTdqQKAoJ"
    ]
    data_list = [
        {"nama": "Kevin Antonio Junior", "nim": "123450109", "umur": "23", "asal": "Sulawesi Tengah", "alamat": "Panjang", "hobbi": "Mancing", "sosmed": "@kevinaja__", "kesan": "Sangat menginspirasi dan memimpin dengan baik", "pesan": "Semangat terus kak!"},
        {"nama": "Gusti Putu Ferazka Dhiyamika", "nim": "123450046", "umur": "21", "asal": "Bekasi", "alamat": "Way Dadi", "hobbi": "Mendaki", "sosmed": "@ferazkaa", "kesan": "Sangat rapi dan cekatan dalam mengelola administrasi", "pesan": "Sukses selalu kak!"},
        {"nama": "Ali Aristo Muthahhari Parisi", "nim": "123450088", "umur": "21", "asal": "Lampung Timur", "alamat": "Gang Sakum Belwis", "hobbi": "Nonton F1", "sosmed": "@ali_parisi3", "kesan": "Keren dan selalu memberikan arahan yang jelas", "pesan": "Semangat menjalankan tugasnya kak!"},
        {"nama": "Ayu Andriani Parlina Wati", "nim": "124450058", "umur": "20", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "Belajar + menghitung uang", "sosmed": "@aayuandriani_", "kesan": "Sangat ramah dan aktif berkontribusi", "pesan": "Tetap semangat dan sukses terus!"},
        {"nama": "Dafa Elpriza", "nim": "124450131", "umur": "21", "asal": "Bekasi", "alamat": "Way Kandis", "hobbi": "Jogging", "sosmed": "@dafaelpriza_", "kesan": "Sangat menyenangkan dan mudah diajak kerja sama", "pesan": "Sukses terus perkuliahan dan aktivitasnya!"},
        {"nama": "Juwita Sari", "nim": "124450066", "umur": "19", "asal": "Lampung Barat", "alamat": "Pemda", "hobbi": "Mancing", "sosmed": "@ju.juwitaaa_", "kesan": "Sangat baik dan murah senyum", "pesan": "Semangat terus kuliahnya!"},
        {"nama": "Muhammad Afdal Luthfi", "nim": "124450047", "umur": "19", "asal": "Lampung Tengah", "alamat": "Jl. Pulau Damar", "hobbi": "Memantau dl tugas", "sosmed": "@afdall.03", "kesan": "Sangat bertanggung jawab dan fokus", "pesan": "Semangat terus kakak!"},
        {"nama": "Salsabila Nazwa Putri", "nim": "124450002", "umur": "20", "asal": "Metro", "alamat": "Korpri", "hobbi": "Nongkrong di kopken", "sosmed": "@slbnzw_", "kesan": "Sangat asik dan ceria", "pesan": "Tetap semangat kuliahnya ya kak!"},
        {"nama": "Muhammad Ridwan", "nim": "123450091", "umur": "21", "asal": "Lampung Tengah", "alamat": "Belwis", "hobbi": "Badminton", "sosmed": "@mridwaan_22", "kesan": "Sangat mengayomi dan membimbing dengan sabar", "pesan": "Semangat terus memimpin divisinya kak!"},
        {"nama": "Andra Ilham Bintang", "nim": "124450060", "umur": "18", "asal": "Sumatera Selatan", "alamat": "Kotabaru", "hobbi": "Main rubik", "sosmed": "@andra.lhm", "kesan": "Sangat kreatif dan pintar", "pesan": "Sukses selalu kuliahnya!"},
        {"nama": "Bryan Paskah Telaumbanua", "nim": "124450003", "umur": "20", "asal": "Nias", "alamat": "Belwis", "hobbi": "Live tiktok", "sosmed": "@bryantel_", "kesan": "Sangat menghibur dan ramah", "pesan": "Semangat terus berkarya kak!"},
        {"nama": "Ghiyats Thabularasa Meardhy", "nim": "124450067", "umur": "17", "asal": "Surabaya", "alamat": "Kemiling", "hobbi": "Nanem Sawit", "sosmed": "@meardhy_ghiyats", "kesan": "Sangat unik dan bersemangat", "pesan": "Tetap semangat dan sukses selalu!"},
        {"nama": "Indah Julia Mawar Pratiwi", "nim": "124450055", "umur": "20", "asal": "Pringsewu", "alamat": "Airan", "hobbi": "Bengong", "sosmed": "@indahjuliaa", "kesan": "Sangat baik dan bersahabat", "pesan": "Sukses terus perkuliahannya kak!"},
        {"nama": "Jacinda Kesya Alvara", "nim": "124450023", "umur": "18", "asal": "Kalimantan Barat", "alamat": "Korpri", "hobbi": "Nyapu depan gacoan", "sosmed": "@cacalvra", "kesan": "Sangat ceria dan menyenangkan", "pesan": "Semangat terus ya kak!"},
        {"nama": "Muhammad Rafka", "nim": "124450089", "umur": "20", "asal": "Padang", "alamat": "Kotabaru", "hobbi": "Bangun pagi", "sosmed": "@muhammdrafka_", "kesan": "Sangat disiplin dan dapat diandalkan", "pesan": "Sukses selalu buat perkuliahannya!"}
    ]
    display_images_with_data(gambar_urls, data_list)
