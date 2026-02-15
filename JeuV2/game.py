######################################
######################################
#####           Import           #####
######################################
######################################


import tkinter as tk
import tkinter.font as font
import random

import player
import combat
import etat_jeu as ej
jeu = ej.etat

import tab
import fonction_fuite as ffuite
import fonction_timer as ft
import constructeur_tableau as cons_tbl
import gravite as g
import deplacement_openworld as dep_ow
import fonction_menu as fm
import fonction_attaque as fa



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



# Ces deux fonctions font changer d'état le booléen des touches

def key_press(e) :
    if e.keysym.lower() in jeu :
        jeu[e.keysym.lower()] = True

def key_release (e) :
    if e.keysym.lower() in jeu :
        jeu[e.keysym.lower()] = False

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


cons_tbl.constructeur_tableau (tableau_actuelle, canva_jeu)


###########################################################################
## Update (c'est vraiment ce qui fait tourner le jeu faut pas le casser) ##
###########################################################################


def update () :

    if jeu[ej.touche_gauche] :
        dep_ow.deplacement_gauche(canva_jeu, root)

    if jeu[ej.touche_droite] :
        dep_ow.deplacement_droite(canva_jeu, root)

    g.saut()

    g.physique_verticale(canva_jeu)


    if jeu["etat"] == "fight" and jeu["type_menu"] == "type_action" :
        fm.choix_type_menu(canva_jeu, root)

# verifié
    if jeu["etat"] == "fight" and jeu["type_menu"] == "choix_action" and jeu["tour"] == "atk" and jeu["num_type"] == 3 :
        ffuite.fuite_yn(canva_jeu, root)

    if jeu["curseur"] :
        fm.deplacement_cursor(canva_jeu, root)

    if jeu["c"] :
        root.after(100)
        combat.intro(root, canva_jeu, zoom)
        jeu["etat"] = "fight"

    if jeu["v"] :
        combat.delete_canva(canva_jeu)


    # dans l'interface de combat, c'est ce qui permet de choisir l'action à effectuer
    if jeu["return"] :
        if jeu["type_menu"] == "type_action" :
            if jeu["etat"] == "fight" and jeu["tour"] == "atk" and jeu["type_menu"] == "type_action" :
                combat.creation_menu_action (canva_jeu, zoom)
                jeu["type_menu"] = "choix_action"
            root.after(100)
        
        elif jeu["type_menu"] == "choix_action" :

            if jeu["num_type"] == 0 :
                if not jeu["qte_en_cour"] :
                    jeu["curseur"] = False
                    fa.attaque_joueur(canva_jeu, root)
                    fa.dessin_qte(canva_jeu)
                    fa.attaque_input(canva_jeu, root)
                    
            if jeu["num_type"] == 3 :
                ffuite.action_fuite(canva_jeu, root)
            
    
    # ça sers juste à revenir dans le menu précédent
    if jeu["escape"] :
        if jeu["etat"] == "fight" and jeu["tour"] == "atk" and jeu["type_menu"] == "choix_action" :
            canva_jeu.delete("menu_action")
            jeu["type_menu"] = "type_action"


    root.after(jeu["f_rappel"], update)

update()



        


root.mainloop()