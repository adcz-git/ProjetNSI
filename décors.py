from tkinter import *

def cage_debut(x,y,canva):
    ######################
    ######contours########
    ######################
    ct1=canva.create_rectangle(x,y+60,x+65,y+65,fill="#FFFFFF")
    ct2=canva.create_rectangle(x,y+35,x+5,y+65,fill="#FFFFFF")
    ct3=canva.create_rectangle(x+5,y+30,x+10,y+35,fill="#FFFFFF")
    ct4=canva.create_rectangle(x+10,y+25,x+15,y+30,fill="#FFFFFF")
    ct5=canva.create_rectangle(x+15,y+20,x+20,y+25,fill="#FFFFFF")
    ct6=canva.create_rectangle(x+20,y+15,x+25,y+20,fill="#FFFFFF")
    ct7=canva.create_rectangle(x+25,y+10,x+40,y+15,fill="#FFFFFF")
    ct8=canva.create_rectangle(x+40,y+15,x+45,y+20,fill="#FFFFFF")
    ct9=canva.create_rectangle(x+45,y+20,x+50,y+25,fill="#FFFFFF")
    ct10=canva.create_rectangle(x+50,y+25,x+55,y+30,fill="#FFFFFF")
    ct11=canva.create_rectangle(x+55,y+30,x+60,y+35,fill="#FFFFFF")
    ct12=canva.create_rectangle(x+60,y+35,x+65,y+65,fill="#FFFFFF")
    ct13=canva.create_rectangle(x+25,y+50,x+30,y+65,fill="#FFFFFF")
    ct14=canva.create_rectangle(x+30,y+45,x+40,y+50,fill="#FFFFFF")
    ct15=canva.create_rectangle(x+40,y+50,x+45,y+65,fill="#FFFFFF")
    #######################
    ######Barreaux#########
    #######################
    b1=canva.create_rectangle(x+10,y+30,x+15,y+60,fill="#7A7A7A")
    b2=canva.create_rectangle(x+20,y+20,x+25,y+60,fill="#7A7A7A")
    b3=canva.create_rectangle(x+30,y+15,x+35,y+45,fill="#7A7A7A")
    b4=canva.create_rectangle(x+40,y+20,x+45,y+45,fill="#7A7A7A")
    b5=canva.create_rectangle(x+50,y+30,x+55,y+60,fill="#7A7A7A")
    #######################
    ########Porte##########
    #######################
    p=canva.create_rectangle(x+30,y+50,x+40,y+60,fill="#551800")
    #######################
    #########Anse##########
    #######################
    a1=canva.create_rectangle(x+25,y+5,x+30,y+10,fill="#FFE600")
    a2=canva.create_rectangle(x+30,y,x+35,y+5,fill="#FFE600")
    a3=canva.create_rectangle(x+35,y+5,x+40,y+10,fill="#FFE600")

