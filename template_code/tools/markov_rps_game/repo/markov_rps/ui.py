"""Antarmuka Streamlit untuk 'Lawan Bot Markov: Batu Gunting Kertas'."""
from __future__ import annotations

import html
import math

import streamlit as st

from .engine import EMOJI, Game, Round
from .model import MOVES, pct_round

KEY = "markov_rps_game"

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@500;700;800&display=swap');
.block-container{max-width:1080px!important}
.rps-hero,.rps-card,.rps-score,.rps-arena,.rps-h,.hm,.hm-legend,.legend,.hist,.bar,.pick-tile,
.stButton button,div[data-testid="stButton"] button{font-family:'Nunito','Source Sans Pro',sans-serif}
.rps-hero h1{font-size:2.1rem;font-weight:800;margin:0;letter-spacing:-.5px}
.rps-hero p{margin:.2rem 0 1rem;opacity:.8}
.rps-h{font-weight:800;font-size:1.25rem;margin:22px 0 10px}
.rps-card{background:#fff;border-radius:22px;padding:16px 18px;
  box-shadow:0 10px 28px rgba(47,62,54,.10);margin-bottom:14px}
.rps-card h4{margin:0 0 .6rem;font-size:1.05rem;font-weight:800}
.rps-score{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:14px}
.rps-score div{background:#fff;border-radius:20px;padding:10px 6px;text-align:center;
  box-shadow:0 6px 18px rgba(47,62,54,.10)}
