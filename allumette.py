from premier_joueur import premier_joueur
from class_joeueur import Joueur
def allumette(joueur1:Joueur,joueur2:Joueur):
    """
    Fonction: jeu des allumettes, qui affiche les règles et gère tour par tour les entrés des joueurs, celui retirant la dernière est perdant.

    Entré: les deux joueurs participants, de type classe Joueur.

    Sortie: aucune sortie n'est effectué, la fonction changera le score des joueurs en fonction du résultat du jeu.
    """
    allumette:str
    valeur_init:int
    affichage:str
    compteur_joueur:int
    compteur_tour:int
    condition:int
    print("")
    print("Vous avez choisi le jeu des allumettes. \n")
    print("----------------------------------------------------------- RÈGLES ------------------------------------------------------------")
    print("|                                                                                                                             |")
    print("| - Le perdant de ce jeu est celui qui retirera la dernière allumette                                                         |")
    print("| - Automatiquement, l'autre joueur sera le vainqueur                                                                         |")
    print("| - Il y a vingt allumettes au début du jeu                                                                                   |")
    print("| - À tour de rôle, les joueurs devront enlevé une, deux ou trois allumettes                                                  |")
    print("| - Il ne peut pas y avoir égalité, le jeu aura forcément un vainqueur                                                        |")
    print("| - Pour plus d'équité, le joueur qui commencera sera déterminé au hasard.                                                    |")
    print("|                                                                                                                             |")
    print("| Bon jeu!                                                                                                                    |")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("")
    allumette='|'   # la variable qu'on affichera n fois
    valeur_init=20
    condition=0
    affichage=allumette*valeur_init # cette variable affichera 20 fois '|'
    compteur_joueur=0   # On utilise un compteur pour savoir quel joueur jouera, ce qui permettre d'avoir un affichage différent pour chuaque joueur
    compteur_tour=1 # variable qui sert simplement à afficher le nombre de tour (uniquement esthétique)
    print("Il y a 20 allumettes :",affichage,", vous pouvez enlever 1, 2 ou 3 allumettes.")
    print("Le joueur qui retirera la dernière allumette sera le perdant du jeu.")
    while affichage!=allumette: # Le jeu se répète tant que l'affichage des allumettes n'est pas égal à '|'
        if compteur_joueur==0: # Quand le compteur joueur est 0 c'est au joueur 1 de jouer
            if valeur_init==0 or valeur_init<0: # Si le nombre d'allumettes est de 0 ou inférieur, c'est donc le joueur qui doit jouer qui a gagner
                joueur1.scoreA += 1     # On ajoute 1 au score allumette
                joueur1.scoreT += 1     # On ajoute 1 au score total
                condition=1 # On rajoute 1 à une condition pour ne rien faire si un joueur a déjà gagner
                affichage=allumette    # Pour sortir de la boucle, on doit valide la condition de sortie
                print("Bravo, le vainqueur de ce jeu est ",joueur1.nom, "!")    # Message pour informer les joueurs du vainqueur
            else:
                print("")
                print("- Tour n°",compteur_tour,"--------------------------------------")   # Affiche le nombre de tour
                print("C'est au tour de ",joueur1.nom)  # Affiche le nom du joueur qui doit jouer
                print("Il y a ",valeur_init,"allumettes :",affichage)   # Affiche le nombre d'allumette restant
                soustraction=int(input("Veuillez choisir entre 1, 2 et 3 :"))   # Prend en entré le nombre choisie
                while soustraction!=1 and soustraction!=2 and soustraction!=3:  # On a besoin de vérifié que le résultat est bien 1, 2 ou 3, répète tant que ce n'est pas le cas
                    print("Vous n'avez pas entré une valeur valide.")
                    soustraction=int(input("Veuillez choisir entre 1, 2 et 3 :"))
                valeur_init=valeur_init-soustraction    # On soustrait
                affichage=allumette*(valeur_init)   # On change l'affichage
                compteur_joueur+=1  # On ajoute 1 au compteur joueur pour changer l'affichage
                compteur_tour+=1    # On ajoute 1 au compteur tour
        elif compteur_joueur==1:    # C'est au joueur 2 de joueur
            if valeur_init==0 or valeur_init<0:     # Si le nombre d'allumettes est de 0 ou inférieur, c'est donc le joueur qui doit jouer qui a gagner
                joueur2.scoreA += 1     # On ajoute 1 au score allumette
                joueur2.scoreT += 1     # On ajoute 1 au score total
                condition=1     # On rajoute 1 à une condition pour ne rien faire si un joueur a déjà gagner
                affichage=allumette     # Pour sortir de la boucle, on doit valide la condition de sortie
                print("Bravo, le vainqueur de ce jeu est ",joueur2.nom, "!")    # Message pour informer les joueurs du vainqueur  
            else:
                print("")
                print("- Tour n°",compteur_tour,"--------------------------------------")   # Affiche le nombre de tour
                print("C'est au tour de ",joueur2.nom)  # Affiche le nom du joueur qui doit jouer
                print("Il y a ",valeur_init,"allumettes :",affichage)   # Affiche le nombre d'allumette restant
                soustraction=int(input("Veuillez choisir entre 1, 2 et 3 :"))   # Prend en entré le nombre choisie
                while soustraction!=1 and soustraction!=2 and soustraction!=3:  # On a besoin de vérifié que le résultat est bien 1, 2 ou 3, répète tant que ce n'est pas le cas
                    print("Vous n'avez pas entré une valeur valide.")
                    soustraction=int(input("Veuillez choisir entre 1, 2 et 3 :"))
                valeur_init=valeur_init-soustraction    # On soustrait
                affichage=allumette*(valeur_init)   # On change l'affichage
                compteur_joueur-=1  # On enlève 1 au compteur joueur pour que ça soit au joueur 1 de jouer
                compteur_tour+=1    # On ajoute 1 au compteur tour
    if condition==1:  # Si un des deux joueurs a déjà gagné, le programme ne fait rien
        pass
    else:
        if compteur_joueur==0:  # Si le programme s'arrête quand le compteur joueur est à 0, alors c'est l'autre joueur qui a gagné, on ajoute un point à son score A (allumette)
            print("Bravo, le vainqueur de ce jeu est",joueur2.nom,"!") # Message pour informer les joueurs du vainqueur 
            joueur2.scoreA += 1     # On ajoute 1 au score allumette
            joueur2.scoreT += 1     # On ajoute 1 au score total
        elif compteur_joueur==1: # Si le programme s'arrête quand le compteur joueur est à 1, alors c'est l'autre joueur qui a gagné, on ajoute un point à son score A (allumette)
            joueur1.scoreA += 1     # On ajoute 1 au score allumette
            joueur1.scoreT += 1     # On ajoute 1 au score total
            print("Bravo, le vainqueur de ce jeu est",joueur1.nom,"!") # Message pour informer les joueurs du vainqueur 

#---------------- Programme principal ------------------
if __name__=="__main__":
    joueur1=Joueur()
    joueur2=Joueur()
    joueur1.nom="Pauline"
    joueur2.nom="Caetano"
    joueur1.scoreA=0
    joueur2.scoreA=0
    joueur1.scoreT=0
    joueur2.scoreT=0
    joueur1.nom,joueur2.nom=premier_joueur(joueur1.nom,joueur2.nom)
    allumette(joueur1,joueur2)
    print("")
    print(joueur1.nom,':',joueur1.scoreA,joueur2.nom,':',joueur2.scoreA)

