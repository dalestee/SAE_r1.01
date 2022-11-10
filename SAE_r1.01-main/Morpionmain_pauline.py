import random

def creation_grille(x:int,y:int,char_empt:str) -> list :
	tabl = [[char_empt for i in range(0,x)] for i in range(0,y)]
	return tabl
	
def aff(tabl:list) :
    print("\n")
    print("----"*len(tabl[0]))
    for i in range(0,len(tabl)) :
        for j in range(0,len(tabl[0])) :
            print("|",tabl[i][j],"",sep=" ",end="")
        print("|")
        print("----"*len(tabl[0]))
    print("\n")


def choix_nom() -> str :
    char_empt:str
    nom_j1:str
    nom_j2:str

    char_empt = " "
    nom_j1 = input("Quel est le nom du joueur 1 ? ")
    nom_j2 = input("Quel est le nom du joueur 2 ? ")
    return char_empt,nom_j1,nom_j2

def premier_joueur(nom1:str,nom2:str) -> str:
    joueur1=random.randint(0,1)
    if joueur1==1:
        joueur1=nom2
        joueur2=nom1
    elif joueur1==0:
        joueur1=nom1
        joueur2=nom2
    return joueur1,joueur2

def choix_char(nom1:str,nom2:str) -> str:
    print(nom1,"vous jouez en premier. Vous pouvez décider votre caractère, entre X et O.")
    char_joueur1=input("Entrez le caractère de votre choix : ")
    while char_joueur1!='X' and char_joueur1!='O':
        print("Vous n'avez pas entré une valeur valide pour pouvoir jouer.")
        char_joueur1=input("Veuillez entrer un caractère valide de votre choix : ")
    if char_joueur1=='X':
        char_joueur2='O'
    elif char_joueur1=='O':
        char_joueur2='X'
    return char_joueur1,char_joueur2

def jeu(nom1:str,nom2:str) -> str:
    char_empt=' '
    joueur1,joueur2=premier_joueur(nom1,nom2)
    char_j1,char_j2=choix_char(joueur1,joueur2)
    tabl = creation_grille(3,3,char_empt)
    compteur_tour=1
    compteur_joueur=0
    gagnant=None
    for i in range(0,9):
        if compteur_joueur==0:
            print("Tour n°",compteur_tour,", c'est à",joueur1,"de jouer.")
            print("Vous devez entrer 0, 1 ou 2 pour choisir la ligne et la colonne du tableau.")
            x=int(input("Entrez x :"))
            y=int(input("Entrez y :"))
            while (x<0 or x>2) and (y<0 or y>2):
                print("Dépassement de capacité du tableu, veuillez entrer d'autres valeurs.")
                x=int(input("Entrez x :"))
                y=int(input("Entrez y :"))
            while tabl[x][y]!=char_empt:
                print("Une valeur est déjà présente, veuillez choisir une autre position.")
                x=int(input("Entrez x :"))
                y=int(input("Entrez y :"))
                while (x<0 or x>2) and (y<0 or y>2):
                    print("Dépassement de capacité du tableu, veuillez entrer d'autres valeurs.")
                    x=int(input("Entrez x :"))
                    y=int(input("Entrez y :"))
            tabl[x][y]=char_j1
            print(aff(tabl))
            compteur_joueur+=1
            compteur_tour+=1
            if tabl[0][0]==char_j1 and tabl[1][1]==char_j1 and tabl[2][2]==char_j1:
                gagnant=joueur1
                return gagnant
            elif tabl[0][2]==char_j1 and tabl[1][1]==char_j1 and tabl[2][0]==char_j1:
                gagnant=joueur1
                return gagnant
            elif tabl[0][0]==char_j1 and tabl[0][1]==char_j1 and tabl[0][2]==char_j1:
                gagnant=joueur1
                return gagnant
            elif tabl[1][0]==char_j1 and tabl[1][1]==char_j1 and tabl[1][2]==char_j1:
                gagnant=joueur1
                return gagnant
            elif tabl[2][0]==char_j1 and tabl[2][1]==char_j1 and tabl[2][2]==char_j1:
                gagnant=joueur1
                return gagnant
            elif tabl[0][0]==char_j1 and tabl[1][0]==char_j1 and tabl[2][0]==char_j1:
                gagnant=joueur1
                return gagnant
            elif tabl[0][1]==char_j1 and tabl[1][1]==char_j1 and tabl[2][1]==char_j1:
                gagnant=joueur1
                return gagnant
            elif tabl[0][2]==char_j1 and tabl[1][2]==char_j1 and tabl[2][2]==char_j1:
                gagnant=joueur1
                return gagnant
            else:
                pass
        elif compteur_joueur==1:
            print("Tour n°",compteur_tour,", c'est à",joueur2,"de jouer.")
            print("Vous devez entrer 0, 1 ou 2 pour choisir la ligne et la colonne du tableau.")
            x=int(input("Entrez x :"))
            y=int(input("Entrez y :"))
            while (x<0 or x>2) and (y<0 or y>2):
                print("Dépassement de capacité du tableu, veuillez entrer d'autres valeurs.")
                x=int(input("Entrez x :"))
                y=int(input("Entrez y :"))
            while tabl[x][y]!=char_empt:
                print("Une valeur est déjà présente, veuillez choisir une autre position.")
                x=int(input("Entrez x :"))
                y=int(input("Entrez y :"))
                while (x<0 or x>2) and (y<0 or y>2):
                    print("Dépassement de capacité du tableu, veuillez entrer d'autres valeurs.")
                    x=int(input("Entrez x :"))
                    y=int(input("Entrez y :"))
            tabl[x][y]=char_j2
            print(aff(tabl))
            compteur_joueur-=1
            compteur_tour+=1
            if tabl[0][0]==char_j2 and tabl[1][1]==char_j2 and tabl[2][2]==char_j2:
                gagnant=joueur2
                return gagnant
            elif tabl[0][2]==char_j2 and tabl[1][1]==char_j2 and tabl[2][0]==char_j2:
                gagnant=joueur2
                return gagnant
            elif tabl[0][0]==char_j2 and tabl[0][1]==char_j2 and tabl[0][2]==char_j2:
                gagnant=joueur2
                return gagnant
            elif tabl[1][0]==char_j2 and tabl[1][1]==char_j2 and tabl[1][2]==char_j2:
                gagnant=joueur2
                return gagnant
            elif tabl[2][0]==char_j2 and tabl[2][1]==char_j2 and tabl[2][2]==char_j2:
                gagnant=joueur2
                return gagnant
            elif tabl[0][0]==char_j2 and tabl[1][0]==char_j2 and tabl[2][0]==char_j2:
                gagnant=joueur2
                return gagnant
            elif tabl[0][1]==char_j2 and tabl[1][1]==char_j2 and tabl[2][1]==char_j2:
                gagnant=joueur2
                return gagnant
            elif tabl[0][2]==char_j2 and tabl[1][2]==char_j2 and tabl[2][2]==char_j2:
                gagnant=joueur2
                return gagnant
            else:
                pass
    if gagnant==None:
        gagnant="égalité"
        return gagnant


#------------ Programme principal -------------
char_empt,nom_j1,nom_j2 = choix_nom()
tabl = creation_grille(3,3,char_empt)
resultat=jeu(nom_j1,nom_j2)
if resultat=="égalité":
    print("Egalité, il n'y a pas de vainqueur.")
else:
    print("Félicitatons à",resultat,", vous avez gagner!")
