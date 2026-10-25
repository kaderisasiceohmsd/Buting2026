import streamlit as st
import random
import time

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title="🃏 Memory Card Kelompok",
    page_icon="🃏",
    layout="wide",
)

# ============================================================
# CSS CUSTOM
# ============================================================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 45%, #6a3093 100%);
        background-attachment: fixed;
    }
    .game-header {
        background: rgba(255,255,255,0.12);
        backdrop-filter: blur(14px);
        border-radius: 20px;
        padding: 24px 30px;
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.25);
        box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    }
    .game-header h1 { margin: 0; font-size: 2.4em; color: #fff;
                      text-shadow: 0 2px 10px rgba(0,0,0,0.3); }
    .game-header p  { margin: 8px 0 0 0; color: rgba(255,255,255,0.85); font-size: 1.05em; }

    .stat-box {
        background: rgba(255,255,255,0.15);
        border-radius: 14px;
        padding: 15px 10px;
        text-align: center;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255,255,255,0.22);
        margin-bottom: 12px;
    }
    .stat-box .val { font-size: 1.8em; font-weight: 800; color: #fff; line-height: 1.1; }
    .stat-box .lbl { font-size: 0.82em; color: rgba(255,255,255,0.8); margin-top: 4px; }

    /* Tombol kartu tertutup */
    div[data-testid="stButton"] > button {
        width: 100% !important;
        height: 130px !important;
        border-radius: 18px !important;
        font-size: 2.2em !important;
        font-weight: 700 !important;
        border: 3px solid rgba(255,255,255,0.3) !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
    }
    div[data-testid="stButton"] > button:hover {
        transform: translateY(-4px) scale(1.03) !important;
        box-shadow: 0 10px 28px rgba(0,0,0,0.4) !important;
        border-color: rgba(255,255,255,0.7) !important;
    }
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button {
        height: auto !important;
        font-size: 1em !important;
        padding: 0.55em 1em !important;
        border: 1px solid rgba(255,255,255,0.35) !important;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        box-shadow: 0 3px 10px rgba(0,0,0,0.2) !important;
    }
    section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
        transform: none !important;
    }

    /* Kartu terbuka */
    .flipped-card {
        height: 130px; border-radius: 18px;
        background: linear-gradient(135deg, #fceabb 0%, #f8b500 100%);
        color: #2c2c2c;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        padding: 8px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.25);
        border: 3px solid rgba(255,255,255,0.55);
        text-align: center;
        animation: flipIn 0.3s ease;
        overflow: hidden;
    }
    .flipped-card .card-emoji   { font-size: 2.2em; line-height: 1; margin-bottom: 4px; }
    .flipped-card .card-text    { font-size: 0.8em; font-weight: 800; line-height: 1.15;
                                  word-break: break-word; }
    .flipped-card .card-subtext { font-size: 0.62em; opacity: 0.75; margin-top: 2px;
                                  word-break: break-word; }

    /* Kartu sudah cocok */
    .matched-card {
        height: 130px; border-radius: 18px;
        background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);
        color: white;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        padding: 8px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.25);
        border: 3px solid rgba(255,255,255,0.65);
        text-align: center;
        animation: matchPulse 0.5s ease;
        overflow: hidden;
    }
    .matched-card .card-emoji { font-size: 2.2em; line-height: 1; margin-bottom: 4px; }
    .matched-card .card-text  { font-size: 0.8em; font-weight: 800; line-height: 1.15;
                                word-break: break-word; }

    /* FOTO anggota di dalam kartu */
    .card-photo {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid rgba(255,255,255,0.85);
        margin-bottom: 4px;
        background: #e9e9e9;
        box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    }
    .matched-card .card-photo { border-color: #fff; }

    @keyframes flipIn {
        from { transform: rotateY(90deg); opacity: 0.3; }
        to   { transform: rotateY(0deg);  opacity: 1;   }
    }
    @keyframes matchPulse {
        0%   { transform: scale(1);    }
        50%  { transform: scale(1.08); }
        100% { transform: scale(1);    }
    }

    /* Banner menang */
    .win-banner {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        padding: 32px 24px; border-radius: 22px;
        color: white; text-align: center; margin-top: 22px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.35);
        animation: matchPulse 0.6s ease;
    }
    .win-banner h1 { margin: 0; font-size: 2.8em; text-shadow: 0 2px 10px rgba(0,0,0,0.2); }
    .win-banner p  { margin: 10px 0 0 0; font-size: 1.15em; }
    .win-stats {
        display: inline-block; background: rgba(255,255,255,0.25);
        padding: 10px 22px; border-radius: 12px; margin-top: 16px;
        font-size: 1.1em; font-weight: 600;
    }

    #MainMenu, footer { visibility: hidden; }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e1e2e 0%, #2a2a3e 100%);
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA ANGGOTA KELOMPOK
# ------------------------------------------------------------
# CARA ISI FOTO:
#   1. Upload foto ke Google Drive
#   2. Klik kanan → Share → "Anyone with the link" → Copy link
#   3. Ambil FILE_ID (bagian antara /d/ dan /view)
#   4. Tempel di field "foto":
#      "https://drive.google.com/thumbnail?id=FILE_ID&sz=w300"
#
#   Jika "foto" dikosongkan (""), kartu akan menampilkan emoji.
#   Setiap anggota WAJIB punya foto BERBEDA agar bisa dicocokkan!
# ------------------------------------------------------------
ANGGOTA = [
    {"nama": "Yosep Winarto Sinulingga", "nim": "125450125", "peran": "Pak Lurah", "bidang": "Web Dev", "emoji": "🫡",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},  # ← contoh
    {"nama": "Tiara Amelia", "nim": "125450015", "peran": "Bu Lurah", "bidang": "Desain UI/UX", "emoji": "🥰",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},
    {"nama": "Muhammad Rizky Pratama", "nim": "125450017", "peran": "Anggota", "bidang": "Data Analyst", "emoji": "😎",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},
    {"nama": "Rasya Rajid Pratama", "nim": "125450029", "peran": "Anggota", "bidang": "Mobile Dev", "emoji": "🤪",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},
    {"nama": "Elena Fariza Zahra", "nim": "125450031", "peran": "Anggota", "bidang": "Backend Dev", "emoji": "😏",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},
    {"nama": "Muhammad Irfan Nugraha", "nim": "125450065", "peran": "Anggota", "bidang": "UI Designer", "emoji": "😌",
     "foto": "https://drive.google.com/thumbnail?id=1LmYWz88aq2OL749V38x_tlFQJ4MtZ-f1"},
    {"nama": "Elisabeth Yulyanti Gultom", "nim": "125450078", "peran": "Anggota", "bidang": "DevOps", "emoji": "😨",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},
    {"nama": "Zetkin Alando Dzaqwan", "nim": "125450086", "peran": "Anggota", "bidang": "QA Engineer", "emoji": "😐",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},
    {"nama": "Jhonatan Best Kingsil Sakerebau", "nim": "125450108", "peran": "Anggota", "bidang": "Data Analyst", "emoji": "🫪",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},
    {"nama": "Jeanis Nahwadisa", "nim": "125450117", "peran": "Anggota", "bidang": "Mobile Dev", "emoji": "🤨",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},
    {"nama": "Intan Abelia Sari", "nim": "125450124", "peran": "Anggota", "bidang": "Backend Dev", "emoji": "🫢",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},
    {"nama": "Yunika Br Malau", "nim": "125450129", "peran": "Anggota", "bidang": "UI Designer", "emoji": "☺️",
     "foto": "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"},
]

