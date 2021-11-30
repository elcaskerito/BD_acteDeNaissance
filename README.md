# BASE DE DONNEES POUR ENREGISTRER LES NAISSANCES
Dans le cadre de la realisation d'une application d'enregistrement des nouveaux (elles) nés,nous avons mis en place cette base de données pour avoir l'statistique exacte des naissances dans les differents hopitaux du Pays.
pour utiliser cette base de données, il faut demarrer un systeme de gestion de base de donnée.
puis aller executer le scripte ecrit en python pour effectuer un enregistrement.

# Pré-requis : 
#
# - avoir un Server local avec SGBD mysql
# - installer mysql-connector pour python.
# - installer python dans votre machine
# 
#
# Guide D'Utilisation : 
#   vous avez deux manières d'utiliser ce programme 
# 1) Utiliser le script denommé "programme.py" avec une une base de donnée vide préalablement créer.
#   - avant d'exécuter ce script il faut dabord créer au préalable une base de données nommée "naissanceDB" dans votre système de gestion de Base de Données
#   - ensuite ajouter le mot de passe de votre SGBD a la ligne 24 de ce fichier. si votre SGBD n'a pas de mot de passe laisser cette partie vide
# 2) Importer le script naissanceDB dans un SGBD ensuite executer le fichier programme
