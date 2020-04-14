
# On importe Tkinter
from tkinter import *
#from tkinter import TK ,Canvas

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

#canvas=Canvas(fenetre, width=768, height=576, bg="ivory")

#bg=PhotoImage(file="noir.png")
#background=canvas.create_image(370,250,image=bg)

#canvas.pack()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Projet B1 Brick Shooter !")

# On affiche le label dans la fenêtre
champ_label.pack()

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side="bottom")
bouton_instruction = Button(fenetre, text="Instruction")
bouton_instruction.pack(side="bottom")
bouton_personnaliser = Button(fenetre, text="Personnaliser")
bouton_personnaliser.pack(side="bottom")
bouton_jouer = Button(fenetre, text="Jouer")
bouton_jouer.pack(side="bottom")

bouton_jouer.configure(width=20, height=2)
bouton_personnaliser.configure(width=20, height=2)
bouton_instruction.configure(width=20, height=2)
bouton_quitter.configure(width=20, heigh=2)
#On met l'écran de jeu en pleine écran
fenetre.attributes('-fullscreen', True)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()