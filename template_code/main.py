import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="01 Jordan",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/002_Sayyidina Najwa Syahra.py",
    title="002 - Sayyidina Najwa Syahra",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/005_Septi Widia Arin.py",
    title="005 - Septi Widia Arin",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/036_Astrit Aisyah Rahmi.py",
    title="036 - Astrit Aisyah Rahmi",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/040_Fildzah Cahya Kamila.py",
    title="040 - Fildzah Cahya Kamila",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/062_Iva Aulia Sofia.py",
    title="062 - Iva Aulia Sofia",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/064_Lintar Abhinaya Putra Zulmi.py",
    title="064 - Lintar Abhinaya Putra Zulmi",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/068_Bening Arianti.py",
    title="068 - Bening Arianti",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/069_Ahda Nabiwa.py",
    title="069 - Ahda Nabiwa",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/093_Rahmad Bayu Ridho.py",
    title="093 - Rahmad Bayu Ridho",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/094_Mojes Wijaya.py",
    title="094 - Mojes Wijaya",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/095_M Rafli Raditya.py",
    title="095 - M Rafli Raditya",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/104_M Abyan Alghaniyyu.py",
    title="104 - M Abyan Alghaniyyu",
    icon=":material/person:",
)
Mahasiswa13 = st.Page(
    "Buku Kating/106_Bintang Mahardika.py",
    title="106 - Bintang Mahardika",
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
                Mahasiswa12,
                Mahasiswa13,
            ],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

