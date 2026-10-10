import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Nama_Kelompok",
    default=True)

Mahasiswa1 = st.Page(
"Buku Kating/005_Ganis Zahrani Sausan.py",
    title="005 - Ganis Zahrani Sausan",
    icon=":material/person:",
)

Mahasiswa2 = st.Page(
    "Buku Kating/011_Kinaryosih Febrianty.py",
    title="011 - Kinaryosih Febrianty",
    icon=":material/person:",
)

Mahasiswa3 = st.Page(
    "Buku Kating/019_Citra Adita Lestari.py",
    title="019 - Citra Adita Lestari",
    icon=":material/person:",
)

Mahasiswa4 = st.Page(
    "Buku Kating/030_Dendy Noverianto.py",
    title="030 - Dendy Noverianto",
    icon=":material/person:",
)

Mahasiswa5 = st.Page(
    "Buku Kating/043_Ester Friana Sitorus.py",
    title="043 - Ester Friana Sitorus",
    icon=":material/person:",
)

Mahasiswa6 = st.Page(
    "Buku Kating/057_Maria Raphita Huaturuk.py",
    title="057 - Maria Raphita Huaturuk",
    icon=":material/person:",
)

Mahasiswa7 = st.Page(
    "Buku Kating/063_Melania Felicytas Gisella Manurung.py",
    title="063 - Melania Felicytas Gisella Manurung",
    icon=":material/person:",
)

Mahasiswa8 = st.Page(
    "Buku Kating/072_Herfan Hidayat.py",
    title="072 - Herfan Hidayat",
    icon=":material/person:",
)

Mahasiswa9 = st.Page(
    "Buku Kating/100_Faiz Rafli Novandra.py",
    title="100 - Faiz Rafli Novandra",
    icon=":material/person:",
)

Mahasiswa10 = st.Page(
    "Buku Kating/112_Nikisya Nalla Widya Dhana Cahyaningrum.py",
    title="112 - Nikisya Nalla Widya Dhana Cahyaningrum",
    icon=":material/person:",
)

Mahasiswa11 = st.Page(
    "Buku Kating/113_Farel Muhammad Pasha.py",
    title="113 - Farel Muhammad Pasha",
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
                Mahasiswa1,Mahasiswa2,Mahasiswa3,
                Mahasiswa4,Mahasiswa5,Mahasiswa6,
                Mahasiswa7,Mahasiswa8,Mahasiswa9,
                Mahasiswa10,Mahasiswa11],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

