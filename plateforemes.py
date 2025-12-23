from tkinter import *

def grande_plateforme(x,y,canva):
    bg1=canva.create_rectangle(x,y,x+150,y+15,fill="#000000")
    bg2=canva.create_rectangle(x+5,y+15,x+140,y+20,fill="#000000")
    bg3=canva.create_rectangle(x+30,y+20,x+35,y+25,fill="#000000")
    bg4=canva.create_rectangle(x+55,y+20,x+70,y+30,fill="#000000")
    bg5=canva.create_rectangle(x+60,y+25,x+65,y+35,fill="#000000")
    ################
    ####Contours####
    ################
    ct1=canva.create_rectangle(x,y,x+150,y+5,fill="#FFFFFF",outline="")
    ct2=canva.create_rectangle(x,y,x+5,y+15,fill="#FFFFFF",outline="")
    ct3=canva.create_rectangle(x+145,y,x+150,y+15,fill="#FFFFFF",outline="")
    ct4=canva.create_rectangle(x+5,y+15,x+25,y+20,fill="#FFFFFF",outline="")
    ct5=canva.create_rectangle(x+40,y+15,x+50,y+20,fill="#FFFFFF",outline="")
    ct6=canva.create_rectangle(x+75,y+15,x+105,y+20,fill="#FFFFFF",outline="")
    ct7=canva.create_rectangle(x+110,y+15,x+145,y+20,fill="#FFFFFF",outline="")
    ct8=canva.create_rectangle(x+25,y+20,x+30,y+25,fill="#FFFFFF",outline="")
    ct9=canva.create_rectangle(x+30,y+25,x+35,y+30,fill="#FFFFFF",outline="")
    ct10=canva.create_rectangle(x+35,y+20,x+40,y+25,fill="#FFFFFF",outline="")
    ct11=canva.create_rectangle(x+50,y+20,x+55,y+25,fill="#FFFFFF",outline="")
    ct12=canva.create_rectangle(x+55,y+25,x+60,y+35,fill="#FFFFFF",outline="")
    ct13=canva.create_rectangle(x+60,y+35,x+65,y+40,fill="#FFFFFF",outline="")
    ct14=canva.create_rectangle(x+65,y+25,x+70,y+35,fill="#FFFFFF",outline="")
    ct15=canva.create_rectangle(x+70,y+15,x+75,y+25,fill="#FFFFFF",outline="")
    ct15=canva.create_rectangle(x+105,y+20,x+110,y+25,fill="#FFFFFF",outline="")

def petite_palteforme(x,y,canva):
    bg1=canva.create_rectangle(x,y,x+55,y+10,fill="#000000")
    bg2=canva.create_rectangle(x+5,y+10,x+50,y+15,fill="#000000")
    bg3=canva.create_rectangle(x+25,y+15,x+30,y+20,fill="#000000")
    ################
    ####Contours####
    ################
    ct1=canva.create_rectangle(x,y,x+55,y+5,fill="#FFFFFF",outline="")
    ct2=canva.create_rectangle(x,y+5,x+5,y+10,fill="#FFFFFF",outline="")
    ct3=canva.create_rectangle(x+5,y+10,x+10,y+15,fill="#FFFFFF",outline="")
    ct4=canva.create_rectangle(x+10,y+15,x+25,y+20,fill="#FFFFFF",outline="")
    ct5=canva.create_rectangle(x+25,y+20,x+30,y+25,fill="#FFFFFF",outline="")
    ct6=canva.create_rectangle(x+30,y+15,x+45,y+20,fill="#FFFFFF",outline="")
    ct7=canva.create_rectangle(x+45,y+10,x+50,y+15,fill="#FFFFFF",outline="")
    ct8=canva.create_rectangle(x+50,y+5,x+55,y+10,fill="#FFFFFF",outline="")

def plateforme_L(x,y,canva):
    bg1=canva.create_rectangle(x,y+20,x+70,y+30,fill="#000000")
    bg2=canva.create_rectangle(x+5,y+30,x+70,y+35,fill="#000000")
    bg3=canva.create_rectangle(x+35,y+35,x+40,y+40,fill="#000000")
    bg4=canva.create_rectangle(x+45,y,x+80,y+25,fill="#000000")
    bg5=canva.create_rectangle(x+45,y,x+85,y+20,fill="#000000")
    bg6=canva.create_rectangle(x+45,y,x+115,y+15,fill="#000000")
    ################
    ####Contours####
    ################
    ct1=canva.create_rectangle(x,y+20,x+50,y+25,fill="#FFFFFF",outline="")
    ct2=canva.create_rectangle(x,y+20,x+5,y+30,fill="#FFFFFF",outline="")
    ct3=canva.create_rectangle(x+5,y+30,x+10,y+35,fill="#FFFFFF",outline="")
    ct4=canva.create_rectangle(x+10,y+35,x+35,y+40,fill="#FFFFFF",outline="")
    ct5=canva.create_rectangle(x+35,y+40,x+40,y+45,fill="#FFFFFF",outline="")
    ct6=canva.create_rectangle(x+40,y+35,x+65,y+40,fill="#FFFFFF",outline="")
    ct7=canva.create_rectangle(x+65,y+25,x+70,y+35,fill="#FFFFFF",outline="")
    ct8=canva.create_rectangle(x+70,y+20,x+80,y+25,fill="#FFFFFF",outline="")
    ct9=canva.create_rectangle(x+80,y+15,x+85,y+20,fill="#FFFFFF",outline="")
    ct10=canva.create_rectangle(x+85,y+10,x+95,y+15,fill="#FFFFFF",outline="")
    ct11=canva.create_rectangle(x+95,y+15,x+100,y+20,fill="#FFFFFF",outline="")
    ct12=canva.create_rectangle(x+100,y+10,x+115,y+15,fill="#FFFFFF",outline="")
    ct13=canva.create_rectangle(x+115,y,x+120,y+10,fill="#FFFFFF",outline="")
    ct14=canva.create_rectangle(x+45,y,x+120,y+5,fill="#FFFFFF",outline="")
    ct15=canva.create_rectangle(x+45,y,x+50,y+25,fill="#FFFFFF",outline="")