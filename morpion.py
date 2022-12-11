from random import random,randint
from class_joueur import Joueur

def afficher(tabl:list[list[str]]) :
    """
    cette procédure permet d'afficher l'objet morpion 
    """
    print("\n")
    print("----"*len(tabl[0]))
    for i in range(0,len(tabl)) :
        for j in range(0,len(tabl[0])) :
            print("|",tabl[i][j],"",sep=" ",end="")
        print("|")
        print("----"*len(tabl[0]))
    print("\n")

def veri_CaseMarque(table : list[list[str]],x : int,y : int)->bool:
    """
    cette fonction renvoi un booléen, si la case est marqué True, sinon False
    Args:
        table (list[list[str]])
        x (int)
        y (int)

    Returns:
        bool
    """
    if table[x][y] == "X" or table[x][y] == "O":
        return True
    else:
        return False

def ensemble_caseVide(table : list[list[str]])->list[list[str]]:
    """
    Fonction qui renvoi l'ensemble des cases non marqués dans une liste suite à l'entrée du board
    Args:
        table (list[list[str]])

    Returns:
        list[list[str]]
    """
    ensemble : list
    ensemble = []
    for ligne in range(len(table)):
        for colonne in range(len(table)):
            if table[ligne][colonne] != "X" and table[ligne][colonne] != "O":
                ensemble.append([ligne,colonne])
    return ensemble
def marque(table,x:int,y:int,car : str):
    """
    entrée : (x,y : entiers) car 
    cette procédure permet suite à l'entrée des coordonées des cases et du Joueur qui joue d'ajouter
    """
    table[x][y] = car

def veri_Pvictoire(board : list[list])->str:
    """
    fonction qui vérifie si il y a une possibilité de victoire, c'est à dire deux symboles égaux alignés, et renvoi une tableau contenant 
    le symbole qui à possibilité de victoire et la position ou il faut jouer

    Args:
        board (list[list])

    Returns:
        list
    """
    casesVides = ensemble_caseVide(board)
    for case in range(len(casesVides)):
        if casesVides[case][0] == 0 and casesVides[case][1] == 0:
            if board[0][1] == board[0][2] and (board[0][1] == "X" or board[0][1] == "O"):
                return [board[0][1],casesVides[case]]
            elif board[1][0] == board[2][0] and (board[1][0] == "X" or board[1][0] == "O"):
                return [board[1][0],casesVides[case]]
            elif board[1][1] == board[2][2] and (board[1][1] == "X" or board[1][1] == "O"):
                return [board[1][1],casesVides[case]]
        elif casesVides[case][0] == 1 and casesVides[case][1] == 0:
            if board[0][0] == board[2][0] and (board[0][0] == "X" or board[0][0] == "O"):
                return [board[0][0],casesVides[case]]
            elif board[1][1] == board[1][2] and (board[1][1] == "X" or board[1][1] == "O"):
                return [board[1][1],casesVides[case]]
        elif casesVides[case][0] == 2 and casesVides[case][1] == 0:
            if board[2][1] == board[2][2] and (board[2][1] == "X" or board[2][1] == "O"):
                return [board[2][1],casesVides[case]]
            elif board[0][0] == board[1][0] and (board[0][0] == "X" or board[0][0] == "O"):
                return [board[0][0],casesVides[case]]
            elif board[1][1] == board[0][2] and (board[1][1] == "X" or board[1][1] == "O"):
                return [board[1][1],casesVides[case]]
        elif casesVides[case][0] == 0 and casesVides[case][1] == 1:
            if board[0][0] == board[0][2] and (board[0][0] == "X" or board[0][0] == "O"):
                return [board[0][0],casesVides[case]]
            elif board[1][1] == board[2][1] and (board[1][1] == "X" or board[1][1] == "O"):
                return [board[1][1],casesVides[case]]
        elif casesVides[case][0] == 1 and casesVides[case][1] == 1:
            if board[1][0] == board[1][2] and (board[1][0] == "X" or board[1][0] == "O"):
                return [board[1][0],casesVides[case]]
            elif board[0][0] == board[2][2] and (board[0][0] == "X" or board[0][0] == "O"):
                return [board[0][0],casesVides[case]]
            elif board[0][2] == board[2][0] and (board[0][2] == "X" or board[0][2] == "O"):
                return [board[0][2],casesVides[case]]
            elif board[0][1] == board[2][1] and (board[0][1] == "X" or board[0][1] == "O"):
                return [board[0][1],casesVides[case]]   
        elif casesVides[case][0] == 2 and casesVides[case][1] == 1:
            if board[2][0] == board[2][2] and (board[2][0] == "X" or board[2][0] == "O"):
                return [board[2][0],casesVides[case]]
            elif board[1][0] == board[1][1] and (board[1][0] == "X" or board[1][0] == "O"):
                return [board[0][1],casesVides[case]]
        elif casesVides[case][0] == 0 and casesVides[case][1] == 2:
            if board[1][1] == board[2][0] and (board[1][1] == "X" or board[1][1] == "O"):
                return [board[1][1],casesVides[case]]
            elif board[0][0] == board[0][1] and (board[0][0] == "X" or board[0][0] == "O"):
                return [board[0][0],casesVides[case]]
            elif board[1][2] == board[2][2] and (board[1][2] == "X" or board[1][2] == "O"):
                return [board[1][2],casesVides[case]]
        elif casesVides[case][0] == 1 and casesVides[case][1] == 2:
            if board[0][2] == board[2][2] and (board[0][2] == "X" or board[0][2] == "O"):
                return [board[0][2],casesVides[case]]
            elif board[1][0] == board[1][1] and (board[1][0] == "X" or board[1][0] == "O"):
                return [board[0][1],casesVides[case]]
        elif casesVides[case][0] == 2 and casesVides[case][1] == 2:
            if board[0][0] == board[1][1] and (board[0][0] == "X" or board[0][0] == "O"):
                return [board[0][0],casesVides[case]]
            elif board[2][0] == board[2][1] and (board[2][0] == "X" or board[2][0] == "O"):
                return [board[2][0],casesVides[case]]
            elif board[0][2] == board[1][2] and (board[0][2] == "X" or board[0][2] == "O"):
                return [board[0][2],casesVides[case]]
    return ["None",casesVides[case]," "]

