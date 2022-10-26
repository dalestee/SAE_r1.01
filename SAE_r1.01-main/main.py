from class_morpion import *
from puissance4 import *
from class_joueur import *
 
if __name__ == "__main__":

    i : int
    n : int
    joueurs : list
    jeu : int

    jeu = -1
    joueurs = []
    n = -1

    while n < 1:
        n = int(input("rentrez le nombre de joueurs : "))
        if n < 1:
            print("le chiffre doit être supérieur à 0")
    for i in range(n):
        joueurs.append(Joueur(input("rentrez le nom du joueur -> ")))
    while jeu > 4 or jeu < 1:
        jeu = int(input("\n -----------------------------\n\nRentrez la valeur de quel jeu vous voulez jouer \n Morpion :    1 \n\n Puissance4 : 2\n\n Allumettes : 3\n\n Devinettes : 4\n\n --> "))

    




