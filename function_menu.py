from function import *
def menu():
    print("========================================================================")
    print("\n  MENU PRINCIPAL")
    print("1- Afficher le graphe initial")
    print("7- Revenir en arrière")
    print("0- Quitter")
    return input("Votre choix : ")


def choisir_graphe():
    print("\n ==== CHOIX DU GRAPHE ====")
    print("Veuillez saisir le numéro du graphe à utiliser :")
    print("Les numéros des graphes vont de XX à YY")

    while True:

        numero = int(input("Numéro du graphe que vous voulez : \n"))
        if (1 <= numero <= 44):
            return numero
        else:
            print("Numéro invalide. Veuillez entrer un numéro compris entre XX et YY.")

def charger_graphe():
    #Lecture Graphe
    numero_graphe = choisir_graphe()
    print("Graphe utilisé: " + str(numero_graphe) + "\n")
    Table_Graphe=lecture_automate("Graphe"+str(numero_graphe)+".txt")
    return Table_Graphe
