"""
Mesin simulasi Frog Jump: murni Python + NumPy, tanpa Streamlit.

Model: 5 daun (state 0..4). Dari tiap daun kodok bisa lompat ke kiri,
ke kanan, atau diam. Di daun paling kiri/kanan, lompatan yang mustahil
(keluar dari barisan) otomatis menjadi "diam".
"""
from __future__ import annotations

import numpy as np

N_STATE = 5
TOL = 1e-9


def validate(p_left: float, p_right: float) -> float:
    """Pastikan peluang valid; kembalikan p_diam = 1 - kiri - kanan."""
    if not (0 <= p_left <= 1 and 0 <= p_right <= 1):
        raise ValueError("Peluang harus di antara 0 dan 1.")
    if p_left + p_right > 1 + TOL:
        raise ValueError("Peluang kiri + kanan tidak boleh lebih dari 100%.")
    return max(0.0, 1.0 - p_left - p_right)


def build_matrix(p_left, p_right, trap=None, absorbing=False) -> np.ndarray:
    """Matriks transisi 5x5. Baris = daun sekarang, kolom = daun berikutnya."""
    p_stay = validate(p_left, p_right)
    P = np.zeros((N_STATE, N_STATE))
    for i in range(N_STATE):
        P[i, i] += p_stay
        P[i, i - 1 if i > 0 else i] += p_left      # kiri (di tepi -> diam)
        P[i, i + 1 if i < N_STATE - 1 else i] += p_right  # kanan (di tepi -> diam)
    if absorbing and trap is not None:             # jebakan menangkap selamanya
        P[trap, :] = 0.0
        P[trap, trap] = 1.0
    if not np.allclose(P.sum(axis=1), 1.0, atol=TOL):
        raise ValueError("Setiap baris matriks harus berjumlah 100%.")
    return P


def simulate(P: np.ndarray, start: int, n_steps: int, seed: int) -> list[int]:
    """Lintasan kodok: daftar state sepanjang n_steps + 1 titik."""
    rng = np.random.default_rng(seed)
    path = [int(start)]
    for _ in range(n_steps):
        path.append(int(rng.choice(len(P), p=P[path[-1]])))
    return path


def is_irreducible(P: np.ndarray) -> bool:
    """Apakah setiap daun bisa dicapai dari daun mana pun?"""
    n = len(P)
    reach = np.linalg.matrix_power((P > 0).astype(float) + np.eye(n), n - 1)
    return bool((reach > 0).all())


def stationary(P: np.ndarray) -> np.ndarray:
    """Distribusi stasioner pi, dari pi P = pi dengan jumlah pi = 1."""
    n = len(P)
    A = np.vstack([P.T - np.eye(n), np.ones(n)])
    b = np.zeros(n + 1)
    b[-1] = 1.0
    pi = np.linalg.lstsq(A, b, rcond=None)[0]
    pi = np.clip(pi, 0, None)
    return pi / pi.sum()


def absorption_analysis(P: np.ndarray, start: int):
    """Absorbing state, peluang terserap, dan rata-rata langkah sampai terserap."""
    n = len(P)
    absb = [i for i in range(n) if np.isclose(P[i, i], 1.0)]
    if not absb:
        return [], [], None
    if start in absb:
        return absb, [1.0 if a == start else 0.0 for a in absb], 0.0
    trans = [i for i in range(n) if i not in absb]
    Q, R = P[np.ix_(trans, trans)], P[np.ix_(trans, absb)]
    try:
        M = np.eye(len(trans)) - Q
        probs = np.linalg.solve(M, R)[trans.index(start)]
        steps = float(np.linalg.solve(M, np.ones(len(trans)))[trans.index(start)])
    except np.linalg.LinAlgError:
        return absb, [], None
    return absb, [float(x) for x in probs], steps


def analyze(P: np.ndarray, start: int) -> dict:
    """Cek asumsi matematis dan hitung nilai teoritis bila valid."""
    irreducible = is_irreducible(P)
    aperiodic = irreducible and bool((np.diag(P) > 0).any())
    ergodic = irreducible and aperiodic
    absb, absb_probs, steps = absorption_analysis(P, start)
    pi = stationary(P) if ergodic else None
    if ergodic:
        note = "Rantai ergodik, jadi frekuensi kunjungan boleh dibandingkan dengan distribusi stasioner."
    elif absb:
        nama = ", ".join(f"Daun {a + 1}" for a in absb)
        note = (f"Ada absorbing state ({nama}), jadi rantai tidak irreducible. "
                "Kodok akhirnya terperangkap di sana dan distribusi stasioner tidak "
                "bisa dipakai sebagai pembanding.")
    else:
        note = "Rantai tidak memenuhi asumsi ergodik, jadi tidak ada pembanding teori."
    return {
        "irreducible": irreducible, "aperiodic": aperiodic, "ergodic": ergodic,
        "stationary": None if pi is None else [float(x) for x in pi],
        "absorbing": absb, "absorb_probs": absb_probs, "expected_steps": steps,
        "note": note,
    }
