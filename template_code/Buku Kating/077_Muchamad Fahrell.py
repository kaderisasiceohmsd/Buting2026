import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import base64

st.set_page_config(layout="wide")

st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F8F5F2;
        color: #000000; 
    }

    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    [data-testid="collapsedControl"] {
        color: #bd411b !important;
    }

    [data-testid="stSidebar"] {
        background-color: #bd411b !important;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    [data-testid="stTabs"] button, 
    [data-testid="stTabs"] button * {
        color: #000000 !important;
    }
    
    [data-testid="stTabs"] [data-baseweb="tab-highlight"] {
        background-color: #bd411b !important;
    }

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
# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Badan Legislatif",
            "Badan Kesenatoran",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
            "Departemen Minbak",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "10px !important", 
                "background-color": "#c84b22", 
                "border": "none !important", 
                "border-radius": "0 !important", 
                "box-shadow": "none !important" 
            },
            "icon": {
                "color": "white", 
                "font-size": "19px"
            },
            "nav-link": {
                "font-size": "14px",
                "text-align": "center",
                "margin": "5px", 
                "color": "white",
                "background-color": "transparent", 
                "--hover-color": "rgba(255, 255, 255, 0.1)",
            },
            "nav-link-selected": {
                "background-color": "#8c3010", 
                "color": "white",
                "border-radius": "10px" 
            },
            },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
     
