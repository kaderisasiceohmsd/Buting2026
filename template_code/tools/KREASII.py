from tools.ui_helper import inject_custom_css, load_image
from tools.game_helper import render_flappy

inject_custom_css()

TIM = {
    "Dyla": "https://drive.google.com/uc?export=view&id=...",
    "Wawa": "https://drive.google.com/uc?export=view&id=...",
    "Anoy": "https://drive.google.com/uc?export=view&id=...",
    "Juju": "https://drive.google.com/uc?export=view&id=...",
    "Anya": "https://drive.google.com/uc?export=view&id=...",
    "Ting Ting": "https://drive.google.com/uc?export=view&id=...",
    "Luigi": "https://drive.google.com/uc?export=view&id=...",
    "Chela": "https://drive.google.com/uc?export=view&id=...",
    "Esha": "https://drive.google.com/uc?export=view&id=1hAAeT7e210klEia-RmuhE2TYtI2vsO4G",
    "Alip": "https://drive.google.com/uc?export=view&id=...",
    "Ia": "https://drive.google.com/uc?export=view&id=...",
    "Oni": "https://drive.google.com/uc?export=view&id=..."
        
}
render_flappy({nama: load_image(url, fallback_name=nama) for nama, url in TIM.items()})