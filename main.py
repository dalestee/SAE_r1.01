from Manage_Joueurs import *
from morpion import *
from puissance4 import *
from allumette import *
from devinette import *
from class_joueur import Joueur

def menu()->int:
    """
    Fonction qui renvoi le choix de l'user suite à l'affichage du menu
    Returns:
        int : entier compris de 1 à 8
    """
    print("")
    print("-------------------------- MENU --------------------------")
    print("|                                                        |")
    print("| - 1 pour entrer les joueurs                            |")
    print("| - 2 pour jouer aux devinettes                          |")
    print("| - 3 pour jouer aux allumettes                          |")
    print("| - 4 pour jouer au morpion                              |")
    print("| - 5 pour jouer au Puissance 4                          |")
    print("| - 6 pour afficher le rang de chaque joueur             |")
    print("| - 7 pour réinitialiser la liste de joueurs             |")
    print("| - 8 pour quitter                                       |")
    print("|                                                        |")
    print("----------------------------------------------------------")
    print("")
    choix=int(input("Veuillez entrer votre choix  : "))
    while choix<1 or choix>8:
        print("Vous n'avez pas rentré une valeur valide dans le programme.")
        choix=int(input("Veuillez entrer votre choix  : "))
    print("")
    return choix
#---------------------main-----------------------
choix : int
joueurs : list[Joueur]
players : list[Joueur]
players_nom : list[str]

joueurs = []
players_nom = [] #le nom des deux joueurs qui jouent actuelment
players = []
choix = -1
while choix != 8:
    choix = menu()
    if choix == 1:
        players_nom = []
        players = []
        for i in range(1,3): #demande le nom pour chaque joueur
            print("Rentrez le nom du Joueur ",i," : ",end="")
            nom = input("")
            players_nom.append(nom)
        if len(joueurs) == 0:
            CreerTableJoueurs(joueurs)
        Entree_joueurs(joueurs,players_nom)
        for joueur in joueurs:
            if joueur.nom == players_nom[0]:
                players.append(joueur)
                players_nom[0]="²"
            elif joueur.nom == players_nom[1]:
                players.append(joueur)
                players_nom[1] = "²"
    elif choix == 2:
        if len(players)==0: #verifie si il y a deja eu un saisie de joueur
            choix = -1
            print("Vous devez rentrer deux joueurs avant de lancer cette option\n")
        else:
            devinette(players[0],players[1])
            enregistrer_joueurs(joueurs)
    elif choix == 3:
        if len(players)==0:
            choix = -1
            print("Vous devez rentrer deux joueurs avant de lancer cette option\n")
        else:
            allumette(players[0],players[1])
            enregistrer_joueurs(joueurs)
    elif choix == 4:
        if len(players)==0:
            choix = -1
            print("Vous devez rentrer deux joueurs avant de lancer cette option\n")
        else:
            Morpion(players[0],players[1])
            enregistrer_joueurs(joueurs)
    elif choix == 5:
        if len(players)==0:
            choix = -1
            print("Vous devez rentrer deux joueurs avant de lancer cette option\n")
        else:
            Puissance4(players[0],players[1])
            enregistrer_joueurs(joueurs)
    elif choix == 6:
        if len(players)==0:
            joueurs = []
            CreerTableJoueurs(joueurs)
        leaderboard(joueurs)
    elif choix == 7:
        effacer_Joueurs()
        Joueurs = []