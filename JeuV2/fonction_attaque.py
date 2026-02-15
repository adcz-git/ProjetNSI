import etat_jeu as ej
jeu = ej.etat
import tkinter as tk
import qte_atk as pat
import combat
import tkinter.font as font

import fonction_timer as ft

def attaque_joueur (canva, racine) :
    canva.delete("menu_action")
    jeu["timer"] = 0
    ft.controle_time(canva, racine)
    racine.after(100)

def attaque_mob (canva, racine) :
    jeu["timer"] = 0
    ft.controle_time(canva, racine, 1)
    dessin_qte(canva)
    attaque_input(canva, racine)

def attaque_input(canva, racine) :

    trad_coul = {"violet" : "purple", "bleu" : "blue", "vert" : "green", "jaune" : "yellow", "orange" : "orange", "rouge" : "red"}

    if jeu["tour"] == "def" :
        jeu["couleur_en_cour"] = "vert"
    
    if jeu["num_input"] == len(jeu["patern_donne"]) :
        input_complet(canva, racine)
        return

    elif not jeu["qte_en_cour"] :
        input_incomplet(canva, racine)
        return
    
    else :

        if jeu[ej.touche_haut] :
            if ej.touche_haut == jeu["patern_donne"][jeu["num_input"]] :
                canva.itemconfig(jeu["lst_input"][jeu["num_input"]], fill = trad_coul[jeu["couleur_en_cour"]])
                jeu["num_input"] += 1
                racine.after(45)
            
            else : 
                for i in range (len(jeu["lst_input"])) :
                    canva.itemconfig(jeu["lst_input"][i], fill = "white")
                    jeu["num_input"] = 0
                    racine.after(45)

        if jeu[ej.touche_bas] :
            if ej.touche_bas == jeu["patern_donne"][jeu["num_input"]] :
                canva.itemconfig(jeu["lst_input"][jeu["num_input"]], fill = trad_coul[jeu["couleur_en_cour"]])
                jeu["num_input"] += 1
                racine.after(45)

            else : 
                for i in range (len(jeu["lst_input"])) :
                    canva.itemconfig(jeu["lst_input"][i], fill = "white")
                    jeu["num_input"] = 0
                    racine.after(45)

        if jeu[ej.touche_gauche] :
            if ej.touche_gauche == jeu["patern_donne"][jeu["num_input"]] :
                canva.itemconfig(jeu["lst_input"][jeu["num_input"]], fill = trad_coul[jeu["couleur_en_cour"]])
                jeu["num_input"] += 1
                racine.after(45)

            else : 
                for i in range (len(jeu["lst_input"])) :
                    canva.itemconfig(jeu["lst_input"][i], fill = "white")
                    jeu["num_input"] = 0
                    racine.after(45)

        if jeu[ej.touche_droite] :
            if ej.touche_droite == jeu["patern_donne"][jeu["num_input"]] :
                canva.itemconfig(jeu["lst_input"][jeu["num_input"]], fill = trad_coul[jeu["couleur_en_cour"]])
                jeu["num_input"] += 1
                racine.after(45)

            else : 
                for i in range (len(jeu["lst_input"])) :
                    canva.itemconfig(jeu["lst_input"][i], fill = "white")
                    jeu["num_input"] = 0
                    racine.after(45)

        racine.after(45, lambda : attaque_input(canva, racine))




def dessin_qte(canva) :

    if jeu["tour"] == "atk" :
        couleur = 3*jeu["pos_curseur"][0] + jeu["pos_curseur"][1]
        lcoul = ["violet", "bleu", "vert", "jaune", "orange", "rouge"]

        jeu["couleur_en_cour"] = lcoul[couleur]

        jeu["patern_donne"] = pat.qte[lcoul[couleur]]

    if jeu["tour"] == "def" :
        jeu["patern_donne"] = ej.dico_mob[ej.lst_mob[jeu["mob_en_cours"]]]["patern"]
    
    jeu["num_input"] = 0

    jeu["lst_input"] = []
    
    zoom = jeu["zoom"]

    x = (1120 - 50*len(jeu["patern_donne"])) // 2
    y = 400

    for i in jeu["patern_donne"] :

        if i == "z" :
            jeu["lst_input"].append(canva.create_polygon((x+20)*zoom, y*zoom, (x+35)*zoom, (y+20)*zoom, (x+25)*zoom, (y+20)*zoom, (x+25)*zoom, (y+40)*zoom, (x+15)*zoom, (y+40)*zoom, (x+15)*zoom, (y+20)*zoom, (x+5)*zoom, (y+20)*zoom, fill = "#ffffff", tags = ("combat", "fleche")))

        if i == "q" :
            jeu["lst_input"].append(canva.create_polygon(x*zoom, (y+20)*zoom, (x+20)*zoom, (y+5)*zoom, (x+20)*zoom, (y+15)*zoom, (x+40)*zoom, (y+15)*zoom, (x+40)*zoom, (y+25)*zoom, (x+20)*zoom, (y+25)*zoom, (x+20)*zoom, (y+35)*zoom, x*zoom, (y+20)*zoom, fill = "#ffffff", tags = ("combat", "fleche")))

        if i == "s" :
            jeu["lst_input"].append(canva.create_polygon((x+20)*zoom, (y+40)*zoom, (x+35)*zoom, (y+20)*zoom, (x+25)*zoom, (y+20)*zoom, (x+25)*zoom, y*zoom, (x+15)*zoom, y*zoom, (x+15)*zoom, (y+20)*zoom, (x+5)*zoom, (y+20)*zoom, fill = "#ffffff", tags = ("combat", "fleche")))

        if i == "d" :
            jeu["lst_input"].append(canva.create_polygon(x*zoom, (y+15)*zoom, (x+20)*zoom, (y+15)*zoom, (x+20)*zoom, (y+5)*zoom, (x+40)*zoom, (y+20)*zoom, (x+20)*zoom, (y+35)*zoom, (x+20)*zoom, (y+25)*zoom, x*zoom, (y+25)*zoom, fill = "#ffffff", tags = ("combat", "fleche")))

        x += 50


