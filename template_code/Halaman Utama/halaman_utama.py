import streamlit as st
from streamlit_option_menu import option_menu
import sys
import os

# Menambahkan root project ke sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from tools.ui_helper import (
    inject_custom_css,
    load_image,
    clean_text,
    get_menu_styles,
)

# Injeksi tema CSS estetis
inject_custom_css()

# Header Judul Halaman Utama
st.markdown(
    """
    <div style='text-align: center; margin-bottom: 20px; padding-top: 10px;'>
        <h1 style='font-size: 3.4rem; font-weight: 800; margin-bottom: 4px; background: linear-gradient(130deg, #ede9fe 10%, #c4b5fd 55%, #a78bfa 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            WEBSITE KATING
        </h1>
        <p style='font-size: 1.2rem; color: #c4b5fd; font-weight: 500; margin: 0;'>
            CEO HMSD Adyatama ITERA 2026
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# URLs Logo
url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"   # Logo Himpunan HMSD (DI ATAS)
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"  # Logo Departemen / Kegiatan (DI BAWAH)

# 1. Logo Himpunan di Atas (Ukuran normal, tidak terpotong, proporsional)
col1, col2, col3 = st.columns([1.5, 2, 1.5])
with col2:
    img_himpunan = load_image(url, fallback_name="Logo Himpunan HMSD", keep_ratio=True)
    st.image(img_himpunan, use_container_width=True)

st.write("")

# 2. Logo Departemen/Kegiatan di Bawah Logo Himpunan (Ukuran normal, tidak terpotong)
col1, col2, col3 = st.columns([1.5, 2, 1.5])
with col2:
    img_kegiatan = load_image(url1, fallback_name="Logo Departemen CEO HMSD", keep_ratio=True)
    st.image(img_kegiatan, use_container_width=True)

st.write("")


def streamlit_menu():
    """Menu navigasi model asli dengan warna ungu elegan dan efek klik/hover."""
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles=get_menu_styles(),
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        # --- DESKRIPSI KELOMPOK YANG MENARIK & BERNYAWA ---
        st.markdown(
            """
            <div style="text-align: center; margin: 10px 0 16px 0;">
                <h2 style="font-size: 2.2rem; font-weight: 700; color: #ffffff; margin: 0;">Deskripsi Kelompok</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="glass-box" style="line-height: 1.9; font-size: 1.02rem; color: #cbd5e1; text-align: justify; margin-bottom: 20px;">
                Kami adalah <b>Kelompok Tensor</b>, representasi dari mahasiswa dan mahasiswi Program Studi 
                <b>Sains Data Institut Teknologi Sumatera (ITERA) Angkatan 2025</b>. 
                Berawal dari individu-individu yang belum saling mengenal dengan latar belakang daerah yang beragam dari penjuru Nusantara, 
                kami dipersatukan dalam satu simfoni kebersamaan di kampus tercinta ITERA.<br><br>
                Dalam rangkaian prosesi <b>CEO HMSD Adyatama ITERA</b>, website Buku Kating Digital ini lahir bukan sekadar sebagai pemenuhan tugas angkatan, 
                melainkan sebagai <b>ruang ekspresi, arsip kenangan, dan jembatan silaturahmi</b> antarangkatan. 
                Di balik setiap profil kating yang terdata, ada cerita tentang bagaimana kami belajar mengatasi rasa canggung, merajut komunikasi hangat, 
                serta menempa kemampuan teknis pemrograman <b>Python & framework Streamlit</b> secara kolaboratif. 
                Kami percaya, ilmu yang dipadukan dengan persaudaraan akan melahirkan karya yang berjiwa dan bermakna.
            </div>
            """,
            unsafe_allow_html=True,
        )

        # --- JARGON KEBANGGAAN KELOMPOK TENSOR ---
        st.markdown(
            """
            <div class="jargon-card">
                <span class="g-tag">⚡ JARGON KELOMPOK TENSOR ⚡</span>
                <div class="jargon-text">
                    "Berpikir Multidimensi ,Bergerak Tanpa Batas, TENSOR hadir membawa Kualitas, Kompak dalam Aksi, Kuat dalam Kreasi, TENSOR TENSOR TENSOR Siap Berprestasi !!!"
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # --- FOTO UTAMA KELOMPOK DENGAN EFEK KACA SAAT DISENTUH ---
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1BFaWjCYfj0HFeGBBDB8SmUYsZkxcEvM7"
        st.markdown(
            """
            <div style="text-align: center; margin: 24px 0 12px 0;">
                <span class="g-tag">📸 Official Tensor Team Portrait</span>
                <div style="font-size: 1.3rem; font-weight: 700; color: #ffffff; margin-top: 6px;">Keluarga Besar Kelompok Tensor</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns([0.8, 3.4, 0.8])
        with col2:
            with st.container(key="shine-photo-team"):
                img_kelompok = load_image(foto_kelompok, fallback_name="Foto Kelompok Tensor", keep_ratio=True)
                st.image(img_kelompok, use_container_width=True)

        st.write("")

        # --- GALERI MOMEN: KERJA KELOMPOK, RANGKAIAN, & HANGOUT ---
        st.markdown(
            """
            <div style="text-align: center; margin: 28px 0 18px 0;">
                <span class="g-tag">🎞️ Behind The Scene & Moments</span>
                <h3 style="font-size: 1.85rem; font-weight: 700; color: #ffffff; margin: 6px 0 4px 0;">Dokumentasi Kami</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # --- DATA GALERI: untuk menambah kartu baru, cukup tambah satu blok {...} di list ini ---
        GALERI = [
            {
                "emoji": "💻",
                "judul": "Kerja Kelompok & Coding",
                "deskripsi": "Momen diskusi seru di selasar gedung kampus dan kafe. Debat logika kode, revisi layout bareng, hingga sharing cemilan saat mata mulai mengantuk.",
                "foto": "https://drive.google.com/uc?export=view&id=19fo5WQL02HB7IzvRUwhNoKySjy6uJ_Lv",
            },
            {
                "emoji": "🚩",
                "judul": "Rangkaian Acara CEO",
                "deskripsi": "Keseruan saat mengikuti dinamika materi, yel-yel kelompok, dan simulasi organisasi. Melatih kekompakan, kepemimpinan, dan mental pantang menyerah.",
                "foto": "https://drive.google.com/uc?export=view&id=11UyAE4hUKZ8dG0JG3OxqZCLOrAGGDGJ_",
            },
            {
                "emoji": "☕",
                "judul": "Main & Refreshing",
                "deskripsi": "Karena hidup mahasiswa bukan cuma soal deadline! Momen makan bareng, nongkrong santai, dan bercanda lepas yang bikin kami makin akrab seperti keluarga.",
                "foto": "https://drive.google.com/uc?export=view&id=1tWFKgAL9u58RnOrhMx-IexoK8y_FJLXb",
            },
        ]

        from html import escape as _esc

        KARTU_PER_BARIS = 3
        for start in range(0, len(GALERI), KARTU_PER_BARIS):
            cols_galeri = st.columns(KARTU_PER_BARIS, gap="medium")
            for ci, item in enumerate(GALERI[start:start + KARTU_PER_BARIS]):
                with cols_galeri[ci]:
                    # depan: foto, belakang: teks (kartu berputar saat disentuh)
                    with st.container(key=f"flip-card-{start + ci}"):
                        img_galeri = load_image(item["foto"], fallback_name=item["judul"], keep_ratio=True)
                        st.image(img_galeri, use_container_width=True)
                        st.markdown(
                            f'<div class="flip-back">'
                            f'<div class="flip-emoji">{item["emoji"]}</div>'
                            f'<div class="flip-title">{_esc(item["judul"])}</div>'
                            f'<div class="flip-desc">{_esc(item["deskripsi"])}</div>'
                            f'</div>',
                            unsafe_allow_html=True,
                        )

        # --- REFLEKSI AKHIR ---
        st.markdown(
            """
            <div class="glass-box" style="line-height: 1.85; font-size: 1.02rem; color: #cbd5e1; text-align: justify; margin-top: 10px;">
                Bagi kami, setiap baris kode dan setiap wawancara kating di website ini menyimpan ceritanya sendiri. 
                Kami belajar bagaimana bekerja sama dalam tim, menghargai waktu, menerima masukan, dan saling melengkapi kekurangan satu sama lain. 
                Semoga website Buku Kating ini dapat menjadi arsip digital yang penuh kenangan manis dan inspirasi untuk perjalanan kami ke depan!
            </div>
            """,
            unsafe_allow_html=True,
        )

    home_page()

elif menu == "About Us":

    import requests
    from io import BytesIO
    from PIL import Image
    from html import escape

    # =========================
    # FUNGSI MENGAMBIL GAMBAR
    # =========================
    @st.cache_data(ttl=3600, show_spinner=False)
    def get_drive_image(file_id):
        """
        Mengambil gambar dari Google Drive menggunakan file ID.
        Mengembalikan gambar PIL jika berhasil.
        """
        if not file_id or file_id == "MASUKKAN_ID_IA_DISINI":
            return None

        url = f"https://drive.google.com/uc?export=download&id={file_id}"

        try:
            response = requests.get(
                url,
                timeout=20,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "")

            # Pastikan respons berupa gambar
            if not content_type.startswith("image/"):
                # Coba baca respons sebagai gambar
                # untuk mengantisipasi header server yang tidak tepat.
                try:
                    image = Image.open(BytesIO(response.content))
                    image.load()
                    return image.convert("RGB")
                except Exception:
                    return None

            image = Image.open(BytesIO(response.content))
            image.load()

            return image.convert("RGB")

        except Exception as e:
            print(f"Gagal memuat gambar {file_id}: {e}")
            return None

    # =========================
    # JUDUL HALAMAN
    # =========================
    st.markdown(
        """
        <div style="text-align:center; margin:10px 0 25px 0;">
            <h2 style="
                font-size:2.2rem;
                font-weight:700;
                color:#ffffff;
                margin:0;">
                Anggota Kelompok
            </h2>
            <p style="color:#c4b5fd; margin-top:8px;">
                Kenali lebih dekat keluarga besar Kelompok Tensor
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # ID FOTO GOOGLE DRIVE
    # Masukkan ID file saja, bukan URL lengkap
    # =========================
    gambar_ids = [
        "1U9qL_kV5pRVGxwjX5vY9Ye60zewUyis1",
        "1VDxX_RUW42qOiFcx2ZzNQIOC5EVmBt9p",
        "1JyZqi_gGn-Z0U7rbn6wm6yCff3iBAXUY",
        "1qn7DTt5dewAf4lrewAOw1wdGqarl4Gjy",
        "1pE1AmXiK-KOvxQgsWiw8LOIJFmSC4qBt",
        "1t-jcrs_NnloNmQS9C1Yx6x79HpRA3PyC",
        "1Q9BG3ckhXSkR241w6WQKUgks1NOisDVR",
        "1wYkTJHX0mhBy9UVW_9XoDMAvXd56xI2r",
        "1BZHhEBU0fE6kbtvuc67sUinlTB8yeKmq",
        "1WDDcHs08ui8kpk4ZgElSmS9LqSPwa3NB",
        "MASUKKAN_ID_IA_DISINI",
        "13nJeccLKDvlcb9X08Vbo2ZKEjyXf0TuR",
    ]

    # =========================
    # DATA ANGGOTA
    # =========================
    data_list = [
        {
            "nama": "Ahmad Fadylah",
            "sebagai": "Pak Lurah",
            "nim": "125450103",
            "fun_fact": "Suka ngeliatin sunset",
            "motto_hidup": (
                "Dalam setiap interaksi pasti ada komunikasi. "
                "Di dalam komunikasi adakalanya terjadi miskomunikasi. "
                "Maka dari itu, butuh evaluasi agar tidak terjadi "
                "miskomunikasi lagi."
            ),
        },
        {
            "nama": "Laikha Salwa Balqis",
            "sebagai": "Bu Lurah",
            "nim": "125450112",
            "fun_fact": "Strict parents, suka hewan, suka jadi penjelajah",
            "motto_hidup": (
                "Tenang, gausah dibikin pusing, gausah dibikin ribet. "
                "Everything's gonna be ok!"
            ),
        },
        {
            "nama": "Hanifa Az'zahra",
            "sebagai": "Anggota",
            "nim": "125450001",
            "fun_fact": "Pindah kost 3 kali dalam satu semester, suka tidur di motor",
            "motto_hidup": (
                "Melangkah ke arah yang asing, membaca apa yang tak "
                "terucap dan yang terlihat."
            ),
        },
        {
            "nama": "Jauza Virna Radyta",
            "sebagai": "Anggota",
            "nim": "125450009",
            "fun_fact": "Banyak cowo, ga punya pacar",
            "motto_hidup": "Semua hal itu butuh proses, bukan protes.",
        },
        {
            "nama": "Lusia Zefanya Sihotang",
            "sebagai": "Anggota",
            "nim": "125450010",
            "fun_fact": "Cinta piscok UIN",
            "motto_hidup": "Ad Maiorem Dei Gloriam",
        },
        {
            "nama": "Enzo Hamman Albarru",
            "sebagai": "Anggota",
            "nim": "125450022",
            "fun_fact": "Sarapan nasi uduk setiap hari",
            "motto_hidup": "Hidup tenang, bebas napas, nasi padang, kopi panas.",
        },
        {
            "nama": "Mario Figo Dito",
            "sebagai": "Anggota",
            "nim": "125450048",
            "fun_fact": "Mirip Bang Zaldy kata Kak Tanty",
            "motto_hidup": "Coba aja dulu bkakakak",
        },
        {
            "nama": "Kasih Martha Reichella",
            "sebagai": "Anggota",
            "nim": "125450060",
            "fun_fact": "Lebih suka baca novel sedih dibanding novel happy ending",
            "motto_hidup": "Apa pun masalahnya, jangan lupa selalu mengandalkan Tuhan.",
        },
        {
            "nama": "Muhammad Reyza Fasihurahman",
            "sebagai": "Anggota",
            "nim": "125450094",
            "fun_fact": "Suka belajar fisika mesin",
            "motto_hidup": "Hidup itu mudah, yang susah itu cuma ADS.",
        },
        {
            "nama": "Nadira Alifa Arifin",
            "sebagai": "Anggota",
            "nim": "125450101",
            "fun_fact": "Cinta kopi walau aslam",
            "motto_hidup": "[Isi Motto]",
        },
        {
            "nama": "Gisella Salvia Pavita",
            "sebagai": "Anggota",
            "nim": "125450107",
            "fun_fact": "[Isi Fun Fact]",
            "motto_hidup": "[Isi Motto]",
        },
        {
            "nama": "Piligo Arga Gayoni",
            "sebagai": "Anggota",
            "nim": "125450123",
            "fun_fact": "Suka kesandung kalau jalan",
            "motto_hidup": (
                "Susah senang jalani saja, tapi hati-hati jalan bolong, "
                "nanti kesandung."
            ),
        },
    ]

    # =========================
    # CSS KARTU ANGGOTA
    # =========================
    st.markdown(
        """
        <style>
        .member-card {
            background: rgba(30, 27, 75, 0.68);
            border: 1px solid rgba(196, 181, 253, 0.25);
            border-radius: 18px;
            overflow: hidden;
            margin-bottom: 22px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        }

        .member-info {
            padding: 17px;
            color: #e2e8f0;
        }

        .member-name {
            font-size: 1.15rem;
            font-weight: 750;
            color: #ffffff;
            margin-bottom: 8px;
            overflow-wrap: anywhere;
        }

        .member-role {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            background: rgba(167, 139, 250, 0.18);
            border: 1px solid rgba(196, 181, 253, 0.4);
            color: #ddd6fe;
            font-size: 0.8rem;
            margin-bottom: 14px;
        }

        .member-detail {
            font-size: 0.91rem;
            line-height: 1.65;
            margin-bottom: 10px;
            overflow-wrap: anywhere;
        }

        .member-label {
            color: #c4b5fd;
            font-size: 0.76rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .member-motto {
            border-left: 3px solid #a78bfa;
            padding-left: 12px;
            margin-top: 13px;
            font-size: 0.9rem;
            font-style: italic;
            line-height: 1.6;
            overflow-wrap: anywhere;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # TAMPILKAN KARTU ANGGOTA
    # =========================
    for row in range(0, len(data_list), 2):

        col_a, col_b = st.columns(2, gap="medium")
        cols = [col_a, col_b]

        for ci in range(2):
            idx = row + ci

            if idx >= len(data_list):
                break

            data = data_list[idx]
            file_id = gambar_ids[idx]

            nama = escape(data["nama"])
            sebagai = escape(data["sebagai"])
            nim = escape(data["nim"])
            fun_fact = escape(data["fun_fact"])
            motto = escape(data["motto_hidup"])

            with cols[ci]:

                # Muat foto dari Google Drive
                img = get_drive_image(file_id)

                if img is not None:
                    st.image(
                        img,
                        use_container_width=True,
                    )
                else:
                    # Fallback jika foto belum berhasil dimuat
                    st.markdown(
                        f"""
                        <div style="
                            height:180px;
                            display:flex;
                            align-items:center;
                            justify-content:center;
                            text-align:center;
                            padding:15px;
                            background:rgba(139,92,246,0.12);
                            border:1px dashed rgba(196,181,253,0.5);
                            border-radius:16px;
                            color:#c4b5fd;
                            margin-bottom:10px;">
                            <div>
                                <div style="font-size:2rem;">📷</div>
                                <b>{nama}</b><br>
                                <small>Foto belum dapat dimuat</small>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                # Informasi anggota
                st.markdown(
                    f"""
                    <div class="member-card">
                        <div class="member-info">
                            <div class="member-name">{nama}</div>
                            <span class="member-role">{sebagai}</span>

                            <div class="member-detail">
                                <span class="member-label">NIM</span><br>
                                🎓 {nim}
                            </div>

                            <div class="member-detail">
                                <span class="member-label">Fun Fact</span><br>
                                ✨ {fun_fact}
                            </div>

                            <div class="member-motto">
                                <span class="member-label">Motto Hidup</span><br>
                                "{motto}"
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
