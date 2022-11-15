from class_morpion import *
from puissance4 import *
from class_joueur import *
from typing import BinaryIO
import pickle 

def leaderboard(Joueurs:list):
    temp_tab : list
    joueur : int

    temp_tab = []
    jeu = int(input("rentrez le jeu que vous voulez faire le classement :\n1-Morpion\n2-Alumettes\n3-Devinette\n4-Puissance 4\n5-Total\n-> "))
    print("")
    while jeu > 1 and jeu < 5 :
        jeu = int(input("Erreur de saisie veuillez saisir 1, 2, 3, 4 ou 5 : "))
        print("")
    if jeu == 1:
        for joueur in Joueurs:
            temp_tab.append([joueur.nom,joueur.scoreM])
    elif jeu == 2:
        if jeu == 1:
            for joueur in Joueurs:
                temp_tab.append([joueur.nom,joueur.scoreA])
    elif jeu == 3:
        if jeu == 1:
            for joueur in Joueurs:
                temp_tab.append([joueur.nom,joueur.scoreD])
    elif jeu == 4:
        if jeu == 1:
            for joueur in Joueurs:
                temp_tab.append([joueur.nom,joueur.scoreP])
    elif jeu == 5:
        if jeu == 1:
            for joueur in Joueurs:
                temp_tab.append([joueur.nom,joueur.scoreT])
    
    
    echange = True
    p = len(temp_tab)

    while echange and p>0:
        echange = False
        for i in range(p-1):
            #échange
            if temp_tab[i][1]>temp_tab[i+1][1]:
                tmp=temp_tab[i]
                temp_tab[i]=temp_tab[i+1]
                temp_tab[i+1]=tmp
                echange = True

        p -= 1
    print("Classement :\n")
    for joueur in temp_tab:
        print(joueur[0]," ",joueur[1],"--\n")


def enregistrer_joueurs(Tab_joueurs:list):
    fichier : BinaryIO
    fichier = open("Scores.dat","wb")
    for joueur in Tab_joueurs:
        joueur.scoreT = joueur.scoreA + joueur.scoreD + joueur.scoreP + joueur.scoreM
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

def Entree_joueurs(Joueurs:list)->None:
    i : int
    n : int
    fichier : BinaryIO
    noms_Joueurs : list
    existe : bool

    noms_Joueurs = []
    n = int(input("rentrez le nombre de joueurs (2 ou plus) : "))
    while n < 2: #demande le nombre de joueurs
        n = int(input("le nombre de joueurs doit être supérieur à 2 : "))

    for i in range(1,n+1): #demande le nom pour chaque joueur
        nom = input("Rentrez le nom du Joueur : ")
        noms_Joueurs.append(nom)

    CreerTableJoueurs(Joueurs)
    #regarde si le joueur existe deja si non on crée le joueur
    for nom in noms_Joueurs:
        existe = False
        for j in Joueurs:
            if nom == j.nom:
                existe = True
        if not existe:
            j_temp = Joueur()
            j_temp.nom = nom
            j_temp.scoreA = 0
            j_temp.scoreD = 0
            j_temp.scoreM = 0
            j_temp.scoreP = 0
            j_temp.scoreT = 0
            Joueurs.append(j_temp)
    for i in Joueurs:
        print(i.nom," ",i.scoreA)


    

if __name__ == "__main__":
    Joueurs : list
    Joueurs = []
    Entree_joueurs(Joueurs)
    enregistrer_joueurs(Joueurs)
