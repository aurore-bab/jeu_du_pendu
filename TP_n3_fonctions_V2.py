#========================================================================================
# TP CS-DEV pendu
# 25/09/2023
#========================================================================================
# objectifs:
# interface graphique
#========================================================================================
# fini !! il reste plus qu'à le faire essayer
# et à mettre des commentaires

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
    """cette fonction change l'affichage 
    - du mot à trous (ex : A _ _ _ _)
    - des lettres déjà proposées"""
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
    """cette fonction prend les images du pendu déjà chargées dans le programme principal,
    et change l'image affichée en fonction du nombre de chances"""
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

def fin_du_jeu(situation,message, icon):
    """cette fonction peut définitivment être améliorée
    elle est appelée quand le nombre de chances tombe à 0 (message et icone de game over)
    ou quand on a trouvé le mot (messages et icone de gagné)
    elle affiche un messagebox qui nous informe de notre situation et qui nous permet soit de recommenecr soit de quitter
    """
    global mot
    global nb_chances
    global lettres_proposees

    MsgBox = msg.askretrycancel(situation,message,icon = icon)
    if not MsgBox: # si on clique sur le bouton 'cancel', ca renvoie un False
        mw.destroy()
    else: # donc le bouton 'recommencer' permet de recommencer
        # réinitialisation de toutes les variables et de l'image
        nb_chances = 8

        # ici, je voulais réinitialiser le mot, 
        # mais la fonction mot_a_deviner refuse d'être appelée dans une fonction, 
        # je n'ai fait que contourner le problème car je n'ai pas trouvé de solution
        # pour cela j'ai donc copié bêtement la fonction qui permet de trouver le mot (et on perd du coup tout le principe d'en avoir fait une fonction mais bon...)
        f = open("mots.txt", 'r')
        l = f.read()
        f.close()
        liste_mots = l.split(", ")
        mot_choisi = rd.randint(0, len(liste_mots) - 1)
        mot = liste_mots[mot_choisi]

        lettres_proposees =  [mot[0]]
        affiche()
        image_pendu()

def verif_lettres() :
    """cette fonction est appelée avec le bouton proposer 
    (j'ai essayé d'associer la touche entrée avec cette fonction, 
    ça ne marche pas mais je ne comprends pas pourquoi)
    
    
    cette fonction est en charge de
    - tester la chaine de caractère
    - changer le nombre de chances, et les affichages en fonction
    - tester si on a trouvé le mot ou perdu
    - appeler la fontion fin_du jeu le cas échéant

    """
    global nb_chances
    global lettres_proposees
    global mot

    alphabet = ["a" , "b" , "c" , "d" , "e" ,"f" , "g" , "h" , "i" , "j" ,"k" ,
            "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" ,
            "w" , "x" , "y" , "z"]
    
    #vérification de la chaine d'entrée
    if lettre_choisie.get() in alphabet and len(lettre_choisie.get()) == 1 and lettre_choisie.get() not in lettres_proposees:
        #on l'ajoute aux lettres proposées
        lettres_proposees.append(lettre_choisie.get())
        # puis on teste si c'était une lettre correcte ou pas
        if lettre_choisie.get() not in mot:
            nb_chances = nb_chances - 1

    lettre_choisie.set('') #on réinitialise la boite entry
    # on change l'image et les affichages en fonction des paramètres qui ont changés
    affiche() 
    image_pendu()
    
    # on teste si on a trouvé le mot en entier
    test = True
    for lettre in mot:
        if lettre not in lettres_proposees:
            test = False
    if test:
        fin_du_jeu('gagné !!',"GAGNE!!\nBravo ! vous avez gagné, le mot était bien: {}".format(mot),'info')

    # puis on teste le nombre de chances
    if nb_chances == 0:
        fin_du_jeu('perdu !!',"GAME OVER!!\nvous avez perdu, le mot était: {}".format(mot),'error')

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

#1 image (= pendu, qui change selon le nombre de chances) qu'on met dans une frame
# cette image sera changé à chaque appel de la fonction image_pendu (dans les fonctions verif lettre, gagne et gameover)
frame1 = Frame(mw , bg = "pink", width = 200, height = 200, relief = 'raised')
frame1.pack(side = 'right', padx = 10, pady = 10)
canvas = Canvas (frame1, width = 200, height = 200)
image_actuelle = PhotoImage(file = "pendu_n8.gif")
pendu_0 = PhotoImage(file = "pendu_n0.gif")
pendu_1 = PhotoImage(file = "pendu_n1.gif")
pendu_2 = PhotoImage(file = "pendu_n2.gif")
pendu_3 = PhotoImage(file = "pendu_n3.gif")
pendu_4 = PhotoImage(file = "pendu_n4.gif")
pendu_5 = PhotoImage(file = "pendu_n5.gif")
pendu_6 = PhotoImage(file = "pendu_n6.gif")
pendu_7 = PhotoImage(file = "pendu_n7.gif")
pendu_8 = PhotoImage(file = "pendu_n8.gif")

canvas.create_image(0,0, anchor = 'nw', image = image_actuelle)
canvas.config(height = image_actuelle.height(), width = image_actuelle.width())
canvas.pack(side='right', padx = 10, pady = 10)

#2 bouton pour quitter le jeu (= titre de la fenêtre)
butt_quit = Button (mw, text = "Le Jeu du Pendu", bg = "peach puff", fg = "darkred", command = mw.destroy, relief = "ridge")
butt_quit['font'] = f
butt_quit.pack(side ='top', padx = 10, pady = 10)

#3 zone de texte qui affiche le mot à trous (ces textes sont changés à chaque appel de la fonction verif lettres)
texte = StringVar()
mot_a_deviner = Label(mw, textvariable = texte)
mot_a_deviner['font'] = f
mot_a_deviner.pack(side = 'top', padx = 10, pady = 10)

#3 bis / lettres déjà proposées
texte2 = StringVar()
l_prop = Label(mw, textvariable = texte2, height = 2)
l_prop['font'] = f
l_prop.pack(side = 'top', padx = 10, pady = 10)

affiche()

#4 boite entry
lettre_choisie = StringVar()
champ = Entry(mw, textvariable = lettre_choisie, bg = 'pink', width = 5) 
champ.focus_set()
champ['font'] = f
champ.pack (side = 'left', padx = 10, pady = 10)

#5 boutton proposer
label_champ = Button(mw, text = 'proposer', command = verif_lettres)
label_champ['font'] = f
label_champ.pack (side = 'left', padx = 10, pady = 10)
#mw.bind('<Return>', verif_lettres)

mw.mainloop()

