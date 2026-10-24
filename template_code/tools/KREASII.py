import streamlit as st
import random
import sys
import os

# Menambahkan root project ke sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from tools.ui_helper import inject_custom_css

inject_custom_css()

# Header Game Tensor
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 20px; padding-top: 10px;">
        <span class="g-tag">🎮 KREASI 2 • MINI GAME SANTAI</span>
        <h1 class="g-title" style="font-size: 2.8rem; margin: 8px 0 4px 0;">
            TEBAK DIMENSI TENSOR!
        </h1>
        <p style="color: #c4b5fd; font-size: 1.05rem; margin: 0;">
            Edisi Benda Sehari-hari & Kehidupan Kampus • Gampang, Seru, dan Bikin Paham! 🎯
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Kumpulan Soal Ringan, Lucu, dan Relatable
SOAL_LIST = [
    {
        "benda": "🍲 Satu butir telur puyuh bulat di dalam mangkok bakso",
        "jawaban": "0D (Skalar)",
        "alasan": "Telur puyuh cuma ada 1 butir tunggal tanpa panjang tabel ataupun arah, jadi dia 0 Dimensi alias Skalar!",
        "hint": "Cuma 1 angka/biji tunggal",
    },
    {
        "benda": "🚶‍♂️🚶‍♀️ Satu garis antrean ayam geprek pas jam istirahat siang",
        "jawaban": "1D (Vektor)",
        "alasan": "Antrean geprek memanjang lurus dalam 1 baris urutan, persis seperti Vektor 1 Dimensi!",
        "hint": "Deretan satu arah",
    },
    {
        "benda": "🧇 Loyang martabak manis 8 rasa yang dipotong kotak-kotak",
        "jawaban": "2D (Matriks)",
        "alasan": "Punya baris dan kolom potongan kotak yang membentuk bidang datar, ini konsep Matriks 2 Dimensi!",
        "hint": "Punya baris dan kolom",
    },
    {
        "benda": "📸 Foto selfie berwarna (RGB) kamu dan teman-teman di HP",
        "jawaban": "3D (Tensor 3D)",
        "alasan": "Foto berwarna punya Tinggi x Lebar x 3 Lapis Warna (Merah, Hijau, Biru), jadi ada 3 dimensi data!",
        "hint": "Bidang gambar yang punya lapisan warna",
    },
    {
        "benda": "🎬 Video TikTok / Reels Instagram 30 detik yang kamu tonton pas jam kosong",
        "jawaban": "4D (Tensor 4D)",
        "alasan": "Video adalah tumpukan foto 3D berwarna yang bergerak seiring berjalannya detik waktu! Jadi ada 4 dimensi!",
        "hint": "Foto berwarna yang punya dimensi durasi waktu",
    },
    {
        "benda": "⭐ Skor IPK impian kamu di semester ini (misal: 3.90)",
        "jawaban": "0D (Skalar)",
        "alasan": "IPK adalah satu angka nilai tunggal tanpa tabel atau dimensi arah, jadi pasti Skalar 0D!",
        "hint": "Hanya 1 angka besaran",
    },
    {
        "benda": "☕ Satu renceng sachet kopi instan yang digantung lurus di warung",
        "jawaban": "1D (Vektor)",
        "alasan": "Sachet kopi tergantung berderet dari atas ke bawah dalam 1 baris lurus memanjang = Vektor 1D!",
        "hint": "Deretan memanjang 1 garis",
    },
    {
        "benda": "📅 Jadwal kuliah mingguan (Baris: Jam Kuliah, Kolom: Hari Senin-Jumat)",
        "jawaban": "2D (Matriks)",
        "alasan": "Tabel jadwal kuliah tersusun dari baris jam dan kolom hari, ini adalah representasi Matriks 2D!",
        "hint": "Tabel baris x kolom",
    },
    {
        "benda": "🍰 Satu kotak kue lapis legit bertingkat warna-warni",
        "jawaban": "3D (Tensor 3D)",
        "alasan": "Kue lapis punya panjang, lebar, dan ketebalan lapisan rasa bertingkat ke atas, ini bentuk nyata Tensor 3D!",
        "hint": "Punya panjang, lebar, dan ketebalan lapis",
    },
    {
        "benda": "📹 Rekaman CCTV gedung kuliah selama 24 jam penuh",
        "jawaban": "4D (Tensor 4D)",
        "alasan": "CCTV merekam visual berwarna (3D) yang terus berjalan sepanjang 24 jam waktu (4D)!",
        "hint": "Visual citra 3D ditambah dimensi rekaman waktu",
    },
]

# State Management Game
if "game_round" not in st.session_state:
    st.session_state.game_round = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "feedback_msg" not in st.session_state:
    st.session_state.feedback_msg = ""
if "is_correct" not in st.session_state:
    st.session_state.is_correct = False