# ============================================================
# FUNGSI INISIALISASI GAME (SELALU PAKAI SEMUA ANGGOTA)
# ============================================================
def init_game():
    """Membuat dek baru berisi 2 kartu per anggota — SEMUA anggota kelompok."""
    selected = ANGGOTA.copy()  # pakai semua anggota, tanpa sampling

    deck = []
    for mid, person in enumerate(selected):
        for t in ("name", "info"):
            deck.append({
                "member_id": mid,
                "type":      t,
                "nama":      person["nama"],
                "nim":       person["nim"],
                "peran":     person["peran"],
                "bidang":    person["bidang"],
                "emoji":     person["emoji"],
                "foto":      person.get("foto", ""),
            })

    random.shuffle(deck)

    st.session_state.deck        = deck
    st.session_state.matched     = set()
    st.session_state.flipped     = []
    st.session_state.moves       = 0
    st.session_state.start_time  = time.time()
    st.session_state.end_time    = None
    st.session_state.won         = False

# ============================================================
# HELPER: RENDER VISUAL KARTU (FOTO / EMOJI)
# ============================================================
def card_visual(card, state):
    """Mengembalikan HTML kartu. 'state' = 'flipped' | 'matched'."""
    cls = "flipped-card" if state == "flipped" else "matched-card"

    if card["type"] == "name":
        # ─── Kartu NAMA → tampilkan FOTO ───
        if card.get("foto"):
            visual = (
                f'<img src="{card["foto"]}" class="card-photo" alt="{card["nama"]}" '
                f'onerror="this.style.display=\'none\'; '
                f'this.nextElementSibling.style.display=\'block\';">'
                f'<div class="card-emoji" style="display:none;">{card["emoji"]}</div>'
            )
        else:
            # Jika foto kosong, fallback tampilkan emoji
            visual = f'<div class="card-emoji">{card["emoji"]}</div>'

        text    = f'<div class="card-text">{card["nama"]}</div>'
        subtext = f'<div class="card-subtext">{card["peran"]}</div>' if state == "flipped" else ""

    else:  # type == "info" → Kartu NIM
        # ─── Kartu NIM → SELALU tampilkan EMOJI ───
        visual  = f'<div class="card-emoji">{card["emoji"]}</div>'
        text    = f'<div class="card-text">{card["nim"]}</div>'
        subtext = f'<div class="card-subtext">{card["bidang"]}</div>' if state == "flipped" else ""

    return f'<div class="{cls}">{visual}{text}{subtext}</div>'

