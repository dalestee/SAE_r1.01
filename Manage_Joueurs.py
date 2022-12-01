from morpion import *
from puissance4 import *
from class_joueur import Joueur
from typing import BinaryIO
import pickle 

def leaderboard(Joueurs:list[Joueur])->None:
    """
    Procédure qui affiche un classement par rapport au jeu choisis
    Args:
        Joueurs (list[Joueur]): Liste des joueurs
    """

    temp_tab : list
    i : int

    temp_tab = []
    if len(Joueurs) == 0:
        print("La liste de joueurs est vide\n")
    else:
        jeu = int(input("rentrez le jeu que vous voulez faire le classement :\n1-Morpion\n2-Allumettes\n3-Devinette\n4-Puissance 4\n5-Total\n-> "))
        print("")
        while jeu < 1 and jeu > 5 :
            jeu = int(input("Erreur de saisie veuillez saisir 1, 2, 3, 4 ou 5 : "))
            print("")
        if jeu == 1:
            for i in range(len(Joueurs)):
                temp_tab.append([Joueurs[i].nom,Joueurs[i].scoreM])
        elif jeu == 2:
            for i in range(len(Joueurs)):
                temp_tab.append([Joueurs[i].nom,Joueurs[i].scoreA])
        elif jeu == 3:
            for i in range(len(Joueurs)):
                temp_tab.append([Joueurs[i].nom,Joueurs[i].scoreD])
        elif jeu == 4:
            for i in range(len(Joueurs)):
                temp_tab.append([Joueurs[i].nom,Joueurs[i].scoreP])
        elif jeu == 5:
            for i in range(len(Joueurs)):
                temp_tab.append([Joueurs[i].nom,Joueurs[i].scoreT])
        
        #tri à bulle 
        echange = True
        p = len(temp_tab)

        while echange and p>0:
            echange = False
            for i in range(p-1):
                #échange
                if temp_tab[i][1]<temp_tab[i+1][1]:
                    tmp=temp_tab[i]
                    temp_tab[i]=temp_tab[i+1]
                    temp_tab[i+1]=tmp
                    echange = True

            p -= 1
        print("Classement :\n")
        for joueur in temp_tab:
            print(joueur[0]," ",joueur[1],"\n")

def enregistrer_joueurs(Tab_joueurs:list[Joueur]):
    """
    Procédure qui enregistre les joueurs dans le fichier binaire
    Args:
        Tab_joueurs (list[Joueur]):
    """
    i : int
    fichier : BinaryIO
    fichier = open("Scores.dat","wb")
    joueur : Joueur
    for i in range(len(Tab_joueurs)):
        pickle.dump(Tab_joueurs[i],fichier)
    fichier.close()

def CreerTableJoueurs(Joueurs:list[Joueur])->None:
    """
    Procédure que gère l'ajout des joueurs dans une liste
    Args:
        Joueurs (list[Joueur]):
    """
    fichier : BinaryIO
    fin = False
    fichier = open("Scores.dat","rb")
    while not fin:
        try:
            Joueurs.append(pickle.load(fichier))
        except EOFError:
            fin = True
    fichier.close()

def Entree_joueurs(Joueurs:list[Joueur],players:list[str])->None:
    """
    Procédure qui gère l'entrée des joueurs
    Args:
        Joueurs (list[Joueur]):
        players (list[str]): 
    """
    i : int
    #regarde si le joueur existe deja si non on crée le joueur
    for i in range(len(players)):
        existe = False
        for j in Joueurs:
            if players[i] == j.nom:
                existe = True
        if not existe:
            j_temp = Joueur()
            j_temp.nom = players[i]
            j_temp.scoreA = 0
            j_temp.scoreD = 0
            j_temp.scoreM = 0
            j_temp.scoreP = 0
            j_temp.scoreT = 0
            Joueurs.append(j_temp)

def effacer_Joueurs()->None:
    """
    Procédure qui efface le contenu du fichier Scores.dat
    """
    fichier : BinaryIO
    fichier = open("Scores.dat","wb")
    fichier.close()
 
if __name__ == "__main__":
    pass
