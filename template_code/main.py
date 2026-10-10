import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Bayesian",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/085_Thomas Yustio.py",
    title="085 - Thomas Yustio",
    icon=":material/person:",
)

Mahasiswa2 = st.Page(
    "Buku Kating/050_Syalom Jubilate Nauli Simanjuntak.py",
    title="050 - Syalom Jubilate Nauli Simanjuntak",
    icon=":material/person:",
)

Mahasiswa3 = st.Page(
    "Buku Kating/026_Chavia Chairunissa.py",
    title="026 - Chavia Chairunissa",
    icon=":material/person:",
)

Mahasiswa4 = st.Page(
    "Buku Kating/038_Aqila Chika Aurelia.py",
    title="038 - Aqila Chika Aurelia",
    icon=":material/person:",
)

Mahasiswa5 = st.Page(
    "Buku Kating/042_Sefina Amanda Putri.py",
    title="042 - Sefina Amanda Putri",
    icon=":material/person:",
)

Mahasiswa6 = st.Page(
    "Buku Kating/047_Aura Putri Ghefira.py",
    title="047 - Aura Putri Ghefira",
    icon=":material/person:",
)


Mahasiswa7 = st.Page(
    "Buku Kating/052_Ezra Hamizan.py",
    title="052 - Ezra Hamizan",
    icon=":material/person:",
)

Mahasiswa8 = st.Page(
    "Buku Kating/061_Afdhi Hafiidz Habibie.py",
    title="061 - Afdhi Hafiidz Habibie",
    icon=":material/person:",
)

Mahasiswa9 = st.Page(
    "Buku Kating/066_Rizqy Ramadhan.py",
    title="066 - Rizqy Ramadhan",
    icon=":material/person:",
)

Mahasiswa10 = st.Page(
    "Buku Kating/091_Alan Garcia Sinaga.py",
    title="091 - Alan Garcia Sinaga",
    icon=":material/person:",
)

#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

