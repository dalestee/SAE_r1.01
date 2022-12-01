import random
def premier_joueur(nom1:str,nom2:str) -> str:
        joueur1=random.randint(0,1)
        if joueur1==1:
            joueur1=nom2
            joueur2=nom1
        elif joueur1==0:
            joueur1=nom1
            joueur2=nom2
        print("Le premier joueur est",joueur1,", le second est",joueur2)
        return joueur1,joueur2