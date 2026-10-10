import streamlit as st
from streamlit_option_menu import option_menu
import requests
import re
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


@st.cache_data(show_spinner=False)
def load_image(url):
    """Mengambil dan memvalidasi gambar sebelum ditampilkan."""
    direct_url = get_direct_image_url(url)

    try:
        response = requests.get(
            direct_url,
            timeout=20,
            allow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()

        # Pastikan respons benar-benar berisi data gambar, bukan halaman HTML.
        content_type = response.headers.get("Content-Type", "").lower()
        if "image" not in content_type:
            try:
                image = Image.open(BytesIO(response.content))
                image.verify()
            except Exception:
                return None

        image = Image.open(BytesIO(response.content))
        image = ImageOps.exif_transpose(image).convert("RGB")
        image.thumbnail((600, 800))
        return image

    except Exception:
        return None


def display_images_with_data(gambar_urls, data_list):
    """Menampilkan setiap data orang dengan gambar yang sesuai."""
    jumlah = max(len(gambar_urls), len(data_list))

    for i in range(jumlah):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            if i < len(gambar_urls):
                with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
                    img = load_image(gambar_urls[i])

                if img is not None:
                    st.image(img, use_container_width=True)
                else:
                    st.info(
                        f"Gambar ke-{i + 1} tidak dapat dimuat. "
                        "Pastikan link benar dan akses Google Drive diatur "
                        "ke 'Siapa saja yang memiliki link'."
                    )
            else:
                st.info("URL gambar belum ditambahkan.")

        if i < len(data_list):
            orang = data_list[i]
            st.write(f"Nama: {orang.get('nama', '-')}")
            st.write(f"NIM: {orang.get('nim', '-')}")
            st.write(f"Umur: {orang.get('umur', '-')}")
            st.write(f"Asal: {orang.get('asal', '-')}")
            st.write(f"Alamat: {orang.get('alamat', '-')}")
            st.write(f"Hobi: {orang.get('hobbi', '-')}")
            st.write(f"Sosial Media: {orang.get('sosmed', '-')}")
            st.write(f"Kesan: {orang.get('kesan', '-')}")
            st.write(f"Pesan: {orang.get('pesan', '-')}")
            st.divider()

    st.success("Selesai memproses daftar anggota.")



menu = streamlit_menu()

# BAGIAN MENU KESEKJENAN
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lMm2cZotf4Zg5npQZTNsGulE71uamr0G",
            "https://drive.google.com/uc?export=view&id=1L1mV6NSK_dwiOB1dMLtHXVss8YvviGF7",
            "https://drive.google.com/uc?export=view&id=1arEBvurK397f3EPs4YmXihuHpY_0Ngnk",
            "https://drive.google.com/uc?export=view&id=1Iv7PgxUJ9qVu-8EuqH73CJZ0ZATL3irL",
            "https://drive.google.com/uc?export=view&id=1Iwen8hJLSVc5_-C7sEAhlDoByhm82chK",
        ]

        data_list = [
            {"nama": "Ginda Fajar Marpaung", "nim": "1234500fadil", "umur": "22", "asal": "Batam", "alamat": "Sekretariat HMSD", "hobbi": "Push Rank sampe IMO", "sosmed": "@gars_mrp", "kesan": "-", "pesan": "-"},
            {"nama": "Muhammad Aqil", "nim": "123450046", "umur": "22", "asal": "Bangkinang", "alamat": "Sekretariat HMSD", "hobbi": "Dzikir", "sosmed": "@muhammadaqil1111", "kesan": "-", "pesan": "-"},
            {"nama": "Evi Defiati", "nim": "123450005", "umur": "21", "asal": "Lamtim", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffifi", "kesan": "-", "pesan": "-"},
            {"nama": "Qois Alfio", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kotabaru", "hobbi": "Mainin surat", "sosmed": "@qoidalfio_", "kesan": "-", "pesan": "-"},
            {"nama": "Hafsa Fadzilah Arraadhila", "nim": "079", "umur": "21", "asal": "Balam", "alamat": "Balam", "hobbi": "Berenang", "sosmed": "@hafsafadhilaa", "kesan": "-", "pesan": "-"},
            {"nama": "Luthfia Laila Ramadhani", "nim": "004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Bertemu Pak Tirta", "sosmed": "@lutfiaarmdhn", "kesan": "-", "pesan": "-"},
        ]

        display_images_with_data(gambar_urls, data_list)

    kesekjenan()
