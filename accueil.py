# On importe Tkinter
from tkinter import *
from random import randint
import subprocess
from gestion_des_donnees_du_joueur import *
RandumCredit = randint(0, 10)

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Projet B1 Brick Shooter !", bg="#000033", fg="white")

# On affiche le label dans la fenêtre
champ_label.pack()

fenetre.configure(bg="#000033")

#Apparition de l'image en fond
canvas=Canvas(fenetre, width=800, heigh=600)
canvas.pack()

photo=PhotoImage(file="images/espace.png")
canvas.create_image(290, 280, image=photo)

#On affiche les crédits
texte = canvas.create_text(750, 20, text="Crédit(s) :" + str(read_file(1)), font="Arial 11 italic", fill="#FFD700")

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
bouton_instruction = Button(fenetre, text="Instruction", command=instruction)
bouton_instruction.pack(side="right", padx=5, pady=5)
bouton_jouer = Button(fenetre, text="Jouer", command=launch) #lancer le file space_invaders.py
bouton_jouer.pack(side="left", padx=5, pady=5)
bouton_personnaliser = Button(fenetre, text="Personnaliser", command=Personnaliser)
bouton_personnaliser.pack(side="left", padx=5, pady=5)
bouton_jouer.configure(width=20, height=2, bg="#000033", fg="white")
bouton_personnaliser.configure(width=20, height=2, bg="#000033", fg="white")
bouton_instruction.configure(width=20, height=2, bg="#000033", fg="white")
bouton_quitter.configure(width=20, heigh=2, bg="#000033", fg="white")

bouton_jouer.place(x=330, y=150)
bouton_personnaliser.place(x=330, y=250)
bouton_instruction.place(x=330, y=350)
bouton_quitter.place(x=330, y= 450)

#On met l'écran de jeu en pleine écran
#fenetre.attributes('-fullscreen', True)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
