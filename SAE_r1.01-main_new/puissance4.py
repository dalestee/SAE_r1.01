from random import random
from class_joueur import Joueur

def marquer(table:list,x:int,tour:int):
    """_summary_

    Args:
        table (list): la table de puissance 4
        x (int): coordonée ou l'on marque
        tour (int): quel est le tour que l'on joue

    Returns:
        int : 
    """

    y:int
    y=5

    if table[0][x] != " ":
        return 0
    else:
        while y >= 0 and table[y][x] != " ":
            y= y-1
        if y < 0:
            return -1
        elif tour % 2 == 0:
            
            table[y][x] = "O"
        else:
            table[y][x] = "X"


def afficher(tabl):
    print("\n")
    print("----"*len(tabl[0]))
    for i in range(0,len(tabl)) :
        for j in range(0,len(tabl[0])) :
            print("|",tabl[i][j],"",sep=" ",end="")
        print("|")
        print("----"*len(tabl[0]))
    print("\n")

def veri_jeu(table,tour)->list:
    """
    Cette foncion vérifie si le jeu est deja fini et renvoi le vainqueur
    rentrée : (table:list,tour:int)
    renvoie : (list[0=égalité,1=victoire,-1=rien;str: "X","O"," " qui correspond au vainquer])
    """
    compt : int
    compt2 : int
    compt = 0
    #regarde si le tour est égal 42 qui est la limite
    if tour >= 42: return [0," "]
    #veri lignes horrizontales
    for i in range(len(table)):
        compt = 0
        for j in range(len(table[i])):
            if table[i][j] != " " and table[i][j] == "X":
                compt += 1
            else:
                compt = 0
            if compt == 4:
                return [1,"X"]

    for i in range(len(table)):
        compt = 0
        for j in range(len(table[i])):
            if table[i][j] != " " and table[i][j] == "O":
                compt += 1
            else:
                compt = 0
            if compt == 4:
                return [1,"O"]

    #veri lignes verticales
    for i in range(len(table[i])):
        compt = 0
        for j in range(len(table)):
            if table[j][i] != " " and table[j][i] == "X":
                compt += 1
            else:
                compt = 0
            if compt == 4:
                return [1,"X"]
    
    for i in range(len(table[0])):
        compt = 0
        for j in range(len(table)):
            if table[j][i] != " " and table[j][i] == "O":
                compt += 1
            else:
                compt = 0
            if compt == 4:
                return [1,"O"]
    #veri lignes diagonales Haut en bas
    compt2 = 0
    compt = 0
    for i in range((len(table)//2)+1):
        compt2 = 3
        compt = 0
        for h in range(len(table)//2):        
            compt2 = 3
            compt = 0
            for j in range((len(table[0])//2)+1):
                if table[j+h][compt2] != " " and table[j+h][compt2] == "O":
                    compt += 1
                else:
                    compt = 0
                if compt == 4:
                    return [1,"O"]
                compt2 += 1
        for i in range(len(table)//2):
            compt2 = 3
            compt = 0
            for j in range((len(table[0])//2)+1):
                if table[j+i][compt2] != " " and table[j+i][compt2] == "O":
                    compt += 1
                else:
                    compt = 0
                if compt == 4:
                    return [1,"O"]
                compt2 -= 1

    compt2 = 0
    compt = 0
    for i in range((len(table)//2)+1):
        compt2 = 3
        compt = 0
        for h in range(len(table)//2):        
            compt2 = 3
            compt = 0
            for j in range((len(table[0])//2)+1):
                if table[j+h][compt2] != " " and table[j+h][compt2] == "X":
                    compt += 1
                else:
                    compt = 0
                if compt == 4:
                    return [1,"X"]
                compt2 += 1
        for i in range(len(table)//2):
            compt2 = 3
            compt = 0
            for j in range((len(table[0])//2)+1):
                if table[j+i][compt2] != " " and table[j+i][compt2] == "X":
                    compt += 1
                else:
                    compt = 0
                if compt == 4:
                    return [1,"X"]
                compt2 -= 1

    #veri lignes diagonales bas haut
    compt2 = 0
    compt = 0
    for i in range((len(table)//2)+1):
        compt2 = 3
        compt = 0
        for h in range(len(table)//2):
            compt2 = 3
            compt = 0
            for j in range(len(table)-1,(len(table[0])//2)-2,-1):
                if table[j-h][compt2] != " " and table[j-h][compt2] == "O":
                    compt += 1
                else:
                    compt = 0
                if compt == 4:
                    return [1,"O"]
                compt2 += 1
        for i in range(len(table)//2):
            compt2 = 3
            compt = 0
            for j in range(len(table)-1,(len(table[0])//2)-2,-1):
                if table[j-i][compt2] != " " and table[j-i][compt2] == "O":
                    compt += 1
                else:
                    compt = 0
                if compt == 4:
                    return [1,"O"]
                compt2 -= 1

    compt2 = 0
    compt = 0
    for i in range((len(table)//2)+1):
        compt2 = 3
        compt = 0
        for h in range(len(table)//2):
            compt2 = 3
            compt = 0
            for j in range(len(table)-1,(len(table[0])//2)-2,-1):
                if table[j-h][compt2] != " " and table[j-h][compt2] == "X":
                    compt += 1
                else:
                    compt = 0
                if compt == 4:
                    return [1,"X"]
                compt2 += 1
        for i in range(len(table)//2):
            compt2 = 3
            compt = 0
            for j in range(len(table)-1,(len(table[0])//2)-2,-1):
                if table[j-i][compt2] != " " and table[j-i][compt2] == "X":
                    compt += 1
                else:
                    compt = 0
                if compt == 4:
                    return [1,"X"]
                compt2 -= 1

    #traitement des derniers cas [0][1],[0][2]|[1][1],[1][2]/[0][5],[0][4]|[1][5],[1][4]/[5][5],[4][5]|[4][5],[4][4]/[5][1],[5][2]|[4][1],[4][2]
    #[0][1],[0][2]|[1][1],[1][2]
    for h in range(2):
        compt2 = 1
        compt = 0
        for j in range(2):
            compt2 = 1
            compt = 0
            for i in range(4):
                if table[j+i][compt2+h] == "O" and table[j+i][compt2+h] != " ":
                    compt += 1
                else:
                    compt = 0
                
                if compt == 4:
                    return [1,"O"]
                compt2 += 1
    
    for h in range(2):
        compt2 = 1
        compt = 0
        for j in range(2):
            compt2 = 1
            compt = 0
            for i in range(4):
                if table[j+i][compt2+h] == "X" and table[j+i][compt2+h] != " ":
                    compt += 1
                else:
                    compt = 0
                
                if compt == 4:
                    return [1,"X"]
                compt2 += 1
    #[0][5],[0][4]|[1][5],[1][4]            
    for h in range(2):
        compt2 = 5
        compt = 0
        for j in range(2):
            compt2 = 5
            compt = 0
            for i in range(4):
                if table[j+i][compt2-h] == "O" and table[j+i][compt2-h] != " ":
                    compt += 1
                else:
                    compt = 0
                
                if compt == 4:
                    return [1,"O"]
                compt2 -= 1

    for h in range(2):
        compt2 = 5
        compt = 0
        for j in range(2):
            compt2 = 5
            compt = 0
            for i in range(4):
                if table[j+i][compt2-h] == "X" and table[j+i][compt2-h] != " ":
                    compt += 1
                else:
                    compt = 0
                
                if compt == 4:
                    return [1,"X"]
                compt2 -= 1
    #[5][5],[4][5]|[4][5],[4][4]
    for h in range(2):
        compt2 = 5
        compt = 0
        for j in range(2):
            compt2 = 5
            compt = 0
            for i in range(5,-1,-1):
                if table[i-j][compt2-h] == "O" and table[i-j][compt2-h] != " ":
                    compt += 1
                else:
                    compt = 0
                
                if compt == 4:
                    return [1,"O"]
                compt2 -= 1

    for h in range(2):
        compt2 = 5
        compt = 0
        for j in range(2):
            compt2 = 5
            compt = 0
            for i in range(5,-1,-1):
                if table[i-j][compt2-h] == "X" and table[i-j][compt2-h] != " ":
                    compt += 1
                else:
                    compt = 0
                
                if compt == 4:
                    return [1,"X"]
                compt2 -= 1
    #[5][1],[5][2]|[4][1],[4][2]
    for h in range(2):
        compt2 = 1
        compt = 0
        for j in range(2):
            compt2 = 1
            compt = 0
            for i in range(5,1,-1):
                if table[i-j][compt2+h] == "O" and table[i-j][compt2+h] != " ":
                    compt += 1
                else:
                    compt = 0
                
                if compt == 4:
                    return [1,"O"]
                compt2 += 1

    for h in range(2):
        compt2 = 1
        compt = 0
        for j in range(2):
            compt2 = 1
            compt = 0
            for i in range(5,1,-1):
                if table[i-j][compt2+h] == "X" and table[i-j][compt2+h] != " ":
                    compt += 1
                else:
                    compt = 0
                
                if compt == 4:
                    return [1,"X"]
                compt2 += 1
    
    return [-1," "]

def Puissance4(j1:Joueur,j2:Joueur):
    tour : int
    table : list
    j1_vic : int
    j2_vic : int
    manches : int

    table = [[" " for i in range(7)] for i in range(6)]

    tour = 0
    manches = int(input("vous voulez jouer 1,3 ou 5 manches? "))
    print("")
    while str(manches) not in "135":
        manches = int(input("vous voulez jouer 1,3 ou 5 manches? "))
        print('')
    j1_vic = 0
    j2_vic = 0

    for compteur in range(manches):
        On_game = True
        table = [[" " for i in range(7)] for i in range(6)]
        if random()>0.5:
            afficher(table)
            while On_game:
                if tour % 2 == 0:
                    marquer(table,int(input(j1.nom+" joue : ")),tour)
                    tour += 1
                else :
                    marquer(table,int(input(j2.nom+" joue : ")),tour)
                    tour += 1
                afficher(table)
                if veri_jeu(table,tour)[0] == 0:
                    print("il y a égalité :( ")
                    On_game = False
                if veri_jeu(table,tour)[0] == 1:
                    On_game = False
                    if veri_jeu(table,tour)[1] == "O":
                        j1_vic += 1
                    else:
                        j2_vic += 1
        
        else:
            afficher(table)
            while On_game:
                if tour % 2 == 0:
                    marquer(table,int(input(j2.nom+" joue : ")),tour)
                    tour += 1
                else :
                    marquer(table,int(input(j1.nom+" joue : ")),tour)
                    tour += 1
                afficher(table)
                if veri_jeu(table,tour)[0] == 0:
                    print("il y a égalité :( ")
                    On_game = False
                if veri_jeu(table,tour)[0] == 1:
                    On_game = False
                    if veri_jeu(table,tour)[1] == "O":
                        j1_vic += 1
                    else:
                        j2_vic += 1

    if j1_vic>j2_vic:
        j1.scoreP += 1
        print("vainqueur est ", j1.nom)
        j1.scoreP += 1
    else:
        j2.scoreP += 1
        print("vainqueur est ", j2.nom)
        j2.scoreP += 1
    
        
if __name__ == "__main__":
    j1 : Joueur
    j2 : Joueur
    j1 = Joueur()
    j2 = Joueur()
    j1.nom = "Camille"
    j2.nom = "Lee sin"
    Puissance4(j1,j2)


