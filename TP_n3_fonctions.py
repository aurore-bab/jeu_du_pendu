#========================================================================================
# Aurore BABIN
# Swann RERAT
# TP CS-DEV pendu
# 25/09/2023
#========================================================================================
# objectifs:
# 
#========================================================================================
# fichier fonctions
import random as rd
def mot(fich):
    """arguements de la fonction: un nom de fichier texte
    renvoie : un mot (str)
    que fait la fonction : elle extrait les mots du fichier texte, en choisit un de façon aléatoire et le renvoit"""
    #on ouvre le fichier texte avec la liste de mots
    f = open(fich, 'r')
    l = f.read()
    f.close()
    #on en extrait les mots
    liste_mots = l.split(", ")
    # on en choisit un au hasard
    mot_choisi = rd.randint(0, len(liste_mots) - 1)
    return liste_mots[mot_choisi]


def affiche(mot, lettres_proposees):
    """ce que fait la fonction : cette fonction sert juste à afficher le mot du pendu, 
    avec des underscore pour chaque lettre pas toruvée et la première lettre affichée
    arguments : le mot du pendu, et la liste des lettres déjà proposées
    renvoie : rien, c'est juste des prints
    """
    print(mot[0], end = " ") #pour forcément afficher la première lettre du mot
    #pour chaque lettre dans le mot, on affiche la lettre si on l'a déjà trouvée, ou on affiche un underscore
    for lettre in range(1, len(mot)): 
        if mot[lettre] in lettres_proposees :
            print(mot[lettre], end = " ")
        else:
            print("_", end = " ")
    print("\n")
 

def cherche_lettres(mot, nb_chances, lettres_proposees, lettre) :
    """arguments : le mot choisi aléatoirement,
    nbdechances = nombre allant de 0 à 8
    lettres_proposées = liste des lettres déjà propoosées
    lettre = un str avec une lettre 
    
    renvoie : le nombre de chances , et les lettres proposées
    
    ce que fait la fonction : elle demande une lettre au joueur et vérifie qu'elle soit bien dans l'alphabet
    puis elle teste si on a déjà proposé la lettre
    puis elle teste si cette lettre est dans le mot ou pas et la met dans la liste de lettres proposées"""
    
    lettres_proposees.append(lettre)
    if lettre in mot :
        print("Vous avez trouvé une bonne lettre : ", lettre)
        return nb_chances, lettres_proposees
    else :
        return nb_chances - 1, lettres_proposees

        
def test_mot(mot, lettres_prop):
    """ce que fait la fonction: elle teste si on a trouvé toutes les lettres du mot ou pas
    argument : le mot, la liste des lettres déjà proposées par le joueur
    retourne : un booléen : ture si on a trouvé tout le mot, false sinon"""

    for lettre in mot:
        if lettre not in lettres_prop:
            return False
    return True