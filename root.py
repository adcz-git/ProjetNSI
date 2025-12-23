
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
from tableau import tb1, tb2


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

tableau = tb2

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
g = 1200*zoom # on garde pas la même gravité que pour le saut il tombe trop vite
chute_yn = False

def chute() :
    global v_y, g, y, chute_yn
    dt = 0.016

    v_y += g * dt # la vitesse augmente en fonction du temps et de la gravité
    y += v_y * dt # moifie la position du personnage

    zone.move("player", 0, v_y * dt)

    coord_x = int(x // (35*zoom))
    coord_y = int((y + 75*zoom) // (35*zoom))
    if tableau[coord_y][coord_x] == 1 :

        delta_sol = coord_y*35*zoom - (y + 75*zoom)
        zone.move("player", 0, delta_sol)
        y += delta_sol
        chute_yn = False
        v_y = 0

        return

    root.after(16, chute)



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
    
        chute_x = int((x + 50*zoom) // (35*zoom))
        chute_y = int((y + 75*zoom) // (35*zoom))

        if tableau[chute_y][chute_x] != 1 and not chute_yn and not saut_en_cours:
            chute_yn = True
            chute()

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
        
        chute_x = int(x // (35*zoom))
        chute_y = int((y + 75*zoom) // (35*zoom))

        if tableau[chute_y][chute_x] != 1 and not chute_yn and not saut_en_cours:
            chute_yn = True
            chute()

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
    acceleration = 450 * zoom
    vitesse_initiale = 300 * zoom

    # pour le boost de saut

    tmp_max = 0.3 # en seconde
    boost_px = 5*zoom # boost en pixel
    compteur_boost = 0
    boost_finie = False

    def saut_update():
        global t, x, y, saut_en_cours
        nonlocal y_initiale, acceleration, vitesse_initiale, tmp_max, boost_px, compteur_boost, boost_finie

        dt = 16 * 0.001
        
        y_old = parabole(acceleration, vitesse_initiale, y_initiale, t)
        y_new = parabole(acceleration, vitesse_initiale, y_initiale, t + dt)
        delta_y = y_new - y_old

        if not keys["space"] :
            boost_finie = True
        
        if keys["space"] and compteur_boost < tmp_max and not boost_finie :
            delta_y -= boost_px
            compteur_boost += 16*0.001

        zone.move("player", 0, delta_y)
        y += delta_y
        t += dt

        coord_x = int(x // (35*zoom))
        coord_y = int((y + 75*zoom) // (35*zoom))
        if tableau[coord_y][coord_x] == 1 :

            delta_sol = coord_y*35*zoom - (y + 75*zoom)
            zone.move("player", 0, delta_sol)
            y += delta_sol

            saut_en_cours = False
            boost_finie = False
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