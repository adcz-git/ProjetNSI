import etat_jeu 
jeu = etat_jeu.etat


def deplacement_gauche(canva, racine) :

    jeu["der_depla"] = "g"

    """
    Pour le déplacement, la limite de déplacement est calculée à l'avance, ne laissant pas le personnage la dépassé.

    Ca se fait en trois points : il y a trois coordonnés prise au niveau du personnage, qui vont pointer vers l'avant jusqu'a atteindre un obstacle.
    Si un obstacle est rencontré, la coordonné est marqué, si rien n'est rencontré, la limite est le bord de la fenêtre
    """

    zoom = jeu["zoom"]

    #######################
    ##### Déplacement #####
    #######################

    limite_deplacement = flag_gauche()

    if jeu["pos_x"] - 5 * (60 // jeu["fps"]) >= limite_deplacement :
        canva.move("player", -5*zoom*(60 // jeu["fps"]), 0)
        jeu["pos_x"] -= 5*(60 // jeu["fps"])




def deplacement_droite(canva, racine) :

    jeu["der_depla"] = "d"

    """
    Pour le déplacement, la limite de déplacement est calculée à l'avance, ne laissant pas le personnage la dépassé.

    Ca se fait en trois points : il y a trois coordonnés prise au niveau du personnage, qui vont pointer vers l'avant jusqu'a atteindre un obstacle.
    Si un obstacle est rencontré, la coordonné est marqué, si rien n'est rencontré, la limite est le bord de la fenêtre
    """

    zoom = jeu["zoom"]

    #######################
    ##### Déplacement #####
    #######################
    limite_deplacement = flag_droite()

    if jeu["pos_x"] + 50 + 5*(60 // jeu["fps"]) <= limite_deplacement :
        canva.move("player", 5*zoom*(60 // jeu["fps"]), 0)
        jeu["pos_x"] += 5*(60 // jeu["fps"])


def flag_gauche() :
    x_tbl = jeu["pos_x"] // 35
    if jeu["pos_x"] % 35 == 0 and x_tbl > 0 :
        x_tbl -= 1

    lst_flag_collision = []
    flag_pas_de_mur = False

    for pt in range (3) :
            
        pt_test = jeu["pos_y"] + 5 + 35 * pt
        y_tbl = pt_test // 35
        if pt_test % 35 == 0 and pt == 2 :
            y_tbl -= 1

        while jeu["tbl_act"][y_tbl][x_tbl] != 1 and x_tbl - 1 >= 0 :
            x_tbl -= 1

        if x_tbl == 0 and jeu["tbl_act"][y_tbl][x_tbl] != 1 :
            lst_flag_collision.append(-1)
        else :
            lst_flag_collision.append(x_tbl)


    if lst_flag_collision[0] == lst_flag_collision[1] == lst_flag_collision[2] == -1 :
        flag_pas_de_mur = True

    if flag_pas_de_mur :
        limite_deplacement = 0
    else :
        limite_deplacement = (max(lst_flag_collision) + 1) * 35

    return limite_deplacement




def flag_droite() :
    x_tbl = (jeu["pos_x"] + 50) // 35
    if (jeu["pos_x"] + 50) % 35 == 0 :
        x_tbl -= 1

    lst_flag_collision = []
    flag_pas_de_mur = False
        

    for pt in range (3) :
        
        pt_test = jeu["pos_y"] + 5 + 35*pt
        y_tbl = pt_test // 35
        if pt_test % 35 == 0 and pt == 2 :
            y_tbl -= 1

        while jeu["tbl_act"][y_tbl][x_tbl] != 1 and x_tbl + 1 <= 31 :
            x_tbl += 1

        if x_tbl == 31 and jeu["tbl_act"][y_tbl][x_tbl] != 1 :
            lst_flag_collision.append(99)
        else :
            lst_flag_collision.append(x_tbl)

    if lst_flag_collision[0] == lst_flag_collision[1] == lst_flag_collision[2] == 99 :
        flag_pas_de_mur = True

    if flag_pas_de_mur :
        limite_deplacement = 1120
    else :
        limite_deplacement = min(lst_flag_collision) * 35

    return limite_deplacement