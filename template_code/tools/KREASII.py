import time
import warnings

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


class _State:


    def setdefault(self, k, v):
        return st.session_state.setdefault("dq_" + k, v)

    def __getattr__(self, k):
        return st.session_state["dq_" + k]

    def __setattr__(self, k, v):
        st.session_state["dq_" + k] = v


ss = _State()

# ======================================================================
# KONTEN (mata kuliah: kurikulum Prodi Sains Data ITERA, itera.ac.id)
# mk = (kode, nama, semester)
# ======================================================================
ROLES = {
    "eng": dict(
        icon="🛠", name="Data Engineer", analogi="Tim logistik & dapur persiapan", tools="Python, SQL, Airflow, Spark",
        tag="Bangun jalur data yang rapi, cepat, dan tahan banting.",
        why="Dashboard dan model secanggih apa pun percuma kalau datanya telat, kotor, atau salah. Data Engineer "
            "memastikan data **sampai**, **bersih**, dan **bisa dipercaya**. Di sini kamu merasakan kerja di balik layar itu.",
        real=["Transaksi marketplace dibersihkan lalu dimuat ke warehouse setiap malam",
              "Pipeline yang gagal = laporan pagi untuk direksi kosong atau salah",
              "Data sensor IoT divalidasi dulu sebelum dianalisis"],
        mk=[("SD2206", "Basis Data", 4), ("SD2104", "Struktur Data", 3), ("SD3205", "Pergudangan Data", 6),
            ("SD3203", "Statistik BigData", 6)],
        concept="**ETL**: Extract → Transform → Load. **Data quality**: unik, lengkap, konsisten, valid."),
    "ana": dict(
        icon="🔎", name="Data Analyst", analogi="Manajer yang membaca laporan penjualan", tools="SQL, Excel, BI, statistik",
        tag="Ubah tumpukan angka jadi jawaban dan keputusan.",
        why="Bisnis butuh jawaban, bukan tumpukan angka. Data Analyst mengubah data menjadi **keputusan**: kenapa omzet "
            "turun, produk apa yang laris, di mana masalahnya.",
        real=["Menemukan penyebab penjualan anjlok di satu kota atau produk",
              "Memantau KPI harian lewat dashboard BI",
              "Menyusun rekomendasi berbasis data untuk tim marketing & operasional"],
        mk=[("SD2105", "Analisis Data Statistika", 3), ("SD2203", "Statistika Sains Data", 4),
            ("SD3106", "Visualisasi Data dan Informasi", 5), ("SD3204", "Penggalian Data", 6),
            ("SD3206", "Inteligensi Bisnis", 6), ("SD4110", "Analisis Bisnis", 7)],
        concept="Alur: gambaran besar → **GROUP BY** → **WHERE** → temuan → rekomendasi (*data storytelling*)."),
    "sci": dict(
        icon="🧪", name="Data Scientist", analogi="Chef eksperimen", tools="Python, statistik, machine learning",
        tag="Latih model yang jujur: bagus di data baru, bukan sekadar hafalan.",
        why="Prediksi yang bagus bukan yang paling rumit, tapi yang tetap akurat pada data **baru**. Data Scientist "
            "belajar menguji model dengan jujur agar tidak tertipu hasil yang cuma kelihatan bagus.",
        real=["Prediksi permintaan produk untuk mengatur stok",
              "Deteksi transaksi mencurigakan (fraud)",
              "Estimasi harga atau risiko kredit"],
        mk=[("SD3101", "Pembelajaran Mesin", 5), ("SD3102", "Kecerdasan Buatan", 5), ("SD3103", "Komputasi Statistik", 5),
            ("SD2204", "Metode Numerik", 4), ("SD2101", "Aljabar Linier", 3), ("SD3104", "Teori Optimasi", 5)],
        concept="Model dilatih di **train**, diuji di **test**. Terlalu sederhana = *underfitting*, terlalu rumit = *overfitting*."),
}
MISSIONS = {
    "eng_clean": ("eng", "Data Cleaning", "🧹 Data Cleaner"),
    "eng_pipe": ("eng", "ETL Pipeline", "🔧 Pipeline Master"),
    "analyst": ("ana", "Analisis Eksploratif & Storytelling", "🕵️ Detektif Data"),
    "sci": ("sci", "Evaluasi Model (Train vs Test)", "🔮 Model Whisperer"),
}
REMEDIAL = {
    "eng_clean": "Perbaiki dulu yang bisa diperbaiki: rapikan teks (strip/title), hapus duplikat, isi null dengan median. "
                 "Hapus baris hanya bila memang tidak valid (harga ≤ 0). Jangan `dropna` sembarangan: itu membuang data bagus.",
    "eng_pipe": "Alur ETL: Ingest (ambil) → Validate (cek) → Transform (olah) → Load (simpan ke warehouse) → Serve (dipakai "
                "dashboard/model). Data harus lolos validasi sebelum diolah, dan harus tersimpan sebelum dilayani.",
    "analyst": "Mulai dari gambaran besar, pecah per dimensi (GROUP BY), lalu lihat perubahan % Q4 vs Q3. Cari satu kota dan "
               "satu kategori yang anjlok jauh melebihi yang lain, lalu persempit dengan WHERE.",
    "sci": "Error train kecil tapi test besar = overfitting (terlalu rumit). Keduanya besar = underfitting (terlalu "
           "sederhana). Cari derajat di tengah yang membuat error test paling kecil.",
}

