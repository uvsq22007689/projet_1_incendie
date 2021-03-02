########################################################
# Auteurs:
# Nabila Elaidoudi
# Marco Laurent De-Riemacker
# Gabriela Da Luz
# Abdul-Malik 
# Camelia Rili
# Groupe: BI 1
#https://github.com/uvsq22007689/projet_1_incendie.git
##########################################################

#####################
#import des modules
from tkinter import*
from random import*
from time import sleep

#####################
# fonctions

LARGEUR= 800
HAUTEUR = 800

fen = Tk() 
fen.attributes('-fullscreen', 1)#Fenetre en plein écran 
fen.title("IncendieSim")

def terrain() :
    global T
    T = []
    L = []
    for i in range(100) :#initialisation du terrain
        T.append(L) 
        for j in range(40):
            if i == 0 or i == 30 or j == 0 or j == 40-1:
                L.append(0) #on remplit les bords d'eau 
            else :
                L.append(randint(0,1)) #On place aléatoirement des arbres ou de l'eau 
        L = []
    return T

def cendre():
    global U
    U = []
    E = []
    for i in range(40):
        U.append(E)
        for j in range (40):
            E.append(3)
        E = []



def feu():
    global T
    x=randint(0,40-1)
    y=randint(0,40-1)
    while T[y][x] != 2: #On cherche un arbre pour l'enflammer
        if T[y][x] == 1: 
            T[y][x]=2
        else: #Si ce n'est pas un arbre on cherche une autre case
            x=randint(0,40-1)
            y=randint(0,40-1)
    
    return T

#propagation du feu 
def temps():
    global T
    for i in range(40):
        for j in range (40): 
            if T[i][j] == 2: #On cherche les cases "feu"
                if T[i][j+1]==1:
                    T[i][j+1]=4 #on modifie les cases adjacentes
                if T[i][j-1]==1:
                    T[i][j-1]=4
                if T[i+1][j]==1:
                    T[i+1][j]=4
                if T[i-1][j]==1:
                    T[i-1][j]=4
    for i in range(40):
        for j in range (40): 
            if T[i][j] == 4:
                T[i][j] = 2
    return T

def TimCendre():
    
    for i in range(40):
        for j in range (40): 
            if T[i][j] == 2: 
                U[i][j] = U[i][j] - 1
                if U[i][j] == 0 :
                    T[i][j] = 3
    return U

def avancement() :#Boucle permettant la propagation automatique du feu
    début()
    TimCendre()
    temps()

#fenetre

def quadrillage() :
    xl=0
    for i in range(40):#Boucle de creation des traits de lignes et colonnes
        can.create_line(xl, 0, xl, LARGEUR, fill ='black')
        can.create_line(0, xl, HAUTEUR, xl, fill ='black')
        xl=xl+20

def début() :
    global T
    x=0 #coord de départ
    y=0
    n=0
    c=0
    for i in range(40): #Double boucles pour lancer le feu 
        for j in range(40):
            if T[i][j] == 0 :
                can.create_rectangle(x,y,x+20,y+20,fill='cyan') #Canvas générant le feu 
            if T[i][j] == 1 :
                can.create_rectangle(x,y,x+20,y+20,fill='green') #Canvas générant le feu 
            if T[i][j] == 2 :
                can.create_rectangle(x,y,x+20,y+20,fill='red') #Canvas générant le feu 
                n=n+1#Détection du nombre de cases en feu
            if T[i][j] == 3 :
                can.create_rectangle(x,y,x+20,y+20,fill='grey') #Canvas générant le feu 
                c=c+1#Détection du nombre de cases en cendre
            if T[i][j] == 4 :
                can.create_rectangle(x,y,x+20,y+20,fill='red') #Canvas générant le feu 
            x=x+20
        x=0
        y=y+20
    if n==0 and c>=1:#Si il n'y a plus de feu mais présence de cendre
        fin()#Fonction de fin de la simulation
    else :
        fen.after(500,avancement)#Sinon on continue la propagation

def fin() : 
    fin = Tk()
    finm = Message(fin , width=200, justify =CENTER,font ="Century",text ='La simulation est terminée').pack()#Effacement de la fenêtre après 2 secondes
    fen.after(3000) #La simulation recommence

#lancement


def lancement():#On lance la boucle ,on supprime le bouton et on initialise les tableaux
    can.delete('all')#On supprime ce qu'il y a sur le canevas
    quadrillage()
    terrain()
    cendre()
    feu()
    avancement()


#####################
# programme principal 

mainmenu = Menu(fen)#Creation d'un menu
 
menuJeu = Menu(mainmenu)  #Menu deroulant
menuJeu.add_separator()#Ligne separatrice

menuJeu.add_command(label = "Quitter" , command = fen.destroy)
mainmenu.add_cascade(label = "Jeu", menu = menuJeu)#Menu cascade
Button(fen, text ='Quitter', command = fen.destroy).pack(side=BOTTOM, padx=5, pady=5)
Button(fen, text ='Lancer la simulation', command = lancement).pack(side=BOTTOM, padx=5, pady=5)
fen.iconbitmap("flamme.ico")
fen.config(menu = mainmenu)
 

n=0 
can = Canvas(fen, width = LARGEUR, height = HAUTEUR, bg ='ivory')#Creation d'un caneva dans la fenetre
can.pack(side =TOP, padx =5, pady =5)#Affichage du caneva dans la fenetre

fen.mainloop()
