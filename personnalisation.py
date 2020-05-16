# On importe Tkinter
from tkinter import *
from random import randint
import subprocess
#pour le temps

import time

credits = 100
cost = 20

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Projet B1 Brick Shooter !", bg="#000033", fg="white")

# On affiche le label dans la fenêtre
champ_label.pack()

fenetre.configure(background="#000033")

#Apparition de l'image en fond
canvas=Canvas(fenetre, width=800, heigh=600)

canvas.pack()

photo=PhotoImage(file="images/espace.png")
canvas.create_image(290, 280, image=photo)

# ______________    ___________     \    /     ______________    ______________
#       |           |                \  /            |          |
#       |           |                 \/             |          |
#       |           |__________       /\             |          |_____________
#       |           |                /  \            |          |
#       |           |__________     /    \           |          |_____________

#On affiche les crédits
texte = canvas.create_text(750, 20, text="Crédit(s) :" + str(credits), font="Arial 11 italic", fill="#FFD700")

#On affiche le cout de l'achat 1
texte1 = canvas.create_text(150, 320, text="Coup de Crédit : 50", font="Arial 11 italic", fill="#FFD700")
#On affiche le cout de l'achat 2
texte2 = canvas.create_text(400, 320, text="Coup de Crédit : 50", font="Arial 11 italic", fill="#FFD700")
#On affiche le cout de l'achat 3
texte3 = canvas.create_text(645, 320, text="Coup de Crédit : 50", font="Arial 11 italic", fill="#FFD700")

texteHide = canvas.create_text(300, 50, text="Coup de Crédit : 50", font="Arial 11 italic", fill="#FFD700")
#---->
texteHide.pack()
texteHide.pack_forget()
#       /\
#       \/
#                         ____
#       |   |\    /|     /    \
#       |   | \  / |    /
#       |   |  \/  |    \     __
#       |   |      |     \____/
#Image pour le premier choix de vaisseau
vaisseau1=PhotoImage(file="images/vaisseau_ship1.png")
canvas.create_image(205, 280, image=vaisseau1)
vaisseau1.configure(width=270, height=200)

#Image pour le deuxième choix de vaisseau
vaisseau2=PhotoImage(file="images/vaisseau_ship2.png")
canvas.create_image(460, 280, image=vaisseau2)
vaisseau2.configure(width=270, height=200)

#Image pour le troisième choix de vaisseau
vaisseau3=PhotoImage(file="images/vaisseau_ship3.png")
canvas.create_image(750, 290, image=vaisseau3)
vaisseau3.configure(width=370, height=200)


#-------------------------------------
#Fonction pour les boutons
choix_ship = 1

def ship1():
    choix_ship = 1

def ship2():
    choix_ship = 2

def ship3():
    choix_ship = 3

def menus():
    fenetre.destroy()
    subprocess.run('python accueil.py')

#---->
def upgradeTir(credits,cost):
    if credits >= cost :
        credits = credits - cost
        while True:
            show()
            time.sleep(5)  # Delay en seconde (5 seconds).



    else :
        print(credits)

# ecrire dans fichier le + 1 de tir
def show():
    texteHide.pack()
def hide():
    texteHide.pack_forget()

def upgradeDeplacement(credits,cost):
    if credits >= cost:
        credits = credits - cost
        print(credits)

# ecrire dans fichier le + 1 de deplacement

def upgradeDefilement():
    if credits >= cost:
        credits = credits - cost
        print(credits)
    # ecrire dans fichier le - 1 de defilement


if choix_ship == 1 :
    ship_player = "ship1.gif"
elif choix_ship == 2 :
    ship_player = "ship2.gif"
elif choix_ship == 3 :
    ship_player = "ship3.gif"

#-------------------------------------
#   SHIP
# vaiseau 1
bouton_ship1 = Button(fenetre, text="Ship1", command=ship1)
bouton_ship1.pack(side="left", padx=5, pady=5)
bouton_ship1.configure(width=20, heigh=2, bg="#000033", fg="white")
# vaisseau 2
bouton_ship2 = Button(fenetre, text="Ship2", command=ship2)
bouton_ship2.pack(side="left", padx=5, pady=5)
bouton_ship2.configure(width=20, height=2, bg="#000033", fg="white")
# vaisseau 3
bouton_ship3 = Button(fenetre, text="ship3", command=ship3)
bouton_ship3.pack(side="left", padx=5, pady=5)
bouton_ship3.configure(width=20, heigh=2, bg="#000033", fg="white")
# retour
bouton_retour = Button(fenetre, text="Retourner à l'accueil", command=menus)
bouton_retour.pack(side="bottom", padx=5, pady=5)
bouton_retour.configure(width=20, heigh=2, bg="#000033", fg="white")
#

# --------------------------------------------------------------------
#
#  UPGRADE
#            ___     ___    ____    _____    __   _____        /|
#   |     | |   \   /       |   \   |    |  |  \  |           / |
#   |     | |___/   \    _  |___/   |____|  |   | |____      /  |
#   |_____| |        \___|  |   \   |    |  |__/  |____         |

    # vaisseau 1 upgrade vitesse de tir
