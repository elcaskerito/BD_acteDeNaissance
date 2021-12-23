# -*- coding: utf-8 -*-
#*****************************************************************************************************#
#   PROGRAMME POUR LA CREATION D'UNE BASE DE DONNEES D'ENREGISTREMENT DES NAISSANCES A L'HÔPITAL      # 
#                                                                                                     #
#*****************************************************************************************************#
# Pré-requis : 
#
# - avoir un Server local avec SGBD mysql
# - installer mysql-connector pour python.
# - installer python dans votre machine
# 
#
# Guide D'Utilisation : 
#
#   - avant d'exécuter ce script il faut dabord créer au préalable une base de données nommée "naissanceDB" dans votre système de gestion de Base de Données
#   - ensuite ajouter le mot de passe de votre SGBD a la ligne 24 de ce fichier. si votre SGBD n'a pas de mot de passe laisser cette partie vide
import mysql.connector
from tkinter import *
from functools import partial
#connexion au base de données
def globa():
  db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "TopSecret_1998@",
    database = "naissanceDB"
    )
  cur = db.cursor()

#******************************************************************************************************



### $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$-- interface --$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

def validateLogin(nom, prenom,ndp,sp,fp,nm,sm,fm,se,ln,dn,hn):
  db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "TopSecret_1998@",
    database = "naissanceDB"
    )
  cur = db.cursor()
  print("name  :", nom.get())
  print("prenom :", prenom.get())
  print("nom du père :", ndp.get())
  print("situation du père :", sp.get())
  print("fonction du père :", fp.get())
  print("nom du mère :", nm.get())
  print("situation du mère :", sm.get())
  print("fonction du mère :", fm.get())
  print("sexe de l'enfant :", se.get())
  print("lieu de naissance :", ln.get())
  print("date de naissance  :", dn.get())
  print("heure de naissance :", hn.get())

  value1 = (""+nom.get()+"", prenom.get(),ndp.get(),sp.get(),fp.get(),nm.get(),sm.get(),fm.get(),se.get(),ln.get(),dn.get(),hn.get())
  sql = "INSERT INTO `nouveau_ne`(nom, `prenom`, `nom_pere`, `situation_matrimoniale_père`, `fonction_père`, `nom_mère`, `situation_matrimonial_mère`, `fonction_mère`, `sexe_enfant`, `lieu_de_naissance`, `date_naissance`, `heure_de_naissance`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"
  # value = ("idris", "mahamat  ","Mahamat idris","marié","Avocat","kelou fatime","mariée", "sage femme","masculin","N'djamena","1998-11-1","10:20")
  cur.execute(sql, value1)
  db.commit()
  return
    
#tkwindow est une création de l'instance de la classe Tk
tkWindow = Tk()  
# definition de la taill de l'interface
tkWindow.geometry('500x600')  
# titre de l'interface
tkWindow.title('INTERFACE FONCTIONNAIRE')



#username label and text entry box
usernameLabel = Label(tkWindow, text="Name", font=("Time New Roman", 8, "")).grid(row=1, column=0)
nom = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=nom).grid(row=1, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=2, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="Prenom",font=("Time New Roman", 8, "")).grid(row=2, column=0)
prenom = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=prenom).grid(row=2, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=3, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="Nom du pere", font=("Time New Roman", 8, "")).grid(row=3, column=0)
ndp = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=ndp).grid(row=3, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=4, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="situation matrimonial pere", font=("Time New Roman", 8, "")).grid(row=4, column=0)
sp = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=sp).grid(row=4, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=5, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="fonction du pere", font=("Time New Roman", 8, "")).grid(row=5, column=0)
fp = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=fp).grid(row=5, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=6, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="Nom de la mere", font=("Time New Roman", 8, "")).grid(row=6, column=0)
nm = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=nm).grid(row=6, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=7, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="situation matrimonial de la mere", font=("Time New Roman", 8, "")).grid(row=7, column=0)
sm = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=sm).grid(row=7, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=8, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="fonction de la mere", font=("Time New Roman", 8, "")).grid(row=8, column=0)
fm = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=fm).grid(row=8, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=9, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="sexe enfant", font=("Time New Roman", 8, "")).grid(row=9, column=0)
se = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=se).grid(row=9, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=10, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="lieu de naissance",font=("Time New Roman", 8, "")).grid(row=10, column=0)
ln = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=ln).grid(row=10, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=11, column=0)

#***********************************************************************#
#username label and text entry box
usernameLabel = Label(tkWindow, text="date de naissance", font=("Time New Roman", 8, "")).grid(row=11, column=0)
dn = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=dn).grid(row=11, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=12, column=0)

#***********************************************************************#
#username label and text entry box
usernameLabel = Label(tkWindow, text="heure de naissance",font=("Time New Roman", 8, "")).grid(row=12, column=0)
hn = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=hn).grid(row=12, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=13, column=0)

validateLogin = partial(validateLogin, nom, prenom,ndp,sp,fp,nm,sm,fm,se,ln,dn,hn)

#login button
loginButton = Button(tkWindow, text="Enregistrer l'enfant", command=validateLogin).grid(row=15, column=0)  



# print(cur.rowcount, "ligne insérée.")
tkWindow.mainloop()
globa()