def input_complet(canva, racine) :

    police = font.Font(size = 28, weight = "bold")
    zoom = jeu["zoom"]

    if jeu["tour"] == "atk" :

        jeu["timer"] = ej.dico_mob[ej.lst_mob[jeu["mob_en_cours"]]]["temps_atk"]

        canva.move("mob", 40*jeu["zoom"], 40*jeu["zoom"])
        racine.after(120, lambda : fin_deplacment_mob(canva))

        jeu["pv_mob"] -= 5

        if jeu["pv_mob"] <= 0 :
            canva.create_text ( 550*zoom, 410*zoom, text = f"Il reste {jeu["pv_mob"]} pv à {ej.lst_mob[jeu["mob_en_cours"]]}", fill = "#ffffff",  font = police, tags = "combat")
            

            racine.after(2000, lambda : victoire(canva, racine))

        else :

            canva.create_text ( 550*zoom, 410*zoom, text = f"Il reste {jeu["pv_mob"]} pv à {ej.lst_mob[jeu["mob_en_cours"]]}", fill = "#ffffff",  font = police, tags = "combat")

            racine.after(2000, lambda : fin_input(canva, racine))


    if jeu["tour"] == "def" :

        jeu["timer"] = ej.dico_mob[ej.lst_mob[jeu["mob_en_cours"]]]["temps_atk"]

        canva.move("mob", 40*jeu["zoom"], 40*jeu["zoom"])
        racine.after(120, lambda : fin_deplacment_mob(canva))

        canva.create_text ( 550*zoom, 410*zoom, text = f"{ej.lst_mob[jeu["mob_en_cours"]]} t'a raté", fill = "#ffffff",  font = police, tags = "combat")

        racine.after(2000, lambda : fin_input(canva, racine))

        

def fin_deplacment_mob(canva) :
    canva.move("mob", -40*jeu["zoom"], -40*jeu["zoom"])

def fin_input(canva, racine) :

    if jeu["tour"] == "def" :
        jeu["tour"] = "atk"
    else :
        jeu["tour"] = "def"

    combat.delete_canva(canva)
    combat.combat(canva, racine, jeu["zoom"])


def input_incomplet(canva, racine) :

    police = font.Font(size = 28, weight = "bold")
    zoom = jeu["zoom"]

    if jeu["tour"] == "atk" :
        canva.create_text ( 550*zoom, 410*zoom, text = f"Tu as raté {ej.lst_mob[jeu["mob_en_cours"]]}", fill = "#ffffff",  font = police, tags = "combat")

        racine.after(2000, lambda : fin_input(canva, racine))

    if jeu["tour"] == "def" :

        canva.move("mob", 40*jeu["zoom"], 40*jeu["zoom"])
        racine.after(120, lambda : fin_deplacment_mob(canva))

        jeu["pv_joueur"] -= ej.dico_mob[ej.lst_mob[jeu["mob_en_cours"]]]["degat"]

        if jeu["pv_joueur"] <= 0 :
            canva.create_text ( 550*zoom, 410*zoom, text = f"{ej.lst_mob[jeu["mob_en_cours"]]} t'as infligé {ej.dico_mob[ej.lst_mob[jeu["mob_en_cours"]]]["degat"]} dégat", fill = "#ffffff",  font = police, tags = "combat")

            racine.after(2000, lambda : defaite(canva, racine))

        else :
            canva.create_text ( 550*zoom, 410*zoom, text = f"{ej.lst_mob[jeu["mob_en_cours"]]} t'as infligé {ej.dico_mob[ej.lst_mob[jeu["mob_en_cours"]]]["degat"]} dégat", fill = "#ffffff",  font = police, tags = "combat")

            racine.after(2000, lambda : fin_input(canva, racine))

def victoire(canva, racine) :

    police = font.Font(size = 28, weight = "bold")
    zoom = jeu["zoom"]

    canva.create_rectangle(0, 0, 1120*zoom, 630*zoom, fill = "#000000", tags = "combat")

    canva.create_text ( 550*zoom, 410*zoom, text = f"Bravo ! Tu as battu {ej.lst_mob[jeu["mob_en_cours"]]}", fill = "#ffffff",  font = police, tags = "combat")

    racine.after(2000, lambda : combat.delete_canva(canva))


def defaite(canva, racine) :

    police = font.Font(size = 28, weight = "bold")
    zoom = jeu["zoom"]
    
    canva.create_rectangle(0, 0, 1120*zoom, 630*zoom, fill = "#000000", tags = "combat")
    canva.create_text ( 550*zoom, 410*zoom, text = "T'es mort... Skill issue, vraiment", fill = "#ffffff",  font = police, tags = "combat")