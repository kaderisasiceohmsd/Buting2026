import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Nama_Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/117_Nobel Nizam Fathirizki.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)

Mahasiswa2 = st.Page(
    "Buku Kating/013_Faiz Hikmawan.py",
    title="013 - Faiz Hikmawan",
    icon=":material/person:",
)

Mahasiswa3 = st.Page(
    "Buku Kating/081_Nickolas Filbert Kartika.py",
    title="081 - Nickolas Filbert Kartika",
    icon=":material/person:",
)

Mahasiswa4 = st.Page(
    "Buku Kating/077_Muchamad Fahrell.py",
    title="077 - Muchamad Fahrell",
    icon=":material/person:",
)

Mahasiswa5 = st.Page(
    "Buku Kating/105_Muhammad Ayyas Haidar Farros.py",
    title="105 - Muhammad Ayyas Haidar Farros",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

