import streamlit as st

if 'pindah' not in st.session_state:
    st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py", title="TENSOR", default=True)

Mahasiswa9 = st.Page("Buku Kating/103_Ahmad Fadylah.py", title="103 - Ahmad Fadylah", icon=":material/person:")
Mahasiswa12 = st.Page("Buku Kating/123_Piligo Arga Gayoni.py", title="123 - Piligo Arga Gayoni", icon=":material/person:")
Mahasiswa7 = st.Page("Buku Kating/094_Muhammad Reyza Fasihurahman.py", title="094 - Muhammad Reyza Fasihurahman", icon=":material/person:")
Mahasiswa11 = st.Page("Buku Kating/112_Laikha Salwa Balqis.py", title="112 - Laikha Salwa Balqis", icon=":material/person:")
Mahasiswa1 = st.Page("Buku Kating/001_Hanifa Az'zahra.py", title="001 - Hanifa Az'zahra", icon=":material/person:")
Mahasiswa5 = st.Page("Buku Kating/048_Mario Figo Dito.py", title="048 - Mario Figo Dito", icon=":material/person:")
Mahasiswa6 = st.Page("Buku Kating/060_Kasih Martha Reichella.py", title="060 - Kasih Martha Reichella", icon=":material/person:")
Mahasiswa8 = st.Page("Buku Kating/101_Nadira Alifa Arifin.py", title="101 - Nadira Alifa Arifin", icon=":material/person:")
Mahasiswa3 = st.Page("Buku Kating/010_Lusia Zefanya Sihotang.py", title="010 - Lusia Zefanya Sihotang", icon=":material/person:")
Mahasiswa10 = st.Page("Buku Kating/107_Gisella Salvia Pavita.py", title="107 - Gisella Salvia Pavita", icon=":material/person:")
Mahasiswa4 = st.Page("Buku Kating/022_Enzo Hamman Albarru.py", title="022 - Enzo Hamman Albarru", icon=":material/person:")
Mahasiswa2 = st.Page("Buku Kating/009_Jauza Virna Radyta.py", title="009 - Jauza Virna Radyta", icon=":material/person:")

KREASI = st.Page("tools/KREASI.py", title="Tensor", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="Tebak Angka", icon=":material/search:")

if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12],
            "Kreasi Tensor!!": [KREASI, KREASII]
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 

pg.run()