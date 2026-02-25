import tkinter as tk
import etat_jeu as ej
import mob_hostile_1 as mh

jeu = ej.etat

def dir_atk (canva, racine, x, y) :
    if jeu[ej.touche_haut] and not jeu["atk_en_cour"] :
        h_trace (canva, racine, x, y)
        atk_joueur (canva, racine, 2)

    elif jeu[ej.touche_bas] and not jeu["atk_en_cour"] :
        b_trace (canva, racine, x, y)
        atk_joueur (canva, racine, 3)

    elif jeu[ej.touche_droite] and not jeu["atk_en_cour"] :
        d_trace (canva, racine, x+50, y)
        atk_joueur (canva, racine, 1)

    elif jeu[ej.touche_gauche] and not jeu["atk_en_cour"] :
        g_trace (canva, racine, x, y)
        atk_joueur (canva, racine, 0)

    else :
        if jeu["der_depla"] == "d" and not jeu["atk_en_cour"] :
            d_trace (canva, racine, x+50, y)
            atk_joueur (canva, racine, 1)

        if jeu["der_depla"] == "g" and not jeu["atk_en_cour"] :
            g_trace (canva, racine, x, y)
            atk_joueur (canva, racine, 0)



def timer_atk (canva, racine) :
    if jeu["timer_atk"] >= 400 :
        jeu["atk_en_cour"] = False
        jeu["del_trace"] = False
        return

    elif not jeu["del_trace"] and jeu["timer_atk"] >= 100 :
        jeu["del_trace"] = True
        canva.delete("trace_atk")
        racine.after(jeu["f_rappel"], lambda : timer_atk (canva, racine))

    else :
        jeu["timer_atk"] += jeu["f_rappel"]
        racine.after(jeu["f_rappel"], lambda : timer_atk (canva, racine))


def g_trace (canva, racine, x, y, etape = 0) :
    zoom = jeu["zoom"]

    jeu["timer_atk"] = 0
    jeu["atk_en_cour"] = True
    timer_atk(canva, racine)

    canva.create_rectangle(x*zoom, (y-5)*zoom, (x-100)*zoom, (y + 85)*zoom, outline = "red", tags = "trace_atk")

def d_trace (canva, racine, x, y, etape = 0) : 
    zoom = jeu["zoom"]

    jeu["timer_atk"] = 0
    jeu["atk_en_cour"] = True
    timer_atk(canva, racine)

    canva.create_rectangle(x*zoom, (y-5)*zoom, (x+100)*zoom, (y + 85)*zoom, outline = "red", tags = "trace_atk")

def h_trace (canva, racine, x, y, etape = 0) :
    zoom = jeu["zoom"]

    jeu["timer_atk"] = 0
    jeu["atk_en_cour"] = True
    timer_atk(canva, racine)

    canva.create_rectangle((x-20)*zoom, (y+5)*zoom, (x+70)*zoom, (y - 95)*zoom, outline = "red", tags = "trace_atk")

def b_trace (canva, racine, x, y, etape = 0) : 
    zoom = jeu["zoom"]

    jeu["timer_atk"] = 0
    jeu["atk_en_cour"] = True
    timer_atk(canva, racine)

    canva.create_rectangle((x-20)*zoom, (y+75)*zoom, (x+70)*zoom, (y + 175)*zoom, outline = "red", tags = "trace_atk")

def atk_joueur (canva, racine, dir) :
    if dir == 0 :
        for mob in jeu["lst_mob"] :
            flag_x = False
            for coord in range (mob.x, mob.x + mob.larg) :
                if jeu["pos_x"] - 100 <= coord and coord <= jeu["pos_x"] :
                    flag_x = True
                    break
            if flag_x :
                flag_y = False
                for coord in range (mob.y, mob.y + mob.haut) :
                    if jeu["pos_y"] - 5 <= coord and coord <= jeu["pos_y"] + 85 :
                        flag_y = True
                        break
                if flag_y :
                    coup (canva, racine, mob, dir)

    if dir == 1 :
        for mob in jeu["lst_mob"] :
            flag_x = False
            for coord in range (mob.x, mob.x + mob.larg) :
                if jeu["pos_x"] + 50 <= coord and coord <= jeu["pos_x"] + 150:
                    flag_x = True
                    break

            if flag_x :
                flag_y = False
                for coord in range (mob.y, mob.y + mob.haut) :
                    if jeu["pos_y"] - 5 <= coord and coord <= jeu["pos_y"] + 85 :
                        flag_y = True
                        break
                if flag_y :
                    coup (canva, racine, mob, dir)

    if dir == 2 :
        for mob in jeu["lst_mob"] :
            flag_x = False
            for coord in range (mob.x, mob.x + mob.larg) :
                if jeu["pos_x"] - 20 <= coord and coord <= jeu["pos_x"] + 70 :
                    flag_x = True
                    break

            if flag_x :
                flag_y = False
                for coord in range (mob.y, mob.y + mob.haut) :
                    if jeu["pos_y"] - 95 <= coord and coord <= jeu["pos_y"] + 5 :
                        flag_y = True
                        break
                if flag_y :
                    coup (canva, racine, mob, dir)

    if dir == 3 :
        for mob in jeu["lst_mob"] :
            flag_x = False
            for coord in range (mob.x, mob.x + mob.larg) :
                if jeu["pos_x"] - 20 <= coord and coord <= jeu["pos_x"] + 70 :
                    flag_x = True
                    break

            if flag_x :
                flag_y = False
                for coord in range (mob.y, mob.y + mob.haut) :
                    if jeu["pos_y"] + 75 <= coord and coord <= jeu["pos_y"] + 175 :
                        flag_y = True
                        break
                if flag_y :
                    coup (canva, racine, mob, dir)


def coup (canva, racine, mob, dir) :
    zoom = jeu["zoom"]

    mob.pv -= 4
    print(mob.pv)
    if mob.pv <= 0 :
        mob.timer = 0
        jeu["lst_mob"].pop (jeu["lst_mob"].index(mob))
        mort_mob (canva, racine, mob)
        return

    mouv = 40
    if dir == 0 :
        limite_deplacement = mh.flag_gauche_mob (mob)

        if mob.x - mouv >= limite_deplacement :

            canva.move(mob.tag, -mouv*zoom, 0)
            mob.x -= mouv

    if dir == 1 :
        limite_deplacement = mh.flag_droite_mob (mob)

        if mob.x + mouv <= limite_deplacement :
            canva.move(mob.tag, mouv*zoom, 0)
            mob.x += mouv

def mort_mob (canva, racine, mob, sens = 1, compteur = 0) :
    zoom = jeu["zoom"]
    if mob.timer >= 50 :
        mob.timer = 0
        if sens == 1 :
            canva.move (mob.tag, -10*zoom, 0)
        else :
            canva.move (mob.tag, 10*zoom, 0)

        if compteur == 20 :
            canva.delete (mob.tag, mob.tracker)
            return
        
        racine.after (jeu["f_rappel"], lambda : mort_mob (canva, racine, mob, -sens, compteur + 1))
    
    else :
        mob.timer += jeu["f_rappel"]
        racine.after (jeu["f_rappel"], lambda : mort_mob (canva, racine, mob, sens, compteur))