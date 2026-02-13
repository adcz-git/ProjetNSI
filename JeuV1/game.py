
##################
##################
##### Import #####
##################
##################


import tkinter as tk
import tkinter.font as font
import random

import player
import combat
import etat_jeu as ej
import tab

jeu = ej.etat

#############################################################################
#############################################################################
# C'est pour linux qui n'aime pas les dimensions. Vous, le laissez à 1 sauf #
# si la fenêtre est trop petite.                                            #
# Ca doit un être un integer                                                #
#############################################################################
#############################################################################


zoom = jeu["zoom"]




#######################################################
#######################################################
##### Définition de la fenêtre (Bordure + Canvas) #####
#######################################################
#######################################################


root = tk.Tk()
root.title (" On verra bien ")
root.geometry (f"{int(1140*zoom)}x{int(650*zoom)}")

canva_jeu = tk.Canvas (root, width = 1120*zoom, height = 630*zoom, bg = "#000000")
canva_jeu.place (x = 10*zoom, y = 10*zoom)




##################
##################
##### Joueur #####
##################
##################


# Ce sont les positions actuelles du joueur et elles 
# s'actualiseront au fil du temps

position_joueur_x = jeu["pos_x"] * zoom
position_joueur_y = jeu["pos_y"] * zoom

# On appelle juste la fonction qui fait apparaître le personnage

player.player(position_joueur_x, position_joueur_y, canva_jeu, zoom)




###########################
###########################
##### Touche d'action #####
###########################
###########################


touche_haut = "z"
touche_gauche = "q" 
touche_bas = "s"
touche_droite = "d"

# On les stock dans un dictionnaire
# Lorsqu'une touche est pressée, le booléen passse sur True et 
# la fonction associée sera exécutée jusqu'au relachement de la 
# touche, le booléen sera replacé sur False

action_key = {
    touche_haut : False,
    touche_gauche : False,
    touche_bas : False,
    touche_droite : False,
    "space" : False,
    "return" : False,
    "escape" : False,

    # touche temporaire
    "c" : False, 
    "v" :False,
    "e" : False
}

# Ces deux fonctions font changer d'état le booléen des touches

def key_press(e) :
    if e.keysym.lower() in action_key :
        action_key[e.keysym.lower()] = True

def key_release (e) :
    if e.keysym.lower() in action_key :
        action_key[e.keysym.lower()] = False

root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)




#################################################
#################################################
##### Tout ce qui touche au tableau (32x18) #####
#################################################
#################################################


# C'est le tableau qui est actuellement actif. Par défaut au début du 
# jeu c'est le tableau 0
tableau_actuelle = jeu["tbl_act"]

# Cette fonction construit les tableaux
def constructeur_tableau(tbl) :
    for hauteur in range (18) :
        for largeur in range (32) :
            if tbl[hauteur][largeur] == 1 :
                canva_jeu.create_rectangle(35*zoom*largeur, 35*zoom*hauteur, 35*zoom + 35*zoom*largeur, 35*zoom + 35*zoom*hauteur, outline = "yellow")

constructeur_tableau (tableau_actuelle)




####################################################################
####################################################################
##### Les déplacements (liés à la gravité, aux mouvements ...) #####
####################################################################
####################################################################


########################################
########################################
#####           Gravité            #####
########################################
########################################


def physique_verticale () :

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


    canva_jeu.move("player", 0, var_vert*zoom)
    jeu["pos_y"] += var_vert




###############################
###############################
#####         Saut        #####
###############################
###############################


def saut() :
    """
    pour faire sauter le personnage, on règle la vitesse verticale en négatif, ce qui va le faire monter.

    En relachant la barre espace, on augmente cette valeur pour le faire tomber plus rapidement

    Et pour que la touche fonctionne, il faut que le personnage soit dans le monde ouvert,
    pas dans un combat
    """

    if jeu["etat"] == "openworld" :

        if action_key["space"] and jeu["is_on_ground"] :
            jeu["is_on_ground"] = False
            jeu["v_vert"] = -600

        if not action_key["space"] and jeu["v_vert"] < 0 :
            jeu["v_vert"] *= 0.5




#######################################
#######################################
#####        Touche Gauche        #####
#######################################
#######################################


