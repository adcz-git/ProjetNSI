
#############################################################################
# C'est pour linux qui n'aime pas les dimensions. Vous, laisser le à 1 sauf #
# si la fenêtre est trop petite.                                            #
#############################################################################

zoom = 2

###########################################################################

#################################
### On met les imports ici :) ###
#################################

import tkinter as tk
from player import player
from tableau import tb1


###################
##### Fenêtre #####
###################

root = tk.Tk()
root.title ("Jsp on verra plus tard")
root.geometry(f"{int(1140*zoom)}x{int(650*zoom)}")


#################
##### Canva #####
#################

larg_canva = 1120*zoom
haut_canva = 630*zoom

zone = tk.Canvas (root, width = larg_canva, height = haut_canva, bg = "Grey")
zone.place(x = 10*zoom, y = 10*zoom)


##########################################################
##### La fonctions créer la zone à partir du tableau #####
##### Ce sont des tableaux de 32x18                  ##### 
##########################################################

# ce sont des carrés de 35x35
def constructeur(tbl) :
    for hauteur in range (18) :
        for largeur in range (32) :
            if tbl[hauteur][largeur] == 1 :
                zone.create_rectangle(35*largeur*zoom, 35*hauteur*zoom, 35*zoom + 35*largeur*zoom, 35*zoom + 35*hauteur*zoom, fill = "black", outline = "yellow")

constructeur(tb1)

###################
##### Touches #####
###################

# C'est beaucoup plus fluide avec un dico
# Et je préfère ZQSD, si vous préférez avec des flèches mettez les variables ene commentaire et retirer les """ sur l'autre
# Et faudra faire pareil avec les fonctions qui suivent

touche_haut = "z"
touche_gauche = "q" 
touche_bas = "s"
touche_droite = "d"

"""
touche_haut = "Up"
touche_gauche = "Left" 
touche_bas = "Down"
touche_droite = "Right"
"""

keys = {
    touche_haut : False,
    touche_gauche : False,
    touche_bas : False,
    touche_droite : False,
    "space" : False
}


# Ces deux fonctions modifient l'état des touches quand on appuie et qu'on relache. Ça marche bcp mieux que de juste bind une touche sur une fonction

def key_press(e) :
    if e.keysym in keys :
        keys[e.keysym] = True

def key_release (e) :
    if e.keysym in keys :
        keys[e.keysym] = False

##########################################
##### La c'est pour bind les touches #####
##########################################

root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)


######################
##### Personnage #####
######################

# On y stock les positions du player :
x = 800*zoom
y = 450*zoom

player(x, y, zone, zoom) # et le faire apparaître c'est pas mal aussi



#######################
##### Déplacement #####
#######################

def gauche() :
    global x, y
    x = int(x)
    y = int(y)
    coord_x = x // (35*zoom)
    coord_y = (y + 5*zoom) // (35*zoom)
    if x >= 5*zoom :
        if tb1[coord_y][coord_x] != 1 and tb1[coord_y + 1][coord_x] != 1 :
            zone.move("player", -5*zoom, 0)
            x -= 5*zoom

def droite() :
    global x, y
    x = int(x)
    y = int(y)
    coord_x = (x + 50*zoom) // (35*zoom)
    coord_y = (y + 5*zoom) // (35*zoom)
    if x + 50*zoom <= 1115*zoom :
        if tb1[coord_y][coord_x] != 1 and tb1[coord_y + 1][coord_x] != 1 :
            zone.move("player", 5*zoom, 0)
            x += 5*zoom

# pour le saut

# flag pour éviter qu'un couillon spam le saut
saut_en_cours = False
t = 0 # ça gère la hauteur en fonction du temps


# on gère le saut avec une équation parabolique

def parabole(acc, v_init, y_init, t) :
    return (acc * t * t) - (v_init * t) + y_init
    # acc : accélération
    # v_init : vitesse initiale
    # y_init : hauteur initiale du perso
    # t : duré


def saut():
    global saut_en_cours, y, t

    if saut_en_cours:
        return

    saut_en_cours = True
    t = 0

    y_initiale = y
    acceleration = 600 * zoom
    vitesse_initiale = 600 * zoom

    def saut_update():
        global t, y, saut_en_cours
        nonlocal y_initiale, acceleration, vitesse_initiale

        dt = 16 * 0.001

        y_old = parabole(acceleration, vitesse_initiale, y_initiale, t)
        y_new = parabole(acceleration, vitesse_initiale, y_initiale, t + dt)
        delta_y = y_new - y_old

        zone.move("player", 0, delta_y)
        y = y_new
        t += dt

        if y >= y_initiale:
            zone.move("player", 0, y_initiale - y)
            y = y_initiale
            saut_en_cours = False
            return

        root.after(16, saut_update)

    saut_update()




###########################################################################
## Update (c'est vraiment ce qui fait tourner le jeu faut pas le casser) ##
###########################################################################

def update() :
    if keys[touche_gauche] :
        gauche()
    if keys[touche_droite] :
        droite()
    if keys["space"] :
        saut()


    root.after(16, update)



update()
root.mainloop()