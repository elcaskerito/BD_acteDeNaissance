from tkinter import *

from tkinter.ttk import *

import sqlite3

import sys

import traceback
import mysql.connector
 

# fenêtre principale

def admin():
    fenetre = Tk()

    fenetre.title('Interface Admin')

    

    # libellé

    libelle = Label(fenetre, text = 'Tous les nouveaux nés')

    libelle.pack(padx = 10, pady = 10)

    

    #tableau

    tableau = Treeview(fenetre, columns=('Nom', 'prenom','nom du père', 'situation matrimonial du père','fonction du pere','nom de la mère','situation matrimonial de la mère', 'fonction de la mère','sexe de l\'enfant','lieu de naissance','date de naissance','heure de naissance'))

    tableau.heading('Nom', text='Nom')

    tableau.heading('prenom', text='Prénom')

    tableau.heading('nom du père', text='nom du père')

    tableau.heading('situation matrimonial du père', text='situation matrimonial du père')

    tableau.heading('fonction du pere', text='fonction du pere')

    tableau.heading('nom de la mère', text='nom de la mère')

    tableau.heading('situation matrimonial de la mère', text='situation matrimonial de la mère')

    tableau.heading('fonction de la mère', text='fonction de la mère')

    tableau.heading('sexe de l\'enfant', text='sexe de l\'enfant')

    tableau.heading('lieu de naissance', text='lieu de naissance')

    tableau.heading('date de naissance', text='date de naissance')

    tableau.heading('heure de naissance', text='heure de naissance')

    tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert

    tableau.pack(padx = 10, pady = (0, 10))

    

    # bouton pour terminer le programme

    bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

    bouton_terminer.pack(padx = 10, pady = (0, 10))

    

    # lecture et affichage des données

    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "TopSecret_1998@",
    database = "naissanceDB"
    )

    #créer un curseur de base de données pour effectuer des opérations SQL
    cur = db.cursor()




    requete = 'SELECT * from nouveau_ne'

    cur.execute(requete)

    resultat = cur.fetchall()

    

    if len(resultat):

        for enreg in resultat:

            # chaque ligne n'a pas de parent, est ajoutée à la fin de la liste, utilise le champ id comme identifiant et on fournit les valeurs pour chacune des colonnes du tableau

            tableau.insert('', 'end', iid=enreg[0], values=(enreg[1], enreg[2], enreg[3],enreg[4],enreg[5],enreg[6],enreg[7],enreg[8],enreg[9],enreg[10],enreg[11],enreg[12]))

    else:

        libelle.configure(text = 'Il n\'y a présentement aucun étudiant.')

        tableau.pack_forget()


    # la fenêtre s'affiche puis attend les interactions de l'usager

    fenetre.mainloop()
admin()