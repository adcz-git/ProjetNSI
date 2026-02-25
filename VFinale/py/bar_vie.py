import tkinter as tk
import etat_jeu as ej
jeu = ej.etat
import tkinter.font as font

def dessin_bar_vie (canva) :
    zoom = jeu["zoom"]

    canva.delete("bar_vie")

    # Aiguille
    canva.create_rectangle (80*zoom, 55*zoom, 230*zoom, 65*zoom, fill = "grey", tags = "bar_vie")
    canva.create_oval (20*zoom, 20*zoom, 100*zoom, 100*zoom, fill = "grey", tags = "bar_vie")
    canva.create_oval (40*zoom, 40*zoom, 80*zoom, 80*zoom, fill = "#000000", tags = "bar_vie")

    # Point de vie
    for i in range (jeu["pv"]) :
        canva.create_rectangle ((102 + 12*i)*zoom, 45*zoom, (112 + 12*i)*zoom, 75*zoom, fill = "white", tags = "bar_vie")

    if jeu["pv"] <= 0 :
        zoom = jeu["zoom"]
        
        canva.delete("player")
        jeu["lst_mob"] = []
        
        police = font.Font(size = 112, weight = "bold")
        canva.create_rectangle (0, 0, 1120*zoom, 630*zoom, fill = "#000000")
        canva.create_text ( 550*zoom, 300*zoom, text = "Game Over", fill = "#FFFFFF",  font = police)