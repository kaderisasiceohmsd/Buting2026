import sys
from pathlib import Path

import streamlit as st

# Agar halaman ini juga bisa dijalankan langsung (streamlit run pages/1_Frog_Jump.py)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

st.set_page_config(page_title="Frog Jump", page_icon="🐸", layout="wide")

from frog_jump.ui import render  # noqa: E402

render()
