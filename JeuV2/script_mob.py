import tkinter as tk
import os
from PIL import Image, ImageTk


def victime(canva, zoom, x, y):
    scale = 2.5  # 60 * 2.5 ≈ 150

    def r(x1, y1, x2, y2, color):
        canva.create_rectangle(
            (x + x1*scale) * zoom,
            (y + y1*scale) * zoom,
            (x + x2*scale) * zoom,
            (y + y2*scale) * zoom,
            outline=color,
            fill=color,
            tags=("combat", "mob")
        )

    # Haut
    r(12, 0, 17, 5, "white")
    r(18, 0, 23, 5, "white")
    r(24, 0, 29, 5, "white")
    r(30, 0, 35, 5, "white")
    r(36, 0, 41, 5, "white")
    r(42, 0, 47, 5, "white")
    r(48, 0, 53, 5, "white")

    # Côtés
    r(6, 6, 11, 11, "white")
    r(54, 6, 59, 11, "white")

    # Centre
    r(0, 12, 5, 17, "red")
    r(54, 12, 59, 17, "white")

    # Corps
    r(6, 18, 11, 23, "white")
    r(12, 18, 17, 23, "white")
    r(18, 18, 23, 23, "white")
    r(24, 18, 29, 23, "white")
    r(30, 18, 35, 23, "white")
    r(36, 18, 41, 23, "white")
    r(42, 18, 47, 23, "white")
    r(48, 18, 53, 23, "white")

    # Bas
    r(12, 24, 17, 29, "white")
    r(42, 24, 47, 29, "white")

    # Pieds
    r(12, 30, 17, 35, "red")
    r(42, 30, 47, 35, "red")


def gary(canva, zoom, x, y) :
    BASE_DIR = os.path.dirname(__file__)
    gary_cat = os.path.join(BASE_DIR, "Image", "gary.png")

    gary_cat = Image.open(gary_cat).convert("RGBA")
    gary_cat = gary_cat.resize((int(150*zoom), int(150*zoom)), Image.NEAREST)

    gary_cat = ImageTk.PhotoImage(gary_cat)
    canva.gary_cat = gary_cat

    canva.create_image(x*zoom, y*zoom, image=gary_cat, tags="combat")