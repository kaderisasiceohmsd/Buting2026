"""Halaman Streamlit: Lawan Bot Markov. Letakkan di folder pages/ repo buku angkatan."""
import sys
from pathlib import Path

import streamlit as st

# Pastikan root repo (berisi markov_rps/) bisa di-import dari halaman ini.
ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

try:
    st.set_page_config(page_title="Lawan Bot Markov", page_icon="🪨", layout="wide")
except Exception:  # sudah diatur oleh app.py
    pass

from markov_rps.ui import main  # noqa: E402

main()