.rps-score b{display:block;font-size:1.9rem;line-height:1.1}
.rps-score span{font-size:.85rem;opacity:.75}
.rps-score .me b{color:#2E8B5E}.rps-score .bot b{color:#C2573F}
.rps-arena{display:grid;grid-template-columns:1fr minmax(120px,auto) 1fr;gap:10px;align-items:center;
  background:linear-gradient(160deg,#DCEBDD 0%,#BFDCC8 100%);border-radius:30px;
  padding:22px 14px;margin-bottom:18px;box-shadow:inset 0 -8px 0 rgba(47,62,54,.08)}
.rps-side{text-align:center}
.rps-side .who{font-weight:800;margin-bottom:6px}
.rps-tile{background:#fff;border-radius:28px;width:min(150px,34vw);aspect-ratio:1;margin:0 auto;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 9px 0 rgba(47,62,54,.14),0 18px 28px rgba(47,62,54,.16)}
.rps-tile svg{width:78%;height:78%}
.rps-side .nm{margin-top:16px;font-weight:800}
.rps-vs{text-align:center;font-weight:800;min-width:110px}
.rps-badge{display:inline-block;padding:8px 16px;border-radius:999px;color:#fff;font-size:1rem}
.win{background:#2E8B5E}.lose{background:#C2573F}.draw{background:#8A9A91}
@keyframes pop-a{0%{transform:scale(.3) rotate(-14deg);opacity:0}65%{transform:scale(1.12) rotate(3deg)}100%{transform:scale(1);opacity:1}}
@keyframes pop-b{0%{transform:scale(.3) rotate(-14deg);opacity:0}65%{transform:scale(1.12) rotate(3deg)}100%{transform:scale(1);opacity:1}}
@keyframes pulse-a{0%{transform:scale(.7);opacity:0}100%{transform:scale(1);opacity:1}}
@keyframes pulse-b{0%{transform:scale(.7);opacity:0}100%{transform:scale(1);opacity:1}}
.anim-a .rps-tile{animation:pop-a .5s ease-out}.anim-b .rps-tile{animation:pop-b .5s ease-out}
.anim-a .rps-badge{animation:pulse-a .45s .25s ease-out both}.anim-b .rps-badge{animation:pulse-b .45s .25s ease-out both}
.rps-tile.idle svg{opacity:.25}
/* ---- pilihan langkah: tile + tombol selebar kolom ---- */
.pick-tile{background:#fff;border-radius:22px;height:104px;width:100%;display:flex;align-items:center;
  justify-content:center;box-shadow:0 8px 20px rgba(47,62,54,.10);margin-bottom:10px}
.pick-tile svg{height:86px;width:auto}
.stButton,div[data-testid="stButton"]{width:100%!important;max-width:100%!important}
div[data-testid="stElementContainer"]:has(>div[data-testid="stButton"]){width:100%!important}
.stButton>button,div[data-testid="stButton"]>button{width:100%!important;min-height:3.3rem;
  display:flex;justify-content:center;align-items:center;border-radius:20px;border:0;
  background:#fff;color:#2F3E36;box-shadow:0 6px 0 rgba(47,62,54,.15);
  transition:transform .1s,background .2s,box-shadow .1s}
.stButton>button p,div[data-testid="stButton"]>button p{margin:0;text-align:center;font-size:1.2rem;font-weight:800}
.stButton>button:hover,div[data-testid="stButton"]>button:hover{background:#EAF4EC;color:#2F3E36;transform:translateY(-3px)}
.stButton>button:active,div[data-testid="stButton"]>button:active{transform:translateY(3px);box-shadow:0 2px 0 rgba(47,62,54,.15)}
.st-key-mv0 button{box-shadow:0 6px 0 #9AA6A0}
.st-key-mv1 button{box-shadow:0 6px 0 #E0705A}
.st-key-mv2 button{box-shadow:0 6px 0 #5B9BD5}
.st-key-mrps_reset button{background:#DCEBDD;min-height:2.7rem}
.st-key-mrps_reset button p{font-size:1rem}
/* ---- heatmap ---- */
.hm{width:100%;border-collapse:separate!important;border-spacing:6px;table-layout:fixed;text-align:center}
.hm,.hm tr,.hm th,.hm td{border:0!important}
.hm tr,.hm th{background:transparent!important}
.hm th,.hm td{text-align:center!important;vertical-align:middle!important}
.hm th{font-weight:700;font-size:.85rem;padding:4px}
.hm td{border-radius:14px;padding:12px 4px;font-weight:800;font-size:1.15rem;transition:background .4s}
.hm td small{display:block;font-weight:500;font-size:.7rem;opacity:.75}
.hm td.empty{background:#EEF3EF;color:#9AA7A0;font-weight:500}
.hm td.cur{outline:3px solid #2F3E36}
.hm-legend{display:flex;align-items:center;gap:8px;font-size:.78rem;opacity:.8;margin-top:8px}
.hm-legend i{flex:1;height:8px;border-radius:99px;background:linear-gradient(90deg,rgb(236,245,238),rgb(46,139,94))}
.bar{display:flex;align-items:center;gap:8px;margin:6px 0;font-size:.9rem}
.bar .lab{width:92px}.bar .track{flex:1;background:#E4EEE6;border-radius:99px;height:14px;overflow:hidden}
.bar .fill{height:100%;background:#7CB99A;border-radius:99px;transition:width .4s}
.bar .fill.top{background:#2E8B5E}.bar .pc{width:46px;text-align:right;font-weight:700}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:.85rem;margin:2px 0 4px}
.legend i{display:inline-block;width:18px;height:4px;border-radius:3px;margin-right:6px;vertical-align:middle}
.chart-wrap{background:#fff;border-radius:22px;padding:12px 14px;box-shadow:0 10px 28px rgba(47,62,54,.10)}
.chart-wrap svg{width:100%;height:auto;display:block}
.hist-wrap{overflow-x:auto;background:#fff;border-radius:22px;padding:6px 10px;box-shadow:0 10px 28px rgba(47,62,54,.10)}
.hist{width:100%;border-collapse:collapse!important;font-size:.9rem;white-space:nowrap}
.hist th,.hist td{border:0!important;border-bottom:1px solid #EEF3EF!important;background:transparent!important;
  text-align:center!important;padding:8px 10px}
.hist th{border-bottom:2px solid #DCEBDD!important;font-weight:800}
@media (max-width:640px){
  .rps-arena{grid-template-columns:1fr 1fr}.rps-vs{grid-column:1/-1;order:3}
  .rps-hero h1{font-size:1.6rem}.hm td{font-size:.95rem;padding:9px 2px}
  .pick-tile{display:none}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
"""

# ---- ilustrasi SVG ekspresif -------------------------------------------
_EYES = ('<circle cx="{a}" cy="{y}" r="4.5" fill="#2F3E36"/><circle cx="{b}" cy="{y}" r="4.5" fill="#2F3E36"/>'
         '<circle cx="{a1}" cy="{y1}" r="1.5" fill="#fff"/><circle cx="{b1}" cy="{y1}" r="1.5" fill="#fff"/>')


def _eyes(a, b, y):
    return _EYES.format(a=a, b=b, y=y, a1=a + 1.5, b1=b + 1.5, y1=y - 1.5)


SVGS = (
    # Batu
    '<svg viewBox="0 0 100 100"><ellipse cx="50" cy="90" rx="30" ry="6" fill="rgba(0,0,0,.12)"/>'
    '<path d="M16 64Q10 34 38 22Q68 12 84 38Q94 60 76 78Q50 90 26 80Z" fill="#9AA6A0"/>'
    '<path d="M30 34Q44 22 62 26" stroke="#C5CEC9" stroke-width="6" stroke-linecap="round" fill="none"/>'
    + _eyes(40, 60, 54) + '<path d="M42 68Q50 75 58 68" stroke="#2F3E36" stroke-width="3" fill="none" stroke-linecap="round"/></svg>',
    # Gunting
    '<svg viewBox="0 0 100 100"><ellipse cx="50" cy="92" rx="28" ry="5" fill="rgba(0,0,0,.12)"/>'
    '<path d="M50 52L28 8L38 6L56 46Z" fill="#B8C4CC"/><path d="M50 52L72 8L62 6L44 46Z" fill="#D5DEE3"/>'
    '<circle cx="34" cy="74" r="14" fill="none" stroke="#E0705A" stroke-width="9"/>'
    '<circle cx="66" cy="74" r="14" fill="none" stroke="#E0705A" stroke-width="9"/>'
    '<circle cx="50" cy="54" r="10" fill="#FFE08A"/>' + _eyes(46, 54, 52)
    + '<path d="M46 58Q50 62 54 58" stroke="#2F3E36" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg>',
    # Kertas
    '<svg viewBox="0 0 100 100"><ellipse cx="50" cy="92" rx="28" ry="5" fill="rgba(0,0,0,.12)"/>'
    '<path d="M22 10H64L82 28V84Q82 90 76 90H28Q22 90 22 84Z" fill="#FFFDF5" stroke="#C9D6CD" stroke-width="3"/>'
    '<path d="M64 10V28H82Z" fill="#DCEBDD" stroke="#C9D6CD" stroke-width="3" stroke-linejoin="round"/>'
    '<path d="M32 70H72M32 78H60" stroke="#DCEBDD" stroke-width="4" stroke-linecap="round"/>'
    + _eyes(42, 62, 46) + '<path d="M44 56Q52 64 60 56" stroke="#2F3E36" stroke-width="3" fill="none" stroke-linecap="round"/></svg>',
)
UNKNOWN = '<svg viewBox="0 0 100 100"><text x="50" y="68" font-size="60" text-anchor="middle" fill="#2F3E36">?</text></svg>'


# ---- state & aksi ------------------------------------------------------
def get_game() -> Game:
    if KEY not in st.session_state:
        st.session_state[KEY] = Game()
    return st.session_state[KEY]


def _btn(label: str, container=None, **kw):
    """Tombol selebar kolom; kompatibel dengan Streamlit lama (use_container_width) dan baru (width)."""
    target = container if container is not None else st
    try:
        return target.button(label, width="stretch", **kw)
    except TypeError:
        return target.button(label, use_container_width=True, **kw)


def _play(move: int) -> None:
    get_game().play(move)


def _reset() -> None:
    st.session_state[KEY] = Game()


# ---- komponen tampilan -------------------------------------------------
def _scoreboard(g: Game) -> str:
    s = g.scores
    return ('<div class="rps-score">'
            f'<div class="me"><b>{s["Menang"]}</b><span>🙂 Kamu menang</span></div>'
            f'<div><b>{s["Seri"]}</b><span>🤝 Seri</span></div>'
            f'<div class="bot"><b>{s["Kalah"]}</b><span>🤖 Bot menang</span></div></div>')


def _arena(last: Round | None) -> str:
    if last is None:
        tile = f'<div class="rps-tile idle">{UNKNOWN}</div>'
        side = lambda who: f'<div class="rps-side"><div class="who">{who}</div>{tile}<div class="nm">Pilih langkahmu</div></div>'
        return f'<div class="rps-arena">{side("Kamu")}<div class="rps-vs">VS</div>{side("Bot Markov")}</div>'
    ab = "a" if last.n % 2 else "b"
    cls, txt = {"Menang": ("win", "Kamu menang! 🎉"), "Kalah": ("lose", "Bot menang 🤖"),
                "Seri": ("draw", "Seri 🤝")}[last.result]
    side = lambda who, m: (f'<div class="rps-side"><div class="who">{who}</div>'
                           f'<div class="rps-tile">{SVGS[m]}</div><div class="nm">{MOVES[m]}</div></div>')
    return (f'<div class="rps-arena anim-{ab}">{side("Kamu", last.player)}'
            f'<div class="rps-vs"><div>Ronde {last.n}</div><div class="rps-badge {cls}">{txt}</div></div>'
            f'{side("Bot Markov", last.bot)}</div>')


def _heatmap(g: Game) -> str:
    m, c = g.model.matrix(), g.model.counts
    cur = g.model.last_state
    head = "".join(f"<th>{EMOJI[j]} {MOVES[j]}</th>" for j in range(3))
    rows = []
    for i in range(3):
        n = g.model.row_total(i)
        th = f'<th>{EMOJI[i]} {MOVES[i]}</th>'
        if n == 0:
            cells = '<td class="empty">–</td>' * 3
        else:
            pcts = pct_round(m[i])
            cells = ""
            for j in range(3):
                p = m[i][j]
                rgb = tuple(int(lo + (hi - lo) * p) for lo, hi in zip((236, 245, 238), (46, 139, 94)))
                fg = "#fff" if p > 0.5 else "#2F3E36"
                outline = " cur" if cur == i else ""
                cells += (f'<td class="{outline.strip()}" style="background:rgb{rgb};color:{fg}">'
                          f'{pcts[j]}%<small>n={c[i][j]}</small></td>')
        rows.append(f"<tr>{th}{cells}</tr>")
    return (f'<table class="hm"><tr><th style="width:24%">Sebelumnya ↓<br>Berikutnya →</th>{head}</tr>'
            + "".join(rows) + "</table>"
            '<div class="hm-legend"><span>0%</span><i></i><span>100%</span></div>')


def _bars(probs, top=None) -> str:
    pcts = pct_round(probs)
    out = ""
    for j in range(3):
        star = " ⭐" if j == top else ""
        out += (f'<div class="bar"><span class="lab">{EMOJI[j]} {MOVES[j]}{star}</span>'
                f'<span class="track"><span class="fill{" top" if j == top else ""}" style="width:{pcts[j]}%;display:block"></span></span>'
                f'<span class="pc">{pcts[j]}%</span></div>')
    return out


def _learning(g: Game) -> None:
    t = g.model.total_transitions
    status = ("Belum cukup data untuk mengenali pola" if t < 5
              else "Mulai mengumpulkan pola" if t < 20 else "Data cukup untuk uji pola kasar")
    hit, tot = g.accuracy_stats()
    if tot:
        note = " Terlalu sedikit untuk menyimpulkan." if tot < 10 else ""
        perf = (f"Performa prediksi aktual: {hit} dari {tot} tebakan benar "
                f"({hit / tot:.0%}); tebakan acak rata-rata 33%.{note}")
    else:
        perf = "Belum ada prediksi berbasis pola yang bisa dievaluasi."
    pct = min(t / 20, 1.0) * 100
    st.markdown(
        '<div class="rps-card"><h4>🧠 Indikator pembelajaran</h4>'
        f'<div><b>{t}</b> transisi teramati · <b>{status}</b></div>'
        f'<div class="bar"><span class="track"><span class="fill" style="width:{pct:.0f}%;display:block"></span></span>'
        f'<span class="pc">{min(t, 20)}/20</span></div>'
        f'<div style="font-size:.85rem;opacity:.8">{perf}</div></div>', unsafe_allow_html=True)


def _svg_line_chart(series: dict, colors: dict, dashed=(), y_title: str = "%", x_title: str = "Ronde") -> str:
    """Grafik garis SVG murni (tanpa Altair). series: nama -> daftar nilai 0-100 (None = tidak ada data)."""
    W, H, L, R, T, B = 640, 300, 52, 16, 14, 44
    n = max(len(v) for v in series.values())
    pw, ph = W - L - R, H - T - B

    def X(i: int) -> float:
        return L + (pw / 2 if n == 1 else pw * i / (n - 1))

    def Y(v: float) -> float:
        return T + ph * (1 - v / 100)

    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Grafik garis {html.escape(y_title)} per {html.escape(x_title)}">']
    for gv in (0, 25, 50, 75, 100):
        y = Y(gv)
        out.append(f'<line x1="{L}" x2="{W - R}" y1="{y:.1f}" y2="{y:.1f}" stroke="#C9D6CD" stroke-width="1"/>'
                   f'<text x="{L - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="12" fill="#2F3E36">{gv}%</text>')
    step = max(1, math.ceil(n / 8))
    for i in range(0, n, step):
        out.append(f'<text x="{X(i):.1f}" y="{H - B + 18}" text-anchor="middle" font-size="12" fill="#2F3E36">{i + 1}</text>')
    out.append(f'<text x="{L + pw / 2:.1f}" y="{H - 6}" text-anchor="middle" font-size="12" fill="#2F3E36">{html.escape(x_title)}</text>')
    out.append(f'<text transform="translate(14 {T + ph / 2:.1f}) rotate(-90)" text-anchor="middle" font-size="12" fill="#2F3E36">{html.escape(y_title)}</text>')

    for name, vals in series.items():
        color = colors[name]
        dash = ' stroke-dasharray="6 5"' if name in dashed else ""
        segs, cur = [], []
        for i, v in enumerate(vals):
            if v is None:
                if cur:
                    segs.append(cur)
                cur = []
            else:
                cur.append((i, v))
        if cur:
            segs.append(cur)
        for seg in segs:
            if len(seg) > 1:
                d = " ".join(("M" if k == 0 else "L") + f"{X(i):.1f} {Y(v):.1f}" for k, (i, v) in enumerate(seg))
                out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5" '
                           f'stroke-linejoin="round" stroke-linecap="round"{dash}/>')
        if name not in dashed:
            for seg in segs:
                for k, (i, v) in enumerate(seg):
                    if n <= 60 or len(seg) == 1 or (seg is segs[-1] and k == len(seg) - 1):
                        out.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3.5" fill="{color}">'
                                   f'<title>{html.escape(name)} - ronde {i + 1}: {v:.0f}%</title></circle>')
    out.append("</svg>")
    legend = "".join(f'<span><i style="background:{colors[k]}"></i>{html.escape(k)}</span>' for k in series)
    return f'<div class="chart-wrap"><div class="legend">{legend}</div>{"".join(out)}</div>'


def _charts(g: Game) -> None:
    if not g.history:
        st.info("Grafik akan muncul setelah ronde pertama.")
        return
    t1, t2 = st.tabs(["Akurasi prediksi bot", "Distribusi pilihanmu"])
    with t1:
        acc, hit, n = [], 0, 0
        for r in g.history:
            if r.correct is not None:
                n += 1
                hit += r.correct
            acc.append(hit / n * 100 if n else None)
        if n:
            st.markdown(_svg_line_chart(
                {"Akurasi bot (%)": acc, "Tebakan acak (%)": [100 / 3] * len(acc)},
                {"Akurasi bot (%)": "#2E8B5E", "Tebakan acak (%)": "#C2573F"},
                dashed=("Tebakan acak (%)",), y_title="Akurasi (%)"), unsafe_allow_html=True)
        else:
            st.caption("Bot belum membuat prediksi berbasis pola.")
        st.caption("Akurasi kumulatif hanya dari ronde saat bot punya cukup data. "
                   "Garis tebakan acak adalah pembanding.")
    with t2:
        cnt = [0, 0, 0]
        share = {m: [] for m in MOVES}
        for k, r in enumerate(g.history, start=1):
            cnt[r.player] += 1
            for j, m in enumerate(MOVES):
                share[m].append(cnt[j] / k * 100)
        st.markdown(_svg_line_chart(
            share, {"Batu": "#7A8A83", "Gunting": "#E0705A", "Kertas": "#5B9BD5"},
            y_title="% pilihan"), unsafe_allow_html=True)


def _history(g: Game) -> None:
    if not g.history:
        st.caption("Belum ada ronde.")
        return
    head = ["Ronde", "Kamu", "Bot", "Hasil", "Prediksi bot", "Status", "Mode bot"]
    body = ""
    for r in reversed(g.history[-20:]):
        pred = "—" if r.predicted is None else MOVES[r.predicted]
        stat = "—" if r.correct is None else ("✅ Benar" if r.correct else "❌ Salah")
        cells = [r.n, f"{EMOJI[r.player]} {MOVES[r.player]}", f"{EMOJI[r.bot]} {MOVES[r.bot]}",
                 r.result, pred, stat, r.plan.mode]
        body += "<tr>" + "".join(f"<td>{html.escape(str(c))}</td>" for c in cells) + "</tr>"
    st.markdown('<div class="hist-wrap"><table class="hist"><tr>'
                + "".join(f"<th>{h}</th>" for h in head) + f"</tr>{body}</table></div>",
                unsafe_allow_html=True)


def _education() -> None:
    with st.expander("📚 Cara kerja Markov Chain (klik untuk membuka)"):
        st.markdown("""
**Apa itu Markov Chain?** Model yang memprediksi langkah berikutnya hanya dari keadaan saat ini, tanpa melihat jauh ke belakang. Di sini keadaannya adalah pilihan terakhirmu (orde satu).

**State dan transisi.** State adalah Batu, Gunting, atau Kertas. Transisi adalah perpindahan dari pilihan satu ronde ke pilihan ronde berikutnya, misalnya Batu → Kertas.

**Membentuk transition matrix.** Setiap pasangan pilihan berurutan dihitung. Baris adalah pilihan sebelumnya, kolom adalah pilihan berikutnya:
`P(i → j) = (jumlah transisi i→j + pseudocount) / (total transisi dari i + 3 × pseudocount)`.
Pseudocount 1 menjaga probabilitas tetap terdefinisi saat data masih sedikit, dan setiap baris berjumlah 100%.

**Probabilitas untuk prediksi.** Bot melihat baris dari pilihan terakhirmu, mengambil kolom dengan probabilitas tertinggi sebagai tebakan, lalu memilih langkah yang mengalahkannya. Bot memilih sebelum kamu memilih, memakai data ronde sebelumnya saja.

**Mengapa bisa salah?** Matriks hanya merangkum pola masa lalu. Data sedikit, pola berubah, atau kamu sengaja mengubah strategi akan membuat tebakan meleset. Bot juga sesekali bermain acak, sehingga kamu masih bisa menang.

**Pola vs acak murni.** Jika pilihanmu benar-benar acak, semua sel mendekati 33% dan bot hanya menebak kebetulan, sehingga akurasinya akan mendekati 33%. Bila ada kebiasaan, sebagian sel akan menonjol dan akurasi bisa di atas 33%, tetapi tidak pernah dijamin.
""")


# ---- halaman utama -----------------------------------------------------
def main() -> None:
    st.markdown(CSS, unsafe_allow_html=True)
    g = get_game()
    st.markdown('<div class="rps-hero"><h1>🪨✂️📄 Lawan Bot Markov</h1>'
                '<p>Bot ini mempelajari kebiasaanmu lewat Markov Chain. Bisakah kamu bermain acak?</p></div>',
                unsafe_allow_html=True)

    st.markdown(_scoreboard(g), unsafe_allow_html=True)
    last = g.history[-1] if g.history else None
    st.markdown(_arena(last), unsafe_allow_html=True)

    st.markdown('<div class="rps-h" style="text-align:center;margin-top:4px">Pilih langkahmu</div>',
                unsafe_allow_html=True)
    cols = st.columns(3, gap="small")
    for i, col in enumerate(cols):
        col.markdown(f'<div class="pick-tile">{SVGS[i]}</div>', unsafe_allow_html=True)
        _btn(f"{EMOJI[i]} {MOVES[i]}", container=col, key=f"mv{i}", on_click=_play, args=(i,))

    left, right = st.columns([1.15, 1])
    with left:
        st.markdown('<div class="rps-card"><h4>🔥 Transition matrix (kamu)</h4>' + _heatmap(g)
                    + '<div style="font-size:.78rem;opacity:.7;margin-top:6px">Persentase sudah termasuk '
                    'smoothing (pseudocount 1). n = jumlah transisi teramati. Kotak tebal = baris yang '
                    'dipakai bot berikutnya. "–" = belum ada data.</div></div>', unsafe_allow_html=True)
        _learning(g)
    with right:
        if last is None:
            body = "Mainkan ronde pertama. Bot belum punya data apa pun."
        else:
            p = last.plan.prediction
            top = p.predicted if last.plan.mode != "fallback" else None
            body = (f"<b>Prediksi ronde {last.n}</b><br>{_bars(p.probs, top)}"
                    f'<div style="font-size:.9rem;margin-top:8px">💬 {last.plan.reason}</div>')
            if p.predicted is not None:
                body += (f'<div style="font-size:.9rem;margin-top:6px">'
                         f'Hasil: {"tebakan benar ✅" if last.correct else "tebakan salah ❌"}</div>')
        st.markdown(f'<div class="rps-card"><h4>🤖 Prediksi bot</h4>{body}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="rps-card"><h4>💡 Insight dari datamu</h4>{g.model.insight()}</div>',
                    unsafe_allow_html=True)
        if st.toggle("Intip prediksi ronde berikutnya (mode curang)", key="mrps_peek"):
            q = g.plan.prediction
            msg = (_bars(q.probs, q.predicted) if q.state is not None else "Belum ada data.")
            st.markdown(f'<div class="rps-card">{msg}</div>', unsafe_allow_html=True)
        _btn("🔄 Mulai Ulang", key="mrps_reset", on_click=_reset)

    st.markdown('<div class="rps-h">📈 Perkembangan</div>', unsafe_allow_html=True)
    _charts(g)
    st.markdown('<div class="rps-h">🧾 Riwayat ronde</div>', unsafe_allow_html=True)
    _history(g)
    st.caption("Markov Chain hanya memodelkan pola transisi dari data yang teramati. Model tidak "
               "bisa memastikan pilihanmu berikutnya, terutama jika kamu mengubah strategi atau memilih acak.")
    _education()
