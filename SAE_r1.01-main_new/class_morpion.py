from random import random
from class_joueur import Joueur

def afficher(tabl:list) :
    """
    cette méthode permet d'afficher l'objet morpion 
    """
    print("\n")
    print("----"*len(tabl[0]))
    for i in range(0,len(tabl)) :
        for j in range(0,len(tabl[0])) :
            print("|",tabl[i][j],"",sep=" ",end="")
        print("|")
        print("----"*len(tabl[0]))
    print("\n")

def marque(table,x:int,y:int,car : str):
    """
    entrée : (x,y : entiers) car 
    cette méthode permet suite à l'entrée des coordonées des cases et du Joueur qui joue d'ajouter  
    """
    table[x][y] = car

def veri_Jeu(table,tour)->int:
    """
    cette methode verifie si la partie est fini, si oui elle envoi "X" ou "O" pour le gagnant, 0 pour égalité et -1 pour le reste des cas
    """
    if tour > 9:
        return 0

    elif table[0][0] == table[1][1] and table[0][0] == table[2][2] and table[0][0] != "_" :
        return table[0][0]

    elif table[0][0] == table[1][0] and table[0][0] == table[2][0] and table[0][0] != "_" :
        return table[0][0]

    elif table[0][0] == table[0][1] and table[0][0] == table[0][2] and table[0][0] != "_" :
        return table[0][0]

    elif table[0][1] == table[1][1] and table[0][1] == table[2][1] and table[0][1] != "_" :
        return table[0][1]

    elif table[0][2] == table[1][2] and table[0][2] == table[2][2] and table[0][2] != "_" :
        return table[0][2]

    elif table[0][2] == table[1][1] and table[0][2] == table[2][1] and table[0][2] != "_" :
        return table[0][2]

    elif table[1][0] == table[1][1] and table[1][0] == table[1][2] and table[1][0] != "_" :
        return table[1][0]

    elif table[2][0] == table[2][1] and table[2][0] == table[2][2] and table[2][0] != "_" :
        return table[2][0]
    
    else:
        return -1

