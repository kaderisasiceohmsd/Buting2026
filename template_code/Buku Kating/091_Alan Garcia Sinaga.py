import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

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
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1erwcdW2OSk2EHluafxh7g_sq0Rh9jnPo",
            "https://drive.google.com/uc?export=view&id=1KYhvRbnMIO0S2S4FSm5lvo5qEaFoc23Z",
            "https://drive.google.com/uc?export=view&id=17er9A0OVeDNNyJCFLd7xrBklWmnzGi5T",
            "https://drive.google.com/uc?export=view&id=1EJrwajIoDoLCzc0sOAYtv1qGDaZIHzH4",
            "https://drive.google.com/uc?export=view&id=1BcFZFrEuzuTjZ6V0xtOspubiKB-8XY7s",
            "https://drive.google.com/uc?export=view&id=1A3Zo9AZjmoIjguZqVU5-nMUrjPTzUrro",
            
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Bang Ginda berwibawa sekali,nampak banget aura sibuk nya.",  
                "pesan":"Semangat nge TA sambil mengkepalai Himpunan bg."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil juga ga kalah keren! Btw,aku mulet terinspirasi dari bg aqil.",  
                "pesan":"semangat terus kuliah nya bg,tetap jadi orang keren!!!"# 2
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya baik banget meski jarang ketemu, tapi kakaknya selalu ramah dan welcome banget",  
                "pesan":"Semangat terus kuliah nya kak!"# 3
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois orangnya humble banget, ramah.Nampaknya si sedikit pendiam hehe",  
                "pesan":"Semangat Nge TA nya ka!"# 4
            },
            {
                "nama": "Luthfia Laila Rahmadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Keliling Balam",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya baik banget dan humble, ramah juga,lihat kakanya seperti melihat uang",  
                "pesan":"Semangat terus kuliah nya kak!"# 5
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu lulu",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya baik,pokoknya keren banget deh, ramah juga",  
                "pesan":"Semangat kuliah dan menjaga uangnya ka heheh"# 6
            },                      
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xX5xZzfgo0YDPwwbrSFrKi7lgwQ-kVdv",
            "https://drive.google.com/uc?export=view&id=1UEY6eUBmefJnUdzEjQxLi0IfDgssihvW",
            "https://drive.google.com/uc?export=view&id=1gNBesG19vBN49uRG74sQxz-nJIs_2Nw_",
            "https://drive.google.com/uc?export=view&id=1kNQ86zfTja8MzETJjXG4OmcXAJoISPvk",
            "https://drive.google.com/uc?export=view&id=1D6Hb2IVfecYJ_rOLMZtnQWJs7Klocg4E",
            "https://drive.google.com/uc?export=view&id=1AJzdcl_Xw1anSBzkBjUew6wIRzyMiwpA",
            "https://drive.google.com/uc?export=view&id=1NMMz0q0yNyR9L231OIzcTtqQuuxKv7DX",
            "https://drive.google.com/uc?export=view&id=19_9PyVwtj51UW1ymFD2vr39hu5o7JXhy",
            "https://drive.google.com/uc?export=view&id=11oFbrtdVUOQkH4vJkCP89U7xLPYr8ux2",
            "https://drive.google.com/uc?export=view&id=1A3Zo9AZjmoIjguZqVU5-nMUrjPTzUrro",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya cantik, baik, kalem, keren,wanita paling berwibawa yang pernah aku temui",
                "pesan": "Sehat selalu kak, semoga lancar skripsinya"
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Tanya Bapas",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Abangnya seru, asik, lucu,dan sudah pernah satu divisi di natal Sains Data",
                "pesan": "Semangat terus bang Helmy,semoga makin jago Gitarannya"
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Abangnya baik, asik, dan king nya badminton di Data",
                "pesan": "Semoga selalu dimudahkan bang Fernando,kapan kapan sparing ya bang"
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kota Baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "Kakaknya asik,sudah pernah jadi partner mc di sains data mengabdi",
                "pesan": "Sehat selalu ya kak,terima kasih ilmu mc nyaa kak"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Abangnya asik, keren, pinter juga pastinya,dan abang ini kasra lantaiku dulu.",
                "pesan": "Sehat selalu bang, semangat terus menjaga asrama bg"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia,h_264",
                "kesan": "Kakaknya lucu,ramah,asik,dan cantik banget wkwk",
                "pesan": "Semoga kuliahnya lancar ya kak"
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasi Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakak mentor aku.Kalau Messi itu pemain bola terbaik,kalau ka Aqila ini mentor terbaik sepanjang masa. Kakak ini baik banget,dan asik banget pastinya.",
                "pesan": "Semoga segala hal berjalan baik untuk kakak,semoga kakak selalu sehat dan bahagia,semoga kuliahnya lancar kak,semoga semakin bersinar seperti bunga matahari kakak,dan jangan lupa sama dodol-dodol kakak ini yaa ka."
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Giring Ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abangnya keren, asik juga",
                "pesan": "Semoga sukses bang"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakaknya cantik, ramah, baik",
                "pesan": "Semangat terus kak, semoga kuliahnya lancar"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca Buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Sehat selalu dan semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Badan Legislatif":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_iPcLG7nq0NQxMILOrG9J1O8RTB1hfft",
            "https://drive.google.com/uc?export=view&id=18cXKrXhO_wKD-3xjp2OIe3GIdgeFk1MQ",
            "https://drive.google.com/uc?export=view&id=134yZZFcwQmIdUx985QuEeYWDopslWUaC",
            "https://drive.google.com/uc?export=view&id=1q-ne5XjrI4e3VlVcIWBD3oDooBQoQ8H-",
            "https://drive.google.com/uc?export=view&id=1at8AOga0Jh9_vTDeiuKmbiedcT4_txbI",
            "https://drive.google.com/uc?export=view&id=1564Ps6ViL9QSKOjaAOg53z_38o6M_eKs",
            "https://drive.google.com/uc?export=view&id=1fYdwn3qmDYrwkoWDnlO08b5ljmnqtKF6",
            "https://drive.google.com/uc?export=view&id=1PquoD8A9Rz_UszUm5tbWM_Q3aTfdlO73",
            "https://drive.google.com/uc?export=view&id=1fkPiFGyy4CbEyUWXMWxKcjHtAdENmS7T",
            "https://drive.google.com/uc?export=view&id=1cQNoI6KdUxFqNDrDD6ByHZl0obbjrQg3",
            "https://drive.google.com/uc?export=view&id=1Dy5278ma_6FlXsF2oglR5pEeiPHbWtIm",
            "https://drive.google.com/uc?export=view&id=1G-9WncVzkXmhDTO0PHCiL-qQ0eCeh6Xm",
            "https://drive.google.com/uc?export=view&id=19AtJbFz5XshQH4p15O6Midzekb65WOUI",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal": "Kuala lumpur",
                "alamat": "GH",
                "hobbi": "Bernyanyi",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho orangnya asik banget, to the point dan penjelasan yang di kasih mudah dipahami",  
                "pesan":"Semoga kedepannya abang selalu diberi kelancaran dalam segala hal , dan diberi kesehatan, terimakasih bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue orangnyaaa asik banget, lucuu, penyampaian tentang Balegnya juga mudah dipahami",  
                "pesan":"Semoga Kedepannya kak jue selalu diberi kelancaran dalam segala hal, dan juga selalu diberikan kesehatan, Terimakasih kak"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa orangnya baik, humble, kenal kak nisa udah dari semester satu, kak nisa orangnya sangat sangat bertanggung jawab.",  
                "pesan":"Semoga kedepannya kak nisa selalu diberikan kelancaran dalam segala hal ya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya asik banget, vibes-nya bikin betah belajar. Kalau ngajarin jangan bosen-bosen ya, Bang, soalnya ilmu dari bang dharu masih banyak yang mau fadyl serap,wkwkkwk.",
                "pesan": "Semangat terus kuliahnya, Bang! Semoga tugas lancar, nilai aman, dan rezeki mengalir deras. Jangan lupa bahagia bang!"
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal": "Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Mikael orangnya humble dan asik, auranya presidiumnya kenceng banget.",
                "pesan": "Semoga kuliahnya lancar terus, dan semoga diberi kesehatan dan kelancaran dalam segala hal ya Bang! "
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro orangnya asik, penjelasan yang bang givaro kasih jujur mudah banget dipahami",
                "pesan": "Semoga kuliahnya lancar, Bang! Semoga kopinya selalu enak, dompetnya selalu aman, dan hidupnya jauh dari deadline dadakan."
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal": "City Earth",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya asik dan ramah. keliatan soft spoken banget",  
                "pesan":"Semoga kedepannya kak hani selalu diberi kesehatan dan kelancaran dalam segala hal yaa kak ."# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremia orangnya asik, dan humble parah.",  
                "pesan":"Semoga Kedepannya Abang selalu diberikan kelancaran dan Kesehatan ya bang."# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jona orangnya lucu paraaah, seruuu, dan juga suka sharing biskuat kalau abangnya lagi jadi operator.",  
                "pesan":"semangat terus kuliahnya bang, sehat selaluuu ya bang, SUKSEEES !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica orangnya murah senyum, baik dan lucu",  
                "pesan":"semangat terus kuliahnya kakak, semoga sehat selaluuu"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Sekar orangnya baik banget, humble, dan tegas, tapi perhatian",  
                "pesan":"semangat terus kuliahnya kak, dan sehat selaluu ya kak."# 1
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kakaknya baik dan seru, jujur syok pas tau kakaknya orang palembang jugaa.",
                "pesan": "Semoga kuliahnya lancar terus, Kak! Semoga nanti saya bisa nyicip pempek buatan kakak :)"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya seruuu asik dan humbleee banget.",  
                "pesan":"semangat terus kuliahnya kak, dan sehat selaluu ya kak."# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


