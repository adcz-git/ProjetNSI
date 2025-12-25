
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
from tableau import tb1, tb2, tb3
from plateforemes import *


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

# le tableau actif

tableau = tb3

# ce sont des carrés de 35x35
def constructeur(tbl) :
    for hauteur in range (18) :
        for largeur in range (32) :
            if tbl[hauteur][largeur] == 1 :
                zone.create_rectangle(35*largeur*zoom, 35*hauteur*zoom, 35*zoom + 35*largeur*zoom, 35*zoom + 35*hauteur*zoom, fill = "black", outline = "yellow")

constructeur(tableau)



###################
##### Touches #####
###################

# C'est beaucoup plus fluide avec un dico
# Et je préfère ZQSD, si vous préférez avec des flèches mettez les variables en commentaire et retirer les """ sur l'autre
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

# faut tomber quand on arrive sur le bord

v_y = 0 # c'est la vitesse de chute, quand on marche on tombe pas
g = 1200*zoom # la gravité on peut modifier la valeur pour sauter plus ou moins haut
chute_yn = False

def physique_verticale():
    global v_y, y, saut_en_cours, chute_yn

    dt = 0.016

    # gravité
    v_y += g * dt
    delta_y = v_y * dt

    # saut court si on relâche la touche
    if not keys["space"] and v_y < 0:
        v_y *= 0.5


    # ===== COLLISION PLAFOND =====
    coord_y_haut = int(y // (35*zoom))
    coord_x = int((x + 25*zoom) // (35*zoom))
    coord_x1 = int(x // (35*zoom))
    coord_x2 = int((x + 50*zoom) // (35*zoom))
    if coord_x2 == 32 :
        coord_x2 -= 1
    
    co_x = [coord_x1, coord_x, coord_x2]
    flag = False
    for i in co_x :
        if tableau[coord_y_haut][i] == 1 :
            flag = True

    if delta_y < 0 and flag :
        v_y = 0
        delta_y = 0

    # déplacement
    zone.move("player", 0, delta_y)
    y += delta_y

    # ===== COLLISION SOL =====
    coord_x1 = int(x // (35*zoom))
    coord_x2 = int((x + 50*zoom) // (35*zoom))
    if (x + 50*zoom) % (35*zoom) == 0:
        coord_x2 -= 1

    coord_y_sol = int((y + 75*zoom) // (35*zoom))
    flag2 = False
    for i in range(coord_x1, coord_x2 + 1):
        if tableau[coord_y_sol][i] == 1 :
            flag2 = True
        
    if flag2 and v_y > 0:
        delta_sol = coord_y_sol*35*zoom - (y + 75*zoom)
        zone.move("player", 0, delta_sol)
        y += delta_sol
        v_y = 0
        saut_en_cours = False
        chute_yn = False



def gauche() :
    global x, y, chute_yn, saut_en_cours
    tmp_x = int(x)
    tmp_y = int(y)
    coord_x = (tmp_x - 5) // (35*zoom)
    coord_y = (tmp_y + 5*zoom) // (35*zoom)
    if x >= 5*zoom :
        if tableau[coord_y][coord_x] != 1 and tableau[coord_y + 1][coord_x] != 1 :
            zone.move("player", -5*zoom, 0)
            x -= 5*zoom

def droite() :
    global x, y, chute_yn, saut_en_cours
    tmp_x = int(x)
    tmp_y = int(y)
    coord_x = (tmp_x + 50*zoom) // (35*zoom)
    coord_y = (tmp_y + 5*zoom) // (35*zoom)
    if x + 50*zoom <= 1115*zoom :
        if tableau[coord_y][coord_x] != 1 and tableau[coord_y + 1][coord_x] != 1 :
            zone.move("player", 5*zoom, 0)
            x += 5*zoom



# pour le saut

# flag pour éviter qu'un couillon spam le saut
saut_en_cours = False

def saut():
    global v_y, saut_en_cours

    if saut_en_cours:
        return

    saut_en_cours = True
    v_y = -600 * zoom  # impulsion vers le haut



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
    
    physique_verticale()


    root.after(16, update)

update()
root.mainloop()