CSS = """<style>
:root{--dq:#800020;--dq-dark:#5b0f1b;--dq-light:#a4243b;--dq-rgb:128,0,32}
.dq-hero{padding:1.3rem 1.6rem;border-radius:18px;color:#fff;margin:.3rem 0 1rem;box-shadow:0 12px 30px -14px rgba(var(--dq-rgb),.85);
 background:linear-gradient(120deg,var(--dq-dark),var(--dq) 55%,var(--dq-light))}
.dq-h1{font-size:2rem;font-weight:800;line-height:1.15}.dq-hero p{margin:.35rem 0 0;opacity:.93}
.dq-chip{display:inline-block;padding:.18rem .7rem;margin:.15rem .3rem .15rem 0;border-radius:999px;font-size:.78rem;
 font-weight:600;background:rgba(var(--dq-rgb),.12);border:1px solid rgba(var(--dq-rgb),.5)}
.dq-pipe{display:flex;gap:.45rem;flex-wrap:wrap;align-items:center;margin:.5rem 0 1rem}
.dq-step{padding:.4rem .9rem;border-radius:10px;font-weight:700;background:rgba(var(--dq-rgb),.14);border:1px solid rgba(var(--dq-rgb),.55)}
.dq-step.empty{opacity:.45;border-style:dashed}
.dq-hearts{font-size:1.5rem;letter-spacing:.15rem}
.dq-win{padding:1rem 1.3rem;border-radius:16px;border:1px solid rgba(var(--dq-rgb),.6);margin:.6rem 0;animation:dqpop .45s ease;
 background:linear-gradient(120deg,rgba(var(--dq-rgb),.22),rgba(164,36,59,.1))}
@keyframes dqpop{from{transform:scale(.92);opacity:0}to{transform:scale(1);opacity:1}}
div.stButton>button{border-radius:12px;font-weight:600;transition:transform .12s,box-shadow .12s}
div.stButton>button:hover{transform:translateY(-2px);box-shadow:0 6px 16px -8px rgba(var(--dq-rgb),.9)}
button[kind="primary"],button[data-testid="stBaseButton-primary"]{background:linear-gradient(120deg,var(--dq-dark),var(--dq));border:0;color:#fff}
div[data-testid="stMetric"]{background:rgba(128,128,128,.08);border:1px solid rgba(128,128,128,.22);padding:.7rem .9rem;border-radius:14px}
button[data-baseweb="tab"]{font-weight:600}
div[data-baseweb="tab-highlight"]{background-color:var(--dq)!important}
</style>"""


# ======================================================================
# KOMPONEN BERSAMA
# ======================================================================
def chips(items):
    return "".join(f'<span class="dq-chip">{x}</span>' for x in items)


def hero(title, sub):
    st.markdown(f'<div class="dq-hero"><div class="dq-h1">{title}</div><p>{sub}</p></div>', unsafe_allow_html=True)


def conveyor(names, states):
    body = "<span>➜</span>".join(f'<span class="dq-step {s}">{n}</span>' for n, s in zip(names, states))
    return f'<div class="dq-pipe">{body}</div>'


