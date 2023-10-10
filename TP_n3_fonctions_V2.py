#========================================================================================
# TP CS-DEV pendu
# 25/09/2023
#========================================================================================
# objectifs:
# interface graphique
#========================================================================================
# à améliorer / régler:
# dans les fonctions game over et gagné, régler cette erreur pour faire en sorte de pouvoir recommencer le jeu du pendu
# mot = mot_a_deviner("mots.txt")
# TypeError: 'Label' object is not callable

import random as rd
from tkinter import Tk, Frame, Label, Button, StringVar, Entry, Canvas, PhotoImage
import tkinter.font as font
from tkinter import messagebox as msg

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

def image_pendu():
    global image_actuelle
    global nb_chances
    global frame1
    global canvas

    if nb_chances == 8:
        image_actuelle = pendu_8
    elif nb_chances == 7:
        image_actuelle = pendu_7
    elif nb_chances == 6:
        image_actuelle = pendu_6
    elif nb_chances == 5:
        image_actuelle = pendu_5
    elif nb_chances == 4:
        image_actuelle = pendu_4
    elif nb_chances == 3:
        image_actuelle = pendu_3
    elif nb_chances == 2:
        image_actuelle = pendu_2
    elif nb_chances == 1:
        image_actuelle = pendu_1
    elif nb_chances == 0:
        image_actuelle = pendu_0

    canvas.delete(all)
    canvas.create_image(0,0, anchor = 'nw', image = image_actuelle)
    canvas.config(height = image_actuelle.height(), width = image_actuelle.width())

def game_over():
    global mot
    global nb_chances
    global lettres_proposees

    MsgBox = msg.askretrycancel('perdu',"GAME OVER!!\nvous avez perdu, le mot était: {}".format(mot),icon = 'error')
    if not MsgBox:
        mw.destroy()
    else:
        msg.showinfo('Welcome Back',"c'est bien!\nil ne faut pas se laisser abattre")

        #réinitialisation de toutes les variables et de l'image
        nb_chances = 8
        mot = mot_a_deviner("mots.txt")
        lettres_proposees =  [mot[0]]
        affiche()
        image_pendu()

def gagne():
    global mot
    global nb_chances
    global lettres_proposees

    MsgBox = msg.askretrycancel('gégné',"GAGNE!!\nBravo ! vous avez gagné perdu, le mot était bien: {}".format(mot),icon = 'info')
    if not MsgBox:
        mw.destroy()
    else:
        #réinitialisation de toutes les variables et de l'image
        nb_chances = 8
        mot = mot_a_deviner("mots.txt")
        lettres_proposees =  [mot[0]]
        affiche()
        image_pendu()

def verif_lettres() :
    global nb_chances
    global lettres_proposees
    global mot

    alphabet = ["a" , "b" , "c" , "d" , "e" ,"f" , "g" , "h" , "i" , "j" ,"k" ,
            "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" ,
            "w" , "x" , "y" , "z"]
    if lettre_choisie.get() not in mot and len(lettre_choisie.get()) == 1:
        if lettre_choisie.get() in alphabet and lettre_choisie.get() not in lettres_proposees:
            nb_chances = nb_chances - 1

    if lettre_choisie.get() not in lettres_proposees and len(lettre_choisie.get()) == 1 :
        if lettre_choisie.get() in alphabet:
            lettres_proposees.append(lettre_choisie.get())

    #ce truc est à supprimer, il sert juste à pouvoir tester rapidement la fonction game_over et gagne
    if lettre_choisie.get() == 'non':
        game_over()
    elif lettre_choisie.get() == 'oui':
        gagne()


    lettre_choisie.set('')
    affiche()
    image_pendu()
    
    test = True
    for lettre in mot:
        if lettre not in lettres_proposees:
            test = False
    
    
    if nb_chances == 0:
        game_over()

    if test:
        gagne()

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
canvas = Canvas (frame1, width = 200, height = 200)
image_actuelle = "pendu_n8.gif"
pendu = PhotoImage(file = image_actuelle)
pendu_0 = PhotoImage(file = "pendu_n0.gif")
pendu_1 = PhotoImage(file = "pendu_n1.gif")
pendu_2 = PhotoImage(file = "pendu_n2.gif")
pendu_3 = PhotoImage(file = "pendu_n3.gif")
pendu_4 = PhotoImage(file = "pendu_n4.gif")
pendu_5 = PhotoImage(file = "pendu_n5.gif")
pendu_6 = PhotoImage(file = "pendu_n6.gif")
pendu_7 = PhotoImage(file = "pendu_n7.gif")
pendu_8 = PhotoImage(file = "pendu_n8.gif")

#canvas.delete(all)
canvas.create_image(0,0, anchor = 'nw', image = pendu)
canvas.config(height = pendu.height(), width = pendu.width())
canvas.pack(side='right', padx = 10, pady = 10)

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
#mw.bind('<Return>', verif_lettres)

mw.mainloop()

