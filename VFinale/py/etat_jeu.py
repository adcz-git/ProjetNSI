
##########################################################
##########################################################
##### C'est ici qu'est stocké tous les états du jeux #####
##########################################################
##########################################################

import tableau

""" 
toutes les clés liés aux positions du personnage ou de quoi
que ce soit dans le jeu est indiqué sans le facteur zoom
"""

touche_haut = "z"
touche_gauche = "q" 
touche_bas = "s"
touche_droite = "d"

# On les stock dans un dictionnaire
# Lorsqu'une touche est pressée, le booléen passse sur True et 
# la fonction associée sera exécutée jusqu'au relachement de la 
# touche, le booléen sera replacé sur False

etat = {

    touche_haut : False,
    touche_gauche : False,
    touche_bas : False,
    touche_droite : False,
    "space" : False,
    "return" : False,
    "escape" : False,

    # Attaque du joueur
    "l" : False,

    "timer_atk" : 0,
    "atk_en_cour" : False,
    "del_trace" : False,

    # Apparence générale
    "zoom" : 1,
    "fps" : 60, # remplacer par 30 si besoin
    "f_rappel" : 1000 // 60, # remplacer 60 par la valeur de fps

    # Etat global du jeu

    "tbl_act" : tableau.tb0, #tab.monde[0,2]

    # Position du joueur et déplacement
    "pos_x" : 800,
    "pos_y" : 450,

    "der_depla" : "d",

    "v_vert" : 0,
    "gravite" : 1200,
    "is_on_ground" : True,
    "collision_plafond" : False,
    "collision_sol" : False,
    "recul" : 40,

    "pv" : 10,

    # Mob présent 
    "lst_mob" : [],
    "lst_projectile" : [],

}