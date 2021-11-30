# -*- coding: utf-8 -*-
#*****************************************************************************************************#
#   PROGRAMME POUR LA CREATION D'UNE BASE DE DONNEES D'ENREGISTREMENT DES NAISSANCES A L'HÔPITAL      # 
#                                                                                                     #
#*****************************************************************************************************#
import mysql.connector

#connexion au base de données
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "TopSecret@_1998",
  database = "naissanceDB1"
)

#créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()

#******************************************************************************************************
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
sql = "INSERT INTO `nouveau_ne`(id_nouveau_né,`nom`, `prenom`, `nom_pere`, `situation_matrimoniale_père`, `fonction_père`, `nom_mère`, `situation_matrimonial_mère`, `fonction_mère`, `sexe_enfant`, `lieu_de_naissance`, `date_naissance`, `heure_de_naissance`) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"

#les valeurs de la requéte SQL
value = (1,"idris", "mahamat  ","Mahamat idris","marié","Avocat","kelou fatime","mariée", "sage femme","masculin","N'djamena","1998-11-1","10:20")

cur.execute(sql, value)

#*******************************************************************************************************
#requéte SQL permettant d'inserer les données dans la table utilisateur
sql = "INSERT INTO `utilisateur`(`iduser`, `nom`, `prenom`, `login`, `password`, `role`) VALUES (%s, %s, %s, %s, %s, %s)"
valueuser=(1,"Nassir", "ahmat","ali","nassir19","Fonctionnaire")

cur.execute(sql, valueuser)

#*******************************************************************************************************
#valider la transaction

db.commit()

#afficher le nombre de lignes insérées

print(cur.rowcount, "ligne insérée.")