bouton_upgradeTir1 = Button(fenetre, text="Augmenter vitesse de tir", command=upgradeTir(credits, cost))
bouton_upgradeTir1.pack(side="left", padx=5, pady=5)
bouton_upgradeTir1.configure(width=20, heigh=2, bg="#000033", fg="white")
    # vaisseau 1 upgrade vitesse de déplacement
bouton_upgradeDeplacement1 = Button(fenetre, text="Augmenter vitesse de déplacement", command=upgradeDeplacement)
bouton_upgradeDeplacement1.pack(side="left", padx=5, pady=5)
bouton_upgradeDeplacement1.configure(width=28, heigh=2, bg="#000033", fg="white")
    # vaisseau 1 upgrade vitesse de défilement
bouton_upgradeDefilement1 = Button(fenetre, text="Diminuer vitesse de défilement", command=upgradeDefilement)
bouton_upgradeDefilement1.pack(side="left", padx=5, pady=5)
bouton_upgradeDefilement1.configure(width=25, heigh=2, bg="#000033", fg="white")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
bouton_upgradeTir1.place(x=68, y=370)
bouton_upgradeDeplacement1.place(x=40, y=420)
bouton_upgradeDefilement1.place(x=50, y=470)

# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
#
#                                                             ___.
#            ___     ___    ____    _____    __   _____          |
#   |     | |   \   /       |   \   |    |  |  \  |           ___|
#   |     | |___/   \    _  |___/   |____|  |   | |____      |
#   |_____| |        \___|  |   \   |    |  |__/  |____      |____

    # vaisseau 2 upgrade vitesse de tir
bouton_upgradeTir2 = Button(fenetre, text="Augmenter vitesse de tir", command=upgradeTir)
bouton_upgradeTir2.pack(side="left", padx=2, pady=2)
bouton_upgradeTir2.configure(width=20, heigh=2, bg="#000033", fg="white")
    # vaisseau 2 upgrade vitesse de déplacement
bouton_upgradeDeplacement2 = Button(fenetre, text="Augmenter vitesse de déplacement", command=upgradeDeplacement)
bouton_upgradeDeplacement2.pack(side="left", padx=5, pady=5)
bouton_upgradeDeplacement2.configure(width=28, heigh=2, bg="#000033", fg="white")
    # vaisseau 2 upgrade vitesse de défilement
bouton_upgradeDefilement2 = Button(fenetre, text="Diminuer vitesse de défilement", command=upgradeDefilement)
bouton_upgradeDefilement2.pack(side="left", padx=5, pady=5)
bouton_upgradeDefilement2.configure(width=25, heigh=2, bg="#000033", fg="white")

#--------------------------------------------------------------------
#--------------------------------------------------------------------
bouton_upgradeTir2.place(x=322, y=370)
bouton_upgradeDeplacement2.place(x=294, y=420)
bouton_upgradeDefilement2.place(x=304, y=470)



# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------

#            ___     ___    ____    _____    __   _____    _____
#   |     | |   \   /       |   \   |    |  |  \  |        .____|
#   |     | |___/   \    _  |___/   |____|  |   | |____    |____|
#   |_____| |        \___|  |   \   |    |  |__/  |____    _____|

    # vaisseau 3 upgrade vitesse de tir
bouton_upgradeTir3 = Button(fenetre, text="Augmenter vitesse de tir", command=upgradeTir)
bouton_upgradeTir3.pack(side="left", padx=5, pady=5)
bouton_upgradeTir3.configure(width=20, heigh=2, bg="#000033", fg="white")
    # vaisseau 3 upgrade vitesse de déplacement
bouton_upgradeDeplacement3 = Button(fenetre, text="Augmenter vitesse de déplacement", command=upgradeDeplacement)
bouton_upgradeDeplacement3.pack(side="left", padx=5, pady=5)
bouton_upgradeDeplacement3.configure(width=28, heigh=2, bg="#000033", fg="white")
    # vaisseau 3 upgrade vitesse de défilement
bouton_upgradeDefilement3 = Button(fenetre, text="Diminuer vitesse de défilement", command=upgradeDefilement)
bouton_upgradeDefilement3.pack(side="left", padx=5, pady=5)
bouton_upgradeDefilement3.configure(width=25, heigh=2, bg="#000033", fg="white")

#--------------------------------------------------------------------
#--------------------------------------------------------------------
bouton_upgradeTir3.place(x=564, y=370)
bouton_upgradeDeplacement3.place(x=536, y=420)
bouton_upgradeDefilement3.place(x=546, y=470)



# placement bouton
bouton_retour.place(x=620, y=575)
bouton_ship1.place(x=35, y=575)
bouton_ship2.place(x=230, y=575)
bouton_ship3.place(x=425, y=575)









#On met l'écran de jeu en pleine écran
#fenetre.attributes('-fullscreen', True)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()