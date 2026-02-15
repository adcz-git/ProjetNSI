import etat_jeu as ej
jeu = ej.etat

import combat

def choix_type_menu (canva, racine) :
    if jeu[ej.touche_gauche] :
        if jeu["num_type"] > 0 :
            canva.itemconfig(combat.lst_menu[jeu["num_type"]], fill = "grey")
            jeu["num_type"] -= 1
            canva.itemconfig(combat.lst_menu[jeu["num_type"]], fill = "white")
            racine.after(100)
    
    if jeu[ej.touche_droite] :
        if jeu["num_type"] < 3 :
            canva.itemconfig(combat.lst_menu[jeu["num_type"]], fill = "grey")
            jeu["num_type"] += 1
            canva.itemconfig(combat.lst_menu[jeu["num_type"]], fill = "white")
            racine.after(100)


def deplacement_cursor (canva, racine) :

    zoom = jeu["zoom"]

    if jeu[ej.touche_haut] :
        if jeu["pos_curseur"][0] == 1 :
            jeu["pos_curseur"][0] = 0
            canva.move("cursor", 0, -70*zoom)
            racine.after(100)
    
    if jeu[ej.touche_bas] :
        if jeu["pos_curseur"][0] == 0 :
            jeu["pos_curseur"][0] = 1
            canva.move("cursor", 0, 70*zoom)
            racine.after(100)

    if jeu[ej.touche_gauche] :
        if jeu["pos_curseur"][1] > 0 :
            jeu["pos_curseur"][1] -= 1
            canva.move("cursor", -300*zoom, 0)
            racine.after(100)

    if jeu[ej.touche_droite] :
        if jeu["pos_curseur"][1] < 2 :
            jeu["pos_curseur"][1] += 1
            canva.move("cursor", 300*zoom, 0)
            racine.after(100)