def veri_Jeu(table:list,tour:int)->str:
    """
    Cette fonction verifie si il y a victoire ou égalité, en cas de égalité la fonction renvoi "egal" en cas de vicoire elle renvoi le symbole du vainqueur "O" ou "X"
    Args:
        table (list)
        tour (int)

    Returns:
        str
    """

    if table[0][0] == table[1][1] and table[0][0] == table[2][2] and table[0][0] != " " :
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
    elif tour > 8:
        return "egal"

def matche(j1:Joueur,j2:Joueur)->Joueur:
    """
    Procédure qui renvoi le joueur vainqueur ou un joueur de nom '0' si il y a égalité
    Args:
        j1 (Joueur):
        j2 (Joueur):
        j1_vic (int):
        j2_vic (int):

    Returns:
        Joueur:
    """
    winner : Joueur
    x : int
    y : int
    tour : int
    p_vic : list
    ensemble : list
    nombre_Aleatoire : int
    winner = Joueur()
    winner.nom = "0"
    tour = 0
    board : list[list[str]]
    board = [[" "," "," "],
             [" "," "," "],
             [" "," "," "]]
    while True:
                if tour % 2 == 0:
                    print("")
                    print("tour de ",j1.nom)
                    print("")
                    if j1.botSimple: #vérifie si le joueur est un bot simple
                        x = randint(0,2)
                        y = randint(0,2)
                        while board[x][y] == "X" or board[x][y] == "O":
                            x = randint(0,2)
                            y = randint(0,2)
                        marque(board,x,y,"X")
                        afficher(board)
                        tour += 1
                    elif j1.botComplex: #vérifie si le joueur est un bot complexe
                        if tour == 0:
                            marque(board,0,0,"X")
                            afficher(board)
                            tour += 1
                        elif tour == 2:
                            if board[1][0] == "O" or board[2][0] == "O":
                                marque(board,0,2,"X")
                                afficher(board)
                                tour += 1
                            else:
                                marque(board,2,0,"X")
                                afficher(board)
                                tour += 1
                        elif tour == 4:
                            p_vic = veri_Pvictoire(board)
                            print(p_vic)
                            if p_vic[0] == "X":
                                marque(board,p_vic[1][0],p_vic[1][1],"X")
                                afficher(board)
                                tour += 1
                            elif board[1][1] == " ":
                                marque(board,1,1,"X")
                                afficher(board)
                                tour += 1
                        elif tour == 6:
                            p_vic = veri_Pvictoire(board)
                            if p_vic[0] == "X":
                                marque(board,p_vic[1][0],p_vic[1][1],"X")
                                afficher(board)
                                tour += 1
                            else:
                                ensemble = ensemble_caseVide(board)
                                nombre_Aleatoire = randint(0,len(ensemble)-1)
                                marque(board,ensemble[nombre_Aleatoire][0],ensemble[nombre_Aleatoire][1],"X")
                                afficher(board)
                                tour += 1
                        elif tour == 8:
                            ensemble = ensemble_caseVide(board)
                            print(ensemble)
                            marque(board,ensemble[0][0],ensemble[0][1],"X")
                            afficher(board)
                            tour += 1
                    else:
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
                    print("tour de ",j2.nom)
                    print("")
                    if j2.botSimple: #vérifie si le joueur est un bot simple
                        x = randint(0,2)
                        y = randint(0,2)
                        while board[x][y] == "X" or board[x][y] == "O":
                            x = randint(0,2)
                            y = randint(0,2)
                        marque(board,x,y,"O")
                        afficher(board)
                        tour += 1
                    elif j2.botComplex: #vérifie si le joueur est un bot complexe
                        if tour == 1:
                            marque(board,1,1,"O")
                        elif tour == 3:
                            pass
                    else:
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
                    return j1
                elif veri_Jeu(board,tour) == "O":
                    return j2
                elif veri_Jeu(board,tour) == "egal":
                    return winner
