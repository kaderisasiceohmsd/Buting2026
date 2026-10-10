import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Anova",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/015_Tiara Amelia.py",
    title="015 - Tiara Amelia",
    icon=":material/person:",
)

Mahasiswa2 = st.Page(
    "Buku Kating/017_Muhammad Rizky Pratama.py",
    title="017 - Muhammad Rizky Pratama",
    icon=":material/person:",
)

Mahasiswa3 = st.Page(
    "Buku Kating/029_Rasya Rajid Pratama.py",
    title="029 - Rasya Rajid Pratama",
    icon=":material/person:",
)

Mahasiswa4 = st.Page(
    "Buku Kating/031_Elena Fariza Zahra.py",
    title="031 - Elena Fariza Zahra",
    icon=":material/person:",
)

Mahasiswa5 = st.Page(
    "Buku Kating/065_Muhammad Irfan Nugraha.py",
    title="065 - Muhammad Irfan Nugraha.py",
    icon=":material/person:",
)

Mahasiswa6 = st.Page(
    "Buku Kating/078_Elisabeth Yulyanti Gultom.py",
    title="078 - Elisabeth Yulyanti Gultom",
    icon=":material/person:",
)

Mahasiswa7 = st.Page(
    "Buku Kating/086_Zetkin Alando Dzaqwan.py",
    title="086 - Zetkin Alando Dzaqwan",
    icon=":material/person:",
)

Mahasiswa8 = st.Page(
    "Buku Kating/108_Jhonatan Best Kingsil Sakerebau.py",
    title="108 - Jhonatan Best Kingsil Sakerebau",
    icon=":material/person:",
)

Mahasiswa9 = st.Page(
    "Buku Kating/117_Jeanis Nahwadisa.py",
    title="117 - Jeanis Nahwadisa",
    icon=":material/person:",
)

Mahasiswa10 = st.Page(
    "Buku Kating/124_Intan Abelia Sari.py",
    title="124 - Intan Abelia Sari",
    icon=":material/person:",
)

Mahasiswa11 = st.Page(
    "Buku Kating/125_Yosep Winarto Sinulingga.py",
    title="125 - Yosep Winarto Sinulingga",
    icon=":material/person:",
)

Mahasiswa12 = st.Page(
    "Buku Kating/129_Yunika Br Malau.py",
    title="129 - Yunika Br Malau.py",
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

