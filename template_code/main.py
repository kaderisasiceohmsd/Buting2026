import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia
st.session_state.pindah = True

Homepage = st.Page(
    "Halaman Utama/halaman_utama.py", 
    title="Kelompok Pandas", 
    default=True
)

# Diurutkan berdasarkan NIM (027 -> 131)
Mahasiswa1 = st.Page(
<<<<<<< HEAD
    "Buku Kating/035_Pradana Ilhamsyah.py",
    title="035 - Pradana Ilhamsyah",
=======
    "Buku Kating/027_Zaky Firmansyah.py",
    title="027 - Zaky Firmansyah",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/034_Hasna Azwa Az Zahra.py",
    title="034 - Hasna Azwa Az Zahra",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/035_Pradana Ilhamsyah.py",
    title="035 - Pradana Ilhamsyah",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/049_Muhammad Haikal Farros.py",
    title="049 - Muhammad Haikal Farros",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/054_Marcellius Kevin Anggasana.py",
    title="054 - Marcellius Kevin Anggasana",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/079_Mas Renno Octaviano AR.py",
    title="079 - Mas Renno Octaviano AR",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/080_Ivana Ikshan.py",
    title="080 - Ivana Ikshan",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/092_Ridho Bitsiqah Akila Hartono.py",
    title="092 - Ridho Bitsiqah Akila Hartono",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/102_Citra Handayani Pakpahan.py",
    title="102 - Citra Handayani Pakpahan",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/126_Resti Amanda Ritonga.py",
    title="126 - Resti Amanda Ritonga",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/131_Mayang Nuraini.py",
    title="131 - Mayang Nuraini",
>>>>>>> a6543e5f84fecf062a2868651c368f68e328aee9
    icon=":material/person:",
)

# Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

# Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [
                Mahasiswa1,
                Mahasiswa2,
                Mahasiswa3,
                Mahasiswa4,
                Mahasiswa5,
                Mahasiswa6,
                Mahasiswa7,
                Mahasiswa8,
                Mahasiswa9,
                Mahasiswa10,
                Mahasiswa11,
            ],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(")

pg.run()