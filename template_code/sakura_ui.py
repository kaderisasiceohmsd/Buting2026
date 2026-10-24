import base64
from concurrent.futures import ThreadPoolExecutor
import html
from io import BytesIO
import json
import os
import re
from PIL import Image, ImageOps
import requests
import streamlit as st
from streamlit_option_menu import option_menu

# ==============================================================================
# 1. PATH & STATIC DATA LOADER (KELOMPOK 02 JACOBI PRIORITIZED)
# ==============================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_JSON_PATH = os.path.join(BASE_DIR, "data_kating_statis.json")
JSON_PATH = STATIC_JSON_PATH

DEPARTMENT_META = {
    "Kesekjenan": {
        "json_dept": "Kesekjenan",
        "title": "Kesekjenan HMSD Adyatama",
        "jp": " • Badan Pengurus Harian",
        "desc": "Jantung koordinasi, administrasi kesekretariatan, dan pengelolaan kebendaharaan HMSD Adyatama ITERA 2026.",
        "icon": "award-fill",
    },
    "Baleg": {
        "json_dept": "Badan Legislatif (BALEG)",
        "title": "Badan Legislatif (BALEG)",
        "jp": " • Komisi Legislasi, Pengawasan & Aspirasi",
        "desc": "Lembaga legislatif mahasiswa yang merumuskan regulasi, mengawasi jalannya roda organisasi, dan mengawal aspirasi.",
        "icon": "bank2",
    },
    "Senator": {
        "json_dept": "Badan Kesenatoran (BASON)",
        "title": "Badan Kesenatoran (BASON)",
        "jp": " • Aspirasi, Kajian Strategis & Kesekretariatan",
        "desc": "Representasi mahasiswa Sains Data di tingkat KM ITERA dalam menyerap aspirasi dan mengkaji isu strategis.",
        "icon": "megaphone-fill",
    },
    "Departemen PSDA": {
        "json_dept": "Pengembangan Sumber Daya Anggota (PSDA)",
        "title": "Departemen Pengembangan Sumber Daya Anggota (PSDA)",
        "jp": " • Kaderisasi & Peningkatan Mutu Anggota",
        "desc": "Garda terdepan pembinaan karakter, kaderisasi, dan pengembangan potensi anggota HMSD Adyatama.",
        "icon": "people-fill",
    },
    "Departemen MIKFES": {
        "json_dept": "Akademik dan Keprofesian (MIKFES)",
        "title": "Departemen Akademik & Keprofesian (MIKFES)",
        "jp": " • PSD, PIKA & Research Development",
        "desc": "Wadah pengembangan kompetensi akademik, keprofesian sains data, serta riset dan inovasi mahasiswa.",
        "icon": "mortarboard-fill",
    },
    "Departemen Eksternal": {
        "json_dept": "Eksternal",
        "title": "Departemen Eksternal",
        "jp": " • Hubungan Luar & Pengabdian Masyarakat",
        "desc": "Jembatan diplomasi relasi eksternal himpunan serta pengabdian nyata bagi masyarakat luas.",
        "icon": "globe2",
    },
    "Departemen Internal": {
        "json_dept": "Internal",
        "title": "Departemen Internal",
        "jp": " • Keharmonisasian & Kerohanian",
        "desc": "Penjaga kehangatan kekeluargaan, keharmonisan antaranggota, dan nilai spiritual di HMSD Adyatama.",
        "icon": "heart-fill",
    },
    "Departemen SSD": {
        "json_dept": "Storage Sains Data (SSD)",
        "title": "Departemen Storage Sains Data (SSD)",
        "jp": " • Kemitraan & Kewirausahaan",
        "desc": "Motor kemandirian finansial, pengembangan kewirausahaan kreatif, dan kemitraan strategis himpunan.",
        "icon": "graph-up-arrow",
    },
    "Departemen Medkraf": {
        "json_dept": "Media Kreatif (MEDKRAF)",
        "title": "Departemen Media Kreatif (MEDKRAF)",
        "jp": " • Dokumentasi, Media Konten & Visual Design",
        "desc": "Pusat wajah visual, dokumentasi momen berharga, dan pengelolaan informasi kreatif HMSD Adyatama.",
        "icon": "palette-fill",
    },
    "Departemen MINBAK": {
        "json_dept": "Minat dan Bakat (MINBAK)",
        "title": "Departemen Minat dan Bakat (MINBAK)",
        "jp": " • Manajemen Aktivitas, Kompetisi & Bakat",
        "desc": "Ruang ekspresi olahraga, seni, kompetisi, dan penyaluran minat bakat mahasiswa Sains Data.",
        "icon": "trophy-fill",
    },
}

# Canonical Kelompok 02 Jacobi ordering per department (Division-grouped order matching Jacobi's photo shoots)
JACOBI_DEPT_ORDER = {
    "Kesekjenan": [
        "Ginda Fajar Riadi Marpaung",
        "Muhammad Aqil Ramadhan",
        "Efi Defiyati",
        "Qois Olifio",
        "Hafsa Fazila Arradhi",
        "Luthfia Laila Ramadhani",
    ],
    "Baleg": [
        "Ridho Benedictus Togi Manik",
        "Juesi Apridelia Saragih",
        "Dharu Cahyoaji Sasongko",
        "Givaro Ananta",
        "Gh Mikael Niko A S",
        "Siti Sarifah Sumamah",
        "Afghanis Nursholehatunnisa",
        "Hani Qurrota Aini",
        "Jeremia Halim",
        "Monica Patricia Tanjung",
        "Jona Timothy Ogatse Panjaitan",
        "Sekar Dini Widya Putri",
        "Wan Nashwa Alhasni Yuska",
    ],
    "Senator": [
        "Fathinah Nur Azizah",
        "Helmy Surya Pratama",
        "Lia Hana Ichisasmita",
        "Nadya Ratu Anjani",
        "Fernando Dimetrius Barus",
        "Suci Aulia",
        "Wielman Itolo Halawa",
        "Aqila Zayyan Salsabil",
        "Hazel Mahesa Handhaka",
        "Dwi Rahma Fitriani",
    ],
    "Departemen PSDA": [
        "Arienta Khusnul Ananda",
        "Vany Salsabila Putri",
        "Nobel Nizam Fathirizki",
        "Desman Velius Halawa",
        "Afriza Azmi",
        "Ayake Alfatih Ramadan",
        "Caesar Ozora Alrando",
        "Euodia Meiliana Friedita",
        "Haikal Seventino Tamba",
        "Putri Manna Anantama Simbolon",
        "Queenta Thifaal Nabila",
        "Azzelya Thianandry",
        "Charrlindah",
        "Jeremi Marolop P. Situmorang",
        "Nabila Nur Azizah",
        "Rafli Al Mansyah Tambunan",
        "Salavia Naharani",
    ],
    "Departemen MIKFES": [
        "Fabio Banyu Cyto",
        "Tanty Widiyastuti",
        "Fadil Prasetyo Alfarizzi",
        "Akeyla Fairuz Shafi",
        "Razin Hafid Hamdi",
        "Manuel Frederika",
        "Ni Made Okta Viola Darma Putri",
        "Risa Romadona",
        "Vannisa Ramadhani",
        "Yulia Kristine Malau",
        "Elsa Sitorus",
        "Fadya Izzatul 'Aini",
        "Lovianora Saragih",
        "M. Alsi Syahrulloh",
        "Sherena Florencia",
        "Faiza Try Anjani",
        "Gathfan Nadif Ali",
        "Hafidz Wahdiansyah",
        "Kaleb Filbert Istel",
        "Melva Shaprina Febrianti",
        "Muhammad Syafiqul Falakh",
        "Rifky Henry Ferdianto",
    ],
    "Departemen Eksternal": [
        "Arini Puteri Elandra",
        "Nabyla Sharfina",
        "Khoirul Muttoharoh",
        "Aditya Taufiqurrohman",
        "Indah Khairunnisa",
        "Bima Ekayasa",
        "Ahmad Bimo Akbar Arkana",
        "Adinda Deswita Maharani",
        "Yollanda Agustina",
        "Riska Erlis Dayu Tiara",
        "Alfaya Abiyyi",
        "Asri Meilani",
        "Ahmad Rizky",
        "Selma Siti Aisyah",
        "Ashila Islamisahfa Vanisha",
        "Fathya Intami Gusda",
        "Tarisya Hidayatul Rahmi",
        "Danil N Fadillah",
        "Favian Arkaanda",
        "Muhammad Fathiy Zumar Yazid",
        "Muhammad Rizaldi",
        "Saskia Nova Magdalena",
    ],
    "Departemen Internal": [
        "Haikal Fransisko Simbolon",
        "Kharisma Mustika Sari",
        "Hanna Gresia Sinaga",
        "Muhammad Hanif Dzaky Arifin",
        "Ahmad Farhan Ghani",
        "Aisyah Khairun Nisa",
        "Cerine Sihotang",
        "Jaya Saputra Tamba",
        "Najla Nursyifa",
        "Rozak Ramdani",
        "Teresa Christiani Purba",
        "Audina Fitria",
        "Cika Adelia Br Marbun",
        "Gustin Haleluya Tampubolon",
        "Muhammad Harvinsyah",
        "Rafa Sabina Fahimah",
    ],
    "Departemen SSD": [
        "Ihsan Maulana Yusuf",
        "Hanifah Inaya Sani",
        "Afifah Fauziah",
        "Anadia Carana",
        "Hasan Nur Ramadhan",
        "Layina Ropiqo",
        "Mochammad Iqbal Az-Zahir",
        "Talitha Justine",
        "Abdillah Fikri Al Pome",
        "Afdhal Rahmad Setiawan",
        "Anggun Nita",
        "Della Anisa Fitri",
    ],
    "Departemen Medkraf": [
        "Nayla Salsabila Fathianisa",
        "Donna Maya Puspita",
        "Labo John Noel Napitupulu",
        "Sania Dwi Ayu Lestari",
        "Raihana Adelia Putri",
        "Anash Tasya Ausyaqila",
        "Felisya Nabila Putri Nugroho",
        "Muhammad Razan Maulana Pratama",
        "Allisha",
        "Alya Ramadhanti",
        "Bunga Clarisa Sefa",
        "Difanya Husakina",
        "Nazlah Auliya",
        "Daffa Kharisma Adzana",
        "Edsel Adya Pradipta",
        "Lucia Advencia Rachel Nainggolan",
        "Shafa Delaila Azzahra",
        "Zannuba Arifah Ilman",
    ],
    "Departemen MINBAK": [
        "Kevin Antonio Junior",
        "Gusti Putu Ferazka Dhiyamika",
        "Ali Aristo Muthahhari Parisi",
        "Muhammad Ridwan",
        "Ayu Andriani Parlina Wati",
        "Dafa Elpriza",
        "Salsabila Nazwa Putri",
        "Muhammad Afdal Lutfi",
        "Juwita Sari",
        "Andra Ilham Bintang",
        "Bryan Paskah Telaumbanua",
        "Ghiyats Thabularasa Meardhy",
        "Indah Julia Mawar Pratiwi",
        "Jacinda Kesya Alvara",
        "Muhammad Rafka Fatih Al Ghathfaan",
    ],
}


