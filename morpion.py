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

def veri_Jeu(table:list,tour:int)->str:
    """
    cette methode verifie si la partie est fini, si oui elle envoi "X" ou "O" pour le gagnant, "egal" pour égalité
    """
    if tour > 8:
        return "egal"

    elif table[0][0] == table[1][1] and table[0][0] == table[2][2] and table[0][0] != " " :
        return table[0][0]

    elif table[0][0] == table[1][0] and table[0][0] == table[2][0] and table[0][0] != " " :
        return table[0][0]

    elif table[0][0] == table[0][1] and table[0][0] == table[0][2] and table[0][0] != " " :
        return table[0][0]

    elif table[0][1] == table[1][1] and table[0][1] == table[2][1] and table[0][1] != " " :
        return table[0][1]

    elif table[0][2] == table[1][2] and table[0][2] == table[2][2] and table[0][2] != " " :
        return table[0][2]

    elif table[0][2] == table[1][1] and table[0][2] == table[2][0] and table[0][2] != " " :
        return table[0][2]

    elif table[1][0] == table[1][1] and table[1][0] == table[1][2] and table[1][0] != " " :
        return table[1][0]

    elif table[2][0] == table[2][1] and table[2][0] == table[2][2] and table[2][0] != " " :
        return table[2][0]

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
    egalite : bool
    x : int
    y : int

    manches = int(input("vous voulez jouer combien de manches 1, 3 ou 5? "))
    while manches not in [1,3,5]:
        manches = int(input("rentrez 1, 3 ou 5 : "))
    j1_vic = 0
    j2_vic = 0
    print("Pour jouer il suffit de rentrer un entier de 0 à 2 pour la ligne et la collonne ou 0 est la première ligne/colonne et 2 la dernière\n")
    for compteur in range(manches):
        egalite = False
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
                        if (x<0 or x>2)or(y<0 or y>2):
                            print("\nentrée hors limite\n")
                        elif (board[x][y] == "X" or board[x][y] == "O"):
                            print("\nCase deja marqué\n")
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
                        if (x<0 or x>2)or(y<0 or y>2):
                            print("\nentrée hors limite\n")
                        elif (board[x][y] == "X" or board[x][y] == "O"):
                            print("\nCase deja marqué\n")
                        x = int(input("entrez la ligne : "))
                        y = int(input("entrez la colonne : "))
                    marque(board,x,y,"O")
                    afficher(board)
                    tour += 1
                if veri_Jeu(board,tour) == "X":
                    j1_vic += 1
                    on_game = False
                elif veri_Jeu(board,tour) == "O":
                    j2_vic += 1
                    on_game = False
                elif veri_Jeu(board,tour) == "egal":
                    egalite = True
                    on_game = False
        else:
            while on_game:
                if tour % 2 == 0:
                    print("")
                    x = int(input("entrez la ligne : "))
                    y = int(input("entrez la colonne : "))
                    while ((x<0 or x>2)or(y<0 or y>2)) or (board[x][y] == "X" or board[x][y] == "O"):
                        if (x<0 or x>2)or(y<0 or y>2):                            
                            print("\nentrée hors limite\n")
                        elif (board[x][y] == "X" or board[x][y] == "O"):
                            print("\nCase deja marqué\n")
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
                        if (x<0 or x>2)and(y<0 or y>2):     
                            print("\nentrée hors limite\n")
                        elif (board[x][y] == "X" or board[x][y] == "O"):
                            print("\nCase deja marqué\n")
                        x = int(input("entrez la ligne : "))
                        y = int(input("entrez la colonne : "))
                    marque(board,x,y,"X")
                    afficher(board)
                    tour += 1
                if veri_Jeu(board,tour) == "O":
                    j1_vic += 1
                    on_game = False
                elif veri_Jeu(board,tour) == "X":
                    j2_vic += 1
                    on_game = False
                elif veri_Jeu(board,tour) == "egal":
                    egalite = True
                    on_game = False

        if not egalite:
            if j1_vic > j2_vic:
                j1.scoreM += 1
                j1.scoreT += 1
                print("vainqueur est ", j1.nom)
            else:
                j2.scoreM += 1
                j2.scoreT += 1
                print("vainqueur est ", j2.nom)
        else:
            print("\négalité :/\n")
        
        




if __name__ == "__main__":
    j1 : Joueur
    j2 : Joueur
    j1 = Joueur()
    j2 = Joueur()
    j1.scoreM = 0
    j2.scoreM = 0
    j1.scoreT = 0
    j2.scoreT = 0
    j1.nom = "aaaa"
    j2.nom = "bbbb"
    Morpion(j1,j2)