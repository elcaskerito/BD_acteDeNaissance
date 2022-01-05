from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    Role=(('fonctionnaire', 'fonctionnaire'),
        ('administrateur','administrateur'))
    nom = models.CharField('Nom', max_length=100)
    prenom= models.CharField('Prenom', max_length=100)
    mail= models.CharField('Email', max_length=150)
    login= models.CharField('Login', max_length=120)
    motDePass= models.CharField('PassWord', max_length=120)
    role = models.CharField(max_length=120, choices=Role)
    def __str__(self):
	    return self.nom

class nouveau_ne(models.Model):
    nom = models.CharField('Nom', max_length=100)
    prenom= models.CharField('Prenom', max_length=100)
    sexe = models.CharField('Sexe', max_length=50)
    lieu = models.CharField('lieu de naissance', max_length=100)
    dateAnne= models.DateField('Date et annee de naissance', max_length=100)
    heure = models.TimeField('Heure de naissance', max_length=100)
    nom_pere= models.CharField('Nom de pere', max_length=150)
    situ_matri_pere= models.CharField('situation matrimoniale du pere', max_length=100)
    fonction_pere = models.CharField('Fonction de pere', max_length=100)
    nom_mere= models.CharField('Nom de mere', max_length=150)
    fonction_mere = models.CharField('Fonction de la mere', max_length=100)
    situa_matri_mere = models.CharField('situation matrimoniale de la mere', max_length=100)
    def __str__(self):
	    return self.nom