# Pilihan Jawaban
PILIHAN_DIMENSI = [
    "0D (Skalar)",
    "1D (Vektor)",
    "2D (Matriks)",
    "3D (Tensor 3D)",
    "4D (Tensor 4D)",
]

# Total Soal per Game Session
TOTAL_SOAL = 8

if st.session_state.game_round < TOTAL_SOAL:
    soal = SOAL_LIST[st.session_state.game_round % len(SOAL_LIST)]

    # Status Bar
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.markdown(f"**Pertanyaan:** `{st.session_state.game_round + 1} / {TOTAL_SOAL}`")
    with col_s2:
        st.markdown(f"**Skor Kamu:** `<b style='color: #c4b5fd;'>{st.session_state.score} Poin</b>`", unsafe_allow_html=True)
    with col_s3:
        combo_txt = f"🔥 {st.session_state.streak}x Combo!" if st.session_state.streak > 1 else "Semangat!"
        st.markdown(f"**Status:** {combo_txt}")

    st.progress((st.session_state.game_round + 1) / TOTAL_SOAL)
    st.write("")

    # Kotak Soal Benda
    st.markdown(
        f"""
        <div class="g-card" style="text-align: center; padding: 24px;">
            <div style="font-size: 0.82rem; color: #a78bfa; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">
                Tebak, Benda Ini Termasuk Dimensi Berapa?
            </div>
            <h3 style="color: #ffffff; font-size: 1.35rem; font-weight: 700; margin: 4px 0 12px 0;">
                {soal['benda']}
            </h3>
            <div style="font-size: 0.85rem; color: #94a3b8; font-style: italic;">
                💡 Petunjuk: {soal['hint']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Tombol Pilihan Jawaban
    if not st.session_state.answered:
        st.markdown("<div style='text-align: center; margin-bottom: 10px; color: #cbd5e1; font-size: 0.9rem;'>Pilih tebakanmu di bawah ini:</div>", unsafe_allow_html=True)
        cols_btn = st.columns(len(PILIHAN_DIMENSI))
        for idx, pil in enumerate(PILIHAN_DIMENSI):
            with cols_btn[idx]:
                if st.button(pil, key=f"btn_{st.session_state.game_round}_{idx}", use_container_width=True):
                    st.session_state.answered = True
                    if pil == soal["jawaban"]:
                        st.session_state.is_correct = True
                        st.session_state.streak += 1
                        st.session_state.score += 10 + (st.session_state.streak * 5)
                        st.session_state.feedback_msg = f"🎉 <b>BENAR BANGET!</b> {soal['alasan']}"
                    else:
                        st.session_state.is_correct = False
                        st.session_state.streak = 0
                        st.session_state.feedback_msg = f"😅 <b>Kurang tepat!</b> Jawaban yang benar adalah <b>{soal['jawaban']}</b>. {soal['alasan']}"
                    st.rerun()

    else:
        # Tampilkan Feedback
        if st.session_state.is_correct:
            st.success(st.session_state.feedback_msg)
        else:
            st.warning(st.session_state.feedback_msg)

        st.write("")
        if st.button("Lanjut ke Benda Berikutnya ➔", use_container_width=True):
            st.session_state.game_round += 1
            st.session_state.answered = False
            st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# GAME SELESAI / HASIL AKHIR
# ─────────────────────────────────────────────────────────────────────────────
else:
    st.balloons()
    col_e1, col_e2, col_e3 = st.columns([1, 2.4, 1])
    with col_e2:
        st.markdown(
            f"""
            <div class="g-card" style="text-align: center; padding: 28px;">
                <div style="font-size: 3.5rem; margin-bottom: 6px;">🏆✨</div>
                <h2 style="color: #ffffff; margin: 0 0 6px 0;">PERMAINAN SELESAI!</h2>
                <div style="font-size: 1.15rem; color: #c4b5fd; font-weight: 700; margin-bottom: 12px;">
                    Kamu Hebat! Sekarang Sudah Resmi Paham Dimensi Tensor!
                </div>
                <div style="font-size: 2.2rem; font-weight: 800; color: #f8fafc; margin: 14px 0;">
                    Total Skor: <span style="color: #c4b5fd;">{st.session_state.score}</span> Poin
                </div>
                <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.7; margin: 0;">
                    Ternyata belajar konsep Tensor itu gak perlu pusing kan? 
                    Mulai dari telur puyuh (0D), antrean geprek (1D), loyang martabak (2D), foto selfie (3D), 
                    sampai video TikTok (4D), semuanya adalah bagian dari dunia data!
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")
        if st.button("🔄 Main Lagi dari Awal", use_container_width=True):
            st.session_state.game_round = 0
            st.session_state.score = 0
            st.session_state.streak = 0
            st.session_state.answered = False
            st.session_state.feedback_msg = ""
            st.session_state.is_correct = False
            st.rerun()
