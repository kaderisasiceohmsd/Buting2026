import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubahh
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
            "Departemen Minbak"
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
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
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
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"NIM: {data_list[i]['NIM']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobi: {data_list[i]['Hobi']}")
            st.write(f"Sosial Media: {data_list[i]['Sosmed']}")
            st.write(f"Kesan: {data_list[i]['Kesan']}")
            st.write(f"Pesan: {data_list[i]['Pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xsPXI2fhQjeLsRS-w-45sGIcV05IrSHB", # fajar
            "https://drive.google.com/uc?export=view&id=16-8EutSEIHVLuoxbcqpoh4dmPpIc_N5L", # aqil
            "https://drive.google.com/uc?export=view&id=1VppIOE5acHpEb4uGU-5zMOE6ucTigchg", # efi
            "https://drive.google.com/uc?export=view&id=1EdjKu09QB_Z1SbR0D9XEQdZMettVnFnZ", # qois
            "https://drive.google.com/uc?export=view&id=1mPC9ZSdw6bZhOXTJXaEfnf0Yw-u8ngK6", # hafsa
            "https://drive.google.com/uc?export=view&id=1EQsCgvaLbIxed31vz10R76rRnyFOHGEr", # luthfia
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM": "123450103",
                "Umur": "22",
                "Asal": "Batam",
                "Alamat": "Kesektariatan HMSD",
                "Hobi": "Push IMO",
                "Sosmed": "@jars_mrp",
                "Kesan": "Bang Fajar orangnya berwibawa, keren bisa jadi ketua himpunan",  
                "Pesan":"Semangat selalu bang dalam mengerjakan tugas akhrinya"# 1
            },
            {
                "Nama": "Muhammmad Aqil Ramadhan",
                "NIM": "1233450066",
                "Umur": "22",
                "Asal":"Bangkinam",
                "Alamat": "Sekretariatan HMSD",
                "Hobi": "Dzikie",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Bang Aqil orangnya ramah dan baik, saat menjawab pertanyaan kemarin pun sangat mudah dipahami",  
                "Pesan":"Terima kasih bang atas penjelasan mengenai kesekjenan saat wwc kemarin, semoga Bang Aqil selalu diberikan kelancaran dalam mengerjakan tugas akhirnya"# 1
            },
            {
                "Nama": "Efi Defiyati",
                "NIM": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "Seru ngedengerin penjelasan mengenai tugas dan peran dari sekretaris",  
                "Pesan":"Semangat terus Kak Efi dalam menjalani perkuliahan dan mengerjakan tugas akhrinya"# 1
            },
            {
                "Nama": "Qois Olifio",
                "NIM": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobi": "Mainin Surat",
                "Sosmed": "@qoisolifio",
                "Kesan": "Bang Qois orangnya ramah banget jadi pas ngedengerin penjelasan mengenai sekretaris mudah dipahami",  
                "Pesan":"Semoga Bang Qois kedepannya selalu diberikan kemudahan dan kesuksesan. Semangat terus Bang Qois buat mengerjakan tugas akhirnya!"
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "NIM": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Berkuda",
                "Sosmed": "@Hafsafazilaa",
                "Kesan": "Kak Hafsa orangnya humble, penjelasan yang diberikan mudah dipahami",  
                "Pesan":"Semoga selalu diberi kelancaran dalam mengerjakan tugas akhirnya, semangat kakk!"# 1
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "NIM": "123450004",
                "Umur": "21",
                "Asal":"Bengkulu",
                "Alamat": "Airan",
                "Hobi": "main ke kost Efi",
                "Sosmed": "@luthfiaarmdhni",
                "Kesan": "Kak Luthfia orangnya seru dan aktif. Dari penjelasannya, saya jadi lebih tahu tentang tugas dan tanggung jawab bendahara dalam himpunan",
                "Pesan": "Semangat terus Kak Luthfia buat ngerjain tugas akhirnya, semoga dilancarkan sampai selesai dan cepat wisuda!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Legislatif":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14Vd8Co6TUXkMB5OrtO32ln7Llcn9ehnd", #ridho
            "https://drive.google.com/uc?export=view&id=11LbyqgvvmYcSqeALYIpD8XASQ99apdTe", #jue
            "https://drive.google.com/uc?export=view&id=1zcPzLFdeGCDaps_427IyVSRyADggDTPZ", #dharu
            "https://drive.google.com/uc?export=view&id=118nlpm_U_jIMpE859bTGeqWjivIA9AiU", #niko
            "https://drive.google.com/uc?export=view&id=1Kp9Xu7pGRDZ0c2axmbGMoRGdh0YAqzdB", #siti
            "https://drive.google.com/uc?export=view&id=1FT1UZ3KvQ7zFQ0clZhV_XRym6jRlJVOv", #givaro
            "https://drive.google.com/uc?export=view&id=1LGswmCklrK7HX9zU9M6Zl5md2Ey_9hwX", #afganis
            "https://drive.google.com/uc?export=view&id=1nOK8jsMSc0PiA0uvsygY1BkW6zBqbzI3", #hani
            "https://drive.google.com/uc?export=view&id=1azA91mJuheeltUyYTSDpIR9i3iEoXXhi", #jeremi
            "https://drive.google.com/uc?export=view&id=1c5Jj08jOsxN802D1ReNDAy9AoV0Rzx4D", #monica
            "https://drive.google.com/uc?export=view&id=1dgnm1zLNHAlxNq8e6GOHiD8dK_5YwC6F", #sekar
            "https://drive.google.com/uc?export=view&id=1gf4-B7GesdwTOpYvtHQPGKGonvfozHL0", #jhona
            "https://drive.google.com/uc?export=view&id=1ReLF7lfV_Ez9_p552FCS_75IuJrF0j_j", #wan
        ]

        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "NIM": "123450060",
                "Umur": "20",
                "Asal": "Cambridge",
                "Alamat": "GH",
                "Hobi": "Wawancara",
                "Sosmed": "@imridhomanik",
                "Kesan": "Bang Ridho orangnya asik suka bercanda dan saat wwc kesannya enjoy no tegang-tegang club",
                "Pesan": "Semoga Bang Ridho selalu diberi kelancaran dalam menjalani kegiatan-kegiatannya dan selalu semangat dalam mengerjakan tugas akhirnya nanti"
            },
            {
                "Nama": "Juesi Apridelia Saragih ",
                "NIM": "123450085",
                "Umur": "19",
                "Asal": "Singkawang",
                "Alamat": "Pelangi",
                "Hobi": "Dengerin lagu duhai sayang",
                "Sosmed": "j__eesie",
                "Kesan": "Kak Jue orangnya baik banget karena pernah jadi kakak asuh pas TPB, lucu juga orangnya dan berwawasan",
                "Pesan": "Sehat selalu Kak Jue semoga apa yang ingin dicapai dapat dipermudah oleh Tuhan dan semangat buat mengerjakan tugas akhirnya"
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "NIM": "123450023",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Nonton drama AI",
                "Sosmed": "@exvoltas",
                "Kesan": "Bang Dharu orangnya keren banget, saya jadi termotivasi buat lebih aktif dalam mengikuti perlombaan",
                "Pesan": "Semangat terus Bang Dharu buat persiapan PIMNAS nya!! "
            },
            {
                "Nama": "Gh Mikael Niko A S",
                "NIM": "124450025",
                "Umur": "20",
                "Asal": "Jabung",
                "Alamat": "Jati Agung",
                "Hobi": "COD Musang",
                "Sosmed": "@me._kael",
                "Kesan": "Bang Niko baik banget apalagi pas waktu jadi asprak Alpro banyak banget ngebantu nya",
                "Pesan": "Terima kasih bang Niko atas bimbingannya dan semangat terus bang Niko"
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "NIM": "124450015",
                "Umur": "18",
                "Asal": "Banten",
                "Alamat": "Kedaton",
                "Hobi": "Koleksi kartu boboiboy",
                "Sosmed": "@syt.rifa",
                "Kesan": "Kak Siti orangnya lucu pas wwc sering dijailin sama Bang Ridho",
                "Pesan": "Semangat terus kak Siti buat menjalani kegiatan sehari-hari dan perkuliahannya"
            },
            {
                "Nama": "Givaro Ananta",
                "NIM": "123450078",
                "Umur": "21",
                "Asal": "Lampung Barat",
                "Alamat": "Sukabumi",
                "Hobi": "Ngopi",
                "Sosmed": "@gifaroo",
                "Kesan": "Abangnya seru dan tau bang Givaro karena sering dimirip-miripin sama temen angkatan",
                "Pesan": "Sehat selalu bang Givaro dan semangat terus dalam menjalani perkulihannya"
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450042",
                "Umur": "21",
                "Asal": "Krui",
                "Alamat": "Jatimulyo",
                "Hobi": "Memancing",
                "Sosmed": "@afghanisnt_",
                "Kesan": "Kak Afghanis orangnya baik banget banyak banget ngebantu pas acara magenta angkatan 25 dan sekarang jadi pentutor metnum buat kelas RC keren bangett..",
                "Pesan": "Semangat terus kak Nisa dan sabar sabar ya buat nutor di kelas RC"
            },
            {
                "Nama": "Hani Qurrota Aini",
                "NIM": "124450020",
                "Umur": "20",
                "Asal": "Kota Bumi",
                "Alamat": "Sukarame",
                "Hobi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "Kakaknya lucu sering diganguin juga sama Bang Ridho waktu wwc",
                "Pesan": "semangat dan sehat selalu kak Hani"
            },
            {
                "Nama": "Jeremia Halim",
                "NIM": "124450101",
                "Umur": "20",
                "Asal": "Cibaduyut",
                "Alamat": "Teluk",
                "Hobi": "Makan Pedes",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Abangnya keren dan humble banget waktu pertama kali ketemu pas wwc",
                "Pesan": "Semangat teus bang jerem dalam menjalani kegiatan dan perkuliahannya"
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "123450073",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@monica_tjg",
                "Kesan": "Kakaknya lucu tapi sayang pas wwc kemarin datangnya pas kami udah mau pulang",
                "Pesan": "semangat terus kak Monica dan semangat selaluuuu!!!"
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "NIM": "124450082",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Pemda",
                "Hobi": "Nginep di kost putri",
                "Sosmed": "@sekardnwp",
                "Kesan": "Kak Sekar orangnya baik dan humble, pas wwc juga sharing-sharing tentang waktu kak sekar magang di RND",
                "Pesan": "Semangat terus kak Sekar..."
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "NIM": "124450121",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Gym dan koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "Bang Jhona orangnya lucu dan asik banget, enjoyy banget orangnya",
                "Pesan": "Semangat terus Bang Jhona dan congratsss abis menanggg perlombaan "
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "NIM": "123450077",
                "Umur": "20",
                "Asal": "Pasay",
                "Alamat": "Belwis",
                "Hobi": "Nyapa angin",
                "Sosmed": "@nshayka",
                "Kesan": "Kakaknya lucu, baik, humble dan funcfact nya kakak ini dulu kelompoknya Bayes juga",
                "Pesan": "Semangat terus buat Kak Wan buat mengerjakan tugas akhirnyaa"
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    baleg()
    
if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YlbPBaw4_9Lc7O-OZVVQYXcWDUQABjMb",
            "https://drive.google.com/uc?export=view&id=1GJprv39cDID83FLxgDRp6eKZNhGqfb6Q",
            "https://drive.google.com/uc?export=view&id=1GFtEm0RpwzEiARCKOkoej8ZhPoBbbNSp",
            "https://drive.google.com/uc?export=view&id=1lwgrbaXhiwh8u-e5Hw6EGrh8NhCvVNpH",
            "https://drive.google.com/uc?export=view&id=1RhXblTe0jiPmP4Bb9qJnOdZM4EOMI1VA",
            "https://drive.google.com/uc?export=view&id=1UDQUSS2fwEeug0-IEjznHRqtjP2RgdZh",
            "https://drive.google.com/uc?export=view&id=1I8nti61QH96zBFPgHGzShJ8l7fVihWXz",
            "https://drive.google.com/uc?export=view&id=1B5VrrIeQb5jxkOhOvkAqSsbSl9MssKus",
            "https://drive.google.com/uc?export=view&id=1ndP6-n8lE0mcoH9SigK7ASF8D4uC8Y27",
            "https://drive.google.com/uc?export=view&id=1XyJoJPrX4nmfWkHr0VSv_XC2nXzzaz9s",
        ]

        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "NIM": "123450072",
                "Umur": "21",
                "Asal": "jakarta",
                "Alamat": "Belakang PB",
                "Hobi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kak Fathinah orangnya baik banget dan humble penjelasannya mengenai badan kesenatoran mudah dipahami",
                "Pesan": "Terima kasih kak atas penjelasannya kemarin semoga ilmu yang telah diberikan dapat bermanfaat untuk kami"
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "NIM": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Denger lagu",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Kakaknya baik banget, keren, dan lucu banyak ngejelasin juga waktu wwc kemarin",
                "Pesan": "Terima kasih kak atas ilmu yang diberikan semoga kakak selalu diberi kelancaran didalam semua kegiatan yang akan dilakukan "
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "NIM": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. lapas",
                "Hobi": "Baca buku nonton film, denegrin musik",
                "Sosmed": "@dwi_rahmftnii",
                "Kesan": "Kak Dwi orangnya murah senyum.",
                "Pesan": "Semangat terus kak Dwi dalam menjalani perkuliahannya"
            },
            {
                "Nama": "Helmy Surya Pratama",
                "NIM": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Kedamaian",
                "Hobi": "Ngesen kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "Bang Helmi lucu banget waktu foto harus melet katanya dan kerenn banget orangnyaa",
                "Pesan": "Semangat terus bang Helmi dan sehat selalu "
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "NIM": "124450063",
                "Umur": "19",
                "Asal": "Tanggerang Kota",
                "Alamat": "Sebelah kamar biwa",
                "Hobi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Bang Nando baik banget, banyak ngebantu waktu persiapan acara magenta kemarin",
                "Pesan": "Terima kasih banyak bang Nando semoga selalu diberikan kelancaran"
            },
            {
                "Nama": "Suci Aulia",
                "NIM": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota Baru",
                "Hobi": "Mancing",
                "Sosmed": "@sciia_",
                "Kesan": "Kak Suci orangnya lucu, baik, murah senyum",
                "Pesan": "Sehat selalu kak Suci, sang mentor kebanggaan Cosval"
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "NIM": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Bang Wiel keren banget denger-denger jago nge MC sama Moderator",
                "Pesan": "Semangat terus bang Wiel dalam menjalani kegiatan-kegiatannya"
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "NIM": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobi": "Nonton",
                "Sosmed": "@lia.h_264",
                "Kesan": "Kak Hana keren banget beberapa kali tampil sebagai pemateri saat rangkaian",
                "Pesan": "Terima kasih atas ilmunya kak Hana semoga ilmu yang telah disampaikan dapat bermanfaat sama kami"
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "NIM": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Mendokumentasikan Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": """Pertama kali ketemu kak Aqila itu pas ada pertemuan sama panitia-panitia pilketang di tahum sebelumnya. Kebetulan kak Aqila dulu ada di divisi acara juga dan selama pertemuan itu saya ngeliat senidiri gimana ide-ide yang dikasih sama kak Aqila yang membuat saya ternganga kayak keren bener kakak ini saya mau jadi kayak dia (tapi boong) nah dari situ kesan saya ke kak Aqila Zayyan Salsabil ga pake A ini keren banget. Nah yang bener ga disangka-sangka itu waktu pengumuman kelompok kader ternyata kak Aqila ini jadi my i am mentorr gweh saya aku sikam eug wathasi, selama proses kaderisasi ini kak Aqila udah banyak banget ngebantu kami bukan cuman sekedar mengingatkan dan mengarahkan aja, tapi berusaha buat kami ini ngeklop antar satu sama lain. Mulai dari ngajak main, fotobooth, ngerayain ultah sampe hal-hal kecil yang bisa bikin kami makin klop. Kegiatan-kegiatan kayak gini yang ngebuat kaderisasi jadi lebih bewarna. Pokoknya keren lah josjis terbaik terhebat tergokil termangu. Nah itulah kesan saya kepada my mentor gweh saya, selesai sudah permintaan kanjeng mentor Aqila Zayyan Salsabil ini yang meminta kesan ke beliau harus panjang, sekian dari saya Afdhi Hafiidz Habibie sang anggota tanpa tanda jasa. Terima Kasih""",
                "Pesan": """Terima kasih banyak ya kak Aqila buat semua waktu, tenaga ,dan usaha yang sudah diberikan ke kami selama proses kaderisasi ini. Makasih juga udah mau nemenin kami, ngajak kami buat makin deket, dan ngebuat kelompok ini banyak momen-momen yang ga bisa dilupain dan akan selalu dikenang oleh para anggota-anggota bayesmup. Semoga kak Aqila selalu diberikan kelancaran baik diperkuliahan maupun di organisasi dan semoga hal baik yang kakak kasih ke kami bisa kembali ke kakak sendiri. Semoga kak Aqila selalu dikelilingi oleh orang baik seperti saya eaaa. Sekian dari Bibi terima kasih atas semuanya....."""
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "NIM": "124450114",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Gunung Terang",
                "Hobi": "giring ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Bang Hazel orangnya keren bisa jadi ketuplak Science fest apalagi rambutnya keren badai kece abiezz",
                "Pesan": "Sehat selalu bang Hazel dan semoga apa yang diinginkan bisa tercapai"
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VILA3Myg4MmQi9zRERh0EhDNddUebs-Z",
            "https://drive.google.com/uc?export=view&id=1Zw0GhSzPhqAnc0F-QtPmoSU3Xpkh4aJ7",
            "https://drive.google.com/uc?export=view&id=1P-v7H0dJmpTzU5MZMxt1nGCzUwFYUqu6",
            "https://drive.google.com/uc?export=view&id=1HGN1H0Fw9l14csffCPToUP5G5f7rSvYd",
            "https://drive.google.com/uc?export=view&id=1YblwbyeESgZUhohH04HKEAuzw6WU8efT",
            "https://drive.google.com/uc?export=view&id=1Le_gvaqkQzPbBkwojQkvW2aJ-Y1x5HLX",
            "https://drive.google.com/uc?export=view&id=1IxiSk970twnOJ3j5JWiNvI653wmyzY5V",
            "https://drive.google.com/uc?export=view&id=16AZauaLNeuHDIoQtf-txefRWtYNUFMMF",
            "https://drive.google.com/uc?export=view&id=1N67aB2EUiUIJyzSKBklyPLTbdHvj0_ij",
            "https://drive.google.com/uc?export=view&id=1OuC5LekFh-kXpvjXLcqXzFtQwzqu329d",
            "https://drive.google.com/uc?export=view&id=1tVFa9PmZYTuBGjmWT7MT_EWGmMHeeDM-",
            "https://drive.google.com/uc?export=view&id=1Rk_HjRTNQWTau4wCdyTB-achjxOo0VFL",
            "https://drive.google.com/uc?export=view&id=12qoTRr9TkMoZj-yVxbIQOZwC2ozGoyx9",
            "https://drive.google.com/uc?export=view&id=1hvgiwOjPiIFhawpMd9VkCtpDsBAP9z3-",
            "https://drive.google.com/uc?export=view&id=1x2kLv-mx3NHCfHQRw1i0a-tKQ2vizewX",
            "https://drive.google.com/uc?export=view&id=1IPPQkfZDi_qbiaguwMCkahz6u4VgtmCv",
            "https://drive.google.com/uc?export=view&id=1J-K2KRMvtRb9kQJJRyojNrVMFtZpec4i",
        ]
        data_list = [
            {
                "Nama": "Arienta Khusnul Ananda",
                "NIM": "123450097",
                "Umur": "21",
                "Asal": "Pinggir Pantai",
                "Alamat": "Samping Kost Capo",
                "Hobi": "Ngerjain Anak Kader",
                "Sosmed": "@arientakhsnl_",
                "Kesan": "Kak Arienta orangnya murah senyum dan humble",  
                "Pesan":"Semoga kak Arienta selalu diberikan kelancaran dan dimudahkan dalam mengerjakan tugas akhirnya nanti"
            },
            {
                "Nama": "Vany Salsabila Putri",
                "NIM": "123450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Pudan Kost",
                "Hobi": "Pacaran",
                "Sosmed": "@vany.salsabilaa",
                "Kesan": "Kak Vany orangnya baik banget dan murah senyum juga",  
                "Pesan":"Sehat selalu kak Vany dan semoga selalu diberikan kelancaran dalam menjalani tugas akhirnya nanti"
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "NIM": "123450023",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Banyak",
                "Sosmed": "@nobelnizam",
                "Kesan": "Bang Nobel orangnya tegas, berwibawa dan profesional dalam bertugas",  
                "Pesan":"Sehat selalu dan sukses untuk kedepannya buat Bang Nobel"
            },
            {
                "Nama": "Afriza Azmi",
                "NIM": "124450110",
                "Umur": "20",
                "Asal":"Malang",
                "Alamat": "Samping Pasar",
                "Hobi": "Duel boxing sama reno",
                "Sosmed": "@friezazmi",
                "Kesan": "Orangnya keren banget apalagi pas supporteran dan tegas juga orangnya",  
                "Pesan":"Sehat terus bang Azmi dan sukses buat kedepannya"
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "NIM": "124450059",
                "Umur": "21",
                "Asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "Alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "Hobi": "Cekek Ayam",
                "Sosmed": "@ykeall",
                "Kesan": "Orangnya humble, baik, suka bercanda",  
                "Pesan":"Semoga bang Ayake selalu diberikan kesehatan dan kelancaran dalam menjalani kegiatan-kegiatan serta perkuliahan"
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "NIM": "124450017",
                "Umur": "20",
                "Asal":"Painar, Sumatera Barat",
                "Alamat": "Gedung F",
                "Hobi": "Mandiin anak ayam",
                "Sosmed": "@caesar.oriza",
                "Kesan": "Bang Caesar orangnya tegas dan humble juga",  
                "Pesan":"Sehat selalu untuk bang Caesar dan semoga apa yang diimpi-impikan bisa tercapai"
            },
            {
                "Nama": "Euodia Meiliana Fredita",
                "NIM": "124450029",
                "Umur": "18",
                "Asal":"Adam dan Hawa",
                "Alamat": "Depan Kontrakan Yazids",
                "Hobi": "Nonjokin orang
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Kak Euodia orangnya seru, Tegas , dan juga baik",  
                "Pesan":"Semoga kak Euodia selalu dikelilingi oleh orang baik-baik "
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "NIM": "124450032",
                "Umur": "Tinggi Yosep - 170",
                "Asal":"Jambi",
                "Alamat": "Belakang Pemancingan",
                "Hobi": "Goreng Ayam",
                "Sosmed": "@_haikaaall",
                "Kesan": "Bang Haikal orangnya tegas",  
                "Pesan":"Semangat bang Haikal dalam menjalani perkuliahannya"
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "NIM": "124450029",
                "Umur": "18",
                "Asal": "Rumah sakit",
                "Alamat": "Arga Kost 1 jalan Way Huwi gang Mawar Raya",
                "Hobi": "liatin bang Nobel main sulap",
                "Sosmed": "@putrimannaa",
                "Kesan": "Kak Putri orangnya baikk, ramah, dan murah senyum",  
                "Pesan":"Sehat selalu kak Putri dan semangat selalu"
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "NIM": "124450059",
                "Umur": "18",
                "Asal": "Lampung Tengah",
                "Alamat": "Gang Cendrawasih",
                "Hobi": "Makan di wardat",
                "Sosmed": "@quenntanaabilaa",
                "Kesan": "Kak Queenta orangnya baik dan perhatian",  
                "Pesan":"Semoga kak queenta selalu dipermudah untuk mencapai keinginannya"
            },
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "123450114",
                "Umur": "23",
                "Asal": "Nias",
                "Alamat": "Airan",
                "Hobi": "Main musik",
                "Sosmed": "@dsmanhal",
                "Kesan": "Bang Desman orangnya kerenn, dan juga asikk, baikk",  
                "Pesan":"Semoga bang desman selalu didekat hal-hal baikk"
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "Kak Azzel orangnya humble, dan juga baikkk sekali",  
                "Pesan":"Semoga semua keinginan kak azzel tercapai"
            },
            {
                "Nama": "Charrlindah",
                "NIM": "124450041",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cendrawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlln",
                "Kesan": "Kak Charrlindah orangnya baikk, dan juga ramah",  
                "Pesan":"Semoga kak charlindah dikelilingi hal-hal baik"
            },
            {
                "Nama": "Jeremi Marolop P. Situmorang",
                "NIM": "124450111",
                "Umur": "17",
                "Asal":"Jayapura",
                "Alamat": "RS airan",
                "Hobi": "Nonton a day in my life",
                "Sosmed": "@jemarrro",
                "Kesan": "Bang Jemar orangnya kerenn apalagi saat damaskus",  
                "Pesan":"Semoga bang jeremi bisa menggapai semua keinginannya"
            },
            {
                "Nama": "Nabila Nur Azizah",
                "NIM": "124450048",
                "Umur": "18",
                "Asal":"Lampung",
                "Alamat": "Barokah",
                "Hobi": "Main Roblox",
                "Sosmed": "@n.bila_a",
                "Kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa",  
                "Pesan":"Semoga kak nabila mendapatkan hal-hal yang diinginkan"
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "NIM": "124450007",
                "Umur": "18",
                "Asal":"Sibolga",
                "Alamat": "Belwis",
                "Hobi": "Membaca peraturan rektor",
                "Sosmed": "@dearrfkvmfl",
                "Kesan": "Bang Rafli orangnya humble , baik, dan juga ramah",  
                "Pesan":"Semoga bang rafli selalu bisa mencapai semua keinginannya"
            },
            {
                "Nama": "Salavi Naharani",
                "NIM": "124450090",
                "Umur": "20",
                "Asal":"Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobi": "Minum air putih",
                "Sosmed": "@afi.nhr",
                "Kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh",  
                "Pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cPCW894G5bbpmmNtB3--wZJMJE94AHFs", #fabio1
            "https://drive.google.com/uc?export=view&id=1Q6_9SaCCNu68T7txIMPHEwoCk58EPEK0", #tanty2
            "https://drive.google.com/uc?export=view&id=1sejXGjqSOzajQpI_ax0UAn5LMMgU6Lia", #fadyl3
            "https://drive.google.com/uc?export=view&id=1O6sVgJ6D1VD5RLty2UwoNjNZf-SQ2tDP", #nuel4
            "https://drive.google.com/uc?export=view&id=1iiAn3yefi1s5wA-OKxGM4alU11MdgCaS", #viola5
            "https://drive.google.com/uc?export=view&id=12Rvc3EJ4FLKd_O3DUGTsAHeYGDY13IMC", #risa6
            "https://drive.google.com/uc?export=view&id=1tHZJWNC9pGABN_wgCIdVNbarGHGDV63B", #vanis7a
            "https://drive.google.com/uc?export=view&id=1Q8IihY68dunX-vtYST9ZDZ0HeBzgnXlB", #yulia8
            "https://drive.google.com/uc?export=view&id=19nIwMobYNb4dx9Leoehnkpz0jD9G2-aQ", #akeyla9
            "https://drive.google.com/uc?export=view&id=1OjUaTOlcipLL8eZnkK8H-vm0yTSrAphR", #elsa10
            "https://drive.google.com/uc?export=view&id=154RfaTTcgOIitgugm42S4Xmwe7Fp2h2p", # fadya11
            "https://drive.google.com/uc?export=view&id=1OUyGstrQvgVZhMHz1yAhAACyK5jwHE0-", #lovi12
            "https://drive.google.com/uc?export=view&id=1YoS5cfkG1dNFRYjVWoR0hOkttEO9PX4E", # asli131
            "https://drive.google.com/uc?export=view&id=1YBBKb8V2eNw0yTzCBrQ25O7QEo0WACcn", #sherena14
            "https://drive.google.com/uc?export=view&id=1UIr6yc3WFqCBHgqoCHnY2BtRK8wA-Wyj", #razin15
            "https://drive.google.com/uc?export=view&id=1Gtkz8gsfACMo4sZ7OCPWEsbnc5D0m78K", #faiza16
            "https://drive.google.com/uc?export=view&id=1seX3ZXFKTnBBrD1aAtwO26kXo9h8aK40", #gathan17
            "https://drive.google.com/uc?export=view&id=1FchSeApf0IrIFCXOXqOoq0n3tknDHMP2", #pidzy18
            "https://drive.google.com/uc?export=view&id=15bRtOQhXN0OFNGUDi3usPnOEhBVfKj9a", #kaleb19
            "https://drive.google.com/uc?export=view&id=1quPXZLaVpPU92hiCB9g5X7-lwwl5HWxV", #melva20
            "https://drive.google.com/uc?export=view&id=1G5n2J1AThSCikA4G0NJu54w4zgeN_9or", #falakh21
            "https://drive.google.com/uc?export=view&id=1eWCDBWGUb8s_rfRtSxHHXeEzutUJCuJw", #henry22
        ]
        data_list = [
            {
                "Nama": "Fabio Banyu Cyto",
                "NIM" : "12340104",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Kedaton",
                "Hobi": "Tidur",
                "Umur" : "21",
                "Sosmed" : "@biyokcb",
                "Kesan" : "Abangnya keren suka marvel.",
                "Pesan" : "Ayok nobar Doomsday bang."
            },
            {
                "Nama": "Tanty Widiyastuti",
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "Tenang dan suka memperhatikan hal-hal kecil.",
                "Pesan" : "Terus bagikan ketelitianmu ke kami, Kak."
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi",
                "NIM" : "Belum Tahu",
                "Asal" : "Bandar Lampungku",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "Permainan gitarnya bikin suasana nyaman.",
                "Pesan" : "Sering-sering hibur kami lewat musikmu, Kak."
            },
            {
                "Nama": "Manuel Frederika",
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Energik dan cepat akrab dengan siapa saja.",
                "Pesan" : "Tetap semangat dan jangan berubah, Kak."
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "NIM" : "124450005",
                "Asal" : "Bali",
                "Alamat" : "Nusa Penida",
                "Hobi": "Menghayal",
                "Umur" : "12",
                "Sosmed" : "Violaadrtr_",
                "Kesan" : "Pembawaannya kalem dan penuh imajinasi.",
                "Pesan" : "Semoga ide-idemu terus berkembang, Kak."
            },
            {
                "Nama": "Risa Romadona",
                "NIM" : "124450127",
                "Asal" : "Natar",
                "Alamat" : "Natar",
                "Hobi": "Rolling skate",
                "Umur" : "20",
                "Sosmed" : "risarmdna",
                "Kesan" : "Aktif dan berani mencoba hal baru.",
                "Pesan" : "Terus berani melangkah, Kak."
            },
            {
                "Nama": "Vannisa Ramadhani",
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Ramah dan selalu terlihat ceria.",
                "Pesan" : "Tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "Nama": "Yulia Cristine Malau",
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Sopan dan menghargai orang lain.",
                "Pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "Nama": "Akeyla Fairuz Shafi",
                "NIM" : "1234501",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Umur" : "21",
                "Sosmed" : "@keyashafi",
                "Kesan" : "Pendengar yang baik dan tidak suka menghakimi.",
                "Pesan" : "Tetap jadi teman cerita yang nyaman, Kak."
            },
            {
                "Nama": "Elsa Sitorus",
                "NIM" : "124450088",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Pemda",
                "Hobi": "Rebahan",
                "Umur" : "21",
                "Sosmed" : "_els.a",
                "Kesan" : "Murah senyum dan enak diajak bicara.",
                "Pesan" : "Tetap jadi kakak yang hangat, ya, Kak."
            },
            {
                "Nama": "Fadya Izzatul ‘Aini",
                "NIM" : "124450062",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Mancing",
                "Umur" : "20",
                "Sosmed" : "fadyaizzatul_",
                "Kesan" : "Sabar dan telaten kalau menjelaskan sesuatu.",
                "Pesan" : "Jangan bosan membimbing kami, Kak."
            },
            {
                "Nama": "Lovianora Saragih",
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Kalem tapi tetap hangat saat berinteraksi.",
                "Pesan" : "Semoga selalu dimudahkan dalam studinya, Kak."
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "NIM" : "124450092",
                "Asal" : "Kalianda",
                "Alamat" : "Kotabaru",
                "Hobi": "Main Game, Tidur",
                "Umur" : "20",
                "Sosmed" : "@aluccy_",
                "Kesan" : "Humoris dan gampang bikin tawa.",
                "Pesan" : "Jangan lupa tetap fokus kuliah juga, Kak."
            },
            {
                "Nama": "Sherena Florencia",
                "NIM" : "124450027",
                "Asal" : "Bengkulu Selatan",
                "Alamat" : "Belwis",
                "Hobi": "Make up",
                "Umur" : "19",
                "Sosmed" : "sher_renna",
                "Kesan" : "Rapi dan selalu tampil percaya diri.",
                "Pesan" : "Tetap jadi inspirasi bagi adik tingkat, Kak."
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "NIM" : "123450096",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Futsal",
                "Umur" : "21",
                "Sosmed" : "@razyn.hfd",
                "Kesan" : "Sportif dan semangat kerja samanya tinggi.",
                "Pesan" : "Terus ajak kami aktif bersama, Kak."
            },
            {
                "Nama": "Faiza Try Anjani",
                "NIM" : "124450075",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Membaca Novel",
                "Umur" : "19",
                "Sosmed" : "FAIZAANJANII",
                "Kesan" : "Tutur katanya sopan dan penuh pertimbangan.",
                "Pesan" : "Tetap jadi kakak yang bijak, Kak."
            },
            {
                "Nama": "Gathfan Nadif Ali",
                "NIM" : "124450001",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Rajabasa",
                "Hobi": "Main game",
                "Umur" : "20",
                "Sosmed" : "@gathfannadif",
                "Kesan" : "Santai tapi tetap bertanggung jawab.",
                "Pesan" : "Terus jaga keseimbangan itu, Kak."
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "NIM" : "124450064",
                "Asal" : "Metro",
                "Alamat" : "Metro Kibang, Lampung Timur",
                "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "Umur" : "20",
                "Sosmed" : "@apiszzaja_",
                "Kesan" : "Cekatan soal teknis dan mau berbagi ilmu.",
                "Pesan" : "Ajari kami ngoding dengan sabar, Kak."
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "Konsisten menjaga kebiasaan hidup sehat.",
                "Pesan" : "Tularkan semangat hidup sehatmu ke kami, Kak."
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "NIM" : "124450087",
                "Asal" : "Sumsel",
                "Alamat" : "Sukarame",
                "Hobi": "Scroll",
                "Umur" : "19",
                "Sosmed" : "@melva_fbrt",
                "Kesan" : "Ceria dan mudah menyesuaikan diri.",
                "Pesan" : "Tetap jadi pribadi yang ramah, Kak."
            },
            {
                "Nama": "Muhammad Syafiqul Falakh",
                "NIM" : "124450099",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "@syaafiqui",
                "Kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "Pesan" : "Jangan sungkan berbagi pendapat ke kami, Kak."
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "NIM" : "124450115",
                "Asal" : "Kobum",
                "Alamat" : "Rajabasa",
                "Hobi": "Lari dari kenyataan",
                "Umur" : "28",
                "Sosmed" : "henryferdianto",
                "Kesan" : "Humornya unik dan bikin suasana cair.",
                "Pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pwlw1-RTQyCiq4nq2QgMhqydzgSvQ9qX", #1
            "https://drive.google.com/uc?export=view&id=1_VUVl0HE7SrauNUqhDlKLPNvZWHCe7jZ", #2
            "https://drive.google.com/uc?export=view&id=16PEudyp5uQ8-qlL6GunHNGF56-dsy4Tu", #3
            "https://drive.google.com/uc?export=view&id=1_qNLUULhqPfEVcL00HicFs4ehd0Rsyll",#4
            "https://drive.google.com/uc?export=view&id=1QRay-KLH1xZ18GLVDfGWfEtLrKXKXtAS",#5
            "https://drive.google.com/uc?export=view&id=16mWiVWj1F025_cN2R2u6vof4Se0qWLhq",#6
            "https://drive.google.com/uc?export=view&id=1BTuryXjxBUwcdMMYZPKE4sBkmeB5yIav",#7
            "https://drive.google.com/uc?export=view&id=1oOCtU5TTASLXqa80K8pMrOQ6DXvyS0fK",#8
            "https://drive.google.com/uc?export=view&id=1QM-qIlLAtsilWfelOlCmkOkdCO3bCd6v",#9
            "https://drive.google.com/uc?export=view&id=1fg-hKxYhPqF3aUVrkp_8i1OFbzrl6qA2",#10
            "https://drive.google.com/uc?export=view&id=1cbLWm3BkymEIxv_SA4dMuCc5lR0H9NIA",#11
            "https://drive.google.com/uc?export=view&id=1cetKDpe7mka3rnWG2-aaE67rnVmxLhj5",#12
            "https://drive.google.com/uc?export=view&id=1mFD4-DN0bGInQF1e7BNzRRrWyl0AKoHZ",#13
            "https://drive.google.com/uc?export=view&id=1LBxFVZ7iSXNDMIw7ViYA3qBonXYzQbS9",#14
            "https://drive.google.com/uc?export=view&id=1HxWZXJOBp4r7rw9xJDkT1TLq1m-LuhgC",#15
            "https://drive.google.com/uc?export=view&id=1hXqTnpzj42mlNZHMGr9oG3q53ztieR2d",#16
            "https://drive.google.com/uc?export=view&id=1VedvFJejI-jcorJ4za_aT93hCfAEdUup",#17
            "https://drive.google.com/uc?export=view&id=18pyw9ooTA-T5bRluRZuP2XWM-yWHACVL",#18
            "https://drive.google.com/uc?export=view&id=1nOIwUf9F-BwMKPQiOG8VFs52Zpky2yfR",#19
            "https://drive.google.com/uc?export=view&id=1-BSmI-8O1kdwIQemA6JEaKgFgUkF_O2N",#20
            "https://drive.google.com/uc?export=view&id=1ZgVveH_LBGKcluOplOXWKdDn8ilm2cCv",#21
            "https://drive.google.com/uc?export=view&id=1xh50OuMGjLPw4vzokm7o4KWe2O7xIC20",#22
        ]
        data_list = [
            {
                "Nama": "Arini Puteri Elandra",
                "NIM": "123450069",
                "Umur": "21",
                "Asal": "LAMPUNG!!!",
                "Alamat": "Teluk Betung Selatan",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@elandraa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan - jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Khoirul Muttoharoh",
                "NIM": "123450021",
                "Umur": "21",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobi": "Main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Ahmad Rizky",
                "NIM": "124450050",
                "Umur": "21 Tahun ini alhamdulillah",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobi": "Ga ngapa ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "NIM": "124450083",
                "Umur": "cepuyuh tayun",
                "Asal": "Ikut kadep",
                "Alamat": "Love Earth",
                "Hobi": "Jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1  
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "NIM": "124450113",
                "Umur": "20",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobi": "Lihat-lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            }, 
            { 
                "Nama": "Alfaya Abiyyi",
                "NIM": "124450006",
                "Umur": "nelson piquet",
                "Asal": "Balam",
                "Alamat": "Balam",
                "Hobi": "Makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Asri Meilani",
                "NIM": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobi": "menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Bima Ekayasa",
                "NIM": "124450106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Indah Khairunnisa",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "NIM": "124450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Bebas",
                "Hobi": "Ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },  
            {
                "Nama": "Yollanda Agustina",
                "NIM": "124450024",
                "Umur": "-",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "NIM": "123450032",
                "Umur": "22",
                "Asal": "Tetangga Kadep",
                "Alamat": "Belwis",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@adityatfq",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },            
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "123450052",
                "Umur": "25",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobi": "Jadi orang baik",
                "Sosmed": "-",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal": "Sini",
                "Alamat": "Jauh Pokoknya",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
                
            }, 
            { 
                "Nama": "Danil N Fadillah",
                "NIM": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnnn05",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "124450081",
                "Umur": "20",
                "Asal": "Situlah",
                "Alamat": "Pohon mulia",
                "Hobi": "Nyari Hobi",
                "Sosmed": "@zydddddd__",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "124450093",
                "Umur": "Masih muda lah",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "-",
                "Sosmed": "@jaldii._",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobi": "Nonton thinkerbell",
                "Sosmed": "@snova.19",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "123450044",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aGSnRvsfcBPonyn-DqkR5JyZljBAcK7J",#1
            "https://drive.google.com/uc?export=view&id=17gtcaGzqMTeKD3DSL3mScDl2HCKTw-O6",#2
            "https://drive.google.com/uc?export=view&id=1_mXGO4zYm9ZVvW4YYIwQiQRCazjiVyG_",#3
            "https://drive.google.com/uc?export=view&id=1Yd-xng4VuDxGBEFbRr53J2K7Mui8D4p-",#4
            "https://drive.google.com/uc?export=view&id=1AvqApaS2w_jKmGwOP29J9LseM5-BUIHB",#5
            "https://drive.google.com/uc?export=view&id=1B_W2WfHhyqOHaay9RQAyDZeX86DFgYtH",#6
            "https://drive.google.com/uc?export=view&id=1_l2XwzCYAFZvC4DFDW5MhNg-O1BCsqMh",#7
            "https://drive.google.com/uc?export=view&id=1ulIQF9ja83yqGtQtJMatcar7hjs6a_Vl",#8
            "https://drive.google.com/uc?export=view&id=16-vam2fahIKZkfZPvRzsORnqWOGZWV1T",#9
            "https://drive.google.com/uc?export=view&id=1md5bHHNNFlKTaQ-8h2F2JVihYAkXcbYL",#10
            "https://drive.google.com/uc?export=view&id=1eUASLjBcD7Fc7r_pwK0maLhPDzlvUJ4h",#11
            "https://drive.google.com/uc?export=view&id=1GWeAtSo29_YhB8S-sJfBFCVI23AXzYZ8",#12
            "https://drive.google.com/uc?export=view&id=1qsWDLXjHAsUw5GHsiiGc2Ru1hYNtMTi-",#13
            "https://drive.google.com/uc?export=view&id=14LpdNKr9LSLhn4IUYCREbPFs5ruOMdPT",#13
            "https://drive.google.com/uc?export=view&id=11z9mp14nEGF4JkicgHnAfNcjjPL1_dU4",#14
            "https://drive.google.com/uc?export=view&id=1lj22YtU5rFV778YFcSmUc-dikLVC7keM",#15
        ]
        data_list = [
            {
                "Nama": "Haikal Fransiskus Simbolon",
                "NIM": "123450123",
                "Umur": "23",
                "Asal": "Bengkulu",
                "Alamat": "Belwis",
                "Hobi": "Merokok",
                "Sosmed": "@haikalsbln_",
                "Kesan": "Bang haikal orangnya seruu banget.",  
                "Pesan":"Semoga kedepannya bang haikal diberi kelancaran dalam segala hal."# 1
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "untung suropat",
                "Hobi": "Suka menolong orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Kak Kharisma lucuu, baikk, dan juga ramah paraaah",  
                "Pesan":"Semoga kak kharisma selalu dikelilingi dengan orang baik"# 1
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "123450038",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Sukarame",
                "Hobi": "menyapa satpam gedung f",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Kak Hanna seru, baikk, lucu ",  
                "Pesan":"Semoga semua yang kak hanna inginkan semuanyaa tercapaii, aamiin"# 1
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "NIM": "123450121",
                "Umur": "19",
                "Asal":"Kemiling",
                "Alamat": "Kemiling",
                "Hobi": "Suka motor bukan ngabers",
                "Sosmed": "@farhanghani",
                "Kesan": "Bang Farhan orangnya keren, selalu keren pas damaskus",  
                "Pesan":"Semoga bang farhan selalu diberi kelancaran dan kesehatan"
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "18",
                "Asal":"Riau",
                "Alamat": "Belwis",
                "Hobi": "Ngestalker in orang",
                "Sosmed": "@aisyahkhair",
                "Kesan": "Kak Aisyah orangnya lucuuu, dan juga asikkk sekali",  
                "Pesan":"Semoga semua apa yang kakak lakuin sekarang dan nanti diberi kelancaran"# 1
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450049",
                "Umur": "....",
                "Asal":"....",
                "Alamat": "....",
                "Hobi": "....",
                "Sosmed": "@...",
                "Kesan": "Kak Cerine orangnya sangat asikk, humble, dan juga baikk banget",  
                "Pesan":"Semoga kak cerine selalu dikelilingi orang orang baikk"# 1
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "22",
                "Asal":"kisaran city",
                "Alamat": "Pemda city",
                "Hobi": "Balap liar",
                "Sosmed": "@jay_saputra_tmb",
                "Kesan": "Bang Jaya orangnya keren, baikk, dan seru",  
                "Pesan":"Semoga bang jaya diberi kesehatan dan kelancaran dalam segala hal!"
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobi": "...",
                "Sosmed": "@...",
                "Kesan": "Kak Najla orangnya baikk, dan juga ramah sekalii",  
                "Pesan":"Semoga semua keinginan kak najla tercapi secepatnya"# 1
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "18",
                "Asal":"lampung selatan",
                "Alamat": "korpri raya",
                "Hobi": "isengin harvin di kelas",
                "Sosmed": "@rozakramdani__",
                "Kesan": "Bang Rozak orangnya asik sihh, dan juga murah senyuum",  
                "Pesan":"Semoga bang rozak didekatkan dengan hal-hal baik"# 1
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal":"riau",
                "Alamat": "belwis",
                "Hobi": "masak",
                "Sosmed": "@christiani8872",
                "Kesan": "Kak Teresa orangnya lucuu, baikk, dan juga ramahh",  
                "Pesan":"Semoga kak teresa segera mendapatkan semua keinginannya"# 1
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal":"Padang",
                "Alamat": "Perumnas Way Kandis",
                "Hobi": "Main game fps",
                "Sosmed": "@hndfzky_",
                "Kesan": "Bang Hanif orangnya baikk, dan juga asikk",  
                "Pesan":"Semoga bang hanif selalu menjadi yang terbaik"# 1
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal":"sumbar",
                "Alamat": "sukarame",
                "Hobi": "main ke air terjun",
                "Sosmed": "@audinaf_03",
                "Kesan": "Kak orangnya Audina lucuu, baikk, dan juga sangat amat ramah",  
                "Pesan":"Semoga kak audin selalu dilingkung yang memiliki hal-hal baik"# 1
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450050",
                "Umur": "20",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@Cikamrbn",
                "Kesan": "Kak Cika orangnya lucuu, baikk, dan juga asikk",  
                "Pesan":"Semoga semua keinginan kak cika tercapai secepatnyaaa"# 1
            },
            {
                "Nama": "Gustin H. Tampubolon",
                "NIM": "124450068",
                "Umur": "...",
                "Asal": "...",
                "Alamat": "...",
                "Hobi": "...",
                "Sosmed": "@...",
                "Kesan": "Kak Gustin orangnya lucuu, baikk, dan juga ramahh",  
                "Pesan":"Semoga kak gustin selalu didekat hal-hal baik"# 1
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Berkuda",
                "Sosmed": "@Muhvnz_",
                "Kesan": "Bang Harvin orangnya baiikk , dan soft spoken",  
                "Pesan":"Semoga semua keinginan bang harvin tercapai secepatnyaa"# 1
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal": "natar",
                "Alamat": "natar",
                "Hobi": "nginep di rumah kak yollanda",
                "Sosmed": "@snasha._",
                "Kesan": "Kak Sabina orangnya baikk, dan juga sangat ramahh",  
                "Pesan":"Semoga kak sabina mendapatkan hal-hal baik teruss"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18Snn1oKdKsitsRlwz7quUfyCYVvFZRhW",#1
            "https://drive.google.com/uc?export=view&id=11iI5bKwyiUGxYuEYkFaiioDkwEUwkgTu",#2
            "https://drive.google.com/uc?export=view&id=1KEDk56lw9SbaxFhBzoYIQyDpT-HKH1um",#3
            "https://drive.google.com/uc?export=view&id=1gauDKPTq3DItQBtG9XmXUrbag1JS64T9",#4
            "https://drive.google.com/uc?export=view&id=14DerUSD76-VmTyZcOrwQ_b4kMMWKKB68",#5
            "https://drive.google.com/uc?export=view&id=16vJt15Z__l3b8AJptgi6OHDgVYphpYMe",#6
            "https://drive.google.com/uc?export=view&id=10ef_OFY2BLl2bBNImxE_0vatDYCQbu8X",#7
            "https://drive.google.com/uc?export=view&id=1uFvYyJfNbf0U8mxeozTRGVBBXtx_7MVc",#8
            "https://drive.google.com/uc?export=view&id=1b5_hB69XyZtF1_eByDXVNwpiMf559JKz",#9
            "https://drive.google.com/uc?export=view&id=1EFfaBSODDOTTPY_CclvniMkh0KVHVcRi",#10
            "https://drive.google.com/uc?export=view&id=1MQxAhkpxqdRIKA0xJ42i8ZKzRuwxvD0i",#11
            "https://drive.google.com/uc?export=view&id=1Hx2w7RDqvJzYSQBLoC4KbQRxNqIXLv4O",#12
        ]
        data_list = [
            {
                "Nama": "Ihsan Maulana Yusuf",
                "NIM": "123450110",
                "Umur": "21 Tahun",
                "Asal":"Sumbar",
                "Alamat": "Belwis",
                "Hobi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "Sosmed": "@ihsan.myusuf",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Hanifah Inaya Sari",
                "NIM": "123450123",
                "Umur": "21",
                "Asal":"Balam",
                "Alamat": "Balam",
                "Hobi": "Masak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Afifah Fauziah",
                "NIM": "123450002",
                "Umur": "19",
                "Asal":"Padang",
                "Alamat": "Hasan 4",
                "Hobi": "Nonton Marvel, Tidur",
                "Sosmed": "@fifah.zy",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Hasan Nur Ramadhan",
                "NIM": "124450012",
                "Umur": "21",
                "Asal":"lampung",
                "Alamat": "Pemda",
                "Hobi": "Main game",
                "Sosmed": "@hasan.ramadhan08",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Layina Ropiqo",
                "NIM": "124450016",
                "Umur": "19 tahun",
                "Asal":"Semarang",
                "Alamat": "Balam",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@lay.inr_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Moch. Iqbal Az-Zahir",
                "NIM": "124450052",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Natar",
                "Hobi": "Mancing",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Talitha Justine",
                "NIM": "124450076",
                "Umur": "19",
                "Asal":"Sumbar",
                "Alamat": "Kelengkeng 5",
                "Hobi": "Tidur",
                "Sosmed": "@talithaaajtine",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Anadia Carana",
                "NIM": "123450019",
                "Umur": "19",
                "Asal":"Palembang",
                "Alamat": "Wayhui",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Abdillah Fikri Al pome",
                "NIM": "123450062",
                "Umur": "21",
                "Asal":"Sumsel",
                "Alamat": "Airan",
                "Hobi": "Basket",
                "Sosmed": "@pomest_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "NIM": "124450008",
                "Umur": "20",
                "Asal":"Sumbar",
                "Alamat": "Samping kost rafli",
                "Hobi": "Fishing",
                "Sosmed": "@dhal_setiawan",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Anggun Nita",
                "NIM": "124450009",
                "Umur": "20",
                "Asal":"Lampung Utara",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Della Anisa Fitri",
                "NIM": "124450095",
                "Umur": "20",
                "Asal":"Lampung Timur",
                "Alamat": "Nargo Lestari",
                "Hobi": "Olahraga, Makan makanan manis",
                "Sosmed": "@dellaansaftr",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Tb9t2b_dcmUifnpvF_MVox0TaJKdNqj_",#1
            "https://drive.google.com/uc?export=view&id=1KcWl-5wjFm0k5Izo-L_MLoZfh7dyzggE",#2
            "https://drive.google.com/uc?export=view&id=12NBOPoaRFq6asImjxkkpisQhFmgioIN7",#3
            "https://drive.google.com/uc?export=view&id=12CPbzJcUxjblIVPYGHgndjr-foRXr1WP",#4
            "https://drive.google.com/uc?export=view&id=1Sx8xVqXBnoHXPg6tZM_gnlHQp__UugBq",#5
            "https://drive.google.com/uc?export=view&id=1_S3rd5ZaYbGDwLQTB45fj8zszr_9o0He",#6
            "https://drive.google.com/uc?export=view&id=104CShPSfS42P0m3Nxbw4JKd0zNDnvx3c",#7
            "https://drive.google.com/uc?export=view&id=1_bJc2lZmV8V8C-Mlw_cpORH1IcVu138M",#8
            "https://drive.google.com/uc?export=view&id=1XLMJkdjtqBIlRigeT2Zu4qklW3RSVQ0Z",#9
            "https://drive.google.com/uc?export=view&id=1cYNf6aXyQH4_K7NVt8zVsPzfgDxH0BU7",#10
            "https://drive.google.com/uc?export=view&id=1ShdRkJxC3O9oHmv9WUfz2eDvXXPC7iy8",#11
            "https://drive.google.com/uc?export=view&id=1VOUaaVNAwFApOoT2w-QI7Vgui5H3Zjo9",#12
            "https://drive.google.com/uc?export=view&id=1pomRbvK276Q1n0YqgbX3-tn3fDULyoYr",#13
            "https://drive.google.com/uc?export=view&id=1GYwsonnDm-iwMC7mDyqlm3UbjgztjvgH",#14
            "https://drive.google.com/uc?export=view&id=1QzPRS629mDk5iev93gR_jaii_-Z5Nrcl",#15
            "https://drive.google.com/uc?export=view&id=11KsCpHqgIP0HcSIUoJn43kH-aTIvASlC",#16
            "https://drive.google.com/uc?export=view&id=1PUZIF0gNX0L5XDlkBNpmBNX_FMLgHXuC",#17
            "https://drive.google.com/uc?export=view&id=1L_nH2YccTcl8il3lpjnRQxEKuz0wr1n4",#18
        ]
        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "NIM": "123450082",
                "Umur": "20",
                "Asal":"Payakumbuh, Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Musingin TA",
                "Sosmed": "@naylAsalsabilaa._",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": " Donna Maya Puspita",
                "NIM": "123450028",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Way Huwi",
                "Hobi": " Berenang",
                "Sosmed": "@donNamaya.p",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Labo John Noel Napitupulu",
                "NIM": "123450037",
                "Umur": "20",
                "Asal": "Jakpus, Medan, Palembang",
                "Alamat": " Way Huwi",
                "Hobi": " Tong setan",
                "Sosmed": "@noerruuu",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "NIM": "124450050",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobi": "Nonton F1",
                "Sosmed": "@anshtsyaaql",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "NIM": " 124450104",
                "Umur": "18",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobi": "Mancing",
                "Sosmed": "@ felisyanbl__",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "NIM": "124450031",
                "Umur": "18",
                "Asal": "Rumah",
                "Alamat": "Ryacudu",
                "Hobi": " Bully Felisya Nabila Nugroho",
                "Sosmed": "@muh_razan_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "NIM": "123450086",
                "Umur": "21",
                "Asal":"karawang",
                "Alamat": "Airan",
                "Hobi": "nongkrong depan ruang prodi",
                "Sosmed": "@saniayyllstr",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Allisha",
                "NIM": "124450019",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukabumi",
                "Hobi": "Gebuk Snare",
                "Sosmed": "@aallishaa.a",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Alya Ramadhanti",
                "NIM": "124450091",
                "Umur": "19",
                "Asal": "Jambi",
                "Alamat": "Airan",
                "Hobi": "Jalan jalan dengan sepatu rodaku",
                "Sosmed": "@ alya.rmdhnti",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "NIM": "124450097",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Pemda",
                "Hobi": "Belajar",
                "Sosmed": "@bungaclrssf",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Raihana Adelia Putri",
                "NIM": "123450041",
                "Umur": "20",
                "Asal":"Terbanggi Besar",
                "Alamat": "Airan Raya 1",
                "Hobi": "menulis, membaca",
                "Sosmed": "@n1tg._",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Nazlah Aulia",
                "NIM": "124450054",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Memanah",
                "Sosmed": "@nzlhauly",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Difanya Husakina",
                "NIM": " 124450043",
                "Umur": "Gada yang tau",
                "Asal": "Rumah bapak ",
                "Alamat": "Gedung F",
                "Hobi": "Ngitungin beras di karung",
                "Sosmed": "@difanyhsa_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "NIM": "124450061",
                "Umur": "21",
                "Asal": "Surabaya",
                "Alamat": "Sukarame",
                "Hobi": "nyuluh manuk",
                "Sosmed": "@daffascript_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "NIM": "124450098",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Scroll fesnuk",
                "Sosmed": "@edsel_0712",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": " Lucia Advencia Rachel Nainggolan",
                "NIM": " 124450085",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobi": " Mencintai Andrew Garfield",
                "Sosmed": "@ luciarachel_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "NIM": "124450124",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobi": "Ngoding",
                "Sosmed": "@_shaazzh",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "NIM": "124450112",
                "Umur": "19",
                "Asal": "Jabung",
                "Alamat": "Rajabasa",
                "Hobi": "bobo",
                "Sosmed": "@Xifasky",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

if menu == "Departemen Minbak":
    def minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Y4zQRAz0nZlVdQUaXUAcL-jnCnlXCm5M",#1
            "https://drive.google.com/uc?export=view&id=1yO_bG0KqM4He6qpJEo99j5YsfZ8f3gpk",#2
            "https://drive.google.com/uc?export=view&id=1eMKC81LAD_dfHviLGgOuyqyBXOl3YJIt",#3
            "https://drive.google.com/uc?export=view&id=11RUp65LWA8nkUasCOpBoeLsJtyjK0GlF",#4
            "https://drive.google.com/uc?export=view&id=1utvC8yM0rf6JqE6LTX5OtDqA6aK5-13h",#5
            "https://drive.google.com/uc?export=view&id=1Mch3363oasnQ3bdyrBPVLVzAsxWqSfg2",#6
            "https://drive.google.com/uc?export=view&id=1ETJbFI_gPTntNZXl5Hcad17j6XOGUcGL",#7
            "https://drive.google.com/uc?export=view&id=1gi6KGeDoJ1LRzvpWQMDQRRlkqyVUSB55",#8
            "https://drive.google.com/uc?export=view&id=1TwZy6jMQmd8fL71ZzcaIz7qU9HUyhvWn",#9
            "https://drive.google.com/uc?export=view&id=1ZbMmEb-W4XUq1BzrzWNG0ZU5BW3wp2AS",#10
            "https://drive.google.com/uc?export=view&id=1snvbh_IBFF1uxL2e4xR1v40kEoKG8OtE",#11
            "https://drive.google.com/uc?export=view&id=10wrgQJwB-X0ObAq8m1Csy_FnlTwYLBBQ",#12
            "https://drive.google.com/uc?export=view&id=1Onpnfc3--I9CFxYXqaLrwQ3QukaNV5F-",#13
            "https://drive.google.com/uc?export=view&id=1pSkNWYTnXwakyL4HVinyEhhmv6OLsang",#14
            "https://drive.google.com/uc?export=view&id=1O77bEY9W0-Ckb9Eg4LhMO-jjrPd9WPbw",#15
        ]
        data_list = [
            {
                "Nama": "Kevin Antonio Junior",
                "NIM": "123450109",
                "Umur": "23",
                "Asal": "Sulawesi Tengah",
                "Alamat": "Panjang",
                "Hobi": "Mancing",
                "Sosmed": "@kevinaja__",
                "Kesan": "Sangat menginspirasi dan memimpin dengan baik",
                "Pesan": "Semangat terus kak!"
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "NIM": "123450046",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Way Dadi",
                "Hobi": "Mendaki",
                "Sosmed": "@ferazkaa",
                "Kesan": "Sangat rapi dan cekatan dalam mengelola administrasi",
                "Pesan": "Sukses selalu kak!"
            },
            {
                "Nama": "Ali Aristo Muthahhari Parisi",
                "NIM": "123450088",
                "Umur": "21",
                "Asal": "Lampung Timur",
                "Alamat": "Gang Sakum Belwis",
                "Hobi": "Nonton F1",
                "Sosmed": "@ali_parisi3",
                "Kesan": "Keren dan selalu memberikan arahan yang jelas",
                "Pesan": "Semangat menjalankan tugasnya kak!"
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "NIM": "124450058",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Airan",
                "Hobi": "Belajar + menghitung uang",
                "Sosmed": "@aayuandriani_",
                "Kesan": "Sangat ramah dan aktif berkontribusi",
                "Pesan": "Tetap semangat dan sukses terus!"
            },
            {
                "Nama": "Dafa Elpriza",
                "NIM": "124450131",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Way Kandis",
                "Hobi": "Jogging",
                "Sosmed": "@dafaelpriza_",
                "Kesan": "Sangat menyenangkan dan mudah diajak kerja sama",
                "Pesan": "Sukses terus perkuliahan dan aktivitasnya!"
            },
            {
                "Nama": "Juwita Sari",
                "NIM": "124450066",
                "Umur": "19",
                "Asal": "Lampung Barat",
                "Alamat": "Pemda",
                "Hobi": "Mancing",
                "Sosmed": "@ju.juwitaaa_",
                "Kesan": "Sangat baik dan murah senyum",
                "Pesan": "Semangat terus kuliahnya!"
            },
            {
                "Nama": "Muhammad Afdal Luthfi",
                "NIM": "124450047",
                "Umur": "19",
                "Asal": "Lampung Tengah",
                "Alamat": "Jl. Pulau Damar",
                "Hobi": "Memantau dl tugas",
                "Sosmed": "@afdall.03",
                "Kesan": "Sangat bertanggung jawab dan fokus",
                "Pesan": "Semangat terus kakak!"
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "NIM": "124450002",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Korpri",
                "Hobi": "Nongkrong di kopken",
                "Sosmed": "@slbnzw_",
                "Kesan": "Sangat asik dan ceria",
                "Pesan": "Tetap semangat kuliahnya ya kak!"
            },
            {
                "Nama": "Muhammad Ridwan",
                "NIM": "123450091",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Belwis",
                "Hobi": "Badminton",
                "Sosmed": "@mridwaan_22",
                "Kesan": "Sangat mengayomi dan membimbing dengan sabar",
                "Pesan": "Semangat terus memimpin divisinya kak!"
            },
            {
                "Nama": "Andra Ilham Bintang",
                "NIM": "124450060",
                "Umur": "18",
                "Asal": "Sumatera Selatan",
                "Alamat": "Kotabaru",
                "Hobi": "Main rubik",
                "Sosmed": "@andra.lhm",
                "Kesan": "Sangat kreatif dan pintar",
                "Pesan": "Sukses selalu kuliahnya!"
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "NIM": "124450003",
                "Umur": "20",
                "Asal": "Nias",
                "Alamat": "Belwis",
                "Hobi": "Live tiktok",
                "Sosmed": "@bryantel_",
                "Kesan": "Sangat menghibur dan ramah",
                "Pesan": "Semangat terus berkarya kak!"
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "NIM": "124450067",
                "Umur": "17",
                "Asal": "Surabaya",
                "Alamat": "Kemiling",
                "Hobi": "Nanem Sawit",
                "Sosmed": "@meardhy_ghiyats",
                "Kesan": "Sangat unik dan bersemangat",
                "Pesan": "Tetap semangat dan sukses selalu!"
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "NIM": "124450055",
                "Umur": "20",
                "Asal": "Pringsewu",
                "Alamat": "Airan",
                "Hobi": "Bengong",
                "Sosmed": "@indahjuliaa",
                "Kesan": "Sangat baik dan bersahabat",
                "Pesan": "Sukses terus perkuliahannya kak!"
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "NIM": "124450023",
                "Umur": "18",
                "Asal": "Kalimantan Barat",
                "Alamat": "Korpri",
                "Hobi": "Nyapu depan gacoan",
                "Sosmed": "@cacalvra",
                "Kesan": "Sangat ceria dan menyenangkan",
                "Pesan": "Semangat terus ya kak!"
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "NIM": "124450089",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Kotabaru",
                "Hobi": "Bangun pagi",
                "Sosmed": "@muhammdrafka_",
                "Kesan": "Sangat disiplin dan dapat diandalkan",
                "Pesan": "Sukses selalu buat perkuliahannya!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    minbak()
# Tambahkan menu lainnya sesuai kebutuhan
