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

# URLs Logo (Sudah diubah ke format thumbnail)
url = "https://drive.google.com/thumbnail?id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx&sz=w1000"   # Logo Himpunan HMSD (DI ATAS)
url1 = "https://drive.google.com/thumbnail?id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb&sz=w1000"  # Logo Departemen / Kegiatan (DI BAWAH)

# 1. Logo Himpunan di Atas (Ukuran normal, tidak terpotong, proporsional)
col1, col2, col3 = st.columns([1.5, 2, 1.5])
with col2:
    # Memanggil st.image secara langsung (bypass load_image)
    st.image(url, use_container_width=True)

st.write("")

# 2. Logo Departemen/Kegiatan di Bawah Logo Himpunan (Ukuran normal, tidak terpotong)
col1, col2, col3 = st.columns([1.5, 2, 1.5])
with col2:
    # Memanggil st.image secara langsung (bypass load_image)
    st.image(url1, use_container_width=True)

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
        foto_kelompok = "https://drive.google.com/thumbnail?id=1BFaWjCYfj0HFeGBBDB8SmUYsZkxcEvM7&sz=w1000"
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
                st.image(foto_kelompok, use_container_width=True)

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

        GALERI = [
            {
                "emoji": "💻",
                "judul": "Kerja Kelompok & Coding",
                "deskripsi": "Momen diskusi seru di selasar gedung kampus dan kafe. Debat logika kode, revisi layout bareng, hingga sharing cemilan saat mata mulai mengantuk.",
                "foto": "https://drive.google.com/thumbnail?id=1LlKGfllyj2v536zpkPKSzsJ4tPjRcjwC&sz=w1000",
            },
            {
                "emoji": "🚩",
                "judul": "Rangkaian Acara CEO",
                "deskripsi": "Keseruan saat mengikuti dinamika materi, yel-yel kelompok, dan simulasi organisasi. Melatih kekompakan, kepemimpinan, dan mental pantang menyerah.",
                "foto": "https://drive.google.com/thumbnail?id=11UyAE4hUKZ8dG0JG3OxqZCLOrAGGDGJ_&sz=w1000",
            },
            {
                "emoji": "☕",
                "judul": "Main & Refreshing",
                "deskripsi": "Karena hidup mahasiswa bukan cuma soal deadline! Momen makan bareng, nongkrong santai, dan bercanda lepas yang bikin kami makin akrab seperti keluarga.",
                "foto": "https://drive.google.com/thumbnail?id=1tWFKgAL9u58RnOrhMx-IexoK8y_FJLXb&sz=w1000",
            },
        ]

        from html import escape as _esc

        KARTU_PER_BARIS = 3
        for start in range(0, len(GALERI), KARTU_PER_BARIS):
            cols_galeri = st.columns(KARTU_PER_BARIS, gap="medium")
            for ci, item in enumerate(GALERI[start:start + KARTU_PER_BARIS]):
                with cols_galeri[ci]:
                    with st.container(key=f"flip-card-{start + ci}"):
                        st.image(item["foto"], use_container_width=True)
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

    def about_page():
        st.markdown(
            """
            <div style="text-align: center; margin: 10px 0 20px 0;">
                <h2 style="font-size: 2.2rem; font-weight: 700; color: #ffffff; margin: 0;">Anggota Kelompok</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Menggunakan format thumbnail Google Drive
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1U9qL_kV5pRVGxwjX5vY9Ye60zewUyis1&sz=w1000",
            "https://drive.google.com/thumbnail?id=1VDxX_RUW42qOiFcx2ZzNQIOC5EVmBt9p&sz=w1000",  # wawa
            "https://drive.google.com/thumbnail?id=1JyZqi_gGn-Z0U7rbn6wm6yCff3iBAXUY&sz=w1000",  # anoy
            "https://drive.google.com/thumbnail?id=1qn7DTt5dewAf4lrewAOw1wdGqarl4Gjy&sz=w1000",  # juju
            "https://drive.google.com/thumbnail?id=1pE1AmXiK-KOvxQgsWiw8LOIJFmSC4qBt&sz=w1000",  # anya
            "https://drive.google.com/thumbnail?id=1t-jcrs_NnloNmQS9C1Yx6x79HpRA3PyC&sz=w1000",  # tingting
            "https://drive.google.com/thumbnail?id=1Q9BG3ckhXSkR241w6WQKUgks1NOisDVR&sz=w1000",  # lui
            "https://drive.google.com/thumbnail?id=1wYkTJHX0mhBy9UVW_9XoDMAvXd56xI2r&sz=w1000",  # cella
            "https://drive.google.com/thumbnail?id=1BZHhEBU0fE6kbtvuc67sUinlTB8yeKmq&sz=w1000",  # esha
            "https://drive.google.com/thumbnail?id=1WDDcHs08ui8kpk4ZgElSmS9LqSPwa3NB&sz=w1000",  # alip
            "",  # ia (ID masih kosong, sengaja dibiarkan kosong agar tidak error)
            "https://drive.google.com/thumbnail?id=13nJeccLKDvlcb9X08Vbo2ZKEjyXf0TuR&sz=w1000",  # oni
        ]

        data_list = [
            {
                "nama": "Ahmad Fadylah",
                "sebagai": "Pak lurah",
                "nim": "125450103",
                "fun_fact": "Suka ngeliatin Sunset",
                "motto_hidup": "Dalam setiap Interaksi pasti ada Komunikasi, Didalam komunikasi adakalanya terjadi Miskomunikasi, Maka dari itu butuh Evaluasi agar dalam komunikasi, tak terjadi lagi miskomunikasi",
            },
            {
                "nama": "Laikha Salwa Balqis",
                "sebagai": "Bu Lurah",
                "nim": "125450112",
                "fun_fact": "strict parents, suka hewan, suka jadi penjelajah",
                "motto_hidup": "Tenang, gausah dibikin pusing gausah dibikin ribet. Everything's gonna be ok!",
            },
            {
                "nama": "Hanifa Az'zahra",
                "sebagai": "Anggota",
                "nim": "125450001",
                "fun_fact": "Pindah kost 3 kali dlm satu semester, suka tidur dimotor",
                "motto_hidup": "Melangkah ke arah yang asing, membaca apa yang tak terucap dan yang terlihat",
            },
            {
                "nama": "Jauza Virna Radyta",
                "sebagai": "Anggota",
                "nim": "125450009",
                "fun_fact": "banyak cowo, ga punya pacar",
                "motto_hidup": "semua hal itu butuh proses bukan protes",
            },
            {
                "nama": "Lusia Zefanya Sihotang",
                "sebagai": "Anggota",
                "nim": "125450010",
                "fun_fact": "cinta piscok uin",
                "motto_hidup": "Ad Maiorem Dei Gloriam",
            },
            {
                "nama": "Enzo Hamman Albarru",
                "sebagai": "Anggota",
                "nim": "125450022",
                "fun_fact": "sarapan nasi uduk setiap hari",
                "motto_hidup": "hidup tenang, bebas nafas, nasi padang, kopi panas",
            },
            {
                "nama": "Mario Figo Dito",
                "sebagai": "Anggota",
                "nim": "125450048",
                "fun_fact": "mirip bang zaldy kata kak tanty",
                "motto_hidup": "Coba aja dulu bkakakak",
            },
            {
                "nama": "Kasih Martha Reichella",
                "sebagai": "Anggota",
                "nim": "125450060",
                "fun_fact": "Lebih suka baca novel sedih dibandingkan novel happy ending",
                "motto_hidup": "Apapun masalahnya jangan lupa buat selalu mengandalkan Tuhan",
            },
            {
                "nama": "Muhammad Reyza Fasihurahman",
                "sebagai": "Anggota",
                "nim": "125450094",
                "fun_fact": "suka belajar fisika mesin",
                "motto_hidup": "Hidup itu mudah, yang susah itu cuma ADS",
            },
            {
                "nama": "Nadira Alifa Arifin",
                "sebagai": "Anggota",
                "nim": "125450101",
                "fun_fact": " cinta kopi walau aslam",
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
                "fun_fact": "suka kesandung kalau jalan",
                "motto_hidup": "susah senang jalani saja, tapi hati hati jalan bolong, nanti kesandung",
            },
        ]

        # Tampilkan anggota secara vertikal proporsional (2 kolom) dengan efek kaca saat disentuh
        for row in range(0, len(data_list), 2):
            _pad_l, col_a, col_b, _pad_r = st.columns([1.2, 3, 3, 1.2], gap="medium")
            cols = [col_a, col_b]
            for ci in range(2):
                idx = row + ci
                if idx >= len(data_list):
                    break
                data = data_list[idx]
                url_img = gambar_urls[idx] if idx < len(gambar_urls) else ""
                nama = clean_text(data.get("nama", "Anggota"))
                sebagai = clean_text(data.get("sebagai", "Anggota"))
                nim = clean_text(data.get("nim", "-"))
                fun_fact = clean_text(data.get("fun_fact", "-"))
                motto = clean_text(data.get("motto_hidup", "-"))

                is_lurah = "lurah" in sebagai.lower()
                badge_class = "tm-lurah" if is_lurah else "tm-member"

                with cols[ci]:
                    with st.container(key=f"glass-card-{idx}"):
                        with st.container(key=f"glass-photo-{idx}"):
                            # MEMANGGIL GAMBAR LANGSUNG (Bypass load_image)
                            if url_img:
                                st.image(url_img, use_container_width=True)
                            else:
                                st.write("Gambar belum dimasukkan")

                            st.markdown(
                                f"""
                                <div class="photo-overlay">
                                    <div class="po-head">
                                        <div class="po-name">{nama}</div>
                                        <span class="tm-role {badge_class}">{sebagai}</span>
                                    </div>
                                    <div class="po-more">
                                        <div class="po-row">
                                            <span class="po-ico">🎓</span>
                                            <div>
                                                <div class="po-label">NIM</div>
                                                <div class="po-val po-mono">{nim}</div>
                                            </div>
                                        </div>
                                        <div class="po-row">
                                            <span class="po-ico">✨</span>
                                            <div>
                                                <div class="po-label">Fun Fact</div>
                                                <div class="po-val">{fun_fact}</div>
                                            </div>
                                        </div>
                                        <div class="po-quote">
                                            <span class="po-label">Motto</span>
                                            "{motto}"
                                        </div>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )

    about_page()
