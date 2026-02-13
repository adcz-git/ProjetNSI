
##########################################################
##########################################################
##### C'est ici qu'est stocké tous les états du jeux #####
##########################################################
##########################################################

import tab
import tableau

""" 
toutes les clés liés aux positions du personnage ou de quoi
que ce soit dans le jeu est indiqué sans le facteur zoom
"""

etat = {

    # Apparence générale
    "zoom" : 2,
    "fps" : 60, # remplacer par 30 si besoin
    "f_rappel" : 1000 // 60, # remplacer 60 par la valeur de fps

    # Etat global du jeu
    "pv_joueur" : 10,

    "tbl_act" : tableau.tb0,#tab.monde[0,2]
    "etat" : "openworld",

    # Position du joueur et déplacement
    "pos_x" : 800,
    "pos_y" : 450,

    "v_vert" : 0,
    "gravite" : 1200,
    "is_on_ground" : True,
    "collision_plafond" : False,
    "collision_sol" : False,

    # Menu de combat
    "type_menu" : "type_action",
    "num_type" : 0,# 0 attaque; 1 duo; 2 item; 3 fuite 
    "tour" : "atk",

    "curseur" : False,
    "pos_curseur" : [0,0],

    "choix_fuite" : 0,
    "fuite_en_cour" : False,

    "enter_en_cour" : False,

    "timer" : 0,

    "qte_en_cour" : False,

    "input_box" : "",

    # Le mob qu'on affronte 
    "mob_en_cours" : 0,
    "pv_mob" : 0,

    "inventaire" : [["truc"], ["machin"], ["bidule"], [], [], []]

}

lst_mob = ["victime"]

dico_mob = {
    "victime" : [20, "vert", "rouge", 1, "gau, hau, dro, bas"]
}