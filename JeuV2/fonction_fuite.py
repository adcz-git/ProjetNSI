import etat_jeu as ej
jeu = ej.etat

import combat
import random
import tkinter.font as font



##########################################################
############ La fonction qui gère la si le curseur #######
############ fuite est sur oui ou non              #######
##########################################################

def fuite_yn (canva, racine) :
    if jeu[ej.touche_gauche] :
        if jeu["choix_fuite"] == 1 :
            canva.itemconfig(combat.lst_fuite[jeu["choix_fuite"]], fill = "grey")
            jeu["choix_fuite"] = 0
            canva.itemconfig(combat.lst_fuite[jeu["choix_fuite"]], fill = "white")
            racine.after(100)

    if jeu[ej.touche_droite] :
        if jeu["choix_fuite"] == 0 :
            canva.itemconfig(combat.lst_fuite[jeu["choix_fuite"]], fill = "grey")
            jeu["choix_fuite"] = 1
            canva.itemconfig(combat.lst_fuite[jeu["choix_fuite"]], fill = "white")
            racine.after(100)


def fin_fuite(flag, canva, racine) :
    canva.delete("texte_fuite")
    jeu["type_menu"] = "type_action"
    combat.delete_canva (canva)
    jeu["enter_en_cour"] = False

    if flag == 1 :
        jeu["tour"] = "def"
        combat.combat(canva, racine, jeu["zoom"])


def action_fuite(canva, racine) :

    zoom = jeu["zoom"]

    if jeu["enter_en_cour"] == False :
        jeu["enter_en_cour"] = True
        if jeu["choix_fuite"] == 0 :
            prob = random.randint(0,3)
            print(prob)
            if prob == 3 :
                police = font.Font(size = 22, weight = "bold")
                canva.delete("menu_action")
                canva.create_text ( 550*zoom, 410*zoom, text = "Il ne t'a pas rattrapé, mais ...", fill = "#ffffff",  font = police, tags = "texte_fuite")
                canva.create_text ( 550*zoom, 480*zoom, text = "Tu ne fuiras pas indéfiniment", fill = "#ffffff",  font = police, tags = "texte_fuite")
                racine.after(3000, lambda : fin_fuite(0, canva, racine))

            else :
                dialogue = {
                    0 : {
                        0 : "La peur t'as figée sur place", 
                        1 : ""
                        },
                    1 : {
                        0 : "Tu as lamentablement trébuché",
                        1 : "sur un caillou"
                        },
                    2 : {0 : "La fuite c'est pour les faibles,", 
                        1 : "tu es trop faible pour fuir"
                        }

                }

                police = font.Font(size = 22, weight = "bold")
                canva.delete("menu_action")
                canva.create_text ( 550*zoom, 410*zoom, text = dialogue[prob][0], fill = "#ffffff",  font = police, tags = "texte_fuite")
                canva.create_text ( 550*zoom, 480*zoom, text = dialogue[prob][1], fill = "#ffffff",  font = police, tags = "texte_fuite")
                racine.after(3000, lambda : fin_fuite(1, canva, racine))


        elif jeu["choix_fuite"] == 1 :
            canva.delete("menu_action")
            jeu["type_menu"] = "type_action"
            jeu["enter_en_cour"] = False

        racine.after(100)
