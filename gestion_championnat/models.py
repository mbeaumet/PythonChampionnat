import random 
from prettytable import PrettyTable
import sys





class GestionChampionnat:
    listChampionnat=[]
    # def __init__(self):
    # @staticmethod
    def menu(self):
        print("1/ Ajouter championnat")
        print("2/ Ajouter equipe")
        print("3/ Ajouter resultat de matche")
        print("4/ Afficher les championnats")
        print("5/ Afficher liste équipe d'un championnat")
        print("6/ Afficher le classement d'un championnat")
        print("7/ Quitter l'application")

        choixMenu = int(input("Choisissez l'option de votre choix dans le menu suivant le numéro indiquer ?"))
        while(choixMenu != 7):
            if (choixMenu == 1):
                gestion_championnat = Championnat()
                # Championnat.ajouter_classement()
                more_data = input("Avez vous d'autre donnée a enregistrer ? (Si oui répondez oui sinon non)")
                if (more_data == "oui"):
                    return GestionChampionnat.menu(self)
                else : 
                    print("Merci pour votre ajout")
                    print(GestionChampionnat.listChampionnat)
                return "Championnat ajouter"


            elif (choixMenu == 2): # Ajoutez une équipe a la liste des equipes 
                equipe = Equipe() 
                Equipe.list_info_equipe.append([equipe.nom,equipe.date_creation,equipe.stade,equipe.capacite_stade,equipe.entraineur,equipe.president])               
                more_data = input("Avez vous d'autre donnée a enregistrer ? (Si oui répondez oui sinon non)")
                if (more_data == "oui"):
                    return GestionChampionnat.menu(self)
                else : 
                    return "Merci de votre ajout"

            elif (choixMenu == 3): # Saisir le résultat d'un matche A REFAIRE 
                matche = Match.ajout_resultat_matche(self)  
                Match.list_info_matche.append([matche.score_equipe_1,matche.score_equipe_2,matche.numero_journee,matche.equipe_1,matche.equipe_2])
                more_data = input("Avez vous d'autre donnée a enregistrer ? (Si oui répondez oui sinon non)")
                if (more_data == "oui"):
                    print(Match.list_info_equipe)
                    return GestionChampionnat.menu(self)
                else : 
                    return "Merci de votre ajout"
                    print(Match.list_info_equipe)

            elif (choixMenu == 4): # Afficher les championnats A REFAIRE
                print(Championnat.afficher(self,gestion_championnat))
                return "Choix quatres"
                more_data = input("Avez vous d'autre donnée a enregistrer ? (Si oui répondez oui sinon non)")

            elif (choixMenu == 5): # Afficher la liste des équipes d’un championnat.
                if (Equipe.list_info_equipe != []) : 
                    # Pourquoi qu'une info dans la liste list_info_equipe
                    print(Equipe.list_info_equipe)
                    for equipe in Equipe.list_info_equipe:
                        print(equipe)
                else : 
                    return ("Pas d'information")
                    
                more_data = input("Avez vous d'autre donnée a enregistrer ? (Si oui répondez oui sinon non)")

            elif (choixMenu == 6): # Afficher le classement d’un championnat
                choixMenu = int(input("Choisissez l'option de votre choix dans le menu suivant le numéro indiquer ?"))
                return Championnat.afficher(self)
                more_data = input("Avez vous d'autre donnée a enregistrer ? (Si oui répondez oui sinon non)")
            elif (choixMenu == 7): # Quitter l'application 
                sys.exit()

    def affiche_menu():
        menu = menu()
        return (menu)

