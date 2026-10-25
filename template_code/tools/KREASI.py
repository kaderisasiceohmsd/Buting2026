
import streamlit as st
import random

st.title("❤️ Kalkulator Cinta")
st.write("Cari tahu seberapa cocok kalian berdua!")

def kalkulator_cinta(nama1, nama2):
    if not nama1.strip() or not nama2.strip():
        return None

    persentase = random.randint(0, 100)
    return persentase

nama1 = st.text_input("Nama kamu:")
nama2 = st.text_input("Nama pasanganmu:")

if st.button("Hitung Kecocokan ❤️"):
    hasil = kalkulator_cinta(nama1, nama2)

    if hasil is None:
        st.warning("Masukkan kedua nama terlebih dahulu!")
    else:
        st.subheader(f"{nama1} ❤️ {nama2}")
        st.metric("Persentase Cinta", f"{hasil}%")
        st.progress(hasil)

        if hasil >= 90:
            st.success("Ciee!! Calon pasangan ideal! 💕")
        elif hasil >= 80:
            st.info("Wah, cocok nih, tinggal nunggu jadian 💖")
        elif hasil >= 50:
            st.info("Ada kecocokan nih! 💗")
        elif hasil >= 30:
            st.info("Ayo kasih effort lagi!!❤️")
        else:
            st.warning("Jangan menyerah, cinta butuh usaha! 💌")
