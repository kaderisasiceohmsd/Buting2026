import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="07 - POISSON",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/116_Yobel Imanuel Pasaribu.py",
    title="116 - Yobel Imanuel Pasaribu",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/109_Rena Aprilia.py",
    title="109 - Rena Aprilia",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/020_Fadhilah Adelyia Putri.py",
    title="020 - Fadhilah Adelyia Putri",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/075_Inness Eymard Gultom.py",
    title="075 - Inness Eymard Gultom",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/084_Samuel Kristian.py",
    title="084 - Samuel Kristian",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/008_Egia Ninta Pepayosa Ketaren.py",
    title="008 - Egia Ninta Pepayosa Ketaren",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/028_Dzahra Adila Fatma.py",
    title="028 - Dzahra Adila Fatma",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/018_Achmad Fardhan Al Basri Bandarudin.py",
    title="018 - chmad Fardhan Al Basri Bandarudin",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/033_Kayyisah Mazaya.py",
    title="033 - Kayyisah Mazaya",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/074_Alfajri Anwar.py",
    title="074 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/037_Nailatun Inayah.py",
    title="037 - Nailatun Inayah",
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
            "Buku Kating": [Mahasiswa1],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

