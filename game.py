##################
##### Import #####
##################

import tkinter as tk
from player import player
from tableau import *
from tableau import *

#############################################################################
# C'est pour linux qui n'aime pas les dimensions. Vous, laisser le à 1 sauf #
# si la fenêtre est trop petite.                                            #
# Ca doit un être un integer                                                #
#############################################################################

zoom = 1

#######################################################
##### Définition de la fenêtre (Bordure + Canvas) #####
#######################################################

root = tk.Tk()
root.title (" On verra bien ")
root.geometry (f"{int(1140*zoom)}x{int(650*zoom)}")

canva_jeu = tk.Canvas (root, width = 1120*zoom, height = 630*zoom, bg = "#000000")
canva_jeu.place (x = 10*zoom, y = 10*zoom)


###############
##### Fps #####
###############

fps = 60
frequence_rappel = 1000 // fps # c'est en ms faut quand mm faire gaffe


##################
##### Joueur #####
##################

# Ce sont les positions actuelles du joueurs et elles 
# s'actualiseront au fil du temps

position_joueur_x = 800*zoom
position_joueur_y = 450*zoom

# On appelle juste la fonction qui fait apparaître le personnage

player(position_joueur_x, position_joueur_y, canva_jeu, zoom)


###########################
##### Touche d'action #####
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
    "space" : False
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
##### Tout ce qui touche au tableau (32x18) #####
#################################################

# C'est le tableau qui est actuellement actif, par défaut au début du 
# jeu c'est le tableau 0
tableau_actuelle = tb0

# Cette fonction construit les tableaux
def constructeur_tableau(tbl) :
    for hauteur in range (18) :
        for largeur in range (32) :
            if tbl[hauteur][largeur] == 1 :
                canva_jeu.create_rectangle(35*zoom*largeur, 35*zoom*hauteur, 35*zoom + 35*zoom*largeur, 35*zoom + 35*zoom*hauteur, outline = "yellow")

constructeur_tableau (tableau_actuelle)


####################################################################
##### Les déplacements (liés à la gravité, aux mouvements ...) #####
####################################################################

# Ici la fonction qui gère la chute

# La variable qui initialise la vitesse de la chute verticale
# plus la valeur est haute plus la chute est rapide

vitesse_verticale = 0


# La gravité, plus on la monte moins le personnage saute haut, comme 
# la gravité sur terre en gros

gravite = 1200*zoom


# La c'est le flag qui gère si le perso est en l'air ou pas, si le 
# flag est placé sur true, la fonction de saut sera désactivé jusqu'au
# changement d'état du flag

is_on_ground = True


# la fonction suivante gère tout ce qui touche à la gravité, si le perso 
# doit retomber au sol ou pas

