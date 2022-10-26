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

    





    

if __name__ == "__main__":
    Puissance4()