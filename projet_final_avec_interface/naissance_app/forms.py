
from django import forms
from .models import Utilisateur, nouveau_ne
from django.forms import ModelForm



class nouveau_neForm(ModelForm):
						class Meta:
							model = nouveau_ne
							fields = ( 'nom', 'prenom', 'sexe', 'lieu', 'dateAnne', 'heure' , 'nom_pere', 'situ_matri_pere', 'fonction_pere', 'nom_mere', 'fonction_mere', 'situa_matri_mere' )

							labels = {
								'nom': '',  
								'prenom': '',    
								'sexe': '',  
								'lieu': '', 
								'dateAnne': '',
								'heure': '',  
								'nom_pere': '',
								'situ_matri_pere': '',
								'fonction_pere':'', 
								'nom_mere':'', 
								'fonction_mere':'', 
								'situa_matri_mere':'', 
							}

							widgets = {
								'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom',}),  
								'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom',}), 
								'sexe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexe',}), 
								'lieu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu de naissance',}),  
								'dateAnne': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de naissance',}), 
								'heure': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Heure de naissance',}), 
								'nom_pere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du pere',}),
								'situ_matri_pere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Situation matrimoniale',}),
								'fonction_pere':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fonction',}), 
								'nom_mere':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la mere',}),
								'fonction_mere':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fonction',}), 
								'situa_matri_mere':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'situation matrimoniale',}),
							}



class UtlisateurForm(ModelForm):
						class Meta:
							model = Utilisateur
							fields = ( 'nom', 'prenom', 'mail', 'login', 'motDePass', 'role' )

							labels = {
								'nom': '',  
								'prenom': '',    
								'mail': '',  
								'login': '', 
								'motDePass': '',
								'role': '',  
								 
							}

							widgets = {
								'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom',}),  
								'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom',}), 
								'mail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mail',}), 
								'login': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login',}),  
								'motDePass': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe',}), 
								'role': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Selectioner un role',}), 
								
							}