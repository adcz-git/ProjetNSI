import etat_jeu
jeu = etat_jeu.etat
import mob_hostile_1 as mh


def constructeur_tableau(tbl, canva) :
    zoom = jeu["zoom"]
    for hauteur in range (18) :
        for largeur in range (32) :
            if tbl[hauteur][largeur] == 1 :
                canva.create_rectangle(35*zoom*largeur, 35*zoom*hauteur, 35*zoom + 35*zoom*largeur, 35*zoom + 35*zoom*hauteur, outline = "yellow")

    # Deuxième tour pour les mobs et tout
    for hauteur in range (18) :
        for largeur in range (32) :
            if tbl[hauteur][largeur] == 9 :
                jeu["lst_mob"].append (mh.mob_hostile_1(35*largeur, 35*hauteur))
                jeu["lst_mob"][-1].y = jeu["lst_mob"][-1].y + (35 - jeu["lst_mob"][-1].haut)
                jeu["lst_mob"][-1].hitbox(canva)