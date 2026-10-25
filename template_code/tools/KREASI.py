import streamlit as st

st.set_page_config(page_title="Bayesian Mystery", page_icon="🔎", layout="wide")

SUSPECTS = ["Andi", "Bima", "Citra"]
PRIOR = {"Andi": 0.40, "Bima": 0.35, "Citra": 0.25}
SOLUTION = "Bima"

CLUES = [
    {
        "title": "Petunjuk 1 — Catatan akses ruangan",
        "story": (
            "Catatan akses menunjukkan bahwa orang yang masuk ke ruang "
            "penyimpanan pada waktu kejadian lebih mungkin adalah Bima."
        ),
        "likelihood": {"Andi": 0.20, "Bima": 0.70, "Citra": 0.30},
    },
    {
        "title": "Petunjuk 2 — Serat kain di dekat lemari",
        "story": (
            "Serat kain yang ditemukan lebih cocok dengan jaket yang biasa "
            "dipakai Citra. Bukti ini mendukung Citra, tetapi tidak memastikan "
            "bahwa ia mengambil piala."
        ),
        "likelihood": {"Andi": 0.25, "Bima": 0.35, "Citra": 0.65},
    },
    {
        "title": "Petunjuk 3 — Kesaksian penjaga",
        "story": (
            "Penjaga mengingat seseorang dengan ciri yang lebih sesuai dengan "
            "Andi. Kesaksian bisa keliru, sehingga bukti ini perlu dinilai "
            "bersama petunjuk lainnya."
        ),
        "likelihood": {"Andi": 0.75, "Bima": 0.30, "Citra": 0.20},
    },
]

def update_bayes(prior, likelihood):
    weighted = {name: prior[name] * likelihood[name] for name in SUSPECTS}
    total = sum(weighted.values())
    if total == 0:
        return prior.copy()
    return {name: weighted[name] / total for name in SUSPECTS}

def calculate_posterior(number_of_clues):
    posterior = PRIOR.copy()
    for clue in CLUES[:number_of_clues]:
        posterior = update_bayes(posterior, clue["likelihood"])
    return posterior

def reset_game():
    st.session_state.prediction = None
    st.session_state.clues_opened = 0
    st.session_state.final_guess = None
    st.session_state.game_finished = False

if "prediction" not in st.session_state:
    reset_game()

