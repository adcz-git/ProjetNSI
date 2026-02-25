# Créé par soren, le 02/01/2026 en Python 3.7
from tkinter import *

def buttonclicked(cox,coy):
    button_list[coy][cox].config(bg = colors[coloractu])
    colorlist[coy][cox]=coloractu

def colorchange(color):
    global coloractu
    coloractu = color
    for button in buttoncolor:
        button.config(state = NORMAL)
    buttoncolor[color].config(state =DISABLED)

def min(a,b):
    if a>b:
        return b
    else:
        return a

def max(a,b):
    if a>b:
        return a
    else:
        return b

hauteur = int(input("largeur du pixel art"))
longueur = int(input ("longueur du pixel art"))
echelle = int(input("echelle du pixel art(si il y a un problème dans les contours, mettez 2)(combien de pixels affichés par la fonction pour chaque pixel de l'interface"))


fen = Tk()
fen.geometry(str(longueur*20)+"x"+str(hauteur*20 + 30))

colors = [None, "red","orange","yellow","green","blue","purple", "white","black"]

button_list = []
buttoncolor = []
colorlist = []
pixel = []

coloractu = 0

for i in range(hauteur):
    button_list.append([])
    colorlist.append([])
    for ind in range (longueur):
        frame = Frame(fen, width = 20,height =20)
        button_list[i].append(Button(fen, command=  lambda x = ind, y=i : buttonclicked(x,y)))
        button_list[i][ind].place(x=ind*20,y=i*20,width = 20,height = 20)
        colorlist[i].append(0)

for i in range(len(colors)):
    buttoncolor.append(Button(fen, bg = colors[i]if colors[i]!=None else "grey", command = lambda couleur = i:colorchange(couleur)))
    buttoncolor[i].place(x = 20 + 20*i, y = hauteur*20+10,width = 20,height = 20)


fen.mainloop()

for i in range(len(colorlist)):
    print(colorlist[i])

ymin = hauteur
xmin = longueur

for i in range(len(colorlist)):
    for ind in range(len(colorlist)):
        if colorlist[i][ind] !=0:
            ymin = min(i,ymin)
            xmin = min(ind,xmin)
            pixel.append({"x":ind,"y":i,"color" : colors[colorlist[i][ind]]})
zoom = echelle

print("def image(x,y):")
for i in range (len(pixel)):
    cox =str((pixel[i]["x"]-xmin)*zoom)
    coy = str((pixel[i]["y"]-ymin)*zoom)
    cox2 = str(int(cox)+zoom-1)
    coy2 = str(int(coy)+zoom-1)
    print("    dessin.create_rectangle(x+"    +cox+",y+"+ coy  +",x+" + cox2+",y+"+coy2 +',outline="'+pixel[i]["color"]+'"' +',fill="'+pixel[i]["color"]+'")')
