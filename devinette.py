from class_joueur import Joueur 
def devinette(joueur1:Joueur,joueur2:Joueur):
    """
    Fonction : jeu des devinettes, fonctionne en 2 manches, il ne peut y avoir d'égalité, les joueurs joueront à tour de rôle

    Entré : deux joueurs de type classe Joueur

    Sortie : change le score D et T du joueur vainqueur
    """
    compteur_manche:int
    jeu:int
    limite:int
    nombre:int
    resultat:int
    compteur_tour_joueur1:int
    compteur_tour_joueur2:int
    affichage:str
    compteur_manche=1
    jeu=0
    print("")
    print("Vous avez choisi le jeu des devinettes. \n")
    print("----------------------------------------------------------- RÈGLES ------------------------------------------------------------")
    print("|                                                                                                                             |")
    print("| - Ce jeu est en deux manches                                                                                                |")
    print("| - En revanche, il se répètera tant qu'il n'y a pas de vainqueur                                                             |")
    print("| - Les joueurs devront décider ensemble de la limite de l'intervalle                                                         |")
    print("| - Le joueur 1 décidera en premier de la valeur à trouver                                                                    |")
    print("| - Une fois que le joueur 2 aura trouver la bonne valeur, ce sera à lui de décider quelle valeur le joueur 1 devra trouver   |")
    print("| - Les deux joueurs n'ont pas le droit de mentir!                                                                            |")
    print("| - Le vainqueur sera le joueur qui a trouvé le bon nombre avec le moins de tour sur la même intervalle                       |")
    print("| - Si les deux joueurs ont trouvé le nombre avec le même nombre de tour, le jeu se répètera car il y a égalité               |")
    print("|                                                                                                                             |")
    print("| Bon jeu!                                                                                                                    |")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("")
    while jeu==0:   # Le programme ne s'arrête pas dans que la condition d'arrêt est pas égal à 0
        print(" - MANCHE n°",compteur_manche," ----------------------------------") # Affiche le numéro de la manche, 1 ou 2
        while compteur_manche==1:   # Cette boucle tant que correspond à la partie où le joueur 2 doit deviner le nombre
            limite=int(input("Choissisez la limite n de l'intervalle [1,n] : "))    # La limite n'a pas de borne, les joueurs peuvent choisir ce qu'ils veulent
            while limite<2: # Boucle qui vérifie que la limite est supérieur à 1
                print("La limite ne peut pas être négative et doit être supérieure à 1.")
                limite=int(input("Choissisez la limite n de l'intervalle [1,n] : "))
            print(joueur1.nom,"est le joueur 1, c'est lui qui choisit le nombre à deviner. Faites en sorte que",joueur2.nom,"ne puisse pas voir la valeur choisit.")
            print("")
            nombre=int(input("Entrez le nombre à deviner qui est entre 1 et la limite inclus : "))
            while nombre>limite or nombre<1:    # Le nombre à deviner doit être dans l'intervalle [1,limite], redemande la valeur si la condition n'est pas remplis
                print("La valeur choisit n'est pas dans l'intervalle.")
                nombre=int(input("Entrez le nombre à deviner qui est entre 1 et la limite inclus : "))
            resultat=0
            compteur_tour_joueur2=1
            for i in range(30): # Cela permet de sauté 30 lignes, pour que le joueur 2 ne voit pas le nombre a deviner
                print("")
            while nombre!=resultat:
                print("")
                print("- Tour n°",compteur_tour_joueur2,"--------------------------------------")
                resultat=int(input("Veuillez entrer un nombre : "))
                while resultat>limite or resultat<1:    # Le nombre entré doit être forcément dans l'intervalle, redemande de l'entrer jusqu'à que la valeur soit correcte
                    print("La valeur choisit n'est pas dans l'intervalle.")
                    resultat=int(input("Veuillez entrer un nombre : "))
                if resultat==nombre:    # Ne fait rien car c'est le joueur 1 qui doit entré la condition
                    pass
                print(joueur1.nom,"vous devez sélectionner entre - (si le nombre est trop grand), + (si le nombre est trop petit) ou gagné afin d'informer",joueur2.nom,".")
                affichage=input("Veuillez entrer la valeur (+/-/gagné) : ")
                while affichage!='+' and affichage!='-' and affichage!="gagné": # Vérifie que la valeur est correcte
                    print(joueur1.nom,"vous n'avez pas entré une valeur valide.")
                    affichage=input("Veuillez entrer la valeur (+/-/gagné) : ")
                if affichage=='-':
                    if resultat>nombre:
                        print("Trop grand!")    # Affiche le message correspondant
                    elif resultat==nombre:
                        print(joueur1.nom,"a menti, vous avez trouvé le bon nombre.")
                        print("C'est gagné.")   # Affiche le message correspondant
                    else:
                        print(joueur1.nom,"a menti,",resultat,"est trop petit.")    # Affiche un message si le joueur 1 à menti
                elif affichage=='+':
                    if resultat<nombre:
                        print("Trop petit!")    # Affiche le message correspondant
                    elif resultat==nombre:
                        print(joueur1.nom,"a menti, vous avez trouvé le bon nombre.")
                        print("C'est gagné.")   # Affiche le message correspondant
                    else:
                        print(joueur1.nom,"a menti,",resultat,"est trop grand.")    # Affiche un message si le joueur 1 à menti
                elif affichage=="gagné":
                    if resultat==nombre:
                        print("C'est gagné.")   # Affiche le message correspondant
                    else:
                        while affichage=="gagné":
                            print(joueur1.nom,"a menti, il doit entrer une valeur correcte.")   # Affiche un message si le joueur 1 à menti
                            affichage=input("Veuillez entrer la valeur (+/-) : ")   # Si le joueur a menti, cela veut dire que le nombre entré est soit plus petit soit plus grand
                            while affichage!='+' and affichage!='-':    # Donc il faut afficher le message correspondant à la valeur
                                print(joueur1.nom,"vous n'avez pas entré une valeur valide.")
                                affichage=input("Veuillez entrer la valeur (+/-) : ")   # Ici le joueur n'aura le droit que d'entré + ou - car on sait déjà qu'il a menti pour gagné
                            if affichage=='-':
                                if resultat>nombre:
                                    print("Trop grand!")
                                else:
                                    print(joueur1.nom,"a menti,",resultat,"est trop petit.")
                            elif affichage=='+':
                                if resultat<nombre:
                                    print("Trop petit!")
                                else:
                                    print(joueur1.nom,"a menti,",resultat,"est trop grand.")
                compteur_tour_joueur2+=1    # On change de manche, c'est au joueur 2 de choisir le nombre à deviner
            compteur_manche+=1
        print("")
        print(" - MANCHE n°",compteur_manche," ----------------------------------")
        while compteur_manche==2:
            print("C'est au tour de",joueur2.nom,"de choisir le nombre à trouver. Nous vous rappelons que la limite est",limite,"et que c'est au tour de",joueur1.nom,"de trouver le nombre.")
            print("")
            nombre=int(input("Entrez le nombre à deviner qui est entre 1 et la limite inclus : "))
            while nombre>limite or nombre<1:    # Le nombre à deviner doit être dans l'intervalle [1,limite], redemande la valeur si la condition n'est pas remplis
                print("La valeur choisit n'est pas dans l'intervalle.")
                nombre=int(input("Entrez le nombre à deviner qui est entre 1 et la limite inclus : "))
            resultat=0
            compteur_tour_joueur1=1
            for i in range(30): # Cela permet de sauté 30 lignes, pour que le joueur 2 ne voit pas le nombre a deviner
                print("")
            while nombre!=resultat:
                print("")
                print("- Tour n°",compteur_tour_joueur1,"--------------------------------------")
                resultat=int(input("Veuillez entrer un nombre : "))
                while resultat>limite or resultat<1:    # Le nombre entré doit être forcément dans l'intervalle, redemande de l'entrer jusqu'à que la valeur soit correcte
                    print("La valeur choisit n'est pas dans l'intervalle.")
                    resultat=int(input("Veuillez entrer un nombre : "))
                if resultat==nombre:    # Ne fait rien car c'est le joueur 2 qui doit entré la condition
                    pass
                print(joueur2.nom,"vous devez sélectionner entre - (si le nombre est trop grand), + (si le nombre est trop petit) ou gagné afin d'informer",joueur1.nom,".")
                affichage=input("Veuillez entrer la valeur (+/-/gagné) : ")
                while affichage!='+' and affichage!='-' and affichage!="gagné":
                    print(joueur2.nom,"vous n'avez pas entré une valeur valide.")
                    affichage=input("Veuillez entrer la valeur (+/-/gagné) : ")
                if affichage=='-':
                    if resultat>nombre:
                        print("Trop grand!")    # Affiche le message correspondant
                    elif resultat==nombre:
                        print(joueur2.nom,"a menti, vous avez trouvé le bon nombre.")
                        print("C'est gagné.")   # Affiche le message correspondant
                    else:
                        print(joueur2.nom,"a menti,",resultat,"est trop petit.")    # Affiche un message si le joueur 2 à menti
                elif affichage=='+':
                    if resultat<nombre:
                        print("Trop petit!")    # Affiche le message correspondant
                    elif resultat==nombre:
                        print(joueur2.nom,"a menti, vous avez trouvé le bon nombre.")
                        print("C'est gagné.")   # Affiche le message correspondant
                    else:
                        print(joueur2.nom,"a menti,",resultat,"est trop grand.")    # Affiche un message si le joueur 2 à menti
                elif affichage=="gagné":
                    if resultat==nombre:
                        print("C'est gagné.")   # Affiche le message correspondant
                    else:
                        while affichage=="gagné":
                            print(joueur1.nom,"a menti, il doit entrer une valeur correcte.")   # Affiche un message si le joueur 2 à menti
                            affichage=input("Veuillez entrer la valeur (+/-) : ")   # Si le joueur a menti, cela veut dire que le nombre entré est soit plus petit soit plus grand
                            while affichage!='+' and affichage!='-':    # Ici le joueur n'aura le droit que d'entré + ou - car on sait déjà qu'il a menti pour gagné
                                print(joueur1.nom,"vous n'avez pas entré une valeur valide.")
                                affichage=input("Veuillez entrer la valeur (+/-) : ")
                            if affichage=='-':
                                if resultat>nombre:
                                    print("Trop grand!")
                                else:
                                    print(joueur1.nom,"a menti,",resultat,"est trop petit.")
                            elif affichage=='+':
                                if resultat<nombre:
                                    print("Trop petit!")
                                else:
                                    print(joueur1.nom,"a menti,",resultat,"est trop grand.")
                compteur_tour_joueur1+=1
            compteur_manche+=1
        if compteur_tour_joueur1==compteur_tour_joueur2:    # Si les compteurs sont égaux, les joueurs devront rejouer
            print("Les deux joueurs ont trouvé le bon nombre en",compteur_tour_joueur1 -1,"fois, il y a donc égalité.")
            print("Vous devez refaire une partie pour déterminer le vainqueur.")
            compteur_manche=1
            jeu=0   # La boucle tant que va continuer à tourner tant qu'il y a égalité
        else:
            jeu=1   # condition de sortie validé, la boucle cesse
    if compteur_tour_joueur1<compteur_tour_joueur2:
        print("Bravo, le vainqueur de ce jeu est",joueur1.nom,"!")  # Si le joueur 1 a trouvé le nombre avec moins de tour, il gagne
        joueur1.scoreD += 1 # On ajoute 1 au score D (devinette) 
        joueur1.scoreT += 1 # On ajoute 1 au score T (total)
    elif compteur_tour_joueur1>compteur_tour_joueur2:
        print("Bravo, le vainqueur de ce jeu est",joueur2.nom,"!")  # Si le joueur 2 a trouvé le nombre avec moins de tour, il gagne
        joueur2.scoreD += 1 # On ajoute 1 au score D (devinette)
        joueur2.scoreT += 1 # On ajoute 1 au score T (total)

#--------------------- Programme principal -------------------
if __name__=="__main__":
    joueur1=Joueur()
    joueur2=Joueur()
    joueur1.nom="Pauline"
    joueur2.nom="Caetano"
    joueur1.scoreD=0
    joueur1.scoreT=0
    joueur2.scoreD=0
    joueur2.scoreT=0
    devinette(joueur1,joueur2)
    print(joueur1.nom,':',joueur1.scoreD,joueur2.nom,':',joueur2.scoreD)
    




    