def deplacement_gauche() :

    """
    Pour le déplacement, la limite de déplacement est calculée à l'avance, ne laissant pas le personnage la dépassé.

    Ca se fait en trois points : il y a trois coordonnés prise au niveau du personnage, qui vont pointer vers l'avant jusqu'a atteindre un obstacle.
    Si un obstacle est rencontré, la coordonné est marqué, si rien n'est rencontré, la limite est le bord de la fenêtre
    """


    #######################
    ##### Déplacement #####
    #######################

    if jeu["etat"] == "openworld" :

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


        if jeu["pos_x"] - 5 * (60 // jeu["fps"]) >= limite_deplacement :
            canva_jeu.move("player", -5*zoom*(60 // jeu["fps"]), 0)
            jeu["pos_x"] -= 5*(60 // jeu["fps"])


        ##############################
        ##### Apparition ennemie #####
        ##############################

        mob = random.randint(1, int(1800*(30/jeu["fps"])))
        if mob == 1 :
            combat.intro(root, canva_jeu, zoom)
            jeu["etat"] = "fight"




def deplacement_droite() :

    """
    Pour le déplacement, la limite de déplacement est calculée à l'avance, ne laissant pas le personnage la dépassé.

    Ca se fait en trois points : il y a trois coordonnés prise au niveau du personnage, qui vont pointer vers l'avant jusqu'a atteindre un obstacle.
    Si un obstacle est rencontré, la coordonné est marqué, si rien n'est rencontré, la limite est le bord de la fenêtre
    """


    #######################
    ##### Déplacement #####
    #######################

    if jeu["etat"] == "openworld" :

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

        if jeu["pos_x"] + 50 + 5*(60 // jeu["fps"]) <= limite_deplacement :
            canva_jeu.move("player", 5*zoom*(60 // jeu["fps"]), 0)
            jeu["pos_x"] += 5*(60 // jeu["fps"])


        ##############################
        ##### Apparition ennemie #####
        ##############################

        mob = random.randint(1, int(1800*(30/jeu["fps"])))
        if mob == 1 :
            combat.intro(root, canva_jeu, zoom)
            jeu["etat"] = "fight"




#############################################
#############################################
##### Choix de menu (pendant le combat) #####
#############################################
#############################################


################################
#### Choix du type d'action ####
################################

def choix_type_menu () :
    if action_key[touche_gauche] :
        if jeu["num_type"] > 0 :
            canva_jeu.itemconfig(combat.lst_menu[jeu["num_type"]], fill = "grey")
            jeu["num_type"] -= 1
            canva_jeu.itemconfig(combat.lst_menu[jeu["num_type"]], fill = "white")
            root.after(100)
    
    if action_key[touche_droite] :
        if jeu["num_type"] < 3 :
            canva_jeu.itemconfig(combat.lst_menu[jeu["num_type"]], fill = "grey")
            jeu["num_type"] += 1
            canva_jeu.itemconfig(combat.lst_menu[jeu["num_type"]], fill = "white")
            root.after(100)


############################################################
## Déplacement du curseur, pour le choix des atk / objets ##
############################################################

def deplacement_cursor () :

    if action_key[touche_haut] :
        if jeu["pos_curseur"][0] == 1 :
            jeu["pos_curseur"][0] = 0
            canva_jeu.move("cursor", 0, -70*zoom)
            root.after(100)
    
    if action_key[touche_bas] :
        if jeu["pos_curseur"][0] == 0 :
            jeu["pos_curseur"][0] = 1
            canva_jeu.move("cursor", 0, 70*zoom)
            root.after(100)

    if action_key[touche_gauche] :
        if jeu["pos_curseur"][1] > 0 :
            jeu["pos_curseur"][1] -= 1
            canva_jeu.move("cursor", -300*zoom, 0)
            root.after(100)

    if action_key[touche_droite] :
        if jeu["pos_curseur"][1] < 2 :
            jeu["pos_curseur"][1] += 1
            canva_jeu.move("cursor", 300*zoom, 0)
            jeu["type_menu"]
            root.after(100)


##############################
#### Choix fuite yes / no ####
##############################

def fuite_yn () :
    if action_key[touche_gauche] :
        if jeu["choix_fuite"] == 1 :
            canva_jeu.itemconfig(combat.lst_fuite[jeu["choix_fuite"]], fill = "grey")
            jeu["choix_fuite"] = 0
            canva_jeu.itemconfig(combat.lst_fuite[jeu["choix_fuite"]], fill = "white")
            root.after(100)

    if action_key[touche_droite] :
        if jeu["choix_fuite"] == 0 :
            canva_jeu.itemconfig(combat.lst_fuite[jeu["choix_fuite"]], fill = "grey")
            jeu["choix_fuite"] = 1
            canva_jeu.itemconfig(combat.lst_fuite[jeu["choix_fuite"]], fill = "white")
            root.after(100)
        

def fin_fuite(flag) :
    canva_jeu.delete("texte_fuite")
    jeu["type_menu"] = "type_action"
    combat.fin_combat (canva_jeu)
    jeu["enter_en_cour"] = False

    if flag == 1 :
        jeu["tour"] = "def"
        combat.combat(canva_jeu, zoom)


###########################################################################
## Update (c'est vraiment ce qui fait tourner le jeu faut pas le casser) ##
###########################################################################


def update () :

    if action_key[touche_gauche] :
        deplacement_gauche()

    if action_key[touche_droite] :
        deplacement_droite()

    saut()

    physique_verticale()


    if jeu["etat"] == "fight" and jeu["type_menu"] == "type_action" :
        choix_type_menu()

# verifié
    if jeu["etat"] == "fight" and jeu["type_menu"] == "choix_action" and jeu["tour"] == "atk" and jeu["num_type"] == 3 :
        fuite_yn()

    if jeu["curseur"] :
        deplacement_cursor()


    if action_key["c"] :
        combat.intro(root, canva_jeu, zoom)
        jeu["etat"] = "fight"

    if action_key["v"] :
        combat.fin_combat (canva_jeu)

    # dans l'interface de combat, c'est ce qui permet de choisir l'action à effectuer
    if action_key["return"] :
        if jeu["type_menu"] == "type_action" :
            if jeu["etat"] == "fight" and jeu["tour"] == "atk" and jeu["type_menu"] == "type_action" :
                combat.creation_menu_action (canva_jeu, zoom)
                jeu["type_menu"] = "choix_action"
            root.after(100)
        
        elif jeu["type_menu"] == "choix_action" :

            if jeu["num_type"] == 0 :
                if not jeu["qte_en_cour"] :
                    canva_jeu.delete("menu_action")
                    controle_time()
                    root.after(100)

            if jeu["num_type"] == 3 :
                print(jeu["enter_en_cour"] == False)
                if jeu["enter_en_cour"] == False :
                    jeu["enter_en_cour"] = True
                    if jeu["choix_fuite"] == 0 :
                        prob = random.randint(0,3)
                        print(prob)
                        if prob == 3 :
                            police = font.Font(size = 22, weight = "bold")
                            canva_jeu.delete("menu_action")
                            canva_jeu.create_text ( 550*zoom, 410*zoom, text = "Il ne t'a pas rattrapé, mais ...", fill = "#FFFFFF",  font = police, tags = "texte_fuite")
                            canva_jeu.create_text ( 550*zoom, 480*zoom, text = "Tu ne fuiras pas indéfiniment", fill = "#FFFFFF",  font = police, tags = "texte_fuite")
                            root.after(3000, lambda : fin_fuite(0))

                        else :
                            dialogue = [[["La peur t'as figée sur place"],[]], [["Tu as lamentablement trébuché"],["sur un caillou"]],[["La fuite c'est pour les faibles,"],["tu es trop faible pour fuir"]]]
                            police = font.Font(size = 22, weight = "bold")
                            canva_jeu.delete("menu_action")
                            canva_jeu.create_text ( 550*zoom, 410*zoom, text = dialogue[prob][0], fill = "#FFFFFF",  font = police, tags = "texte_fuite")
                            canva_jeu.create_text ( 550*zoom, 480*zoom, text = dialogue[prob][1], fill = "#FFFFFF",  font = police, tags = "texte_fuite")
                            root.after(3000, lambda : fin_fuite(1))


                    elif jeu["choix_fuite"] == 1 :
                        canva_jeu.delete("menu_action")
                        jeu["type_menu"] = "type_action"
                        jeu["enter_en_cour"] = False

                    root.after(100)

    
    # ça sers juste à revenir dans le menu précédent
    if action_key["escape"] :
        if jeu["etat"] == "fight" and jeu["tour"] == "atk" and jeu["type_menu"] == "choix_action" :
            canva_jeu.delete("menu_action")
            jeu["type_menu"] = "type_action"


    root.after(jeu["f_rappel"], update)

update()

def controle_time() :
    temps_max = 4000 # en ms
    jeu["qte_en_cour"] = True
    if jeu["timer"] == 0 :
        canva_jeu.create_rectangle (210*zoom, 500*zoom, 910*zoom, 520*zoom, fill = "#ffffff", tags = ("combat", "barre_timer"))
        canva_jeu.create_rectangle (210*zoom, 500*zoom, 910*zoom, 520*zoom, fill = "grey", tags = "combat")
    if jeu["timer"] >= temps_max :
        jeu["timer"] = 0
        return
    else :
        jeu["timer"] += jeu["f_rappel"]
        print(jeu["timer"])
        root.after(jeu["f_rappel"], controle_time)
        canva_jeu.delete("barre_timer")
        if jeu["timer"] <= temps_max - 1000 :
            couleur_util = "#ffffff"
        else :
            couleur_util = "red"
        canva_jeu.create_rectangle (210*zoom, 500*zoom, (910 - 700*(jeu["timer"]/temps_max))*zoom, 520*zoom, fill = couleur_util, tags = ("combat", "barre_timer"))

        



root.mainloop()