from tkinter import *
from agro_GUI.agro_widgets import *
import matplotlib.pyplot as plt
def mise_en_page () :
 """
 Fonction de composition de la fenêtre app créée dans le programme principal
 """
 global app
 app.inserer_titre("Voici un titre de niveau 1", 1)
 texte = "Du texte qui peut être plus ou moins long"
 texte += " et contenir des sauts de ligne"
 app.inserer_text(texte)

 app.inserer_text("Un tableau avec des colonnes nommées")
 valeurs = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]
 entetes = ['nom', 'prenom', 'adresse', 'compte']
 app.inserer_tableau(valeurs, entetes)
 app.inserer_text("Une liste")
 app.inserer_listebullets(['bonjour', 'tout le monde'])

 app.inserer_text("Une image")
 app.inserer_image('img/perso.png')

 app.inserer_text("Une image obtenu avec la bibliothèque matplotlib !")
 draw_graph('img/scatter.png')
 app.inserer_image('img/scatter.png')
 app.manage_view() #afin de garantir un affichage correct de la fenêtre

def draw_graph(name):
 """
 Fonction de création et sauvegarde d'un graphique simple
 """
 plt.scatter([1,2,3], [1,2,3], marker='s', s=200) #On créé le nuage de points
 plt.savefig(name, dpi=30) #On sauvegarde la figure produite

###############################################################################
# Programme Principal #
###############################################################################
app = Agro_App("Première fenêtre")
mise_en_page()
app.show()