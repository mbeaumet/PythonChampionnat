from models import *
from prettytable import PrettyTable

# ETAPE 1 : AFFICHAGE DU MENU 
gestionnaire = GestionChampionnat()
gestionnaire.menu()
Championnat.afficher()

# # ETAPE 2 CREATION D'UN CHAMPIONNAT 
# championnat = Championnat.AjouterChampionnat() # enregistrement de cette création dans une variable 
# print(championnat.calculer_point()) # calcul des points totaux des équipes 
# print(championnat.afficher()) # affichage du nom des championnats qu'on connait 
# print(championnat.afficher_classement()) # affichage graphique du contnu du classement 

# # ETAPE 3 AJOUT D'UN MATCHE
# match = Match()
# match.ajout_resultat_matche()

# # ETAPE 4 AJOUT D'UNE EQUIPE
# equipe = Equipe()
# print(equipe.afficher())