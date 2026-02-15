import etat_jeu
jeu = etat_jeu.etat

def physique_verticale (canva) :

    zoom = jeu["zoom"]

    ###########################
    ###########################
    ##### Reset des flags #####
    ###########################
    ###########################


    jeu["collision_sol"] = False
    jeu["collision_plafond"] = False
    jeu["is_on_ground"] = False


    

    """
    C'est la fonction qui gère la chute, c'est géré avec une vitesse vertical qui augmente constament et qui est replacé à 0 uniquement lorsque le personnage est au sol.

    C'est un flag qui gère si le personnage est au sol : etat["is_on_ground"] (bool)

    Et il y a bien sûr un facteur gravité qui est constant

    le * 0.001 pour avoir la fréquence de rappel en seconde
    """

    jeu["v_vert"] += jeu["gravite"] * jeu["f_rappel"] * 0.001
    var_vert = int(jeu["v_vert"] * jeu["f_rappel"] * 0.001)

    jeu["is_on_ground"] = False


    """
    Lorsque le personnage saute, il faut voir s'il heurte le plafond, c'est ce que fait ce test.

    La collision est vérifier en 3 points, à gauche, au centre et à droite du personnage, cela évite qu'une partie du personnage puisse traverser un obstacle

    Le concept : la position du personnage est reliée à une coordonné du tableau, avec plusieurs valeurs numériques. Le personnages étant autorisé à se déplacer sur les coordonnées ayant une valeur différente de 1

    La collision est toujours géré avec un flag : etat["collision_plafond"] (bool)
    """

    y_tbl = jeu["pos_y"] // 35
    if jeu["pos_y"] % 35 == 0 and y_tbl > 0 :
        y_tbl -= 1


    for pt in range (3) :

        pt_test = jeu["pos_x"] + 25*pt
        x_tbl = pt_test // 35
        if pt_test % 35 == 0 and pt == 2 :
            x_tbl -= 1
        
        if jeu["tbl_act"][y_tbl][x_tbl] == 1 :
            jeu["collision_plafond"] = True


    if jeu["v_vert"] < 0 and jeu["collision_plafond"] :
        jeu["v_vert"] = 0
        var_vert = 0


    """
    Pour gérer si le personnage est au sol, on vérifie la prochaine coordonné du personnage afin d'éviter de le faire traverser les textures, ça se gère toujours avec un flag :
    etat["collision_sol"] (bool)

    Lorsque le personnage se rapproche du sol, la variation verticale est légèrement changé pour que le personnage tombe complètement au sol
    """

    y_tbl = (jeu["pos_y"] + 75 + var_vert) // 35
    if y_tbl == 18 :
        y_tbl -= 1


    for pt in range (3) :

        pt_test = jeu["pos_x"] + 25*pt
        x_tbl = pt_test // 35
        if pt_test % 35 == 0 and pt == 2 :
            x_tbl -= 1
        

        if jeu["tbl_act"][y_tbl][x_tbl] == 1 :
            jeu["collision_sol"] = True


    if jeu["collision_sol"] and jeu["v_vert"] > 0 :
        
        var_vert = y_tbl * 35 - (jeu["pos_y"] + 75)
        
        jeu["v_vert"] = 0
        jeu["is_on_ground"] = True


    canva.move("player", 0, var_vert*zoom)
    jeu["pos_y"] += var_vert


def saut() :
    """
    pour faire sauter le personnage, on règle la vitesse verticale en négatif, ce qui va le faire monter.

    En relachant la barre espace, on augmente cette valeur pour le faire tomber plus rapidement

    Et pour que la touche fonctionne, il faut que le personnage soit dans le monde ouvert,
    pas dans un combat
    """

    if jeu["etat"] == "openworld" :

        if jeu["space"] and jeu["is_on_ground"] :
            jeu["is_on_ground"] = False
            jeu["v_vert"] = -600

        if not jeu["space"] and jeu["v_vert"] < 0 :
            jeu["v_vert"] *= 0.5