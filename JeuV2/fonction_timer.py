
import tkinter.font as font
import etat_jeu as ej
jeu = ej.etat

def controle_time(canva, racine, mobyn = 0) :
    if mobyn == 0 :
        temps_max = jeu["temps_max_atk"] # en ms
    if mobyn == 1 : 
        temps_max = ej.dico_mob[ej.lst_mob[jeu["mob_en_cours"]]]["temps_atk"]
    zoom = jeu["zoom"]
    jeu["qte_en_cour"] = True
    if jeu["timer"] == 0 :
        canva.create_rectangle (210*zoom, 500*zoom, 910*zoom, 520*zoom, fill = "#ffffff", tags = ("combat", "barre_timer"))
        canva.create_rectangle (210*zoom, 500*zoom, 910*zoom, 520*zoom, fill = "grey", tags = "combat")
    if jeu["timer"] >= temps_max :
        police = font.Font(size = 22, weight = "bold")
        jeu["timer"] = 0
        canva.delete("fleche")
        jeu["qte_en_cour"] = False
        return
    else :
        jeu["timer"] += jeu["f_rappel"]
        canva.delete("barre_timer")
        if jeu["timer"] <= temps_max - 1000 :
            couleur_util = "#ffffff"
        else :
            couleur_util = "red"
        canva.create_rectangle (210*zoom, 500*zoom, (910 - 700*(jeu["timer"]/temps_max))*zoom, 520*zoom, fill = couleur_util, tags = ("combat", "barre_timer"))
        racine.after(jeu["f_rappel"], lambda : controle_time(canva, racine, mobyn))