def game_shell(r, *labels):
    """Hero + tab Briefing (kenapa & manfaat & mata kuliah). Mengembalikan tab untuk tiap misi."""
    R = ROLES[r]
    hero(f"{R['icon']} {R['name']}", R["tag"])
    tabs = st.tabs(["📖 Briefing", *labels])
    with tabs[0]:
        a, b = st.columns(2)
        with a.container(border=True):
            st.markdown(f"#### 🎯 Kenapa main misi ini?\n{R['why']}")
        with b.container(border=True):
            st.markdown("#### 🌍 Gunanya di dunia nyata\n" + "\n".join(f"- {x}" for x in R["real"]))
        with st.container(border=True):
            st.markdown("#### 🎓 Nyambung ke mata kuliah Sains Data ITERA")
            st.markdown(chips(f"{c} · {n} · Smt {s}" + (" (pilihan)" if s >= 6 else "") for c, n, s in R["mk"]),
                        unsafe_allow_html=True)
            st.markdown(f"**Konsep inti:** {R['concept']}")
        st.caption("👉 Sudah paham? Buka tab misi di sebelah kanan. Kamu punya 3 nyawa per misi!")
    return tabs[1:]


# ---------------- nyawa, game over, XP ----------------
def lose(k):
    if k in ss.done:
        return
    ss.lives[k] = ss.lives.setdefault(k, 3) - 1
    if ss.lives[k] <= 0:
        ss.xp = max(0, ss.xp - 10)


def miss(k, msg):
    """Jawaban salah: kurangi nyawa lalu rerun supaya hati terbarui; pesan tampil di gate()."""
    lose(k)
    ss.flash = (k, msg)
    st.rerun()


def reset(k):
    ss.lives[k], ss.flash = 3, None
    if k == "analyst":
        ss.a_seed, ss.a_pts, ss.a_last = ss.a_seed + 1, 5, None
    elif k == "sci":
        ss.s_seed += 1


def gate(k):
    """Tampilkan nyawa & feedback. Return False bila Game Over."""
    n = ss.lives.setdefault(k, 3)
    c1, c2 = st.columns([1, 3])
    c1.markdown(f'<div class="dq-hearts">{"❤️" * n}{"🖤" * (3 - n)}</div>', unsafe_allow_html=True)
    c2.caption("✅ Misi selesai: mode latihan tanpa penalti." if k in ss.done else
               "Salah = -1 nyawa · nyawa habis = **Game Over** (-10 XP) dan misi diulang dengan skenario baru.")
    if ss.flash and ss.flash[0] == k:
        st.error("❌ " + ss.flash[1])
        ss.flash = None
    if n > 0:
        return True
    st.error("💀 **Game Over!** Nyawa habis dan kamu kehilangan 10 XP. Baca remedial, lalu coba lagi.")
    st.info("📖 **Remedial:** " + REMEDIAL[k])
    st.button("🔁 Mengulang misi", key=f"dq_re_{k}", type="primary", on_click=reset, args=(k,))
    return False


def award(k, base, extra=0):
    if k in ss.done:
        return
    bonus = 15 * ss.lives.setdefault(k, 3) + extra
    ss.done.append(k)
    ss.xp += base + bonus
    st.balloons()
    _, skill, badge = MISSIONS[k]
    st.markdown(f'<div class="dq-win">🏆 <b>Misi selesai: {badge}</b><br>+{base} XP dasar · +{bonus} XP bonus '
                f'(sisa nyawa{" & poin query" if extra else ""})<br>🔓 Skill terbuka: <b>{skill}</b></div>',
                unsafe_allow_html=True)


# ======================================================================
# BERANDA
# ======================================================================
def go(page):
    st.session_state["dq_page"] = page


