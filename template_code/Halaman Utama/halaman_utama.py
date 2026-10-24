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
                <div style="font-size: 0.95rem; color: #a78bfa; margin-top: 4px;">✨ Langkah, Karya, & Semangat Juang Kelompok Tensor</div>
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
                <span class="g-tag">⚡ JARGON KEBANGGAAN KELOMPOK TENSOR ⚡</span>
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
                <span class="g-tag">📸 Official Team Portrait</span>
                <div style="font-size: 1.3rem; font-weight: 700; color: #ffffff; margin-top: 6px;">Keluarga Besar Kelompok Tensor</div>
                <div style="font-size: 0.82rem; color: #94a3b8; margin-top: 2px;">(Sentuh / arahkan kursor ke foto untuk melihat efek kilau kaca)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns([0.4, 3.2, 0.4])
        with col2:
            st.markdown('<div class="glass-photo-wrap">', unsafe_allow_html=True)
            img_kelompok = load_image(foto_kelompok, fallback_name="Foto Kelompok Tensor", keep_ratio=True)
            st.image(img_kelompok, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.write("")

        # --- GALERI MOMEN: KERJA KELOMPOK, RANGKAIAN, & HANGOUT ---
        st.markdown(
            """
            <div style="text-align: center; margin: 28px 0 18px 0;">
                <span class="g-tag">🎞️ Behind The Scene & Moments</span>
                <h3 style="font-size: 1.85rem; font-weight: 700; color: #ffffff; margin: 6px 0 4px 0;">Galeri Kebersamaan Kami</h3>
                <p style="color: #94a3b8; font-size: 0.9rem; margin: 0;">Dari nugas larut malam, serunya dinamika lapangan, hingga tawa pelepas penat.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col_m1, col_m2, col_m3 = st.columns(3, gap="medium")

        with col_m1:
            st.markdown(
                """
                <div class="glass-box" style="padding: 16px; text-align: center; margin-bottom: 12px;">
                    <div style="font-size: 1.6rem; margin-bottom: 4px;">💻</div>
                    <div style="font-weight: 700; color: #f1f5f9; font-size: 1rem; margin-bottom: 6px;">Kerja Kelompok & Coding</div>
                    <p style="color: #94a3b8; font-size: 0.83rem; line-height: 1.6; margin: 0;">
                        Momen diskusi seru di selasar gedung kampus dan kafe. Debat logika kode, revisi layout bareng, hingga sharing cemilan saat mata mulai mengantuk.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            # Slot foto kerja kelompok
            foto_nugas = "https://drive.google.com/uc?export=view&id=19fo5WQL02HB7IzvRUwhNoKySjy6uJ_Lv"
            st.markdown('<div class="glass-photo-wrap">', unsafe_allow_html=True)
            img_nugas = load_image(foto_nugas, fallback_name="Kerja Kelompok", keep_ratio=True)
            st.image(img_nugas, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_m2:
            st.markdown(
                """
                <div class="glass-box" style="padding: 16px; text-align: center; margin-bottom: 12px;">
                    <div style="font-size: 1.6rem; margin-bottom: 4px;">🚩</div>
                    <div style="font-weight: 700; color: #f1f5f9; font-size: 1rem; margin-bottom: 6px;">Rangkaian Acara CEO</div>
                    <p style="color: #94a3b8; font-size: 0.83rem; line-height: 1.6; margin: 0;">
                        Keseruan saat mengikuti dinamika materi, yel-yel kelompok, dan simulasi organisasi. Melatih kekompakan, kepemimpinan, dan mental pantang menyerah.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            # Slot foto kegiatan rangkaian
            foto_rangkaian = "https://drive.google.com/uc?export=view&id=11UyAE4hUKZ8dG0JG3OxqZCLOrAGGDGJ_"
            st.markdown('<div class="glass-photo-wrap">', unsafe_allow_html=True)
            img_rangkaian = load_image(foto_rangkaian, fallback_name="Rangkaian Acara", keep_ratio=True)
            st.image(img_rangkaian, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_m3:
            st.markdown(
                """
                <div class="glass-box" style="padding: 16px; text-align: center; margin-bottom: 12px;">
                    <div style="font-size: 1.6rem; margin-bottom: 4px;">☕</div>
                    <div style="font-weight: 700; color: #f1f5f9; font-size: 1rem; margin-bottom: 6px;">Main & Refreshing</div>
                    <p style="color: #94a3b8; font-size: 0.83rem; line-height: 1.6; margin: 0;">
                        Karena hidup mahasiswa bukan cuma soal deadline! Momen makan bareng, nongkrong santai, dan bercanda lepas yang bikin kami makin akrab seperti keluarga.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            # Slot foto hangout/main
            foto_main = "https://drive.google.com/uc?export=view&id=1tWFKgAL9u58RnOrhMx-IexoK8y_FJLXb"
            st.markdown('<div class="glass-photo-wrap">', unsafe_allow_html=True)
            img_main = load_image(foto_main, fallback_name="Main & Hangout", keep_ratio=True)
            st.image(img_main, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.write("")

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
                <div style="font-size: 0.95rem; color: #a78bfa; margin-top: 4px;">Kenali orang-orang di balik pembuatan Buku Kating Tensor</div>
                <div style="font-size: 0.82rem; color: #94a3b8; margin-top: 2px;">(Setiap kartu dilengkapi efek kaca halus saat disentuh)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rJzgdR7_6woOOUN1rxC_kR5RDAex8rYC",  # Foto Anggota 1
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  # Foto Anggota 2
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  # Foto Anggota 3
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  # Foto Anggota 4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  # Foto Anggota 5
        ]

        data_list = [
            {
                "nama": "Ahmad Fadylah",
                "sebagai": "Pak lurah",
                "nim": "124450103",
                "fun_fact": "Suka ngeliatin Sunset",
                "motto_hidup": "Nothing is impossible",
            },
            {
                "nama": "Laikha Salwa Balqis",
                "sebagai": "Bu Lurah",
                "nim": "124450122",
                "fun_fact": "Suka ngoding sampai pagi",
                "motto_hidup": "Tetap santuy walaupun error banyak",
            },
            {
                "nama": "",
                "sebagai": "Anggota",
                "nim": "12445xxxx",
                "fun_fact": "[Isi Fun Fact]",
                "motto_hidup": "[Isi Motto]",
            },
            {
                "nama": "[Nama Teman 4]",
                "sebagai": "Anggota",
                "nim": "12445xxxx",
                "fun_fact": "[Isi Fun Fact]",
                "motto_hidup": "[Isi Motto]",
            },
            {
                "nama": "[Nama Teman 5]",
                "sebagai": "Anggota",
                "nim": "12445xxxx",
                "fun_fact": "[Isi Fun Fact]",
                "motto_hidup": "[Isi Motto]",
            },
        ]

        # Tampilkan anggota secara vertikal proporsional (2 kolom) dengan efek kaca saat disentuh
        for row in range(0, len(data_list), 2):
            cols = st.columns(2, gap="large")
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
                    # Pembungkus Kartu Kaca (Glass Card)
                    st.markdown(
                        f"""
                        <div class="glass-box" style="margin-bottom: 24px; padding: 16px;">
                        """,
                        unsafe_allow_html=True,
                    )

                    # Foto vertikal di atas dengan efek kaca
                    st.markdown('<div class="glass-photo-wrap">', unsafe_allow_html=True)
                    img = load_image(url_img, fallback_name=nama)
                    st.image(img, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Biodata rapi di bawah foto
                    st.markdown(
                        f"""
                            <div style="margin-top: 14px;">
                                <div class="tm-name">{nama}</div>
                                <span class="tm-role {badge_class}">{sebagai}</span>
                                <div class="k-sep"></div>
                                <div class="k-info"><span class="k-info-label">NIM:</span><span class="k-info-val">{nim}</span></div>
                                <div class="k-info"><span class="k-info-label">Fun Fact:</span><span class="k-info-val">{fun_fact}</span></div>
                                <div class="k-info"><span class="k-info-label">Motto:</span><span class="k-info-val" style="font-style: italic;">"{motto}"</span></div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

    about_page()
