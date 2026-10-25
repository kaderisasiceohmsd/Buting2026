from io import BytesIO
from PIL import Image, ImageOps
import requests
import streamlit as st
from streamlit_option_menu import option_menu


# Pengamanan pemuatan gambar agar tidak error jika link bermasalah
@st.cache_data
def load_image(url):
  try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
      img = Image.open(BytesIO(response.content))
      img = ImageOps.exif_transpose(img)
      return img
  except Exception:
    pass
  return None


# Pengaturan Tema Global: Background Krim dengan Grafik Pola Modern Dot-Grid & Diagonal
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;900&family=Inter:wght@400;500;600;700&display=swap');

    /* Global Styling - Background Krim dengan Grafik Multi-Layer Bertumpuk */
    .stApp {
        background-color: #fbf9f5;
        background-image: 
            radial-gradient(rgba(181, 142, 75, 0.28) 1.5px, transparent 1.5px), 
            radial-gradient(rgba(92, 64, 51, 0.15) 1.5px, #fbf9f5 1.5px),
            linear-gradient(45deg, rgba(181, 142, 75, 0.05) 25%, transparent 25%),
            linear-gradient(-45deg, rgba(181, 142, 75, 0.05) 25%, transparent 25%);
        background-size: 36px 36px, 36px 36px, 60px 60px, 60px 60px;
        background-position: 0 0, 18px 18px, 0 0, 30px 30px;
        background-attachment: fixed;
        color: #1e1b18;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar disesuaikan warnanya agar senada dan tetap rapi */
    [data-testid="stSidebar"] {
        background-color: #f0e8d5 !important;
        border-right: 2px solid rgba(181, 142, 75, 0.4);
    }
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label {
        color: #1e1b18 !important;
        font-weight: 500;
    }

    /* Judul Utama dengan Grafis Modern Gradient */
    .main-title {
        font-family: 'Outfit', sans-serif;
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #5c4033 0%, #b58e4b 50%, #3d2817 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 4px 20px rgba(181, 142, 75, 0.25);
        margin-bottom: 0px;
    }

    .sub-title {
        font-family: 'Outfit', sans-serif;
        text-align: center;
        font-size: 1.4rem;
        color: #705335;
        letter-spacing: 4px;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<h1 class='main-title'>WEBSITE KATING</h1>", unsafe_allow_html=True
)
st.markdown(
    "<p class='sub-title'>CEO HMSD ADYATAMA ITERA 2026</p>",
    unsafe_allow_html=True,
)

url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
  col1, col2, col3 = st.columns([1, 2, 1])
  with col1:
    st.write("")
  with col2:
    img = load_image(url)
    if img:
      st.image(img, use_container_width=True)
  with col3:
    st.write("")


layout(url)
layout(url1)


def streamlit_menu():
  selected = option_menu(
      menu_title=None,
      options=["Home", "About Us"],
      icons=["house-door", "hand-index"],
      default_index=0,
      orientation="horizontal",
      styles={
          "container": {
              "padding": "6px",
              "background-color": "rgba(240, 232, 213, 0.95)",
              "border": "2px solid #b58e4b",
              "border-radius": "16px",
              "box-shadow": "0 8px 25px rgba(181, 142, 75, 0.25)",
          },
          "icon": {"color": "#8c672b", "font-size": "19px"},
          "nav-link": {
              "font-size": "15px",
              "font-family": "Outfit, sans-serif",
              "text-align": "center",
              "margin": "0px 6px",
              "color": "#2c221e",
              "font-weight": "600",
              "--hover-color": "rgba(181, 142, 75, 0.25)",
          },
          "nav-link-selected": {
              "background": (
                  "linear-gradient(135deg, #b58e4b 0%, #8c672b 100%)"
              ),
              "border": "1px solid #5c4033",
              "color": "#ffffff",
              "font-weight": "700",
              "box-shadow": "0 4px 15px rgba(140, 103, 43, 0.4)",
          },
      },
  )
  return selected


menu = streamlit_menu()

if menu == "Home":

  def home_page():
    st.markdown(
        """
        <style>
        .deskripsi-title {
            text-align: center;
            font-family: 'Outfit', sans-serif;
            font-size: 2.3em;
            color: #4a3324;
            margin-bottom: 25px;
            font-weight: 800;
            text-shadow: 0 2px 10px rgba(181, 142, 75, 0.2);
        }
        
        .photo-caption-box {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.96) 0%, rgba(246, 240, 226, 0.96) 100%);
            backdrop-filter: blur(8px);
            border: 2px solid #b58e4b;
            outline: 2px dashed rgba(181, 142, 75, 0.4);
            outline-offset: -6px;
            color: #1e1b18;
            text-align: center;
            padding: 26px;
            border-radius: 20px;
            margin-bottom: 25px;
            box-shadow: 0 12px 35px rgba(181, 142, 75, 0.2);
            position: relative;
            overflow: hidden;
        }
        .photo-caption-box::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 6px;
            background: linear-gradient(90deg, #5c4033, #b58e4b, #d4af37, #b58e4b, #5c4033);
        }
        
        .badge-cosval {
            display: inline-block;
            background: #f4ebcc;
            border: 1px solid #b58e4b;
            padding: 6px 18px;
            border-radius: 30px;
            font-size: 0.85em;
            margin-bottom: 12px;
            letter-spacing: 2px;
            font-weight: 700;
            color: #5c4033;
            box-shadow: 0 4px 12px rgba(181, 142, 75, 0.2);
        }
        
        .photo-text-title {
            margin: 0;
            font-family: 'Outfit', sans-serif;
            font-size: 1.3em;
            font-weight: 700;
            color: #1e1b18;
        }

        .desc-box {
            border: 2px solid #b58e4b;
            outline: 2px dashed rgba(181, 142, 75, 0.4);
            outline-offset: -6px;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.96) 0%, rgba(248, 244, 234, 0.96) 100%);
            backdrop-filter: blur(8px);
            border-radius: 20px;
            padding: 35px;
            box-shadow: 0 15px 40px rgba(181, 142, 75, 0.18);
            margin-bottom: 30px;
            position: relative;
        }
        
        .desc-heading {
            color: #4a3324;
            font-family: 'Outfit', sans-serif;
            margin-top: 0;
            margin-bottom: 18px;
            font-size: 1.5em;
            font-weight: 800;
        }
        
        .desc-content {
            color: #2c221e;
            font-family: 'Inter', sans-serif;
            line-height: 1.9;
            font-size: 1.1em;
            margin: 0;
            text-align: justify;
            font-weight: 500;
        }

        .book-cover {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.96) 0%, rgba(236, 226, 205, 0.96) 100%);
            backdrop-filter: blur(8px);
            border: 2px solid #8c672b;
            outline: 2px dashed rgba(140, 103, 43, 0.4);
            outline-offset: -6px;
            color: #1e1b18;
            padding: 55px 25px;
            text-align: center;
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(140, 103, 43, 0.25);
            margin-bottom: 20px;
        }
        
        .book-spread {
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(8px);
            border: 2px solid #b58e4b;
            outline: 2px dashed rgba(181, 142, 75, 0.4);
            outline-offset: -6px;
            border-radius: 20px;
            padding: 35px;
            box-shadow: 0 12px 35px rgba(181, 142, 75, 0.2);
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='deskripsi-title'>✦ Deskripsi Kelompok ✦</div>",
        unsafe_allow_html=True,
    )

    foto_kelompok_url = (
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B"
    )
    img_kelompok = load_image(foto_kelompok_url)
    if img_kelompok:
      st.image(img_kelompok, use_container_width=True)

    st.markdown(
        """
        <div class="photo-caption-box">
            <div class="badge-cosval">✦ KELUARGA COSVAL ✦</div>
            <p class="photo-text-title">COSVAL kuat, COSVAL tuntas, Semangat Terus Sampai Tuntas!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="desc-box">
            <h3 class="desc-heading">Selamat datang di portal resmi kelompok Cosval!</h3>
            <p class="desc-content">
                COSVAL adalah kelompok yang mengutamakan kerja sama, semangat, dan tanggung jawab dalam setiap proses belajar. 
                Dengan visi <b>“Cosval Kuat Semangat, Terus Sampai Tuntas,”</b> COSVAL berkomitmen untuk terus belajar, saling membantu, 
                dan tidak mudah menyerah saat menghadapi kesulitan. Bersama-sama, kami berusaha memberikan yang terbaik dan menyelesaikan 
                setiap tantangan sampai tuntas salah satunya penugasan Buku Kating ini. Di sini kami saling berkolaborasi dan berkerja sama satu sama lain, kami berproses bersama, belajar bersama, dan akan menghadapi semuanya bersama-sama.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("---")

    st.markdown(
        "<h2"
        " style='text-align: center; font-family: Outfit; color:"
        " #4a3324; font-weight: 800;'>Album Dokumentasi Cosval</h2>",
        unsafe_allow_html=True,
    )
    st.write("")

    if "album_page" not in st.session_state:
      st.session_state.album_page = 0

    album_photos = [
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
        "https://drive.google.com/uc?export=view&id=1Ut4jNfhkL6GAum5ppq5O5AJ4z_aV7D-B",
    ]

    if st.session_state.album_page == 0:
      st.markdown(
          """
            <div class="book-cover">
                <h1 style="font-family: Outfit; color: #4a3324; font-weight: 800;">ALBUM Kelompok COSVAL</h1>
                <p style="color: #2c221e; font-size: 1.05em; font-weight: 500;">Album kenangan dan dokumentasi kegiatan kelompok kami.</p>
                <p style="color: #8c672b; font-size: 1em; margin-top: 15px; font-weight: 700;">Klik tombol di bawah untuk membuka lembaran buku album.</p>
            </div>
            """,
          unsafe_allow_html=True,
      )
      col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
      with col_btn2:
        if st.button("Buka Album", use_container_width=True):
          st.session_state.album_page = 1
          st.rerun()

    elif st.session_state.album_page == 1:
      st.markdown(
          """
            <div class="book-spread">
                <h4 style='text-align: center; color: #4a3324; margin-top: 0; font-family: Outfit; font-weight: 700;'>— Halaman 1 dari 3 —</h4>
            """,
          unsafe_allow_html=True,
      )
      col1, col2 = st.columns(2)
      with col1:
        img_a0 = load_image(album_photos[0])
        if img_a0:
          st.image(
              img_a0,
              caption="Dokumentasi 1 (Halaman Kiri)",
              use_container_width=True,
          )
      with col2:
        img_a1 = load_image(album_photos[1])
        if img_a1:
          st.image(
              img_a1,
              caption="Dokumentasi 2 (Halaman Kanan)",
              use_container_width=True,
          )
      st.markdown("</div>", unsafe_allow_html=True)

      c1, c2, c3 = st.columns([1, 2, 1])
      with c1:
        if st.button("◀ Tutup Album"):
          st.session_state.album_page = 0
          st.rerun()
      with c3:
        if st.button("Selanjutnya ▶"):
          st.session_state.album_page = 2
          st.rerun()

    elif st.session_state.album_page == 2:
      st.markdown(
          """
            <div class="book-spread">
                <h4 style='text-align: center; color: #4a3324; margin-top: 0; font-family: Outfit; font-weight: 700;'>— Halaman 2 dari 3 —</h4>
            """,
          unsafe_allow_html=True,
      )
      col1, col2 = st.columns(2)
      with col1:
        img_a2 = load_image(album_photos[2])
        if img_a2:
          st.image(
              img_a2,
              caption="Dokumentasi 3 (Halaman Kiri)",
              use_container_width=True,
          )
      with col2:
        img_a3 = load_image(album_photos[3])
        if img_a3:
          st.image(
              img_a3,
              caption="Dokumentasi 4 (Halaman Kanan)",
              use_container_width=True,
          )
      st.markdown("</div>", unsafe_allow_html=True)

      c1, c2, c3 = st.columns([1, 2, 1])
      with c1:
        if st.button("◀ Sebelumnya"):
          st.session_state.album_page = 1
          st.rerun()
      with c3:
        if st.button("Selanjutnya ▶"):
          st.session_state.album_page = 3
          st.rerun()

    elif st.session_state.album_page == 3:
      st.markdown(
          """
            <div class="book-spread">
                <h4 style='text-align: center; color: #4a3324; margin-top: 0; font-family: Outfit; font-weight: 700;'>— Halaman 3 dari 3 (Akhir) —</h4>
            """,
          unsafe_allow_html=True,
      )
      col1, col2 = st.columns(2)
      with col1:
        img_a4 = load_image(album_photos[4])
        if img_a4:
          st.image(
              img_a4,
              caption="Dokumentasi 5 (Halaman Kiri)",
              use_container_width=True,
          )
      with col2:
        img_a5 = load_image(album_photos[5])
        if img_a5:
          st.image(
              img_a5,
              caption="Dokumentasi 6 (Halaman Kanan)",
              use_container_width=True,
          )
      st.markdown("</div>", unsafe_allow_html=True)

      c1, c2, c3 = st.columns([1, 2, 1])
      with c1:
        if st.button("◀ Sebelumnya"):
          st.session_state.album_page = 2
          st.rerun()
      with c3:
        if st.button("🔒 Tutup Album Kembali"):
          st.session_state.album_page = 0
          st.rerun()

  home_page()

elif menu == "About Us":

  def about_page():
    st.markdown(
        """<style>.centered-title {text-align: center; color: #4a3324; font-family:'Outfit', sans-serif; font-weight: 800;}</style>""",
        unsafe_allow_html=True,
    )
    st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .about-photo img {
            border: 4px solid #b58e4b !important;
            outline: 2px solid #5c4033 !important;
            border-radius: 16px !important;
            padding: 4px !important;
            background-color: #ffffff !important;
            box-shadow: 0 10px 25px rgba(181, 142, 75, 0.3) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    filter_pilihan = st.radio(
        "Tampilkan Profil:",
        ["Semua", "Pak Lurah", "Bu Lurah", "Anggota"],
        horizontal=True,
    )

    if filter_pilihan == "Semua":
      st.markdown(
          "<h2 style='text-align: center; margin-top: 20px;"
          " margin-bottom: 20px; color: #4a3324; font-family: \"Outfit\","
          " sans-serif; font-weight: 800;'>Kenalan Yuk Sama Cosval!</h2>",
          unsafe_allow_html=True,
      )

    st.write("")

    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1CkTOku6mtZq-sryae2A1H_dx5moG-R1q",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
    ]

    data_list = [
        {
            "nama": "Herfan Hidayat",
            "sebagai": "Pak Lurah",
            "nim": "125450072",
            "fun_fact": (
                "Suka penasaran akan hal yang baru, yang penting cobain aja"
                " dulu"
            ),
            "motto_hidup": (
                "Dengan bekingan doa ibu, jangankan kalah imbangpun saya"
                " tidak sudi!"
            ),
        },
        {
            "nama": "Ester Friana Sitorus",
            "sebagai": "Bu Lurah",
            "nim": "122450000",
            "fun_fact": "nyemilin es bata",
            "motto_hidup": "Ya apa ya",
        },
        {
            "nama": "Nama Anggota 1",
            "sebagai": "Anggota",
            "nim": "122450083",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 2",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 3",
            "sebagai": "Anggota",
            "nim": "122450100",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 4",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 5",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 6",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 7",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 8",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
        {
            "nama": "Nama Anggota 9",
            "sebagai": "Anggota",
            "nim": "122450000",
            "fun_fact": "Isi fun fact",
            "motto_hidup": "Isi motto hidup",
        },
    ]

    if filter_pilihan == "Semua":
      indices = list(range(11))
    elif filter_pilihan == "Pak Lurah":
      indices = [0]
    elif filter_pilihan == "Bu Lurah":
      indices = [1]
    else:
      indices = list(range(2, 11))

    for idx in indices:
      if idx < len(data_list) and idx < len(gambar_urls):
        img = load_image(gambar_urls[idx])
        data = data_list[idx]

        col_img, col_bio = st.columns([1, 1.4])

        with col_img:
          if img:
            st.image(img, use_container_width=True)

        with col_bio:
          st.markdown(
              f"""
                    <div style="
                        background: linear-gradient(135deg, rgba(255, 255, 255, 0.96) 0%, rgba(246, 240, 226, 0.96) 100%); 
                        backdrop-filter: blur(8px);
                        border: 2px solid #b58e4b; 
                        outline: 2px dashed rgba(181, 142, 75, 0.4);
                        outline-offset: -6px;
                        padding: 26px; 
                        border-radius: 20px; 
                        box-shadow: 0 10px 30px rgba(181, 142, 75, 0.15); 
                        color: #1e1b18;
                        font-family: 'Inter', sans-serif;
                        position: relative;
                        overflow: hidden;
                        margin-bottom: 20px;">
                        <div style="position: absolute; top: 0; right: 0; width: 80px; height: 80px; background: linear-gradient(135deg, transparent 50%, rgba(181,142,75,0.25) 50%); pointer-events: none;"></div>
                        <h3 style="margin-top: 0; color: #4a3324; border-bottom: 2px solid #b58e4b; padding-bottom: 10px; font-family: 'Outfit', sans-serif; font-weight: 800;">{data['nama']}</h3>
                        <p style="margin: 10px 0; font-size: 1.05em; color: #1e1b18; font-weight: 500;"><b>Sebagai:</b> {data['sebagai']}</p>
                        <p style="margin: 10px 0; font-size: 1.05em; color: #1e1b18; font-weight: 500;"><b>NIM:</b> {data['nim']}</p>
                        <p style="margin: 10px 0; font-size: 1.05em; color: #1e1b18; font-weight: 500;"><b>Fun Fact:</b> {data['fun_fact']}</p>
                        <p style="margin: 10px 0; font-size: 1.05em; color: #1e1b18; font-weight: 500;"><b>Motto Hidup:</b> <i>"{data['motto_hidup']}"</i></p>
                    </div>
                    """,
              unsafe_allow_html=True,
          )

        st.write("---")

  about_page()
