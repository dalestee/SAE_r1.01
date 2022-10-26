from multiprocessing.dummy import JoinableQueue
from random import random
from class_joueur import Joueur

class morpion:
    def __init__(self):
        """
        definis l'objet morpion comme un plateau de 3 par 3
        """
        self.cases = [["_","_","_"],
                      ["_","_","_"],
                      [" "," "," "]]
    
    def afficher(self):
        """
        cette méthode permet d'afficher l'objet morpion 
        """
        print(" _",self.cases[0][0],"_|_",self.cases[0][1],"_|_",self.cases[0][2],"_","\n","_",self.cases[1][0],"_|_",self.cases[1][1],
        "_|_",self.cases[1][2],"_\n ","",self.cases[2][0]," | ",self.cases[2][1]," | ",self.cases[2][2]," ")
        print()

    def marque(self,x:int,y:int,car : str):
        """
        entrée : (x,y : entiers) car 
        cette méthode permet suite à l'entrée des coordonées des cases et du Joueur qui joue d'ajouter  
        """
        self.cases[x][y] = car

    def veri_Jeu(self,tour):
        """
        cette methode verifie si la partie est fini, si oui elle envoi "X" ou "O" pour le gagnant, 0 pour égalité et -1 pour le reste des cas
        """
        if tour > 9:
            return 0

        elif self.cases[0][0] == self.cases[1][1] and self.cases[0][0] == self.cases[2][2] and self.cases[0][0] != "_" :
            return self.cases[0][0]

        elif self.cases[0][0] == self.cases[1][0] and self.cases[0][0] == self.cases[2][0] and self.cases[0][0] != "_" :
            return self.cases[0][0]

        elif self.cases[0][0] == self.cases[0][1] and self.cases[0][0] == self.cases[0][2] and self.cases[0][0] != "_" :
            return self.cases[0][0]

        elif self.cases[0][1] == self.cases[1][1] and self.cases[0][1] == self.cases[2][1] and self.cases[0][1] != "_" :
            return self.cases[0][1]

        elif self.cases[0][2] == self.cases[1][2] and self.cases[0][2] == self.cases[2][2] and self.cases[0][2] != "_" :
            return self.cases[0][2]

        elif self.cases[0][2] == self.cases[1][1] and self.cases[0][2] == self.cases[2][1] and self.cases[0][2] != "_" :
            return self.cases[0][2]

        elif self.cases[1][0] == self.cases[1][1] and self.cases[1][0] == self.cases[1][2] and self.cases[1][0] != "_" :
            return self.cases[1][0]

        elif self.cases[2][0] == self.cases[2][1] and self.cases[2][0] == self.cases[2][2] and self.cases[2][0] != "_" :
            return self.cases[2][0]
        
        else:
            return -1

    def veri_Pvictoire(self):
        """
        à l'entrée du morpion, la méthode renvoi un tableau si il y a possibilité de victoire ou defaite, qui contient les coordonéees de la case à jouer dans ce cas et le joueur qui peut gagner
        , autrement elle renvoi -1   
        """

        if self.cases[0][0] == self.cases[0][1] and self.cases[0][2] == "_"  and self.cases[0][0] != "_":
            return [0,2], self.cases[0][0]

        elif self.cases[0][2] == self.cases[0][1] and self.cases[0][0] == "_" and self.cases[0][2] != "_":
            return [0,0], self.cases[0][2]

        elif self.cases[0][0] == self.cases[1][0] and self.cases[2][0] == " " and self.cases[0][0] != "_":
            return [2,0], self.cases[0][0]

        elif self.cases[2][0] == self.cases[1][0] and self.cases[0][0] == "_" and self.cases[2][0] != " ":
            return [0,0], self.cases[2][0]

        elif self.cases[2][2] == self.cases[1][1] and self.cases[0][0] == "_" and self.cases[2][2] != " ":
            return [0,0], self.cases[2][2]

        elif self.cases[0][1] == self.cases[1][1] and self.cases[2][1] == " " and self.cases[0][1] != "_":
            return [2,1], self.cases[0][1]

        elif self.cases[2][1] == self.cases[1][1] and self.cases[0][1] == "_" and self.cases[2][1] != " ":
            return [0,1], self.cases[2][1]

        elif self.cases[0][2] == self.cases[1][1] and self.cases[2][0] == " " and self.cases[0][2] != "_":
            return [2,0], self.cases[0][2]

        elif self.cases[2][0] == self.cases[1][1] and self.cases[0][2] == "_" and self.cases[2][0] != " ":
            return [0,2], self.cases[2][0]

        elif self.cases[1][0] == self.cases[1][1] and self.cases[1][2] == "_" and self.cases[1][0] != "_":
            return [1][2], self.cases[1][0]

        elif self.cases[1][2] == self.cases[1][1] and self.cases[1][0] == "_" and self.cases[1][2] != "_":
            return [1,0], self.cases[1][2]

        elif self.cases[2][0] == self.cases[2][1] and self.cases[2][2] == " " and self.cases[2][0] != " ":
            return [2,2], self.cases[2][0]

        elif self.cases[2][2] == self.cases[2][1] and self.cases[2][0] == " " and self.cases[2][2] != " ":
            return [2,0], self.cases[2][2]

        else:
            return -1

