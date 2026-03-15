from function import *
def menu():
    print("========================================================================")
    print("\n  MENU PRINCIPAL")
    print("1- Afficher le graphe initial")
    print("2- Trouver le plus court chemin entre tous les couples de sommets à l'aide de Floyd-Warshall")
    print("3- Revenir en arrière")
    print("0- Quitter")
    return input("Votre choix : ")


def choisir_graphe():
    print("\n ==== CHOIX DU GRAPHE ====")
    print("Veuillez saisir le numéro du graphe à utiliser :")
    print("Les numéros des graphes vont de 1 à 14 (14 pour le problème réel)")

    while True:

        numero = int(input("Numéro du graphe que vous voulez : \n"))
        if (1 <= numero <= 14):
            return numero
        else:
            print("Numéro invalide. Veuillez entrer un numéro compris entre 1 et 14.")

def charger_graphe():
    #Lecture Graphe
    numero_graphe = choisir_graphe()
    print("Graphe utilisé: " + str(numero_graphe) + "\n")
    Table_Graphe=lecture_graphe("Graphes\Graphe"+str(numero_graphe)+".txt")
    return Table_Graphe