import streamlit as st

st.set_page_config(page_title="Buku Kating | Poisson", layout="wide")

# ============================================================
# 👑 CSS GLOBAL — ROYAL DYNASTY THEME (MAROON & GOLD)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Playfair+Display:ital,wght@0,600;0,800;1,600&family=Inter:wght@300;400;500;600&display=swap');

/* 1. Background Utama: Beludru Merah & Emas */
.stApp {
    background-color: #1a0a0d;
    background-image: 
        radial-gradient(circle at 50% 0%, rgba(112, 28, 35, 0.4) 0%, transparent 60%),
        radial-gradient(circle at 15% 85%, rgba(212, 175, 55, 0.05) 0%, transparent 40%),
        url('https://www.transparenttextures.com/patterns/black-felt.png'); /* Tekstur kain */
    background-attachment: fixed;
    font-family: 'Inter', sans-serif;
    color: #f4f0eb;
}

/* 2. Font & Warna Judul ala Kerajaan */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Cinzel', serif !important; /* Font khas Romawi/Kerajaan */
    color: #d4af37 !important; /* Warna Emas */
    text-shadow: 0 2px 10px rgba(212, 175, 55, 0.3) !important;
    letter-spacing: 1.5px !important;
}
p, span, div {
    color: #e6ddd1;
}

/* 3. Sidebar: Lorong Istana */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2d0a0d 0%, #1a0a0d 100%) !important;
    border-right: 2px solid #d4af37; /* Garis Emas */
    box-shadow: 5px 0 25px rgba(0, 0, 0, 0.8);
}
[data-testid="stSidebar"] *,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] svg {
    color: #f4f0eb !important;
    fill: #f4f0eb !important;
    font-family: 'Inter', sans-serif !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] strong {
    font-family: 'Cinzel', serif !important;
    letter-spacing: 1px;
    color: #d4af37 !important; /* Emas untuk menu */
}

/* 4. Efek Hover Menu Sidebar (Mahkota) */
[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
    transition: all 0.4s ease;
    border-radius: 5px;
    margin: 2px 8px;
    border: 1px solid transparent;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
    background: rgba(212, 175, 55, 0.15) !important;
    border: 1px solid rgba(212, 175, 55, 0.5);
    transform: translateX(5px);
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(112,28,35,0.9) 0%, transparent 100%) !important;
    border-left: 4px solid #d4af37;
    box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
}

/* 5. Kotak Konten (Seperti Gulungan Perkamen Gelap) */
div[data-testid="stVerticalBlock"] > div {
    background-color: rgba(26, 10, 13, 0.7) !important;
    backdrop-filter: blur(8px);
    border-radius: 8px;
    border: 1px solid rgba(212, 175, 55, 0.3);
    box-shadow: inset 0 0 20px rgba(112, 28, 35, 0.3), 0 8px 32px rgba(0, 0, 0, 0.5);
    padding: 15px;
    margin-bottom: 15px;
}

/* 6. Tombol Emas Kerajaan */
.stButton > button {
    background: linear-gradient(135deg, #d4af37 0%, #b8912e 100%) !important;
    color: #1a0a0d !important;
    font-family: 'Cinzel', serif !important;
    font-weight: 700 !important;
    border: 1px solid #f4f0eb !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #f4f0eb 0%, #d4af37 100%) !important;
    box-shadow: 0 0 20px rgba(212, 175, 55, 0.6) !important;
    transform: translateY(-2px) !important;
}

/* 7. Sembunyikan Menu Bawaan */
#MainMenu { visibility: hidden; }
header { visibility: hidden; }

/* 8. Scrollbar Emas */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #1a0a0d; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #d4af37, #b8912e);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 🧭 NAVIGASI HALAMAN
# ============================================================
Homepage = st.Page("Halaman Utama/halaman_utama.py", title="07 - POISSON", default=True)

Mahasiswa1  = st.Page("Buku Kating/116_Yobel Imanuel Pasaribu.py", title="116 - Yobel Imanuel Pasaribu", icon=":material/person:")
Mahasiswa2  = st.Page("Buku Kating/109_Rena Aprilia.py", title="109 - Rena Aprilia", icon=":material/person:")
Mahasiswa3  = st.Page("Buku Kating/020_Fadhilah Adelyia Putri.py", title="020 - Fadhilah Adelyia Putri", icon=":material/person:")
Mahasiswa4  = st.Page("Buku Kating/075_Inness Eymard Gultom.py", title="075 - Inness Eymard Gultom", icon=":material/person:")
Mahasiswa5  = st.Page("Buku Kating/084_Samuel Kristian.py", title="084 - Samuel Kristian", icon=":material/person:")
Mahasiswa6  = st.Page("Buku Kating/008_Egia Ninta Pepayosa Ketaren.py", title="008 - Egia Ninta Pepayosa Ketaren", icon=":material/person:")
Mahasiswa7  = st.Page("Buku Kating/028_Dzahra Adila Fatma.py", title="028 - Dzahra Adila Fatma", icon=":material/person:")
Mahasiswa8  = st.Page("Buku Kating/018_Achmad Fardhan Al Basri Bandarudin.py", title="018 - Achmad Fardhan Al Basri Bandarudin", icon=":material/person:")
Mahasiswa9  = st.Page("Buku Kating/033_Kayyisah Mazaya.py", title="033 - Kayyisah Mazaya", icon=":material/person:")
Mahasiswa10 = st.Page("Buku Kating/074_Alfajri Anwar.py", title="074 - Alfajri Anwar", icon=":material/person:")
Mahasiswa11 = st.Page("Buku Kating/037_Nailatun Inayah.py", title="037 - Nailatun Inayah", icon=":material/person:")

KREASI  = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

pg = st.navigation({
    "Halaman Utama": [Homepage],
    "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5,
                    Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11],
    "Try Me !!": [KREASI, KREASII],
})

pg.run()
