# On importe Tkinter
from tkinter import *
from random import randint
import subprocess
from gestion_des_donnees_du_joueur import *

randumCredit = randint(0, 10)

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

#Image pour le premier choix de vaisseau
vaisseau1=PhotoImage(file="images/vaisseau_ship1.gif")
canvas.create_image(205, 280, image=vaisseau1)
vaisseau1.configure(width=270, height=200)

#Image pour le deuxième choix de vaisseau
vaisseau2=PhotoImage(file="images/vaisseau_ship2.gif")
canvas.create_image(435, 280, image=vaisseau2)
vaisseau2.configure(width=270, height=200)

#Image pour le troisième choix de vaisseau
vaisseau3=PhotoImage(file="images/vaisseau_ship3.gif")
canvas.create_image(750, 290, image=vaisseau3)
vaisseau3.configure(width=370, height=200)

#Fonction pour les boutons
choix_ship = 0

def ship1():
    change_ship(1)

def ship2():
    change_ship(2)

def ship3():
    change_ship(3)

def menus():
    fenetre.destroy()
    subprocess.run('python accueil.py')


#Fonction pour les boutons
bouton_ship1 = Button(fenetre, text="Ship1", command=ship1)
bouton_ship1.pack(side="left", padx=5, pady=5)
bouton_ship1.configure(width=20, heigh=2, bg="#000033", fg="white")
#
bouton_ship2 = Button(fenetre, text="Ship2", command=ship2)
bouton_ship2.pack(side="left", padx=5, pady=5)
bouton_ship2.configure(width=20, height=2, bg="#000033", fg="white")
#
bouton_ship3 = Button(fenetre, text="ship3", command=ship3)
bouton_ship3.pack(side="left", padx=5, pady=5)
bouton_ship3.configure(width=20, heigh=2, bg="#000033", fg="white")
#
bouton_retour = Button(fenetre, text="Retourner à l'accueil", command=menus)
bouton_retour.pack(side="bottom", padx=5, pady=5)
bouton_retour.configure(width=20, heigh=2, bg="#000033", fg="white")

bouton_retour.place(x=620, y=575)
bouton_ship1.place(x=35, y=575)
bouton_ship2.place(x=230, y=575)
bouton_ship3.place(x=425, y=575)


if choix_ship == 1 :
    ship_player = "ship1.gif"
elif choix_ship == 2 :
    ship_player = "ship2.gif"
elif choix_ship == 3 :
    ship_player = "ship3.gif"

#On met l'écran de jeu en pleine écran
#fenetre.attributes('-fullscreen', True)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
