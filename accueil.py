# On importe Tkinter pour l'interface graphique
from tkinter import *
#On importe subprocess pour pouvoir relier les différentes pages de notre jeu à notre page princiaple
import subprocess
#On importe notre page de gestion de donnée pour pouvoir récupérer les crédits du joueur
from gestion_des_donnees_du_joueur import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Projet B1 Brick Shooter !", bg="#000033", fg="white")

# On affiche le label dans la fenêtre
champ_label.pack()

fenetre.configure(bg="#000033")

#On donne les dimensions de notre fenêtre de jeu 
canvas=Canvas(fenetre, width=800, heigh=600)
canvas.pack()

#On ajoute une image de fond sur notre fenêtre de jeu
photo=PhotoImage(file="images/espace.png")
canvas.create_image(290, 280, image=photo)

#On affiche les crédits
texte = canvas.create_text(740, 20, text="Crédit(s) :" + str(read_file(1)), font="Arial 11 italic", fill="#FFD700")

#Cette fonction permettra de relier notre fenêtre d'accueil a notre fenêtre de jeu
def launch():
    fenetre.destroy()
    subprocess.run('python space_invaders.py')

#Cette fonction permettra de relier notre fenêtre d'accueil a notre fenêtre d'instruction
def instruction():
        fenetre.destroy()
        subprocess.run('python instruction.py')

#Cette fonction permettra de relier notre fenêtre d'accueil a notre fenêtre de personnalisation de vaisseau ainsi que de modification de données
def Personnaliser():
    fenetre.destroy()
    subprocess.run('python personnalisation.py')

#Fonction pour les boutons
#Le command=<notreFonction> permet de pouvoir relier un bouton a une page ou à une action
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side="right", padx=5, pady=5)
bouton_instruction = Button(fenetre, text="Instruction", command=instruction)
bouton_instruction.pack(side="right", padx=5, pady=5)
bouton_jouer = Button(fenetre, text="Jouer", command=launch) #lancer le file space_invaders.py
bouton_jouer.pack(side="left", padx=5, pady=5)
bouton_personnaliser = Button(fenetre, text="Personnaliser", command=Personnaliser)
bouton_personnaliser.pack(side="left", padx=5, pady=5)

#Le .configure permet de choisir l'épaisseur du bouton ainsi que la couleur de que l'on veut donner a notre bouton
bouton_jouer.configure(width=20, height=2, bg="#000033", fg="white")
bouton_personnaliser.configure(width=20, height=2, bg="#000033", fg="white")
bouton_instruction.configure(width=20, height=2, bg="#000033", fg="white")
bouton_quitter.configure(width=20, heigh=2, bg="#000033", fg="white")

#Le .place permet de placer le bouton où l'on veut sur notre fenêtre
bouton_jouer.place(x=330, y=150)
bouton_personnaliser.place(x=330, y=250)
bouton_instruction.place(x=330, y=350)
bouton_quitter.place(x=330, y= 450)

#On met l'écran de jeu en pleine écran
#fenetre.attributes('-fullscreen', True)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
