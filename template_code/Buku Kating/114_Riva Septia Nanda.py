import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import pandas as pd

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
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
            st.write(f"Hobi: {data_list[i]['hobi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
SPREADSHEET_ID = "19QttcdKavxnCs-ai2SciOPLSvLfNEexUYrxM8nhlJ-s"

@st.cache_data(ttl=60)
def ambil_data_sps(nama_sheet):
    url = (
        "https://docs.google.com/spreadsheets/d/"
        + SPREADSHEET_ID
        + "/gviz/tq?tqx=out:csv&sheet="
        + requests.utils.quote(nama_sheet)
    )

    df = pd.read_csv(url)
    df = df.fillna("")
    df.columns = df.columns.str.strip().str.lower()

    return df.to_dict(orient="records")

if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oo2dHEi4cKrrFuqrmoH_WBhpKL0jQzJp",
            "https://drive.google.com/uc?export=view&id=1glm6d2JTebdMyFl6jB1_0-_p40texPg1",
            "https://drive.google.com/uc?export=view&id=1Rf57oK1k4nMnvONnFr8lJOibRhG0O0LK",
            "https://drive.google.com/uc?export=view&id=1_z-LJw6rUhur9UcEk4IxyVHE98ahqBI7",
            "https://drive.google.com/uc?export=view&id=1opjjWbVuvYm8WUPSjUN8qRskJqjJnPfK",
            "https://drive.google.com/uc?export=view&id=1rm36l_1tTEAmt5hLlvep5EeNGf7tPtwS",
        ]
        data_list = ambil_data_sps("Kesekjenan")
        
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1C6hd0z2yKfgkW-6CSB0E9eJI9qiWp2mX",
            "https://drive.google.com/uc?export=view&id=1bL1O8AP1RKh0Qx8wgN8ElUYyO4EergFM",
            "https://drive.google.com/uc?export=view&id=1Th9c6oukLc8aWxYOonmt-8ZfZ8hduA1F",
            "https://drive.google.com/uc?export=view&id=1Y4VdYjpINET0WNLqOan8JRt4_0jFe3Iq",
            "https://drive.google.com/uc?export=view&id=1f_DkcgqoRIe-R7f8lMnxtt2xiABS1rIO",
            "https://drive.google.com/uc?export=view&id=1oH-2KFGVYJpJTgWJ5rzX_SQ5tqiAW_Pc",
            "https://drive.google.com/uc?export=view&id=1wyN5jkQvwtvIKAY7CYG63D3Dhv99PTdX", #1
            "https://drive.google.com/uc?export=view&id=1PS0Glqg4WrUKgeF1nsEMpM7JIwu6YXX7",
            "https://drive.google.com/uc?export=view&id=114SxAKeyMUaUgTSQZoM3xyVMsYnES0FV",
            "https://drive.google.com/uc?export=view&id=18kQOlCFHGLwAI_pzXI1F3TQDD5nQtBs3",
            "https://drive.google.com/uc?export=view&id=1wyN5jkQvwtvIKAY7CYG63D3Dhv99PTdX", #1 
            "https://drive.google.com/uc?export=view&id=15rb66HPbp0mKP-Us-oSrPJJ2FgaBNr3T",
            "https://drive.google.com/uc?export=view&id=15UGyigsmy5wl_bMAoSVG_YoKWqBSJz63",
        ]
        data_list = ambil_data_sps("Baleg")

        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fvch54WFUi25gz552kes9Q1XQiC7WG4a",
            "https://drive.google.com/uc?export=view&id=1cJ9c7QFQZs4J34D7YvYe-d7S597Bxyi8",
            "https://drive.google.com/uc?export=view&id=1tP0SkIstIT8_Di2BnGHrl1NVxnVZSDmM",
            "https://drive.google.com/uc?export=view&id=138t_tAqA-1m7q0EJ6jA71tmbPByj65xn",
            "https://drive.google.com/uc?export=view&id=1ByKc-8NLZC4LoxkPZd2UvPW3x_UHreYZ",
            "https://drive.google.com/uc?export=view&id=1-k3XndQFEwqEbCRIGObU1wn5R9t0sVrm",
            "https://drive.google.com/uc?export=view&id=1Vx8sQqEcornGubWYJqW3o5EDSP4hU9eq", 
            "https://drive.google.com/uc?export=view&id=15n8yEv-TQjluVPLD5gZgJdKA5Vf8g08P",
            "https://drive.google.com/uc?export=view&id=12Eqm2SqaP0OTWDw9hsrT9Vsae_vczVr7",
            "https://drive.google.com/uc?export=view&id=1C39RbgMRYKF7YyVwAU7dnuS3_sV1I4aY",
        ]
        data_list = ambil_data_sps("Senator")

        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen SSD":
    def departemen_ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17pXV9gmQiCLnUS2XT5k8EcftBmkiiZFz",
            "https://drive.google.com/uc?export=view&id=1wyN5jkQvwtvIKAY7CYG63D3Dhv99PTdX", #1
            "https://drive.google.com/uc?export=view&id=1RV5zOQ7-CFehK-iUmeYVKrBcV3lucgAq",
            "https://drive.google.com/uc?export=view&id=15b7FJuWvwIe7FWYreidGsAQ9qvK4gXQX",
            "https://drive.google.com/uc?export=view&id=1-e8ErgawiyitDN_aVur7vgCg_1PI8BJD",
            "https://drive.google.com/uc?export=view&id=10vDGyYK-gy5XcGY8OLFVDzR3rCbj_7XW",
            "https://drive.google.com/uc?export=view&id=1I-pLP73PtigoMb4LiSK8X0DAvhZkOE2J", 
            "https://drive.google.com/uc?export=view&id=1f08QLd8d0u0EJKfh20782xhBvx0MzZc8",
            "https://drive.google.com/uc?export=view&id=1kWoQ7_1KqkYV6m_2Vbj4MAIKsqbH8qDV",
            "https://drive.google.com/uc?export=view&id=1tjViOzm4t0pdZ3gOkOj0IVEtFm3bQyaU",
            "https://drive.google.com/uc?export=view&id=1JFFX4jJS0HhwwVix6_YDd4jNpsADU4rB",
            "https://drive.google.com/uc?export=view&id=1eVo1OsDWrQzAJtAYsGilcCghNeCm1fnn",
           
        ]
        data_list = ambil_data_sps("Departemen SSD")

        display_images_with_data(gambar_urls, data_list)
    departemen_ssd()

if menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xebnOudRMPzPvmU4n9Nopw5o2eLxCNNO",
            "https://drive.google.com/uc?export=view&id=1wyN5jkQvwtvIKAY7CYG63D3Dhv99PTdX", #1
            "https://drive.google.com/uc?export=view&id=1JFxHzb08AinyO0j20muxpaK0TzPB8-_y",
            "https://drive.google.com/uc?export=view&id=1kR9Btj1CZIQ9Lk9f3pLxBSSxclPblPA4",
            "https://drive.google.com/uc?export=view&id=1cGfL0AlXCoqPUmr8ZeZZ9TWcAVtRNAie",
            "https://drive.google.com/uc?export=view&id=1uQiakCbE1eSiTTijHtoUVZ9s_023tG05",
            "https://drive.google.com/uc?export=view&id=1PeRBIKs160n_zfIh1yGvPVxW8t0NRmDc", 
            "https://drive.google.com/uc?export=view&id=1uw7pwFmQqsYhhJ9E-sWw_AFjk-JZPVY4",
            "https://drive.google.com/uc?export=view&id=1wyN5jkQvwtvIKAY7CYG63D3Dhv99PTdX", #1
            "https://drive.google.com/uc?export=view&id=1VBysj7IbKI1aglJ3X9GWzL72QZJSwHlq",
            "https://drive.google.com/uc?export=view&id=12bgXAN3JdzW1y7OWa7PZ2-suT_mZBLMb",
            "https://drive.google.com/uc?export=view&id=1L1XsWhg2L3sgPya5toZaaz2ZJdHMfWzD",
            "https://drive.google.com/uc?export=view&id=1fvhS9OjfnIdWTEZR3vmIJBkO-D4gCjJa",
            "https://drive.google.com/uc?export=view&id=1UemdV-jdmqtGvVlRC8oFnQ4zMdY4XVHo",
            "https://drive.google.com/uc?export=view&id=1BNbrTlF2oVBFTjBxeb6jGQoNR7L-q75S",
            "https://drive.google.com/uc?export=view&id=1orIhH1ExbV85W60Yjnvfv88uY2b7vd3k",
        
        ]
        data_list = ambil_data_sps("Departemen Internal")

        display_images_with_data(gambar_urls, data_list)
    departemen_internal()

if menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FYOZsInYqTbmMiEyrNXOvtvtxSjwQp8I",
            "https://drive.google.com/uc?export=view&id=1Gj0tdeq8eMO57g27tTl2IYcTG2TgmTFT",
            "https://drive.google.com/uc?export=view&id=14Rv_jiHL2IEOOSQnVz1KNt9hWGQxmv30", 
            "https://drive.google.com/uc?export=view&id=1wyN5jkQvwtvIKAY7CYG63D3Dhv99PTdX", #1
            "https://drive.google.com/uc?export=view&id=1B2YJKMKZIrJzoxBVYXITtSCFlHW3t5qm", 
            "https://drive.google.com/uc?export=view&id=1wyN5jkQvwtvIKAY7CYG63D3Dhv99PTdX", #1
            "https://drive.google.com/uc?export=view&id=1nEW-yqIL4aFbqaoo3gS2iF3cKREq_xKz", 
            "https://drive.google.com/uc?export=view&id=1mVW2p8w9ZqMknQIHYET6B9nGLqUQWApR", 
            "https://drive.google.com/uc?export=view&id=1RCvX3-wO58o9KYco_0FNNtWXiX3d6up5", 
            "https://drive.google.com/uc?export=view&id=175jBAcijJjrxRpOPdoCey95dE6-4E-9X", 
            "https://drive.google.com/uc?export=view&id=1tCsvweutNgYoD760LZdtJcKwQitgeBvw", 
            "https://drive.google.com/uc?export=view&id=1xZhT4V4GTOGUGNYnialJgG68Zta5ErFB", 
            "https://drive.google.com/uc?export=view&id=1pLYNjXFbZov6__zVnh2YWHt9yLpDzRDE", 
            "https://drive.google.com/uc?export=view&id=1vvGukK0m75nvTr7ErQp8adgX17wyA53M", 
            "https://drive.google.com/uc?export=view&id=1wyN5jkQvwtvIKAY7CYG63D3Dhv99PTdX", #1
            "https://drive.google.com/uc?export=view&id=1A6wiwUEAPrBXWU58fP7XVyYz8ep4byEA", 
            "https://drive.google.com/uc?export=view&id=1ec4_TC4bSYZgSb0_ryzG7yPADw7kIAET", 
            "https://drive.google.com/uc?export=view&id=1dUcUOJoJsBliNekHJU52at0N85S_GlWy", 
            "https://drive.google.com/uc?export=view&id=1EFKodN1EG01xt3uIRRh95oZmKFgUamka", 
            "https://drive.google.com/uc?export=view&id=1KMdacBKU4DyG_Etav1evlzL9sltkxqpd", 
            "https://drive.google.com/uc?export=view&id=1oB8HBDZj57PyD6gRBjHYgszej1g3oR-E", 
            "https://drive.google.com/uc?export=view&id=1gkSBvxEVWhMe90eIYxqR0ShhzjyyqJq0",       
        ]
        data_list = ambil_data_sps("Departemen Internal")

        display_images_with_data(gambar_urls, data_list)
    departemen_internal()