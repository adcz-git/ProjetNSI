import etat_jeu as ej
jeu = ej.etat
import tkinter as tk
import math
import bar_vie as bar
import deplacement_openworld as openworld

class mob_hostile_1 :
    def __init__ (self, x, y) :
        self.tag = f"mob_{id(self)}" # tag du mob
        self.tracker = f"tracker_{id(self)}" # chaque mob à son propre tracker (le trait en jaune vous pouvez l'enlever aussi c dans f_player)
        self.x = x # coordonné
        self.y = y # idem
        self.pv = 10
        self.dgt = 2
        self.t_atk = False # est qu'il attaque ou pas en gros
        self.timer = 0 # remet le flag à false pour qu'il puisse réattaquer
        self.larg = 100 # largeur du mob
        self.haut = 50 # hauteur du mob
        self.vision = 200 # à combien de pixel il peut attaque le joueur (pas le voir, vraiment l'attaque)
        self.v_projectile = 7 # la vitesse du projectile ça c clair
        self.v_mob = 2

    def hitbox (self, canva) :
        zoom = jeu["zoom"]

        canva.create_rectangle (self.x*zoom, self.y*zoom, (self.x+self.larg)*zoom, (self.y+self.haut)*zoom, outline = "blue", tags = self.tag)

    def f_player (self, canva, racine) :
        zoom = jeu["zoom"]
        d_player = math.sqrt((self.x - jeu["pos_x"])**2 + (self.y - jeu["pos_y"])**2)
        canva.delete(self.tracker)
        canva.create_polygon ((self.x + self.larg//2)*zoom, (self.y + self.haut//2)*zoom, (jeu["pos_x"] + 25)*zoom, (jeu["pos_y"] + 40)*zoom, outline = "yellow", tags = self.tracker)

        if d_player >= self.vision :
            if self.x > jeu["pos_x"] :
                self.move_mob (1, canva)
            else : 
                self.move_mob (2, canva)

        elif not self.t_atk :
            self.t_atk = True
            self.delay_atk(racine)
            self.atk_mob (canva, self.x, self.y, jeu["pos_x"], jeu["pos_y"])

    def move_mob (self, action, canva) :
        zoom = jeu["zoom"]
        if action == 1 :
            limite_deplacement = flag_gauche_mob(self)

            if self.x - self.v_mob*(60 // jeu["fps"]) >= limite_deplacement :

                canva.move(self.tag, -self.v_mob*(60 // jeu["fps"])*zoom, 0)
                self.x -= self.v_mob*(60 // jeu["fps"])

        if action == 2 :
            limite_deplacement = flag_droite_mob(self)
            if self.x + self.v_mob*(60 // jeu["fps"]) <= limite_deplacement :

                canva.move(self.tag, +self.v_mob*(60 // jeu["fps"])*zoom, 0)
                self.x += self.v_mob*(60 // jeu["fps"])

    def atk_mob (self, canva, x_mob, y_mob, x_j, y_j) :
        zoom = jeu["zoom"]
        x, y, angle = calcul_atk (x_mob, y_mob, x_j, y_j, self.v_projectile)

        if x_mob > x_j :
            x = -x
        if y_mob > y_j :
            y = -y

        jeu["lst_projectile"].append ([canva.create_oval ((self.x + 40)*zoom, (self.y + 15)*zoom, (self.x + 60)*zoom, (self.y + 35)*zoom, fill = "red"), x, y, self.x + 50, self.y + 25, self.dgt, 5000, angle])

    def delay_atk (self, racine) :
        if self.timer >= 2000 :
            self.timer = 0
            self.t_atk = False
            return
        else :
            self.timer += jeu["f_rappel"]
            racine.after(jeu["f_rappel"], lambda : self.delay_atk(racine))



def calcul_atk (x_mob, y_mob, x_j, y_j, v_projectile) :
    zoom = jeu["zoom"]

    if x_mob < x_j :
        x_mob, x_j = x_j, x_mob

    adj = x_mob - x_j

    if y_mob < y_j :
        y_mob, y_j = y_j, y_mob

    opp = y_mob - y_j

    angle = math.atan(opp / adj)


    d_x = v_projectile*zoom * math.cos(angle)
    d_y = v_projectile*zoom * math.sin(angle)

    return d_x, d_y, angle

def d_projectile (canva) :
    pro = jeu["lst_projectile"]

    for projectile in pro :
        canva.move (projectile[0], projectile[1], projectile[2])

        projectile[3] += projectile[1]
        projectile[4] += projectile[2]
    

def collision_projectile (canva) :
    zoom = jeu["zoom"]
    pro = jeu["lst_projectile"]

    i_to_del = []

    for proj in range (len(pro)) :
        pro[proj][6] -= jeu["f_rappel"]
        if pro[proj][6] <= 0 :
            i_to_del.append(proj)
            canva.delete(pro[proj][0])

        if jeu["pos_x"] <= pro[proj][3] and pro[proj][3] <= jeu["pos_x"] + 50 :
            if jeu["pos_y"] <= pro[proj][4] and pro[proj][4] <= jeu["pos_y"] + 75 :
                jeu["pv"] -= pro[proj][5]
                canva.delete(pro[proj][0])
                bar.dessin_bar_vie(canva)
                i_to_del.append(proj)
                recul(canva, pro[proj][7])

    for i in range (len(i_to_del)-1, -1, -1) :
        jeu["lst_projectile"].pop (i_to_del[i])



##############################
##############################
####  FLAG DEPLACMENT    #####
##############################
##############################

def flag_gauche_mob(mob) :
    x_tbl = mob.x // 35
    if mob.x % 35 == 0 and x_tbl > 0 :
        x_tbl -= 1

    lst_flag_collision = []
    flag_pas_de_mur = False

    for pt in range (3) :
            
        pt_test = mob.y + (mob.haut//(mob.haut//35 + 1) * pt)
        y_tbl = pt_test // 35
        if pt_test % 35 == 0 and pt == 2 :
            y_tbl -= 1

        while jeu["tbl_act"][y_tbl][x_tbl] != 1 and x_tbl - 1 >= 0 :
            x_tbl -= 1

        if x_tbl == 0 and jeu["tbl_act"][y_tbl][x_tbl] != 1 :
            lst_flag_collision.append(-1)
        else :
            lst_flag_collision.append(x_tbl)


    if lst_flag_collision[0] == lst_flag_collision[1] == lst_flag_collision[2] == -1 :
        flag_pas_de_mur = True

    if flag_pas_de_mur :
        limite_deplacement = 0
    else :
        limite_deplacement = (max(lst_flag_collision) + 1) * 35

    return limite_deplacement




def flag_droite_mob(mob) :
    x_tbl = (mob.x + mob.larg) // 35
    if (mob.x + mob.larg) % 35 == 0 :
        x_tbl -= 1

    lst_flag_collision = []
    flag_pas_de_mur = False
        

    for pt in range (3) :
        
        pt_test = mob.y + (mob.haut//(mob.haut//35 + 1))*pt
        y_tbl = pt_test // 35
        if pt_test % 35 == 0 and pt == 2 :
            y_tbl -= 1

        while jeu["tbl_act"][y_tbl][x_tbl] != 1 and x_tbl + 1 <= 31 :
            x_tbl += 1

        if x_tbl == 31 and jeu["tbl_act"][y_tbl][x_tbl] != 1 :
            lst_flag_collision.append(99)
        else :
            lst_flag_collision.append(x_tbl)

    if lst_flag_collision[0] == lst_flag_collision[1] == lst_flag_collision[2] == 99 :
        flag_pas_de_mur = True

    if flag_pas_de_mur :
        limite_deplacement = 1120
    else :
        limite_deplacement = min(lst_flag_collision) * 35

    return limite_deplacement

def recul(canva, angle) :
    zoom = jeu["zoom"]
    if angle <= math.pi/2 :
        limite_deplacement = openworld.flag_droite()

        if jeu["pos_x"] + 50 + jeu["recul"] <= limite_deplacement :
            canva.move("player", jeu["recul"]*zoom, 0)
            jeu["pos_x"] += jeu["recul"]

    else :
        limite_deplacement = openworld.flag_gauche()

        if jeu["pos_x"] - jeu["recul"] >= limite_deplacement :
            canva.move("player", -jeu["recul"]*zoom, 0)
            jeu["pos_x"] -= jeu["recul"]