import streamlit as st
import random

st.set_page_config(page_title="Gold Vault Challenge", layout="centered")

st.markdown("""
<style>
.stApp {
    background-color: #0b0b0b;
    color: #e5e5e5;
}
h1, h2, h3 {
    color: #ffd700 !important;
    font-family: 'Helvetica Neue', sans-serif;
}
.stMetric {
    background-color: #161616;
    border: 1px solid #d4af37;
    padding: 15px;
    border-radius: 8px;
}
[data-testid="stMetricValue"] {
    color: #ffd700 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Gold Vault Challenge")
st.markdown("Tebak kombinasi angka rahasia brankas antara 1 sampai 100.")

if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

if not st.session_state.game_over:
    guess = st.number_input("Masukkan Angka Tebakan Anda", min_value=1, max_value=100, step=1)
    
    if st.button("Coba Buka Brankas"):
        st.session_state.attempts += 1
        if guess == st.session_state.secret_number:
            st.session_state.game_over = True
            st.rerun()
        elif guess < st.session_state.secret_number:
            st.warning("Angka terlalu kecil. Naikkan tebakan Anda.")
        else:
            st.warning("Angka terlalu besar. Turunkan tebakan Anda.")
            
    st.metric("Total Percobaan", st.session_state.attempts)
else:
    st.success(f"Brankas Berhasil Dibuka dalam {st.session_state.attempts} percobaan!")
    if st.button("Main Lagi"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
