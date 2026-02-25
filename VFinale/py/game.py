######################################
######################################
#####           Import           #####
######################################
######################################


import tkinter as tk
import tkinter.font as font
import random

import player
import etat_jeu as ej
jeu = ej.etat

import attaque as atk
import tab
import constructeur_tableau as cons_tbl
import gravite as g
import deplacement_openworld as dep_ow

import mob_hostile_1 as mh
import bar_vie as bar



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


#################################################
#################################################
##### Tout ce qui touche au tableau (32x18) #####
#################################################
#################################################


# C'est le tableau qui est actuellement actif. Par défaut au début du 
# jeu c'est le tableau 0
tableau_actuelle = jeu["tbl_act"]

# Cette fonction construit les tableaux


cons_tbl.constructeur_tableau (tableau_actuelle, canva_jeu)



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

# C'est la bar de vie

bar.dessin_bar_vie(canva_jeu)



# Ces deux fonctions font changer d'état le booléen des touches

def key_press(e) :
    if e.keysym.lower() in jeu :
        jeu[e.keysym.lower()] = True

def key_release (e) :
    if e.keysym.lower() in jeu :
        jeu[e.keysym.lower()] = False

root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)





###########################################################################
## Update (c'est vraiment ce qui fait tourner le jeu faut pas le casser) ##
###########################################################################


def update () :

    if jeu[ej.touche_gauche] :
        dep_ow.deplacement_gauche(canva_jeu, root)

    if jeu[ej.touche_droite] :
        dep_ow.deplacement_droite(canva_jeu, root)

    if jeu["l"] :
        atk.dir_atk (canva_jeu, root, jeu["pos_x"], jeu["pos_y"])

    if len(jeu["lst_mob"]) > 0 :
        for mob in jeu["lst_mob"] :
            mob.f_player(canva_jeu, root)

    g.saut()
    g.physique_verticale(canva_jeu)

    if len(jeu["lst_projectile"]) > 0 :
        mh.d_projectile (canva_jeu)

    if len(jeu["lst_projectile"]) > 0 :
        mh.collision_projectile(canva_jeu)

    root.after(jeu["f_rappel"], update)

update()

root.mainloop()