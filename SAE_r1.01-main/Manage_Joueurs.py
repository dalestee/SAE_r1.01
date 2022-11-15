from class_morpion import *
from puissance4 import *
from class_joueur import *
from typing import BinaryIO
import pickle 

def enregistrer_joueurs(Tab_joueurs:list):
    fichier : BinaryIO
    fichier = open("Scores.dat","wb")
    for joueur in Tab_joueurs:
        pickle.dump(joueur,fichier)
    fichier.close()

def CreerTableJoueurs(Joueurs:list)->None:
    fichier : BinaryIO
    fin = False
    fichier = open("Scores.dat","rb")
    while not fin:
        try:
            Joueurs.append(pickle.load(fichier))
        except EOFError:
            fin = True
    fichier.close()

def Entree_joueurs(Joueurs : list)->None:
    i : int
    n : int
    fichier : BinaryIO
    noms_Joueurs : list

    noms_Joueurs = []
    Joueurs = []

    n = int(input("rentrez le nombre de joueurs (2 ou plus) : "))
    while n < 2: #demande le nombre de joueurs
        n = int(input("le nombre de joueurs doit être supérieur à 2 : "))

    for i in range(1,n+1): #demande le nom pour chaque joueur
        nom = input("Rentrez le nom du Joueur")
        noms_Joueurs.append(nom)

    CreerTableJoueurs(noms_Joueurs,Joueurs)#regarde si le joueur existe deja si non on crée le joueur
    for i in Joueurs:
        print(i.nom," ",i.scoreA)


    

if __name__ == "__main__":

    j1 = Joueur()
    j2 = Joueur()
    j1.nom = "a"
    j2.nom = "b"
    j1.scoreA = 1
    j1.scoreM = 0
    j1.scoreD = 0
    j1.scoreA = 0
    j1.scoreT= 0
    j2.scoreA = 0
    j2.scoreM = 0
    j2.scoreD = 0
    j2.scoreA = 0
    j2.scoreT= 0
    Joueurs = []


    fichier = open("Scores.dat","rb")
    fin = False
    while not fin:
        try:
            j_tmp = pickle.load(fichier)
            print(j_tmp.nom,j_tmp.scoreA)
        except EOFError:
            fin = True
    fichier.close()