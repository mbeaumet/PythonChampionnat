import sys
from prettytable import PrettyTable

class GestionChampionnat:
    listChampionnat = []

    def menu(self):
        print("1/ Ajouter championnat")
        print("2/ Ajouter equipe")
        print("3/ Ajouter resultat de matche")
        print("4/ Afficher les championnats")
        print("5/ Afficher liste équipe d'un championnat")
        print("6/ Afficher le classement d'un championnat")
        print("7/ Quitter l'application")

        choixMenu = int(input("Choisissez l'option de votre choix dans le menu suivant le numéro indiquer ?"))
        while choixMenu <= 7:
            if choixMenu == 1:
                Championnat.ajouter_championnat(self)
            elif choixMenu == 2:
                Equipe.ajouter_equipe(self)
            elif choixMenu == 3:
                Match.ajout_resultat_matche(self)
            elif choixMenu == 4:
                GestionChampionnat.afficher_list_championnats(self)
            elif choixMenu == 5:
                GestionChampionnat.afficher_equipes_championnat(self)
            elif choixMenu == 6:
                GestionChampionnat.afficher_classement_championnat(self)
            elif choixMenu == 7:
                exit()

            choixMenu = int(input("Choisissez l'option de votre choix dans le menu suivant le numéro indiquer ? "))


    @staticmethod
    def afficher_list_championnats(self):
        if GestionChampionnat.listChampionnat:
            for champ in GestionChampionnat.listChampionnat:
                print(champ)
        else:
            print("Pas de championnat disponible.")
        
        GestionChampionnat.menu(self)

    @staticmethod
    def afficher_equipes_championnat(self):
        Equipe.afficher_equipe(self)
        GestionChampionnat.menu(self)
        

    @staticmethod
    def afficher_classement_championnat(self):
        if(Championnat.list_data_championnat != None):
            for champ in GestionChampionnat.listChampionnat:
                print(Championnat.afficher_classement(self))
        else : 
            print("Ajoutez d'abord un championnat")
        GestionChampionnat.menu(self)

class Championnat:
    id_counter = 0
    list_data_championnat = []

    def __init__(self):
        Championnat.id_counter += 1
        self.id = Championnat.id_counter
        self.nom = input("Nom du championnat : ")
        self.pays = input("Pays : ")
        self.date_debut = int(input("Date de début : "))
        self.date_fin = int(input("Date de fin : "))
        self.point_gagne = int(input("Nombre de points gagnés : "))
        self.point_perdu = int(input("Nombre de points perdus : "))
        self.point_nul = int(input("Nombre de points pour les matchs nuls : "))
        self.type_classement = input("Type de classement : ")
        self.equipes = input("Noms des équipes : ")
        self.matchs = input("Nombre de matchs : ")


    def ajouter_championnat(self):
        championnat = Championnat()
        Championnat.list_data_championnat.append([championnat.id,championnat.nom,championnat.point_gagne,championnat.point_perdu,championnat.point_nul,championnat.matchs])
        GestionChampionnat.listChampionnat.append(championnat.nom)
        GestionChampionnat.menu(self)

    def calculer_point(self):
        print(self.point_gagne + self.point_perdu + self.point_nul)
        GestionChampionnat.menu(self)

    def afficher_classement(self):
        table = PrettyTable()
        table.field_names = ["ID", "Nom", "Points", "Matchs"]
        for index in range(len(Championnat.list_data_championnat)): 
            calculer_point = Championnat.list_data_championnat[index][2] + Championnat.list_data_championnat[index][4] + Championnat.list_data_championnat[index][3]
            table.add_row([Championnat.list_data_championnat[index][0], Championnat.list_data_championnat[index][1], calculer_point, Championnat.list_data_championnat[index][5]])
        return table
        GestionChampionnat.menu(self)

class Match:
    list_info_matche = []

    @staticmethod
    def ajout_resultat_matche(self):
        score_equipe_1 = int(input("Score de l'équipe numéro 1 : ")) 
        score_equipe_2 = int(input("Score de l'équipe numéro 2 : ")) 
        numero_journee = int(input("Numéro de la journée : "))
        equipe_1 = input("Nom de l'équipe numéro une : ")
        equipe_2 = input("Nom de l'équipe numéro deux : ")
        Match.list_info_matche.append([score_equipe_1, score_equipe_2, numero_journee, equipe_1, equipe_2])
        GestionChampionnat.menu(self)

class Equipe:
    equipe_id = 0
    list_info_equipe = []

    def __init__(self):
        Equipe.equipe_id += 1
        self.id = Equipe.equipe_id
        self.nom = input("Nom de l'équipe : ")
        self.date_creation = int(input("Date de création : "))
        self.capacite_stade = int(input("Capacité du stade : "))
        self.stade = input("Nom du stade : ")
        self.entraineur = input("Nom de l'entraineur : ")
        self.president = input("Nom du président : ")

    @staticmethod
    def ajouter_equipe(self):
        equipe = Equipe()
        print(equipe.nom)
        Equipe.list_info_equipe.append([equipe.nom,equipe.date_creation,equipe.capacite_stade,equipe.stade,equipe.entraineur,equipe.president])
        GestionChampionnat.menu(self)

    def afficher_equipe(self):
        if (Equipe.list_info_equipe != None):
            print(Equipe.list_info_equipe)
        else : 
            print("Crée une équipe d'abord")

def main(self):
    gestionnaire = GestionChampionnat()
    gestionnaire.menu(self)

if __name__ == "__main__":
    main()
