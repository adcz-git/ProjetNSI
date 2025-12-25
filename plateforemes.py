from tkinter import *

def grande_plateforme(x, y, canva, zoom=1):
    bg1 = canva.create_rectangle(x, y, x+150*zoom, y+15*zoom, fill="#000000")
    bg2 = canva.create_rectangle(x+5*zoom, y+15*zoom, x+140*zoom, y+20*zoom, fill="#000000")
    bg3 = canva.create_rectangle(x+30*zoom, y+20*zoom, x+35*zoom, y+25*zoom, fill="#000000")
    bg4 = canva.create_rectangle(x+55*zoom, y+20*zoom, x+70*zoom, y+30*zoom, fill="#000000")
    bg5 = canva.create_rectangle(x+60*zoom, y+25*zoom, x+65*zoom, y+35*zoom, fill="#000000")

    # Contours
    ct1 = canva.create_rectangle(x, y, x+150*zoom, y+5*zoom, fill="#FFFFFF", outline="")
    ct2 = canva.create_rectangle(x, y, x+5*zoom, y+15*zoom, fill="#FFFFFF", outline="")
    ct3 = canva.create_rectangle(x+145*zoom, y, x+150*zoom, y+15*zoom, fill="#FFFFFF", outline="")
    ct4 = canva.create_rectangle(x+5*zoom, y+15*zoom, x+25*zoom, y+20*zoom, fill="#FFFFFF", outline="")
    ct5 = canva.create_rectangle(x+40*zoom, y+15*zoom, x+50*zoom, y+20*zoom, fill="#FFFFFF", outline="")
    ct6 = canva.create_rectangle(x+75*zoom, y+15*zoom, x+105*zoom, y+20*zoom, fill="#FFFFFF", outline="")
    ct7 = canva.create_rectangle(x+110*zoom, y+15*zoom, x+145*zoom, y+20*zoom, fill="#FFFFFF", outline="")
    ct8 = canva.create_rectangle(x+25*zoom, y+20*zoom, x+30*zoom, y+25*zoom, fill="#FFFFFF", outline="")
    ct9 = canva.create_rectangle(x+30*zoom, y+25*zoom, x+35*zoom, y+30*zoom, fill="#FFFFFF", outline="")
    ct10 = canva.create_rectangle(x+35*zoom, y+20*zoom, x+40*zoom, y+25*zoom, fill="#FFFFFF", outline="")
    ct11 = canva.create_rectangle(x+50*zoom, y+20*zoom, x+55*zoom, y+25*zoom, fill="#FFFFFF", outline="")
    ct12 = canva.create_rectangle(x+55*zoom, y+25*zoom, x+60*zoom, y+35*zoom, fill="#FFFFFF", outline="")
    ct13 = canva.create_rectangle(x+60*zoom, y+35*zoom, x+65*zoom, y+40*zoom, fill="#FFFFFF", outline="")
    ct14 = canva.create_rectangle(x+65*zoom, y+25*zoom, x+70*zoom, y+35*zoom, fill="#FFFFFF", outline="")
    ct15 = canva.create_rectangle(x+70*zoom, y+15*zoom, x+75*zoom, y+25*zoom, fill="#FFFFFF", outline="")
    ct16 = canva.create_rectangle(x+105*zoom, y+20*zoom, x+110*zoom, y+25*zoom, fill="#FFFFFF", outline="")