# ============================================================
# SIDEBAR — KONTROL GAME (TANPA PILIHAN KESULITAN)
# ============================================================
with st.sidebar:
    st.markdown("## 🎮 Kontrol Game")

    if st.button("🔄 Game Baru", use_container_width=True):
        init_game()
        st.rerun()

    st.divider()
    st.markdown("### 💡 Cara Bermain")
    st.markdown("""
    1. Klik kartu tertutup untuk membalik
    2. Cocokkan **dua kartu milik anggota yang sama**  
       (kartu **nama** & kartu **NIM** punya foto/emoji yang sama)
    3. Semakin sedikit langkah, semakin tinggi rating ⭐
    """)

    st.divider()
    with st.expander("📋 Daftar Anggota (Cheat Sheet)"):
        for a in ANGGOTA:
            st.markdown(
                f"{a['emoji']} **{a['nama']}**  \n"
                f"&nbsp;&nbsp;&nbsp;`{a['nim']}` · {a['peran']} · {a['bidang']}"
            )

# ============================================================
# AUTO INIT (HANYA SAAT PERTAMA LOAD)
# ============================================================
if "deck" not in st.session_state:
    init_game()

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="game-header">
    <h1>🃏 Memory Card Kelompok</h1>
    <p>Cocokkan dua kartu milik anggota yang sama — kenali tim dengan cara seru!</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# STATISTIK
# ============================================================
elapsed       = time.time() - st.session_state.start_time
matched_pairs = len(st.session_state.matched) // 2
total_pairs   = len(ANGGOTA)
best          = st.session_state.get("best_moves", "—")

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f'<div class="stat-box"><div class="val">{st.session_state.moves}</div><div class="lbl">🎯 Langkah</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="stat-box"><div class="val">{matched_pairs}/{total_pairs}</div><div class="lbl">✅ Pasangan</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="stat-box"><div class="val">{int(elapsed)}s</div><div class="lbl">⏱️ Waktu</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown(f'<div class="stat-box"><div class="val">{best}</div><div class="lbl">🏆 Rekor</div></div>', unsafe_allow_html=True)

st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

# ============================================================
# GRID KARTU
# ============================================================
deck     = st.session_state.deck
NUM_COLS = 4   # 12 pasang = 24 kartu → 6 baris

for row_start in range(0, len(deck), NUM_COLS):
    cols = st.columns(NUM_COLS, gap="small")
    for col_idx in range(NUM_COLS):
        idx = row_start + col_idx
        if idx >= len(deck):
            continue
        card = deck[idx]

        with cols[col_idx]:
            if idx in st.session_state.matched:
                st.markdown(card_visual(card, "matched"), unsafe_allow_html=True)
            elif idx in st.session_state.flipped:
                st.markdown(card_visual(card, "flipped"), unsafe_allow_html=True)
            else:
                if st.button("❓", key=f"card_{idx}", use_container_width=True):
                    st.session_state.flipped.append(idx)
                    st.rerun()

# ============================================================
# CEK PASANGAN
# ============================================================
if len(st.session_state.flipped) == 2:
    a, b = st.session_state.flipped
    is_match = deck[a]["member_id"] == deck[b]["member_id"]

    st.session_state.moves += 1

    if is_match:
        st.session_state.matched.add(a)
        st.session_state.matched.add(b)
        st.session_state.flipped = []
        st.toast(f"✅ Cocok! {deck[a]['nama']}")
        st.rerun()
    else:
        time.sleep(1.0)
        st.session_state.flipped = []
        st.rerun()

# ============================================================
# CEK MENANG
# ============================================================
if (
    "won" in st.session_state
    and not st.session_state.won
    and st.session_state.matched
    and len(st.session_state.matched) == len(deck)
):
    st.session_state.won = True
    st.session_state.end_time = time.time()
    if "best_moves" not in st.session_state or st.session_state.moves < st.session_state.best_moves:
        st.session_state.best_moves = st.session_state.moves

# ============================================================
# BANNER MENANG
# ============================================================
if st.session_state.get("won"):
    elapsed_win = st.session_state.end_time - st.session_state.start_time
    total_cards = len(deck)
    if st.session_state.moves <= total_cards:
        stars = "⭐⭐⭐"
    elif st.session_state.moves <= total_cards * 1.5:
        stars = "⭐⭐"
    else:
        stars = "⭐"

    st.markdown(f"""
    <div class="win-banner">
        <h1>🎉 SELAMAT!</h1>
        <p>Kamu berhasil mencocokkan semua kartu anggota!</p>
        <div class="win-stats">
            ⏱️ {elapsed_win:.1f} detik &nbsp;·&nbsp;
            🎯 {st.session_state.moves} langkah &nbsp;·&nbsp;
            {stars}
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()

    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if st.button("🔄 Main Lagi", key="play_again", use_container_width=True):
            init_game()
            st.rerun()