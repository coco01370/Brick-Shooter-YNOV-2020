# On importe Tkinter pour l'interface graphique
from tkinter import *
#On importe subprocess pour pouvoir relier les différentes pages de notre jeu à notre page princiaple
import subprocess
#On importe notre page de gestion de donnée pour pouvoir récupérer les crédits du joueur ainsi que pouvoir améliorer nos vaisseaux
from gestion_des_donnees_du_joueur import *

#On initialise nos crédits à l'aide du fichier gestion_des_donnees_du_joueur
credit = read_file(1)
#On initialise aléatoirement le cout pour les améliorations de cahque vaisseau
cout = 20

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Projet B1 Brick Shooter !", bg="#0F056b", fg="white")

# On affiche le label dans la fenêtre
champ_label.pack()

#On donne une couleur de fond au contour de l'image de notre fenêtre
fenetre.configure(background="#0F056b")

#On donne les dimensions de notre fenêtre de jeu 
canvas=Canvas(fenetre, width=800, heigh=600)
canvas.pack()

#On ajoute une image de fond sur notre fenêtre de jeu
photo=PhotoImage(file="images/espace.png")
canvas.create_image(290, 280, image=photo)

#On affiche les lignes de texte pour le coût de chaque vaisseau en dur dans notre fenêtre
texte = canvas.create_text(740, 20, text="Crédit(s) : " + str(credit), font="Arial 11 italic", fill="#FFD700")
texte1 = canvas.create_text(150, 320, text="Coût de crédit : 50", font="Arial 11 italic", fill="#FFD700")
texte2 = canvas.create_text(400, 320, text="Coût de crédit : 50", font="Arial 11 italic", fill="#FFD700")
texte3 = canvas.create_text(640, 320, text="Coût de crédit : 50", font="Arial 11 italic", fill="#FFD700")

#On affiche notre premier vaisseau sur notre fenêtre
Vaisseau1 = PhotoImage(file="images/vaisseau_ship1.gif")
canvas.create_image(250, 280, image=Vaisseau1)
Vaisseau1.configure(width=270, height=200)

#On affiche notre deuxième vaisseau sur notre fenêtre
Vaisseau2 = PhotoImage(file="images/vaisseau_ship2.gif")
canvas.create_image(503, 280, image=Vaisseau2)
Vaisseau2.configure(width=270, height=200)

#On affiche notre troisième vaisseau sur notre fenêtre
Vaisseau3 = PhotoImage(file="images/vaisseau_ship3.gif")
canvas.create_image(740, 280, image=Vaisseau3)
Vaisseau3.configure(width=270, height=200)

#On initialise aléatoirement le choix du vaisseau
choix_ship = 1

#Cette fonctioin permettra de relier le premier bouton au premier vaisseau
def ship1():
    change_ship(1)

#Cette fonctioin permettra de relier le deuxième bouton au deuxième vaisseau
def ship2():
    change_ship(2)

#Cette fonctioin permettra de relier le troisième bouton au troisième vaisseau
def ship3():
    change_ship(3)


#Cette fonction permettra de pouvoir revenir à la page d'accueil en attribuant cette fonction à un bouton
def menus():
    fenetre.destroy()
    subprocess.run("python accueil.py")

#Cette fonction permet de récupérer les crédits du joueur puis de les afficher sur la fenêtre de personnalisation
def print_credit(texte):
    texte = canvas.itemconfigure(texte, text="Crédit(s) : " + str(read_file(1)))

#Cette fonction permet de pouvoir augmenter la vitesse de tir du vaisseau du joueur
def vitShot_increment():
    if(read_file(1) >= 50):
        change_credit(read_file(1) - 50)
        change_tirSpeed(read_file(2) + 10) #augmente la vitesse de tir de 10
        print_credit(texte)

#Cette fonction permet de pouvoir augmenter la vitesse de déplacement du vaisseau du joueur
def vitMove_increment():
    if(read_file(1) >= 50):
        change_credit(read_file(1) - 50)
        change_deplacementSpeed(read_file(3) + 2) #augmente la vitesse de déplacement de 2
        print_credit(texte)

#Cette fonction permet de pouvoir augmenter la vitesse de défilement des blocs ennemis
def vitEnemie_decrement():
    if(read_file(1) >= 50 and read_file(4) > 1):
        change_credit(read_file(1) - 50)
        change_defilementSpeed(read_file(4) -1) #diminue la vitesse des enemis de 1
        print("ttttttttt");
        print_credit(texte)


#Ce bouton permet de choisir le premier vaisseau afficher 
bouton_ship1 = Button(fenetre , text="Ship1", command=ship1)
bouton_ship1.pack(side="left", padx=5, pady=5)
bouton_ship1.configure(width=20, height=2, bg="#000033", fg="white")

#Ce bouton permet de choisir le deuxième vaisseau afficher 
bouton_ship2 = Button(fenetre , text="Ship2", command=ship2)
bouton_ship2.pack(side="left", padx=5, pady=5)
bouton_ship2.configure(width=20, height=2, bg="#000033", fg="white")

