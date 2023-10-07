#========================================================================================
# Aurore BABIN
# Swann RERAT
# TP CS-DEV pendu
# 25/09/2023
#========================================================================================
# objectifs:
# faire le jeu du pendu
#========================================================================================
# programme principal
import random as rd
from TP_n3_fonctions import mot, affiche, cherche_lettres, test_mot

# initialisation du mot, et du nombre de chances
mot_pendu = mot("mots.txt")
l_prop = [mot_pendu[0]] #c'est la liste des lettres déjà proposées par le joueur, avec la première lettre dedans pour initialiser
nb_chances = 8 
alphabet = ["a" , "b" , "c" , "d" , "e" ,"f" , "g" , "h" , "i" , "j" ,"k" ,
            "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" ,*
            "w" , "x" , "y" , "z"]
affiche(mot_pendu, l_prop) #pour afficher les trous une première fois
test = False #cette variable sert à valider si on a trouvé tout le mot ou pas

#pgme principal
while nb_chances > 0 and not test:
    #on demande une lettre au joueur
    lettre = input("Quelle lettre voulez-vous jouer ? ")

    #on teste si la lettre est bien une lettre, et qu'on ne l'ait pas déjà proposée, dans le cas contraire on recommence
    if lettre in l_prop: 
        print("vous l'avez déjà proposé")
    elif lettre not in alphabet or len(lettre) != 1 :
        print("ce n'est pas une lettre")
    else:
        p = cherche_lettres(mot_pendu, nb_chances, l_prop, lettre)
        nb_chances = p[0]
        l_prop = p[1]
        test = test_mot(mot_pendu, l_prop)
        print("il vous reste {} chances".format(nb_chances))
        affiche(mot_pendu, l_prop)

if nb_chances == 0:
    print("vous avez perdu!, le mot était :", mot_pendu)
elif test:
    print("Bravo! vous avez trouvé le mot :", mot_pendu)
    