def Morpion(j1:Joueur,j2:Joueur):
    """
    entrée (j1,j2:joueur)
    sortie (entier : 0 si j1 gagne et 1 sil j2 gagne)
    """
    manches : int
    winner : Joueur
    compteur : int
    j1_vic : int
    j2_vic : int
    egalite : bool
    x : int
    y : int

    manches = int(input("vous voulez jouer combien de manches 1, 3 ou 5? "))
    while manches not in [1,3,5]:
        manches = int(input("rentrez 1, 3 ou 5 : "))
    j1_vic = 0
    j2_vic = 0
    winner = Joueur()
    winner.nom = "-1"
    print("Pour jouer il suffit de rentrer un entier de 0 à 2 pour la ligne et la collonne ou 0 est la première ligne/colonne et 2 la dernière\n")
    for compteur in range(manches):
        if random()>0.5:
            winner = matche(j1,j2)
        else:
            winner = matche(j2,j1)
        
        print(winner.nom,j1.nom)
        if winner.nom == "0":
            print("\négalité :/\n")
        elif winner.nom == j1.nom:
            j1_vic += 1 
            print("vainqueur de la manche est ", j1.nom)
        else:
            j2_vic += 1
            print("vainqueur de la manche est ", j2.nom)
    print(j1_vic,j2_vic,"--------------")

        
    if j1_vic == j2_vic:
        print("il y a eu égalité")
    elif j1_vic>j2_vic:
        j1.scoreM += 1
        j1.scoreT += 1
        print(j1.nom," à gagné!!")
    else:
        j2.scoreM += 1
        j2.scoreT += 1
        print(j2.nom," à gagné!!")
if __name__ == "__main__":
    j1 : Joueur
    j2 : Joueur
    j1 = Joueur()
    j2 = Joueur()
    j1.scoreM = 0
    j2.scoreM = 0
    j1.scoreT = 0
    j2.scoreT = 0
    j1.botSimple = False
    j2.botSimple = False
    j1.botComplex = True
    j2.botComplex = False
    j1.nom = "bot"
    j2.nom = "j2"
    Morpion(j1,j2)
    print("scoreM j1 : ",j1.scoreM,"scoreT j1 : ",j1.scoreT)
    print("\nscoreM j2 : ",j2.scoreM,"scoreT j2 : ",j2.scoreT)
    board = [["X"," "," "],
             ["O"," "," "],
             ["X"," ","O"]]
    #print(veri_Pvictoire(board))
        
