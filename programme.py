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
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "TopSecret_1998@",
  database = "naissanceDB"
)

#créer un curseur de base de données pour effectuer des opérations SQL
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
  print("username entered :", nom.get())
  print("password entered :", prenom.get())
  print("username entered :", ndp.get())
  print("password entered :", sp.get())
  print("password entered :", fp.get())
  print("password entered :", nm.get())
  print("username entered :", sm.get())
  print("password entered :", fm.get())
  print("password entered :", se.get())
  print("password entered :", ln.get())
  print("username entered :", dn.get())
  print("password entered :", hn.get())

  value1 = (""+nom.get()+"", prenom.get(),ndp.get(),sp.get(),fp.get(),nm.get(),sm.get(),fm.get(),se.get(),ln.get(),dn.get(),hn.get())
  sql = "INSERT INTO `nouveau_ne`(nom, `prenom`, `nom_pere`, `situation_matrimoniale_père`, `fonction_père`, `nom_mère`, `situation_matrimonial_mère`, `fonction_mère`, `sexe_enfant`, `lieu_de_naissance`, `date_naissance`, `heure_de_naissance`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"
  value = ("idris", "mahamat  ","Mahamat idris","marié","Avocat","kelou fatime","mariée", "sage femme","masculin","N'djamena","1998-11-1","10:20")
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
usernameLabel = Label(tkWindow, text="Name").grid(row=1, column=0)
nom = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=nom).grid(row=1, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=2, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="Prenom").grid(row=2, column=0)
prenom = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=prenom).grid(row=2, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=3, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="Nom du pere").grid(row=3, column=0)
ndp = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=ndp).grid(row=3, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=4, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="situation matrimonial pere").grid(row=4, column=0)
sp = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=sp).grid(row=4, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=5, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="fonction du pere").grid(row=5, column=0)
fp = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=fp).grid(row=5, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=6, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="Nom de la mere").grid(row=6, column=0)
nm = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=nm).grid(row=6, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=7, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="situation matrimonial de la mere").grid(row=7, column=0)
sm = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=sm).grid(row=7, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=8, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="fonction de la mere").grid(row=8, column=0)
fm = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=fm).grid(row=8, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=9, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="sexe enfant").grid(row=9, column=0)
se = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=se).grid(row=9, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=10, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="lieu de naissance").grid(row=10, column=0)
ln = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=ln).grid(row=10, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=11, column=0)

#***********************************************************************#
#username label and text entry box
usernameLabel = Label(tkWindow, text="date de naissance").grid(row=11, column=0)
dn = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=dn).grid(row=11, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=12, column=0)

#***********************************************************************#
#username label and text entry box
usernameLabel = Label(tkWindow, text="heure de naissance").grid(row=12, column=0)
hn = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=hn).grid(row=12, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=13, column=0)

validateLogin = partial(validateLogin, nom, prenom,ndp,sp,fp,nm,sm,fm,se,ln,dn,hn)

#login button
loginButton = Button(tkWindow, text="Enregistrer l'enfant", command=validateLogin).grid(row=15, column=0)  



### $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$-- interface _fin --$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##
#requéte SQL permettant de créer la table nouveau_né DANS LA BASE DE DONNÉES naissance_DB

sql1 = """CREATE TABLE IF NOT EXISTS `nouveau_ne` (
  `id_nouveau_né` int NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `nom_pere` varchar(50) NOT NULL,
  `situation_matrimoniale_père` varchar(50) NOT NULL,
  `fonction_père` varchar(50) NOT NULL,
  `nom_mère` varchar(50) NOT NULL,
  `situation_matrimonial_mère` varchar(100) NOT NULL,
  `fonction_mère` varchar(50) NOT NULL,
  `sexe_enfant` varchar(20) NOT NULL,
  `lieu_de_naissance` varchar(100) NOT NULL,
  `date_naissance` date NOT NULL,
  `heure_de_naissance` time(6) NOT NULL
)"""

cur.execute(sql1)

#*******************************************************************************************************
#requéte SQL permettant de créer la table utilisateur

sql2 = """CREATE TABLE IF NOT EXISTS `utilisateur` (
  `iduser` int NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `login` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(50) NOT NULL
  )
"""

#exécuter le curseur avec la méthode execute() et transmis la requéte SQL
cur.execute(sql2)

#*******************************************************************************************************
#requéte SQL permettant d'inserer les données dans la table nouveau né 
sql = "INSERT INTO `nouveau_ne`(nom, `prenom`, `nom_pere`, `situation_matrimoniale_père`, `fonction_père`, `nom_mère`, `situation_matrimonial_mère`, `fonction_mère`, `sexe_enfant`, `lieu_de_naissance`, `date_naissance`, `heure_de_naissance`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"

#************************(*******************************************************************************
#requéte SQL permettant d'inserer les données dans la table utilisateur
sql = "INSERT INTO `utilisateur`(`nom`, `prenom`, `login`, `password`, `role`) VALUES (%s, %s, %s, %s, %s)"
valueuser=("Nassir", "ahmat","ali","nassir19","Fonctionnaire")

cur.execute(sql, valueuser)

#*******************************************************************************************************
#valider la transaction

db.commit()

#afficher le nombre de lignes insérées

print(cur.rowcount, "ligne insérée.")
tkWindow.mainloop()