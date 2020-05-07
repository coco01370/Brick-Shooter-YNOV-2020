# On importe Tkinter
from tkinter import *
from random import randint
import subprocess

RandumCredit = randint(0, 10)

def instruction():
    #On affiche les lignes d'instructions
    texte1 = canvas.create_text(47, 235, text="Règles :", font="Arial 11 italic", fill="white")
    texte2 = canvas.create_text(274, 260, text="Casser les blocs qui apparaissent sur l'écran de jeu grâce au vaisseau.", font="Arial 11 italic", fill="white")
    texte3 = canvas.create_text(266, 285, text="Si vous casser un carré, aucun bonus/malus influera sur votre partie.", font="Arial 11 italic", fill="white")
    texte4 = canvas.create_text(224, 310, text="Si vous casser une tortue, la vitesse de tir sera diminue.", font="Arial 11 italic", fill="white")
    texte5 = canvas.create_text(283, 335, text="Si vous casser un rond, la vitesse de déplacement du joueur sera diminue.", font="Arial 11 italic", fill="white")
    texte5 = canvas.create_text(309, 360, text="Si vous casser un triangle, la vitesse de déplacement de l'ennemi sera augmentée.", font="Arial 11 italic", fill="white")

    #Fonction pour les boutons
    bouton_retour = Button(fenetre, text="Retourner à l'accueil")
    bouton_retour.pack(side="bottom", padx=5, pady=5)
    bouton_retour.configure(width=20, heigh=2, bg="#0F056b", fg="white")

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Projet B1 Brick Shooter !", bg="#0F056b", fg="white")

# On affiche le label dans la fenêtre
champ_label.pack()

fenetre.configure(bg="#0F056b")

#Apparition de l'image en fond
canvas=Canvas(fenetre, width=800, heigh=600)
canvas.pack()

photo=PhotoImage(file="espace.png")
canvas.create_image(290, 280, image=photo)

#On affiche les crédits
texte = canvas.create_text(750, 20, text="Crédit(s) :" + str(RandumCredit), font="Arial 11 italic", fill="#FFD700")

def launch():
    fenetre.destroy()
    subprocess.run('python space_invaders.py')

def instruction():
        fenetre.destroy()
        subprocess.run('python instruction.py')

def Personnaliser():
    fenetre.destroy()
    subprocess.run('python personnalisation.py')

#Fonction pour les boutons
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side="right", padx=5, pady=5)
bouton_quitter.configure(width=20, heigh=2, bg="#0F056b", fg="white")
#
bouton_instruction = Button(fenetre, text="Instruction", command=instruction)
bouton_instruction.pack(side="right", padx=5, pady=5)
bouton_instruction.configure(width=20, height=2, bg="#0F056b", fg="white")
#
bouton_jouer = Button(fenetre, text="Jouer", command=launch) #lancer le file space_invaders.py
bouton_jouer.pack(side="left", padx=5, pady=5)
bouton_jouer.configure(width=20, height=2, bg="#0F056b", fg="white")
#
bouton_personnaliser = Button(fenetre, text="Personnaliser", command=Personnaliser)
bouton_personnaliser.pack(side="left", padx=5, pady=5)
bouton_personnaliser.configure(width=20, height=2, bg="#0F056b", fg="white")


#On met l'écran de jeu en pleine écran
#fenetre.attributes('-fullscreen', True)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
