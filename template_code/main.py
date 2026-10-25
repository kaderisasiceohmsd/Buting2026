import streamlit as st

st.set_page_config(page_title="Buku Kating | Poisson", layout="wide")

# ============================================================
# 🍷 CSS GLOBAL — VINTAGE WINE THEME (MAROON & CREAM)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

/* 1. Background Utama: Kertas Tua (Cream) */
.stApp {
    background-color: #f4f0eb;
    background-image: 
        linear-gradient(rgba(244, 240, 235, 0.95), rgba(244, 240, 235, 0.95)),
        url('https://www.transparenttextures.com/patterns/cream-paper.png');
    background-attachment: fixed;
    font-family: 'Inter', sans-serif;
    color: #222222;
}

/* 2. Sidebar: Maroon Mewah */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #701c23 0%, #4e1318 100%) !important;
    border-right: 1px solid rgba(217, 195, 163, 0.3);
    box-shadow: 4px 0 15px rgba(0,0,0,0.1);
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
    font-family: 'Playfair Display', serif !important;
    letter-spacing: 0.5px;
}

/* 3. Efek Hover di Menu Sidebar */
[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
    transition: all 0.3s ease;
    border-radius: 8px;
    margin: 2px 8px;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
    background: rgba(217, 195, 163, 0.15) !important;
    transform: translateX(4px);
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(217, 195, 163, 0.25) !important;
    border-left: 3px solid #d9c3a3;
}

/* 4. Sembunyikan Menu Bawaan */
#MainMenu { visibility: hidden; }
header { visibility: hidden; }

/* 5. Scrollbar Elegan (Maroon) */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #f4f0eb; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #701c23, #a8323d);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 🧭 NAVIGASI HALAMAN (LENGKAP)
# ============================================================
Homepage = st.Page("Halaman Utama/halaman_utama.py", title="07 - POISSON", default=True)

Mahasiswa1  = st.Page("Buku Kating/116_Yobel Imanuel Pasaribu.py", title="116 - Yobel Imanuel Pasaribu", icon=":material/person:")
Mahasiswa2  = st.Page("Buku Kating/109_Rena Aprilia.py", title="109 - Rena Aprilia", icon=":material/person:")
Mahasiswa3  = st.Page("Buku Kating/020_Fadhilah Adelyia Putri.py", title="020 - Fadhilah Adelyia Putri", icon=":material/person:")
Mahasiswa4  = st.Page("Buku Kating/075_Inness Eymard Gultom.py", title="075 - Inness Eymard Gultom", icon=":material/person:")
Mahasiswa5  = st.Page("Buku K
