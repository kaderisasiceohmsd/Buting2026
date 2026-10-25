"""Markov Chain orde satu untuk memodelkan urutan pilihan pemain.

State  : Batu (0), Gunting (1), Kertas (2)
Matriks: baris = pilihan sebelumnya, kolom = pilihan berikutnya.
P(i -> j) = (count[i, j] + alpha) / (sum_j count[i, j] + alpha * 3)
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

MOVES = ("Batu", "Gunting", "Kertas")
N = len(MOVES)


def counter_move(move: int) -> int:
    """Langkah yang mengalahkan `move` (Batu<Kertas, Gunting<Batu, Kertas<Gunting)."""
    return (move + 2) % N


def pct_round(probs) -> list[int]:
    """Bulatkan probabilitas ke persen bulat dengan jumlah tepat 100 (largest remainder)."""
    raw = np.asarray(probs, dtype=float) * 100
    floors = np.floor(raw).astype(int)
    missing = 100 - int(floors.sum())
    for k in np.argsort(-(raw - floors))[:missing]:
        floors[k] += 1
    return floors.tolist()


@dataclass(frozen=True)
class Prediction:
    state: int | None        # pilihan terakhir pemain (baris yang dipakai)
    probs: tuple             # distribusi probabilitas pilihan berikutnya
    predicted: int | None    # None bila data belum cukup
    row_n: int               # jumlah transisi teramati dari state tsb
    confident: bool


class MarkovChain:
    def __init__(self, pseudocount: float = 1.0, min_row_obs: int = 3):
        self.alpha = pseudocount
        self.min_row_obs = min_row_obs
        self.reset()

    def reset(self) -> None:
        self.counts = np.zeros((N, N), dtype=int)
        self.last_state: int | None = None

    # ---- pembelajaran -------------------------------------------------
    def observe(self, move: int) -> None:
        """Catat pilihan pemain. Dipanggil SETELAH ronde selesai."""
        if self.last_state is not None:
            self.counts[self.last_state, move] += 1
        self.last_state = move

    @property
    def total_transitions(self) -> int:
        return int(self.counts.sum())

    def row_total(self, i: int) -> int:
        return int(self.counts[i].sum())

    def matrix(self) -> np.ndarray:
        """Matriks transisi 3x3 dengan smoothing; setiap baris berjumlah 1."""
        smoothed = self.counts + self.alpha
        return smoothed / smoothed.sum(axis=1, keepdims=True)

    # ---- prediksi (hanya memakai data sebelum ronde berjalan) ---------
    def predict(self) -> Prediction:
        s = self.last_state
        if s is None:
            return Prediction(None, (1 / N,) * N, None, 0, False)
        probs = self.matrix()[s]
        n = self.row_total(s)
        ok = n >= self.min_row_obs
        return Prediction(s, tuple(float(p) for p in probs),
                          int(np.argmax(probs)) if ok else None, n, ok)

    # ---- insight dari data nyata --------------------------------------
    def insight(self) -> str:
        t = self.total_transitions
        if t < 5:
            return (f"Baru {t} transisi yang teramati. Mainkan beberapa ronde lagi "
                    "sebelum ada pola yang bisa dibaca.")
        best = None
        for i in range(N):
            n = self.row_total(i)
            if n < self.min_row_obs:
                continue
            j = int(np.argmax(self.counts[i]))
            p = self.counts[i, j] / n
            z = (p - 1 / N) / math.sqrt((1 / N) * (1 - 1 / N) / n)
            if best is None or z > best[4]:
                best = (i, j, n, p, z)
        if best is None:
            return "Belum ada pilihan sebelumnya yang muncul cukup sering untuk dianalisis."
        i, j, n, p, z = best
        c = int(self.counts[i, j])
        text = (f"Setelah memilih {MOVES[i]}, kamu memilih {MOVES[j]} "
                f"sebanyak {c} dari {n} kali ({p * 100:.0f}%).")
        if z >= 1.64:
            text += " Ini cukup menonjol dibanding tebakan acak (33%), tetapi bukan jaminan."
        else:
            text += " Selisihnya dari tebakan acak (33%) belum cukup kuat; bisa jadi hanya kebetulan."
        if n < 10:
            text += " Jumlah datanya masih terbatas."
        return text