def home():
    hero("🧭 Data Journey", "Pelajari Data Engineer, Data Analyst & Data Scientist lewat 4 misi interaktif, "
                          "lengkap dengan nyawa, XP, dan badge.")
    st.markdown("Bayangkan sebuah **restoran besar**. Data adalah bahan makanannya, dan tiga peran ini menjaga dapurnya tetap jalan:")
    for col, (r, R) in zip(st.columns(3), ROLES.items()):
        name = f"{R['icon']} {R['name']}"
        with col.container(border=True):
            st.markdown(f"### {name}\n*{R['analogi']}*\n\n{R['tag']}\n\n**Tools:** {R['tools']}")
            st.caption("  ·  ".join(("✅ " if k in ss.done else "🔒 ") + m[2] for k, m in MISSIONS.items() if m[0] == r))
            st.button("Mulai misi ➜", key=f"dq_go_{r}", type="primary", use_container_width=True, on_click=go, args=(name,))
    with st.container(border=True):
        st.markdown("#### 🎮 Aturan main\n"
                    "- ❤️ **3 nyawa** per misi. Jawaban salah **-1 nyawa**.\n"
                    "- 💀 Nyawa habis = **Game Over**: **-10 XP**, skenario diacak ulang, dan kamu wajib baca remedial.\n"
                    "- ⚡ Makin banyak nyawa tersisa saat menang, makin besar **bonus XP**. Kumpulkan 4 badge!\n"
                    "- Alur data di dunia nyata: 🛠 Engineer → 🔎 Analyst → 🧪 Scientist. Disarankan main berurutan.")
    with st.expander("🎓 Peta mata kuliah Sains Data ITERA ↔ peran data"):
        rows = [(R["name"], c, n, s) for R in ROLES.values() for c, n, s in R["mk"]]
        st.dataframe(pd.DataFrame(rows, columns=["Peran", "Kode", "Mata kuliah", "Semester"]),
                     hide_index=True, use_container_width=True)
        st.caption("Sumber: halaman kurikulum Prodi Sains Data di itera.ac.id (semester 6-7 berupa mata kuliah pilihan). "
                   "Kurikulum bisa berubah, cek sd.itera.ac.id untuk versi terbaru.")


# ======================================================================
# GAME 1: DATA ENGINEER
# ======================================================================
RAW = pd.DataFrame({
    "order_id": [1, 2, 2, 3, 4, 5, 6, 7],
    "kota": ["Jakarta", "jakarta ", "jakarta ", "BANDUNG", "Bandung", "Surabaya", "surabaya ", " MEDAN"],
    "umur": [25, 31, 31, None, 42, None, 29, 35],
    "harga": [150, 200, 200, 120, -80, 90, 300, 110],
})
STEPS = {
    "text": "Rapikan teks kota (strip + title case)",
    "dup": "Hapus baris duplikat",
    "fill": "Isi umur kosong dengan median",
    "neg": "Buang baris dengan harga ≤ 0",
    "dropna": "Hapus SEMUA baris yang mengandung nilai kosong",
}
STAGES = ["Ingest", "Validate", "Transform", "Load", "Serve"]
STAGE_INFO = {
    "Ingest": ("Data mentah diambil dari API, database, dan file log.", "Pipeline harus dimulai dengan mengambil data mentah dari sumbernya."),
    "Validate": ("Skema & kualitas dicek, data rusak ditandai.", "Data mentah dicek dulu sebelum diolah, agar sampah tidak ikut mengalir."),
    "Transform": ("Data dibersihkan, digabung, dan dibentuk ulang.", "Data yang sudah valid diolah dulu sebelum disimpan."),
    "Load": ("Hasil disimpan ke data warehouse.", "Hanya data yang sudah rapi yang layak masuk warehouse."),
    "Serve": ("Dashboard & model membaca data siap pakai.", "Dashboard baru bisa membaca data setelah tersimpan di warehouse."),
}


def clean(df, steps):
    d = df.copy()
    if "text" in steps:
        d["kota"] = d.kota.str.strip().str.title()
    if "dup" in steps:
        d = d.drop_duplicates()
    if "dropna" in steps:
        d = d.dropna()
    if "fill" in steps:
        d["umur"] = d.umur.fillna(d.umur.median())
    if "neg" in steps:
        d = d[d.harga > 0]
    return d