def petite_plateforme(x, y, canva, zoom=1):
    bg1 = canva.create_rectangle(x, y, x+55*zoom, y+10*zoom, fill="#000000")
    bg2 = canva.create_rectangle(x+5*zoom, y+10*zoom, x+50*zoom, y+15*zoom, fill="#000000")
    bg3 = canva.create_rectangle(x+25*zoom, y+15*zoom, x+30*zoom, y+20*zoom, fill="#000000")

    ct1 = canva.create_rectangle(x, y, x+55*zoom, y+5*zoom, fill="#FFFFFF", outline="")
    ct2 = canva.create_rectangle(x, y+5*zoom, x+5*zoom, y+10*zoom, fill="#FFFFFF", outline="")
    ct3 = canva.create_rectangle(x+5*zoom, y+10*zoom, x+10*zoom, y+15*zoom, fill="#FFFFFF", outline="")
    ct4 = canva.create_rectangle(x+10*zoom, y+15*zoom, x+25*zoom, y+20*zoom, fill="#FFFFFF", outline="")
    ct5 = canva.create_rectangle(x+25*zoom, y+20*zoom, x+30*zoom, y+25*zoom, fill="#FFFFFF", outline="")
    ct6 = canva.create_rectangle(x+30*zoom, y+15*zoom, x+45*zoom, y+20*zoom, fill="#FFFFFF", outline="")
    ct7 = canva.create_rectangle(x+45*zoom, y+10*zoom, x+50*zoom, y+15*zoom, fill="#FFFFFF", outline="")
    ct8 = canva.create_rectangle(x+50*zoom, y+5*zoom, x+55*zoom, y+10*zoom, fill="#FFFFFF", outline="")


def plateforme_L(x, y, canva, zoom=1):
    bg1 = canva.create_rectangle(x, y+20*zoom, x+70*zoom, y+30*zoom, fill="#000000")
    bg2 = canva.create_rectangle(x+5*zoom, y+30*zoom, x+70*zoom, y+35*zoom, fill="#000000")
    bg3 = canva.create_rectangle(x+35*zoom, y+35*zoom, x+40*zoom, y+40*zoom, fill="#000000")
    bg4 = canva.create_rectangle(x+45*zoom, y, x+80*zoom, y+25*zoom, fill="#000000")
    bg5 = canva.create_rectangle(x+45*zoom, y, x+85*zoom, y+20*zoom, fill="#000000")
    bg6 = canva.create_rectangle(x+45*zoom, y, x+115*zoom, y+15*zoom, fill="#000000")

    ct1 = canva.create_rectangle(x, y+20*zoom, x+50*zoom, y+25*zoom, fill="#FFFFFF", outline="")
    ct2 = canva.create_rectangle(x, y+20*zoom, x+5*zoom, y+30*zoom, fill="#FFFFFF", outline="")
    ct3 = canva.create_rectangle(x+5*zoom, y+30*zoom, x+10*zoom, y+35*zoom, fill="#FFFFFF", outline="")
    ct4 = canva.create_rectangle(x+10*zoom, y+35*zoom, x+35*zoom, y+40*zoom, fill="#FFFFFF", outline="")
    ct5 = canva.create_rectangle(x+35*zoom, y+40*zoom, x+40*zoom, y+45*zoom, fill="#FFFFFF", outline="")
    ct6 = canva.create_rectangle(x+40*zoom, y+35*zoom, x+65*zoom, y+40*zoom, fill="#FFFFFF", outline="")
    ct7 = canva.create_rectangle(x+65*zoom, y+25*zoom, x+70*zoom, y+35*zoom, fill="#FFFFFF", outline="")
    ct8 = canva.create_rectangle(x+70*zoom, y+20*zoom, x+80*zoom, y+25*zoom, fill="#FFFFFF", outline="")
    ct9 = canva.create_rectangle(x+80*zoom, y+15*zoom, x+85*zoom, y+20*zoom, fill="#FFFFFF", outline="")
    ct10 = canva.create_rectangle(x+85*zoom, y+10*zoom, x+95*zoom, y+15*zoom, fill="#FFFFFF", outline="")
    ct11 = canva.create_rectangle(x+95*zoom, y+15*zoom, x+100*zoom, y+20*zoom, fill="#FFFFFF", outline="")
    ct12 = canva.create_rectangle(x+100*zoom, y+10*zoom, x+115*zoom, y+15*zoom, fill="#FFFFFF", outline="")
    ct13 = canva.create_rectangle(x+115*zoom, y, x+120*zoom, y+10*zoom, fill="#FFFFFF", outline="")
    ct14 = canva.create_rectangle(x+45*zoom, y, x+120*zoom, y+5*zoom, fill="#FFFFFF", outline="")
    ct15 = canva.create_rectangle(x+45*zoom, y, x+50*zoom, y+25*zoom, fill="#FFFFFF", outline="")