def maison1(x,y,canva):
    ######################
    ######contours########
    ######################
    ct1=canva.create_rectangle(x,y+110,x+120,y+115,fill="#FFFFFF")
    ct2=canva.create_rectangle(x,y+25,x+120,y+30,fill="#FFFFFF")
    ct3=canva.create_rectangle(x,y+25,x+5,y+115,fill="#FFFFFF")
    ct4=canva.create_rectangle(x+115,y+25,x+120,y+115,fill="#FFFFFF")
    ct5=canva.create_rectangle(x+25,y,x+95,y+5,fill="#FFFFFF")
    ct6=canva.create_rectangle(x+5,y+20,x+10,y+25,fill="#FFFFFF")
    ct7=canva.create_rectangle(x+10,y+15,x+15,y+20,fill="#FFFFFF")
    ct8=canva.create_rectangle(x+15,y+10,x+20,y+15,fill="#FFFFFF")
    ct9=canva.create_rectangle(x+20,y+5,x+25,y+10,fill="#FFFFFF")
    ct10=canva.create_rectangle(x+95,y+5,x+100,y+10,fill="#FFFFFF")
    ct11=canva.create_rectangle(x+100,y+10,x+105,y+15,fill="#FFFFFF")
    ct12=canva.create_rectangle(x+105,y+15,x+110,y+20,fill="#FFFFFF")
    ct13=canva.create_rectangle(x+110,y+20,x+115,y+25,fill="#FFFFFF")
    #petite fenetre
    ct14=canva.create_rectangle(x+15,y+55,x+40,y+60,fill="#FFFFFF")
    ct15=canva.create_rectangle(x+15,y+55,x+20,y+80,fill="#FFFFFF")
    ct16=canva.create_rectangle(x+15,y+75,x+40,y+80,fill="#FFFFFF")
    ct17=canva.create_rectangle(x+35,y+55,x+40,y+80,fill="#FFFFFF")
    #grande fenetre
    ct18=canva.create_rectangle(x+60,y+55,x+105,y+60,fill="#FFFFFF")
    ct19=canva.create_rectangle(x+60,y+55,x+65,y+80,fill="#FFFFFF")
    ct20=canva.create_rectangle(x+60,y+75,x+105,y+80,fill="#FFFFFF")
    ct21=canva.create_rectangle(x+100,y+55,x+105,y+80,fill="#FFFFFF")
    #fentre toit
    ct22=canva.create_rectangle(x+50,y+10,x+55,y+20,fill="#FFFFFF")
    ct23=canva.create_rectangle(x+55,y+5,x+65,y+10,fill="#FFFFFF")
    ct24=canva.create_rectangle(x+55,y+20,x+65,y+25,fill="#FFFFFF")
    ct25=canva.create_rectangle(x+65,y+10,x+70,y+20,fill="#FFFFFF")
    #cadre porte
    ct26=canva.create_rectangle(x+40,y+90,x+45,y+115,fill="#FFFFFF")
    ct27=canva.create_rectangle(x+45,y+85,x+55,y+90,fill="#FFFFFF")
    ct28=canva.create_rectangle(x+55,y+90,x+60,y+115,fill="#FFFFFF")
    #######################
    ########Porte##########
    #######################
    p=canva.create_rectangle(x+45,y+90,x+55,y+110,fill="#551800")
    #######################
    ######intfenetres######
    #######################
    #interieur fenetre de toit
    ifen1=canva.create_rectangle(x+55,y+10,x+60,y+15,outline="#FFFFFF")
    ifen1=canva.create_rectangle(x+55,y+15,x+60,y+20,outline="#FFFFFF")
    ifen3=canva.create_rectangle(x+60,y+10,x+65,y+15,outline="#FFFFFF")
    ifen4=canva.create_rectangle(x+60,y+15,x+65,y+20,outline="#FFFFFF")
    #intérieur petite fenetre
    ifen5=canva.create_rectangle(x+20,y+60,x+25,y+65,outline="#FFFFFF")
    ifen6=canva.create_rectangle(x+20,y+65,x+25,y+70,outline="#FFFFFF")
    ifen7=canva.create_rectangle(x+20,y+70,x+25,y+75,outline="#FFFFFF")
    ifen8=canva.create_rectangle(x+25,y+60,x+30,y+65,outline="#FFFFFF")
    ifen9=canva.create_rectangle(x+25,y+65,x+30,y+70,outline="#FFFFFF")
    ifen10=canva.create_rectangle(x+25,y+70,x+30,y+75,outline="#FFFFFF")
    ifen11=canva.create_rectangle(x+30,y+60,x+35,y+65,outline="#FFFFFF")
    ifen12=canva.create_rectangle(x+30,y+65,x+35,y+70,outline="#FFFFFF")
    ifen13=canva.create_rectangle(x+30,y+70,x+35,y+75,outline="#FFFFFF")
    #intérieur grande fenetre
    ifen14=canva.create_rectangle(x+65,y+60,x+75,y+65,outline="#FFFFFF")
    ifen15=canva.create_rectangle(x+65,y+65,x+75,y+70,outline="#FFFFFF")
    ifen16=canva.create_rectangle(x+65,y+70,x+75,y+75,outline="#FFFFFF")
    ifen17=canva.create_rectangle(x+75,y+60,x+90,y+65,outline="#FFFFFF")
    ifen18=canva.create_rectangle(x+75,y+65,x+90,y+70,outline="#FFFFFF")
    ifen19=canva.create_rectangle(x+75,y+70,x+90,y+75,outline="#FFFFFF")
    ifen20=canva.create_rectangle(x+90,y+60,x+100,y+65,outline="#FFFFFF")
    ifen21=canva.create_rectangle(x+90,y+65,x+100,y+70,outline="#FFFFFF")
    ifen22=canva.create_rectangle(x+90,y+70,x+100,y+75,outline="#FFFFFF")
    #######################
    ########Briques########
    #######################
    #briques haut gauche
    br1=canva.create_rectangle(x+30,y+40,x+40,y+45,outline="#FFFFFF")
    br2=canva.create_rectangle(x+35,y+35,x+45,y+40,outline="#FFFFFF")
    br3=canva.create_rectangle(x+45,y+40,x+55,y+45,outline="#FFFFFF")
    br4=canva.create_rectangle(x+35,y+45,x+45,y+50,outline="#FFFFFF")
    #briques haut droite
    br5=canva.create_rectangle(x+75,y+40,x+90,y+45,outline="#FFFFFF")
    br6=canva.create_rectangle(x+85,y+35,x+95,y+40,outline="#FFFFFF")
    #briques bas gauche
    br7=canva.create_rectangle(x+10,y+100,x+20,y+105,outline="#FFFFFF")
    br8=canva.create_rectangle(x+15,y+95,x+25,y+100,outline="#FFFFFF")
    br9=canva.create_rectangle(x+20,y+90,x+30,y+95,outline="#FFFFFF")
    #briques bas droite
    br10=canva.create_rectangle(x+75,y+95,x+85,y+100,outline="#FFFFFF")
    br11=canva.create_rectangle(x+80,y+90,x+90,y+95,outline="#FFFFFF")
    br12=canva.create_rectangle(x+85,y+95,x+95,y+100,outline="#FFFFFF")
    br13=canva.create_rectangle(x+80,y+100,x+90,y+105,outline="#FFFFFF")