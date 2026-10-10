import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Markov",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/023_Muhamad Helmi Fahma.py",
    title="023 - Muhamad Helmi Fahma",
    icon=":material/person:",
)

Mahasiswa2 = st.Page(
    "Buku Kating/039_Diah Ayu Puspita Sastra.py",
    title="039 - Diah Ayu Puspita Sastra",
    icon=":material/person:",
)

Mahasiswa3 = st.Page(
    "Buku Kating/007_Indah Lestari.py",
    title="007 - Indah Lestari",
    icon=":material/person:",
)

Mahasiswa4 = st.Page(
    "Buku Kating/025_Lian Ilham Nurthoriq.py",
    title="025 - Lian Ilham Nurthoriq",
    icon=":material/person:",
)

Mahasiswa5 = st.Page(
    "Buku Kating/016_Sakinah Farhana Al Qisthi.py",
    title="016 - Sakinah Farhana Al Qisthi",
    icon=":material/person:",
)

Mahasiswa6 = st.Page(
    "Buku Kating/024_Armeyza Varyan.py",
    title="024 - Armeyza Varyan",
    icon=":material/person:",
)

Mahasiswa7 = st.Page(
    "Buku Kating/090_Maryam Zahra Rahmadani.py",
    title="090 - Maryam Zahra Rahmadani",
    icon=":material/person:",
)

Mahasiswa8 = st.Page(
    "Buku Kating/032_Nisa Aura.py",
    title="032 - Nisa Aura",
    icon=":material/person:",
)

Mahasiswa9 = st.Page(
    "Buku Kating/056_Sapta Daffa Mulya.py",
    title="056 - Sapta Daffa Mulya",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(")
pg.run()

