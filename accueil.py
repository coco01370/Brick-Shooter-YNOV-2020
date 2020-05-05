# On importe Tkinter
from tkinter import *
from random import randint

RandumCredit = randint(0, 10) 

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
txt = canvas.create_text(700, 20, text="Vous avez 10 crédit(s)", font="Arial 11 italic", fill="white")

#Fonction pour les boutons
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side="right", padx=5, pady=5)
bouton_instruction = Button(fenetre, text="Instruction")
bouton_instruction.pack(side="right", padx=5, pady=5)
bouton_jouer = Button(fenetre, text="Jouer")
bouton_jouer.pack(side="left", padx=5, pady=5)
bouton_personnaliser = Button(fenetre, text="Personnaliser")
bouton_personnaliser.pack(side="left", padx=5, pady=5)
bouton_jouer.configure(width=20, height=2, bg="#0F056b", fg="white")
bouton_personnaliser.configure(width=20, height=2, bg="#0F056b", fg="white")
bouton_instruction.configure(width=20, height=2, bg="#0F056b", fg="white")
bouton_quitter.configure(width=20, heigh=2, bg="#0F056b", fg="white")
#On met l'écran de jeu en pleine écran
#fenetre.attributes('-fullscreen', True)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()