# PSDA
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bfeoLdTPLcR84j0tNaTIqoQScIAn-5M3",
            "https://drive.google.com/uc?export=view&id=1MgV1KtBTwKLl5xlQdQyEA_YrUeYCPqd3",
            "https://drive.google.com/uc?export=view&id=1atakdZfVuFQkbAtu2immCu27wQiWa2f9",
            "https://drive.google.com/uc?export=view&id=1824Ysb1cab3IV7sruKTcHn5pa-sZywYN",
            "https://drive.google.com/uc?export=view&id=1WbKnDhWcWL39GyfmIzSCFfdQxnpm6r6j",
            "https://drive.google.com/uc?export=view&id=19DOs7BzUsgjhNp1gXFWdaGS97ESEeMWk",
            "https://drive.google.com/uc?export=view&id=1LzgnhSE97uGtMW3VjKdTGyhGpfx_mzMc",
            "https://drive.google.com/uc?export=view&id=1VrpVJsvnTq3LYi4ckm6OT7rxznPIoqSF",
            "https://drive.google.com/uc?export=view&id=13SfsKaXDnZipnQK9CBCrSpHWD_8RdgjU",
            "https://drive.google.com/uc?export=view&id=1f9QHeWyzKSCN9WgGpFQtkIWjbnAirdYD",
            "https://drive.google.com/uc?export=view&id=1_PngtFGyHyVKgwnEoNeuFsljMk0drPq4",
            "https://drive.google.com/uc?export=view&id=1AEO2eUsPD3vTiVh2AgRcLESynTJ62T5B",
            "https://drive.google.com/uc?export=view&id=10x1T3fQYlKnTg71xnh2z0ohgcA6Qex1Z",
            "https://drive.google.com/uc?export=view&id=19dwnIzMegc3Uh8mbOTa3CPzLug2LwXs1",
            "https://drive.google.com/uc?export=view&id=1St8VoUGESYZYqWElikgyDRDi33zjTuR2",
            "https://drive.google.com/uc?export=view&id=1cbG84MOmaMX4yVEtpN1K_itP0TnBzUAT",
            "https://drive.google.com/uc?export=view&id=1viKl2p9qwDDPJoINHVrJj1HB-83TGNn_",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal": "Pinggir Pantai",
                "alamat": "Samping Kost Capo",
                "hobbi": "Ngerjain Anak Kader",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arienta orangnya baik, dan juga ramahh",  
                "pesan":"Semoga semua keinginan kak arienta sgera tercapai"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany orangnya humble, dan baik juga",  
                "pesan":"Semoga kak vany mencapai semua keinginannya secepatnya, salam dari orang sesama palembang"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel orangnya kerenn, Tegas,dan juga baiik",  
                "pesan":"Semoga bang nobel selalu diberi kelancaran dan kesehatan dalam segala hal."# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal": "Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi orangnya kerenn, to the point dan juga baikk",  
                "pesan":"Semoga semua keinginan bang azmi cepat tercapaii"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang Ayake orangnyaa humble , kerenn, Tegas dan baikk",  
                "pesan":"Semoga bang ayake diberi kelancaran dalam segala hal dan semoga selalu diberi kesehatan"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar orangnya kereen, Tegas dan Humble",  
                "pesan":"Semoga bang caesar diberi kesehatan dan kelancaran"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Euodia orangnya seru, Tegas , dan juga baikk,",  
                "pesan":"Semoga kak euodia selalu didekatkan hal-hal baikk"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal orangnya kerenn, Tegas ,baikk, dan juga ramahh",  
                "pesan":"Semoga bang haikal mencapai semua hal yang bang haikal inginkan"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450029",
                "umur": "18",
                "asal": "Depok",
                "alamat": "Oiya Cefa",
                "hobbi": "Jalan kaki gaboleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri orangnya baikk, humble dan juga ramah",  
                "pesan":"Semoga semua keinginan kak putri segera terwujud"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@quenntanaabilaa",
                "kesan": "Kak Queenta orangnya baik, humble, dan perhatian",  
                "pesan":"Semoga kak queenta selalu bisa mencapai keinginannya"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "23",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman orangnya kerenn, dan juga asikk, baikk",  
                "pesan":"Semoga bang desman selalu didekat hal-hal baikk"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel orangnya humble, dan juga baikkk sekali",  
                "pesan":"Semoga semua keinginan kak azzel tercapai"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah orangnya baikk, dan juga ramah",  
                "pesan":"Semoga kak charlindah dikelilingi hal-hal baik"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jemar orangnya kerenn apalagi saat damaskus",  
                "pesan":"Semoga bang jeremi bisa menggapai semua keinginannya"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa",  
                "pesan":"Semoga kak nabila mendapatkan hal-hal yang diinginkan"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearrfkvmfl",
                "kesan": "Bang Rafli orangnya humble , baik, dan juga ramah",  
                "pesan":"Semoga bang rafli selalu bisa mencapai semua keinginannya"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh",  
                "pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K-BWBGPPPaX3Oj6uyr3JKQuqzFzeyeJb",
            "https://drive.google.com/uc?export=view&id=1CU2bPjPbr_QMto1Fi9qM-Ii99TUJy0nb",
            "https://drive.google.com/uc?export=view&id=1piJ-EMgPPFY_qTlbzAzwdeV4Oc29u4lO",
            "https://drive.google.com/uc?export=view&id=1xQ4iu8VVktxap2ESyBsaDEXDb6vViERM",
            "https://drive.google.com/uc?export=view&id=1LMT3puy9pZR0auxHN8G6nm1w3S3GX2-N",
            "https://drive.google.com/uc?export=view&id=1VJiK9Rd4Irp7vDpavxWYI5TS_ZKCz3Eb",
            "https://drive.google.com/uc?export=view&id=1ReLlGv2VIiTlNt8F8VBm8VtbRxi1ftfC",
            "https://drive.google.com/uc?export=view&id=1UxlZ-MyAVjtIlwjpLJM0ehiugkaG9cwI",
            "https://drive.google.com/uc?export=view&id=1_5YrgGvHBhmxY2uRh4zSG1IjWZaaUJQe",
            "https://drive.google.com/uc?export=view&id=1oqDLqcZWo73Tg3eVpXWvzuJoRnfHZY1T",
            "https://drive.google.com/uc?export=view&id=10qUhDsA5q3ivgW-B2B1eg1vfPKZnsxKg",
            "https://drive.google.com/uc?export=view&id=10QjP2upeOtr40APRjPEOMy8nHiAe7JHP",
            "https://drive.google.com/uc?export=view&id=1H3XrhHc8VlwpmR4WrAmlefifblUsUUka",
            "https://drive.google.com/uc?export=view&id=1aLEdJRahrMGbrzCs4i-I4IcVkfdWm-KX",
            "https://drive.google.com/uc?export=view&id=17dwiMCh8nSMufTS36AKTz2p-JuBzIbsw",
            "https://drive.google.com/uc?export=view&id=1CnRAaty2SAD0HWb_VZE1R6vxknV-BACO",
            "https://drive.google.com/uc?export=view&id=1EgRDUQXT8fFYhlWYBJqYZFQBTuxY6isL",
            "https://drive.google.com/uc?export=view&id=1HGpd9n1-lhZ3z3TapAF_eg4KhydYVfV3",
            "https://drive.google.com/uc?export=view&id=1zxrAoSo7ijtdQHIhB-4hRddjej873QiP",
            "https://drive.google.com/uc?export=view&id=1VLjUzeo8rZCyEWhraMlBTyBoRjD-hXv0",
            "https://drive.google.com/uc?export=view&id=1roXyKLX_IgiA2q0Q6EH_oNhu0mfmPxgv",
            "https://drive.google.com/uc?export=view&id=1dRPhhJzyOsddkwe4GPklStCdciBi8zG9",
        ]

        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim" : "12340104",
                "asal" : "Bandar Lampung",
                "alamat" : "Kedaton",
                "hobbi": "Tidur",
                "umur" : "21",
                "sosmed" : "@biyokcb",
                "kesan" : "Abangnya keren suka marvel.",
                "pesan" : "Ayok nobar Doomsday bang."
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim" : "123450094",
                "asal" : "Lampung",
                "alamat" : "Airan Raya",
                "hobbi": "Membaca",
                "umur" : "21",
                "sosmed" : "@tvnty_",
                "kesan" : "Tenang dan suka memperhatikan hal-hal kecil.",
                "pesan" : "Terus bagikan ketelitianmu ke kami, Kak."
            },
            {
                "nama": "Fadil Prasetyo Alfaritzi",
                "nim" : "Belum Tahu",
                "asal" : "Bandar Lampungku",
                "alamat" : "Bandar Lampung",
                "hobbi": "Gitar",
                "umur" : "21",
                "sosmed" : "@fadilalfarizzii",
                "kesan" : "Permainan gitarnya bikin suasana nyaman.",
                "pesan" : "Sering-sering hibur kami lewat musikmu, Kak."
            },
            {
                "nama": "Manuel Frederika",
                "nim" : "124450039",
                "asal" : "Batam",
                "alamat" : "Way Kandis",
                "hobbi": "Tenis meja",
                "umur" : "20",
                "sosmed" : "@manuelfdk_",
                "kesan" : "Energik dan cepat akrab dengan siapa saja.",
                "pesan" : "Tetap semangat dan jangan berubah, Kak."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim" : "124450005",
                "asal" : "Bali",
                "alamat" : "Nusa Penida",
                "hobbi": "Menghayal",
                "umur" : "12",
                "sosmed" : "Violaadrtr_",
                "kesan" : "Pembawaannya kalem dan penuh imajinasi.",
                "pesan" : "Semoga ide-idemu terus berkembang, Kak."
            },
            {
                "nama": "Risa Romadona",
                "nim" : "124450127",
                "asal" : "Natar",
                "alamat" : "Natar",
                "hobbi": "Rolling skate",
                "umur" : "20",
                "sosmed" : "risarmdna",
                "kesan" : "Aktif dan berani mencoba hal baru.",
                "pesan" : "Terus berani melangkah, Kak."
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim" : "124450078",
                "asal" : "Kepulauan Riau",
                "alamat" : "Teluk Betung",
                "hobbi": "Nonton KHW",
                "umur" : "19",
                "sosmed" : "@vunnycaa",
                "kesan" : "Ramah dan selalu terlihat ceria.",
                "pesan" : "Tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "nama": "Yulia Cristine Malau",
                "nim" : "Belum Tahu",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "Belum Tahu",
                "kesan" : "Sopan dan menghargai orang lain.",
                "pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim" : "1234501",
                "asal" : "Bandar Lampung",
                "alamat" : "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "umur" : "21",
                "sosmed" : "@keyashafi",
                "kesan" : "Pendengar yang baik dan tidak suka menghakimi.",
                "pesan" : "Tetap jadi teman cerita yang nyaman, Kak."
            },
            {
                "nama": "Elsa Sitorus",
                "nim" : "124450088",
                "asal" : "Sumatera Utara",
                "alamat" : "Pemda",
                "hobbi": "Rebahan",
                "umur" : "21",
                "sosmed" : "_els.a",
                "kesan" : "Murah senyum dan enak diajak bicara.",
                "pesan" : "Tetap jadi kakak yang hangat, ya, Kak."
            },
            {
                "nama": "Fadya Izzatul Aini",
                "nim" : "124450062",
                "asal" : "Pringsewu",
                "alamat" : "Airan",
                "hobbi": "Mancing",
                "umur" : "20",
                "sosmed" : "fadyaizzatul_",
                "kesan" : "Sabar dan telaten kalau menjelaskan sesuatu.",               
                "pesan" : "Jangan bosan membimbing kami, Kak."
            },
            {
                "nama": "Lovianora Saragih",
                "nim" : "124450105",
                "asal" : "Sumatera Utara",
                "alamat" : "Way Huwi",
                "hobbi": "Dengerin Musik",
                "umur" : "19",
                "sosmed" : "_loviaa",
                "kesan" : "Kalem tapi tetap hangat saat berinteraksi.",
                "pesan" : "Semoga selalu dimudahkan dalam studinya, Kak."
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim" : "124450092",
                "asal" : "Kalianda",
                "alamat" : "Kotabaru",
                "hobbi": "Main Game, Tidur",
                "umur" : "20",
                "sosmed" : "@aluccy_",
                "kesan" : "Humoris dan gampang bikin tawa.",
                "pesan" : "Jangan lupa tetap fokus kuliah juga, Kak."
            },
            {
                "nama": "Sherena Florencia",
                "nim" : "124450027",
                "asal" : "Bengkulu Selatan",
                "alamat" : "Belwis",
                "hobbi": "Make up",
                "umur" : "19",
                "sosmed" : "sher_renna",
                "kesan" : "Rapi dan selalu tampil percaya diri.",
                "pesan" : "Tetap jadi inspirasi bagi adik tingkat, Kak."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim" : "123450096",
                "asal" : "Padang",
                "alamat" : "Belwis",
                "hobbi": "Futsal",
                "umur" : "21",
                "sosmed" : "@razyn.hfd",
                "kesan" : "Sportif dan semangat kerja samanya tinggi.",
                "pesan" : "Terus ajak kami aktif bersama, Kak."
            },
            {
                "nama": "Faiza Try Anjani",
                "nim" : "124450075",
                "asal" : "Padang",
                "alamat" : "Belwis",
                "hobbi": "Membaca Novel",
                "umur" : "19",
                "sosmed" : "FAIZAANJANII",
                "kesan" : "Tutur katanya sopan dan penuh pertimbangan.",
                "pesan" : "Tetap jadi kakak yang bijak, Kak."
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim" : "124450001",
                "asal" : "Bandar Lampung",
                "alamat" : "Rajabasa",
                "hobbi": "Main game",
                "umur" : "20",
                "sosmed" : "@gathfannadif",
                "kesan" : "Santai tapi tetap bertanggung jawab.",
                "pesan" : "Terus jaga keseimbangan itu, Kak."
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim" : "124450064",
                "asal" : "Metro",
                "alamat" : "Metro Kibang, Lampung Timur",
                "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "umur" : "20",
                "sosmed" : "@apiszzaja_",
                "kesan" : "Cekatan soal teknis dan mau berbagi ilmu.",
                "pesan" : "Ajari kami ngoding dengan sabar, Kak."
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim" : "124450053",
                "asal" : "Bandar Lampung",
                "alamat" : "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "umur" : "20",
                "sosmed" : "@kelelep_comberan",
                "kesan" : "Konsisten menjaga kebiasaan hidup sehat.",
                "pesan" : "Tularkan semangat hidup sehatmu ke kami, Kak."
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim" : "124450087",
                "asal" : "Sumsel",
                "alamat" : "Sukarame",
                "hobbi": "Scroll",
                "umur" : "19",
                "sosmed" : "@melva_fbrt",
                "kesan" : "Ceria dan mudah menyesuaikan diri.",
                "pesan" : "Tetap jadi pribadi yang ramah, Kak."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim" : "124450099",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "@syaafiqui",
                "kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "pesan" : "Jangan sungkan berbagi pendapat ke kami, Kak."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim" : "124450115",
                "asal" : "Kobum",
                "alamat" : "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "umur" : "28",
                "sosmed" : "henryferdianto",
                "kesan" : "Humornya unik dan bikin suasana cair.",
                "pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()


if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12XoIWTrEbd78PVO_pkh2rlQRTN4rqZcJ",
            "https://drive.google.com/uc?export=view&id=1PhtBOSKo0HKx7JJbGuN9R-2oK_tFdCeG",
            "https://drive.google.com/uc?export=view&id=1P3FvUBN8egEX8d76DOhLVriHr7cxnl9O",
            "https://drive.google.com/uc?export=view&id=1hlqv8VSh93vfr7iPzmbQvCU_sMcANXWo",
            "https://drive.google.com/uc?export=view&id=1XIseKqKErK63WTfboQGiOWFUFAiptZfJ",
            "https://drive.google.com/uc?export=view&id=1AYtjOHCGXWeBjwhfbKlVN2BPxAn8qyGW",
            "https://drive.google.com/uc?export=view&id=1g8kyjJp11lSFKJXYPAfQe5q_mYxFuAje",
            "https://drive.google.com/uc?export=view&id=148IPzn8eGkxLF_mK0A0hE0L2CcVvRA5K",
            "https://drive.google.com/uc?export=view&id=1TuJrqmU2-TNDJS-IRHBqtZjeEkPR9676",
            "https://drive.google.com/uc?export=view&id=113Q-WHA0W5yRasDc3-EYDE94aIyoKy4X",
            "https://drive.google.com/uc?export=view&id=1fbo7jnYKU09E5oq30C9ofTV33czs9IMN",
            "https://drive.google.com/uc?export=view&id=1n2IjM653m0LO2J-dMV77MJ6wuS-D5OaB",
            "https://drive.google.com/uc?export=view&id=1Y4brYTTmY88XHVxHZKbOLCOv1hMfXElJ",
            "https://drive.google.com/uc?export=view&id=1BlUmSUdX8pEKsEtQXxaG-YiIPVsm4E7W",
            "https://drive.google.com/uc?export=view&id=1-F0Toruv7FwRnNDXJAuTlOZluLSTpVzV",
            "https://drive.google.com/uc?export=view&id=1Em42LwmmqsdJA0iHISJQQ2PxrpxFCqh1",
            "https://drive.google.com/uc?export=view&id=1ETzfcISbFZHQgjJnrg-EtgDUSL5zeifT",
            "https://drive.google.com/uc?export=view&id=1KzLg-U13HBMlHCJ83vnBJBqZYVpdlUUO",
            "https://drive.google.com/uc?export=view&id=13pgw3qDKKOXy094EHCmMu75f1GsOeuS_",
            "https://drive.google.com/uc?export=view&id=1BGSdirqm4KH5z6lsd7J1yUOuaZNi-ovj",
            "https://drive.google.com/uc?export=view&id=1rpni-yakf3atLMDlConsaANhaL15ftQm",
        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "21",
                "asal": "LAMPUNG!!!",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "124450050",
                "umur": "21 Tahun ini alhamdulillah",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Love Earth",
                "hobbi": "Jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1  
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat-lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }, 
            { 
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },  
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing Keributan",
                "sosmed": "@adityatfq",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },            
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh Pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
                
            }, 
            { 
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "Pohon mulia",
                "hobbi": "Nyari Hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "-",
                "sosmed": "@jaldii._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UDW1zfCEo3QeE90YpY9_XwSyytOstH7_",
            "https://drive.google.com/uc?export=view&id=1U5oqjgWhSPrXXy7zzDeAuc-Y6KKjtUNW",
            "https://drive.google.com/uc?export=view&id=1JLYzOdoNs9wsyomEyAFoZveQFQJ4kAE1",
            "https://drive.google.com/uc?export=view&id=1ixgB4z8bmQVfc3-R_16gbUGpGqtmo8q0",
            "https://drive.google.com/uc?export=view&id=15En31ghDdk6wESP8t-7HwUVjoKyw9ee_",
            "https://drive.google.com/uc?export=view&id=1YDFyH46GQRZiDKAtzi5hZN0hRQ3myW3k",
            "https://drive.google.com/uc?export=view&id=1Br6mpshKHlmg6lJIgxDj5pLy3rY7P0Ub",
            "https://drive.google.com/uc?export=view&id=1VOy94Y_KM5PnXT7ijv-OliQcYUwCWoLO",
            "https://drive.google.com/uc?export=view&id=1Fy4T8QEQjb3_-X_kRAOXqEp1ZZ6bCWB1",
            "https://drive.google.com/uc?export=view&id=1R7N3shNrPVCj0IN773Qbefha2U8aREaI",
            "https://drive.google.com/uc?export=view&id=1iDVzuBn8oZPxBJK2GkTwzvSg-BHMxDSv",
            "https://drive.google.com/uc?export=view&id=1_jM8LMhzRZD-3Mp_wxytd52Y7UzdHVB-",
            "https://drive.google.com/uc?export=view&id=1OWz0XtiMBUv5gu10ca2rLmRbixqSfQ7o",
            "https://drive.google.com/uc?export=view&id=1sBVcmh-ZVV1JSKVUHxscaVmd3C7zH7wu",
            "https://drive.google.com/uc?export=view&id=1k9hH3BEjMw74VFScqh61MLvP4wOFKE9l",
            "https://drive.google.com/uc?export=view&id=1wjLddHAoU9gR4t_yO7vcZHdHwY7-ga63",
        ]
        data_list = [
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450123",
                "umur": "23",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Merokok",
                "sosmed": "@haikalsbln_",
                "kesan": "Bang haikal orangnya seruu banget.",  
                "pesan":"Semoga kedepannya bang haikal diberi kelancaran dalam segala hal."# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma lucuu, baikk, dan juga ramah paraaah",  
                "pesan":"Semoga kak kharisma selalu dikelilingi dengan orang baik"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna seru, baikk, lucu ",  
                "pesan":"Semoga semua yang kak hanna inginkan semuanyaa tercapaii, aamiin"# 1
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan orangnya keren, selalu keren pas damaskus",  
                "pesan":"Semoga bang farhan selalu diberi kelancaran dan kesehatan"
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak Aisyah orangnya lucuuu, dan juga asikkk sekali",  
                "pesan":"Semoga semua apa yang kakak lakuin sekarang dan nanti diberi kelancaran"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "....",
                "asal":"....",
                "alamat": "....",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "Kak Cerine orangnya sangat asikk, humble, dan juga baikk banget",  
                "pesan":"Semoga kak cerine selalu dikelilingi orang orang baikk"# 1
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya orangnya keren, baikk, dan seru",  
                "pesan":"Semoga bang jaya diberi kesehatan dan kelancaran dalam segala hal!"
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak Najla orangnya baikk, dan juga ramah sekalii",  
                "pesan":"Semoga semua keinginan kak najla tercapi secepatnya"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"lampung selatan",
                "alamat": "korpri raya",
                "hobbi": "isengin harvin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "Bang Rozak orangnya asik sihh, dan juga murah senyuum",  
                "pesan":"Semoga bang rozak didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"riau",
                "alamat": "belwis",
                "hobbi": "masak",
                "sosmed": "@christiani8872",
                "kesan": "Kak Teresa orangnya lucuu, baikk, dan juga ramahh",  
                "pesan":"Semoga kak teresa segera mendapatkan semua keinginannya"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Bang Hanif orangnya baikk, dan juga asikk",  
                "pesan":"Semoga bang hanif selalu menjadi yang terbaik"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"sumbar",
                "alamat": "sukarame",
                "hobbi": "main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kak orangnya Audina lucuu, baikk, dan juga sangat amat ramah",  
                "pesan":"Semoga kak audin selalu dilingkung yang memiliki hal-hal baik"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kak Cika orangnya lucuu, baikk, dan juga asikk",  
                "pesan":"Semoga semua keinginan kak cika tercapai secepatnyaaa"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak Gustin orangnya lucuu, baikk, dan juga ramahh",  
                "pesan":"Semoga kak gustin selalu didekat hal-hal baik"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Bang Harvin orangnya baiikk , dan soft spoken",  
                "pesan":"Semoga semua keinginan bang harvin tercapai secepatnyaa"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "nginep di rumah kak yollanda",
                "sosmed": "@snasha._",
                "kesan": "Kak Sabina orangnya baikk, dan juga sangat ramahh",  
                "pesan":"Semoga kak sabina mendapatkan hal-hal baik teruss"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KtXyg2KyvsXBErR8Sf7BVwK5cWzEt8jp",
            "https://drive.google.com/uc?export=view&id=1o0lfXsNPNhEDaIY-zRcWpJPoX5doD8-X",
            "https://drive.google.com/uc?export=view&id=1jFpeb4u-lwAPbMlYU8Y3dIz9Afbedo0x",
            "https://drive.google.com/uc?export=view&id=1knOClFLdzto3Kyy1rhxtkhNFLKU6H1Hu",
            "https://drive.google.com/uc?export=view&id=1NlEj5wMWmHiVCaKqRag1DKx0Z6Bgq6Xq",
            "https://drive.google.com/uc?export=view&id=1jTFXyGOLCFG90e6PX_pMHlN61ti8k8iI",
            "https://drive.google.com/uc?export=view&id=1NlEj5wMWmHiVCaKqRag1DKx0Z6Bgq6Xq",
            "https://drive.google.com/uc?export=view&id=1ps1rcyrZDI9a1_RVD0rfpdE_KNoywiYs",
            "https://drive.google.com/uc?export=view&id=12hymD1uz4sqjEYdti3r5I0Y93jDuWyhu",
            "https://drive.google.com/uc?export=view&id=1YX9SYNSd71vVROf9cyM-bwuEHWkRMQ7D",
            "https://drive.google.com/uc?export=view&id=1KsV_F9C7u_7SRdZyGEO80JEqJZMqWtji", 
            "https://drive.google.com/uc?export=view&id=19BZmt6qEEE3N9orRTsQA1USNyDJJO9lT",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21 Tahun",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal": "lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal": "Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oMTwLxqIaWp_qrsBQR7cuWOl3MxwHNsi",
            "https://drive.google.com/uc?export=view&id=1sCNOmxnzLu16WRYUa5O-sO1lQr_nPPaw",
            "https://drive.google.com/uc?export=view&id=1_eJU59tzPHesQruuX3fxhl-GHXFRiIMc",
            "https://drive.google.com/uc?export=view&id=1r9oKQSjElSCtAtCF7vSF_P1EypzO05yu",
            "https://drive.google.com/uc?export=view&id=1wCusvCcjKDn0psiMoOxMjNk4m_rjQJcX",
            "https://drive.google.com/uc?export=view&id=1pYR_q4aUT6P0xYKPTqavsa2VBbTeJk7t",
            "https://drive.google.com/uc?export=view&id=1BtV6cXvp1O0g7D5DFGWQoYF_9cdEob__",
            "https://drive.google.com/uc?export=view&id=1xK4r721fkFc3pMCOV73t4j1xvrnWgBzN",
            "https://drive.google.com/uc?export=view&id=1sC-lJ9aU-cZ_T1OkmESFPLncUw-cwdXe",
            "https://drive.google.com/uc?export=view&id=1Y_TAKrLxtbbLms9wiU_NEMAAKXn9u1UE",
            "https://drive.google.com/uc?export=view&id=19pzp1O5fwZZ_WUBUCOO_4q7oVQ_oYP5b",
            "https://drive.google.com/uc?export=view&id=1RowqUGSBgzg0iPUplifS9L_fD0wCdOkC",
            "https://drive.google.com/uc?export=view&id=1rnfrZTZ7kbM1DhP1vlhNUysI-lpROSPm",
            "https://drive.google.com/uc?export=view&id=1cPl-oAZhP3A9qku27R8WRmdWGHQgAlqP",
            "https://drive.google.com/uc?export=view&id=1qzmuhkBit2hGfB9jorIV_RX8OspXXkHT",
            "https://drive.google.com/uc?export=view&id=1hFKAKMr2UMqxi7T43ZSNAQolUlIkZpN1",
            "https://drive.google.com/uc?export=view&id=1oRpcrPdbLTL7n8z_B2dhD5S-1IjSGFDi",
            "https://drive.google.com/uc?export=view&id=1IUhTebMSmdEkzAtEAzC0HV3ngj--hwzm",
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylAsalsabilaa._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": " Berenang",
                "sosmed": "@donNamaya.p",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": " Way Huwi",
                "hobbi": " Tong setan",
                "sosmed": "@noerruuu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": " 124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@ felisyanbl__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": " Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal": "karawang",
                "alamat": "Airan",
                "hobbi": "nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukabumi",
                "hobbi": "Gebuk Snare",
                "sosmed": "@aallishaa.a",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@ alya.rmdhnti",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nazlah Aulia",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memanah",
                "sosmed": "@nzlhauly",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": " 124450043",
                "umur": "Gada yang tau",
                "asal": "Rumah bapak ",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "nyuluh manuk",
                "sosmed": "@daffascript_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll fesnuk",
                "sosmed": "@edsel_0712",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Lucia Advencia Rachel Nainggolan",
                "nim": " 124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": " Mencintai Andrew Garfield",
                "sosmed": "@ luciarachel_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Pemda",
                "hobbi": "Ngoding",
                "sosmed": "@_shaazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "bobo",
                "sosmed": "@Xifasky",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },    
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

