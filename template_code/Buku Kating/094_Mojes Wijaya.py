import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import json
import os

# ===== STYLING TEMA HITAM - OREN =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

    .stApp {
        font-family: 'Poppins', sans-serif;
    }

    .kating-title {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 2.8em;
        font-weight: 800;
        background: linear-gradient(135deg, #ffd740, #ffab40, #ff6e40);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 2px;
        margin-bottom: 0.1rem;
    }
    .kating-subtitle {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 1.05em;
        color: #b0bec5;
        font-weight: 300;
        letter-spacing: 1.5px;
        margin-bottom: 0.5rem;
    }
    .fancy-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ffd740, #ffab40, transparent);
        margin: 1rem auto 1.5rem auto;
        max-width: 450px;
        border: none;
    }

    /* Division section banner */
    .division-banner {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: 2rem 0 1.2rem 0;
        padding: 0.7rem 1.4rem;
        background: linear-gradient(90deg, rgba(255, 171, 64, 0.18), rgba(20, 20, 36, 0.5));
        border-left: 4px solid #ff9800;
        border-radius: 0 12px 12px 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    .division-banner-title {
        font-size: 1.2em;
        font-weight: 700;
        color: #ffd740;
        letter-spacing: 0.5px;
    }
    .division-banner-badge {
        font-size: 0.82em;
        font-weight: 600;
        color: #ffd740;
        background: rgba(255, 171, 64, 0.2);
        padding: 4px 10px;
        border-radius: 20px;
        border: 1px solid rgba(255, 171, 64, 0.4);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center;'>
    <h1 class='kating-title'>BUKU KATING</h1>
    <p class='kating-subtitle'>CEO HMSD Adyatama ITERA 2026</p>
    <div class='fancy-divider'></div>
</div>
""", unsafe_allow_html=True)


# ===== MENU UTAMA DEPARTEMEN (TEMA HITAM - OREN) =====
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
            "Departemen MINBAK",
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
            "container": {
                "padding": "6px 4px!important",
                "background-color": "#12121e",
                "border-radius": "12px",
                "border": "1px solid rgba(255, 171, 64, 0.25)",
                "box-shadow": "0 4px 20px rgba(0, 0, 0, 0.3)",
            },
            "icon": {"color": "#ffd740", "font-size": "17px"},
            "nav-link": {
                "font-size": "13px",
                "font-weight": "500",
                "text-align": "center",
                "margin": "2px",
                "color": "#cfd8dc",
                "--hover-color": "rgba(255, 171, 64, 0.15)",
                "border-radius": "8px",
            },
            "nav-link-selected": {
                "background-color": "#ff9800",
                "color": "#0f0f1a",
                "font-weight": "700",
                "box-shadow": "0 2px 10px rgba(255, 152, 0, 0.35)",
            },
        },
    )
    return selected


# ===== SUB-MENU DIVISI (TEMA HITAM - OREN) =====
def divisi_menu(options, dept_key):
    if len(options) <= 1:
        return options[0] if options else "Semua"

    selected_divisi = option_menu(
        menu_title=None,
        options=options,
        icons=["grid-fill"] + ["folder-fill"] * (len(options) - 1),
        orientation="horizontal",
        styles={
            "container": {
                "padding": "4px 2px!important",
                "background-color": "rgba(22, 22, 38, 0.7)",
                "border-radius": "10px",
                "border": "1px solid rgba(255, 215, 64, 0.2)",
                "margin": "1rem 0 1.2rem 0",
            },
            "icon": {"color": "#ffab40", "font-size": "14px"},
            "nav-link": {
                "font-size": "12.5px",
                "font-weight": "500",
                "text-align": "center",
                "margin": "2px 4px",
                "color": "#b0bec5",
                "--hover-color": "rgba(255, 215, 64, 0.15)",
                "border-radius": "6px",
            },
            "nav-link-selected": {
                "background-color": "#ffd740",
                "color": "#0f0f1a",
                "font-weight": "700",
            },
        },
        key=f"sub_divisi_{dept_key}",
    )
    return selected_divisi


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


def display_images_with_data(gambar_urls, data_list, show_finished_message=True):
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
            if "jabatan" in data_list[i] and data_list[i]["jabatan"] and data_list[i]["jabatan"] != "-":
                st.write(f"Jabatan: {data_list[i]['jabatan']}")
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

    if show_finished_message:
        st.write("Semua gambar telah dimuat!")


menu = streamlit_menu()


# ========================================================================
# PENGAMBILAN & PENGELOLAAN DATA BUKU KATING
# ========================================================================
# Helper: Load data dari JSON
@st.cache_data
def load_json_data():
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data/data_statis/data_anggota_hmsd_2026.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

data_anggota = load_json_data()

# Mapping menu label -> departemen name di JSON
DEPT_MAP = {
    "Kesekjenan": "Kesekjenan",
    "Baleg": "Badan Legislatif (BALEG)",
    "Senator": "Badan Kesenatoran (BASON)",
    "Departemen PSDA": "Pengembangan Sumber Daya Anggota (PSDA)",
    "Departemen MIKFES": "Akademik dan Keprofesian (MIKFES)",
    "Departemen Eksternal": "Eksternal",
    "Departemen Internal": "Internal",
    "Departemen SSD": "Storage Sains Data (SSD)",
    "Departemen Medkraf": "Media Kreatif (MEDKRAF)",
    "Departemen MINBAK": "Minat dan Bakat (MINBAK)",
}

# Urutan jabatan di tingkat Pimpinan (Kadep/Senator/Baleg/Ketua lebih dulu, lalu Sekdep/Sekretaris, dsb.)
def jabatan_sort_key_pimpinan(member, menu_label):
    jab = member.get("jabatan", "").lower().strip()
    if "kesekjenan" in menu_label.lower():
        order = {
            "ketua himpunan": 1, "wakil ketua himpunan": 2,
            "sekretaris jendral": 3, "sekretaris jenderal": 3,
            "sekretaris": 4, "sekretaris 1": 4, "sekretaris 2": 5,
            "bendahara": 6, "bendahara 1": 6, "bendahara 2": 7
        }
        return order.get(jab, 10)
    elif "baleg" in menu_label.lower():
        order = {
            "ketua baleg": 1, "ketua badan legislatif": 1, "wakil ketua legislatif": 2,
            "sekretaris": 3, "sekretaris legislatif": 3, "bendahara legislatif": 4
        }
        return order.get(jab, 10)
    elif "senator" in menu_label.lower():
        order = {
            "senator": 1, "wakil senator": 2, "sekretaris senator": 3, "sekretaris": 3, "bendahara senator": 4
        }
        return order.get(jab, 10)
    else:
        # Departemen: Kadep -> Sekdep -> Bendahara
        order = {
            "kepala departement": 1, "kepala departemen": 1, "wakil kepala departemen": 2,
            "sekretaris departemen": 3, "sekretaris": 3, "sekretaris 1": 3, "sekretaris 2": 4,
            "bendahara departemen": 5, "bendahara": 5
        }
        return order.get(jab, 10)


# Urutan jabatan di dalam Divisi: Kadiv -> Wakil Kadiv -> Staff Ahli -> Anggota/Staff
def jabatan_sort_key_divisi(member):
    jab = member.get("jabatan", "").lower().strip()
    if "kepala divisi" in jab or "kepala komisi" in jab or "kepala biro" in jab:
        return 1
    if "wakil kepala divisi" in jab or "wakil kepala komisi" in jab or "wakil biro" in jab:
        return 2
    if "sekretaris divisi" in jab or "sekretaris komisi" in jab or "sekretaris biro" in jab:
        return 3
    if "staff ahli" in jab:
        return 4
    if "anggota" in jab or "staff" in jab:
        return 5
    return 6


def get_divisions_for_dept(menu_label):
    """
    Mengambil struktur divisi dari departemen yang dipilih.
    Mengembalikan (has_pimpinan, pimpinan_label, unique_divs)
    """
    dept_name = DEPT_MAP.get(menu_label, "")
    members = [m for m in data_anggota if m.get("departemen") == dept_name]
    has_pimpinan = any(not m.get("divisi", "").strip() for m in members)

    unique_divs = []
    for m in members:
        d = m.get("divisi", "").strip()
        if d and d not in unique_divs:
            unique_divs.append(d)

    if "baleg" in menu_label.lower():
        pimpinan_label = "Pimpinan Baleg"
    elif "senator" in menu_label.lower():
        pimpinan_label = "Pimpinan Senator"
    elif "kesekjenan" in menu_label.lower():
        pimpinan_label = "BPH Kesekjenan"
    else:
        pimpinan_label = "Pimpinan Departemen"

    return has_pimpinan, pimpinan_label, unique_divs


# ========================================================================
# DATA DINAMIS: foto massal, kesan, pesan — unik per pemilik buku kating
# ========================================================================
PEMILIK = "Mojes"  # <-- GANTI SESUAI NAMA PEMILIK BUKU KATING INI

@st.cache_data
def load_dinamis_data(pemilik_nama):
    dinamis_filename = pemilik_nama.lower().strip().replace(" ", "_") + ".json"
    dinamis_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data", "data_dinamis", dinamis_filename)
    if not os.path.exists(dinamis_path):
        # Fallback case-sensitivity
        dinamis_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data", "Data_dinamis", dinamis_filename)
        if not os.path.exists(dinamis_path):
            return {}
    with open(dinamis_path, "r", encoding="utf-8") as f:
        all_data = json.load(f)
    # Cari data milik pemilik ini, buat lookup dict: nama_kating / id / nim -> item
    for entry in all_data:
        if entry.get("pemilik", "").strip().lower() == pemilik_nama.strip().lower():
            return {str(item.get("nama_kating", "")).strip().lower(): item for item in entry.get("data", [])}
    # Jika pemilik tidak persis cocok tetapi hanya ada 1 entry di file
    if len(all_data) == 1 and "data" in all_data[0]:
        return {str(item.get("nama_kating", "")).strip().lower(): item for item in all_data[0].get("data", [])}
    return {}

dinamis_map = load_dinamis_data(PEMILIK)


def build_data_for_dept(members):
    """
    Konversi data JSON ke format gambar_urls & data_list
    yang sesuai dengan display_images_with_data().
    Foto, kesan, dan pesan diambil dari json dinamis
    berdasarkan nama kating. Jika foto belum ada, pakai foto default.
    """
    default_foto = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"

    gambar_urls = []
    data_list = []

    for m in members:
        nama_asli = m.get("nama", "")
        # Lookup dinamis berdasarkan nama kating (case insensitive)
        nama_lower = nama_asli.lower().strip()
        mid = str(m.get('id', ''))
        dinamis = dinamis_map.get(nama_lower)
        if not dinamis and mid in dinamis_map:
            dinamis = dinamis_map[mid]
        if not dinamis:
            for k_name, k_data in dinamis_map.items():
                if len(k_name) >= 5 and (k_name in nama_lower or nama_lower.startswith(k_name)):
                    dinamis = k_data
                    break
        if not dinamis:
            dinamis = {}

        # Gunakan foto massal jika tersedia, fallback ke foto default
        gdrive_id = dinamis.get("foto_massal_gdrive_id", "")
        if gdrive_id:
            foto_url = f"https://drive.google.com/uc?export=view&id={gdrive_id}"
        else:
            foto_url = default_foto
        gambar_urls.append(foto_url)

        hobi_list = m.get("hobi", [])
        hobi_str = ", ".join(hobi_list) if hobi_list else "-"

        data_list.append({
            "nama": nama_asli or "-",
            "jabatan": m.get("jabatan", "") or "-",
            "divisi": m.get("divisi", "") or "-",
            "nim": m.get("nim", "") or "-",
            "umur": str(m.get("umur", "")) if m.get("umur") else "-",
            "asal": m.get("asal", "") or "-",
            "alamat": m.get("alamat", "") or "-",
            "hobbi": hobi_str,
            "sosmed": m.get("sosial_media", "") or "-",
            # Prioritas: data dinamis -> data statis JSON -> default "-"
            "kesan": dinamis.get("kesan", "") or m.get("kesan", "") or "-",
            "pesan": dinamis.get("pesan", "") or m.get("pesan", "") or "-",
        })

    return gambar_urls, data_list


def render_department_page(menu_label):
    """
    Merender halaman departemen dengan fitur kategorisasi divisi yang elok:
    1. Filter sub-menu divisi (Hitam Oren)
    2. Header pemisah kategori per divisi
    3. Urutan kating hierarkis (Kadep -> Sekdep, lalu Kadiv -> Anggota)
    """
    dept_name = DEPT_MAP.get(menu_label, "")
    dept_members = [m for m in data_anggota if m.get("departemen") == dept_name]
    has_pimpinan, pimpinan_label, unique_divs = get_divisions_for_dept(menu_label)

    def get_cat_icon(cat_name):
        cat_lower = cat_name.lower()
        if "pimpinan" in cat_lower or "bph" in cat_lower:
            return "🏛️ "
        if "komisi" in cat_lower or "legislasi" in cat_lower:
            return "📜 "
        if "biro" in cat_lower:
            return "📁 "
        if "wirausaha" in cat_lower or "bisnis" in cat_lower:
            return "💼 "
        if "mitra" in cat_lower:
            return "🤝 "
        if "kader" in cat_lower or "psda" in cat_lower or "mutu" in cat_lower:
            return "🌱 "
        if "kreatif" in cat_lower or "media" in cat_lower or "desain" in cat_lower:
            return "🎨 "
        if "bakat" in cat_lower or "minat" in cat_lower or "olahraga" in cat_lower:
            return "🏆 "
        if "riset" in cat_lower or "research" in cat_lower or "akademik" in cat_lower:
            return "🔬 "
        if "eksternal" in cat_lower or "luar" in cat_lower or "masyarakat" in cat_lower:
            return "🌐 "
        if "internal" in cat_lower or "harmonis" in cat_lower or "rohani" in cat_lower:
            return "✨ "
        return "📂 "

    all_label = "Semua"
    if unique_divs:
        if "baleg" in menu_label.lower():
            all_label = "Semua Komisi"
        elif "senator" in menu_label.lower():
            all_label = "Semua Biro"
        else:
            all_label = "Semua Divisi"

        divisi_options = [all_label]
        if has_pimpinan:
            divisi_options.append(pimpinan_label)
        divisi_options.extend(unique_divs)

        selected_cat = divisi_menu(divisi_options, menu_label)
    else:
        selected_cat = all_label

    # Kasus departemen tanpa sub-divisi (misal Kesekjenan)
    if not unique_divs:
        pim_members = [m for m in dept_members if not m.get("divisi", "").strip()]
        pim_members.sort(key=lambda m: jabatan_sort_key_pimpinan(m, menu_label))
        urls, data_items = build_data_for_dept(pim_members)
        display_images_with_data(urls, data_items, show_finished_message=True)
        return

    # Siapkan daftar kategori yang akan ditampilkan
    categories_to_show = []
    if selected_cat == all_label:
        if has_pimpinan:
            categories_to_show.append((pimpinan_label, True))
        for d in unique_divs:
            categories_to_show.append((d, False))
    elif selected_cat == pimpinan_label:
        categories_to_show.append((pimpinan_label, True))
    else:
        categories_to_show.append((selected_cat, False))

    # Tampilkan per kategori
    for idx, (cat_name, is_pimpinan) in enumerate(categories_to_show):
        if is_pimpinan:
            members = [m for m in dept_members if not m.get("divisi", "").strip()]
            members.sort(key=lambda m: jabatan_sort_key_pimpinan(m, menu_label))
        else:
            members = [m for m in dept_members if m.get("divisi", "").strip() == cat_name]
            members.sort(key=jabatan_sort_key_divisi)

        if not members:
            continue

        icon = get_cat_icon(cat_name)
        st.markdown(f"""
        <div class='division-banner'>
            <span class='division-banner-title'>{icon}{cat_name}</span>
            <span class='division-banner-badge'>{len(members)} Anggota</span>
        </div>
        """, unsafe_allow_html=True)

        urls, data_items = build_data_for_dept(members)
        is_last = (idx == len(categories_to_show) - 1)
        display_images_with_data(urls, data_items, show_finished_message=is_last)


# ===== RENDER BERDASARKAN MENU YANG DIPILIH =====

if menu == "Kesekjenan":
    def kesekjenan():
        render_department_page("Kesekjenan")
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        render_department_page("Baleg")
    baleg()

elif menu == "Senator":
    def senator():
        render_department_page("Senator")
    senator()

elif menu == "Departemen PSDA":
    def psda():
        render_department_page("Departemen PSDA")
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        render_department_page("Departemen MIKFES")
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        render_department_page("Departemen Eksternal")
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        render_department_page("Departemen Internal")
    internal()

elif menu == "Departemen SSD":
    def ssd():
        render_department_page("Departemen SSD")
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        render_department_page("Departemen Medkraf")
    medkraf()

elif menu == "Departemen MINBAK":
    def minbak():
        render_department_page("Departemen MINBAK")
    minbak()
