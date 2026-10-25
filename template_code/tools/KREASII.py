# app.py
import random
import html
import streamlit as st

# =========================================================
# KONFIGURASI
# =========================================================
st.set_page_config(
    page_title="Kreasi Bayes — Tebak Kotak",
    page_icon="🎲",
    layout="centered",
    initial_sidebar_state="collapsed",
)

JUMLAH_RONDE = 5

# =========================================================
# STYLING (Warna Biru Lebih Cerah & Segar)
# =========================================================
st.markdown(
    """
    <style>
    /* Warna Latar Belakang Utama: Royal Blue yang lebih cerah */
    .stApp {
        background: linear-gradient(135deg, #1e3a8a 0%, #172554 100%);
        color: #f8fafc;
    }
    
    [data-testid="stSidebar"] {
        background-color: #1e3a8a;
    }

    /* Gaya Judul Bagian */
    .section-head {
        display: flex; align-items: center; justify-content: space-between;
        gap: 12px; margin-bottom: 16px;
    }
    .section-head h2 {
        margin: 0; font-size: 1.6rem; color: #ffffff;
        font-weight: 700; letter-spacing: .5px;
    }
    
    /* Chip Skor */
    .count-chip {
        background-color: #3b82f6; /* Biru cerah */
        color: #ffffff;
        padding: 6px 18px; 
        border-radius: 8px; 
        font-weight: 600;
        font-size: .9rem;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }

    /* Kartu Glassmorphism (Lebih transparan agar warna dasar terlihat) */
    .glass-card, .quiz-card, .score-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
        color: #f1f5f9;
        backdrop-filter: blur(10px);
    }
    
    /* Badge */
    .quiz-badge {
        display: inline-block;
        background: rgba(59, 130, 246, 0.25);
        color: #bfdbfe;
        border: 1px solid rgba(59, 130, 246, 0.5);
        padding: 4px 12px; 
        border-radius: 6px;
        font-size: .8rem; 
        font-weight: 700;
        margin-bottom: 12px;
    }
    
    .quiz-q { 
        font-size: 1.15rem; 
        font-weight: 500; 
        color: #f8fafc; 
        margin: 8px 0 16px; 
    }
    
    /* Kotak A & B */
    .box-grid {
        display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px;
    }
    .box-card {
        background: rgba(255, 255, 255, 0.1); /* Lebih terang dari background utama */
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 10px; 
        padding: 20px; 
        text-align: center;
    }
    .box-name { 
        font-weight: 600; 
        color: #93c5fd; 
        margin-bottom: 12px; 
        font-size: 1.1rem;
    }
    .balls { 
        font-size: 1.8rem; 
        letter-spacing: 6px; 
    }
    
    /* Tombol Feedback */
    .fb-ok, .fb-no {
        border-radius: 10px; 
        padding: 16px 20px; 
        margin-top: 16px;
        line-height: 1.6;
        font-size: 1rem;
    }
    .fb-ok {
        background: rgba(16,185,129,.15);
        border-left: 4px solid #10b981;
        color: #d1fae5;
    }
    .fb-no {
        background: rgba(239,68,68,.15);
        border-left: 4px solid #ef4444;
        color: #fee2e2;
    }
    
    /* Skor Akhir */
    .score-big {
        font-size: 3.5rem; 
        font-weight: 800;
        color: #60a5fa; 
        margin: 10px 0;
        text-shadow: 0 0 20px rgba(96, 165, 250, 0.5);
    }
    
    /* Tombol Radio Pilihan Jawaban */
    div[role="radiogroup"] {
        gap: 10px !important;
    }
    div[role="radiogroup"] > label {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        padding: 12px 20px !important;
        border-radius: 8px !important;
        color: #f8fafc !important;
        transition: all 0.2s ease;
    }
    div[role="radiogroup"] > label:hover {
        border-color: #60a5fa !important;
        background-color: rgba(59, 130, 246, 0.2) !important;
    }
    
    /* Tombol Streamlit */
    .stButton > button {
        background: linear-gradient(to right, #3b82f6, #2563eb);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.2s ease;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(to right, #60a5fa, #3b82f6);
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.5);
    }
    .stButton > button:disabled {
        background: #475569;
        color: #94a3b8;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        color: #bfdbfe !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# LOGIKA GAME (Tidak Ada Perubahan)
# =========================================================
def persen(a, b):
    total = a + b
    if total == 0:
        return 0
    return round(100 * a / total)

def buat_ronde():
    pasangan = [(x, y) for x in (1, 2, 3) for y in (1, 2, 3) if x != y]
    ronde = []
    for x, y in random.sample(pasangan, JUMLAH_RONDE):
        benar = persen(x, y)
        salah = []
        kandidat = [50, x * 25, persen(y, x), 25, 33, 40, 60, 67, 75, 80]
        for v in kandidat:
            if v != benar and v not in salah:
                salah.append(v)
            if len(salah) == 3:
                break
        nilai = salah + [benar]
        random.shuffle(nilai)
        ronde.append({
            "x": x,
            "y": y,
            "benar": benar,
            "opsi": [f"{v}%" for v in nilai],
            "jawaban": f"{benar}%",
        })
    return ronde

def reset_game():
    st.session_state.k2_ronde_list = buat_ronde()
    st.session_state.k2_i = 0
    st.session_state.k2_skor = 0
    st.session_state.k2_sudah = False
    st.session_state.k2_ronde = st.session_state.get("k2_ronde", 0) + 1

def bola(biru):
    biru = max(0, min(4, biru))
    return "🔵" * biru + "🔴" * (4 - biru)

# =========================================================
# HALAMAN GAME
# =========================================================
def game_page():
    if "k2_ronde_list" not in st.session_state:
        reset_game()

    daftar = st.session_state.k2_ronde_list
    total = len(daftar)
    i = st.session_state.k2_i
    skor = st.session_state.k2_skor
    sudah = st.session_state.k2_sudah

    st.markdown(
        '<div class="section-head"><h2>Kreasi 2 — Tebak Kotak Bayes</h2>'
        f'<span class="count-chip">Skor {skor}</span></div>',
        unsafe_allow_html=True,
    )
    
    st.markdown(
        '<div class="glass-card">'
        '<b style="color:#bfdbfe; font-size:1.1rem;">Apa itu Teorema Bayes?</b><br><br>'
        'Kita mulai dari tebakan awal, lalu <b>memperbarui</b> tebakan itu setelah melihat bukti baru. '
        'Di game ini: dua kotak (A dan B) dipilih secara acak (peluang awal 50 : 50), lalu diambil satu bola 🔵. '
        'Berapa peluang bola itu berasal dari <b>Kotak A</b>?'
        '</div>',
        unsafe_allow_html=True,
    )
    st.write("")

    if i >= total:
        if skor == total:
            pesan = "Luar biasa! Kamu sudah paham cara kerja Bayes 🎉"
        elif skor >= 3:
            pesan = "Bagus! Tinggal sedikit lagi jadi master Bayesian."
        else:
            pesan = "Tenang, coba lagi. Ingat: hitung semua bola biru dulu!"
        st.markdown(
            '<div class="quiz-card score-card" style="text-align: center;">'
            '<div class="quiz-badge">Hasil Akhir</div>'
            f'<div class="score-big">{skor} / {total}</div>'
            f'<p class="quiz-q" style="margin-top:14px;">{html.escape(pesan)}</p>'
            '</div>',
            unsafe_allow_html=True,
        )
        if st.button("🔄 Main lagi", key="k2_ulang"):
            reset_game()
            st.rerun()
        return

    r = daftar[i]
    st.progress(i / total)
    st.markdown(
        '<div class="quiz-card">'
        f'<div class="quiz-badge">Ronde {i + 1} dari {total}</div>'
        '<p class="quiz-q">Kamu mengambil 1 bola 🔵. Berapa peluang bola itu dari Kotak A?</p>'
        '<div class="box-grid">'
        f'<div class="box-card"><div class="box-name">Kotak A</div><div class="balls">{bola(r["x"])}</div></div>'
        f'<div class="box-card"><div class="box-name">Kotak B</div><div class="balls">{bola(r["y"])}</div></div>'
        '</div></div>',
        unsafe_allow_html=True,
    )

    with st.expander("💡 Petunjuk"):
        st.write(
            "Hitung dulu ada berapa bola biru di kedua kotak. "
            "Peluang = bola biru di Kotak A ÷ total bola biru."
        )

    pilihan = st.radio(
        "Pilih jawaban",
        r["opsi"],
        index=None,
        key=f"k2_radio_{st.session_state.k2_ronde}_{i}",
        label_visibility="collapsed",
        disabled=sudah,
        horizontal=True,
    )

    if not sudah:
        if st.button(
            "Jawab",
            key=f"k2_jawab_{st.session_state.k2_ronde}_{i}",
            disabled=pilihan is None,
        ):
            st.session_state.k2_sudah = True
            if pilihan == r["jawaban"]:
                st.session_state.k2_skor += 1
            st.rerun()
        return

    penjelasan = (
        f'Total bola 🔵 = {r["x"]} + {r["y"]} = <b>{r["x"] + r["y"]}</b>. '
        f'Yang dari Kotak A = <b>{r["x"]}</b>. '
        f'Jadi peluangnya = {r["x"]}/{r["x"] + r["y"]} ≈ <b>{r["benar"]}%</b>.'
    )
    if pilihan == r["jawaban"]:
        st.markdown(
            f'<div class="fb-ok"><b>✅ Benar!</b><br>{penjelasan}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="fb-no"><b>❌ Belum tepat.</b><br>{penjelasan}</div>',
            unsafe_allow_html=True,
        )

    label = "Lihat Hasil ➜" if i == total - 1 else "Ronde berikutnya ➜"
    if st.button(label, key=f"k2_lanjut_{st.session_state.k2_ronde}_{i}"):
        st.session_state.k2_i += 1
        st.session_state.k2_sudah = False
        st.rerun()

# =========================================================
# ENTRY POINT
# =========================================================
if __name__ == "__main__":
    game_page()
