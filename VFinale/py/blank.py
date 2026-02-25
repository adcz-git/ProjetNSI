import tkinter as tk
import bar_vie as bar

root = tk.Tk()
root.title (" On verra bien ")
root.geometry (f"{int(1140)}x{int(650)}")

canva_jeu = tk.Canvas (root, width = 1120, height = 630, bg = "#000000")
canva_jeu.place (x = 10, y = 10)

bar.dessin_bar_vie(canva_jeu)

root.mainloop()