def mission_clean():
    if not gate("eng_clean"):
        return
    st.write("Data order di bawah kotor. Pilih langkah pembersihan lalu **kirim**. Awas, ada **jebakan** yang membuang data bagus!")
    picked = [k for k, v in STEPS.items() if st.checkbox(v, key=f"dq_st_{k}")]
    out = clean(RAW, picked)
    a, b = st.columns(2)
    a.caption("Sebelum")
    a.dataframe(RAW, hide_index=True)
    b.caption("Sesudah (pratinjau)")
    b.dataframe(out, hide_index=True)
    if st.button("📤 Kirim hasil cleaning", type="primary", key="dq_send"):
        checks = {"unik (tanpa duplikat)": out.order_id.is_unique, "lengkap (tanpa null)": bool(out.umur.notna().all()),
                  "konsisten (nama kota seragam)": out.kota.nunique() == 4, "valid (harga > 0)": bool((out.harga > 0).all())}
        lost = max(0, 6 - len(out))
        score = max(0, 25 * sum(checks.values()) - 15 * lost)
        if score == 100:
            award("eng_clean", 50)
        else:
            bad = ", ".join(k for k, ok in checks.items() if not ok) or "-"
            miss("eng_clean", f"Data Quality Score {score}/100. Belum terpenuhi: {bad}."
                              + (f" Kamu membuang {lost} baris yang sebenarnya bisa diselamatkan." if lost else ""))


def mission_pipe():
    if not gate("eng_pipe"):
        return
    st.write("Susun 5 tahap pipeline lalu jalankan. Urutan salah → pipeline **gagal**.")
    opts = ["—", "Load", "Serve", "Ingest", "Transform", "Validate"]
    pick = [c.selectbox(f"Langkah {i + 1}", opts, key=f"dq_slot{i}") for i, c in enumerate(st.columns(5))]
    st.markdown(conveyor(pick, ["empty" if p == "—" else "" for p in pick]), unsafe_allow_html=True)
    if st.button("🚀 Jalankan pipeline", type="primary", key="dq_run"):
        if "—" in pick or len(set(pick)) < 5:
            st.warning("Isi kelima langkah dengan tahap yang berbeda.")
            return
        bad = next((i for i, (p, t) in enumerate(zip(pick, STAGES)) if p != t), None)
        with st.status("Menjalankan pipeline...", expanded=True) as s:
            for p in pick[: 5 if bad is None else bad]:
                time.sleep(0.4)
                st.write(f"✅ **{p}** · {STAGE_INFO[p][0]}")
            if bad is not None:
                st.write(f"❌ **{pick[bad]}** gagal di langkah {bad + 1}")
                time.sleep(0.8)
            s.update(label="Pipeline sukses!" if bad is None else "Pipeline gagal", state="complete" if bad is None else "error")
        if bad is None:
            award("eng_pipe", 50)
        else:
            miss("eng_pipe", f"Langkah {bad + 1} gagal: **{pick[bad]}** salah tempat. Di posisi ini seharusnya "
                             f"**{STAGES[bad]}**. {STAGE_INFO[STAGES[bad]][1]}")


def game_engineer():
    t1, t2 = game_shell("eng", "🧹 Misi 1 · Bersihkan data", "🔧 Misi 2 · Susun pipeline")
    with t1:
        mission_clean()
    with t2:
        mission_pipe()


# ======================================================================
# GAME 2: DATA ANALYST
# ======================================================================
CITIES = ["Jakarta", "Bandung", "Surabaya", "Medan"]
CATS = ["Elektronik", "Fashion", "Makanan", "Buku"]
CITYW = dict(zip(CITIES, [120, 80, 90, 60]))
CATW = dict(zip(CATS, [0.5, 2, 10, 5]))       
PRICE = dict(zip(CATS, [2.0, 0.5, 0.1, 0.2]))


@st.cache_data
def make_sales(seed):
    rng = np.random.default_rng(seed)
    culprit = (CITIES[rng.integers(4)], CATS[rng.integers(4)])
    rows = []
    for m in range(1, 13):
        for c in CITIES:
            for k in CATS:
                n = CITYW[c] * CATW[k] * rng.normal(1, 0.05)
                if (c, k) == culprit and m >= 10:
                    n *= 0.1
                rows.append((m, c, k, int(n), round(n * PRICE[k], 1)))
    return pd.DataFrame(rows, columns=["bulan", "kota", "kategori", "order", "revenue"]), culprit


def run_query(df, dim, met, fk, fc):
    sub = df[df.kota.isin(fk) & df.kategori.isin(fc)]
    if dim == "bulan":
        return dim, sub.groupby("bulan")[met].sum().to_frame()
    sub = sub[sub.bulan >= 7].assign(periode=lambda t: np.where(t.bulan >= 10, "Q4", "Q3"))
    p = sub.pivot_table(index=dim, columns="periode", values=met, aggfunc="sum")
    p["perubahan_%"] = (p.Q4 / p.Q3 - 1) * 100
    return dim, p


