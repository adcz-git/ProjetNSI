from PIL import Image, ImageTk
import tkinter.font as font
import tkinter as tk
import os

import etat_jeu as ej
import script_mob as sm

#####################################################################
#####################################################################
##### Ici c'est l'intro (la petite page noire qui pop au début) #####
#####################################################################
#####################################################################

"""
Ca ne fait qu'apparaitre une page noir qui au bout d'1 ou 2 seconde
laisse place au combat
"""

def intro (root, canva, zoom = 1) :

    canva.create_rectangle(0, 0, 1120*zoom, 630*zoom, fill = "#000000", tags = "intro")

    police = font.Font(family="Times New Roman", size = 112, weight = "bold")

    #titre1 = tk.Label(root, text = "Gary", bg = "#000000", fg = "#FFFFFF", font = police)
    #titre1.place(x = 400*zoom, y = 40*zoom)

    canva.create_text ( 550*zoom, 80*zoom, text = "", fill = "#FFFFFF",  font = police, tags = "intro")

    #titre2 = tk.Label(root, text = "conqueror of", bg = "#000000", fg = "#FFFFFF", font = police)
    #titre2.place(x = 150*zoom, y = 220*zoom)

    canva.create_text ( 550*zoom, 260*zoom, text = "", fill = "#FFFFFF", font = police, tags = "intro" )

    #titre3 = tk.Label(root, text = "worlds", bg = "#000000", fg = "#FFFFFF", font = police)
    #titre3.place(x = 350*zoom, y = 400*zoom)

    canva.create_text ( 550*zoom, 440*zoom, text = "", fill = "#FFFFFF", font = police, tags = "intro")

    canva.after(1100, lambda : combat (canva, zoom))





#####################################################################################
#####################################################################################
##### Le premier menu, où l'on choisi l'action ou que l'on se défend, dépendant #####
##### du rôle que l'on joue (attaque ou défense)                                #####
#####################################################################################
#####################################################################################


lst_menu = ["", "", "", ""]

def combat (canva, zoom = 1) :
    global lst_menu

    ###########################################################
    ###########################################################
    ### Permanent, peut importe si c'est attaque ou défense ###
    ###########################################################
    ###########################################################


    canva.delete("intro")

    police = font.Font(size = 22, weight = "bold")

    # c'est le fond de l'interfarce pour le combat
    canva.create_rectangle(0, 0, 1120*zoom, 630*zoom, fill = "#000000", tags = "combat")

    # le menu texte pour le joueur
    canva.create_rectangle(75*zoom, 350*zoom, 1045*zoom, 550*zoom, fill = "grey", tags = "combat")
    canva.create_rectangle(80*zoom, 355*zoom, 1040*zoom, 545*zoom, fill = "#000000", tags = "combat")


    ################################
    ################################
    #####     Menu attaque     #####
    ################################
    ################################

    if ej.etat["tour"] == "atk" :


        #####################################
        ##### Reset la position du menu #####
        #####################################

        ej.etat["num_type"] = 0


        ################################
        ##### Chemin d'accès image #####
        ################################

        BASE_DIR = os.path.dirname(__file__)


        ########################
        ##### Menu 1 : Atk #####
        ########################

        menu_atk = canva.create_rectangle(238*zoom, 560*zoom, 388*zoom, 620*zoom, fill = "white", tags = "combat")
        lst_menu[0] = (menu_atk)
        canva.create_rectangle(243*zoom, 565*zoom, 383*zoom, 615*zoom, fill = "black", tags = "combat")
        canva.create_text ( 330*zoom, 590*zoom, text = "Atk", fill = "#FFFFFF",  font = police, tags = "combat")


        atk_normal_path = os.path.join(BASE_DIR, "Image", "atk_normal.png")

        img_atk_normal = Image.open(atk_normal_path).convert("RGBA")
        img_atk_normal = img_atk_normal.resize((int(40*zoom), int(40*zoom)), Image.NEAREST)

        img_atk_normal = ImageTk.PhotoImage(img_atk_normal)
        canva.atk_normal_img = img_atk_normal

        canva.create_image(270*zoom, 590*zoom, image=img_atk_normal, tags="combat")


        ########################
        ##### Menu 2 : Duo #####
        ########################

        menu_bicolore = canva.create_rectangle(403*zoom, 560*zoom, 553*zoom, 620*zoom, fill = "grey", tags = "combat")
        lst_menu[1] = (menu_bicolore)
        canva.create_rectangle(408*zoom, 565*zoom, 548*zoom, 615*zoom, fill = "black", tags = "combat")
        canva.create_text ( 500*zoom, 590*zoom, text = "Duo", fill = "#FFFFFF",  font = police, tags = "combat")


        atk_path = os.path.join(BASE_DIR, "Image", "atk.png")

        img_atk = Image.open(atk_path).convert("RGBA")
        img_atk = img_atk.resize((int(40*zoom), int(40*zoom)), Image.NEAREST)

        img_atk = ImageTk.PhotoImage(img_atk)
        canva.atk_img = img_atk

        canva.create_image(440*zoom, 590*zoom, image=img_atk, tags="combat")


        ########################
        ##### Menu 3 : Obj #####
        ########################

        menu_heal = canva.create_rectangle(568*zoom, 560*zoom, 718*zoom, 620*zoom, fill = "grey", tags = "combat")
        lst_menu[2] = (menu_heal)
        canva.create_rectangle(573*zoom, 565*zoom, 713*zoom, 615*zoom, fill = "black", tags = "combat")
        canva.create_text (660*zoom, 590*zoom, text = "Heal", fill = "#FFFFFF",  font = police, tags = "combat")


        heal_path = os.path.join(BASE_DIR, "Image", "heal.png")

        img_heal = Image.open(heal_path).convert("RGBA")
        img_heal = img_heal.resize((int(40*zoom), int(40*zoom)), Image.NEAREST)

        img_heal = ImageTk.PhotoImage(img_heal)
        canva.heal_img = img_heal

        canva.create_image(600*zoom, 590*zoom, image=img_heal, tags="combat")


        ########################
        ##### Menu 4 : Fte #####
        ########################

        menu_fuite = canva.create_rectangle(733*zoom, 560*zoom, 883*zoom, 620*zoom, fill = "grey", tags = "combat")
        lst_menu[3] = (menu_fuite)
        canva.create_rectangle(738*zoom, 565*zoom, 878*zoom, 615*zoom, fill = "black", tags = "combat")
        canva.create_text ( 825*zoom, 590*zoom, text = "Run", fill = "#FFFFFF",  font = police, tags = "combat")
 

        run_path = os.path.join(BASE_DIR, "Image", "run.png")

        img_run = Image.open(run_path).convert("RGBA")
        img_run = img_run.resize((int(40*zoom), int(40*zoom)), Image.NEAREST)

        img_run = ImageTk.PhotoImage(img_run)
        canva.run_img = img_run

        canva.create_image(760*zoom, 590*zoom, image=img_run, tags="combat")

    


    ################################
    ################################
    #####     Menu défense     #####
    ################################
    ################################

    if ej.etat["tour"] == "def" :

        sm.victime(canva, zoom)

        canva.create_rectangle(485*zoom, 570*zoom, 635*zoom, 600*zoom, fill = 'grey', tags = "combat")
        canva.create_rectangle(485*zoom, 570*zoom, (485 + int(150*(ej.etat["pv_joueur"] / 10)))*zoom, 600*zoom, fill = 'white', tags = "combat")




