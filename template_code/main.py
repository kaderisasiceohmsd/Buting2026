import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Nama_Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/013_Faiz Hikmawan.py",
    title="013 - Faiz Hikmawan",
    icon=":material/person:",
)

Mahasiswa2 = st.Page(
    "Buku Kating/014_Valen Uswatun Fauziyah Putri.py",
    title="014 - Valen Uswatun Fauziyah Putri",
    icon=":material/person:",
)

Mahasiswa3 = st.Page(
    "Buku Kating/044_Zharifa Azizah Yudistira.py",
    title="044 - Zharifa Azizah Yudistira",
    icon=":material/person:",
)

Mahasiswa4 = st.Page(
    "Buku Kating/046_Theofani Saragih.py",
    title="046 - Theofani Saragih",
    icon=":material/person:",
)

Mahasiswa5 = st.Page(
    "Buku Kating/067_Andrew Chayadi.py",
    title="067 - Andrew Chayadi",
    icon=":material/person:",
)

Mahasiswa6 = st.Page(
    "Buku Kating/077_Muchamad Fahrell.py",
    title="077 - Muchamad Fahrell",
    icon=":material/person:",
)

Mahasiswa7 = st.Page(
    "Buku Kating/081_Nickolas Filbert Kartika.py",
    title="081 - Nickolas Filbert Kartika",
    icon=":material/person:",
)

Mahasiswa8 = st.Page(
    "Buku Kating/105_Muhammad Ayyas Haidar Farros.py",
    title="105 - Muhammad Ayyas Haidar Farros",
    icon=":material/person:",
)

Mahasiswa9 = st.Page(
    "Buku Kating/110_Rasya Zahira Umardi.py",
    title="110 - Rasya Zahira Umardi",
    icon=":material/person:",
)

Mahasiswa10 = st.Page(
    "Buku Kating/111_Nadia Callysta Putri.py",
    title="111 - Nadia Callysta Putri",
    icon=":material/person:",
)

Mahasiswa11 = st.Page(
    "Buku Kating/120_Muhammad Alifatih Freedom Haq.py",
    title="120 - Muhammad Alifatih Freedom Haq",
    icon=":material/person:",
)

Mahasiswa12 = st.Page(
    "Buku Kating/121_Warda Aliya Lubis.py",
    title="121 - Warda Aliya Lubis",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

