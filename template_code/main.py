import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia
if 'pindah' not in st.session_state:
    st.session_state.pindah = True

# --- 1. HALAMAN UTAMA ---
Homepage = st.Page("Halaman Utama/halaman_utama.py", title="TENSOR", default=True)

# --- 2. BUKU KATING (DAFTAR ANGGOTA) ---
Anggota1 = st.Page("Buku Kating/103_Ahmad Fadylah.py", title="103 - Ahmad Fadylah", icon=":material/person:")
Anggota4 = st.Page("Buku Kating/123_Piligo Arga Gayoni.py", title="123 - Piligo Arga Gayoni", icon=":material/person:")
Anggota3 = st.Page("Buku Kating/094_Muhammad Reyza Fasihurahman.py", title="094 - Muhammad Reyza Fasihurahman", icon=":material/person:")
Anggota2 = st.Page("Buku Kating/112_Laikha Salwa Balqis.py", title="112 - Laikha Salwa Balqis", icon=":material/person:")
Anggota5 = st.Page("Buku Kating/001_Hanifa Az'zahra.py", title="001 - Hanifa Az'zahra", icon=":material/person:")
Anggota6 = st.Page("Buku Kating/048_Mario Figo Dito.py", title="048 - Mario Figo Dito", icon=":material/person:")
Anggota7 = st.Page("Buku Kating/060_Kasih Martha Reichella.py", title="060 - Kasih Martha Reichella", icon=":material/person:")
Anggota8 = st.Page("Buku Kating/101_Nadira Alifa Arifin.py", title="101 - Nadira Alifa Arifin", icon=":material/person:")
Anggota9 = st.Page("Buku Kating/010_Lusia Zefanya Sihotang.py", title="010 - Lusia Zefanya Sihotang", icon=":material/person:")
Anggota10 = st.Page("Buku Kating/107_Gisella Salvia Pavita.py", title="107 - Gisella Salvia Pavita", icon=":material/person:")
Anggota11 = st.Page("Buku Kating/022_Enzo Hamman Albarru.py", title="022 - Enzo Hamman Albarru", icon=":material/person:")
Anggota12 = st.Page("Buku Kating/009_Jauza Virna Radyta.py", title="009 - Jauza Virna Radyta", icon=":material/person:")
# (Tambahkan teman-temanmu di sini nanti jika file .py mereka sudah ada di folder Buku Kating)

# --- 3. KREASI ---
KREASI = st.Page("tools/KREASI.py", title="Tensor", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="Tebak Angka", icon=":material/search:")

# --- PENGATURAN SIDEBAR OTOMATIS ---
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Anggota1, Anggota2, Anggota3, Anggota4, Anggota5, Anggota6, Anggota7, Anggota8, Anggota9, Anggota10, Anggota11, Anggota12],
            "Kreasi Tensor!!": [KREASI, KREASII]
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 

pg.run()