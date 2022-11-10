from numpy import append
from class_morpion import *
from puissance4 import *

class Joueur:
    def __init__(self):
        self.score = 0
        self.nom = ""

if __name__ == "__main__":

    i : int
    n : int
    Joueur1 : Joueur

    Joueur1 = Joueur()

    Joueurs = []
    n = int(input("rentrez le nombre de joueurs : "))

    for i in range(0,n):
        i = Joueur()
        Joueurs.append(i.nom = input("Rentrez le nom du Joueur",i," : "))