class Championnat:
    id_counter = 0
    listChampionnat = []  # Ajout de la liste des championnats à la classe

    def __init__(self):
        Championnat.id_counter +=1
        self.id = Championnat.id_counter
        self.nom = input("Nom du championnat : ")
        self.pays = input("pays : ")
        self.date_debut = input("Date de début :")
        self.date_fin = input("Date de fin :")
        self.point_gagne = int(input("Nombre de point gagné :"))
        self.point_perdu = int(input("Nombre de point perdu :"))
        self.point_nul = int(input("Nombre de point obtenu pendant un matche nul :"))
        self.type_classement = input("Type de classement :")
        self.point=int(input("Nombre de point :"))
        self.equipes = input("Nom des équipe :")
        self.matchs = int(input("Nombre de matche :"))
        GestionChampionnat.listChampionnat.append(self.nom)

    @staticmethod
    def ajouter_classement():
        # Créez une nouvelle instance de Championnat
        nouveau_championnat = Championnat()

        # Saisie des données depuis l'utilisateur
        Championnat.id_counter +=1
        self.id = Championnat.id_counter
        nouveau_championnat_nom = input("Nom du championnat : ")
        nouveau_championnat.pays = input("Nom du pays d'ou provient le championnat : ")
        nouveau_championnat.date_debut = input("Date de début du championnat : ")
        nouveau_championnat.date_fin = input("Date de fin du championnat : ")
        nouveau_championnat.point_gagne = int(input("Nombre de points gagnés : "))
        nouveau_championnat.point_perdu = int(input("Nombre de points perdus : "))
        nouveau_championnat.point_nul = int(input("Nombre de points pour les matchs nuls : "))
        nouveau_championnat.type_classement = input("Type de classement : ")
        nouveau_championnat.equipes = input("Noms de l'équipe : ")
        nouveau_championnat.matchs = int(input("Nombre de matchs joués : "))

        # Ajout de la nouvelle instance à la liste des championnats
        Championnat.listChampionnat.append(nouveau_championnat)

        # Retournez la nouvelle instance créée
        return 'enregistrer'

    def calculer_point(self):
        self.point = self.point_gagne +  self.point_perdu + self.point_nul 
        return self.point

    def afficher(self):
        DataChampionnat = PrettyTable()
        DataChampionnat.field_names = ["ID", "Nom", "Date Début", "Date Fin", "Points Gagnés", "Points Perdus", "Points Nuls", "Type Classement", "Équipes", "Matchs"]

        DataChampionnat.add_row([self.id, self.nom, self.date_debut, self.date_fin, self.point_gagne, self.point_perdu, self.point_nul, self.type_classement, self.equipes, self.matchs])
    
        return DataChampionnat

    def afficher_classement(self,gestion_chamionnat):
        DataClassement = PrettyTable()
        DataClassement.field_names = ["id", "nom", "Pts", "J.", "G.", "N.", "P."]

        DataClassement.add_row([self.id, self.equipes, self.point, self.matchs, self.point_gagne, self.point_nul, self.point_perdu])

        return DataClassement

class Match:
    list_info_matche = []
    def __init__(self):
        self.score_equipe_1 = ""
        self.score_equipe_2 = ""
        self.numero_journee = ""
        self.equipe_1 = ""
        self.equipe_2 = ""
    
    def ajout_resultat_matche(self):
        self.score_equipe_1 = int(input("Qu'elle est le score de l'équipe numéro 1 : ")) 
        self.score_equipe_2 = int(input("Qu'elle est le score de l'équipe numéro 2 : ")) 
        self.numero_journee = int(input("Qu'elle est le numéro de la journée : "))
        self.equipe_1 = input("Nom de l'équipe numéro une : ")
        self.equipe_2 = input("Nom de l'équipe numéro deux : ")

    def score_equipe_1(self):
        return ("score de l'équipe numéro 1 :",self.score_equipe_1)

    def score_equipe_2(self):
        return ("score de l'équipe numéro 1 :",self.score_equipe_2)

class Equipe:
    equipe_id = 0
    list_info_equipe = [] 
    def __init__(self):
        Equipe.equipe_id =+ 1
        self.id = Equipe.equipe_id
        self.nom = input("Qu'elle est le nom de cette équipe : ")
        self.date_creation = int(input("Qu'elle est la date de création de votre club : "))
        self.capacite_stade = int(input("Qu'elle est la capacité du stade : "))
        self.stade = input("Qu'elle est le nom du stade : ")
        self.entraineur = input("Qu'elle est le nom de l'entraineur : ")
        self.president = input("Qu'elle est le nom du président : ")

    def afficher(self):
        return (        
            "id :", self.id,
            "nom : ", self.nom,
            "date de création", self.date_creation,
            "Nom du stade :", self.stade,
            "Nom de l'entraineur :",self.entraineur,
            "Nom du président du club :",self.president,
        )