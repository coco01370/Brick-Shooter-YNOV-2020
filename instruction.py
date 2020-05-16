# On importe Tkinter pour l'interface graphique
from tkinter import *
#On importe subprocess pour pouvoir relier les différentes pages de notre jeu à notre page princiaple
import subprocess



# On crée une fenêtre, racine de notre interface
fenetre = Tk()

#Cette fonction permettra de pouvoir revenir à la page d'accueil en attribuant cette fonction à un bouton
def menus():
    fenetre.destroy()
    subprocess.run('python accueil.py')

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Projet B1 Brick Shooter !", bg="#000033", fg="white")

# On affiche le label dans la fenêtre
champ_label.pack()

#On donne une couleur de fond au contour de l'image de notre fenêtre
fenetre.configure(background="#000033")

#On donne les dimensions de notre fenêtre de jeu 
canvas=Canvas(fenetre, width=800, heigh=600)
canvas.pack()

#On donne les dimensions de notre fenêtre de jeu 
photo=PhotoImage(file="images/espace.png")
canvas.create_image(290, 280, image=photo)

#On affiche les lignes d'instructions en dur dans notre fenêtre
texte1 = canvas.create_text(47, 235, text="Règles :", font="Arial 11 italic", fill="white")
texte2 = canvas.create_text(274, 260, text="Casser les blocs qui apparaissent sur l'écran de jeu grâce au vaisseau.", font="Arial 11 italic", fill="white")
texte3 = canvas.create_text(266, 285, text="Si vous casser un carré, aucun bonus/malus influera sur votre partie.", font="Arial 11 italic", fill="white")
texte4 = canvas.create_text(224, 310, text="Si vous casser une tortue, la vitesse de tir sera diminue.", font="Arial 11 italic", fill="white")
texte5 = canvas.create_text(283, 335, text="Si vous casser un rond, la vitesse de déplacement du joueur sera diminue.", font="Arial 11 italic", fill="white")
texte5 = canvas.create_text(309, 360, text="Si vous casser un triangle, la vitesse de déplacement de l'ennemi sera augmentée.", font="Arial 11 italic", fill="white")
texte6 = canvas.create_text(366, 400, text="Une fois la partie terminée, liquez sur le game over lorsque le message appraît pour revenir a l'accueil.", font="Arial 11 italic", fill="white")

#Ce bouton permettra de revenir à la page d'accueil grâce à la fonction : menus
bouton_retour = Button(fenetre, text="Retourner à l'accueil", command=menus)
bouton_retour.pack(side="bottom", padx=5, pady=5)
bouton_retour.configure(width=20, heigh=2, bg="#000033", fg="white")

#On place le bouton où l'on veut dans notre fenêtre
bouton_retour.place(x=330, y=575)

#On met l'écran de jeu en pleine écran
#fenetre.attributes('-fullscreen', True)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