def _norm(text):
    if not text:
        return ""
    return re.sub(r"[^a-z0-9]", "", str(text).lower())


@st.cache_data(show_spinner=False)
def load_static_database():
    if os.path.exists(STATIC_JSON_PATH):
        with open(STATIC_JSON_PATH, encoding="utf-8") as f:
            dept_ordered = json.load(f)
    elif os.path.exists(JSON_PATH):
        with open(JSON_PATH, encoding="utf-8") as f:
            dept_ordered = json.load(f)
    else:
        dept_ordered = {}

    by_name = {}
    by_nim = {}
    for dept_name, entries in dept_ordered.items():
        for item in entries:
            clean = {
                "nama": item.get("nama", "").strip(),
                "nim": str(item.get("nim", "")).strip(),
                "umur": item.get("umur", "-"),
                "asal": item.get("asal", "-"),
                "alamat": item.get("alamat", "-"),
                "hobbi": item.get("hobbi", item.get("hobi", "-")),
                "hobi": item.get("hobbi", item.get("hobi", "-")),
                "sosmed": item.get("sosmed", "-"),
                "jabatan": item.get("jabatan", ""),
                "divisi": item.get("divisi", dept_name),
                "departemen": dept_name,
            }
            if clean["nama"]:
                by_name[_norm(clean["nama"])] = clean
            if clean["nim"]:
                by_nim[clean["nim"]] = clean

    return {
        "by_name": by_name,
        "by_nim": by_nim,
        "dept_ordered": dept_ordered,
    }


def get_canonical_dept_data(menu_key):
    """Returns a fresh list of dicts with static data + empty kesan/pesan for a department."""
    db = load_static_database()
    items = db["dept_ordered"].get(menu_key, [])
    result = []
    for item in items:
        d = dict(item)
        d["kesan"] = "-"
        d["pesan"] = "-"
        result.append(d)
    return result


def resolve_member_data_list(data_list, departemen=None, target_count=None):
    """
    Merges static data (1-for-all from data_kating_statis.json)
    with each member's personal kesan & pesan and photo ordering.
    """
    db = load_static_database()
    canonical = db["dept_ordered"].get(departemen, []) if departemen else []
    by_name = db.get("by_name", {})

    if not data_list:
        data_list = []

    total = target_count if target_count is not None else max(len(data_list), len(canonical))
    resolved = []

    for i in range(total):
        raw_item = data_list[i] if i < len(data_list) else {}
        raw_name = str(raw_item.get("nama", "")).strip()

        matched_entry = by_name.get(_norm(raw_name)) if raw_name else None
        if not matched_entry:
            matched_entry = canonical[i] if i < len(canonical) else {}

        merged = dict(matched_entry)

        kesan = str(raw_item.get("kesan", "")).strip()
        pesan = str(raw_item.get("pesan", "")).strip()

        merged["kesan"] = kesan if kesan and kesan != "." else "Kakaknya sangat ramah, humble, dan menginspirasi!"
        merged["pesan"] = pesan if pesan and pesan != "." else "Semangat terus kuliah dan menjalankan amanahnya di HMSD!"
        resolved.append(merged)

    return resolved


# ==============================================================================
# 2. IMAGE LOADING & FAST PARALLEL BASE64 CONVERTER
# ==============================================================================
def normalize_drive_url(url):
    if not url:
        return ""
    url = url.strip()
    # Fix "https://drive.google.com/uc?export=1XNSX..." -> "https://drive.google.com/uc?export=view&id=1XNSX..."
    m = re.match(r"https://drive\.google\.com/uc\?export=([A-Za-z0-9_-]{15,})$", url)
    if m:
        return f"https://drive.google.com/uc?export=view&id={m.group(1)}"
    return url


def extract_drive_id(url):
    if not url:
        return None
    m = re.search(r"[?&]id=([A-Za-z0-9_-]{15,})", url)
    if m:
        return m.group(1)
    m2 = re.search(r"/d/([A-Za-z0-9_-]{15,})", url)
    if m2:
        return m2.group(1)
    return None


@st.cache_data(show_spinner=False, ttl=3600)
def fetch_image_bytes(url, resize_dim=(360, 460)):
    norm_url = normalize_drive_url(url)
    file_id = extract_drive_id(norm_url)
    candidate_urls = [norm_url]
    if file_id:
        candidate_urls.append(f"https://lh3.googleusercontent.com/d/{file_id}=w800")

    for u in candidate_urls:
        try:
            resp = requests.get(u, timeout=10)
            if resp.status_code == 200 and len(resp.content) > 500:
                img = Image.open(BytesIO(resp.content))
                img = ImageOps.exif_transpose(img)
                if img.mode not in ("RGB", "RGBA"):
                    img = img.convert("RGB")
                if resize_dim:
                    img = ImageOps.fit(img, resize_dim, Image.Resampling.LANCZOS)
                buf = BytesIO()
                if img.mode == "RGBA":
                    img.save(buf, format="PNG")
                else:
                    img.save(buf, format="JPEG", quality=86, optimize=True)
                return base64.b64encode(buf.getvalue()).decode("utf-8")
        except Exception:
            continue
    return None


def create_fallback_pil_image():
    try:
        from PIL import ImageDraw
        img = Image.new("RGBA", (400, 400), (255, 240, 245, 255))
        draw = ImageDraw.Draw(img)
        draw.rectangle([(10, 10), (390, 390)], outline=(245, 194, 215, 255), width=4)
        return img
    except Exception:
        return Image.new("RGBA", (300, 300), (255, 240, 245, 255))


@st.cache_data(show_spinner=False, ttl=3600)
def load_image(url):
    if not url:
        return create_fallback_pil_image()

    # 1. Check if url is a local file path
    if os.path.exists(url):
        try:
            img = Image.open(url)
            return ImageOps.exif_transpose(img)
        except Exception:
            pass

    # 2. Check in assets folder if basename exists
    assets_path = os.path.join(BASE_DIR, "assets", os.path.basename(url))
    if os.path.exists(assets_path):
        try:
            img = Image.open(assets_path)
            return ImageOps.exif_transpose(img)
        except Exception:
            pass

    # 3. Check Google Drive / Web URL
    norm_url = normalize_drive_url(url)
    file_id = extract_drive_id(norm_url)
    candidate_urls = [norm_url]
    if file_id:
        candidate_urls.append(f"https://lh3.googleusercontent.com/d/{file_id}=w1000")
    for u in candidate_urls:
        try:
            response = requests.get(u, timeout=8)
            if response.status_code == 200 and len(response.content) > 500:
                img = Image.open(BytesIO(response.content))
                return ImageOps.exif_transpose(img)
        except Exception:
            continue

    # 4. Safe fallback: return valid PIL Image so st.image NEVER crashes with None
    return create_fallback_pil_image()


@st.cache_data(show_spinner=False, ttl=3600)
def fetch_batch_b64(urls, resize_dim=(360, 460)):
    if not urls:
        return []
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda u: fetch_image_bytes(u, resize_dim), urls))
    return results


