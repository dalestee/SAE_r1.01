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

    def marque(self,x,y,Tour):
        """
        entrée : (x,y,Tour : entiers)
        cette méthode permet suite à l'entrée des coordonées des cases et du Joueur qui joue d'ajouter  
        """
        if Tour % 2 == 0:
            self.cases[x][y] = "X"
        else:
            self.cases[x][y] = "O"

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





if __name__ == "__main__":
    M : morpion 

    M = morpion()
    M.afficher()
    M.marque(0,0,0)
    M.afficher()
