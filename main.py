from Manage_Joueurs import *
from morpion import *
from puissance4 import *
from allumette import *
from devinette import *
from class_joeueur import Joueur

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
botFacile : Joueur
botDifficile : Joueur
joueurs : list[Joueur]
players : list[Joueur]
players_nom : list[str]
i : int

botFacile = Joueur()
botDifficile = Joueur()
botFacile.nom = "BotFacile"
botDifficile.nom = "BotDifficile"
botFacile.botSimple = True
botDifficile.botSimple = False
botFacile.botComplex = False
botDifficile.botComplex = True
botDifficile.scoreA = 0
botDifficile.scoreM = 0
botDifficile.scoreD = 0
botDifficile.scoreP = 0
botDifficile.scoreT = 0
botFacile.scoreT = 0
botFacile.scoreA = 0
botFacile.scoreD = 0
botFacile.scoreM = 0
botFacile.scoreP = 0
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
            while nom == "0":
                nom = input("Le nom '0' n'est pas autorisé veuillez resaisir un autre nom : ")
            players_nom.append(nom)
        if len(joueurs) == 0:
            CreerTableJoueurs(joueurs)
        Entree_joueurs(joueurs,players_nom)
        for i in range(len(joueurs)):
            if joueurs[i].nom == players_nom[0]:
                players.append(joueurs[i])
                players_nom[0]="²"
            elif joueurs[i].nom == players_nom[1]:
                players.append(joueurs[i])
                players_nom[1] = "²"
    elif choix == 2:
        bot = int(input("Options de jeux:\n0. BotSimple x BotSimple\n1. BotSimple x BotComplexe\n2. BotComplexe x BotComplexe\n3. BotSimple x Joueur\n4. BotComplexe x Joueur\n5. Joueur x Joueur\n "))
        while bot < 0 and bot > 5:
            bot = int(input("Le chiffre doit être compris entre 0 et 5"))
        if bot == 0:
            devinette(botFacile,botFacile)
        elif bot == 1:
            devinette(botFacile,botDifficile)
        elif bot == 2:
            devinette(botDifficile,botDifficile)
        else:
            if len(players)==0: #verifie si il y a deja eu un saisie de joueur
                choix = -1
                print("Vous devez rentrer deux joueurs avant de lancer cette option\n")
            elif bot == 3:
                devinette(players[0],botFacile)
            elif bot == 4:
                devinette(players[0],botDifficile)
            elif bot == 5:
                devinette(players[0],players[1])
                enregistrer_joueurs(joueurs)
    elif choix == 3:
        bot = int(input("Options de jeux:\n0. BotSimple x BotSimple\n1. BotSimple x BotComplexe\n2. BotComplexe x BotComplexe\n3. BotSimple x Joueur\n4. BotComplexe x Joueur\n5. Joueur x Joueur\n "))
        while bot < 0 and bot > 5:
            bot = int(input("Le chiffre doit être compris entre 0 et 5"))
        if bot == 0:
            allumette(botFacile,botFacile)
        elif bot == 1:
            allumette(botFacile,botDifficile)
        elif bot == 2:
            allumette(botDifficile,botDifficile)
        else:
            if len(players)==0: #verifie si il y a deja eu un saisie de joueur
                choix = -1
                print("Vous devez rentrer deux joueurs avant de lancer cette option\n")
            elif bot == 3:
                allumette(players[0],botFacile)
            elif bot == 4:
                allumette(players[0],botDifficile)
            elif bot == 5:
                allumette(players[0],players[1])
                enregistrer_joueurs(joueurs)
    elif choix == 4:
        bot = int(input("Options de jeux:\n0. BotSimple x BotSimple\n1. BotSimple x BotComplexe\n2. BotComplexe x BotComplexe\n3. BotSimple x Joueur\n4. BotComplexe x Joueur\n5. Joueur x Joueur\n "))
        while bot < 0 and bot > 5:
            bot = int(input("Le chiffre doit être compris entre 0 et 5"))
        if bot == 0:
            Morpion(botFacile,botFacile)
        elif bot == 1:
            Morpion(botFacile,botDifficile)
        elif bot == 2:
            Morpion(botDifficile,botDifficile)
        else:
            if len(players)==0: #verifie si il y a deja eu un saisie de joueur
                choix = -1
                print("Vous devez rentrer deux joueurs avant de lancer cette option\n")
            elif bot == 3:
                Morpion(players[0],botFacile)
            elif bot == 4:
                Morpion(players[0],botDifficile)
            elif bot == 5:
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
        joueurs = []