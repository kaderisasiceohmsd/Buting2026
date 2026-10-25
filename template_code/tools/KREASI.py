
import streamlit as st
import sys
from pathlib import Path

st.set_page_config(layout="wide")

GAME_DIR = Path(__file__).resolve().parent / "frog_jump_app"

if str(GAME_DIR) not in sys.path:
    sys.path.insert(0, str(GAME_DIR))

st.markdown(
    """
    <style>
    .block-container {
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

from frog_jump.ui import render

render()
