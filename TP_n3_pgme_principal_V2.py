#========================================================================================
# Aurore BABIN
# TP CS-DEV pendu
# 25/09/2023
#========================================================================================
# objectifs:
# faire une interface graphique avec le pendu
#========================================================================================
# programme principal
"""
from TP_n3_fonctions_V2 import *
rejouer = "oui"
print("binvenue au jeu du pendu!")
while rejouer == "oui":
    p = pgme_principal()
    rejouer = input("voulez-vous rejouer?\npour rejouer tapez oui, sinon ça arretera le jeu ")

print("merci d'avoir joué au pendu")"""
import random as rd
from tkinter import Tk, Frame, Label, Button, StringVar, Entry, Canvas, PhotoImage

"""
mw = Tk() 
mw.title('le jeu du pendu')
mw["bg"] = "navajo white"
mw.geometry('500x300+100+100')
mw.config(cursor = "heart")


pendu = PhotoImage(file = "pendu.gif")
canvas = Canvas (mw, width = 200, height = 200)
item = canvas.create_image(0, 0, anchor = 'e', image = pendu)
canvas.pack(side = 'right')

mw.mainloop()"""

import tkinter as tk
 
fenetre = tk.Tk()
 
photo = tk.PhotoImage(file='pendu.gif')
 
label = tk.Label(fenetre, image=photo)
label.pack()
 
fenetre.mainloop()