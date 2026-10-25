"""Logika permainan: aturan, bot, skor, dan riwayat ronde."""
from __future__ import annotations

import random
from dataclasses import dataclass

from .model import MOVES, MarkovChain, Prediction, counter_move

EMOJI = ("🪨", "✂️", "📄")


def outcome(player: int, bot: int) -> str:
    """Hasil dari sudut pandang pemain: Menang / Kalah / Seri."""
    if player == bot:
        return "Seri"
    return "Menang" if (player - bot) % 3 == 2 else "Kalah"


@dataclass(frozen=True)
class BotPlan:
    prediction: Prediction
    move: int
    mode: str   # "markov" | "eksplorasi" | "fallback"
    reason: str


@dataclass(frozen=True)
class Round:
    n: int
    player: int
    bot: int
    result: str
    plan: BotPlan

    @property
    def predicted(self):
        return self.plan.prediction.predicted

    @property
    def correct(self):
        return None if self.predicted is None else self.predicted == self.player


class Game:
    def __init__(self, epsilon: float = 0.15, seed: int | None = None):
        self.epsilon = epsilon          # peluang bot mengambil langkah acak
        self.rng = random.Random(seed)
        self.model = MarkovChain()
        self.history: list[Round] = []
        self.scores = {"Menang": 0, "Kalah": 0, "Seri": 0}
        self.plan = self._make_plan()

    def _make_plan(self) -> BotPlan:
        """Bot memilih langkah SEBELUM pemain memilih, hanya dari data ronde lalu."""
        pred = self.model.predict()
        if pred.state is None:
            return BotPlan(pred, self.rng.randrange(3), "fallback",
                           "Belum ada pilihan sebelumnya, jadi bot memilih acak.")
        s = MOVES[pred.state]
        if not pred.confident:
            return BotPlan(pred, self.rng.randrange(3), "fallback",
                           f"Baru {pred.row_n} transisi setelah {s} "
                           f"(minimal {self.model.min_row_obs}), jadi bot memilih acak.")
        top = MOVES[pred.predicted]
        share = f"{pred.probs[pred.predicted] * 100:.0f}%"
        if self.rng.random() < self.epsilon:
            return BotPlan(pred, self.rng.randrange(3), "eksplorasi",
                           f"Prediksi bot: {top} ({share}), tetapi ronde ini bot sengaja "
                           f"bermain acak ({self.epsilon:.0%}) agar tidak mudah ditebak.")
        move = counter_move(pred.predicted)
        return BotPlan(pred, move, "markov",
                       f"Pilihan terakhirmu {s}. Dari {pred.row_n} kali setelah {s}, "
                       f"{top} paling mungkin ({share}). Bot memilih {MOVES[move]} "
                       f"untuk mengalahkan {top}.")

    def play(self, player: int) -> Round:
        plan = self.plan
        result = outcome(player, plan.move)
        rnd = Round(len(self.history) + 1, player, plan.move, result, plan)
        self.history.append(rnd)
        self.scores[result] += 1
        self.model.observe(player)          # belajar baru setelah ronde selesai
        self.plan = self._make_plan()       # rencana untuk ronde berikutnya
        return rnd

    # ---- statistik prediksi aktual ------------------------------------
    def accuracy_stats(self):
        graded = [r for r in self.history if r.correct is not None]
        hit = sum(r.correct for r in graded)
        return hit, len(graded)
