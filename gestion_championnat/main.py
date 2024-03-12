from models import *
from prettytable import PrettyTable

gestionnaire = GestionChampionnat()
gestionnaire.menu()
# Championnat.afficher()

# Assurez-vous que la classe Championnat est déjà définie avec la méthode ajouter_classement


# championnat = Championnat.AjouterChampionnat()
# print(championnat.calculer_point())
# print(championnat.afficher())
# print(championnat.afficher_classement())

# match = Match()
# match.ajout_resultat_matche()

equipe = Equipe()
print(equipe.afficher())