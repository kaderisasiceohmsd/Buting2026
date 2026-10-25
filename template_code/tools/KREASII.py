import streamlit as st
import numpy as np
import sys
import os

# Menambahkan root project ke sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from tools.ui_helper import inject_custom_css

inject_custom_css()

# Header Halaman Kreasi 1
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 24px; padding-top: 10px;">
        <span class="g-tag">📘 KREASI 1 • SAINS DATA & KOMPUTASI</span>
        <h1 class="g-title" style="font-size: 2.8rem; margin: 8px 0 4px 0;">
            MENGENAL TENSOR
        </h1>
        <p style="color: #c4b5fd; font-size: 1.05rem; margin: 0;">
            Panduan Santai & Mudah Dipahami tentang Wadah Data Multidimensi di Era AI
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Tab Pembahasan Materi Santai & Aplikatif
tab1, tab2, tab3 = st.tabs([
    "💡 1. Apa itu Tensor? (Analogi Santai)",
    "📱 2. Digunakan Buat Apa Aja?",
    "📊 3. Hubungannya dengan Sains Data",
])

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1: APA ITU TENSOR? (ANALOGI SEHARI-HARI)
# ─────────────────────────────────────────────────────────────────────────────
with tab1:
    st.markdown(
        """
        <div class="g-card">
            <h3 style="color: #ffffff; margin-top: 0; font-size: 1.35rem;">
                Gak Usah Pusing Dulu! Yuk Pahami Tensor Lewat Makanan & Kehidupan Sehari-hari 🍲
            </h3>
            <p style="color: #cbd5e1; line-height: 1.8; font-size: 0.98rem; text-align: justify;">
                Di telinga orang awam, kata <b>"Tensor"</b> mungkin terdengar seperti rumus matematika rumit yang bikin kepala pusing. 
                Padahal intinya sangat sederhana: <b>Tensor adalah wadah kotak untuk menyimpan data angka</b>. 
                Bentuk wadahnya bisa dari yang paling kecil (cuma 1 titik), memanjang, berwujud tabel, sampai bertumpuk-tumpuk!
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 4 Tingkatan Dimensi dengan Analogi Lucu & Jelas
    col_a1, col_a2 = st.columns(2, gap="medium")

    with col_a1:
        st.markdown(
            """
            <div class="g-card" style="height: 100%;">
                <div style="font-size: 2rem; margin-bottom: 4px;">🧋 0 Dimensi: Skalar (Scalar)</div>
                <div style="color: #c4b5fd; font-weight: 700; font-size: 0.95rem; margin-bottom: 6px;">
                    Analogi: 1 Butir Boba Tunggal
                </div>
                <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.6; margin: 0;">
                    Skalar adalah <b>cuma 1 angka saja</b>. Dia tidak punya arah ataupun tabel panjang.<br><br>
                    <b>Contoh Nyata:</b><br>
                    • Suhu ruangan: <code>28°C</code><br>
                    • Nilai kuis kamu: <code>100</code><br>
                    • Harga secangkir kopi: <code>Rp 18.000</code>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_a2:
        st.markdown(
            """
            <div class="g-card" style="height: 100%;">
                <div style="font-size: 2rem; margin-bottom: 4px;">🍢 1 Dimensi: Vektor (Vector)</div>
                <div style="color: #c4b5fd; font-weight: 700; font-size: 0.95rem; margin-bottom: 6px;">
                    Analogi: 1 Tusuk Sate / Antrean Kasir
                </div>
                <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.6; margin: 0;">
                    Vektor adalah <b>deretan angka yang memanjang 1 arah</b> (seperti garis atau daftar belanjaan).<br><br>
                    <b>Contoh Nyata:</b><br>
                    • Daftar tinggi badan 4 teman: <code>[165, 170, 175, 168]</code><br>
                    • Riwayat pengeluaran harian selama seminggu.<br>
                    • Posisi koordinat GPS: <code>[Latitude, Longitude]</code>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    col_a3, col_a4 = st.columns(2, gap="medium")

    with col_a3:
        st.markdown(
            """
            <div class="g-card" style="height: 100%;">
                <div style="font-size: 2rem; margin-bottom: 4px;">🧇 2 Dimensi: Matriks (Matrix)</div>
                <div style="color: #c4b5fd; font-weight: 700; font-size: 0.95rem; margin-bottom: 6px;">
                    Analogi: Papan Catur / Loyang Martabak 8 Rasa
                </div>
                <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.6; margin: 0;">
                    Matriks adalah kumpulan angka yang punya <b>Baris dan Kolom</b> (seperti tabel Excel).<br><br>
                    <b>Contoh Nyata:</b><br>
                    • Tabel nilai raport: Baris = Nama Siswa, Kolom = Mata Pelajaran.<br>
                    • Foto hitam-putih jadul: Setiap kotak pixel punya nilai tingkat kegelapan.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_a4:
        st.markdown(
            """
            <div class="g-card" style="height: 100%;">
                <div style="font-size: 2rem; margin-bottom: 4px;">🍰 3D & 4D: Tensor Multidimensi</div>
                <div style="color: #c4b5fd; font-weight: 700; font-size: 0.95rem; margin-bottom: 6px;">
                    Analogi: Kue Lapis Bertingkat / Video Klip
                </div>
                <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.6; margin: 0;">
                    Bayangkan beberapa lembar tabel 2D kamu tumpuk jadi tebal seperti kubus balok!<br><br>
                    <b>Contoh Nyata:</b><br>
                    • <b>Foto Berwarna (3D Tensor):</b> Punya Tinggi $\\times$ Lebar $\\times$ 3 Lapis Warna (Merah, Hijau, Biru).<br>
                    • <b>Video TikTok (4D Tensor):</b> Kumpulan foto berwarna 3D yang bergerak tiap detik waktu!
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown(
        """
        <div class="g-card" style="border-left: 3px solid #8b5cf6;">
            <b>Kesimpulan Singkat:</b> Skalar, Vektor, dan Matriks sebenarnya adalah <b>anggota keluarga Tensor</b>. 
            Skalar itu Tensor 0D, Vektor itu Tensor 1D, Matriks itu Tensor 2D, dan saat dimensinya ada 3 atau lebih, kita sebut sebagai Tensor Tingkat Tinggi!
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────────────────────────────────────
# TAB 2: DIGUNAKAN BUAT APA AJA?
# ─────────────────────────────────────────────────────────────────────────────
with tab2:
    st.markdown(
        """
        <div class="g-card">
            <h3 style="color: #ffffff; margin-top: 0; font-size: 1.35rem;">
                Tanpa Disadari, Tensor Ada di Setiap Aplikasi yang Kamu Pakai Tiap Hari! 📲
            </h3>
            <p style="color: #cbd5e1; line-height: 1.7; font-size: 0.95rem;">
                Komputer atau HP kita sebenarnya tidak tahu apa itu "wajah ganteng", "suara musik", atau "kalimat chat". 
                Semua hal di dunia digital diubah jadi angka tensor agar bisa diproses:
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_u1, col_u2 = st.columns(2, gap="medium")

    with col_u1:
        st.markdown(
            """
            <div class="g-card" style="height: 100%;">
                <div style="font-size: 1.8rem; margin-bottom: 6px;">📸 1. Filter Wajah & Kamera HP</div>
                <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.7; margin: 0;">
                    Saat kamu foto selfie atau pakai filter Instagram, kamera mengubah wajahmu menjadi <b>Tensor 3D (Tinggi x Lebar x 3 Warna RGB)</b>. 
                    Filter membuat kulit lebih mulus atau menambahkan efek kacamata hanya dengan mengalikan angka-angka di dalam tensor tersebut!
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_u2:
        st.markdown(
            """
            <div class="g-card" style="height: 100%;">
                <div style="font-size: 1.8rem; margin-bottom: 6px;">🤖 2. ChatGPT & Otak AI</div>
                <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.7; margin: 0;">
                    Pernah mikir gimana cara AI paham bahasa manusia? Kata-kata kita diubah menjadi deretan vektor angka yang disebut <i>embeddings</i>. 
                    Seluruh proses penalaran ChatGPT berjalan dengan memproses jutaan perkalian tensor secara instan!
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    col_u3, col_u4 = st.columns(2, gap="medium")

    with col_u3:
        st.markdown(
            """
            <div class="g-card" style="height: 100%;">
                <div style="font-size: 1.8rem; margin-bottom: 6px;">🎵 3. Rekomendasi Spotify & YouTube</div>
                <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.7; margin: 0;">
                    Kenapa lagu rekomendasi di Spotify sering pas banget sama selera kita? 
                    Sistem algoritma menggunakan tensor berordo 3: <code>(User x Lagu x Waktu Mendengarkan)</code> untuk mencari pola musik kesukaanmu.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_u4:
        st.markdown(
            """
            <div class="g-card" style="height: 100%;">
                <div style="font-size: 1.8rem; margin-bottom: 6px;">🚗 4. Mobil Pintar Otomatis (Self-Driving)</div>
                <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.7; margin: 0;">
                    Mobil cerdas seperti Tesla membaca jalan raya menggunakan kamera 360 derajat. 
                    Rekaman video jalanan adalah <b>Tensor 4D</b> (Waktu x Tinggi x Lebar x Warna) yang diproses dalam hitungan milidetik agar mobil tidak menabrak.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ─────────────────────────────────────────────────────────────────────────────
# TAB 3: HUBUNGANNYA DENGAN SAINS DATA
# ─────────────────────────────────────────────────────────────────────────────
with tab3:
    st.markdown(
        """
        <div class="g-card">
            <h3 style="color: #ffffff; margin-top: 0; font-size: 1.35rem;">
                Kenapa Mahasiswa Sains Data Belajar Tensor? 🎓
            </h3>
            <p style="color: #cbd5e1; line-height: 1.8; font-size: 0.98rem; text-align: justify;">
                Di masa lalu, pengolah data cuma berurusan dengan tabel biasa (seperti data sensus penduduk di Excel). 
                Tapi di era digital sekarang, data yang harus diolah seorang <b>Data Scientist</b> bentuknya bermacam-macam: 
                ada gambar satelit, rekaman suara voice-note, riwayat transaksi jutaan orang, hingga grafik interaksi sosial media.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="g-card" style="margin-bottom: 14px;">
            <div style="font-weight: 700; color: #c4b5fd; font-size: 1.05rem; margin-bottom: 6px;">
                1. Menangani Data Kompleks Tanpa Kehilangan Informasi
            </div>
            <div style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.7;">
                Kalau kita paksa foto atau rekaman video dijadikan tabel 2D biasa, informasi hubungan ruang dan waktunya bakal rusak. 
                Dengan tensor, data multidimensi bisa disimpan dan dianalisis sesuai bentuk aslinya.
            </div>
        </div>

        <div class="g-card" style="margin-bottom: 14px;">
            <div style="font-weight: 700; color: #c4b5fd; font-size: 1.05rem; margin-bottom: 6px;">
                2. Bahasa Utama Framework Populer (TensorFlow & PyTorch)
            </div>
            <div style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.7;">
                Dua senjata utama praktisi Sains Data dan Machine Learning di dunia industri adalah <b>TensorFlow</b> (milik Google) 
                dan <b>PyTorch</b> (milik Meta). Keduanya bekerja 100% menggunakan operasi tensor! Jadi paham tensor adalah modal wajib anak Sains Data.
            </div>
        </div>

        <div class="g-card">
            <div style="font-weight: 700; color: #c4b5fd; font-size: 1.05rem; margin-bottom: 6px;">
                3. Bikin Komputasi Super Cepat Berkat GPU
            </div>
            <div style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.7;">
                GPU (kartu grafis) dan TPU (Tensor Processing Unit) punya inti khusus bernama <i>Tensor Cores</i>. 
                Hardware ini dirancang untuk menghitung jutaan angka tensor secara serentak (paralel), sehingga model AI yang tadinya butuh waktu berminggu-minggu bisa selesai dilatih hanya dalam beberapa jam!
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