############################################################
############################################################
##### Le sous menu, où l'on choisi l'action à exécuter #####
############################################################
############################################################

lst_fuite = ["", ""]

def creation_menu_action (canva, zoom) :
    global lst_fuite


    #############################
    ##### Police d'écriture #####
    #############################

    police = font.Font(size = 28, weight = "bold")


    ##########################
    #### Type de menu atk ####
    ##########################

    if ej.etat["num_type"] == 0 :

        cursor(canva, zoom)

        canva.create_text ( 265*zoom, 410*zoom, text = "Violet", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(170*zoom, 395*zoom, 200*zoom, 425*zoom, fill = 'purple', tags = "menu_action")

        canva.create_text ( 560*zoom, 410*zoom, text = "Blue", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(470*zoom, 395*zoom, 500*zoom, 425*zoom, fill = 'blue', tags = "menu_action")

        canva.create_text ( 860*zoom, 410*zoom, text = "Vert", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(770*zoom, 395*zoom, 800*zoom, 425*zoom, fill = 'green', tags = "menu_action")

        canva.create_text ( 265*zoom, 480*zoom, text = "Jaune", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(170*zoom, 465*zoom, 200*zoom, 495*zoom, fill = 'yellow', tags = "menu_action")

        canva.create_text ( 585*zoom, 480*zoom, text = "Orange", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(470*zoom, 465*zoom, 500*zoom, 495*zoom, fill = 'orange', tags = "menu_action")

        canva.create_text ( 880*zoom, 480*zoom, text = "Rouge", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(770*zoom, 465*zoom, 800*zoom, 495*zoom, fill = 'red', tags = "menu_action")


    ##########################
    #### Type de menu duo ####
    ##########################

    if ej.etat["num_type"] == 1 :

        cursor(canva, zoom)

        canva.create_text ( 285*zoom, 410*zoom, text = "Rou/Jau", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_polygon(170*zoom, 395*zoom, 200*zoom, 395*zoom, 170*zoom, 425*zoom, fill = 'red', tags = "menu_action")
        canva.create_polygon(170*zoom, 425*zoom, 200*zoom, 395*zoom, 200*zoom, 425*zoom, fill = 'yellow', tags = "menu_action")

        canva.create_text ( 585*zoom, 410*zoom, text = "Jau/Ble", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_polygon(470*zoom, 395*zoom, 500*zoom, 395*zoom, 470*zoom, 425*zoom, fill = 'yellow', tags = "menu_action")
        canva.create_polygon(470*zoom, 425*zoom, 500*zoom, 395*zoom, 500*zoom, 425*zoom, fill = 'blue', tags = "menu_action")

        canva.create_text ( 885*zoom, 410*zoom, text = "Ble/Rou", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_polygon(770*zoom, 395*zoom, 800*zoom, 395*zoom, 770*zoom, 425*zoom, fill = 'blue', tags = "menu_action")
        canva.create_polygon(770*zoom, 425*zoom, 800*zoom, 395*zoom, 800*zoom, 425*zoom, fill = 'red', tags = "menu_action")

        canva.create_text ( 285*zoom, 480*zoom, text = "Ora/Ver", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_polygon(170*zoom, 465*zoom, 200*zoom, 465*zoom, 170*zoom, 495*zoom, fill = 'orange', tags = "menu_action")
        canva.create_polygon(170*zoom, 495*zoom, 200*zoom, 465*zoom, 200*zoom, 495*zoom, fill = 'green', tags = "menu_action")

        canva.create_text ( 585*zoom, 480*zoom, text = "Ver/Vio", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_polygon(470*zoom, 465*zoom, 500*zoom, 465*zoom, 470*zoom, 495*zoom, fill = 'green', tags = "menu_action")
        canva.create_polygon(470*zoom, 495*zoom, 500*zoom, 465*zoom, 500*zoom, 495*zoom, fill = 'purple', tags = "menu_action")

        canva.create_text ( 885*zoom, 480*zoom, text = "Vio/Ora", fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_polygon(770*zoom, 465*zoom, 800*zoom, 465*zoom, 770*zoom, 495*zoom, fill = 'purple', tags = "menu_action")
        canva.create_polygon(770*zoom, 495*zoom, 800*zoom, 465*zoom, 800*zoom, 495*zoom, fill = 'orange', tags = "menu_action")

    ##########################
    #### Type de menu obj ####
    ##########################

    if ej.etat["num_type"] == 2 :

        cursor(canva, zoom)

        canva.create_text ( 265*zoom, 410*zoom, text = ej.etat["inventaire"][0], fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(170*zoom, 395*zoom, 200*zoom, 425*zoom, fill = '#FFFFFF', tags = "menu_action")

        canva.create_text ( 560*zoom, 410*zoom, text = ej.etat["inventaire"][1], fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(470*zoom, 395*zoom, 500*zoom, 425*zoom, fill = '#FFFFFF', tags = "menu_action")

        canva.create_text ( 860*zoom, 410*zoom, text = ej.etat["inventaire"][2], fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(770*zoom, 395*zoom, 800*zoom, 425*zoom, fill = '#FFFFFF', tags = "menu_action")

        canva.create_text ( 265*zoom, 480*zoom, text = ej.etat["inventaire"][3], fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(170*zoom, 465*zoom, 200*zoom, 495*zoom, fill = '#FFFFFF', tags = "menu_action")

        canva.create_text ( 585*zoom, 480*zoom, text = ej.etat["inventaire"][4], fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(470*zoom, 465*zoom, 500*zoom, 495*zoom, fill = '#FFFFFF', tags = "menu_action")

        canva.create_text ( 880*zoom, 480*zoom, text = ej.etat["inventaire"][5], fill = "#FFFFFF",  font = police, tags = "menu_action")
        canva.create_rectangle(770*zoom, 465*zoom, 800*zoom, 495*zoom, fill = '#FFFFFF', tags = "menu_action")

    ##########################
    #### Type de menu fte ####
    ##########################



    if ej.etat["num_type"] == 3 :

        ej.etat["choix_fuite"] = 0
        canva.create_text ( 550*zoom, 420*zoom, text = "Êtes-vous sûr(e) de vouloir fuir ?", fill = "#FFFFFF",  font = police, tags = "menu_action")
        yes = canva.create_rectangle(340*zoom, 460*zoom, 540*zoom, 520*zoom, fill = "white", tags = "menu_action")
        lst_fuite[0] = yes
        canva.create_rectangle(345*zoom, 465*zoom, 535*zoom, 515*zoom, fill = "black", tags = "menu_action")
        canva.create_text ( 440*zoom, 487*zoom, text = "Oui", fill = "#FFFFFF",  font = police, tags = "menu_action")

        no = canva.create_rectangle(580*zoom, 460*zoom, 780*zoom, 520*zoom, fill = "grey", tags = "menu_action")
        lst_fuite[1] = no
        canva.create_rectangle(585*zoom, 465*zoom, 775*zoom, 515*zoom, fill = "black", tags = "menu_action")
        canva.create_text ( 680*zoom, 487*zoom, text = "Non", fill = "#FFFFFF",  font = police, tags = "menu_action")

##########################################################
##########################################################
##### Le curseur (pop uniquement dans certains menu) #####
##########################################################
##########################################################


def cursor (canva, zoom) :

    ej.etat["curseur"] = True
    ej.etat["pos_curseur"] = [0,0]

    canva.create_polygon (110*zoom, 395*zoom, 140*zoom, 410*zoom, 110*zoom, 425*zoom, 120*zoom, 410*zoom, fill = "white", tags = ("cursor", "menu_action"))


def fin_combat(canva) :
    canva.delete("combat")
    ej.etat["etat"] = "openworld"
    ej.etat["tour"] = "atk"
    