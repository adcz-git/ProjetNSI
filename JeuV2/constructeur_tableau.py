import etat_jeu
jeu = etat_jeu.etat


def constructeur_tableau(tbl, canva) :
    zoom = jeu["zoom"]
    for hauteur in range (18) :
        for largeur in range (32) :
            if tbl[hauteur][largeur] == 1 :
                canva.create_rectangle(35*zoom*largeur, 35*zoom*hauteur, 35*zoom + 35*zoom*largeur, 35*zoom + 35*zoom*hauteur, outline = "yellow")