#Ce bouton permet de choisir le troisième vaisseau afficher 
bouton_ship3 = Button(fenetre , text="Ship3", command=ship3)
bouton_ship3.pack(side="left", padx=5, pady=5)
bouton_ship3.configure(width=20, height=2, bg="#000033", fg="white")


#Ce bouton nous permet de pouvoir revenir à la page d'accueil de notre jeu
bouton_retour = Button(fenetre, text="Retourner à l'accueil", command=menus)
bouton_retour.pack(side="bottom", padx=5, pady=5)
bouton_retour.configure(width=20, heigh=2, bg="#0F056b", fg="white")


# vaisseau 1 upgrade vitesse de tir
bouton_upgradeTir1 = Button(fenetre, text="Augmenter vitesse de tir 1", command=vitShot_increment)
bouton_upgradeTir1.pack(side="left", padx=5, pady=5)
bouton_upgradeTir1.configure(width=20, heigh=2, bg="#000033", fg="white")
    # vaisseau 1 upgrade vitesse de déplacement
bouton_upgradeDeplacement1 = Button(fenetre, text="Augmenter vitesse de déplacement", command=vitMove_increment)
bouton_upgradeDeplacement1.pack(side="left", padx=5, pady=5)
bouton_upgradeDeplacement1.configure(width=28, heigh=2, bg="#000033", fg="white")
    # vaisseau 1 upgrade vitesse de défilement
bouton_upgradeDefilement1 = Button(fenetre, text="Diminuer vitesse de défilement", command=vitEnemie_decrement)
bouton_upgradeDefilement1.pack(side="left", padx=5, pady=5)
bouton_upgradeDefilement1.configure(width=25, heigh=2, bg="#000033", fg="white")

#On place les boutons pour les choix d'amélioration de notre premier vaisseau
bouton_upgradeTir1.place(x=68, y=370)
bouton_upgradeDeplacement1.place(x=40, y=420)
bouton_upgradeDefilement1.place(x=50, y=470)

# vaisseau 2 upgrade vitesse de tir
bouton_upgradeTir2 = Button(fenetre, text="Augmenter vitesse de tir", command=vitShot_increment)
bouton_upgradeTir2.pack(side="left", padx=2, pady=2)
bouton_upgradeTir2.configure(width=20, heigh=2, bg="#000033", fg="white")
    # vaisseau 2 upgrade vitesse de déplacement
bouton_upgradeDeplacement2 = Button(fenetre, text="Augmenter vitesse de déplacement", command=vitMove_increment)
bouton_upgradeDeplacement2.pack(side="left", padx=5, pady=5)
bouton_upgradeDeplacement2.configure(width=28, heigh=2, bg="#000033", fg="white")
    # vaisseau 2 upgrade vitesse de défilement
bouton_upgradeDefilement2 = Button(fenetre, text="Diminuer vitesse de défilement", command=vitEnemie_decrement)
bouton_upgradeDefilement2.pack(side="left", padx=5, pady=5)
bouton_upgradeDefilement2.configure(width=25, heigh=2, bg="#000033", fg="white")

#On place les boutons pour les choix d'amélioration de notre deuxième vaisseau
bouton_upgradeTir2.place(x=322, y=370)
bouton_upgradeDeplacement2.place(x=294, y=420)
bouton_upgradeDefilement2.place(x=304, y=470)


# vaisseau 3 upgrade vitesse de tir
bouton_upgradeTir3 = Button(fenetre, text="Augmenter vitesse de tir", command=vitShot_increment)
bouton_upgradeTir3.pack(side="left", padx=5, pady=5)
bouton_upgradeTir3.configure(width=20, heigh=2, bg="#000033", fg="white")
    # vaisseau 3 upgrade vitesse de déplacement
bouton_upgradeDeplacement3 = Button(fenetre, text="Augmenter vitesse de déplacement", command=vitMove_increment)
bouton_upgradeDeplacement3.pack(side="left", padx=5, pady=5)
bouton_upgradeDeplacement3.configure(width=28, heigh=2, bg="#000033", fg="white")
    # vaisseau 3 upgrade vitesse de défilement
bouton_upgradeDefilement3 = Button(fenetre, text="Diminuer vitesse de défilement", command=vitEnemie_decrement)
bouton_upgradeDefilement3.pack(side="left", padx=5, pady=5)
bouton_upgradeDefilement3.configure(width=25, heigh=2, bg="#000033", fg="white")

#On place les boutons pour les choix d'amélioration de notre troisième vaisseau
bouton_upgradeTir3.place(x=564, y=370)
bouton_upgradeDeplacement3.place(x=536, y=420)
bouton_upgradeDefilement3.place(x=546, y=470)


#On place les boutons de choix de vaisseau ainsi que de retour à la page d'accueil sur notre fenêtre
bouton_retour.place(x=620, y=575)
bouton_ship1.place(x=35, y=575)
bouton_ship2.place(x=230, y=575)
bouton_ship3.place(x=425, y=575)


#On met l'écran de jeu en pleine écran
#fenetre.attributes('-fullscreen', True)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()