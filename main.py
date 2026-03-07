from function import *
from function_menu import *

continuer = True
while continuer != False:
    Table_Graphe = charger_graphe()

    while continuer:
        choix = menu()
        print("========================================================================")
        if choix == '7':
            # Revient au choix du graphe

            break
        
        elif choix == '2':
            # Graphe initial

            print("\nFloyd-Warshall : ")
            floyd_warshall(Table_Graphe)


        elif choix == '1':
            # Graphe initial

            print("\nAffichage du graphe : ")
            print(afficher_matrice(Table_Graphe))

        elif choix == '0':
            # Quitte le menu

            print("\nMerci, à bientôt !")
            continuer = False
            break

        else:
            print("\nChoix invalide, veuillez réessayer.")