def get_placeholder_svg_b64(label="Sakura Portrait"):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="360" height="460" viewBox="0 0 360 460">
    <defs>
      <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#FFE4EE"/>
        <stop offset="100%" stop-color="#F8BBD0"/>
      </linearGradient>
    </defs>
    <rect width="360" height="460" fill="url(#g)"/>
    <circle cx="180" cy="190" r="65" fill="#FFF8FA" opacity="0.85"/>
    <text x="180" y="208" font-size="48" text-anchor="middle" fill="#D85A7F">🌸</text>
    <text x="180" y="310" font-family="sans-serif" font-size="16" font-weight="600" text-anchor="middle" fill="#6D2E46">{html.escape(label)}</text>
    <text x="180" y="335" font-family="sans-serif" font-size="12" text-anchor="middle" fill="#9E5872">02 Jacobi • HMSD 2026</text>
    </svg>"""
    return base64.b64encode(svg.encode("utf-8")).decode("utf-8")


# ==============================================================================
# 3. SAKURA AESTHETIC CSS & FLOATING PETALS
# ==============================================================================
def inject_sakura_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=Noto+Serif+JP:wght@500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

        :root {
            --sakura-bg: #FFF9FB;
            --sakura-soft: #FDF0F5;
            --sakura-petal: #FCE4EC;
            --sakura-border: #F5C2D7;
            --sakura-rose: #D85A7F;
            --sakura-deep: #9E3356;
            --sakura-ink: #3A1F2B;
            --sakura-muted: #7A495D;
            --sakura-gold: #C89B3C;
        }

        .stApp {
            background: #FFF9FB;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: var(--sakura-ink);
        }

        /* Sidebar Styling (Preserve Material Symbols Rounded icon ligatures!) */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #FFF3F7 0%, #FCE6EE 100%) !important;
            border-right: 1px solid #F5C6D8 !important;
        }
        section[data-testid="stSidebar"] [data-testid="stSidebarNavLink"] span:not([data-testid="stIconMaterial"]) {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600;
        }
        span[data-testid="stIconMaterial"], .material-icons {
            font-family: 'Material Symbols Rounded' !important;
        }
        [data-testid="stImage"] {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            text-align: center !important;
            width: 100% !important;
            margin: 0 auto !important;
        }
        [data-testid="stImage"] > div {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            text-align: center !important;
            width: 100% !important;
            margin: 0 auto !important;
        }
        [data-testid="stImage"] img {
            max-width: 330px !important;
            width: auto !important;
            height: auto !important;
            margin: 0 auto !important;
            display: block !important;
            border-radius: 8px !important;
        }

        /* Centered Header Logo Wrapper (Matches Foto Kelompok 330px & stays centered on zoom-out) */
        .sakura-header-logo-card {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 6px auto !important;
            max-width: 330px !important;
            width: 100% !important;
            text-align: center !important;
        }
        .sakura-header-logo-card img {
            width: 100% !important;
            max-width: 330px !important;
            max-height: 330px !important;
            height: auto !important;
            object-fit: contain !important;
            margin: 0 auto !important;
            display: block !important;
            border-radius: 8px !important;
        }

        /* Lightweight Sakura Theme: Animasi dimatikan agar hemat performa & cepat dimuat */

        /* Hero Banner on Halaman Utama */
        .sakura-hero-box {
            position: relative;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.92) 0%, rgba(255, 238, 244, 0.94) 100%);
            border: 1.5px solid #F5C2D7;
            border-radius: 28px;
            padding: 36px 28px 28px 28px;
            text-align: center;
            box-shadow: 0 18px 45px rgba(180, 65, 102, 0.09);
            margin-bottom: 24px;
            overflow: hidden;
        }
        .sakura-crest-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: linear-gradient(90deg, #FCE4EC 0%, #FFF0F5 50%, #FCE4EC 100%);
            border: 1px solid #F2ACC6;
            color: #9E3356;
            padding: 6px 18px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            margin-bottom: 12px;
        }
        .sakura-main-title {
            font-family: 'Cormorant Garamond', 'Noto Serif JP', serif !important;
            font-size: clamp(2.8rem, 5.2vw, 4.7rem) !important;
            font-weight: 700 !important;
            color: #3A1F2B !important;
            line-height: 1.06 !important;
            margin: 4px 0 8px 0 !important;
            letter-spacing: 0.03em;
        }
        .sakura-subtitle {
            font-size: clamp(1.1rem, 2vw, 1.5rem);
            font-weight: 600;
            color: #B23A5E;
            letter-spacing: 0.06em;
            margin-bottom: 6px;
        }
        .sakura-jp-caption {
            font-family: 'Noto Serif JP', serif;
            font-size: 0.9rem;
            color: #8C5368;
            letter-spacing: 0.16em;
        }

        /* Dual Emblem Logo Showcase */
        .sakura-logo-showcase {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 36px;
            flex-wrap: wrap;
            margin: 22px auto 10px auto;
            padding: 20px 30px;
            max-width: 640px;
            background: rgba(255, 255, 255, 0.85);
            border: 1px solid #F5C6D8;
            border-radius: 22px;
            box-shadow: 0 10px 28px rgba(216, 90, 127, 0.08);
        }
        .sakura-logo-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
        }
        .sakura-logo-item img {
            height: 130px;
            width: auto;
            object-fit: contain;
            filter: drop-shadow(0 6px 14px rgba(158, 51, 86, 0.12));
            transition: transform 0.3s ease;
        }
        .sakura-logo-item img:hover {
            transform: scale(1.06);
        }
        .sakura-logo-label {
            font-size: 0.78rem;
            font-weight: 700;
            color: #8C4660;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }
        .sakura-logo-divider {
            width: 1.5px;
            height: 85px;
            background: linear-gradient(180deg, transparent, #F2ACC6, transparent);
        }

        /* Group Panorama Frame (Home Tab) */
        .sakura-panorama-card {
            background: #FFFFFF;
            border: 2px solid #F5C2D7;
            border-radius: 8px;
            padding: 12px;
            box-shadow: 0 14px 36px rgba(178, 58, 94, 0.10);
            margin: 10px auto 22px auto;
            max-width: 540px;
            position: relative;
        }
        .sakura-panorama-card img {
            width: 100%;
            max-height: 330px;
            object-fit: contain;
            background: #FFF5F8;
            border-radius: 8px;
            display: block;
        }
        .sakura-panorama-caption {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
            padding: 10px 8px 2px 8px;
        }
        .sakura-panorama-tag {
            background: linear-gradient(135deg, #D85A7F 0%, #B23A5E 100%);
            color: #FFFFFF;
            font-size: 0.8rem;
            font-weight: 700;
            padding: 6px 16px;
            border-radius: 999px;
            letter-spacing: 0.06em;
        }

        /* Description Card on Home Tab */
        .sakura-editorial-card {
            background: linear-gradient(145deg, rgba(255,255,255,0.96) 0%, rgba(255,242,247,0.96) 100%);
            border: 1.5px solid #F5C2D7;
            border-radius: 24px;
            padding: 32px 34px;
            box-shadow: 0 14px 36px rgba(178, 58, 94, 0.08);
            max-width: 880px;
            margin: 0 auto 24px auto;
        }
        .sakura-section-heading {
            font-family: 'Cormorant Garamond', serif !important;
            font-size: 2.3rem !important;
            font-weight: 700 !important;
            color: #3A1F2B !important;
            margin-bottom: 6px !important;
            text-align: center;
        }
        .sakura-pillar-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin-top: 22px;
        }
        .sakura-pillar-box {
            background: #FFF8FA;
            border: 1px solid #F5C6D8;
            border-radius: 16px;
            padding: 18px 20px;
            text-align: left;
        }
        .sakura-pillar-title {
            font-weight: 700;
            font-size: 0.98rem;
            color: #9E3356;
            margin-bottom: 6px;
        }
        .sakura-pillar-text {
            font-size: 0.87rem;
            color: #5C3344;
            line-height: 1.55;
        }

        /* POLAROID YEARBOOK GALLERY (About Us - Clean & Lightweight) */
        .sakura-polaroid-card {
            background: #FFFFFF;
            border: 1.5px solid #F3C1D4;
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 20px;
            box-shadow: 0 4px 14px rgba(168, 56, 92, 0.06);
            position: relative;
        }
        .sakura-polaroid-card:hover {
            border-color: #D85A7F;
            box-shadow: 0 6px 18px rgba(216, 90, 127, 0.12);
        }
        .sakura-washi-tape {
            width: 110px;
            height: 22px;
            background: repeating-linear-gradient(
                45deg,
                rgba(248, 187, 208, 0.65),
                rgba(248, 187, 208, 0.65) 8px,
                rgba(255, 235, 242, 0.75) 8px,
                rgba(255, 235, 242, 0.75) 16px
            );
            border: 1px dashed #E888A7;
            border-radius: 4px;
            margin: -26px auto 12px auto;
            position: relative;
            z-index: 2;
        }
        .sakura-polaroid-img-wrap {
            width: 100%;
            aspect-ratio: 4 / 4.3;
            border-radius: 14px;
            overflow: hidden;
            background: #FCE8EF;
            border: 1px solid #F7D2E0;
            position: relative;
        }
        .sakura-polaroid-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        .sakura-role-ribbon {
            position: absolute;
            top: 12px;
            left: 12px;
            padding: 5px 14px;
            border-radius: 999px;
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
        }
        .sakura-role-leader {
            background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
            color: #FFFFFF;
        }
        .sakura-role-member {
            background: linear-gradient(135deg, #D85A7F 0%, #B23A5E 100%);
            color: #FFFFFF;
        }
        .sakura-nim-Floating {
            position: absolute;
            bottom: 10px;
            right: 10px;
            background: rgba(58, 31, 43, 0.90);
            color: #FFF8FA;
            padding: 4px 12px;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 600;
        }
        .sakura-polaroid-name {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.65rem;
            font-weight: 700;
            color: #3A1F2B;
            margin: 14px 0 8px 0;
            text-align: center;
        }
        .sakura-funfact-box {
            background: #FFF5F8;
            border: 1px solid #F6C8DA;
            border-radius: 12px;
            padding: 10px 14px;
            font-size: 0.86rem;
            color: #592B3E;
            margin-bottom: 10px;
            line-height: 1.45;
        }
        .sakura-motto-box {
            background: linear-gradient(90deg, #FCE8EF 0%, #FFF8FA 100%);
            border-left: 3.5px solid #D85A7F;
            border-radius: 0 12px 12px 0;
            padding: 10px 14px;
            font-style: italic;
            font-size: 0.86rem;
            color: #6D2E46;
            line-height: 1.45;
        }

        /* BUKU KATING: Department Banner & Horizontal 2-Column Kating Card */
        .sakura-dept-banner {
            background: linear-gradient(135deg, #FFF0F5 0%, #FCE4EC 60%, #F8BBD0 100%);
            border: 1.5px solid #F2ACC6;
            border-radius: 22px;
            padding: 20px 26px;
            margin: 14px 0 22px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 14px;
            box-shadow: 0 10px 26px rgba(180, 65, 102, 0.08);
        }
        .sakura-dept-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.9rem;
            font-weight: 700;
            color: #3A1F2B;
            margin: 0;
            line-height: 1.15;
        }
        .sakura-dept-sub {
            font-size: 0.86rem;
            color: #7A3E55;
            margin-top: 4px;
        }
        .sakura-dept-count {
            background: #FFFFFF;
            border: 1.5px solid #E888A7;
            color: #9E3356;
            font-weight: 700;
            font-size: 0.86rem;
            padding: 8px 18px;
            border-radius: 999px;
            box-shadow: 0 4px 12px rgba(216, 90, 127, 0.10);
        }

        /* HORIZONTAL KATING CARD (2 Columns per row - Clean & Lightweight) */
        .sakura-kating-card {
            background: #FFFFFF;
            border: 1.5px solid #F4C2D5;
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 18px;
            box-shadow: 0 4px 14px rgba(178, 58, 94, 0.05);
            display: flex;
            flex-direction: column;
            gap: 12px;
            height: 100%;
        }
        .sakura-kating-card:hover {
            border-color: #E57A9E;
            box-shadow: 0 6px 18px rgba(216, 90, 127, 0.10);
        }
        .sakura-kating-top {
            display: flex;
            gap: 16px;
            align-items: flex-start;
        }
        .sakura-kating-photo-col {
            width: 37%;
            min-width: 130px;
            max-width: 168px;
            flex-shrink: 0;
            position: relative;
        }
        .sakura-kating-photo-col img {
            width: 100%;
            aspect-ratio: 3 / 3.85;
            object-fit: cover;
            border-radius: 14px;
            border: 1.5px solid #F6C8DA;
            display: block;
            background: #FCE8EF;
        }
        .sakura-kating-num {
            position: absolute;
            top: 8px;
            left: 8px;
            background: rgba(58, 31, 43, 0.88);
            color: #FFF8FA;
            font-size: 0.7rem;
            font-weight: 700;
            padding: 3px 9px;
            border-radius: 999px;
        }
        .sakura-kating-info-col {
            flex: 1;
            min-width: 0;
        }
        .sakura-kating-name {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.42rem;
            font-weight: 700;
            color: #3A1F2B;
            line-height: 1.18;
            margin: 0 0 6px 0;
        }
        .sakura-badge-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 10px;
        }
        .sakura-chip-nim {
            background: #FCE4EC;
            color: #9E3356;
            border: 1px solid #F3B6CD;
            font-size: 0.73rem;
            font-weight: 700;
            padding: 2px 10px;
            border-radius: 999px;
        }
        .sakura-chip-role {
            background: linear-gradient(135deg, #D85A7F 0%, #B23A5E 100%);
            color: #FFFFFF;
            font-size: 0.72rem;
            font-weight: 600;
            padding: 2px 10px;
            border-radius: 999px;
        }
        .sakura-bio-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 6px 10px;
            background: #FFF9FB;
            border: 1px solid #F8D5E2;
            border-radius: 12px;
            padding: 9px 11px;
            font-size: 0.78rem;
        }
        .sakura-bio-item {
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .sakura-bio-item.full-span {
            grid-column: 1 / -1;
        }
        .sakura-bio-label {
            color: #9E4768;
            font-weight: 700;
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            display: block;
        }
        .sakura-bio-val {
            color: #3A1F2B;
            font-weight: 500;
            line-height: 1.35;
        }
        .sakura-quote-section {
            background: linear-gradient(90deg, #FFF2F6 0%, #FFF9FB 100%);
            border: 1px solid #F6C8DA;
            border-left: 4px solid #D85A7F;
            border-radius: 12px;
            padding: 10px 13px;
            font-size: 0.81rem;
            display: grid;
            grid-template-columns: 1fr;
            gap: 6px;
        }
        .sakura-quote-line {
            color: #4A2535;
            line-height: 1.42;
        }
        .sakura-quote-tag {
            font-weight: 700;
            color: #B23A5E;
        }

        @media (max-width: 640px) {
            .sakura-kating-top {
                flex-direction: column;
            }
            .sakura-kating-photo-col {
                width: 100%;
                max-width: 100%;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ==============================================================================
# 4. SHARED UI COMPONENTS (HALAMAN UTAMA & BUKU KATING)
# ==============================================================================
def render_centered_logo(url):
    """
    Menampilkan logo di tengah secara proporsional dengan ukuran setara Foto Kelompok (max-width: 540px).
    Tetap 100% berada tepat di tengah layar meskipun halaman di-zoom out.
    """
    inject_sakura_css()
    b64 = fetch_image_bytes(url, resize_dim=None)
    if not b64:
        img = load_image(url)
        if img is not None:
            buf = BytesIO()
            if img.mode == "RGBA":
                img.save(buf, format="PNG")
            else:
                img.save(buf, format="JPEG", quality=92)
            b64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    if b64:
        src = f"data:image/png;base64,{b64}"
    else:
        norm = normalize_drive_url(url)
        fid = extract_drive_id(norm)
        src = f"https://lh3.googleusercontent.com/d/{fid}=w800" if fid else norm

    st.markdown(
        f"""
        <div class="sakura-header-logo-card">
            <img src="{src}" alt="Logo">
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sakura_header(url_hmsd, url_psda):
    inject_sakura_css()
    b64_hmsd = fetch_image_bytes(url_hmsd, resize_dim=None)
    b64_psda = fetch_image_bytes(url_psda, resize_dim=None)

    img_hmsd_tag = (
        f'<img src="data:image/jpeg;base64,{b64_hmsd}" alt="Logo HMSD">'
        if b64_hmsd
        else "🌸"
    )
    img_psda_tag = (
        f'<img src="data:image/jpeg;base64,{b64_psda}" alt="Logo PSDA">'
        if b64_psda
        else "🌸"
    )

    st.markdown(
        f"""
        <div class="sakura-hero-box">
            <div class="sakura-crest-pill">🌸 Kelompok 02 Jacobi • Haru no Sakura 🌸</div>
            <h1 class="sakura-main-title">WEBSITE KATING</h1>
            <div class="sakura-subtitle">CEO HMSD Adyatama ITERA 2026</div>
            <div class="sakura-jp-caption">春の桜 • Harmoni Iterasi Menuju Konvergensi</div>
            <div class="sakura-logo-showcase">
                <div class="sakura-logo-item">
                    {img_hmsd_tag}
                    <span class="sakura-logo-label">HMSD Adyatama</span>
                </div>
                <div class="sakura-logo-divider"></div>
                <div class="sakura-logo-item">
                    {img_psda_tag}
                    <span class="sakura-logo-label">Kaderisasi PSDA</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_home_tab(foto_kelompok_url):
    b64_group = fetch_image_bytes(foto_kelompok_url, resize_dim=None)
    if not b64_group:
        b64_group = get_placeholder_svg_b64("Foto Kelompok 02 Jacobi")

    # 1. PERTAMA: FOTO HORIZONTAL KELOMPOK 02 JACOBI (Proporsional & Tidak Terpotong)
    st.markdown(
        f"""
        <div class="sakura-panorama-card">
            <img src="data:image/jpeg;base64,{b64_group}" alt="Foto Kelompok 02 Jacobi">
            <div class="sakura-panorama-caption">
                <span class="sakura-panorama-tag">🌸 KELOMPOK 02 JACOBI</span>
                <span style="font-size: 0.82rem; color: #7A495D; font-weight: 600;">
                    13 Anggota • Kaderisasi CEO HMSD Adyatama ITERA 2026
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. KEDUA (DI BAWAH FOTO HORIZONTAL): DESKRIPSI KELOMPOK (Tanpa Emdash)
    st.markdown(
        """
        <div class="sakura-editorial-card">
            <div style="text-align: center; margin-bottom: 8px;">
                <span class="sakura-crest-pill"> • Deskripsi Kelompok</span>
            </div>
            <h2 class="sakura-section-heading">Filosofi & Identitas Kami</h2>
            <p style="text-align: justify; font-size: 1.02rem; line-height: 1.8; color: #4A2535; margin-top: 14px;">
                <strong>Kelompok 02 Jacobi</strong> mengambil inspirasi dari matematikawan <em>Carl Gustav Jacob Jacobi</em>,
                sosok di balik metode iteratif dalam aljabar linear dan komputasi sains data yang menemukan solusi paling akurat
                melalui langkah-langkah perbaikan yang konsisten. Dipadukan dengan estetika <strong>Bunga Sakura,
                kelompok kami melambangkan semangat bertumbuh bersama: setiap kelopak individu memiliki keunikan karakter, namun ketika mekar
                bersama dalam satu tangkai kekeluargaan, kami menghadirkan harmoni, ketangguhan, dan keindahan yang bermakna.
            </p>
            <p style="text-align: justify; font-size: 1.02rem; line-height: 1.8; color: #4A2535; margin-top: 10px;">
                Di bawah kepemimpinan <strong>Palu (Dandy Romansyah)</strong> dan <strong>Bulu (Dea Febryana)</strong> bersama seluruh
                13 rekan seperjuangan, Kelompok 02 Jacobi berkomitmen menjalani proses kaderisasi <strong>CEO HMSD Adyatama ITERA 2026</strong>
                dengan rasa ingin tahu yang tinggi, solidaritas tanpa batas, serta rasa hormat dan apresiasi kepada seluruh kakak tingkat HMSD Adyatama.
            </p>
            <div class="sakura-pillar-grid">
                <div class="sakura-pillar-box">
                    <div class="sakura-pillar-title">🌸 Iterasi Tanpa Henti</div>
                    <div class="sakura-pillar-text">
                        Sebagaimana algoritma Jacobi, kami percaya bahwa setiap proses belajar dan evaluasi akan membawa kami semakin dekat menuju konvergensi terbaik.
                    </div>
                </div>
                <div class="sakura-pillar-box">
                    <div class="sakura-pillar-title">💮 Harmoni Bunga Sakura</div>
                    <div class="sakura-pillar-text">
                        Satu kelopak mungkin tampak lembut, namun seribu kelopak sakura yang mekar serentak mampu mengubah seluruh musim menjadi penuh warna.
                    </div>
                </div>
                <div class="sakura-pillar-box">
                    <div class="sakura-pillar-title">✨ Solidaritas 13 Karakter</div>
                    <div class="sakura-pillar-text">
                        Menyatukan 13 latar belakang, cerita, dan mimpi yang berbeda menjadi satu keluarga utuh di rumah besar Sains Data ITERA.
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def to_image_data_uri(b64_str):
    if not b64_str:
        return ""
    if b64_str.startswith("PHN2Zy") or b64_str.startswith("PD94bW"):
        return f"data:image/svg+xml;base64,{b64_str}"
    return f"data:image/jpeg;base64,{b64_str}"


def render_polaroid_about_us(gambar_urls, data_list, mentor_data=None):
    # Separate or construct Mentor + Ketua (Palu) + Wakil Ketua (Bulu) + 11 Anggota
    default_mentor = {
        "nama": "Farhanah Hadaya Fatin",
        "sebagai": "Mentor Kelompok 02",
        "nim": "124450026",
        "fun_fact": "Bisa tidur dimana aja kapan aja",
        "motto_hidup": "Risking better than regretting",
        "foto_url": "https://drive.google.com/uc?export=view&id=1CYURN_LuyaB9QmaVCpIStS1VvjfjQksw",
    }
    if not mentor_data:
        mentor_data = default_mentor
    else:
        # Jika mentor_data di halaman_utama masih memakai template generic atau ada field kosong
        if mentor_data.get("nama") in ("Mentor 02 Jacobi", "", None):
            mentor_data["nama"] = default_mentor["nama"]
        if mentor_data.get("nim") in ("124450000", "", "-", None):
            mentor_data["nim"] = default_mentor["nim"]
        if not mentor_data.get("fun_fact"):
            mentor_data["fun_fact"] = default_mentor["fun_fact"]
        if not mentor_data.get("motto_hidup"):
            mentor_data["motto_hidup"] = default_mentor["motto_hidup"]

    mentor_url = str(mentor_data.get("foto_url") or "").strip()
    all_urls = [mentor_url] + list(gambar_urls)
    with st.spinner("🌸 Menyiapkan Digital Photobook 02 Jacobi (Prelude Edition)..."):
        all_b64 = fetch_batch_b64(all_urls, resize_dim=(520, 640))

    mentor_b64 = (
        all_b64[0]
        if all_b64 and all_b64[0]
        else get_placeholder_svg_b64(mentor_data.get("nama", "Mentor"))
    )
    member_b64_list = all_b64[1:] if len(all_b64) > 1 else []

    ketua_item = None
    wakil_item = None
    anggota_items = []

    for idx, m in enumerate(data_list):
        b64_img = (
            member_b64_list[idx]
            if idx < len(member_b64_list) and member_b64_list[idx]
            else get_placeholder_svg_b64(m.get("nama", f"Anggota {idx + 1}"))
        )
        sebagai_raw = str(m.get("sebagai", "Anggota")).strip()
        sebagai_low = sebagai_raw.lower()
        entry = {
            "nama": str(m.get("nama", "-")),
            "sebagai": sebagai_raw,
            "nim": str(m.get("nim", "-")),
            "fun_fact": str(m.get("fun_fact", "-")),
            "motto_hidup": str(m.get("motto_hidup", "-")),
            "img": to_image_data_uri(b64_img),
        }
        if sebagai_low in ("palu", "ketua", "ketua kelompok") and ketua_item is None:
            entry["role_badge"] = "👑 PAK LURAH (PALU)"
            entry["short_role"] = " • PALU"
            entry["tier"] = "leader"
            ketua_item = entry
        elif sebagai_low in ("bulu", "wakil", "wakil ketua") and wakil_item is None:
            entry["role_badge"] = "👑 BU LURAH (BULU)"
            entry["short_role"] = " • BULU"
            entry["tier"] = "leader"
            wakil_item = entry
        else:
            entry["role_badge"] = "🌸 ANGGOTA KELOMPOK 02 JACOBI"
            entry["short_role"] = "ANGGOTA"
            entry["tier"] = "member"
            anggota_items.append(entry)

    if ketua_item is None and anggota_items:
        ketua_item = anggota_items.pop(0)
    if wakil_item is None and anggota_items:
        wakil_item = anggota_items.pop(0)

    mentor_entry = {
        "nama": str(mentor_data.get("nama", "Farhanah Hadaya Fatin")),
        "sebagai": str(mentor_data.get("sebagai", "Mentor Kelompok 02")),
        "nim": str(mentor_data.get("nim", "-")),
        "fun_fact": str(mentor_data.get("fun_fact", "-")),
        "motto_hidup": str(mentor_data.get("motto_hidup", "-")),
        "img": to_image_data_uri(mentor_b64),
        "role_badge": "🌟 MENTOR KELOMPOK 02 JACOBI",
        "short_role": "★ MENTOR ★",
        "tier": "mentor",
    }

    # Order of 14 profiles:
    # 0: Ketua (Top-Left), 1: Mentor (Top-Center Crown), 2: Wakil Ketua (Top-Right)
    # 3..5: Left Wing (3 Anggota), 6..8: Right Wing (3 Anggota), 9..13: Bottom Fan (5 Anggota)
    ordered_profiles = []
    if ketua_item:
        ketua_item["slot"] = "top-left"
        ketua_item["tilt"] = "-3deg"
        ordered_profiles.append(ketua_item)

    mentor_entry["slot"] = "top-center"
    mentor_entry["tilt"] = "0deg"
    ordered_profiles.append(mentor_entry)

    if wakil_item:
        wakil_item["slot"] = "top-right"
        wakil_item["tilt"] = "3deg"
        ordered_profiles.append(wakil_item)

    slot_configs = [
        ("left-1", "-3.5deg"),
        ("left-2", "2deg"),
        ("left-3", "-2.5deg"),
        ("right-1", "3.5deg"),
        ("right-2", "-2deg"),
        ("right-3", "2.5deg"),
        ("bottom-1", "3deg"),
        ("bottom-2", "-2deg"),
        ("bottom-3", "0deg"),
        ("bottom-4", "2deg"),
        ("bottom-5", "-3deg"),
    ]
    for i, ang in enumerate(anggota_items):
        slot_name, tilt_deg = slot_configs[i] if i < len(slot_configs) else (f"extra-{i}", "0deg")
        ang["slot"] = slot_name
        ang["tilt"] = tilt_deg
        ordered_profiles.append(ang)

    total_profiles = len(ordered_profiles)
    for idx, p in enumerate(ordered_profiles):
        p["index"] = idx

    # Build hidden radio inputs + dynamic CSS selector rules for pure-CSS Spotlight Modal
    radio_inputs_html = ['<input type="radio" name="jacobi_sp" id="jacobi_sp_close" class="jacobi-sp-radio" checked />']
    checked_css_rules = []
    modals_html = []

    for p in ordered_profiles:
        idx = p["index"]
        prev_idx = (idx - 1) % total_profiles
        next_idx = (idx + 1) % total_profiles
        radio_inputs_html.append(
            f'<input type="radio" name="jacobi_sp" id="jacobi_sp_{idx}" class="jacobi-sp-radio" />'
        )
        checked_css_rules.append(
            f"#jacobi_sp_{idx}:checked ~ .jacobi-modals-container #jacobi_modal_{idx} {{ display: flex !important; }}"
        )

        nama_esc = html.escape(p["nama"])
        nim_esc = html.escape(p["nim"])
        sebagai_esc = html.escape(p["sebagai"])
        badge_esc = html.escape(p["role_badge"])
        funfact_esc = html.escape(p["fun_fact"])
        motto_esc = html.escape(p["motto_hidup"])
        img_src = p["img"]

        modals_html.append(
            f"""
            <div id="jacobi_modal_{idx}" class="jacobi-sp-backdrop">
                <label for="jacobi_sp_close" class="jacobi-sp-overlay-close" aria-label="Tutup"></label>
                <div class="jacobi-sp-modal">
                    <label for="jacobi_sp_close" class="jacobi-sp-close-btn">✕ Tutup</label>
                    <div class="jacobi-sp-grid">
                        <div class="jacobi-sp-photo-frame">
                            <img src="{img_src}" alt="{nama_esc}" />
                        </div>
                        <div class="jacobi-sp-details">
                            <div class="jacobi-sp-badge">{badge_esc}</div>
                            <div class="jacobi-sp-name">{nama_esc}</div>
                            <div class="jacobi-sp-meta-row">
                                <div class="jacobi-sp-meta-pill">🪪 NIM: {nim_esc}</div>
                                <div class="jacobi-sp-meta-pill">🌸 Peran: {sebagai_esc}</div>
                            </div>
                            <div class="jacobi-sp-box">
                                <div class="jacobi-sp-box-label">✨ Fun Fact</div>
                                <div class="jacobi-sp-box-val">{funfact_esc}</div>
                            </div>
                            <div class="jacobi-sp-box jacobi-sp-motto">
                                <div class="jacobi-sp-box-label">❝ Motto Hidup ❞</div>
                                <div class="jacobi-sp-box-val">“{motto_esc}”</div>
                            </div>
                        </div>
                    </div>
                    <div class="jacobi-sp-nav-bar">
                        <label for="jacobi_sp_{prev_idx}" class="jacobi-sp-nav-btn">◀ Sebelumnya</label>
                        <div class="jacobi-sp-counter">{idx + 1} dari {total_profiles} • Kelompok 02 Jacobi</div>
                        <label for="jacobi_sp_{next_idx}" class="jacobi-sp-nav-btn">Selanjutnya ▶</label>
                    </div>
                </div>
            </div>
            """
        )

    def build_card_html(p):
        idx = p["index"]
        nama = html.escape(p["nama"])
        short_role = html.escape(p["short_role"])
        tier = p["tier"]
        tilt = p["tilt"]
        slot = p["slot"]
        img_src = p["img"]
        return f"""
        <label for="jacobi_sp_{idx}" class="prelude-card slot-{slot} tier-{tier}" style="--card-tilt: {tilt};" title="Klik untuk melihat foto jelas & biodata {nama}">
            <div class="card-role-tag">{short_role}</div>
            <div class="card-photo-box">
                <img src="{img_src}" alt="{nama}" loading="lazy" />
                <div class="card-hover-cta">✨ KLIK BIODATA</div>
            </div>
            <div class="card-name-plate">
                <div class="card-name-text">{nama}</div>
            </div>
        </label>
        """

    cards_by_slot = {p["slot"]: build_card_html(p) for p in ordered_profiles}

    top_left_html = cards_by_slot.get("top-left", "")
    top_center_html = cards_by_slot.get("top-center", "")
    top_right_html = cards_by_slot.get("top-right", "")

    left_wing_html = "".join(cards_by_slot.get(f"left-{i}", "") for i in range(1, 4))
    right_wing_html = "".join(cards_by_slot.get(f"right-{i}", "") for i in range(1, 4))
    bottom_fan_html = "".join(cards_by_slot.get(f"bottom-{i}", "") for i in range(1, 6))

    radios_block = "\n".join(radio_inputs_html)
    checked_rules_block = "\n".join(checked_css_rules)
    modals_block = "\n".join(modals_html)

    photobook_dom_html = f"""
    <style>
        [data-testid="stHtml"], .stHtml {{
            width: 100% !important;
            max-width: 100% !important;
        }}
        .jacobi-photobook-root {{
            width: 100%;
            max-width: 1040px;
            margin: 14px auto 28px auto;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #3A1F2B;
        }}
        .jacobi-sp-radio {{
            display: none !important;
        }}

        /* MAIN JKT48 PRELUDE SUNBURST POSTER STAGE */
        .prelude-stage {{
            position: relative;
            width: 100%;
            border-radius: 28px;
            padding: 32px 24px 34px 24px;
            background:
                radial-gradient(circle at 50% 48%, rgba(255, 240, 246, 0.94) 0%, rgba(248, 165, 194, 0.45) 36%, rgba(188, 46, 94, 0.92) 100%),
                repeating-conic-gradient(
                    from 0deg at 50% 48%,
                    #D85A7F 0deg 9deg,
                    #F390B0 9deg 18deg,
                    #C44569 18deg 27deg,
                    #F7A8C4 27deg 36deg
                );
            border: 3px solid #F8C8DC;
            box-shadow:
                0 20px 50px rgba(158, 36, 78, 0.24),
                inset 0 0 50px rgba(255, 255, 255, 0.35);
            overflow: hidden;
        }}

        .prelude-stage::before {{
            content: "";
            position: absolute;
            inset: 0;
            background-image: radial-gradient(rgba(255, 255, 255, 0.24) 1.5px, transparent 1.5px);
            background-size: 16px 16px;
            pointer-events: none;
            z-index: 0;
        }}

        .jp-sticker {{
            position: absolute;
            font-family: 'Noto Serif JP', serif;
            font-weight: 900;
            color: rgba(255, 255, 255, 0.95);
            text-shadow: 2px 2px 0px #9E2A52, 0 0 14px rgba(255, 182, 193, 0.8);
            pointer-events: none;
            z-index: 1;
            user-select: none;
            letter-spacing: 0.06em;
        }}
        .jp-sticker.s1 {{ top: 14px; left: 18px; font-size: 1.25rem; transform: rotate(-10deg); }}
        .jp-sticker.s2 {{ top: 16px; right: 18px; font-size: 1.25rem; transform: rotate(10deg); }}

        /* TOP HIERARCHY ROW: PALU (LEFT), MENTOR (TOP CENTER CROWN), BULU (RIGHT) */
        .top-leaders-row {{
            position: relative;
            z-index: 5;
            display: grid;
            grid-template-columns: 1fr 1.14fr 1fr;
            gap: 14px;
            align-items: end;
            max-width: 560px;
            margin: 8px auto 18px auto;
        }}
        .top-slot-wrap {{
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }}
        .top-slot-wrap.mentor-crown {{
            transform: translateY(-10px);
        }}

        /* MIDDLE SECTION: LEFT WING (3), CENTER PRELUDE EMBLEM, RIGHT WING (3) */
        .middle-sunburst-row {{
            position: relative;
            z-index: 5;
            display: grid;
            grid-template-columns: 1fr 1.65fr 1fr;
            gap: 14px;
            align-items: center;
            margin-bottom: 18px;
        }}
        .wing-column {{
            display: flex;
            flex-direction: column;
            gap: 14px;
            align-items: center;
            width: 100%;
        }}

        /* CENTER PRELUDE EMBLEM BOX */
        .prelude-center-emblem {{
            background: linear-gradient(145deg, rgba(255, 250, 252, 0.97) 0%, rgba(255, 228, 238, 0.97) 100%);
            border: 3px solid #FFFFFF;
            outline: 2px solid #D85A7F;
            border-radius: 22px;
            padding: 22px 16px;
            text-align: center;
            box-shadow:
                0 16px 40px rgba(128, 20, 60, 0.28),
                0 0 32px rgba(255, 255, 255, 0.65);
            position: relative;
            overflow: hidden;
        }}
        .emblem-top-pill {{
            display: inline-block;
            background: linear-gradient(90deg, #9E2A52 0%, #D85A7F 100%);
            color: #FFFFFF;
            font-size: 0.64rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            padding: 4px 12px;
            border-radius: 999px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }}
        .emblem-jp-sub {{
            font-family: 'Noto Serif JP', serif;
            font-size: 0.78rem;
            font-weight: 700;
            color: #B23A5E;
            letter-spacing: 0.14em;
            margin-bottom: 4px;
        }}
        .emblem-main-title {{
            font-family: 'Cormorant Garamond', 'Noto Serif JP', serif;
            font-size: clamp(2rem, 3.8vw, 2.9rem);
            font-weight: 700;
            color: #3A1F2B;
            letter-spacing: 0.05em;
            line-height: 1.05;
            margin-bottom: 6px;
        }}
        .emblem-photobook-tag {{
            display: inline-block;
            background: #FCE4EC;
            border: 1.5px solid #F29BB8;
            color: #8C2448;
            font-weight: 800;
            font-size: 0.72rem;
            letter-spacing: 0.16em;
            padding: 3px 12px;
            border-radius: 8px;
            margin-bottom: 10px;
        }}
        .emblem-desc {{
            font-size: 0.78rem;
            color: #5C2D40;
            line-height: 1.5;
            margin: 0 auto 12px auto;
        }}
        .emblem-interactive-hint {{
            background: linear-gradient(135deg, #FFF5F8 0%, #FFE0EC 100%);
            border: 1.5px dashed #D85A7F;
            border-radius: 12px;
            padding: 8px 10px;
            font-size: 0.72rem;
            font-weight: 700;
            color: #9E2A52;
            line-height: 1.4;
        }}

        /* BOTTOM FAN ROW: 5 ANGGOTA */
        .bottom-fan-row {{
            position: relative;
            z-index: 5;
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
            align-items: start;
        }}

        /* PORTRAIT CARD STYLING + HOVER GLOW & SCALE */
        label.prelude-card {{
            display: block;
            position: relative;
            width: 100%;
            max-width: 155px;
            background: #FFFFFF;
            border-radius: 14px;
            padding: 6px 6px 8px 6px;
            border: 2px solid #FFE4EE;
            box-shadow: 0 4px 14px rgba(90, 15, 42, 0.12);
            cursor: pointer;
            user-select: none;
        }}
        label.prelude-card.tier-mentor {{
            max-width: 172px;
            background: #FFFDF7;
            border: 2px solid #FFD700;
            box-shadow: 0 4px 14px rgba(140, 25, 65, 0.15);
        }}
        label.prelude-card.tier-leader {{
            max-width: 160px;
            border: 2px solid #F6C358;
            box-shadow: 0 4px 14px rgba(120, 20, 55, 0.12);
        }}

        /* HOVER EFFECT: SUBTLE BORDER HIGHLIGHT */
        label.prelude-card:hover {{
            z-index: 40 !important;
            border-color: #D85A7F !important;
            box-shadow: 0 6px 18px rgba(158, 42, 82, 0.18) !important;
        }}

        .card-role-tag {{
            position: absolute;
            top: -9px;
            left: 50%;
            transform: translateX(-50%);
            white-space: nowrap;
            font-size: 0.56rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            padding: 2px 8px;
            border-radius: 999px;
            z-index: 4;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.16);
        }}
        .tier-mentor .card-role-tag {{
            background: linear-gradient(135deg, #FFD700 0%, #D49B00 100%);
            color: #3A1F2B;
            border: 1px solid #FFFFFF;
        }}
        .tier-leader .card-role-tag {{
            background: linear-gradient(135deg, #E59838 0%, #B86B11 100%);
            color: #FFFFFF;
            border: 1px solid #FFF8E7;
        }}
        .tier-member .card-role-tag {{
            background: linear-gradient(135deg, #D85A7F 0%, #9E2A52 100%);
            color: #FFFFFF;
            border: 1px solid #FFE4EE;
        }}

        .card-photo-box {{
            position: relative;
            width: 100%;
            aspect-ratio: 3 / 3.5;
            border-radius: 10px;
            overflow: hidden;
            background: #FCE4EC;
        }}
        .card-photo-box img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.35s ease;
        }}
        label.prelude-card:hover .card-photo-box img {{
            transform: scale(1.06);
        }}

        .card-hover-cta {{
            position: absolute;
            bottom: 6px;
            left: 50%;
            transform: translateX(-50%) translateY(6px);
            background: rgba(158, 42, 82, 0.92);
            color: #FFFFFF;
            font-size: 0.56rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            padding: 3px 8px;
            border-radius: 999px;
            border: 1px solid #FFD1E1;
            opacity: 0;
            transition: all 0.22s ease;
            white-space: nowrap;
        }}
        label.prelude-card:hover .card-hover-cta {{
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }}

        .card-name-plate {{
            margin-top: 5px;
            text-align: center;
            background: linear-gradient(90deg, #FFF0F5 0%, #FCE4EC 50%, #FFF0F5 100%);
            border-radius: 6px;
            padding: 4px 4px;
            border: 1px solid #F6C8DA;
        }}
        .card-name-text {{
            font-size: 0.66rem;
            font-weight: 800;
            color: #3A1F2B;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        /* =====================================================================
           PURE-CSS FULLSCREEN SPOTLIGHT BIODATA MODAL (ON CLICK)
           ===================================================================== */
        .jacobi-sp-backdrop {{
            position: fixed;
            inset: 0;
            background: rgba(42, 12, 26, 0.85);
            z-index: 999999;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 18px;
        }}
        .jacobi-sp-overlay-close {{
            position: absolute;
            inset: 0;
            cursor: pointer;
        }}
        {checked_rules_block}

        .jacobi-sp-modal {{
            position: relative;
            z-index: 2;
            width: 100%;
            max-width: 780px;
            background: #FFFFFF;
            border: 2px solid #F7B9D0;
            border-radius: 20px;
            box-shadow: 0 16px 40px rgba(32, 6, 18, 0.35);
            overflow: hidden;
            padding: 24px 26px 20px 26px;
        }}

        .jacobi-sp-close-btn {{
            position: absolute;
            top: 14px;
            right: 16px;
            background: #FCE4EC;
            border: 1.5px solid #E888A7;
            color: #9E2A52;
            font-weight: 800;
            font-size: 0.82rem;
            padding: 5px 14px;
            border-radius: 999px;
            cursor: pointer;
            transition: all 0.2s ease;
            z-index: 10;
        }}
        .jacobi-sp-close-btn:hover {{
            background: #D85A7F;
            color: #FFFFFF;
        }}

        .jacobi-sp-grid {{
            display: grid;
            grid-template-columns: 270px 1fr;
            gap: 22px;
            align-items: center;
        }}
        .jacobi-sp-photo-frame {{
            background: #FFFFFF;
            padding: 9px;
            border-radius: 20px;
            border: 2.5px solid #F4A8C4;
            box-shadow:
                0 0 24px rgba(216, 90, 127, 0.30),
                0 12px 28px rgba(90, 20, 48, 0.16);
        }}
        .jacobi-sp-photo-frame img {{
            width: 100%;
            aspect-ratio: 3 / 3.7;
            object-fit: cover;
            border-radius: 14px;
            display: block;
        }}
        .jacobi-sp-details {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            text-align: left;
        }}
        .jacobi-sp-badge {{
            display: inline-flex;
            align-self: flex-start;
            background: linear-gradient(135deg, #D85A7F 0%, #9E2A52 100%);
            color: #FFFFFF;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            padding: 5px 14px;
            border-radius: 999px;
        }}
        .jacobi-sp-name {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.1rem;
            font-weight: 700;
            color: #3A1F2B;
            line-height: 1.1;
        }}
        .jacobi-sp-meta-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        .jacobi-sp-meta-pill {{
            background: #FCE4EC;
            border: 1px solid #F2ACC6;
            color: #8C2448;
            font-size: 0.8rem;
            font-weight: 700;
            padding: 5px 12px;
            border-radius: 10px;
        }}
        .jacobi-sp-box {{
            background: #FFF8FA;
            border: 1.5px solid #F5C2D7;
            border-radius: 14px;
            padding: 11px 14px;
        }}
        .jacobi-sp-box-label {{
            font-size: 0.72rem;
            font-weight: 800;
            color: #B23A5E;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 3px;
        }}
        .jacobi-sp-box-val {{
            font-size: 0.9rem;
            color: #3A1F2B;
            line-height: 1.5;
            font-weight: 500;
        }}
        .jacobi-sp-motto {{
            background: linear-gradient(90deg, #FCE4EC 0%, #FFF8FA 100%);
            border-left: 4px solid #D85A7F;
            font-style: italic;
        }}
        .jacobi-sp-nav-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 16px;
            padding-top: 12px;
            border-top: 1px solid #F5C6D8;
        }}
        .jacobi-sp-nav-btn {{
            background: #FFF0F5;
            border: 1.5px solid #E888A7;
            color: #9E2A52;
            font-weight: 700;
            font-size: 0.8rem;
            padding: 7px 16px;
            border-radius: 999px;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .jacobi-sp-nav-btn:hover {{
            background: #D85A7F;
            color: #FFFFFF;
        }}
        .jacobi-sp-counter {{
            font-size: 0.78rem;
            font-weight: 700;
            color: #8C4660;
        }}

        @media (max-width: 680px) {{
            .middle-sunburst-row {{
                grid-template-columns: 1fr;
            }}
            .wing-column {{
                flex-direction: row;
                flex-wrap: wrap;
                justify-content: center;
            }}
            .bottom-fan-row {{
                grid-template-columns: repeat(2, 1fr);
            }}
            .jacobi-sp-grid {{
                grid-template-columns: 1fr;
            }}
            .jacobi-sp-photo-frame {{
                max-width: 220px;
                margin: 0 auto;
            }}
        }}
    </style>

    <div class="jacobi-photobook-root">
        {radios_block}

        <div class="prelude-stage">
            <div class="jp-sticker s1">行くぞ! 🌸</div>
            <div class="jp-sticker s2">春の桜 ✨</div>

            <!-- BARIS PALING ATAS: KETUA (KIRI), MENTOR (PALING ATAS TENGAH), WAKIL KETUA (KANAN) -->
            <div class="top-leaders-row">
                <div class="top-slot-wrap">
                    {top_left_html}
                </div>
                <div class="top-slot-wrap mentor-crown">
                    {top_center_html}
                </div>
                <div class="top-slot-wrap">
                    {top_right_html}
                </div>
            </div>

            <!-- BARIS TENGAH: 3 ANGGOTA KIRI, EMBLEM TENGAH 02 JACOBI, 3 ANGGOTA KANAN -->
            <div class="middle-sunburst-row">
                <div class="wing-column">
                    {left_wing_html}
                </div>

                <div class="prelude-center-emblem">
                    <div class="emblem-top-pill">CEO HMSD ADYATAMA ITERA 2026</div>
                    <div class="emblem-main-title">02 JACOBI</div>
                    <div class="emblem-photobook-tag">DIGITAL PHOTOBOOK</div>
                    <p class="emblem-desc">
                        Satu Mentor Pembimbing, Ketua (Palu) &amp; Wakil Ketua (Bulu), bersama 11 Anggota
                        Kelompok 02 Jacobi dalam harmoni musim semi Sakura.
                    </p>
                    <div class="emblem-interactive-hint">
                        ✨ <strong>INTERAKTIF PHOTOBOOK:</strong><br/>
                        Arahkan kursor (<em>Hover</em>) pada foto untuk efek bercahaya &amp; membesar, lalu <strong>KLIK FOTO</strong> untuk membuka potret jelas &amp; Biodata Lengkap!
                    </div>
                </div>

                <div class="wing-column">
                    {right_wing_html}
                </div>
            </div>

            <!-- BARIS BAWAH: 5 ANGGOTA -->
            <div class="bottom-fan-row">
                {bottom_fan_html}
            </div>
        </div>

        <div class="jacobi-modals-container">
            {modals_block}
        </div>
    </div>
    """

    st.html(photobook_dom_html)




def render_buku_kating_header(member_name=None):
    inject_sakura_css()
    subtitle = f"Koleksi Memori & Kenangan Bersama Kakak Tingkat • {member_name}" if member_name else "Koleksi Memori & Kenangan Bersama Kakak Tingkat HMSD Adyatama"
    st.markdown(
        f"""
        <div class="sakura-hero-box" style="padding: 24px 22px 20px 22px; margin-bottom: 16px;">
            <div class="sakura-crest-pill">🌸 Kelompok 02 Jacobi • Buku Kating 2026 🌸</div>
            <h1 class="sakura-main-title" style="font-size: clamp(2.1rem, 4vw, 3.2rem) !important;">BUKU KATING</h1>
            <div class="sakura-jp-caption">{html.escape(subtitle)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def sakura_dept_menu():
    inject_sakura_css()
    options = list(DEPARTMENT_META.keys())
    icons = [DEPARTMENT_META[k]["icon"] for k in options]
    selected = option_menu(
        menu_title=None,
        options=options,
        icons=icons,
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "8px!important",
                "background-color": "#FFF0F5",
                "border": "1.5px solid #F5C2D7",
                "border-radius": "18px",
                "display": "flex",
                "flex-wrap": "wrap",
                "justify-content": "center",
                "gap": "6px",
                "box-shadow": "0 8px 22px rgba(216, 90, 127, 0.08)",
            },
            "icon": {"color": "#9E3356", "font-size": "15px"},
            "nav-link": {
                "font-size": "13px",
                "font-weight": "600",
                "color": "#4A2535",
                "text-align": "center",
                "margin": "2px",
                "padding": "8px 12px",
                "border-radius": "12px",
                "--hover-color": "#FCE4EC",
                "white-space": "nowrap",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #D85A7F 0%, #B23A5E 100%)",
                "color": "#FFFFFF",
                "font-weight": "700",
                "box-shadow": "0 4px 12px rgba(178, 58, 94, 0.25)",
            },
        },
    )
    st.session_state["_current_sakura_dept"] = selected
    return selected


def render_kating_cards(kating_data_or_urls, kesan_pesan_or_dept=None, departemen=None):
    # Support both shapes:
    # 1. render_kating_cards(kating_data, departemen=menu) where kating_data = [{'nama': ..., 'link_gdrive': ..., 'kesan': ..., 'pesan': ...}]
    # 2. render_kating_cards(gambar_urls, kesan_pesan, departemen=menu)
    if isinstance(kating_data_or_urls, list) and kating_data_or_urls and isinstance(kating_data_or_urls[0], dict):
        kating_data = kating_data_or_urls
        dept_key = departemen or (kesan_pesan_or_dept if isinstance(kesan_pesan_or_dept, str) else None) or st.session_state.get("_current_sakura_dept", "Kesekjenan")
        gambar_urls = [item.get("link_gdrive", item.get("gambar_url", item.get("foto", ""))) for item in kating_data]
        data_list = kating_data
    else:
        gambar_urls = kating_data_or_urls or []
        data_list = kesan_pesan_or_dept if isinstance(kesan_pesan_or_dept, list) else []
        dept_key = departemen or (kesan_pesan_or_dept if isinstance(kesan_pesan_or_dept, str) else None) or st.session_state.get("_current_sakura_dept", "Kesekjenan")

    # Normalize legacy menu names
    if dept_key in ("Minbak", "Departemen Minbak"):
        dept_key = "Departemen MINBAK"
    elif dept_key == "Badan Legislatif":
        dept_key = "Baleg"

    meta = DEPARTMENT_META.get(
        dept_key,
        {
            "title": dept_key,
            "jp": "桜の絆 • HMSD Adyatama ITERA",
            "desc": "Keluarga Besar HMSD Adyatama ITERA 2026.",
        },
    )

    canonical_list = get_canonical_dept_data(dept_key)
    target_len = len(gambar_urls) if gambar_urls else len(canonical_list)
    resolved_data = resolve_member_data_list(data_list, departemen=dept_key, target_count=target_len)

    # Department Visual Header Banner
    st.markdown(
        f"""
        <div class="sakura-dept-banner">
            <div>
                <div style="font-size: 0.76rem; font-weight: 700; color: #B23A5E; letter-spacing: 0.1em; text-transform: uppercase;">
                    🌸 {html.escape(meta['jp'])}
                </div>
                <h2 class="sakura-dept-title">{html.escape(meta['title'])}</h2>
                <div class="sakura-dept-sub">{html.escape(meta['desc'])}</div>
            </div>
            <div class="sakura-dept-count">
                🌸 {len(resolved_data)} Kakak Tingkat
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.spinner(f"🌸 Memuat galeri {meta['title']} ({len(resolved_data)} kating)..."):
        b64_list = fetch_batch_b64(gambar_urls, resize_dim=(360, 460)) if gambar_urls else []

    # Render in 2-Column Horizontal Cards Grid
    for row_idx in range(0, len(resolved_data), 2):
        cols = st.columns(2, gap="medium")
        for col_offset in range(2):
            idx = row_idx + col_offset
            if idx >= len(resolved_data):
                break
            item = resolved_data[idx]
            b64_img = (
                b64_list[idx]
                if idx < len(b64_list) and b64_list[idx]
                else get_placeholder_svg_b64(item.get("nama", f"Kating #{idx + 1}"))
            )

            nama = html.escape(str(item.get("nama", "-")))
            nim = html.escape(str(item.get("nim", "-")))
            umur = html.escape(str(item.get("umur", "-")))
            asal = html.escape(str(item.get("asal", "-")))
            alamat = html.escape(str(item.get("alamat", "-")))
            hobi = html.escape(str(item.get("hobbi", item.get("hobi", "-"))))
            sosmed = html.escape(str(item.get("sosmed", "-")))
            kesan = html.escape(str(item.get("kesan", "-")))
            pesan = html.escape(str(item.get("pesan", "-")))

            jabatan = str(item.get("jabatan", "")).strip()
            divisi = str(item.get("divisi", "")).strip()
            if jabatan and divisi:
                role_label = f"{jabatan} • {divisi}"
            elif jabatan:
                role_label = jabatan
            else:
                role_label = dept_key
            role_html = html.escape(role_label)

            with cols[col_offset]:
                st.markdown(
                    f"""
                    <div class="sakura-kating-card">
                        <div class="sakura-kating-top">
                            <div class="sakura-kating-photo-col">
                                <img src="data:image/jpeg;base64,{b64_img}" alt="{nama}">
                                <span class="sakura-kating-num">#{idx + 1:02d}</span>
                            </div>
                            <div class="sakura-kating-info-col">
                                <h3 class="sakura-kating-name">{nama}</h3>
                                <div class="sakura-badge-row">
                                    <span class="sakura-chip-role">🌸 {role_html}</span>
                                    <span class="sakura-chip-nim">NIM {nim}</span>
                                </div>
                                <div class="sakura-bio-grid">
                                    <div class="sakura-bio-item">
                                        <span class="sakura-bio-label">🎂 Umur</span>
                                        <span class="sakura-bio-val">{umur}</span>
                                    </div>
                                    <div class="sakura-bio-item">
                                        <span class="sakura-bio-label">📸 Instagram</span>
                                        <span class="sakura-bio-val">{sosmed}</span>
                                    </div>
                                    <div class="sakura-bio-item">
                                        <span class="sakura-bio-label">📍 Asal</span>
                                        <span class="sakura-bio-val">{asal}</span>
                                    </div>
                                    <div class="sakura-bio-item">
                                        <span class="sakura-bio-label">🏠 Alamat</span>
                                        <span class="sakura-bio-val">{alamat}</span>
                                    </div>
                                    <div class="sakura-bio-item full-span">
                                        <span class="sakura-bio-label">✨ Hobi</span>
                                        <span class="sakura-bio-val">{hobi}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="sakura-quote-section">
                            <div class="sakura-quote-line">
                                <span class="sakura-quote-tag">💬 Kesan:</span> “{kesan}”
                            </div>
                            <div class="sakura-quote-line">
                                <span class="sakura-quote-tag">💌 Pesan:</span> “{pesan}”
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# Alias for intuitive usage in member files
display_kating = render_kating_cards

