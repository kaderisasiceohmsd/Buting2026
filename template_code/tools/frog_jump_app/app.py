import streamlit as st

st.set_page_config(page_title="Frog Jump", page_icon="🐸", layout="wide")

st.title("Frog Jump")
st.write(
    "Mini-game edukasi sains data: kodok melompat di antara lima daun teratai "
    "dan kamu mengatur peluangnya. Dari situ kamu bisa melihat langsung apa itu "
    "Markov chain."
)
st.page_link("pages/1_Frog_Jump.py", label="Mulai bermain", icon="🐸")
