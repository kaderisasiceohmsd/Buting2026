"""Halaman Streamlit Frog Jump. Logika ada di engine.py, visual di scene.py."""
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from . import engine
from .scene import build_html

try:  # Streamlit baru memakai width="stretch"; versi lama masih use_container_width
    from packaging.version import Version
    LEBAR = {"width": "stretch"} if Version(st.__version__) >= Version("1.50") else {"use_container_width": True}
except Exception:
    LEBAR = {"use_container_width": True}

N_STEPS = 1500
NAMA = [f"Daun {i}" for i in range(1, 6)]
DEFAULTS = dict(fj_left=30, fj_right=40, fj_start=3, fj_fly=5, fj_trap=1,
                fj_absorb=False, fj_seed=7)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700&family=Figtree:wght@400;500;700&display=swap');
.stApp, .stApp p, .stApp label, .stApp li, .stApp button { font-family: 'Figtree', sans-serif; }
.stApp h1, .stApp h2, .stApp h3 { font-family: 'Bricolage Grotesque', sans-serif; letter-spacing: -0.01em; }
.stButton > button { border-radius: 14px; font-weight: 700; }
.kartu { background: #DCEBDD; border-radius: 18px; padding: 16px 20px; height: 100%; }
.kartu b { font-weight: 700; }
.ok { color: #2F7A52; font-weight: 700; }
.no { color: #B8483A; font-weight: 700; }
</style>
"""


def _init():
    for k, v in DEFAULTS.items():
        st.session_state.setdefault(k, v)


def _kiri_berubah():
    s = st.session_state
    if s.fj_left + s.fj_right > 100:
        s.fj_right = 100 - s.fj_left


def _kanan_berubah():
    s = st.session_state
    if s.fj_left + s.fj_right > 100:
        s.fj_left = 100 - s.fj_right


def _acak():
    st.session_state.fj_seed += 1


def _persen(x: float) -> str:
    t = f"{x * 100:.1f}"
    if t.endswith(".0"):
        t = t[:-2]
    return t.replace(".", ",") + "%"


def _tabel_matriks(P: np.ndarray) -> pd.DataFrame:
    return pd.DataFrame(
        [[_persen(v) for v in row] for row in P],
        index=[f"Sekarang: {n}" for n in NAMA],
        columns=[f"Besok: {n}" for n in NAMA],
    )


def render():
    _init()
    st.markdown(CSS, unsafe_allow_html=True)
    s = st.session_state

    st.title("Frog Jump")
    st.caption("A Markov Chain Adventure")
    st.write(
        "Seekor kodok melompat di antara lima daun teratai. Atur peluang ia melompat "
        "ke kiri, ke kanan, atau diam, lalu tonton bagaimana pola acak itu membentuk "
        "sebuah Markov chain."
    )

    # ------------------------------------------------ pengaturan
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        c1.slider("Peluang lompat ke kiri", 0, 100, key="fj_left",
                  format="%d%%", on_change=_kiri_berubah)
        c2.slider("Peluang lompat ke kanan", 0, 100, key="fj_right",
                  format="%d%%", on_change=_kanan_berubah)
        p_diam = 100 - s.fj_left - s.fj_right
        c3.metric("Peluang diam (otomatis)", f"{p_diam}%")
        c3.markdown('<span class="ok">Kiri + kanan + diam = 100%</span>', unsafe_allow_html=True)

        d1, d2, d3, d4 = st.columns([1, 1, 1, 1.4])
        d1.selectbox("Daun awal kodok", range(1, 6), key="fj_start")
        d2.selectbox("Daun lalat 🪰", range(1, 6), key="fj_fly")
        d3.selectbox("Daun jebakan ⚠️", range(1, 6), key="fj_trap")
        d4.toggle("Jebakan menangkap kodok selamanya", key="fj_absorb",
                  help="Mengubah daun jebakan menjadi absorbing state: sekali masuk, tidak bisa keluar.")
        st.button("Acak lintasan baru", on_click=_acak, help="Mengganti seed, jadi lintasan acak berbeda.")

    start, fly, trap = s.fj_start - 1, s.fj_fly - 1, s.fj_trap - 1
    if fly == trap:
        fly = (trap + 1) % 5
        st.warning(f"Lalat dan jebakan tidak boleh di daun yang sama, lalat dipindah ke Daun {fly + 1}.")

    # ------------------------------------------------ simulasi (engine)
    P = engine.build_matrix(s.fj_left / 100, s.fj_right / 100, trap=trap, absorbing=s.fj_absorb)
    info = engine.analyze(P, start)
    traj = engine.simulate(P, start, N_STEPS, s.fj_seed)

    html = build_html({
        "P": P.tolist(), "start": start, "traj": traj, "fly": fly, "trap": trap,
        "absorbing": bool(s.fj_absorb), "theory": info["stationary"], "note": info["note"],
    })
    if hasattr(st, "iframe"):
        try:
            st.iframe(html, height=1400, width="stretch")
        except TypeError:
            components.html(html, height=1400, width=1600, scrolling=True)
    else:
        components.html(html, height=1400, width=1600, scrolling=True)

    st.caption(
        "Lintasan 1.500 langkah dibuat oleh mesin simulasi Python (engine.py) dari matriks di atas. "
        "Animasi menayangkannya langkah demi langkah dan statistik dihitung ulang setiap kodok mendarat."
    )

    # ------------------------------------------------ edukasi
    st.header("Apa yang sebenarnya terjadi di kolam ini?")
    t1, t2, t3 = st.tabs(["Peta konsep", "Empat konsep kunci", "Matematika di balik layar"])

    row = P[start]
    kiri = P[start, start - 1] if start > 0 else 0.0
    kanan = P[start, start + 1] if start < 4 else 0.0
    diam = P[start, start]
    n = start + 1

    with t1:
        st.markdown(
            "Kodok ini adalah **proses stokastik**: sesuatu yang berubah secara acak seiring "
            "waktu. Yang berubah adalah posisinya. Karena aturan lompatannya hanya melihat "
            "posisi sekarang, prosesnya disebut **Markov chain**."
        )
        st.markdown(
            "| Di game | Di Markov chain |\n|---|---|\n"
            "| Kodok | Proses stokastik yang kita amati |\n"
            "| 5 daun teratai | 5 **state** (keadaan yang mungkin) |\n"
            "| Satu lompatan | Satu **transisi** (berpindah ke langkah waktu berikutnya) |\n"
            "| Peluang kiri, kanan, diam | Satu baris **matriks transisi** |\n"
            "| Riwayat lompatan | **Lintasan** (path) dari proses |"
        )
        st.markdown(
            "**Satu langkah, empat gerakan:** (1) lihat daun tempat kodok berdiri, "
            "(2) ambil baris matriks untuk daun itu, (3) \"putar dadu\" sesuai peluangnya, "
            "(4) pindah ke daun hasilnya. Lalu ulangi."
        )
    with t2:
        a, b = st.columns(2)
        with a:
            st.markdown(
                f'<div class="kartu"><b>1. Current state</b><br>Daun tempat kodok berdiri '
                f'sekarang. Misalnya kodok di <b>Daun {n}</b>: itulah state saat ini, dan '
                f'hanya itu yang perlu diketahui untuk menebak lompatan berikutnya.</div>',
                unsafe_allow_html=True)
        with b:
            st.markdown(
                f'<div class="kartu"><b>2. Transition probability</b><br>Peluang pindah dari '
                f'satu daun ke daun lain dalam sekali lompat. Dari Daun {n}: ke kiri '
                f'<b>{_persen(kiri)}</b>, ke kanan <b>{_persen(kanan)}</b>, diam '
                f'<b>{_persen(diam)}</b>.</div>', unsafe_allow_html=True)
        st.write("")
        a, b = st.columns(2)
        with a:
            st.markdown(
                '<div class="kartu"><b>3. Transition matrix</b><br>Tabel semua peluang '
                'transisi. Baris = daun sekarang, kolom = daun berikutnya, dan tiap baris '
                'berjumlah 100%. Di Daun 1 kiri mustahil, dan di Daun 5 kanan mustahil, '
                'jadi peluang itu digabung ke "diam".</div>', unsafe_allow_html=True)
        with b:
            st.markdown(
                f'<div class="kartu"><b>4. Markov property</b><br>Lompatan berikutnya hanya '
                f'bergantung pada daun sekarang, bukan riwayatnya. Kodok di Daun {n} punya '
                f'peluang kanan {_persen(kanan)} entah ia tadi datang dari kiri, dari kanan, '
                f'atau sudah lama diam di situ. Sifat ini disebut <i>memoryless</i>.</div>',
                unsafe_allow_html=True)
        st.write("")
        st.latex(r"P(S_{t+1}=j \mid S_t=i,\,S_{t-1},\,\dots,\,S_0)\;=\;P(S_{t+1}=j \mid S_t=i)")

    with t3:
        st.markdown("**Matriks transisi saat ini**")
        st.dataframe(_tabel_matriks(P), **LEBAR)
        valid = bool(np.allclose(P.sum(axis=1), 1.0))
        st.markdown(
            f"Validasi: setiap baris berjumlah 100% "
            f"<span class='{'ok' if valid else 'no'}'>{'terpenuhi' if valid else 'gagal'}</span>.",
            unsafe_allow_html=True)

        st.markdown("**Distribusi setelah banyak langkah**")
        st.latex(r"\pi_{t+1}=\pi_t P \qquad\text{dan distribusi stasioner:}\qquad \pi = \pi P,\;\; \sum_i \pi_i = 1")
        cek = lambda ok: "✓" if ok else "✗"
        st.markdown(
            f"- Irreducible (tiap daun bisa dicapai dari daun mana pun): **{cek(info['irreducible'])}**\n"
            f"- Aperiodic (ada peluang diam): **{cek(info['aperiodic'])}**\n"
            f"- Ergodik, syarat membandingkan simulasi dengan teori: **{cek(info['ergodic'])}**"
        )
        if info["ergodic"]:
            dfp = pd.DataFrame({"Daun": NAMA, "Peluang jangka panjang (π)": [_persen(x) for x in info["stationary"]]})
            st.dataframe(dfp, hide_index=True, **LEBAR)
            st.markdown(
                "Pada rantai ergodik, proporsi waktu kodok di tiap daun akan mendekati π "
                "seberapa pun daun awalnya. Itu yang kamu lihat pada panel frekuensi kunjungan "
                "ketika langkah makin banyak (coba tombol +100 langkah instan)."
            )
        else:
            st.info(info["note"])
        if info["absorbing"]:
            nama = ", ".join(f"Daun {a + 1}" for a in info["absorbing"])
            st.markdown(f"**Absorbing state:** {nama}. Sekali masuk, kodok tidak pernah keluar.")
            if info["absorb_probs"]:
                rinci = "; ".join(f"{NAMA[a]}: {_persen(p)}" for a, p in zip(info["absorbing"], info["absorb_probs"]))
                st.markdown(f"Peluang akhirnya terserap (dari Daun {n}): {rinci}.")
            if info["expected_steps"] is not None:
                st.markdown(f"Rata-rata langkah sampai terserap: **{info['expected_steps']:.1f} langkah**.")