def mission_case():
    if not gate("analyst"):
        return
    df, culprit = make_sales(ss.a_seed)
    q3, q4 = df[df.bulan.between(7, 9)].revenue.sum(), df[df.bulan >= 10].revenue.sum()
    st.markdown("**Briefing kasus:** omzet *NusaMart* turun di kuartal 4 padahal harga tidak berubah. Kamu punya "
                "**5 poin query** untuk menemukan **kota** dan **kategori** penyebabnya.")
    m = st.columns(3)
    m[0].metric("Revenue Q3 (juta Rp)", f"{q3:,.0f}")
    m[1].metric("Revenue Q4 (juta Rp)", f"{q4:,.0f}", f"{(q4 / q3 - 1) * 100:.1f}%")
    m[2].metric("Poin query", ss.a_pts)
    st.line_chart(df.groupby("bulan").revenue.sum())

    with st.container(border=True):
        st.markdown("#### 🧰 Query Builder")
        c = st.columns(4)
        dim = c[0].selectbox("GROUP BY", ["kota", "kategori", "bulan"])
        met = c[1].selectbox("Metrik (SUM)", ["revenue", "order"])
        fk = c[2].multiselect("WHERE kota", CITIES, default=CITIES) or CITIES
        fc = c[3].multiselect("WHERE kategori", CATS, default=CATS) or CATS
        q = lambda xs: ", ".join(f"'{x}'" for x in xs)
        st.code(f"SELECT {dim}, SUM({met})\nFROM penjualan\nWHERE kota IN ({q(fk)})\n  AND kategori IN ({q(fc)})\n"
                f"GROUP BY {dim};", "sql")
        if st.button("▶️ Jalankan query (-1 poin)", disabled=ss.a_pts <= 0):
            ss.a_pts -= 1
            ss.a_last = run_query(df, dim, met, fk, fc)
            st.rerun()
        if ss.a_last is not None:
            d_, res = ss.a_last
            if d_ == "bulan":
                st.line_chart(res)
            else:
                st.bar_chart(res["perubahan_%"])
                st.dataframe(res.round(1))
                st.caption("Perubahan % = Q4 dibanding Q3. Cari batang yang paling anjlok.")

    st.markdown("#### ⚖️ Kesimpulan")
    x, y, z = st.columns([2, 2, 1])
    ak = x.selectbox("Kota biang masalah", CITIES, key="dq_ak")
    ac = y.selectbox("Kategori biang masalah", CATS, key="dq_ac")
    if z.button("🔍 Ajukan temuan", type="primary", use_container_width=True):
        if (ak, ac) == culprit:
            st.markdown(f"**Insight:** penjualan **{culprit[1]}** di **{culprit[0]}** anjlok ±90% sejak Oktober, indikasi "
                        "stok habis atau produk hilang dari katalog. **Rekomendasi:** cek stok & listing segera.")
            award("analyst", 100, 10 * ss.a_pts)
        else:
            hint = "Salah satu tebakanmu sudah tepat." if ak == culprit[0] or ac == culprit[1] else "Kedua tebakanmu belum tepat."
            miss("analyst", f"Bukti belum cukup. {hint} Jelajahi data lagi sebelum menuduh.")
    if "analyst" in ss.done and st.button("🎲 Kasus baru (latihan)"):
        reset("analyst")
        st.rerun()


def game_analyst():
    (t1,) = game_shell("ana", "🕵️ Misi · Kasus omzet anjlok")
    with t1:
        mission_case()


