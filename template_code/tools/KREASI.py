import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
    /* Mengubah background utama menjadi terang (krem/beige) seperti foto pertama */
    .stApp {
        background-color: #F8F5F2;
        color: #000000; 
    }

    /* Buat header transparan agar tombol sidebar tetap ada */
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    /* Pastikan warna ikon tombol penutup tab menjadi gelap agar terlihat di background terang */
    [data-testid="collapsedControl"] {
        color: #bd411b !important;
    }

    /* Memberikan warna solid pada sidebar (Oranye dari foto kedua) */
    [data-testid="stSidebar"] {
        background-color: #bd411b !important;
    }
    
    /* Memastikan teks di dalam sidebar berwarna putih */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Memaksa elemen teks di dalam tab menjadi gelap karena background sekarang terang */
    [data-testid="stTabs"] button, 
    [data-testid="stTabs"] button * {
        color: #000000 !important;
    }
    
    /* Mengubah warna garis bawah pada tab yang sedang aktif menggunakan aksen oranye */
    [data-testid="stTabs"] [data-baseweb="tab-highlight"] {
        background-color: #bd411b !important;
    }

    /* Animasi gambar */
    .gambar-timbul {
        width: 100%;
        border-radius: 8px;
        transition: transform 0.3s ease, box-shadow 0.3s ease; 
        cursor: pointer;
    }
    .gambar-timbul:hover {
        transform: translateY(-8px) scale(1.03); 
        box-shadow: 0 10px 20px rgba(0,0,0,0.3); 
    }
    </style>
    """,
    unsafe_allow_html=True
)

def greedy_knapsack(items, capacity):
    for item in items:
        item['rasio'] = item['nilai'] / item['berat']
    
    items_sorted = sorted(items, key=lambda x: x['rasio'], reverse=True)
    
    total_nilai = 0
    kapasitas_sisa = capacity
    hasil_pilihan = []
    
    for item in items_sorted:
        if kapasitas_sisa == 0:
            break
            
        # Jika barang muat sepenuhnya
        if item['berat'] <= kapasitas_sisa:
            kapasitas_sisa -= item['berat']
            total_nilai += item['nilai']
            hasil_pilihan.append({
                'Barang': item['nama'],
                'Diambil (kg)': item['berat'],
                'Nilai Didapat ($)': item['nilai'],
                'Status': 'Utuh'
            })
        # Jika barang hanya muat sebagian (Fractional)
        # ... (kode di atasnya tetap sama)
        else:
            nilai_sebagian = item['rasio'] * kapasitas_sisa
            total_nilai += nilai_sebagian
            hasil_pilihan.append({
                'Barang': item['nama'],
                'Diambil (kg)': kapasitas_sisa,
                'Nilai Didapat ($)': round(nilai_sebagian, 2),
                'Status': 'Sebagian'
            })
            kapasitas_sisa = 0
            
    # Tambahkan baris ini untuk mengurutkan hasil berdasarkan 'Nilai Didapat ($)' (Terbesar ke Terkecil)
    hasil_pilihan = sorted(hasil_pilihan, key=lambda x: x['Nilai Didapat ($)'], reverse=True)
            
    return hasil_pilihan, total_nilai

# Antarmuka Website
st.title("💰 Pencuri Kosan (Greedy Knapsack)")
st.write("Anda adalah pencuri yang ingin memaksimalkan nilai barang yang bisa diambil dalam satu kali perjalanan.")

# Input Kapasitas Tas
kapasitas_tas = st.number_input("Kapasitas Tas (kg)", min_value=1, max_value=100, value=20)

# Daftar Barang Tersedia
st.subheader("Daftar Barang di Kamar Kosan:")
daftar_barang = [
    {'nama': 'Sawit', 'berat': 5, 'nilai': 70},
    {'nama': 'Emas Batangan', 'berat': 7.4, 'nilai': 76},
    {'nama': 'Tumbler Tuku', 'berat': 7, 'nilai': 50},
    {'nama': 'Uang', 'berat': 2.71, 'nilai': 40},
    {'nama': 'Geprek', 'berat': 2, 'nilai': 30},
    {'nama': 'Pertalite', 'berat': 1, 'nilai': 10}
]

# Menampilkan Daftar Barang tanpa desimal
df_barang = pd.DataFrame(daftar_barang)
st.table(df_barang.style.format(precision=0)) # precision=0 menghilangkan desimal

if st.button("Mulai Mencuri!!"):
    st.subheader("🕵️ Hasilnya adalahhh:")
    hasil, total = greedy_knapsack(daftar_barang, kapasitas_tas)
    
    if hasil:
        # Menampilkan Tabel Hasil dengan maksimal 2 desimal (agar nilai pecahan seperti 2.71 tetap terlihat)
        # Ubah angka 2 menjadi 0 jika Anda benar-benar tidak ingin ada desimal sama sekali
        df_hasil = pd.DataFrame(hasil)
        st.table(df_hasil.style.format(precision=2))
        
        # Membulatkan Total Nilai tanpa angka di belakang koma (.0f)
        st.success(f"**Total Nilai Jarahan: ${total:.0f}**")
        
        st.info("Yey sudah berhasil mencuri semua barang yang bernilai tinggi! Jangan lupa untuk segera menjual semua barang")
    else:
        st.warning("Tas tidak memiliki kapasitas!")