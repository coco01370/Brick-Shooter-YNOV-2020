#---------------------ecriture dans le fichier
def write_file(vaiseau_i, credit_i, vitTir_i, vitDep_i, vitDef_i):

    fic = open("donnee_joueur.txt", "wt")
    vaisseau = "vaisseau : " + str(vaiseau_i)+ "\n"
    credit = "credit : " + str(credit_i)+"\n"
    vitesse_de_tire = "vitesse de tire : " + str(vitTir_i) + "\n"
    vitesse_de_déplacement = "vitesse de deplacement : " + str(vitDep_i) + "\n"
    vitesse_de_défilement = "vitesse de defilement : " +  str(vitDef_i)+"\n"

    fic.write(vaisseau)
    fic.write(credit)
    fic.write(vitesse_de_tire)
    fic.write(vitesse_de_déplacement)
    fic.write(vitesse_de_défilement)

    fic.close()


#---------------------lecture des donné du fichier
def read_file(ligne):
    fic = open("donnee_joueur.txt", "r")
    c = fic.readlines()
    j = 0
    variable = "";
    while(c[ligne][j] != "\n" and (c[ligne][j] > "9" or c[ligne][j] < "0")):
        j += 1
    while(c[ligne][j] != "\n" and (c[ligne][j] < "9" or c[ligne][j] > "0")):
        variable += c[ligne][j]
        j += 1
    fic.close()
    return int(variable)


#---------------------changement que de la première ligne
def change_ship(number):
    write_file(number, read_file(1), read_file(2), read_file(3), read_file(4))