if menu == "Departemen Minbak":
    def minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15W17dEyb-v1hSFaYlv5Dv_P-wFGGBF9g",
            "https://drive.google.com/uc?export=view&id=1RHpw7ryMsOMwMopyqqQvzgeENaEag3O0",
            "https://drive.google.com/uc?export=view&id=1ja9fNTnss5ZJxaVvp_6fD_OXLhoErB4b",
            "https://drive.google.com/uc?export=view&id=1f4m1abuyDW7hiY-_cN6tG16Ezp0jq1W7",
            "https://drive.google.com/uc?export=view&id=1YgJLjn1PUQDQHItLyk_mIYe4otVubnUv",
            "https://drive.google.com/uc?export=view&id=1ZKHTy-U119e1EzoR669g4d17XyI6Y2Y9",
            "https://drive.google.com/uc?export=view&id=1b-0b-63w6qIKUsibm_I1wPBQ9FS8kDEz",
            "https://drive.google.com/uc?export=view&id=1-4MYdUhnuEdzP-4Pbg0i5c86O2ih-QUi",
            "https://drive.google.com/uc?export=view&id=1d0qHI5JivsZSDXPyO-7Kh5C4V60hAhRm",
            "https://drive.google.com/uc?export=view&id=1fBDO2ke1DU23EJ-UeHPZia9bNGaQrkPw",
            "https://drive.google.com/uc?export=view&id=1-jGOT72fb07ubgOPueI6h2_1mAtPIDGd",
            "https://drive.google.com/uc?export=view&id=1r0o81bVM41kJSW9oyaPTBHVOnCFESNlk",
            "https://drive.google.com/uc?export=view&id=1LaGOlqx7aNOqwr8w9O34vElmZklyrX08",
            "https://drive.google.com/uc?export=view&id=1KmwR97fsP9gARlDQAT5A_k7UcUhQD74u",
            "https://drive.google.com/uc?export=view&id=1YyE9zNqBr_7Av3ULgg7nqJx7B9_qZvyL",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "23",
                "asal": "Sulawesi Tengah",
                "alamat": "Panjang",
                "hobbi": "Mancing",
                "sosmed": "@kevinaja__",
                "kesan": "Sangat menginspirasi dan memimpin dengan baik",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Sangat rapi dan cekatan dalam mengelola administrasi",
                "pesan": "Sukses selalu kak!"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Keren dan selalu memberikan arahan yang jelas",
                "pesan": "Semangat menjalankan tugasnya kak!"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar + menghitung uang",
                "sosmed": "@aayuandriani_",
                "kesan": "Sangat ramah dan aktif berkontribusi",
                "pesan": "Tetap semangat dan sukses terus!"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Jogging",
                "sosmed": "@dafaelpriza_",
                "kesan": "Sangat menyenangkan dan mudah diajak kerja sama",
                "pesan": "Sukses terus perkuliahan dan aktivitasnya!"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Mancing",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Sangat baik dan murah senyum",
                "pesan": "Semangat terus kuliahnya!"
            },
            {
                "nama": "Muhammad Afdal Luthfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Jl. Pulau Damar",
                "hobbi": "Memantau dl tugas",
                "sosmed": "@afdall.03",
                "kesan": "Sangat bertanggung jawab dan fokus",
                "pesan": "Semangat terus kakak!"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Nongkrong di kopken",
                "sosmed": "@slbnzw_",
                "kesan": "Sangat asik dan ceria",
                "pesan": "Tetap semangat kuliahnya ya kak!"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Sangat mengayomi dan membimbing dengan sabar",
                "pesan": "Semangat terus memimpin divisinya kak!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal": "Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Main rubik",
                "sosmed": "@andra.lhm",
                "kesan": "Sangat kreatif dan pintar",
                "pesan": "Sukses selalu kuliahnya!"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live tiktok",
                "sosmed": "@bryantel_",
                "kesan": "Sangat menghibur dan ramah",
                "pesan": "Semangat terus berkarya kak!"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Sangat unik dan bersemangat",
                "pesan": "Tetap semangat dan sukses selalu!"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "Sangat baik dan bersahabat",
                "pesan": "Sukses terus perkuliahannya kak!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Sangat ceria dan menyenangkan",
                "pesan": "Semangat terus ya kak!"
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Kotabaru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Sangat disiplin dan dapat diandalkan",
                "pesan": "Sukses selalu buat perkuliahannya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    minbak()

# Tambahkan menu lainnya sesuai kebutuhan


    




# Tambahkan menu lainnya sesuai kebutuhan


    




# Tambahkan menu lainnya sesuai kebutuhan