def physique_verticale () :
    global position_joueur_x, position_joueur_y, is_on_ground, frequence_rappel, vitesse_verticale, gravite, tableau_actuelle

    # la vitesse verticale augmente constament, mais elle est réinitialiser 
    # à 0 également, lorsque le perso est au sol

    vitesse_verticale += gravite * (frequence_rappel * 0.001)
    variation_verticale = int(vitesse_verticale * (frequence_rappel * 0.001))

    is_on_ground = False


    # La condition pour la collision avec le plafond, lorsque le perso saute 
    # et qu'il heurte le plafond, la vitesse verticale est redéfinie à 0 et 
    # le perso commance sa chute

    # on rajoute + 25 à la coordonné x du personnage pour être au milieu (faut le changer)

    coordonne_y_tableau = position_joueur_y // (35*zoom)
    if position_joueur_y % (35*zoom) == 0 and coordonne_y_tableau > 0 :
        coordonne_y_tableau -= 1

    flag_collision_plafond = False

    for point in range (3) :

        point_indicateur_position_perso = position_joueur_x + 25*zoom*point
        coordonne_x_tableau = point_indicateur_position_perso // (35*zoom)
        if point_indicateur_position_perso % (35*zoom) == 0 and point == 2 :
            coordonne_x_tableau -= 1
        
        if tableau_actuelle[coordonne_y_tableau][coordonne_x_tableau] == 1 :
            flag_collision_plafond = True


    if vitesse_verticale < 0 and flag_collision_plafond :
        vitesse_verticale = 0
        variation_verticale = 0


    # La c'est la condition qui gère la collision avec le sol
    # le "+ variation verticale" est important, c'est pour avoir la coord en y à la prochaine frame et donc d'éviter 
    # de rentrer dans la texture pour remonter

    coordonne_y_tableau = (position_joueur_y + 75*zoom + variation_verticale) // (35*zoom)
    if coordonne_y_tableau == 18 :
        coordonne_y_tableau -= 1

    flag_collision_sol = False

    for point in range (3) :

        point_indicateur_position_perso = position_joueur_x + 25*zoom*point
        coordonne_x_tableau = point_indicateur_position_perso // (35*zoom)
        if point_indicateur_position_perso % (35*zoom) == 0 and point == 2 :
            coordonne_x_tableau -= 1
        
        if tableau_actuelle[coordonne_y_tableau][coordonne_x_tableau] == 1 :
            flag_collision_sol = True

    
    # Initialiser de déplacement qui va avoir lieu
    delta_verticale = variation_verticale

    # Modifier la valeur de delta_y si jamais le perso se rapproche du sol
    if flag_collision_sol and vitesse_verticale > 0 :
        
        variation_verticale = coordonne_y_tableau*35*zoom - (position_joueur_y + 75*zoom)
        delta_verticale = variation_verticale
        
        vitesse_verticale = 0
        is_on_ground = True


    canva_jeu.move("player", 0, delta_verticale)
    position_joueur_y += delta_verticale
    

    # pour gérer le fait de sauter plus ou moins haut, quand on relache la 
    # barre espace, on réduit la vitesse verticale de moitié (en fait pour 
    # sauter, on met la vitesse verticale en négatif, ce qui fait monter 
    # le perso, donc quand la valeur de la vitesse verticale se rapproche 
    # de 0, le perso monte plus.)

    if action_key["space"] and is_on_ground :
        is_on_ground = False
        vitesse_verticale = -600*zoom

    if not action_key["space"] and vitesse_verticale < 0 :
        vitesse_verticale *= 0.5


def deplacement_gauche() :
    global position_joueur_x, position_joueur_y, tableau_actuelle

    coordonne_x_tableau = position_joueur_x // (35*zoom)
    if position_joueur_x % (35*zoom) == 0 and coordonne_x_tableau > 0 :
        coordonne_x_tableau -= 1

    flag_collision_gauche = False

    for point in range (3) :
        
        point_indicateur_position_perso = position_joueur_y + 5*zoom + 35*zoom*point
        coordonne_y_tableau = point_indicateur_position_perso // (35*zoom)
        if point_indicateur_position_perso % (35*zoom) == 0 and point == 2 :
            coordonne_y_tableau -= 1

        if tableau_actuelle[coordonne_y_tableau][coordonne_x_tableau] == 1 :
            flag_collision_gauche = True

    if not flag_collision_gauche and position_joueur_x - 5*zoom >= 0 :
        canva_jeu.move("player", -5*zoom*(60 // fps), 0)
        position_joueur_x -= 5*zoom*(60 // fps)


def deplacement_droite() :
    global position_joueur_x, position_joueur_y, tableau_actuelle

    coordonne_x_tableau = (position_joueur_x + 50*zoom) // (35*zoom)
    if (position_joueur_x + 50*zoom) % (35*zoom) == 0 :
        coordonne_x_tableau -= 1

    flag_collision_droite = False

    for point in range (3) :
        
        point_indicateur_position_perso = position_joueur_y + 5*zoom + 35*zoom*point
        coordonne_y_tableau = point_indicateur_position_perso // (35*zoom)
        if point_indicateur_position_perso % (35*zoom) == 0 and point == 2 :
            coordonne_y_tableau -= 1

        if tableau_actuelle[coordonne_y_tableau][coordonne_x_tableau] == 1 :
            flag_collision_droite = True

    if not flag_collision_droite and position_joueur_x + 5*zoom <= 1140*zoom :
        canva_jeu.move("player", +5*zoom*(60 // fps), 0)
        position_joueur_x += 5*zoom*(60 // fps)



###########################################################################
## Update (c'est vraiment ce qui fait tourner le jeu faut pas le casser) ##
###########################################################################

def update () :
    if action_key[touche_gauche] :
        deplacement_gauche()

    if action_key[touche_droite] :
        deplacement_droite()

    physique_verticale()


    root.after(frequence_rappel, update)

update()



root.mainloop()