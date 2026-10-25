
"""Halaman Kreasi 2: Lawan Bot Markov."""

import sys
from pathlib import Path

import streamlit as st

# Lokasi folder game yang berisi paket markov_rps
GAME_REPO = (
    Path(__file__).resolve().parent
    / "markov_rps_game"
    / "repo"
)

if str(GAME_REPO) not in sys.path:
    sys.path.insert(0, str(GAME_REPO))

try:
    st.set_page_config(
        page_title="Kreasi 2 - Lawan Bot Markov",
        page_icon="🪨",
        layout="wide",
    )
except Exception:
    pass

from markov_rps.ui import main

main()
