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

def validateLogin():
  db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "TopSecret_1998@",
    database = "naissanceDB"
    )
  cur = db.cursor()
  cur.execute("select * from nouveau_ne")
  res=cur.fetchall()
  db.commit()
  i=2
  b=2
  for re in res:
    data=re
    
    usernameLabel = Label(tkWindow, text=data[1]).grid(row=i, column=0)
    # separateur = Label(tkWindow, text="\n").grid(row=b+1, column=0)
    print(data[1])

  return
    
#tkwindow est une création de l'instance de la classe Tk
tkWindow = Tk()  
# definition de la taill de l'interface
tkWindow.geometry('500x600')  
# titre de l'interface
tkWindow.title('INTERFACE ADMIN')

#username label and text entry box

loginButton = Button(tkWindow, text="lister", command=validateLogin).grid(row=15, column=0)

db.commit()

#afficher le nombre de lignes insérées

# print(cur.rowcount, "ligne insérée.")
tkWindow.mainloop()