class Board:
        def __init__(self):
            self.Table = [[" "," "," "," "," "," "," "],
                          [" "," "," "," "," "," "," "],
                          [" "," "," "," "," "," "," "],
                          [" "," "," "," "," "," "," "],
                          [" "," "," "," "," "," "," "],
                          [" "," "," "," "," "," "," "]]

        def marquer(self,x:int,tour:int):

            y:int
            y=5

            while y >= 0 and self.Table[y][x] != " ":
                y= y-1
            if y < 0:
                return -1
            elif tour % 2 == 0:
                
                self.Table[y][x] = "O"
            else:
                self.Table[y][x] = "X"


        def afficher(self):
            print("\n",
                  self.Table[0][0] ,"|" ,self.Table[0][1],"|",self.Table[0][2] ,"|" ,self.Table[0][3],"|",self.Table[0][4] ,"|" ,self.Table[0][5],"|" ,self.Table[0][6],"\n",
                  self.Table[1][0] ,"|" ,self.Table[1][1],"|",self.Table[1][2] ,"|" ,self.Table[1][3],"|",self.Table[1][4] ,"|" ,self.Table[1][5],"|" ,self.Table[1][6],"\n",
                  self.Table[2][0] ,"|" ,self.Table[2][1],"|",self.Table[2][2] ,"|" ,self.Table[2][3],"|",self.Table[2][4] ,"|" ,self.Table[2][5],"|" ,self.Table[2][6],"\n",
                  self.Table[3][0] ,"|" ,self.Table[3][1],"|",self.Table[3][2] ,"|" ,self.Table[3][3],"|",self.Table[3][4] ,"|" ,self.Table[3][5],"|" ,self.Table[3][6],"\n",
                  self.Table[4][0] ,"|" ,self.Table[4][1],"|",self.Table[4][2] ,"|" ,self.Table[4][3],"|",self.Table[4][4] ,"|" ,self.Table[4][5],"|" ,self.Table[4][6],"\n",
                  self.Table[5][0] ,"|" ,self.Table[5][1],"|",self.Table[5][2] ,"|" ,self.Table[5][3],"|",self.Table[5][4] ,"|" ,self.Table[5][5],"|" ,self.Table[5][6])

        def veri_jeu(self)->list:
            compt : int
            compt = 0
            #veri lignes horrizontales
            for i in range(len(self.Table)):
                for j in range(len(self.Table[i])):
                    if self.Table[i][j] != " " and self.Table[i][j] == self.Table[i-1][j]:
                        compt += 1
                    else:
                        compt = 0
                    if compt == 4:
                        return [1,self.Table[i][j]]

            #veri lignes verticales
            for i in range(len(self.Table[i])):
                for j in range(len(self.Table)):
                    if self.Table[j][i] != " " and self.Table[j][i] == self.Table[j][i-1]:
                        compt += 1
                    else:
                        compt = 0
                    if compt == 4:
                        return [1,self.Table[j][i]]
            #veri lignes diagonales Haut en bas
            for i in range(len(self.Table)//2):
                compt = 0
                for j in range(len(self.Table[0])//2):
                    compt2 = 3
                    for h in range(len(self.Table[0])//2):
                        if self.Table[i][compt2] != " " and self.Table[i][compt2] == self.Table[i][compt2-1]:
                            compt += 1
                        compt2 += 1
                        i += 1
                    for h in range(len(self.Table[0])//2):
                        if self.Table[j][h] != " " and self.Table[j][h] == self.Table[j][h-1]:
                            compt += 1    



            return [-1," "]

def Puissance4():
    tour : int
    Table : Board

    tour = 0
    Table = Board()
    On_game = True

    Joueur_1 = input("Nom joueur 1 : ")
    Joueur_2 = input("Nom joueur 2 : ")
    while On_game:
        if tour % 2 == 0:
            Table.marquer(int(input(Joueur_1+" joue : ")),tour)
            tour += 1
        else :
            Table.marquer(int(input(Joueur_2+" joue : ")),tour)
            tour += 1
        Table.afficher()
        print(Table.veri_jeu()[0])
        if Table.veri_jeu()[0] == 1:
            print("Le gagnant est : ",Table.veri_jeu()[1])
            On_game = False



    





    

if __name__ == "__main__":
    A = Board()
    A.marquer(0,0)
    A.marquer(1,0)
    A.marquer(2,0)
    A.marquer(3,1)

    A.afficher()
    print(A.veri_jeu())