def Morpion(j1:Joueur,j2:Joueur):
    """
    entrée (j1,j2:joueur)
    sortie (entier : 0 si j1 gagne et 1 sil j2 gagne)
    """
    manches : int
    compteur : int
    tour : int
    board : morpion
    j1_vic : int
    j2_vic : int
    on_game : bool
    x : int
    y : int

    manches = int(input("vous voulez jouer combien de manches? "))
    j1_vic = 0
    j2_vic = 0

    for compteur in range(manches):
        board = morpion()
        board.afficher()
        print("-------------------------")
        tour = 0
        on_game = True
        if random()>0.5:
            while on_game:
                if tour % 2 == 0:
                    print("")
                    x = int(input("entrez la ligne : "))
                    y = int(input("entrez la colonne : "))
                    while ((x<0 or x>2)or(y<0 or y>2)) or (board.cases[x][y] == "X" or board.cases[x][y] == "0"):
                        x = int(input("entrez la ligne : "))
                        y = int(input("entrez la colonne : "))
                    board.marque(x,y,"X")
                    board.afficher()
                    tour += 1
                else:
                    print("")
                    x = int(input("entrez la ligne : "))
                    y = int(input("entrez la colonne : "))
                    while ((x<0 or x>2)or(y<0 or y>2)) or (board.cases[x][y] == "X" or board.cases[x][y] == "0"):
                        x = int(input("entrez la ligne : "))
                        y = int(input("entrez la colonne : "))
                    board.marque(x,y,"O")
                    board.afficher()
                    tour += 1

                if board.veri_Jeu(tour) == 0:
                    on_game = False
                elif board.veri_Jeu(tour) == "X":
                    j1_vic += 1
                    on_game = False
                elif board.veri_Jeu(tour) == "O":
                    j2_vic += 1
                    on_game = False

        else:
            while on_game:
                if tour % 2 == 0:
                    print("")
                    x = int(input("entrez la ligne : "))
                    y = int(input("entrez la colonne : "))
                    while ((x<0 or x>2)or(y<0 or y>2)) or (board.cases[x][y] == "X" or board.cases[x][y] == "0"):
                        x = int(input("entrez la ligne : "))
                        y = int(input("entrez la colonne : "))
                    board.marque(x,y,"O")
                    board.afficher()
                    tour += 1
                else:
                    print("")
                    x = int(input("entrez la ligne : "))
                    y = int(input("entrez la colonne : "))
                    while ((x<0 or x>2)or(y<0 or y>2)) or (board.cases[x][y] == "X" or board.cases[x][y] == "0"):
                        x = int(input("entrez la ligne : "))
                        y = int(input("entrez la colonne : "))
                    board.marque(x,y,"X")
                    board.afficher()
                    tour += 1

                if board.veri_Jeu(tour) == 0:
                    on_game = False
                elif board.veri_Jeu(tour) == "O":
                    j1_vic += 1
                    on_game = False
                elif board.veri_Jeu(tour) == "X":
                    j2_vic += 1
                    on_game = False
        
        if j1_vic > j2_vic:
            j1.scoreM += 1
            return 0
        else:
            j2.scoreM += 1
            return 1
        
        




if __name__ == "__main__":
    j1 : Joueur
    j2 : Joueur
    j1 = Joueur("camille")
    j2 = Joueur("lee sin")
    Morpion(j1,j2)
