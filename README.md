Berikut Domain Deploy Streamlit masing-masing kelompok:
- https://kelompok-01-jordan.streamlit.app
- https://kelompok-02-jacobi.streamlit.app
- https://kelompok-03-tensor.streamlit.app <=
- https://kelompok-04-anova.streamlit.app
- https://kelompok-05-markov.streamlit.app
- https://kelompok-06-pandas.streamlit.app
- https://kelompok-07-poison.streamlit.app
- https://kelompok-08-cosval.streamlit.app
- https://kelompok-09-bayesian.streamlit.app
- https://kelompok-10-greedy.streamlit.app

# Buku Kating • TENSOR

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Website **Buku Kating** ini dipersembahkan oleh **Kelompok Tensor**, mahasiswa/i Program Studi **Sains Data Institut Teknologi Sumatera (ITERA) Angkatan 2025**. Proyek ini dibuat sebagai bagian dari rangkaian prosesi **CEO HMSD Adyatama ITERA 2026**.

> *"Berpikir Multidimensi, Bergerak Tanpa Batas, TENSOR hadir membawa Kualitas, Kompak dalam Aksi, Kuat dalam Kreasi, TENSOR TENSOR TENSOR Siap Berprestasi !!!"* 

---

## Fitur Utama

- **Profil Kating:** Data kating disusun rapi berdasarkan departemen (Kesekjenan, Baleg, Senator, MIKFES, dll).
- **Profil:** Menampilkan kartu profil lengkap (Nama, NIM, Umur, Asal, Hobi, Sosmed) dengan efek *hover* kaca yang interaktif.
- **Kreasi Tensor (Game & Tools):** Halaman khusus yang memuat kreasi tambahan dari kelompok Tensor.

---

## Tools

- **Bahasa Pemrograman:** Python 3.x
- **Framework Web:** [Streamlit](https://streamlit.io/) (versi 1.36+ disarankan untuk fitur `st.navigation`)
- **Styling:** Custom HTML & CSS
- **Library Tambahan:**
  - `streamlit-option-menu` (Untuk menu horizontal)
  - `Pillow` / `PIL` (Pemrosesan gambar)
  - `requests` (Mengambil gambar dari Google Drive)

---

## Struktur Proyek

```text
📦 buku-kating-tensor
 ┣ 📂 Buku Kating
 ┃ ┣ 📜 001_Hanifa Az'zahra.py
 ┃ ┣ 📜 009_Jauza Virna Radyta.py
 ┃ ┣ 📜 ... (Anggota lainnya)
 ┣ 📂 Halaman Utama
 ┃ ┗ 📜 halaman_utama.py
 ┣ 📂 tools
 ┃ ┣ 📜 ui_helper.py        # Kumpulan fungsi UI dan injeksi CSS
 ┃ ┣ 📜 KREASI.py           # Tools kreasi Tensor
 ┃ ┗ 📜 KREASII.py          # Game Tensor
 ┣ 📜 main.py               # Entry point aplikasi (Routing navigasi)
 ┗ 📜 README.md             # Dokumentasi proyek
```

---

## Cara Instalasi & Menjalankan Proyek

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/username/buku-kating-tensor.git
   cd buku-kating-tensor
   ```

2. **Buat dan aktifkan virtual environment (Opsional namun disarankan):**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instal dependensi yang dibutuhkan:**
   Pastikan Anda menginstal pustaka berikut (atau jalankan `pip install -r requirements.txt` jika ada):
   ```bash
   pip install streamlit streamlit-option-menu pillow requests
   ```

4. **Jalankan aplikasi Streamlit:**
   ```bash
   streamlit run main.py
   ```

5. Buka browser Anda dan akses `http://localhost:8501`.

---

## 👥 Tim Kelompok Tensor (Sains Data ITERA 2025)

1. **Ahmad Fadylah** (Pak Lurah)
2. **Laikha Salwa Balqis** (Bu Lurah)
3. **Hanifa Az'zahra**
4. **Jauza Virna Radyta**
5. **Lusia Zefanya Sihotang**
6. **Enzo Hamman Albarru**
7. **Mario Figo Dito**
8. **Kasih Martha Reichella**
9. **Muhammad Reyza Fasihurahman**
10. **Nadira Alifa Arifin**
11. **Gisella Salvia Pavita**
12. **Piligo Arga Gayoni**

---

## Lisensi & Apresiasi

Dikembangkan dengan sepenuh hati oleh **Kelompok Tensor** untuk **HMSD Adyatama ITERA**.
Terima kasih kepada seluruh kating yang telah berbagi pengalaman dan ceritanya bersama kami!