def veri_Pvictoire(table):
    """
    à l'entrée du morpion, la méthode renvoi un tableau si il y a possibilité de victoire ou defaite, qui contient les coordonéees de la case à jouer dans ce cas et le joueur qui peut gagner
    , autrement elle renvoi -1   
    """

    if table[0][0] == table[0][1] and table[0][2] == "_"  and table[0][0] != "_":
        return [0,2], table[0][0]

    elif table[0][2] == table[0][1] and table[0][0] == "_" and table[0][2] != "_":
        return [0,0], table[0][2]

    elif table[0][0] == table[1][0] and table[2][0] == " " and table[0][0] != "_":
        return [2,0], table[0][0]

    elif table[2][0] == table[1][0] and table[0][0] == "_" and table[2][0] != " ":
        return [0,0], table[2][0]

    elif table[2][2] == table[1][1] and table[0][0] == "_" and table[2][2] != " ":
        return [0,0], table[2][2]

    elif table[0][1] == table[1][1] and table[2][1] == " " and table[0][1] != "_":
        return [2,1], table[0][1]

    elif table[2][1] == table[1][1] and table[0][1] == "_" and table[2][1] != " ":
        return [0,1], table[2][1]

    elif table[0][2] == table[1][1] and table[2][0] == " " and table[0][2] != "_":
        return [2,0], table[0][2]

    elif table[2][0] == table[1][1] and table[0][2] == "_" and table[2][0] != " ":
        return [0,2], table[2][0]

    elif table[1][0] == table[1][1] and table[1][2] == "_" and table[1][0] != "_":
        return [1][2], table[1][0]

    elif table[1][2] == table[1][1] and table[1][0] == "_" and table[1][2] != "_":
        return [1,0], table[1][2]

    elif table[2][0] == table[2][1] and table[2][2] == " " and table[2][0] != " ":
        return [2,2], table[2][0]

    elif table[2][2] == table[2][1] and table[2][0] == " " and table[2][2] != " ":
        return [2,0], table[2][2]

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
    board : list
    j1_vic : int
    j2_vic : int
    on_game : bool
    x : int
    y : int

    manches = int(input("vous voulez jouer combien de manches 1, 3 ou 5? "))
    while manches not in [1,3,5]:
        manches = int(input("rentrez 1, 3 ou 5 : "))
    j1_vic = 0
    j2_vic = 0

    for compteur in range(manches):
        board = [[" "," "," "],
                 [" "," "," "],
                 [" "," "," "]]
        afficher(board)
        print("-------------------------")
        tour = 0
        on_game = True
        if random()>0.5:
            while on_game:
                if tour % 2 == 0:
                    print("")
                    x = int(input("entrez la ligne : "))
                    y = int(input("entrez la colonne : "))
                    while ((x<0 or x>2)or(y<0 or y>2)) or (board[x][y] == "X" or board[x][y] == "O"):
                        if (x>0 or x<2)and(y>0 or y<2):
                            print("\nentrée hors limite\n")
                        elif (board[x][y] == "X" or board[x][y] == "O"):
                            print("Case deja marqué\n")
                        x = int(input("entrez la ligne : "))
                        y = int(input("entrez la colonne : "))
                    marque(board,x,y,"X")
                    afficher(board)
                    tour += 1
                else:
                    print("")
                    x = int(input("entrez la ligne : "))
                    y = int(input("entrez la colonne : "))
                    while ((x<0 or x>2)or(y<0 or y>2)) or (board[x][y] == "X" or board[x][y] == "O"):
                        if (x>0 or x<2)and(y>0 or y<2):
                            print("\nentrée hors limite\n")
                        elif (board[x][y] == "X" or board[x][y] == "O"):
                            print("Case deja marqué\n")
                        x = int(input("entrez la ligne : "))
                        y = int(input("entrez la colonne : "))
                    marque(board,x,y,"O")
                    afficher(board)
                    tour += 1

                if veri_Jeu(board,tour) == 0:
                    on_game = False
                elif veri_Jeu(board,tour) == "X":
                    j1_vic += 1
                    on_game = False
                elif veri_Jeu(board,tour) == "O":
                    j2_vic += 1
                    on_game = False

        else:
            while on_game:
                if tour % 2 == 0:
                    print("")
                    x = int(input("entrez la ligne : "))
                    y = int(input("entrez la colonne : "))
                    while ((x<0 or x>2)or(y<0 or y>2)) or (board[x][y] == "X" or board[x][y] == "O"):
                        if (x>0 or x<2)and(y>0 or y<2):
                            print("\nentrée hors limite\n")
                        elif (board[x][y] == "X" or board[x][y] == "O"):
                            print("Case deja marqué\n")
                        x = int(input("entrez la ligne : "))
                        y = int(input("entrez la colonne : "))
                    marque(board,x,y,"O")
                    afficher(board)
                    tour += 1
                else:
                    print("")
                    x = int(input("entrez la ligne : "))
                    y = int(input("entrez la colonne : "))
                    while ((x<0 or x>2)or(y<0 or y>2)) or (board[x][y] == "X" or board[x][y] == "O"):
                        if (x>0 or x<2)and(y>0 or y<2):
                            print("\nentrée hors limite\n")
                        elif (board[x][y] == "X" or board[x][y] == "O"):
                            print("Case deja marqué\n")
                        x = int(input("entrez la ligne : "))
                        y = int(input("entrez la colonne : "))
                    marque(board,x,y,"X")
                    afficher(board)
                    tour += 1

                if veri_Jeu(board,tour) == 0:
                    on_game = False
                elif veri_Jeu(board,tour) == "O":
                    j1_vic += 1
                    on_game = False
                elif veri_Jeu(board,tour) == "X":
                    j2_vic += 1
                    on_game = False
        
        if j1_vic > j2_vic:
            j1.scoreM += 1
            print("vainqueur est ", j1.nom)
        else:
            j2.scoreM += 1
            print("vainqueur est ", j2.nom)
        
        




if __name__ == "__main__":
    j1 : Joueur
    j2 : Joueur
    j1 = Joueur()
    j2 = Joueur()
    j1.nom = "aaaa"
    j2.nom = "bbbb"
    Morpion(j1,j2)