# ==========================================
# CSS KUSTOM
# ==========================================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #eef7ff 0%, #dceeff 100%);
        color: #173b68;
    }
    .main-title {
        font-size: 2.7rem; font-weight: 800; color: #0754a6; margin-bottom: 0.1rem;
    }
    .subtitle {
        color: #416b98; font-size: 1.05rem; margin-bottom: 1.5rem;
    }
    .case-box {
        padding: 1.3rem 1.5rem; border: 1px solid #b9dcff; border-radius: 16px;
        background: linear-gradient(135deg, #ffffff, #e4f3ff);
        box-shadow: 0 4px 14px rgba(30, 110, 190, 0.08); margin-bottom: 1rem; color: #173b68;
    }
    h1, h2, h3, h4 { color: #124d8c !important; }
    p, label, .stMarkdown { color: #244c76; }
    
    .stButton > button {
        background: linear-gradient(135deg, #1688ee, #0866cc);
        color: white; border: none; border-radius: 10px;
        padding: 0.55rem 1rem; font-weight: 600; transition: 0.2s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #0874d8, #064fa8);
        box-shadow: 0 4px 12px rgba(8, 102, 204, 0.25); color: white;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #d9edff, #eff8ff);
        border-right: 1px solid #c5e2ff;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { color: #0754a6 !important; }

    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid #c6e2ff; border-radius: 12px; padding: 12px;
    }
    [data-testid="stMetricValue"] { color: #0874d8; }

    /* Custom Bar Chart */
    .chart-container {
        display: flex; justify-content: space-around; align-items: flex-end;
        height: 250px; background: rgba(255,255,255,0.6);
        border-radius: 16px; padding: 20px; margin-bottom: 20px;
        border: 1px solid #c5e2ff;
    }
    .bar-group { display: flex; flex-direction: column; align-items: center; width: 30%; }
    .bars-wrapper { display: flex; gap: 10px; align-items: flex-end; height: 180px; }
    .bar {
        width: 40px; border-radius: 6px 6px 0 0; transition: height 0.5s ease;
        position: relative; display: flex; justify-content: center;
    }
    .bar-prior { background: #8b9bb4; }
    .bar-post { background: #b69cff; }
    .bar-label {
        position: absolute; top: -24px; font-size: 0.8rem; font-weight: 700; color: #173b68;
    }
    .bar-name { margin-top: 10px; font-weight: 600; color: #124d8c; }
    
    .legend-box { display: flex; gap: 20px; justify-content: center; margin-bottom: 10px; }
    .legend-item { display: flex; align-items: center; gap: 8px; font-size: 0.9rem; font-weight: 600; color: #416b98; }
    .legend-color { width: 16px; height: 16px; border-radius: 4px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">🔎 Bayesian Mystery</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Every clue changes the odds. '
    'Gunakan bukti, perbarui probabilitas, pecahkan misterinya.</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("🕵️ Panduan Investigasi")
    st.write("1. Baca kasus dan kenali tersangka.")
    st.write("2. Kunci prediksi awal sebelum membuka petunjuk.")
    st.write("3. Buka petunjuk satu per satu.")
    st.write("4. Amati perubahan probabilitas.")
    st.write("5. Tetapkan jawaban akhir dan lihat skor.")
    st.divider()
    st.caption("Semua probabilitas adalah data simulasi untuk belajar Bayes, bukan tuduhan terhadap orang nyata.")
    if st.button("🔄 Mulai ulang permainan", use_container_width=True):
        reset_game()
        st.rerun()

st.markdown(
    """
    <div class="case-box">
        <h3>📁 Kasus: Piala yang Hilang</h3>
        <p>Piala penghargaan organisasi kampus menghilang dari lemari
        penyimpanan setelah rapat sore. Tiga anggota memiliki akses ke area
        tersebut: Andi, Bima, dan Citra.</p>
        <p>Kamu adalah detektif. Tugasmu bukan sekadar menebak, tetapi menilai
        bagaimana setiap bukti mengubah kemungkinan dari tiap hipotesis.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("🧍 Para tersangka")
details = {
    "Andi": ("🧑‍💼", "Bertugas mengurus inventaris."),
    "Bima": ("🧑‍🔧", "Membantu persiapan ruangan."),
    "Citra": ("🧑‍🎓", "Hadir dalam rapat sore."),
}
cols = st.columns(3)
for col, name in zip(cols, SUSPECTS):
    emoji, description = details[name]
    with col:
        st.markdown(f"### {emoji} {name}")
        st.write(description)
        st.metric("Probabilitas awal", f"{PRIOR[name] * 100:.0f}%")

st.divider()
st.subheader("1. Buat prediksi awal")
st.write("Sebelum melihat bukti, siapa yang menurutmu paling mungkin mengambil piala?")

if st.session_state.prediction is None:
    choice = st.radio("Pilih prediksi awal:", SUSPECTS, horizontal=True)
    if st.button("🔒 Kunci prediksi awal", type="primary"):
        st.session_state.prediction = choice
        st.rerun()
else:
    st.success(f"Prediksi awalmu sudah dikunci: **{st.session_state.prediction}**")

st.subheader("2. Kumpulkan bukti")
if st.session_state.prediction is None:
    st.info("Kunci prediksi awal terlebih dahulu untuk membuka petunjuk.")
else:
    opened = st.session_state.clues_opened
    if opened < len(CLUES):
        st.write(f"Petunjuk berikutnya: **{CLUES[opened]['title']}**")
        if st.button("🧩 Buka petunjuk", type="primary"):
            st.session_state.clues_opened += 1
            st.rerun()
    else:
        st.success("Semua petunjuk telah dibuka.")

    for i, clue in enumerate(CLUES[:st.session_state.clues_opened]):
        with st.expander(clue["title"], expanded=(i == st.session_state.clues_opened - 1)):
            st.write(clue["story"])

opened = st.session_state.clues_opened
posterior = calculate_posterior(opened)

st.subheader("3. Perubahan probabilitas")
st.write(f"Petunjuk terbuka: **{opened} dari {len(CLUES)}**. Bandingkan probabilitas sebelum dan sesudah bukti.")

# ==========================================
# CUSTOM BAR CHART (Murni HTML/CSS - Tanpa Indentasi)
# ==========================================
st.markdown(
    '<div class="legend-box">'
    '<div class="legend-item"><div class="legend-color" style="background:#8b9bb4;"></div> Sebelum Bukti (Prior)</div>'
    '<div class="legend-item"><div class="legend-color" style="background:#b69cff;"></div> Setelah Bukti (Posterior)</div>'
    '</div>', 
    unsafe_allow_html=True
)

chart_html = '<div class="chart-container">'
for name in SUSPECTS:
    prior_val = PRIOR[name] * 100
    post_val = posterior[name] * 100
    
    h_prior = (prior_val / 100) * 180
    h_post = (post_val / 100) * 180
    
    # Teks HTML dibuat sejajar (tanpa spasi/tab di awal baris)
    chart_html += f'<div class="bar-group">'
    chart_html += f'<div class="bars-wrapper">'
    chart_html += f'<div class="bar bar-prior" style="height: {h_prior}px;"><span class="bar-label">{prior_val:.0f}%</span></div>'
    chart_html += f'<div class="bar bar-post" style="height: {h_post}px;"><span class="bar-label">{post_val:.0f}%</span></div>'
    chart_html += f'</div>'
    chart_html += f'<div class="bar-name">{name}</div>'
    chart_html += f'</div>'

chart_html += '</div>'
st.markdown(chart_html, unsafe_allow_html=True)
# ==========================================

cols = st.columns(3)
for col, name in zip(cols, SUSPECTS):
    with col:
        delta_val = (posterior[name] - PRIOR[name]) * 100
        st.metric(
            f"Probabilitas {name}",
            f"{posterior[name] * 100:.1f}%",
            delta=f"{delta_val:+.1f} poin persentase",
        )

with st.expander("📘 Bagaimana Teorema Bayes bekerja?"):
    st.write(
        "Probabilitas awal dikalikan dengan kemungkinan bukti muncul jika "
        "hipotesis benar. Hasilnya lalu dinormalisasi agar total probabilitas "
        "menjadi 100%."
    )
    st.latex(r"P(H_i\mid E)=\frac{P(E\mid H_i)P(H_i)}{\sum_j P(E\mid H_j)P(H_j)}")
    
    table_html = '<table style="width:100%; text-align:left; border-collapse: collapse; margin-top: 10px;">'
    table_html += '<tr style="border-bottom: 2px solid #c5e2ff;">'
    table_html += '<th style="padding: 8px; color: #124d8c;">Tersangka</th>'
    table_html += '<th style="padding: 8px; color: #124d8c;">Probabilitas (%)</th>'
    table_html += '</tr>'
    
    for n in SUSPECTS:
        table_html += f'<tr style="border-bottom: 1px solid #e2e8f0;">'
        table_html += f'<td style="padding: 8px; color: #173b68;">{n}</td>'
        table_html += f'<td style="padding: 8px; color: #173b68; font-weight: bold;">{posterior[n] * 100:.2f}%</td>'
        table_html += f'</tr>'
        
    table_html += '</table>'
    st.markdown(table_html, unsafe_allow_html=True)


st.subheader("4. Tetapkan keputusan akhir")
if st.session_state.prediction is None:
    st.info("Kunci prediksi awal terlebih dahulu.")
elif opened < len(CLUES):
    st.info("Buka semua petunjuk sebelum menetapkan keputusan akhir.")
elif not st.session_state.game_finished:
    final_choice = st.radio("Setelah melihat semua bukti, siapa pilihan akhirmu?", SUSPECTS)
    if st.button("🧾 Selesaikan investigasi", type="primary"):
        st.session_state.final_guess = final_choice
        st.session_state.game_finished = True
        st.rerun()

if st.session_state.game_finished:
    final_guess = st.session_state.final_guess
    final_correct = final_guess == SOLUTION
    initial_correct = st.session_state.prediction == SOLUTION
    score = (60 if final_correct else 0) + (20 if initial_correct else 0) + 20

    st.divider()
    st.subheader("🏁 Hasil investigasi")
    if final_correct:
        st.success(f"Benar! Pilihan akhirmu adalah **{SOLUTION}**.")
    else:
        st.warning(f"Pilihan akhirmu adalah **{final_guess}**. Solusi cerita yang ditetapkan adalah **{SOLUTION}**.")

    c1, c2, c3 = st.columns(3)
    c1.metric("Skor", f"{score}/100")
    c2.metric("Prediksi awal", "Benar" if initial_correct else "Belum tepat")
    c3.metric("Prediksi akhir", "Benar" if final_correct else "Belum tepat")

    st.markdown("### 🧠 Pembahasan")
    st.write("Dalam cerita simulasi ini, Bima ditetapkan sebagai pelaku. Setiap petunjuk hanya mengubah tingkat keyakinan; tidak ada bukti yang memberi kepastian mutlak.")
    st.write(f"Posterior akhir model: Andi **{posterior['Andi'] * 100:.1f}%**, Bima **{posterior['Bima'] * 100:.1f}%**, Citra **{posterior['Citra'] * 100:.1f}%**.")
    
    if st.button("🔁 Main lagi", type="primary"):
        reset_game()
        st.rerun()

st.divider()
st.caption("Bayesian Mystery • Kreasi Streamlit Kelompok Bayesian • Game edukasi probabilitas")
