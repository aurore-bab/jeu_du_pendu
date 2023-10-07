#========================================================================================
# TP CS-DEV pendu
# 25/09/2023
#========================================================================================
# objectifs:
# interface graphique
#========================================================================================
# à améliorer / régler:
# fonction image_pendu
# arreter le programme quand on a perdu ou quand on a gagné


import random as rd
from tkinter import Tk, Frame, Label, Button, StringVar, Entry, Canvas, PhotoImage
import tkinter.font as font

def mot_a_deviner(fich):
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

def affiche():
    #texte.get()
    global mot
    global lettres_proposees
    global texte
    global texte2

    affichage = ""
    for lettre in range(len(mot)):
        if mot[lettre] in lettres_proposees :
            affichage += mot[lettre].upper() + " "
        else:
            affichage += "_ "
    
    affichage2 = "lettres déjà proposées : \n"
    for lettre in lettres_proposees:
        affichage2 += lettre.upper() + " "

    texte.set(affichage)
    texte2.set(affichage2)

def verif_lettres() :
    global nb_chances
    global lettres_proposees
    global mot

    alphabet = ["a" , "b" , "c" , "d" , "e" ,"f" , "g" , "h" , "i" , "j" ,"k" ,
            "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" ,
            "w" , "x" , "y" , "z"]
    
    if lettre_choisie.get() not in lettres_proposees and len(lettre_choisie.get()) == 1 and lettre_choisie.get() in alphabet:
        lettres_proposees.append(lettre_choisie.get())

    if lettre_choisie.get() not in mot and len(lettre_choisie.get()) <= 1 and lettre_choisie.get() in alphabet:
        nb_chances = nb_chances - 1
    
    
    lettre_choisie.set('')
    affiche()
         
def test_mot(word, lettres_prop):
    """ce que fait la fonction: elle teste si on a trouvé toutes les lettres du mot ou pas
    argument : le mot, la liste des lettres déjà proposées par le joueur
    retourne : un booléen : ture si on a trouvé tout le mot, false sinon"""

    for lettre in word:
        if lettre not in lettres_prop:
            return False
    return True

def image_pendu():
    global image_actuelle
    global nb_chances
    
    print(image_actuelle)
    print(nb_chances)

    if nb_chances == 8:
        image_actuelle = "pendu_n8.gif"
    elif nb_chances == 7:
        image_actuelle = "pendu_n7.gif"
    elif nb_chances == 6:
        image_actuelle = "pendu_n6.gif"
    elif nb_chances == 5:
        image_actuelle = "pendu_n5.gif"
    elif nb_chances == 4:
        image_actuelle = "pendu_n4.gif"
    elif nb_chances == 3:
        image_actuelle = "pendu_n3.gif"
    elif nb_chances == 2:
        image_actuelle = "pendu_n2.gif"
    elif nb_chances == 1:
        image_actuelle = "pendu_n1.gif"
    elif nb_chances == 0:
        image_actuelle = "pendu_n0.gif"
        """il faudrait ici faire un truc qui fait apparaitre par desus tout 
        une nouvelle fenêtre qui dit "GAME OVER le mot était : {}".format(le mot actuel)
        avec un bouton "quitter" et un bouton "rejouer"
        """


#initialisation de toutes les variables
nb_chances = 8
mot = mot_a_deviner("mots.txt")
lettres_proposees =  [mot[0]]


#on initialise une fenêtre
mw = Tk() 
mw.title('le jeu du pendu')
mw["bg"] = "navajo white"
mw.geometry('500x300+100+100')
mw.config(cursor = "star")

f = font.Font(size = 14, family = "Berlin Sans FB")

#1 image (= pendu, qui change selon le nombre de chances)
frame1 = Frame(mw , bg = "pink", width = 200, height = 200, relief = 'raised')
frame1.pack(side = 'right', padx = 10, pady = 10)
#image_actuelle = StringVar(frame1, "pendu.gif")
#image_actuelle.set(
#image_pendu() 
image_actuelle = "pendu.gif"

pendu = PhotoImage(file = image_actuelle)
canvas = Label(frame1, image = pendu)
# la méthode suivante ne veut pas marcher alors que c'est la méthode du prof, j'ai donc fait autrement
# canvas = Canvas(frame1, width = 200, height = 200)
#item = canvas.create_image(0, 0, anchor = 'e', image = pendu)
canvas.pack(side = 'right')


#2 bouton pour quitter le jeu (= titre)
butt_quit = Button (mw, text = "Le Jeu du Pendu", bg = "peach puff", fg = "darkred", command = mw.destroy, relief = "ridge")
butt_quit['font'] = f
butt_quit.pack(side ='top', padx = 10, pady = 10)

#3 zone de texte qui affiche le mot à trous
texte = StringVar()
mot_a_deviner = Label(mw, textvariable = texte)
mot_a_deviner['font'] = f
mot_a_deviner.pack(side = 'top', padx = 10, pady = 10)

#3 bis = lettres déjà proposées
texte2 = StringVar()
l_prop = Label(mw, textvariable = texte2, height = 2)
l_prop['font'] = f
l_prop.pack(side = 'top', padx = 10, pady = 10)

affiche()

#4 boite entry
lettre_choisie = StringVar()
champ = Entry(mw, textvariable = lettre_choisie, bg = 'pink', width = 5) 
#textvariable ici sert à récupérer le texte qu'on met dans la boite
champ.focus_set()
champ['font'] = f
champ.pack (side = 'left', padx = 10, pady = 10)

#5 boutton proposer
label_champ = Button(mw, text = 'proposer', command = verif_lettres)
label_champ['font'] = f
label_champ.pack (side = 'left', padx = 10, pady = 10)


alphabet = ["a" , "b" , "c" , "d" , "e" ,"f" , "g" , "h" , "i" , "j" ,"k" ,
            "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" ,
            "w" , "x" , "y" , "z"]

"""
test = False #cette variable sert à valider si on a trouvé tout le mot ou pas
# pgme principal
while not test:
    # on demande une lettre au joueur
    lettre_choisie.get()
    # on teste si la lettre est bien une lettre, et qu'on ne l'ait pas déjà proposée, dans le cas contraire on recommence
    if lettre_choisie not in lettres_proposees and lettre_choisie in alphabet and len(lettre_choisie) == 1 :
        lettres_proposees = verif_lettres(lettres_proposees)
        # verif_lettres va automatiquement mettre à jour le nombre de chances normalement
        test = test_mot(mot, lettres_proposees)

if nb_chances == 0:
    texte.set("BRAVO! vous avez gagné! le mot était bien: {}".format(mot))

"""


mw.mainloop()

