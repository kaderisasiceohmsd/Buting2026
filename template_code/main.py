import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/Halaman Utama.py",
    title="02 Jacobi",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/006_Dandy Romansyah.py",
    title="006 - Dandy Romansyah",
    icon=":material/person:",
)

Mahasiswa2 = st.Page(
    "Buku Kating/058_Dea Febryana.py",
    title="058 - Dea Febryana",
    icon=":material/person:",
)

Mahasiswa3 = st.Page(
    "Buku Kating/004_Eyi Adelia.py",
    title="004 - Eyi Adelia",
    icon=":material/person:",
)

Mahasiswa4 = st.Page(
    "Buku Kating/041_Zahro Khoirunnisa.py",
    title="041 - Zahro Khoirunnisa",
    icon=":material/person:",
)

Mahasiswa5 = st.Page(
    "Buku Kating/053_Laura Brety Br Ginting.py",
    title="053 - Laura Brety Br Ginting",
    icon=":material/person:",
)

Mahasiswa6 = st.Page(
    "Buku Kating/076_Dhani Harianto.py",
    title="076 - Dhani Harianto",
    icon=":material/person:",
)

Mahasiswa7 = st.Page(
    "Buku Kating/087_M.Ramadhan Bagus Ar-Rahman.py",
    title="087 - M.Ramadhan Bagus Ar-Rahman",
    icon=":material/person:",
)

Mahasiswa8 = st.Page(
    "Buku Kating/088_Dimas Ardhiteo Putra.py",
    title="088 - Dimas Ardhiteo Putra",
    icon=":material/person:",
)

Mahasiswa9 = st.Page(
    "Buku Kating/089_Krisna Alviansyah.py",
    title="089 - Krisna Alviansyah",
    icon=":material/person:",
)

Mahasiswa10 = st.Page(
    "Buku Kating/114_Riva Septia Nanda.py",
    title="114 - Riva Septia Nanda",
    icon=":material/person:",
)

Mahasiswa11 = st.Page(
    "Buku Kating/118_Halidaziyah Maritoma Hasibuan.py",
    title="118 - Halidaziyah Maritoma Hasibuan",
    icon=":material/person:",
)

Mahasiswa12 = st.Page(
    "Buku Kating/119_Aura Krisna Azzira.py",
    title="119 - Aura Krisna Azzira",
    icon=":material/person:",
)

Mahasiswa13 = st.Page(
    "Buku Kating/130_Rahman Syapei.py",
    title="130 - Rahman Syapei",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12, Mahasiswa13],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