@st.cache_data
@st.cache_data
@st.cache_data
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    from PIL import Image, ImageDraw
    from io import BytesIO
    import base64

    images = []

    def buat_foto_default():
        img = Image.new("RGB", (400, 400), "#E8EDF3")
        draw = ImageDraw.Draw(img)
        draw.ellipse((125, 65, 275, 215), fill="#9CA3AF")
        draw.ellipse((75, 200, 325, 470), fill="#9CA3AF")
        return img

    for i in range(len(data_list)):
        url = gambar_urls[i] if i < len(gambar_urls) else ""

        if url:
            with st.spinner(f"Memuat gambar {i + 1} dari {len(data_list)}"):
                img = load_image(url)
        else:
            img = None

        if img is None:
            img = buat_foto_default()

        images.append(img)

    def img_to_base64(img):
        import base64
        from io import BytesIO
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

    st.markdown("""
    <style>
    .kartu-profil {
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }
    .kartu-profil:hover {
        transform: translateY(-8px) !important;
        box-shadow: 0 15px 25px rgba(0,0,0,0.2) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    for i in range(0, len(images), 2):
        cols = st.columns(2)
        
        for j in range(2):
            index = i + j
            if index < len(images):
                with cols[j]:
                    img_b64 = img_to_base64(images[index])
                    data = data_list[index] if index < len(data_list) else {}
                    
                    nama = data.get('nama', '-')
                    nim = data.get('nim', '-')
                    umur = data.get('umur', '-')
                    asal = data.get('asal', '-')
                    alamat = data.get('alamat', '-')
                    hobbi = data.get('hobbi', '-')
                    sosmed = data.get('sosmed', '-')
                    kesan = data.get('kesan', '-')
                    pesan = data.get('pesan', '-')

                    card_html = f"""<div class="kartu-profil" style="display: flex; flex-direction: row; background-color: #ffffff; border-radius: 16px; box-shadow: 0 6px 12px rgba(0,0,0,0.08); overflow: hidden; margin-bottom: 20px; height: 360px;">
<div style="flex: 0 0 45%;">
<img src="data:image/png;base64,{img_b64}" style="width: 100%; height: 100%; object-fit: cover; display: block;">
</div>
<div style="flex: 1; padding: 18px; display: flex; flex-direction: column; justify-content: space-between;">
<div>
<h4 style="margin: 0 0 4px 0; color: #1e1e1e; font-size: 18px; line-height: 1.2;">{nama}</h4>
<p style="margin: 0 0 12px 0; color: #666; font-size: 14px; font-weight: bold;">{nim}</p>
<div style="font-size: 13px; color: #444; line-height: 1.5;">
<b>Umur:</b> {umur}<br>
<b>Asal:</b> {asal}<br>
<b>Alamat:</b> {alamat}<br>
<b>Hobbi:</b> {hobbi}<br>
<b>Sosmed:</b> {sosmed}
</div>
</div>
<div style="background-color: #FFF3E0; padding: 12px; border-radius: 8px; margin-top: 12px;">
<p style="margin: 0 0 4px 0; font-size: 12px; font-style: italic; color: #bd411b;"><b>Kesan:</b> "{kesan}"</p>
<p style="margin: 0; font-size: 12px; font-style: italic; color: #bd411b;"><b>Pesan:</b> "{pesan}"</p>
</div>
</div>
</div>"""
                    
                    st.markdown(card_html, unsafe_allow_html=True)
menu = streamlit_menu()

# BAGIAN MENU KESEKJENAN
if menu == "Kesekjenan":
    def kesekjenan():
        st.markdown(
            "<h3 style='text-align: center;'>Kesekjenan</h3>",
            unsafe_allow_html=True
        )

        tab1, tab2, tab3, tab4 = st.tabs([
            "Ketua Himpunan",
            "Sekretaris Jenderal",
            "Sekretaris",
            "Bendahara"
        ])

        # ==========================================
        # KETUA HIMPUNAN
        # ==========================================
        with tab1:
            gambar_urls_Ketua = [
                "https://drive.google.com/uc?export=view&id=1lMm2cZotf4Zg5npQZTNsGulE71uamr0G"
            ]

            data_list_Ketua = [
                {
                    "nama": "Ginda Fajar Riadi Marpaung",
                    "nim": "123450103",
                    "umur": "22",
                    "asal": "Batam",
                    "alamat": "Sekretariat HMSD",
                    "hobbi": "Push Rank sampe IMO",
                    "sosmed": "@gars_mrp",
                    "jabatan": "Ketua Himpunan",
                    "kesan": "Orangnya punya jiwa pemimpin dan bisa jadi panutan.",
                    "pesan": "Semangat terus bang, semoga semua rencananya lancar ke depannya!"
                }
            ]

            display_images_with_data(
                gambar_urls_Ketua,
                data_list_Ketua
            )

        with tab2:
            gambar_urls_Sekjen = [
                "https://drive.google.com/uc?export=view&id=1L1mV6NSK_dwiOB1dMLtHXVss8YvviGF7"
            ]

            data_list_Sekjen = [
                {
                    "nama": "Muhammad Aqil Ramadhan",
                    "nim": "123450046",
                    "umur": "22",
                    "asal": "Bangkinang",
                    "alamat": "Sekretariat HMSD",
                    "hobbi": "Dzikir",
                    "sosmed": "@muhammadaqil1111",
                    "jabatan": "Sekretaris Jenderal",
                    "kesan": "Orangnya bijak dan punya cara pandang yang menarik.",
                    "pesan": "Semangat terus bang, jangan lupa istirahat di tengah kesibukannya. Semoga semua urusannya lancar!"
                    
                }
            ]

            display_images_with_data(
                gambar_urls_Sekjen,
                data_list_Sekjen
            )

        with tab3:
            gambar_urls_Sekretaris = [
                "https://drive.google.com/uc?export=view&id=1arEBvurK397f3EPs4YmXihuHpY_0Ngnk",
                "https://drive.google.com/uc?export=view&id=1Iv7PgxUJ9qVu-8EuqH73CJZ0ZATL3irL"
            ]

            data_list_Sekretaris = [
                {
                    "nama": "Efi Defiyati",
                    "nim": "123450005",
                    "umur": "21",
                    "asal": "Lamtim",
                    "alamat": "Airan",
                    "hobbi": "Membaca",
                    "sosmed": "@eeffifi",
                    "jabatan": "Sekretaris",
                    "kesan": "Orangnya kalem dan enak diajak ngobrol.",
                    "pesan": "Semangat terus kaa, semoga kuliah dan semua urusannya lancar!"
                },
                {
                    "nama": "Qois Olifio",
                    "nim": "123450067",
                    "umur": "22",
                    "asal": "Batam",
                    "alamat": "Kotabaru",
                    "hobbi": "Mainin surat",
                    "sosmed": "@qoidalfio_",
                    "jabatan": "Sekretaris",
                    "kesan": "Orangnya asik dan punya semangat yang keren.",
                    "pesan": "Semangat terus bang, semoga ke depannya makin banyak hal baik yang datang!"
                }
            ]

            display_images_with_data(
                gambar_urls_Sekretaris,
                data_list_Sekretaris
            )

        with tab4:
            gambar_urls_Bendahara = [
                "https://drive.google.com/uc?export=view&id=1Iwen8hJLSVc5_-C7sEAhlDoByhm82chK",
                "https://drive.google.com/uc?export=view&id=16feqaSynGDSLmG6TwVb8uUt8V9ylEypi"
            ]

            data_list_Bendahara = [
                {
                    "nama": "Hafsa Fazila Arradhi",
                    "nim": "123450079",
                    "umur": "21",
                    "asal": "Balam",
                    "alamat": "Balam",
                    "hobbi": "Berenang",
                    "sosmed": "@hafsafadhilaa",
                    "jabatan": "Bendahara",
                    "kesan": "Orangnya baik dan menyenangkan.",
                    "pesan": "Semangat terus kaa, semoga kuliahnya lancar dan semua targetnya tercapai!"
                },
                {
                    "nama": "Luthfia Laila Ramadhani",
                    "nim": "123450004",
                    "umur": "20",
                    "asal": "Bengkulu",
                    "alamat": "Airan",
                    "hobbi": "Bertemu Pak tirta",
                    "sosmed": "@hluthfiaarmdhni",
                    "jabatan": "Bendahara",
                    "kesan": "Orangnya seru dan punya pembawaan yang khas.",
                    "pesan": "Semangat terus kaa, semoga semua urusannya lancar dan sukses selalu!"
                }
                ] 

            display_images_with_data(
                gambar_urls_Bendahara,
                data_list_Bendahara
            )


    kesekjenan()


# BAGIAN MENU BALEG
elif menu == "Badan Legislatif":
    def Badan_Legislatif():
        st.markdown(
            "<h3 style='text-align: center;'>Badan Legislatif</h3>",
            unsafe_allow_html=True
        )

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "Ketua Baleg",
            "Sekretaris",
            "Komisi I Legislasi",
            "Komisi II Pengawasan",
            "Komisi III Aspirasi dan Media Informasi"
        ])

        with tab1:
            gambar_urls_Ketua = [
                "https://drive.google.com/uc?export=view&id=1GEVx0r0hwY_jXQP3pD4X-uwE0DMZebcI"
            ]

            data_list_Ketua = [
                {
                    "nama": "Ridho Benedictus Togi Manik",
                    "nim": "123450060",
                    "umur": "20",
                    "asal": "Kota Manchester",
                    "alamat": "GH",
                    "hobbi": "Wawancara",
                    "sosmed": "@iamridhomanik",
                    "jabatan": "Ketua Baleg",
                    "kesan": "Orangnya punya pembawaan yang percaya diri dan cocok jadi pemimpin.",
                    "pesan": "Semangat terus bang, semoga Baleg makin maju dan semua rencananya berjalan lancar!"
                }
            ]

            display_images_with_data(
                gambar_urls_Ketua,
                data_list_Ketua
            )

        # ==========================================
        # SEKRETARIS
        # ==========================================
        with tab2:
            gambar_urls_Sekretaris = [
                "https://drive.google.com/uc?export=view&id=1fUMJq1YXVoroSqWkLIL1wXO73H1eEvDJ"
            ]

            data_list_Sekretaris = [
                {
                    "nama": "Juesi Apridelia Saragih",
                    "nim": "123450085",
                    "umur": "19",
                    "asal": "Singkawang",
                    "alamat": "Pelangi",
                    "hobbi": "Dengerin lagu semusim dari marsel",
                    "sosmed": "@j__eesie",
                    "jabatan": "Sekretaris",
                    "kesan": "Orangnya punya selera musik yang menarik dan pembawaannya asik.",
                    "pesan": "Semangat terus kaa, semoga semua urusannya lancar dan jangan lupa nikmati prosesnya!"
                }
            ]

            display_images_with_data(
                gambar_urls_Sekretaris,
                data_list_Sekretaris
            )

        # ==========================================
        # KOMISI I LEGISLASI
        # ==========================================
        with tab3:
            gambar_urls_Komisi_I = [
                "https://drive.google.com/uc?export=view&id=1Qabc-2O6m8ku8oPNsJSFQToiJh6rekMP",
                "https://drive.google.com/uc?export=view&id=1eJxqhSlWd-vGqvsvbc9KPLPVMHCOK6Fp",
                "https://drive.google.com/uc?export=view&id=173RgfXc3ezh7t14WsWPd49Eddybzjzx0"
            ]

            data_list_Komisi_I = [
                {
                    "nama": "Dharu Cahyoaji Sasongko",
                    "nim": "123450023",
                    "umur": "19",
                    "asal": "Lampung",
                    "alamat": "Bandar Lampung",
                    "hobbi": "Ngidupin api baleg di tiktok",
                    "sosmed": "@exvoltas",
                    "jabatan": "Kepala Komisi",
                    "kesan": "Orangnya punya jiwa yang aktif dan suka bikin suasana jadi rame.",
                    "pesan": "Semangat terus bang, semoga makin sukses dan cita-cita jadi orang kayanya tercapai!"
                },
                {
                    "nama": "Gh. Mikael Niko Antoni Setiadi",
                    "nim": "124450025",
                    "umur": "20",
                    "asal": "Jabung",
                    "alamat": "Jati Agung",
                    "hobbi": "COD Musang",
                    "sosmed": "@me._kael",
                    "jabatan": "Staff Komisi",
                    "kesan": "Orangnya punya hobi yang unik dan kelihatannya suka mencoba hal baru.",
                    "pesan": "Semangat terus bang, semoga setiap pengalaman bisa jadi pelajaran yang berguna ke depannya!"
                },
                {
                    "nama": "Siti Sarifah Sumamah",
                    "nim": "124450015",
                    "umur": "19",
                    "asal": "Bekasi",
                    "alamat": "Kedaton",
                    "hobbi": "Mancing",
                    "sosmed": "@syt.rifa",
                    "jabatan": "Staff Komisi",
                    "kesan": "Orangnya punya hobi yang seru dan kelihatannya sabar.",
                    "pesan": "Semangat terus kaa, jangan lupa bangga sama diri sendiri dan semua hal yang udah berhasil dilewati!"
                }
            ]

            display_images_with_data(
                gambar_urls_Komisi_I,
                data_list_Komisi_I
            )

        # ==========================================
        # KOMISI II PENGAWASAN
        # ==========================================
        with tab4:
            gambar_urls_Komisi_II = [
                "https://drive.google.com/uc?export=view&id=1lpeaME0D5oCgx78rV3HNcAOdsu1p1dXs",
                "https://drive.google.com/uc?export=view&id=1p4Rk4TqyvpxkE5RrXRIzg6fWGzOsQ0qj",
                "https://drive.google.com/uc?export=view&id=1hPqAx0Th8801yxRCCmmuQ_40z1lBZbBw",
                "https://drive.google.com/uc?export=view&id=17hJfFqdJ0J9e2fvMAH-I54-nD0WZJ9fF"
            ]

            data_list_Komisi_II = [
                {
                    "nama": "Givaro Ananta",
                    "nim": "123450078",
                    "umur": "19",
                    "asal": "Lampung Barat",
                    "alamat": "Sukabumi",
                    "hobbi": "Minum Kopi",
                    "sosmed": "@givarooo",
                    "jabatan": "Kepala Komisi",
                    "kesan": "Orangnya keliahatnya santai dan asik.",
                    "pesan": "Semangat terus bang, semoga semua yang terasa sulit bisa dilewati dan semua rencananya lancar!"
                },
                {
                    "nama": "Afghanis Nursholehatunnisa",
                    "nim": "124450042",
                    "umur": "19",
                    "asal": "Kepulauan Mentawai",
                    "alamat": "Owen Kost",
                    "hobbi": "Ngoding",
                    "sosmed": "@afghanisnt_",
                    "jabatan": "Staff Komisi",
                    "kesan": "Orangnya suka belajar hal baru dan punya minat di dunia coding.",
                    "pesan": "Semangat terus kaa ngodingnya, semoga semua target dan impiannya bisa tercapai!"
                },
                {
                    "nama": "Hani Qurrota Aini",
                    "nim": "124450020",
                    "umur": "20",
                    "asal": "CTR",
                    "alamat": "Sukarame",
                    "hobbi": "Baca AU",
                    "sosmed": "@haniquratuain_",
                    "jabatan": "Staff Komisi",
                    "kesan": "Orangnya punya hobi baca yang seru dan imajinasi yang luas.",
                    "pesan": "Semangat terus kaa, semoga selalu ketemu cerita dan pengalaman yang bikin senang!"
                },
                {
                    "nama": "Jeremia Halim",
                    "nim": "124450101",
                    "umur": "20",
                    "asal": "Tanggerang",
                    "alamat": "Teluk",
                    "hobbi": "Nyanyi, olahraga",
                    "sosmed": "@jeremia_hm",
                    "jabatan": "Staff Komisi",
                    "kesan": "Orangnya punya banyak kegiatan seru, dari olahraga sampai nyanyi.",
                    "pesan": "Semangat terus bang, lakukan yang terbaik dan semoga semua urusannya dimudahkan!"
                }
            ]

            display_images_with_data(
                gambar_urls_Komisi_II,
                data_list_Komisi_II
            )

        # ==========================================
        # KOMISI III ASPIRASI DAN MEDIA INFORMASI
        # ==========================================
        with tab5:


            gambar_urls_Komisi_III = [
                "https://drive.google.com/uc?export=view&id=112PQJYl9BJ8q5ORQYnSRGyH8n9l32F8E",
                "https://drive.google.com/uc?export=view&id=1NkMl76Maz1x0FhMtcM1IBmT2SrfIroUj",
                "https://drive.google.com/uc?export=view&id=1w1Pfz_aCH3SSyhmhkDnHJw02PurUwtoH"
            ]

            data_list_Komisi_III = [
                {
            "nama": "Monica Patricia Tanjung",
            "nim": "123450073",
            "umur": "21",
            "asal": "Jakarta Barat",
            "alamat": "Kotabaru",
            "hobbi": "Lari",
            "sosmed": "@monica_tjg",
            "kesan": "Lucu, gemas, tapi tegas",  
            "pesan":"Semangat kaa kuliah dan organisasinyaaa, dan semoga diberikan kemudahan dan kelancaran dalam mengerjakan TA nya, aamiin!"# 1
            },
                {
                    "nama": "Jona Timothy Ogatse Panjaitan",
                    "nim": "124450111",
                    "umur": "20",
                    "asal": "Depok",
                    "alamat": "Pemda Raya",
                    "hobbi": "Gym sama Koleksi figure, nafas manual",
                    "sosmed": "@nagatseee",
                    "jabatan": "Staff Komisi",
                    "kesan": "Orangnya punya hobi yang unik, apalagi koleksi figurenya.",
                    "pesan": "Semangat terus bang, semoga makin konsisten sama hobinya dan semua targetnya tercapai!"
                },
                {
                    "nama": "Sekar Dini Widya Putri",
                    "nim": "124450082",
                    "umur": "20",
                    "asal": "Metro",
                    "alamat": "Pemda",
                    "hobbi": "Jajan sama nisa, putri, suci",
                    "sosmed": "@sekardnwp",
                    "jabatan": "Staff Komisi",
                    "kesan": "Orangnya suka menikmati waktu bareng teman-temannya.",
                    "pesan": "Semangat terus kaa, semoga selalu punya banyak momen seru bareng teman-teman dan kuliahnya lancar!"
                },
                {
                    "nama": "Wan Nashwa Alhasni Yuska",
                    "nim": "123450077",
                    "umur": "20",
                    "asal": "Pasay",
                    "alamat": "Belwis",
                    "hobbi": "Nyapa angin",
                    "sosmed": "@nshaysk",
                    "jabatan": "Staff Komisi",
                    "kesan": "Orangnya punya cara sendiri buat menikmati suasana.",
                    "pesan": "Semangat terus kaa, semoga hari-harinya menyenangkan dan semua urusannya lancar!"
                }
            ]

            display_images_with_data(
                gambar_urls_Komisi_III,
                data_list_Komisi_III
            )

    Badan_Legislatif()





elif menu == "Departemen Minbak":
    def Departemen_Minbak():
        st.markdown(
            "<h3 style='text-align: center;'>Departemen Minbak</h3>",
            unsafe_allow_html=True
        )

        tab1, tab2, tab3, tab4 = st.tabs([
            "Ketua Departemen",
            "Sekretaris",
            "Manajemen Aktivitas dan Kompetisi",
            "Manajemen Minat dan Bakat"
        ])

        # ==========================================
        # KETUA DEPARTEMEN
        # ==========================================
        with tab1:
            gambar_urls_Ketua = [
                "https://drive.google.com/uc?export=view&id=1Udk2xpvnZx6fPqH0f9wwTJN980Bz1TkV"
            ]

            data_list_Ketua = [
                {
                    "nama": "Kevin Antonio Junior",
                    "nim": "123450109",
                    "umur": "23",
                    "asal": "Sulawesi Tengah",
                    "alamat": "Panjang",
                    "hobbi": "Mancing",
                    "sosmed": "@kevinaja__",
                    "jabatan": "Kepala Departemen",
                    "kesan": "Orangnya asik dan seru diajak ngobrol.",
                    "pesan": "Semangat terus bang, semoga Minbak makin kompak dan semua kegiatannya lancar!"
                }
            ]

            display_images_with_data(
                gambar_urls_Ketua,
                data_list_Ketua
            )

        # ==========================================
        # SEKRETARIS
        # ==========================================
        with tab2:
            gambar_urls_Sekretaris = [
                "https://drive.google.com/uc?export=view&id=15Yw6OAHvR23TlQWly2hcYUanBIOinm8K"
            ]

            data_list_Sekretaris = [
                {
                    "nama": "Gusti Putu Ferazka Dhiyamika",
                    "nim": "123450046",
                    "umur": "21",
                    "asal": "Bekasi",
                    "alamat": "Way Dadi",
                    "hobbi": "Mendaki",
                    "sosmed": "@ferazkaa",
                    "jabatan": "Sekretaris",
                    "kesan": "Orangnya santai dan enak diajak ngobrol.",
                    "pesan": "Semangat terus kaa, semoga kuliah dan semua kegiatannya lancar!"
                }
            ]

            display_images_with_data(
                gambar_urls_Sekretaris,
                data_list_Sekretaris
            )

        # ==========================================
        # MANAJEMEN AKTIVITAS DAN KOMPETISI
        # ==========================================
        with tab3:
            gambar_urls_MAK = [
                "https://drive.google.com/uc?export=view&id=1LAJkUbx8KooEozXE57nFs0fWwWtw2aIP",
                "https://drive.google.com/uc?export=view&id=1ycj9bzqvPwFxuGZBljR6lo3qUM8UVrib",
                "https://drive.google.com/uc?export=view&id=1bmq4huEEg36soPANR5uIcqpw-PPk38x2",
                "https://drive.google.com/uc?export=view&id=10dndlb7oI4Iu3gjolRIzTLtk5cAeTpQF",
                "https://drive.google.com/uc?export=view&id=17KZMQOw0MuSyUy28i0J71aVIFCwrPtNf",
                "https://drive.google.com/uc?export=view&id=1CadH0SDhfRZiE9V3cehnGvRk7UDupoYm"
            ]

            data_list_MAK = [
                {
                    "nama": "Ali Aristo Muthahhari Parisi",
                    "nim": "123450088",
                    "umur": "21",
                    "asal": "Lampung Timur",
                    "alamat": "Gang Sakum Belwis",
                    "hobbi": "Nonton F1",
                    "sosmed": "@ali_parisi3",
                    "jabatan": "Kepala Divisi",
                    "kesan": "Orangnya asik dan punya hobi yang menarik.",
                    "pesan": "Semangat terus bang, semoga semua rencana dan kegiatannya berjalan lancar!"
                },
                {
                    "nama": "Ayu Andriani Parlina Wati",
                    "nim": "124450058",
                    "umur": "20",
                    "asal": "Lampung Barat",
                    "alamat": "Airan",
                    "hobbi": "Belajar + menghitung uang",
                    "sosmed": "@aayuandriani_",
                    "jabatan": "Anggota",
                    "kesan": "Hobinya unik juga, belajar sambil menghitung uang.",
                    "pesan": "Semangat terus kaa, semoga makin banyak hal baik yang datang!"
                },
                {
                    "nama": "Dafa Elpriza",
                    "nim": "124450131",
                    "umur": "21",
                    "asal": "Bekasi",
                    "alamat": "Way Kandis",
                    "hobbi": "Jogging",
                    "sosmed": "@dafaelpriza_",
                    "jabatan": "Anggota",
                    "kesan": "Hobinya jogging, cocok buat mengisi waktu luang.",
                    "pesan": "Semoga selalu sehat, kuliahnya lancar, dan tetap semangat!"
                },
                {
                    "nama": "Juwita Sari",
                    "nim": "124450066",
                    "umur": "19",
                    "asal": "Lampung Barat",
                    "alamat": "Pemda",
                    "hobbi": "Mancing",
                    "sosmed": "@ju.juwitaaa_",
                    "jabatan": "Anggota",
                    "kesan": "Sama-sama suka mancing, hobinya seru juga.",
                    "pesan": "Semoga makin banyak pengalaman seru dan jangan takut mencoba hal baru!"
                },
                {
                    "nama": "Muhammad Afdal Luthfi",
                    "nim": "124450047",
                    "umur": "19",
                    "asal": "Lampung Tengah",
                    "alamat": "Jl. Pulau Damar",
                    "hobbi": "Memantau dl tugas",
                    "sosmed": "@afdall.03",
                    "jabatan": "Anggota",
                    "kesan": "Kelihatannya cukup perhatian sama tugas-tugasnya.",
                    "pesan": "Semangat terus bang, semoga tugas kuliah dan kegiatan lainnya lancar!"
                },
                {
                    "nama": "Salsabila Nazwa Putri",
                    "nim": "124450002",
                    "umur": "20",
                    "asal": "Metro",
                    "alamat": "Korpri",
                    "hobbi": "Nongkrong di kopken",
                    "sosmed": "@slbnzw_",
                    "jabatan": "Anggota",
                    "kesan": "Suka nongkrong, cocok buat menghabiskan waktu bareng teman.",
                    "pesan": "Semoga selalu punya waktu buat senang-senang di tengah kesibukan, sukses terus kaa!"
                }
            ]

            display_images_with_data(
                gambar_urls_MAK,
                data_list_MAK
            )

        # ==========================================
        # MANAJEMEN MINAT DAN BAKAT
        # ==========================================
        with tab4:
            gambar_urls_MMB = [
                "https://drive.google.com/uc?export=view&id=1BUjU9oqJxp17o_Rn-Wg-QGqDnkfIZvyX",
                "https://drive.google.com/uc?export=view&id=1Ic-k9SPonBkbgOwesBrmyK__ne-o-rvv",
                "https://drive.google.com/uc?export=view&id=1Yruir4LTmRioWy3eogCH8peS6sw14xg2",
                "https://drive.google.com/uc?export=view&id=1l6WFa-Obnwn1x7t9BQf3L7cAFL9iPss5",
                "https://drive.google.com/uc?export=view&id=13yIUWXRoArqanTVyR5a4I_jGqslJ8J0o",
                "https://drive.google.com/uc?export=view&id=13yIUWXRoArqanTVyR5a4I_jGqslJ8J0o",
                "https://drive.google.com/uc?export=view&id=1cMHzTwL_osj4CvaWdPCSfrrpTdqQKAoJ"
            ]

            data_list_MMB = [
                {
                    "nama": "Muhammad Ridwan",
                    "nim": "123450091",
                    "umur": "21",
                    "asal": "Lampung Tengah",
                    "alamat": "Belwis",
                    "hobbi": "Badminton",
                    "sosmed": "@mridwaan_22",
                    "jabatan": "Kepala Divisi",
                    "kesan": "Hobinya badminton, seru juga buat olahraga bareng.",
                    "pesan": "Semangat terus bang, semoga makin jago badminton dan sukses terus!"
                },
{
    "nama": "Andra Ilham Bintang",
    "nim": "124450060",
    "umur": "18",
    "asal": "Sumatera Selatan",
    "alamat": "Kotabaru",
    "hobbi": "Main rubik",
    "sosmed": "@andra.lhm",
    "jabatan": "Anggota",
"kesan": "Bang Adra adalah sosok mentor yang kehadirannya bukan sekadar memberi arahan, tetapi juga meninggalkan pelajaran yang akan selalu saya ingat. Ada ilmu yang mungkin terlupa seiring waktu, tetapi ada pula kebaikan yang akan tetap hidup dalam ingatan.",
"pesan": "Terima kasih telah menjadi bagian dari perjalanan saya, Bang. Semoga dunia selalu memberi ruang bagi setiap kebaikan yang Bang Adra tanamkan. Ke mana pun langkah membawa Bang Adra kelak, semoga ilmu yang dibagikan menjadi amal yang tak terputus, dan segala lelah dalam membimbing orang lain berbalas kebahagiaan yang tak terhingga."},
                {
                    "nama": "Bryan Paskah Telaumbanua",
                    "nim": "124450003",
                    "umur": "20",
                    "asal": "Nias",
                    "alamat": "Belwis",
                    "hobbi": "Live tiktok",
                    "sosmed": "@bryantel_",
                    "jabatan": "Anggota",
                    "kesan": "Hobinya live TikTok, lumayan buat mengisi waktu luang.",
                    "pesan": "Semoga makin lancar semua kegiatannya dan sukses terus ke depannya!"
                },
                {
                    "nama": "Ghiyats Thabularasa Meardhy",
                    "nim": "124450067",
                    "umur": "17",
                    "asal": "Surabaya",
                    "alamat": "Kemiling",
                    "hobbi": "Nanem Sawit",
                    "sosmed": "@meardhy_ghiyats",
                    "jabatan": "Anggota",
                    "kesan": "Hobinya nanam sawit, cukup unik dibanding yang lain.",
                    "pesan": "Semoga selalu semangat menjalani kuliah dan semua kegiatannya!"
                },
                {
                    "nama": "Indah Julia Mawar Pratiwi",
                    "nim": "124450055",
                    "umur": "20",
                    "asal": "Pringsewu",
                    "alamat": "Airan",
                    "hobbi": "Bengong",
                    "sosmed": "@indahjuliaa",
                    "jabatan": "Anggota",
                    "kesan": "Hobinya bengong, kadang memang enak juga punya waktu buat santai.",
                    "pesan": "Semoga semua yang diinginkan bisa tercapai satu per satu, semangat terus kaa!"
                },
                {
                    "nama": "Jacinda Kesya Alvara",
                    "nim": "124450023",
                    "umur": "18",
                    "asal": "Kalimantan Barat",
                    "alamat": "Korpri",
                    "hobbi": "Nyapu depan gacoan",
                    "sosmed": "@cacalvra",
                    "jabatan": "Anggota",
                    "kesan": "Hobinya unik dan cukup berbeda dari yang lain.",
                    "pesan": "Semoga selalu diberi kelancaran dalam kuliah dan kegiatan sehari-hari!"
                },
                {
                    "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                    "nim": "124450089",
                    "umur": "20",
                    "asal": "Padang",
                    "alamat": "Kotabaru",
                    "hobbi": "Bangun pagi",
                    "sosmed": "@muhammdrafka_",
                    "jabatan": "Anggota",
                    "kesan": "Hobinya bangun pagi, kebiasaan yang bagus juga.",
                    "pesan": "Semoga kebiasaan baiknya terus terjaga dan semua urusannya lancar!"
                }
            ]

            display_images_with_data(
                gambar_urls_MMB,
                data_list_MMB
            )

    Departemen_Minbak()







elif menu == "Departemen SSD":
    def Departemen_SSD():
        st.markdown(
            "<h3 style='text-align: center;'>Departemen SSD</h3>",
            unsafe_allow_html=True
        )

        tab1, tab2, tab3, tab4 = st.tabs([
            "Ketua Departemen",
            "Sekretaris",
            "Kemitraan",
            "Kewirausahaan"
        ])

        # ==========================================
        # KETUA DEPARTEMEN
        # ==========================================
        with tab1:
            gambar_urls_Ketua = [
                "https://drive.google.com/uc?export=view&id=1KGNhbecJJbvZr65wajrzMgkyEvFRewTU"
            ]

            data_list_Ketua = [
                {
                    "nama": "Ihsan Maulana Yusuf",
                    "nim": "123450110",
                    "umur": "21",
                    "asal": "Sumbar",
                    "alamat": "Belwis",
                    "hobbi": "Baca jurnal, cari jurnal yang berhubungan ta",
                    "sosmed": "@ihsan.myusuf",
                    "jabatan": "Kepala Departemen",
                    "kesan": "Bang Ihsan orangnya lumayan asik.",
                    "pesan": "Semangat terus bang, semoga cita-citanya tercapai."
                }
            ]

            display_images_with_data(
                gambar_urls_Ketua,
                data_list_Ketua
            )

        # ==========================================
        # SEKRETARIS
        # ==========================================
        with tab2:
            gambar_urls_sekdep_ssd = [
                "https://drive.google.com/uc?export=view&id=1ofji2_iq8G4OYsOSs-x2YyQwDp8yOo0A"
            ]

            data_list_sekdep_ssd = [
                {
                    "nama": "Hanifah Inaya Sani",
                    "nim": "123450000",
                    "umur": "21",
                    "asal": "Balam",
                    "alamat": "Korpri",
                    "hobbi": "Memasak",
                    "sosmed": "@_inayasani",
                    "kesan": "Kak Hanifah asik juga diajak belajar bareng.",
                    "pesan": "Semangat terus kuliahnya kak, semoga lancar semua."
                }
            ]

            display_images_with_data(
                gambar_urls_sekdep_ssd,
                data_list_sekdep_ssd
            )

        # ==========================================
        # KEMITRAAN
        # ==========================================
        with tab3:
            gambar_urls_Kemitraan = [
                "https://drive.google.com/uc?export=view&id=1KTuSTMaDKhaxk3eXxgPPiVEi_ITvHBTR",
                "https://drive.google.com/uc?export=view&id=1yWdWMPOKHaihUeg-wBKRe3hYTEmkYPfn",
                "https://drive.google.com/uc?export=view&id=10NctbY2MrUvJ-TDYguVCMaDsDYOzokFc",
                "https://drive.google.com/uc?export=view&id=1lonoBPJYVxWpDdPv8IH3FQUWtC-xLRCr",
                "https://drive.google.com/uc?export=view&id=1brlAstkmLBb26_RptHuq4WFcooc77OAs"
            ]

            data_list_Kemitraan = [
                {
                    "nama": "Mochammad Iqbal Az-zahir",
                    "nim": "124450052",
                    "umur": "20",
                    "asal": "Bekasi",
                    "alamat": "Natar",
                    "hobbi": "Nonton Drakor",
                    "sosmed": "@iqbalazzahir_",
                    "kesan": "Kak Iqbal orangnya asik.",
                    "pesan": "Semangat terus kak, semoga kuliahnya lancar."
                },
                {
                    "nama": "Afifah Fauziah",
                    "nim": "123450002",
                    "umur": "18",
                    "asal": "Padang",
                    "alamat": "Hasan 4",
                    "hobbi": "Baca jurnal, nonton Marvel",
                    "sosmed": "-",
                    "jabatan": "Kepala Divisi",
                    "kesan": "Kak Afifah cukup menginspirasi.",
                    "pesan": "Semangat terus kak, semoga divisinya makin maju."
                },
                {
                    "nama": "Hasan Nur Ramadhan",
                    "nim": "124450013",
                    "umur": "25",
                    "asal": "Lamteng",
                    "alamat": "Pemda",
                    "hobbi": "Nonton yutub",
                    "sosmed": "-",
                    "jabatan": "Anggota",
                    "kesan": "Bang Hasan orangnya punya cara sendiri.",
                    "pesan": "Semangat terus bang, semoga sukses selalu."
                },
                {
                    "nama": "Layina Ropiqo",
                    "nim": "124450016",
                    "umur": "20",
                    "asal": "Semarang",
                    "alamat": "Balam",
                    "hobbi": "Nonton dracin",
                    "sosmed": "@layinr_",
                    "jabatan": "Anggota",
                    "kesan": "Kak Layina orangnya asik.",
                    "pesan": "Semoga kuliahnya lancar terus ya kak."
                },
                {
                    "nama": "Talitha Justine",
                    "nim": "124450076",
                    "umur": "19",
                    "asal": "Sumbar",
                    "alamat": "Pemda",
                    "hobbi": "Nonton",
                    "sosmed": "@talljtine_",
                    "jabatan": "Anggota",
                    "kesan": "Kak Talitha orangnya santai.",
                    "pesan": "Semangat terus kak, jangan lupa istirahat."
                }
            ]

            display_images_with_data(
                gambar_urls_Kemitraan,
                data_list_Kemitraan
            )

        # ==========================================
        # KEWIRAUSAHAAN
        # ==========================================
        with tab4:
            gambar_urls_Kewirausahaan = [
                "https://drive.google.com/uc?export=view&id=13LZNR2UKs5-CkVm_8d1YZOU9Rv90Vvfu",
                "https://drive.google.com/uc?export=view&id=13NoUA9gdgZ5CCcfgR1lia-UMgDpj0zKf",
                "https://drive.google.com/uc?export=view&id=1AoKUIoXm_0Me7gwEyMPBgSZFFcYhMvJW",
                "https://drive.google.com/uc?export=view&id=1ER_mNf7HXv__3jkIIkPnHjIx0allpGwA",
                "https://drive.google.com/uc?export=view&id=1IiZlidIX4sOhH0iAr5QFaSb6IHVuq3ia"
            ]

            data_list_Kewirausahaan = [
                {
                    "nama": "Anadia Carana",
                    "nim": "123450019",
                    "umur": "20",
                    "asal": "Palembang",
                    "alamat": "Wayhui",
                    "hobbi": "Nyari duit",
                    "sosmed": "@anadiacrn",
                    "jabatan": "Kepala Divisi",
                    "kesan": "Kak Anadia cukup berjiwa usaha.",
                    "pesan": "Semoga usahanya lancar dan sukses terus kak."
                },
                {
                    "nama": "Abdillah Fikri Al pome",
                    "nim": "124450062",
                    "umur": "21",
                    "asal": "Sumsel",
                    "alamat": "Airan",
                    "hobbi": "Basket",
                    "sosmed": "@pomest",
                    "jabatan": "Staff Ahli",
                    "kesan": "Bang Fikri orangnya punya prinsip yang bagus.",
                    "pesan": "Semangat terus bang, semoga semua urusannya lancar."
                },
                {
                    "nama": "Afdhal Rahmad Setiawan",
                    "nim": "124450008",
                    "umur": "20",
                    "asal": "Sumbar",
                    "alamat": "Belwis",
                    "hobbi": "Fishing and game",
                    "sosmed": "@Afdhal",
                    "jabatan": "Anggota",
                    "kesan": "Bang Afdhal orangnya cukup santai.",
                    "pesan": "Semoga kuliahnya lancar dan sukses terus bang."
                },
                {
                    "nama": "Anggun Nita",
                    "nim": "124450009",
                    "umur": "20",
                    "asal": "Lamutara",
                    "alamat": "-",
                    "hobbi": "Nonton kartun",
                    "sosmed": "@anggunitaaa_",
                    "jabatan": "Anggota",
                    "kesan": "Kak Anggun orangnya lumayan asik.",
                    "pesan": "Semangat terus kak, semoga impiannya tercapai."
                },
                {
                    "nama": "Della Anisa Fitri",
                    "nim": "124450095",
                    "umur": "18",
                    "asal": "Lamtim",
                    "alamat": "Kotabaru",
                    "hobbi": "Olahraga",
                    "sosmed": "@delaanisafitri",
                    "jabatan": "Anggota",
                    "kesan": "Kak Della orangnya cukup menyenangkan.",
                    "pesan": "Semoga kuliahnya lancar dan sehat selalu kak."
                }
            ]

            display_images_with_data(
                gambar_urls_Kewirausahaan,
                data_list_Kewirausahaan
            )

    Departemen_SSD()



elif menu == "Badan Kesenatoran":
    def Badan_Kesenatoran():
        st.markdown(
            "<h3 style='text-align: center;'>Badan Kesenatoran</h3>",
            unsafe_allow_html=True
        )

        tab1, tab2, tab3, tab4 = st.tabs([
            "Senator",
            "Biro Aspirasi dan Media Komunikasi",
            "Biro Kajian Strategis dan Propaganda",
            "Biro Kesekretariatan"
        ])

        # ==========================================
        # SENATOR
        # ==========================================
        with tab1:
            gambar_urls_Senator = [
                "https://drive.google.com/uc?export=view&id=1qXTcpwU6K2lJX9g8hkOG6vTrKTL1nsHu"
            ]

            data_list_Senator = [
                {
                    "nama": "Fathinah Nur Azizah",
                    "nim": "123450072",
                    "umur": "21",
                    "asal": "Jakarta Timur",
                    "alamat": "Airan",
                    "hobbi": "Nulis Medium",
                    "sosmed": "@fathinahnaazh",
                    "jabatan": "Senator",
                    "kesan": "Kakaknya keren banget dan bisa jadi inspirasi, apalagi dari cara berpikirnya.",
                    "pesan": "Semangat terus kaa, semoga bisa terus berkembang dan makin banyak hal baik yang datang. Let's fly higher together!"
                }
            ]

            display_images_with_data(
                gambar_urls_Senator,
                data_list_Senator
            )

        # ==========================================
        # BIRO ASPIRASI DAN MEDIA KOMUNIKASI
        # ==========================================
        with tab2:
            gambar_urls_Aspirasi = [
                "https://drive.google.com/uc?export=view&id=1ziHLhH1s23EVUIijWeq9_XTaB8_pMl97",
                "https://drive.google.com/uc?export=view&id=1tRMZPKtBdzYX7f-L5IwVH3s-UvHSRmJP",
                "https://drive.google.com/uc?export=view&id=18MSeOOoEK84tJw33nM2wS4aZ0Cec1B8Q",
                "https://drive.google.com/uc?export=view&id=14QFgxk1U1JEfrVT8MGhwpeiNVFJAiqGo"
            ]

            data_list_Aspirasi = [
                {
                    "nama": "Helmy Surya Pratama",
                    "nim": "124450033",
                    "umur": "20",
                    "asal": "Jakarta",
                    "alamat": "Kedamaian",
                    "hobbi": "Ngesen kiri",
                    "sosmed": "@helmy_ist",
                    "jabatan": "Kepala Biro",
                    "kesan": "Orangna keliatanya lucu dan seru.",
                    "pesan": "Semangat terus bang, jangan lupa istirahat juga di tengah kesibukan. Kerja boleh keras, tapi istirahat jangan dilupain!"
                },
                {
                    "nama": "Fernando Dimetrius Barus",
                    "nim": "124450063",
                    "umur": "21",
                    "asal": "Tangerang",
                    "alamat": "Sebelah kamar biwa",
                    "hobbi": "Badminton",
                    "sosmed": "@barus.fernando",
                    "jabatan": "Staff Biro",
                    "kesan": "Orangnya santai banget dan enak diajak ngobrol.",
                    "pesan": "Semangat terus bang, semoga urusannya lancar. Jangan lupa sisihin waktu buat rebahan juga!"
                },
                {
                    "nama": "Suci Aulia",
                    "nim": "124450034",
                    "umur": "19",
                    "asal": "Krui",
                    "alamat": "Kota Baru",
                    "hobbi": "Bikin video random dan upload di second",
                    "sosmed": "@sciia_staff",
                    "jabatan": "Staff Biro",
                    "kesan": "kakaknya asiik dan seru",
                    "pesan": "Semangat terus kaa, semoga makin banyak pengalaman seru dan bisa terus jadi diri sendiri!"
                },
                {
                    "nama": "Wielman Itolo Halawa",
                    "nim": "124450072",
                    "umur": "20",
                    "asal": "Nias Selatan",
                    "alamat": "Asrama TB3",
                    "hobbi": "Mancing",
                    "sosmed": "@wielhawny",
                    "jabatan": "Staff Biro",
                    "kesan": "Orangnya ramah banget !",
                    "pesan": "Semangat terus bang, semoga makin bisa mengembangkan bakat yang dimiliki dan sukses ke depannya!"
                }
            ]

            display_images_with_data(
                gambar_urls_Aspirasi,
                data_list_Aspirasi
            )

        with tab3:
            gambar_urls_Kajian = [
                "https://drive.google.com/uc?export=view&id=1aspJ7jkM6un0Pm69tf9WbIVw5phPid1d",
                "https://drive.google.com/uc?export=view&id=1TTvL53wkhdoVSRkMk3ImAKqplZhKJ5cN",
                "https://drive.google.com/uc?export=view&id=1iBKV0BXhOZgpst0N-lmttk8i7LtWwme5",
                # Masukkan link foto Aqila
                # Masukkan link foto Hazel
            ]

            data_list_Kajian = [
                {
                    "nama": "Lia Hana Ichisasmita",
                    "nim": "123450089",
                    "umur": "21",
                    "asal": "Jakarta Timur",
                    "alamat": "Belwis",
                    "hobbi": "Nyari jurnal",
                    "sosmed": "@lia.h_264",
                    "jabatan": "Kepala Biro",
                    "kesan": "Banyak ilmu dan hal baru yang bisa dipelajari dari kakaknya.",
                    "pesan": "Semangat terus kaa, semoga selalu menikmati prosesnya dan semua yang diusahakan bisa membuahkan hasil!"
                },
                {
                    "nama": "Aqila Zayyan Salsabil",
                    "nim": "124450014",
                    "umur": "19",
                    "asal": "Lampung Utara",
                    "alamat": "Sukarame",
                    "hobbi": "Mendokumentasikan bayyesian",
                    "sosmed": "@aqilazayyaan",
                    "jabatan": "Staff Biro",
                    "kesan": "Style-nya keren banget dan orangnya kelihatan imut.",
                    "pesan": "Semangat terus kaa, semoga makin banyak hal baik yang datang dan semua targetnya tercapai!"
                },
                {
                    "nama": "Hazel Mahesa Handhaka",
                    "nim": "124450114",
                    "umur": "20",
                    "asal": "Lampung Timur",
                    "alamat": "Ujung Terang",
                    "hobbi": "Bulu Tangkis",
                    "sosmed": "@hazelhandhaka",
                    "jabatan": "Staff Biro",
                    "kesan": "Abangnya kece, style-nya keren banget!",
                    "pesan": "Semangat terus bang, semoga selalu diberi kemudahan dalam setiap urusan dan tetap kuat menghadapi tantangan!"
                }
            ]

            display_images_with_data(
                gambar_urls_Kajian,
                data_list_Kajian
            )

        # ==========================================
        # BIRO KESEKRETARIATAN
        # ==========================================
        with tab4:
            gambar_urls_Sekretariat = [
                "https://drive.google.com/uc?export=view&id=1SVKcc7jQH8jSgkLM66Wt4EskW__IWmUz",
                "https://drive.google.com/uc?export=view&id=1jXO6YB73KN8vU-FpdZwLfauDQioW_pge"
            ]

            data_list_Sekretariat = [
                {
                    "nama": "Nadya Ratu Anjani",
                    "nim": "123450083",
                    "umur": "21",
                    "asal": "Bandar Lampung",
                    "alamat": "Sukarame",
                    "hobbi": "Denger Lagu",
                    "sosmed": "@nadyaanjaani",
                    "jabatan": "Kepala Biro",
                    "kesan": "Kakaknya ramah banget dan cara menyampaikan materinya juga gampang dipahami.",
                    "pesan": "Semangat terus kaa, tetap konsisten dan jangan gampang nyerah. Semoga semua rencananya berjalan lancar!"
                },
                {
                    "nama": "Dwi Rahma Fitriani",
                    "nim": "124450084",
                    "umur": "19",
                    "asal": "Tulang Bawang",
                    "alamat": "Jl. Lapas Belwis",
                    "hobbi": "Dengerin musik",
                    "sosmed": "@dwi_rahmftrnii",
                    "jabatan": "Staff Biro",
                    "kesan": "Orangnya gemas dan punya pembawaan yang menyenangkan.",
                    "pesan": "Semangat terus kaa, nggak perlu buru-buru, yang penting terus berkembang. Semoga nanti bisa bersinar di waktu yang tepat!"
                }
            ]

            display_images_with_data(
                gambar_urls_Sekretariat,
                data_list_Sekretariat
            )

    Badan_Kesenatoran()


elif menu == "Departemen Internal":
    def Departemen_Internal():
        st.markdown(
            "<h3 style='text-align: center;'>Departemen Internal</h3>",
            unsafe_allow_html=True
        )

        # Template Tab Departemen Internal
        tab1, tab2, tab3, tab4 = st.tabs([
            "Kepala Departemen",
            "Sekretaris Departemen",
            "Divisi Keharmonisasian",
            "Divisi Kerohanian"
        ])

        # ==========================================
        # KEPALA DEPARTEMEN
        # ==========================================
        with tab1:
            gambar_urls_Kadep_Internal = [
                "https://drive.google.com/uc?export=view&id=1vVAZ0QX0lq5ejOrkNOkNRwlgNqfS7z5A"
            ]

            data_list_Kadep_Internal = [
                {
                    "nama": "Haikal Fransisko Simbolon",
                    "nim": "106",
                    "umur": "23",
                    "asal": "Jambi",
                    "alamat": "Jatimulyo",
                    "hobbi": "Ngerosting orang",
                    "sosmed": "Haikalsbln_",
                    "divisi": "Departemen Internal",
                    "jabatan": "Kepala Departemen",
                    "kesan": "Bang Haikal orangnya asik.",
                    "pesan": "Kegagalan berawal dari ketakutan sebelum mencoba"
                }
            ]

            display_images_with_data(
                gambar_urls_Kadep_Internal,
                data_list_Kadep_Internal
            )

        # ==========================================
        # SEKRETARIS DEPARTEMEN
        # ==========================================
        with tab2:
            gambar_urls_Sekdep_Internal = [
                "https://drive.google.com/uc?export=view&id=1N4eAdLI053YpszBf9yxF3MF_9RJCUel_"
            ]

            data_list_Sekdep_Internal = [
                {
                    "nama": "Kharisma Mustika Sari",
                    "nim": "123450034",
                    "umur": "21",
                    "asal": "Waikana",
                    "alamat": "Untung Seropati",
                    "hobbi": "Suka menolong orang",
                    "sosmed": "Rismaa. Mustika_",
                    "divisi": "Sekretariat Departemen",
                    "jabatan": "Sekretaris",
                    "kesan": "Kak Kharisma orangnya ramah.",
                    "pesan": "Keep going, no matter what"
                }
            ]

            display_images_with_data(
                gambar_urls_Sekdep_Internal,
                data_list_Sekdep_Internal
            )

        # ==========================================
        # DIVISI KEHARMONISASIAN
        # ==========================================
        with tab3:
            gambar_urls_Divisi_Keharmonisasian = [
                "https://drive.google.com/uc?export=view&id=12LZ0XtAnbGURwhOy7lam83wuYcR0QEhz",
                "https://drive.google.com/uc?export=view&id=1BZwrgyAFBRG8yKbj-fu4nN0Pa6suOdOX",
                "https://drive.google.com/uc?export=view&id=1vCb3UlfxZMBk9AddSTJgkrz1Kox-zWnq",
                "https://drive.google.com/uc?export=view&id=1H-VMICv379Wa9OrfJkLRcQ2EO3doD3iT",
                "https://drive.google.com/uc?export=view&id=1AhjJ5ZRHdnPEL2gmIr98lgyDaohrhBGm",
                "https://drive.google.com/uc?export=view&id=1bu1xoZSEn9zQjpIOcxjcw_WbIyaHtSwX",
                "https://drive.google.com/uc?export=view&id=1xlkMoP-SztD29dzgnxW_NdqwewQKskF7",
                "https://drive.google.com/uc?export=view&id=1RpFwNSci-K7L12w09gYpBONhgtTUSD4c"
            ]

            data_list_Divisi_Keharmonisasian = [
                {
                    "nama": "Hanna Gresia Sinaga",
                    "nim": "123450038",
                    "umur": "21",
                    "asal": "Kisaran CV",
                    "alamat": "Sukarame",
                    "hobbi": "Menyapa satpam ITERA",
                    "sosmed": "Hanna_g_sinaga",
                    "divisi": "Keharmonisasian",
                    "jabatan": "Kepala Divisi",
                    "kesan": "Kak Hanna orangnya asik.",
                    "pesan": "Senantiasa bertanggung jawab"
                },
                {
                    "nama": "Ahmad Farhan Ghani",
                    "nim": "123450121",
                    "umur": "",
                    "asal": "",
                    "alamat": "",
                    "hobbi": "",
                    "sosmed": "",
                    "divisi": "Keharmonisasian",
                    "jabatan": "Staf Ahli",
                    "kesan": "Bang Farhan orangnya keren.",
                    "pesan": "Gatau pen beli truck"
                },
                {
                    "nama": "Aisyah Khairun Nisa",
                    "nim": "124450009",
                    "umur": "20",
                    "asal": "Riau, Air Molek",
                    "alamat": "Belwis",
                    "hobbi": "Nulis whitlits",
                    "sosmed": "Aisyahkhairun",
                    "divisi": "Keharmonisasian",
                    "jabatan": "Anggota",
                    "kesan": "Kak Aisyah orangnya ramah.",
                    "pesan": "Jalani aja, yang penting semangat"
                },
                {
                    "nama": "Cerine Sihotang",
                    "nim": "",
                    "umur": "",
                    "asal": "",
                    "alamat": "",
                    "hobbi": "",
                    "sosmed": "",
                    "divisi": "Keharmonisasian",
                    "jabatan": "Anggota",
                    "kesan": "Kak Cerine orangnya baik.",
                    "pesan": "Hidup untuk menjadi berkat"
                },
                {
                    "nama": "Jaya Saputra Tamba",
                    "nim": "94",
                    "umur": "22",
                    "asal": "Kisaran CV",
                    "alamat": "Pemda",
                    "hobbi": "Tim boxing",
                    "sosmed": "Jay_saputra_tmb",
                    "divisi": "Keharmonisasian",
                    "jabatan": "Anggota",
                    "kesan": "Bang Jaya orangnya asik.",
                    "pesan": "Kalau tidak Sekarang Kapan Lagi"
                },
                {
                    "nama": "Najla Nursyifa",
                    "nim": "",
                    "umur": "",
                    "asal": "",
                    "alamat": "",
                    "hobbi": "",
                    "sosmed": "",
                    "divisi": "Keharmonisasian",
                    "jabatan": "Anggota",
                    "kesan": "Kak Najla orangnya ramah.",
                    "pesan": "Quote so fire I'm gate keeping"
                },
                {
                    "nama": "Rozak Ramdani",
                    "nim": "124450100",
                    "umur": "18",
                    "asal": "Lampung Selatan",
                    "alamat": "Kopri Raya",
                    "hobbi": "Isengin Arvin di kelas",
                    "sosmed": "Rozakramdani__",
                    "divisi": "Keharmonisasian",
                    "jabatan": "Anggota",
                    "kesan": "Bang Rozak orangnya seru.",
                    "pesan": "Motto tanpa kerja nyata hanyalah hiasan retorika."
                },
                {
                    "nama": "Teresa Christiani Purba",
                    "nim": "124450046",
                    "umur": "19",
                    "asal": "Riau",
                    "alamat": "Belwis",
                    "hobbi": "Masak",
                    "sosmed": "Christiani8872",
                    "divisi": "Keharmonisasian",
                    "jabatan": "Anggota",
                    "kesan": "Kak Teresa orangnya baik.",
                    "pesan": "Ciptakan peluang, jangan tunggu peluang datang"
                }
            ]

            display_images_with_data(
                gambar_urls_Divisi_Keharmonisasian,
                data_list_Divisi_Keharmonisasian
            )

        # ==========================================
        # DIVISI KEROHANIAN
        # ==========================================
        with tab4:
            gambar_urls_Divisi_Kerohanian = [
                "https://drive.google.com/uc?export=view&id=1fKxg8CNPG74YfOzPe3RKObVTkw4ZJjBz",
                "https://drive.google.com/uc?export=view&id=16rfF2DQ6oPNAMBmQjqo1pqsWoSRsQ1eq",
                "https://drive.google.com/uc?export=view&id=10pJbkahnjR8orXlPoFLKtPxSMBtBZRmv",
                "https://drive.google.com/uc?export=view&id=19iVBnrizA52Sq-QE_XYuw22XF75fC9Vw",
                "https://drive.google.com/uc?export=view&id=11xlFRspdCefbM037HdQdSlJB4sZ-AjV4",
                "https://drive.google.com/uc?export=view&id=1i_pFBl2vossbi08uXag9hssIzJkodEW4"
            ]

            data_list_Divisi_Kerohanian = [
                {
                    "nama": "Muhammad Hanif Dzaky Arifin",
                    "nim": "123450064",
                    "umur": "21",
                    "asal": "Sumbar",
                    "alamat": "Perum Way Kandis",
                    "hobbi": "Nonton film",
                    "sosmed": "Hnsdzkf_",
                    "divisi": "Kerohanian",
                    "jabatan": "Kepala Divisi",
                    "kesan": "Bang Hanif orangnya asik.",
                    "pesan": "Senja adalah hadiah pejalan kaki menjemput maghribnya"
                },
                {
                    "nama": "Audina Fitria",
                    "nim": "124450038",
                    "umur": "20",
                    "asal": "Sumbar",
                    "alamat": "Sukarame",
                    "hobbi": "Main air terjun",
                    "sosmed": "Aulinaf_03",
                    "divisi": "Kerohanian",
                    "jabatan": "Anggota",
                    "kesan": "Kak Audina orangnya ramah.",
                    "pesan": "Trust the process, embrace the journey."
                },
                {
                    "nama": "Cika Adelia Br Marbun",
                    "nim": "124451007",
                    "umur": "20",
                    "asal": "Riau, Pekanbaru",
                    "alamat": "Belwis",
                    "hobbi": "Dengerin lagu",
                    "sosmed": "Chikamrbn",
                    "divisi": "Kerohanian",
                    "jabatan": "Anggota",
                    "kesan": "Kak Cika orangnya seru.",
                    "pesan": "Amor fati"
                },
                {
                    "nama": "Gustin H. Tampubolon",
                    "nim": "",
                    "umur": "",
                    "asal": "",
                    "alamat": "",
                    "hobbi": "",
                    "sosmed": "",
                    "divisi": "Kerohanian",
                    "jabatan": "Anggota",
                    "kesan": "Kak Gustin orangnya baik.",
                    "pesan": "Kamu adalah apa yang kamu pikirkan"
                },
                {
                    "nama": "Muhammad Harvinsyah",
                    "nim": "12445128",
                    "umur": "20",
                    "asal": "Sumsel",
                    "alamat": "Belwis",
                    "hobbi": "Berburu ayam hutan",
                    "sosmed": "Muhvinz_",
                    "divisi": "Kerohanian",
                    "jabatan": "Anggota",
                    "kesan": "Bang Harvin orangnya keren.",
                    "pesan": "Tindakan adalah bahasa paling jujur."
                },
                {
                    "nama": "Rafa Sabina Fahimah",
                    "nim": "124450036",
                    "umur": "20",
                    "asal": "Natar",
                    "alamat": "Natar",
                    "hobbi": "Nanya ke Andra dan Yolanda",
                    "sosmed": "Snasaa. _",
                    "divisi": "Kerohanian",
                    "jabatan": "Anggota",
                    "kesan": "Kak Rafa orangnya ramah.",
                    "pesan": "Never let anyone including yourself, belittle your dreams"
                }
            ]

            display_images_with_data(
                gambar_urls_Divisi_Kerohanian,
                data_list_Divisi_Kerohanian
            )

    Departemen_Internal()


if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        st.markdown(
            "<h3 style='text-align: center;'>"
            "Departemen Minat, Keilmuan, dan Festival"
            "</h3>",
            unsafe_allow_html=True
        )

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "Kepala Departemen",
            "Sekretaris Departemen",
            "Professional Skill Development",
            "Pusat Inovasi dan Kajian Akademik",
            "Research & Development"
        ])

        # ==========================================
        # KEPALA DEPARTEMEN
        # ==========================================
        with tab1:
            gambar_urls_Kadep = [
                "https://drive.google.com/uc?export=view&id=1EItQL1qnCclU0hgfdjMNWT8OGiWfQZLX"
            ]

            data_list_Kadep = [
                {
                    "nama": "Fabio Banyu Cyto",
                    "nim": "123450104",
                    "umur": "21",
                    "asal": "Kedaton",
                    "alamat": "Kedaton",
                    "hobbi": "Main game & travel",
                    "sosmed": "@biyokcb",
                    "jabatan": "Kepala Departemen",
                    "kesan": "Bang Fabio orangnya asik.",
                    "pesan": "Semangat terus bang, semoga sukses selalu."
                }
            ]

            display_images_with_data(
                gambar_urls_Kadep,
                data_list_Kadep
            )

        # ==========================================
        # SEKRETARIS DEPARTEMEN
        # ==========================================
        with tab2:
            gambar_urls_Sekdep = [
                "https://drive.google.com/uc?export=view&id=1EYcbueZmijEDm3bOnbgj1tGNr_ByVOfz"
            ]

            data_list_Sekdep = [
                {
                    "nama": "Tanty Widiyastuti",
                    "nim": "123450094",
                    "umur": "21",
                    "asal": "Lampung Tengah",
                    "alamat": "Airan",
                    "hobbi": "Mendengarkan Musik",
                    "sosmed": "@tvnty_",
                    "jabatan": "Sekretaris",
                    "kesan": "Kak Tanty orangnya ramah.",
                    "pesan": "Semangat terus kak, semoga semua urusannya lancar."
                }
            ]

            display_images_with_data(
                gambar_urls_Sekdep,
                data_list_Sekdep
            )

        # ==========================================
        # PROFESSIONAL SKILL DEVELOPMENT
        # ==========================================
        with tab3:
            gambar_urls_PSD = [
                "https://cdn-icons-png.flaticon.com/512/149/149071.png",
                "https://drive.google.com/uc?export=view&id=1UAEl_eGW5QVSNpB0Ak-de0QqyVihe56N",
                "https://drive.google.com/uc?export=view&id=1icE1IozC_ZNVTALwPNvlLy9iB1YU9wep",
                "https://drive.google.com/uc?export=view&id=1ydiT2V8JZV5vNa4p5iFhUVPsXcrPFEf8",
                "https://drive.google.com/uc?export=view&id=1bJ1RKh2wrEPhQGYfZLeClK18YAtL8TnH",
                "https://drive.google.com/uc?export=view&id=1sZ8RBJ6_pogOukk42n5TmNLD9UWuVpL2"
            ]

            data_list_PSD = [
                                {
                    "nama": "Fadil Prasetyo Alfarizzi",
                    "nim": "123450...",
                    "umur": "...",
                    "asal": "...",
                    "alamat": "...",
                    "hobbi": "...",
                    "sosmed": "...",
                    "jabatan": "Kepala Divisi",
                    "kesan": "Bang Fadil orangnya keren.",
                    "pesan": "Semangat terus bang, semoga makin sukses."
                },
                {
                    "nama": "Manuel Frederika",
                    "nim": "124450039",
                    "umur": "20",
                    "asal": "Batam",
                    "alamat": "Way kandis",
                    "hobbi": "Katama",
                    "sosmed": "manuelfdk_",
                    "jabatan": "Anggota",
                    "kesan": "Kak Manuel orangnya ramah.",
                    "pesan": "Semoga semua urusannya lancar ya kak."
                },
                {
                    "nama": "Ni Made Okta Viola Darma Putri",
                    "nim": "124450005",
                    "umur": "20",
                    "asal": "Lampung Tengah",
                    "alamat": "Korpri",
                    "hobbi": "Travelling",
                    "sosmed": "@violaadrtr_",
                    "jabatan": "Anggota",
                    "kesan": "Kak Viola orangnya baik.",
                    "pesan": "Semangat terus kak, jangan lupa istirahat."
                },
                {
                    "nama": "Risa Romadona",
                    "nim": "124450127",
                    "umur": "20",
                    "asal": "Natar",
                    "alamat": "Natar",
                    "hobbi": "Rolling skate",
                    "sosmed": "@risarmdna",
                    "jabatan": "Anggota",
                    "kesan": "Kak Risa orangnya seru.",
                    "pesan": "Semoga makin sukses dan lancar terus kak."
                },
                {
                    "nama": "Vannisa Ramadhani",
                    "nim": "124450078",
                    "umur": "19",
                    "asal": "Kepulauan Riau",
                    "alamat": "Telung Betung",
                    "hobbi": "Nonton KHW",
                    "sosmed": "@vunnycaa",
                    "jabatan": "Anggota",
                    "kesan": "Kak Vannisa orangnya asik.",
                    "pesan": "Semangat terus kak, semoga semua targetnya tercapai."
                },
{
                    "nama": "Yulia Kristine Malau",
                    "nim": "",
                    "umur": "...",
                    "asal": "...",
                    "alamat": "...",
                    "hobbi": "...",
                    "sosmed": "...",
                    "jabatan": "Anggota",
                    "kesan": "Kak Yulia orangnya asik.",
                    "pesan": "Semangat terus kak, semoga sukses selalu."
                },
            ]

            display_images_with_data(
                gambar_urls_PSD,
                data_list_PSD
            )

        # ==========================================
        # PUSAT INOVASI DAN KAJIAN AKADEMIK
        # ==========================================
        with tab4:
            gambar_urls_PIKA = [
                "https://drive.google.com/uc?export=view&id=1NVX4LTh_K8Uc4y2pq-pJ8-nnbqeT2bC6",
                "https://drive.google.com/uc?export=view&id=1GxbrGTk5UNtSPslZj8VIlPLXUz2gqGEm",
                "https://drive.google.com/uc?export=view&id=1uVCr880Q0gCtPZxW8eMplMzjkENK5rZv",
                "https://drive.google.com/uc?export=view&id=1HM_vIaManQUtDQ1tFTIo8Lvgac9zRJDF",
                "https://drive.google.com/uc?export=view&id=1i2HqNDn9p58patWEl-EKbYbja8-I1qge",
                "https://drive.google.com/uc?export=view&id=168WWS8YGyOdx-04EHTdzNAUoUjssO2wh"
            ]

            data_list_PIKA = [
                {
                    "nama": "Akeyla Fairus Shafi",
                    "nim": "123450119",
                    "umur": "21",
                    "asal": "Bandar Lampung",
                    "alamat": "Bandara Lampung",
                    "hobbi": "Dengerin Musik",
                    "sosmed": "@keyashafi_",
                    "jabatan": "Kepala Divisi",
                    "kesan": "Kak Akeyla orangnya ramah.",
                    "pesan": "Semoga sukses terus kak, semangat selalu."
                },
                {
                    "nama": "Elsa Sitorus",
                    "nim": "124450088",
                    "umur": "21",
                    "asal": "Sumatera Utara",
                    "alamat": "Pemda",
                    "hobbi": "Rebahan",
                    "sosmed": "_els.a",
                    "jabatan": "Anggota",
                    "kesan": "Kak Elsa orangnya asik.",
                    "pesan": "Semoga semua urusannya lancar ya kak."
                },
                {
                    "nama": "Fadya Izzatul 'Aini",
                    "nim": "124450062",
                    "umur": "20",
                    "asal": "Pringsewu",
                    "alamat": "Airan",
                    "hobbi": "Makan",
                    "sosmed": "@fadyaizzatul_",
                    "jabatan": "Anggota",
                    "kesan": "Kak Fadya orangnya seru.",
                    "pesan": "Semangat terus kak, semoga sukses ke depannya."
                },
                {
                    "nama": "Lovianora Saragih",
                    "nim": "...",
                    "umur": "...",
                    "asal": "...",
                    "alamat": "...",
                    "hobbi": "...",
                    "sosmed": "...",
                    "jabatan": "Anggota",
                    "kesan": "Kak Lovianora orangnya baik.",
                    "pesan": "Semoga semua rencananya berjalan lancar kak."
                },
                {
                    "nama": "M. Alsi Syahrulloh",
                    "nim": "124450092",
                    "umur": "20",
                    "asal": "Kalianda",
                    "alamat": "Gedung Harapan",
                    "hobbi": "Main Game",
                    "sosmed": "@keyashafi",
                    "jabatan": "Anggota",
                    "kesan": "Bang Alsi orangnya asik.",
                    "pesan": "Semangat terus bang, pelan-pelan yang penting maju."
                },
                {
                    "nama": "Sherena Florencia",
                    "nim": "124450027",
                    "umur": "19",
                    "asal": "Bengkulu Selatan",
                    "alamat": "Belwis",
                    "hobbi": "Make up",
                    "sosmed": "@sher_renna",
                    "jabatan": "Anggota",
                    "kesan": "Kak Sherena orangnya ramah.",
                    "pesan": "Semoga selalu bahagia dan sukses ya kak."
                }
            ]

            display_images_with_data(
                gambar_urls_PIKA,
                data_list_PIKA
            )

        # ==========================================
        # RESEARCH & DEVELOPMENT
        # ==========================================
        with tab5:
            gambar_urls_RnD = [
                "https://drive.google.com/uc?export=view&id=1DJdoKKm9ShJ4X0vqniTDCOC2xpfXI5em",
                "https://drive.google.com/uc?export=view&id=1M5AQA2nZJbGeHKjPX5bZe6sW-K2JE1LR",
                "https://drive.google.com/uc?export=view&id=1y7a1BrZ922RGeLCSOflQJvW2-gNiGsiJ",
                "https://drive.google.com/uc?export=view&id=1ZA5ipGLFW4aURVxQx02POqkMNiYskLUn",
                "https://drive.google.com/uc?export=view&id=10RNknUtx5T_pSsw0QHg18QAdBXwu8L_n",
                "https://drive.google.com/uc?export=view&id=1X4I0tW0fPp85RKbPRRWtyVFDHYtWarAf",
                "https://drive.google.com/uc?export=view&id=18GVfQG9L3D8kpMR5LdMvY-DQlUsHm-GL",
                "https://drive.google.com/uc?export=view&id=1JNSwWggwzGp-9B7N0ZEV3J5wgK40VAQw"
            ]

            data_list_RnD = [
                {
                    "nama": "Razin Hafid Hamdi",
                    "nim": "123450096",
                    "umur": "21",
                    "asal": "Padang",
                    "alamat": "Belwis",
                    "hobbi": "Futsal",
                    "sosmed": "@razyn.hfd",
                    "jabatan": "Kepala Divisi",
                    "kesan": "Bang Razin orangnya asik.",
                    "pesan": "Semangat terus bang, semoga makin sukses."
                },
                {
                    "nama": "Faiza Try Anjani",
                    "nim": "124450075",
                    "umur": "19",
                    "asal": "Padang",
                    "alamat": "Belwis",
                    "hobbi": "Baca",
                    "sosmed": "@faizaanjanii",
                    "jabatan": "Anggota",
                    "kesan": "Kak Faiza orangnya ramah.",
                    "pesan": "Semoga semua urusannya lancar ya kak."
                },
                {
                    "nama": "Gathfan Nadif Ali",
                    "nim": "124450001",
                    "umur": "20",
                    "asal": "Bandar Lampung",
                    "alamat": "Rajabasa",
                    "hobbi": "Main game",
                    "sosmed": "@gathfannadif",
                    "jabatan": "Anggota",
                    "kesan": "Bang Gathfan orangnya seru.",
                    "pesan": "Semangat terus bang, semoga sukses selalu."
                },
                {
                    "nama": "Hafidz Wahdiansyah",
                    "nim": "124450064",
                    "umur": "20",
                    "asal": "Metro",
                    "alamat": "Metro Kibang",
                    "hobbi": "Ngegame",
                    "sosmed": "@apiszzaja_",
                    "jabatan": "Anggota",
                    "kesan": "Bang Hafidz orangnya asik.",
                    "pesan": "Semoga semua urusannya lancar bang."
                },
                {
                    "nama": "Kaleb Filbert Istel",
                    "nim": "124450062",
                    "umur": "20",
                    "asal": "Bandar Lampung",
                    "alamat": "Campang Raya",
                    "hobbi": "Nge-gym, baca novel",
                    "sosmed": "@kelelep_comberan",
                    "jabatan": "Anggota",
                    "kesan": "Bang Kaleb orangnya keren.",
                    "pesan": "Semangat terus bang, semoga makin sukses."
                },
                {
                    "nama": "Melva Shaprina Febrianti",
                    "nim": "124450087",
                    "umur": "19",
                    "asal": "Sumatera Selatan",
                    "alamat": "Sukarame",
                    "hobbi": "Menari",
                    "sosmed": "@melva_fbrt",
                    "jabatan": "Anggota",
                    "kesan": "Kak Melva orangnya ramah.",
                    "pesan": "Semoga semua targetnya tercapai ya kak."
                },
                {
                    "nama": "Muhammad Syafiqul Falakh",
                    "nim": "125450099",
                    "umur": "20",
                    "asal": "Lampung Selatan",
                    "alamat": "Asrama",
                    "hobbi": "Membaca",
                    "sosmed": "@syaafiq",
                    "jabatan": "Anggota",
                    "kesan": "Bang Syafiqul orangnya baik.",
                    "pesan": "Semangat terus bang, jangan berhenti melangkah."
                },
                {
                    "nama": "Rifky Henry Ferdianto",
                    "nim": "124450115",
                    "umur": "150 (p, mksud bg??? #kaget)",
                    "asal": "Rajabasa",
                    "alamat": "Balam",
                    "hobbi": "Tennis Meja",
                    "sosmed": "@henryferdianto",
                    "jabatan": "Anggota",
                    "kesan": "Bang Henry orangnya kocak.",
                    "pesan": "Semoga hal-hal baik selalu datang ke abang, aamiin!"
                }
            ]

            display_images_with_data(
                gambar_urls_RnD,
                data_list_RnD
            )

    Departemen_MIKFES()


elif menu == "Departemen Medkraf":
    def medkraf():
        st.markdown("<h3 style='text-align: center;'>Departemen Media Kreatif</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Dokumentasi", "Divisi Media dan Konten Spesialis", "Visual Design"])

        with tab1:
            gambar_urls_Kadep_medkraf = [
            "https://cdn-icons-png.flaticon.com/512/149/149071.png",
            ]
            data_list_Kadep_medkraf = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "KAKA KERENN!!",
                "pesan": "Jujur takjub sih aku untuk orang orang di bidang media kreatif, walaupun dikejar dl desain tapi masih tangguh sekali"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)                

        with tab2:
            gambar_urls_sekdep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1ZAwy3d9CCX9ImZVDtq5UisAp57UYDuey",
            ]
            data_list_sekdep_medkraf = [
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "KEREN JUGA JUJURRR",
                "pesan": "Tetap semangat terus ya kaaa, semoga apapun wishlist kaka bisa tercapai satu persatuu"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_medkraf, data_list_sekdep_medkraf)

        with tab3:
            gambar_urls_Divisi_dokumentasi = [
            "https://cdn-icons-png.flaticon.com/512/149/149071.png",
            "https://drive.google.com/uc?export=view&id=1y2iwlU696nroX0f_UyELiR7yzOcnBw5x",
            "https://drive.google.com/uc?export=view&id=1KxoDgA3nqCelQEqUCOLXDnUvv10dluig",
            "https://drive.google.com/uc?export=view&id=1FycXnl-DvD-RXtjGUKO2R2TgkUnVL38E"
            ]
            data_list_Divisi_dokumentasi = [
            {
                "nama": "Labo Napitupulu",
                "nim": "37",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Tong setan",
                "sosmed": "noerruuu",
                "divisi": "Dokumentasi",
                "kesan": "Abangnya lucu dan seru",
                "pesan": "Semangatt terus bangg kuliah dan organisasinyaa!"
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "divisi": "Dokumentasi",
                "kesan": "Kakaknya baik hati dan tidak sombong",
                "pesan": "Tetap semangat ya kaa walau beban tugas kaka sometimes cukup beratt!"
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "felisyanbl__",
                "divisi": "Dokumentasi",
                "kesan": "Kakanya tidak sombong dan baik hati",
                "pesan": "Jaga kesehatan selalu kakaa, jangan lupa bahagia jugaa!!"
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": "Bully Felisya Nabila Nugroho",
                "sosmed": "muh_razan_",
                "divisi": "Dokumentasi",
                "kesan": "Abangnya baik banget dan",
                "pesan": "Semangattt terus banggg!! sempetin waktu untuk abang istirahat sejenak dari organisasi dan perkuliahan yaa"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_dokumentasi, data_list_Divisi_dokumentasi)

        with tab4:
            gambar_urls_Divisi_Media_dan_Konten_Spesialis = [
                "https://drive.google.com/uc?export=view&id=1EMocR_dFqXkiCURxTiNrukGen4JJ46eb",
            "https://drive.google.com/uc?export=view&id=1Q44RMIkg8h9hM0Poa5tgGQWFVQGUkHcP",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1190DOPvYlbtUpgm1edzRbCTAfA26kYzw",
            "https://drive.google.com/uc?export=view&id=1U5fH9zRe16gy2NulJy6VIuHDbO3kOMSP",
            "https://drive.google.com/uc?export=view&id=1T3QXa70er8MLHUDErqZsKQZySB3P-ZVu"
            ]
            data_list_Divisi_Media_dan_Konten_Spesialis = [
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Nongkrong depan ruang prodi",
                "sosmed": "saniayyllstr",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Ramah sekaliii",
                "pesan": "Semangattt ka kuliah dan organisasinyaa, sempatin waktu untuk self reward yaa"
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Kakanya baik dan ramah ",
                "pesan": "Terus bahagia ya ka Allishaa!"
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu roda",
                "sosmed": "alya.rmdhnti",
                "divisi": "Media dan Konten Speasialis",
                "kesan": "Kerenn",
                "pesan": "Kakanya ramah bangett, semoga kaka selalu dikelilingi oleh hal hal baik yaa!"
            },
            {
                "nama": "Bunga Clarissa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "bungaclrssf",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Ramah bangettt",
                "pesan": "Semangatt ka kuliah dan organisasinyaa, jaga pola makan dan jangan stress-stress yaa"
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "Gada yang tau",
                "asal": "Rumah bapak",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "difanyhsa_",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Lucuu",
                "pesan": "Semangattt teruss ka kuliah dan organisasinyaa, sempatkan waktu untuk rehat sejenak yaa"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@nzlhauly_",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Gemass",
                "pesan": "Semangat selalu kaa kuliah dan organisasinyaa"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Media_dan_Konten_Spesialis, data_list_Divisi_Media_dan_Konten_Spesialis)

        with tab5:
            gambar_urls_Divisi_Visual_Design = [
            "https://drive.google.com/uc?export=view&id=1t3GTVl4c0iA4rjgdqZ2-nb8IgT8cNFlJ",
            "https://cdn-icons-png.flaticon.com/512/149/149071.png",    
            "https://drive.google.com/uc?export=view&id=1A5VRTMIddHOVG-r92TBPneq165SZ9TZz",
            "https://drive.google.com/uc?export=view&id=1alRBZXhHayce8JMqdXxW-d-zSMrnXKjd",
            "https://drive.google.com/uc?export=view&id=1sB4bSaoU-o1U5aMQlgtzTnh08Cy0t_YX",
            "https://drive.google.com/uc?export=view&id=1yZIQ5ADt1fldaEP9ZzCdCOGD0ITInZXK"
            ]
            data_list_Divisi_Visual_Design = [
            {
                "nama": "Raihanna Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "n1tg._",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Kakanya baik dan ramah",
                "pesan": "Semangatt kuliah dan organisasinya kaa, jangan lupa berbahagiaa!"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "Nyuluh manuk",
                "sosmed": "@daffascript_",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Baik banget abangnya",
                "pesan": "Semoga abang selalu dilingkupi oleh kebaikan"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll fesnuk",
                "sosmed": "edsel_0712",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Kerenn",
                "pesan": "Jangan lupa jaga kesehatann dan jangan lupa berbahagia"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "luciarachel_",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Kakanya asik",
                "pesan": "Sehat selalu kaka"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis, menulis",
                "sosmed": "@_shaazzh",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Kakanya baik dan ramah",
                "pesan": "Semangatt terus ka, semoga selalu berbahagiaa"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "Bobo",
                "sosmed": "Xifasky",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Cantik dan ramah sekalii",
                "pesan": "Semangattt kaa untuk kuliah dan organisasinyaa!!"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Visual_Design, data_list_Divisi_Visual_Design)
    medkraf()

elif menu == "Departemen PSDA":
    def PSDA():
        st.markdown(
            "<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>",
            unsafe_allow_html=True
        )

        tab1, tab2, tab3, tab4 = st.tabs([
            "Kepala Departemen",
            "Sekretaris Departemen",
            "Divisi Kaderisasi",
            "Divisi Peningkatan Mutu Anggota"
        ])

        with tab1:
            gambar_urls_Kadep_psda = [
                "https://drive.google.com/uc?export=view&id=1UfpA348X1CPJ3NqdMU6KvVN1GurRpdVF",
            ]

            data_list_Kadep_psda = [
                {
                    "nama": "Arienta Khusnul Ananda",
                    "nim": "123450097",
                    "umur": "21",
                    "asal": "Dekat Pantai Kedu, Kalianda",
                    "alamat": "Samping kos capo",
                    "hobbi": "Baca jurnal",
                    "sosmed": "@arientakhsnl_",
                    "kesan": "Kak Arienta orangnya ramah dan keren.",
                    "pesan": "Semangat terus TA-nya kak, semoga lancar semua urusannya!"
                },
            ]

            display_images_with_data(
                gambar_urls_Kadep_psda,
                data_list_Kadep_psda
            )

        with tab2:
            gambar_urls_sekdep_psda = [
                "https://drive.google.com/uc?export=view&id=1OWqKYr-ELER0iVLLmG4aodlWiVCybArr",
            ]

            data_list_sekdep_psda = [
                {
                    "nama": "Vany Salsabila Putri",
                    "nim": "123450022",
                    "umur": "20",
                    "asal": "Sibolga",
                    "alamat": "Pudan Kost",
                    "hobbi": "Pacaran",
                    "sosmed": "@vany.salsabilaa",
                    "kesan": "Kak Vany orangnya tegas.",
                    "pesan": "Semangat terus TA-nya kak"
                },
            ]

            display_images_with_data(
                gambar_urls_sekdep_psda,
                data_list_sekdep_psda
            )

        with tab3:
            gambar_urls_Divisi_Kaderisasi = [
                "https://drive.google.com/uc?export=view&id=1_X8cdO3n6bRywv9Wo2P2nUoyO1TreqXB",
                "https://drive.google.com/uc?export=view&id=1g2_oinsN9jEYiD1yb1LDWsEkcYZuKqeo",
                "https://drive.google.com/uc?export=view&id=1J79rHGUPKaJo85OOoLrTzkR_Bac84Mq4",
                "https://drive.google.com/uc?export=view&id=18gJGimrkUpgkkIRioFN53Cl6dkSfqK8q",
                "https://drive.google.com/uc?export=view&id=1rbWovzdiAQVBAwxEbbpZQBjd3Y-CU1Om",
                "https://drive.google.com/uc?export=view&id=1Uf0DIa6s6aYeKMk8AuTQWVlwUqBYGPSZ",
                "https://drive.google.com/uc?export=view&id=1ZbnF90CueYcMk6-oPjmYe8hAAowUDuyI",
                "https://drive.google.com/uc?export=view&id=1qoxQRP06JD059c7treh_vekSdUVzFc1o"
            ]

            data_list_Divisi_Kaderisasi = [
                {
                    "nama": "Nobel Nizam Fathirizki",
                    "nim": "123450117",
                    "umur": "21",
                    "asal": "Bandar Lampung",
                    "alamat": "Urip",
                    "hobbi": "Banyak",
                    "sosmed": "@nobelnizam",
                    "kesan": "Bang Nobel orangnya berwibawa.",
                    "pesan": "Semoga selalu diberi kebaikan bang, semangat juga buat TA-nya!"
                },
                {
                    "nama": "Afriza Azmi",
                    "nim": "124450110",
                    "umur": "20",
                    "asal": "Malang",
                    "alamat": "Samping kos Jemar",
                    "hobbi": "Berantem",
                    "sosmed": "@friezazmi",
                    "kesan": "Bang Afriza orangnya keren dan tegas.",
                    "pesan": "Semangat terus bang, semoga sukses ke depannya!"
                },
                {
                    "nama": "Ayake Alfatih Ramadan",
                    "nim": "124450108",
                    "umur": "21",
                    "asal": "Peninjauan, 10 kota di atas, Solok, Sumatera Barat",
                    "alamat": "Blok D 79, Jl Manggis 8 Perum Pemda, Way Huwi Jati Agung, Lampung Selatan, Lampung",
                    "hobbi": "Masak ayam",
                    "sosmed": "@ykeall",
                    "kesan": "Bang Ayake orangnya tegas dan keren.",
                    "pesan": "Jaga kesehatan bang, semoga semua urusannya lancar!"
                },
                {
                    "nama": "Caesar Ozora Alrando",
                    "nim": "124450017",
                    "umur": "21",
                    "asal": "Painar, Sumatera Barat",
                    "alamat": "Gedung F",
                    "hobbi": "Mandiin anak ayam",
                    "sosmed": "@caesar.oriza",
                    "kesan": "Bang Caesar orangnya tegas.",
                    "pesan": "Semangat terus bang, jangan lupa istirahat!"
                },
                {
                    "nama": "Euodia Meiliana Friedita",
                    "nim": "124450029",
                    "umur": "18",
                    "asal": "Debu Tanah",
                    "alamat": "Di sebelah pasar, di bawah turunan, di atas tanjakan, di seberang kontrakan Yazid Rizal",
                    "hobbi": "Ngegiring anak ayam bermain di Lapangan",
                    "sosmed": "@yudiameilianaa_",
                    "kesan": "Kak Euodia orangnya keren .",
                    "pesan": "Semangat terus kuliahnya kak, semoga semuanya lancar!"
                },
                {
                    "nama": "Haikal Seventino Tamba",
                    "nim": "124450012",
                    "umur": "18",
                    "asal": "Rantau Perapat",
                    "alamat": "Belakang kos Ayake",
                    "hobbi": "Goreng ayam",
                    "sosmed": "@_haikaaall",
                    "kesan": "Bang Haikal orangnya berwibawa.",
                    "pesan": "Semangat terus bang kuliahnya, semoga sukses selalu!"
                },
                {
                    "nama": "Putri Manna Anantama Simbolon",
                    "nim": "124450056",
                    "umur": "18",
                    "asal": "Sabang",
                    "alamat": "Nomaden",
                    "hobbi": "Duduk samping Henry",
                    "sosmed": "@putrimannaa",
                    "kesan": "Kak Putri orangnya baik dan ramah.",
                    "pesan": "Semangat terus kak, semoga semua urusannya lancar!"
                },
                {
                    "nama": "Queenta Thifaal Nabila",
                    "nim": "124450059",
                    "umur": "18",
                    "asal": "Kota Gajah",
                    "alamat": "Depan pemancingan",
                    "hobbi": "Nyuapin anak ayam",
                    "sosmed": "@queentanabila",
                    "kesan": "Kak Queenta orangnya keren.",
                    "pesan": "Jaga kesehatan kak, semangat terus kuliahnya!"
                },
            ]

            display_images_with_data(
                gambar_urls_Divisi_Kaderisasi,
                data_list_Divisi_Kaderisasi
            )

        with tab4:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
                "https://drive.google.com/uc?export=view&id=1Da5pAF2ebpRMaKbz8BC05tC7VfxOl1Mw",
                "https://drive.google.com/uc?export=view&id=1vvGm2DWskBhWyAQeB09BIkiasmIsvozA",
                "https://drive.google.com/uc?export=view&id=1nm0x_8upBO0O6es_CBlHGhj3VmUuf5bM",
                "https://drive.google.com/uc?export=view&id=1_p5-BmKa09OSBXXNodvU_kHmUmfQiJRp",
                "https://drive.google.com/uc?export=view&id=1wp-E7pjfo7U1nYEw_Sd9BO-xGkeRGvAI",
                "https://drive.google.com/uc?export=view&id=1hhjp_8cQ81u1FmWnllCSd1KvXvDUkN3N",
                "https://drive.google.com/uc?export=view&id=1O4sgU9N59p48lQSaCbGbN8KLfCYF0SD6",
            ]

            data_list_Divisi_Peningkatan_Mutu_Anggota = [
                {
                    "nama": "Desman Velius Halawa",
                    "nim": "123450114",
                    "umur": "17",
                    "asal": "Nias",
                    "alamat": "Airan",
                    "hobbi": "Bermusik",
                    "sosmed": "@desmannhal_",
                    "kesan": "Bang Desman orangnya asik dan seru.",
                    "pesan": "Semangat terus TA-nya bang, semoga lancar semua urusannya!"
                },
                {
                    "nama": "Azzelya Thianandry",
                    "nim": "124450041",
                    "umur": "19",
                    "asal": "Lampung",
                    "alamat": "Sukarame",
                    "hobbi": "Makan Aice",
                    "sosmed": "@azzelytn",
                    "kesan": "Kak Azzelya orangnya cantik dan ramah.",
                    "pesan": "Semangat terus kuliahnya kak, jangan lupa jaga kesehatan!"
                },
                {
                    "nama": "Charrlindah",
                    "nim": "124450037",
                    "umur": "21",
                    "asal": "Jakarta Pusat",
                    "alamat": "Cendrawasih 1",
                    "hobbi": "Ngurus peternakan",
                    "sosmed": "@charrlln",
                    "kesan": "Kak Charrlindah orangnya baik dan ramah.",
                    "pesan": "Sehat selalu kak, semangat terus kuliahnya!"
                },
                {
                    "nama": "Jeremi Marolop P. Situmorang",
                    "nim": "124450111",
                    "umur": "17",
                    "asal": "Nibire, Papua",
                    "alamat": "Sebelah kos Haikal",
                    "hobbi": "Memahat patung",
                    "sosmed": "@jemarrro",
                    "kesan": "Bang Jeremi orangnya tegas dan asik.",
                    "pesan": "Semangat terus kuliahnya bang, sehat selalu!"
                },
                {
                    "nama": "Nabila Nur Azizah",
                    "nim": "124450048",
                    "umur": "19",
                    "asal": "Lampung Timur",
                    "alamat": "Belwis",
                    "hobbi": "Main Roblox",
                    "sosmed": "@n.bila_a",
                    "kesan": "Kak Nabila orangnya baik dan ramah.",
                    "pesan": "Jangan lupa jaga kesehatan kak, semangat kuliahnya!"
                },
                {
                    "nama": "Rafli Al Mansyah Tambunan",
                    "nim": "124450007",
                    "umur": "20",
                    "asal": "Tembung",
                    "alamat": "Belwis Tengah",
                    "hobbi": "Mancing",
                    "sosmed": "@dearfkvmfl",
                    "kesan": "Bang Rafli orangnya baik dan asik.",
                    "pesan": "Semangat terus kuliahnya bang, semoga sukses!"
                },
                {
                    "nama": "Salavia Naharani",
                    "nim": "124450090",
                    "umur": "20",
                    "asal": "Lampung Timur",
                    "alamat": "Jatimulyo",
                    "hobbi": "Nonton",
                    "sosmed": "@avi.nhr",
                    "kesan": "Kak Salavia orangnya imut dan lucu.",
                    "pesan": "Semangat terus kuliahnya kak, semoga sukses selalu!"
                },
            ]

            display_images_with_data(
                gambar_urls_Divisi_Peningkatan_Mutu_Anggota,
                data_list_Divisi_Peningkatan_Mutu_Anggota
            )

    PSDA()


elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        st.markdown(
            "<h3 style='text-align: center;'>Departemen Eksternal</h3>",
            unsafe_allow_html=True
        )

        tab1, tab2, tab3, tab4 = st.tabs([
            "Kepala Departemen",
            "Sekretaris Departemen",
            "Hubungan Luar",
            "Pengabdian Masyarakat"
        ])

        def buat_data(nama, jabatan, pesan):
            return {
                "nama": nama,
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "jabatan": jabatan,
                "kesan": "",
                "pesan": pesan
            }

        # ==========================================
        # KEPALA DEPARTEMEN
        # ==========================================
        with tab1:
            gambar_urls_Kadep = [
                    "https://cdn-icons-png.flaticon.com/512/149/149071.png",
            ]

            data_list_Kadep = [
                    {
        "nama": "Arini Puteri Elandra",
        "nim": "123450069",
        "umur": "21",
        "asal": "Lampung",
        "alamat": "Teluk Betung Selatan",
        "hobbi": "Nonton Kartun",
        "sosmed": "@elandraa_",
        "jabatan": "Kepala Departemen",
        "kesan": "Karismatik, baik tapi tetap tegas.",
        "pesan": "Sukses selalu kaa ke depannya, semangat juga nyusun TA-nya nanti!"
    }
            ]

            if len(gambar_urls_Kadep) == len(data_list_Kadep):
                display_images_with_data(
                    gambar_urls_Kadep,
                    data_list_Kadep
                )
            else:
                for data in data_list_Kadep:
                    st.subheader(data["nama"])
                    st.write("Jabatan:", data["jabatan"])
                    st.write("Kutipan:", data["pesan"])

        with tab2:
            gambar_urls_Sekretaris = [
                "https://drive.google.com/uc?export=view&id=1po9Zc71s492t7IHrHDPkoDQ_R3iMX3AC"
            ]

            data_list_Sekretaris = [
                    {
        "nama": "Nabyla Sharfina",
        "nim": "123450008",
        "umur": "20",
        "asal": "Bengkulu",
        "alamat": "Jalan Lapas",
        "hobbi": "Jalan-jalan",
        "sosmed": "@bylaash",
        "jabatan": "Sekretaris",
        "kesan": "Cantik dan baik banget.",
        "pesan": "Semangat terus kaa kuliahnya, sama nyusun TA-nya juga!"
    }

            ]

            if len(gambar_urls_Sekretaris) == len(data_list_Sekretaris):
                display_images_with_data(
                    gambar_urls_Sekretaris,
                    data_list_Sekretaris
                )
            else:
                for data in data_list_Sekretaris:
                    st.subheader(data["nama"])
                    st.write("Jabatan:", data["jabatan"])
                    st.write("Kutipan:", data["pesan"])

        with tab3:
            gambar_urls_Hublu = [
                "https://cdn-icons-png.flaticon.com/512/149/149071.png",
                "https://drive.google.com/uc?export=view&id=12zwjROMAotcfbofBB1Z9UiZcD2cTEd9r",
                "https://cdn-icons-png.flaticon.com/512/149/149071.png",
                "https://drive.google.com/uc?export=view&id=1vauYi3DSbBW4z_av5y61RVuc2L3UTTob",
                "https://cdn-icons-png.flaticon.com/512/149/149071.png",
                "https://drive.google.com/uc?export=view&id=1nqItjLRHDfGn4XFBKtz6IqNRka6-6Z4z",
                "https://drive.google.com/uc?export=view&id=1QL0Wr4G3DhBGejLOHo7Tupj2_N5HBM7e",
                "https://drive.google.com/uc?export=view&id=18ntPlDx2CDsFS3BFpafebR7p0R89poYV",
                "https://drive.google.com/uc?export=view&id=1wbN2O-SFlOX4Ki9vL_HsYO3sg7Q3KX5Z",
                "https://drive.google.com/uc?export=view&id=1a4oCi8kvuEduimWkDEIDnlP2lQ2OLC8k"
                # sesuai urutan nama di bawah
            ]

            data_list_Hublu = [
    {
        "nama": "Khoirul Muttoharoh",
        "nim": "123450021",
        "umur": "21",
        "asal": "Lampung Barat",
        "alamat": "Airan",
        "hobbi": "Main",
        "sosmed": "@khoirul_muttoharoh",
        "jabatan": "Kepala Divisi",
        "kesan": "Imut banget.",
        "pesan": "Semangat ya kaa nanti nyusun TA-nya, semoga semua urusannya dipermudah. Aamiin!"
    },
    {
        "nama": "Ahmad Rizky",
        "nim": "123450050",
        "umur": "21",
        "asal": "Tangerang Selatan",
        "alamat": "GH",
        "hobbi": "Ga ngapa-ngapain",
        "sosmed": "@ahmad.rizky___",
        "jabatan": "Staff Ahli",
        "kesan": "Keren banget, abang beneran jadi role model saya!",
        "pesan": "Jaga kesehatan bang, di negara yang ga sehat ini wkwk."
    },
    {
        "nama": "Adinda Deswita Maharani",
        "nim": "124450083",
        "umur": "cepuyuh tayun",
        "asal": "Ikut kadep",
        "alamat": "Sukabumi",
        "hobbi": "Mancing",
        "sosmed": "@khaindaa_",
        "jabatan": "Anggota",
        "kesan": "Kakaknya ramah dan baik.",
        "pesan": "Jaga kesehatan ya kaa, semangat juga kuliahnya!"
    },
    {
        "nama": "Ahmad Bimo Akbar Arkana",
        "nim": "124450113",
        "umur": "-",
        "asal": "Tanggamus",
        "alamat": "Balam",
        "hobbi": "Lihat-lihat perumahan",
        "sosmed": "@bimo_arkana",
        "jabatan": "Anggota",
        "kesan": "Keren dan ramah.",
        "pesan": "Semangat terus bang kuliahnya, jangan lupa jaga kesehatan juga!"
    },
    {
        "nama": "Alfaya Abiyyi",
        "nim": "124450006",
        "umur": "20",
        "asal": "Bandar Lampung",
        "alamat": "Bandar Lampung",
        "hobbi": "Makan yang manis biar manis",
        "sosmed": "@alfayabiyi",
        "jabatan": "Anggota",
        "kesan": "Keren banget!",
        "pesan": "Semangat terus bang kuliahnya, jaga kesehatan juga ya!"
    },
    {
        "nama": "Asri Meilani",
        "nim": "124450010",
        "umur": "20",
        "asal": "Lampung Barat",
        "alamat": "Korpri",
        "hobbi": "Nonton Film",
        "sosmed": "@asemeilani",
        "jabatan": "Anggota",
        "kesan": "Baik dan lucu orangnya.",
        "pesan": "Sukses selalu kak buat ke depannya!"
    },
    {
        "nama": "Bima Ekayasa",
        "nim": "124450106",
        "umur": "20",
        "asal": "Lampung",
        "alamat": "Bandar Lampung",
        "hobbi": "Berlaku humoris dan manis",
        "sosmed": "@bimayasa_",
        "jabatan": "Anggota",
        "kesan": "Keren, baik, dan ramah.",
        "pesan": "Semangat terus bang kuliahnya. Makin tinggi semester makin banyak juga stresnya wkwk, jadi tetap jaga kesehatan!"
    },
    {
        "nama": "Indah Khairunnisa",
        "nim": "124450077",
        "umur": "20",
        "asal": "Ampera",
        "alamat": "Disini aja",
        "hobbi": "Mancing",
        "sosmed": "@khaindaa_",
        "jabatan": "Anggota",
        "kesan": "Baik dan lucu.",
        "pesan": "Kak, jangan ikut marah-marah yaa. Versi medisnya kakak beneran terbaik!"
    },
    {
        "nama": "Riska Erlis Dayu Tiara",
        "nim": "124450022",
        "umur": "20",
        "asal": "Palembang",
        "alamat": "Bebas",
        "hobbi": "Nge-follow up chat",
        "sosmed": "@erlsriska",
        "jabatan": "Anggota",
        "kesan": "Gemes banget.",
        "pesan": "Jaga kesehatan ya kaa, semangat juga buat kuliahnya!"
    },
    {
        "nama": "Yollanda Agustina",
        "nim": "124450024",
        "umur": "20",
        "asal": "Kerangka Bawang Sebelah Barat",
        "alamat": "Jati Agung",
        "hobbi": "Tanya Bang Henry",
        "sosmed": "@yollanda_agustina16",
        "jabatan": "Anggota",
        "kesan": "Kak Yollanda keren, hebat, dan kuat!",
        "pesan": "Jaga kesehatan ya kaa, apalagi kegiatannya banyak. Jangan sampai kecapekan!"
    }
            ]

            if len(gambar_urls_Hublu) == len(data_list_Hublu):
                display_images_with_data(
                    gambar_urls_Hublu,
                    data_list_Hublu
                )
            else:
                st.info(
                    "Foto anggota Hubungan Luar belum lengkap. "
                    "Biodata tetap ditampilkan sementara."
                )

                for data in data_list_Hublu:
                    with st.container(border=True):
                        st.subheader(data["nama"])
                        st.write("Jabatan:", data["jabatan"])
                        st.write("Kutipan:", data["pesan"])

        # ==========================================
        # DIVISI PENGABDIAN MASYARAKAT
        # ==========================================
        with tab4:
            gambar_urls_Pengabdian = [
                "https://drive.google.com/uc?export=view&id=1kjDwn8aOyeeNqU7dW9meNaUYQcCRnL1L",
                "https://cdn-icons-png.flaticon.com/512/149/149071.png",
                "https://drive.google.com/uc?export=view&id=1BzhvEpBMc5egJv4_Vv0gvfSDiP0DA6yU",
                                "https://drive.google.com/uc?export=view&id=1eY4JNHxKyHxkPeMtnXEynacx53GvAOOC",
                                "https://drive.google.com/uc?export=view&id=1YvcF20oy33_zojrQDDy4u5UMJZAmMmg7",
                                "https://drive.google.com/uc?export=view&id=1JTDAqPhQIv7IHg5dA4ZfHRq12ECD96_J",
                                "https://drive.google.com/uc?export=view&id=1ReLSCgNByeglL5P_p2AAlpxIFOuhVJOW",
                                "https://drive.google.com/uc?export=view&id=1vYyjEr8TwdQABa8bxh_H5wQYMT4nHeqv",
                                "https://drive.google.com/uc?export=view&id=1VC6ww4HJhMUeo92u3dLPU_1xUGXeddo4",
                                                "https://cdn-icons-png.flaticon.com/512/149/149071.png",

            ]

            data_list_Pengabdian = [
    {
        "nama": "Aditya Taufiqurrohman",
        "nim": "123450032",
        "umur": "22",
        "asal": "Tetangga Kadep",
        "alamat": "Belwis",
        "hobbi": "Memancing keributan",
        "sosmed": "@adityatfq",
        "jabatan": "Kepala Divisi",
        "kesan": "Baik, ramah, dan welcome banget.",
        "pesan": "Semangat bang ngerjain TA-nya, semoga semua langkah ke depannya dipermudah. Aamiin!"
    },
    {
        "nama": "Fathya Intami Gusda",
        "nim": "123450095",
        "umur": "25",
        "asal": "Tangerang Selatan",
        "alamat": "Sukarame",
        "hobbi": "Baca Wattpad",
        "sosmed": "@fatthyaa_",
        "jabatan": "Staff Ahli",
        "kesan": "Keren banget kakaknya.",
        "pesan": "Jaga kesehatan ya kaa, semoga impian kakak bisa tercapai satu per satu!"
    },
    {
        "nama": "Tarisya Hidayatul Rahmi",
        "nim": "123450052",
        "umur": "25",
        "asal": "Luhak Tanah Data",
        "alamat": "Gerbang Barat",
        "hobbi": "Jadi orang baik",
        "sosmed": "-",
        "jabatan": "Staff Ahli",
        "kesan": "Manis dan imut.",
        "pesan": "Sukses selalu kaa ke depannya, semoga goals-nya tercapai satu per satu!"
    },
    {
        "nama": "Ashila Islamisahfa Vanisha",
        "nim": "124450028",
        "umur": "20",
        "asal": "Sini",
        "alamat": "Jauh pokoknya",
        "hobbi": "Tidur",
        "sosmed": "@kshigf",
        "jabatan": "Anggota",
        "kesan": "Cantik dan ramah.",
        "pesan": "Jangan lupa bahagia ya kaa, semoga hari-harinya selalu menyenangkan!"
    },
    {
        "nama": "Danil N Fadillah",
        "nim": "124450103",
        "umur": "19",
        "asal": "Karawang",
        "alamat": "Belakang Polda",
        "hobbi": "Ngasih makan ikan cupang",
        "sosmed": "@d4niel_fdlh",
        "jabatan": "Anggota",
        "kesan": "Keren dan baik.",
        "pesan": "Semangat terus kuliahnya bang, jangan lupa jaga kesehatan!"
    },
    {
        "nama": "Favian Arkaanda",
        "nim": "124450021",
        "umur": "19",
        "asal": "Swiss",
        "alamat": "Main Game",
        "hobbi": "Ngesen kanan",
        "sosmed": "@fvnnn05",
        "jabatan": "Anggota",
        "kesan": "Mirip influencer itu, siapa ya namanya wkwk.",
        "pesan": "Keren bang, semangat menjalani perkuliahan dan kehidupannya! #salambinjai"
    },
    {
        "nama": "Muhammad Fathiy Zumar Yazid",
        "nim": "124450081",
        "umur": "20",
        "asal": "Sit u lah",
        "alamat": "Pohon Mulia",
        "hobbi": "Nyari hobi",
        "sosmed": "@zydddddd__",
        "jabatan": "Anggota",
        "kesan": "Abangnya keren kalau nggak marah-marah wkwk.",
        "pesan": "Panjang umur dan sehat selalu bang. Tetap semangat kuliah walaupun tiap semester bikin asam lambung naik!"
    },
    {
        "nama": "Muhammad Rizaldi",
        "nim": "124450093",
        "umur": "Masih muda lah",
        "asal": "Rahim Ibu",
        "alamat": "Pasar lantai 3.5",
        "hobbi": "Tanyain sama Yuder (beneran ditanya ya)",
        "sosmed": "@jaldii._",
        "jabatan": "Anggota",
        "kesan": "Keren banget, jujur inspiring!",
        "pesan": "Semangat terus bang Jaldi, semoga bisa menggapai impian satu per satu!"
    },
    {
        "nama": "Saskia Nova Magdalena",
        "nim": "124450074",
        "umur": "...",
        "asal": "Banyak Begal",
        "alamat": "Pinggir Jalan",
        "hobbi": "Nonton Tinker Bell",
        "sosmed": "@snova.19",
        "jabatan": "Anggota",
        "kesan": "Kakaknya imut dan ramah.",
        "pesan": "Semangat terus kaa kuliahnyaaa, go go!"
    },
    {
        "nama": "Selma Siti Aisyah",
        "nim": "123450044",
        "umur": "20",
        "asal": "Lampung",
        "alamat": "Bandara Lampung",
        "hobbi": "Jalan-jalan",
        "sosmed": "@selmasiti_aisyah",
        "jabatan": "Anggota",
        "kesan": "Ramah dan cantik.",
        "pesan": "Vibes kakaknya ceria dan positif banget!"
    }
            ]

            if len(gambar_urls_Pengabdian) == len(data_list_Pengabdian):
                display_images_with_data(
                    gambar_urls_Pengabdian,
                    data_list_Pengabdian
                )
            else:
                st.info(
                    "Foto anggota Pengabdian Masyarakat belum lengkap. "
                    "Biodata tetap ditampilkan sementara."
                )

                for data in data_list_Pengabdian:
                    with st.container(border=True):
                        st.subheader(data["nama"])
                        st.write("Jabatan:", data["jabatan"])
                        st.write("Kutipan:", data["pesan"])

    Departemen_Eksternal()
