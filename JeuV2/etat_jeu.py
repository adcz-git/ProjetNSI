
##########################################################
##########################################################
##### C'est ici qu'est stocké tous les états du jeux #####
##########################################################
##########################################################

import tab
import tableau
import script_mob as sm

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

    # touche temporaire
    "c" : False, 
    "v" :False,

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
    "lst_input" : ["", "", "", "", "", ""],
    "couleur_en_cour" : "",
    "num_input" : 0,
    "patern_donne" : "",

    "temps_max_atk" : 4000,

    # Le mob qu'on affronte 
    "mob_en_cours" : 0,
    "pv_mob" : 0,

    "inventaire" : [["truc"], ["machin"], ["bidule"], [], [], []]

}

lst_mob = ["victime", "gary"]
lst_fonction_mob = [sm.victime, sm.gary]

dico_mob = {
    "victime" : {
        "pv" : 20, 
        "couleur1" : "vert", 
        "couleur2" : "rouge",
        "patern" : "qzds",
        "x" : 480, 
        "y" : 200,
        "temps_atk" : 4000,
        "degat" : 5
        },
    "gary" : {
        "pv" : 999999,
        "patern" : "qdzqdzqsqdz",
        "x" : 550,
        "y" : 230,
        "temps_atk" : 8000,
        "degat" : 999999
    }
}