# ======================================================================
# GAME 3: DATA SCIENTIST
# ======================================================================
def mission_model():
    if not gate("sci"):
        return
    rng = np.random.default_rng(ss.s_seed)
    x = rng.uniform(0, 10, 40)
    y = 3 * np.sin(x) + 0.3 * x + rng.normal(0, 0.6, 40)
    idx = rng.permutation(40)
    tr, te = idx[:20], idx[20:]
    xs = x / 5 - 1

    def fit(d):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            p = np.poly1d(np.polyfit(xs[tr], y[tr], d))
        r = lambda i: float(np.sqrt(np.mean((p(xs[i]) - y[i]) ** 2)))
        return p, r(tr), r(te)

    fits = {d: fit(d) for d in range(1, 13)}
    goal = min(f[2] for f in fits.values()) * 1.15
    st.markdown("**Misi:** prediksi pola penjualan musiman dari 40 titik data (20 train, 20 test). "
                f"Capai **error test ≤ {goal:.2f}** dengan mengatur kompleksitas model.")
    deg = st.slider("Kompleksitas model (derajat polinomial; 1 = garis lurus)", 1, 12, 1)
    p, e_tr, e_te = fits[deg]

    pts = pd.DataFrame({"x": x, "y": y, "set": np.where(np.isin(np.arange(40), tr), "Train", "Test")})
    gx = np.linspace(0, 10, 200)
    sc = alt.Scale(domain=[-6, 9])
    st.altair_chart(alt.layer(
        alt.Chart(pd.DataFrame({"x": gx, "y": p(gx / 5 - 1)})).mark_line(color="#888", clip=True)
        .encode(x="x:Q", y=alt.Y("y:Q", scale=sc)),
        alt.Chart(pts).mark_circle(size=80, opacity=0.85).encode(x="x:Q", y=alt.Y("y:Q", scale=sc), color="set:N"),
    ).properties(height=330), use_container_width=True)

    m = st.columns(3)
    m[0].metric("Error Train", f"{e_tr:.2f}")
    m[1].metric("Error Test", f"{e_te:.2f}")
    m[2].metric("Target Test ≤", f"{goal:.2f}")
    st.progress(min(1.0, goal / e_te), text="Menuju target (penuh = tercapai)")
    if e_tr > 1.2:
        st.warning("📉 **Underfitting**: model terlalu sederhana, pola belum tertangkap (error train pun tinggi).")
    elif e_te <= goal:
        st.success("🎯 **Sweet spot**: model menangkap pola tanpa menghafal noise.")
    else:
        st.error("📈 **Overfitting**: error train kecil tapi test besar. Model menghafal noise, bukan pola.")

    if st.button("✅ Kirim model ini", type="primary"):
        if e_te <= goal:
            st.markdown("**Pelajaran:** model terbaik bukan yang paling rumit, tapi yang paling baik di data *baru*.")
            award("sci", 100)
        else:
            miss("sci", f"Error test {e_te:.2f} masih di atas target {goal:.2f}. "
                        + ("Model terlalu sederhana." if e_tr > 1.2 else "Model terlalu rumit, mulai menghafal noise."))
    if "sci" in ss.done:
        with st.expander("📈 Pembahasan: kurva error train vs test"):
            st.line_chart(pd.DataFrame({"Train": [f[1] for f in fits.values()], "Test": [f[2] for f in fits.values()]},
                                       index=list(fits)))
            st.caption("Error train terus turun, tapi error test membentuk huruf U. Itulah bias-variance tradeoff.")
        if st.button("🎲 Dataset baru (latihan)"):
            reset("sci")
            st.rerun()


def game_scientist():
    (t1,) = game_shell("sci", "🧪 Misi · Latih si peramal")
    with t1:
        mission_model()

PAGES = {"🏠 Beranda": home, **{f"{R['icon']} {R['name']}": fn for R, fn in
                               zip(ROLES.values(), (game_engineer, game_analyst, game_scientist))}}


def render():
    for k, v in dict(xp=0, done=[], lives={}, flash=None, a_seed=1, a_pts=5, a_last=None, s_seed=3).items():
        ss.setdefault(k, v)
    st.session_state.setdefault("dq_page", "🏠 Beranda")
    st.markdown(CSS, unsafe_allow_html=True)
    status = st.empty()
    if hasattr(st, "segmented_control"):
        page = st.segmented_control("Menu", list(PAGES), key="dq_page", label_visibility="collapsed")
    else:
        page = st.radio("Menu", list(PAGES), horizontal=True, key="dq_page", label_visibility="collapsed")
    PAGES[page or "🏠 Beranda"]()
    with status.container():
        st.progress((ss.xp % 100) / 100, text=f"⚡ Level {ss.xp // 100 + 1} · {ss.xp} XP")
        st.caption("  ·  ".join(("✅ " if k in ss.done else "🔒 ") + m[2] for k, m in MISSIONS.items()))


if __name__ == "__main__":
    render()
