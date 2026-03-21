import copy

def afficher_matrice(matrice):
    nb_sommets = len(matrice)
    result = []
    
    # On définit une largeur fixe pour chaque case (comme ta longueur_maximale_etats)
    L = 6 
    
    # 1. Ligne tout en haut (fermeture haute au-dessus des numéros de sommets)
    # Laisse un vide au-dessus du "X", puis tire des traits "___"
    result.append(" " * (L + 2) + "_" * ((L + 1) * nb_sommets - 1))
    
    # 2. En-tête avec les colonnes (X | 0 | 1 | 2 ...)
    en_tete = " " * (L + 1) + "|"
    for i in range(nb_sommets):
        en_tete += str(i).center(L) + "|"
    result.append(en_tete)
    
    # 2. Ligne de séparation sous l'en-tête (Fermeture haute de la grille)
    ligne_sep_haut = " " + "_" * L + "|" + ("_" * L + "|") * nb_sommets
    result.append(ligne_sep_haut)
    
    # Ligne de séparation standard entre les données (Fermée à gauche)
    ligne_sep_donnees = "|" + ("_" * L + "|") * (nb_sommets + 1)
    
    # 3. Remplissage des lignes avec les données
    for i in range(nb_sommets):
        # Titre de la ligne avec sa bordure gauche
        ligne_visuelle = "|" + str(i).center(L) + "|" 
        
        for val in matrice[i]:
            if val == float('inf'):
                chaine_val = "" # Case vide si pas d'arc
            else:
                chaine_val = str(val)
            # Ajout de la valeur centrée avec sa bordure droite
            ligne_visuelle += chaine_val.center(L) + "|"
        
        result.append(ligne_visuelle)
        
        # 4. Ligne de séparation après chaque ligne de données
        result.append(ligne_sep_donnees)

    return "\n".join(result) + "\n"

def lecture_graphe(fichier):
    # Initialisation des variables que l'on va utiliser
    tableau = [] # Tableau de base que l'on va remplir et retourner (Matrice N x N pure)
    tab_text = []

    with open(fichier, 'r') as fichier_ouvert: # Chaque ligne du fichier texte entré est mis dans un élément du tableau
        for ligne in fichier_ouvert:
            tab_text.append(ligne.strip())

    nb_sommets = int(tab_text[0])  # nombre de sommets
    nb_arcs = int(tab_text[1])  # nombre d'arcs

    # Initialisation matrice vide avec l'infini (représente l'absence d'arc)
    for i in range(nb_sommets):    
        ligne_matrice = []
        for j in range(nb_sommets):
            ligne_matrice.append(float('inf')) 
        tableau.append(ligne_matrice)

    # Remplissage des transitions (à partir de la ligne 3 du fichier)
    for k in range(2, 2 + nb_arcs):
        ligne = tab_text[k].split()  # Sépare "3 1 25" en ["3","1","25"]

        sommet_depart = int(ligne[0])
        sommet_arrivee = int(ligne[1])
        valeur = int(ligne[2])

        # On remplit la matrice avec la valeur exacte du fichier (aucune modification)
        tableau[sommet_depart][sommet_arrivee] = valeur

    # Le graphe lu est stocké dans une structure de données unique [cite: 21]
    return tableau

def contient_circuit_absorbant(L):
    for i in range(len(L)):
        if L[i][i] < 0:
            return True
    return False

def floyd_warshall(matrice):
    L = copy.deepcopy(matrice)
    P = [[None for _ in range(len(L))] for _ in range(len(L))]
    determiner_matrices_l_et_p(L, P)

    if contient_circuit_absorbant(L):
        print("Le graphe contient un circuit absorbant. L'algorithme de Floyd-Warshall ne peut pas être appliqué.")
    else:
        afficher_chemins(L, P)



def determiner_matrices_l_et_p(L, P):
    n = len(L)

    for k in range(n):
        if L[k][k] == float('inf'):
            L[k][k] = 0  # Assure que la distance d'un sommet à lui-même est au plus 0

    # initialisation matrice prédecesseur
    for i in range(n):
        for j in range(n):
            if L[i][j] != float('inf') and i!=j:
                P[i][j] = i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if L[i][k] + L[k][j] < L[i][j]:
                    L[i][j] = L[i][k] + L[k][j]
                    P[i][j] = P[k][j]  # correspond au dernier arrêt avant d'arriver au noeud j, ce qui va être utile pour la remontée lors de la reconstruction des chemins
    return L, P


def afficher_chemins(L, P):
    n = len(L)
    print("\n--- Consultation des plus courts chemins ---")
    
    while True:
        chemin_reponse = input("Chemin ? (oui/non) : ").strip().lower()
        
        if chemin_reponse in ['oui', 'o', 'y']:
            try:
                depart = int(input(f"Sommet de départ (0 à {n-1}) ? "))
                arrivee = int(input(f"Sommet d'arrivée (0 à {n-1}) ? "))
                
                if 0 <= depart < n and 0 <= arrivee < n:
                    afficher_un_chemin(L, P, depart, arrivee)
                else:
                    print(f"Erreur : Les sommets doivent être compris entre 0 et {n-1}.")
            except ValueError:
                print("Erreur : Veuillez entrer des numéros valides.")
                
            recommencer = input("Recommencer ? (oui/non) : ").strip().lower()
            if recommencer not in ['oui', 'o', 'y']:
                print("Fin de la consultation des chemins.")
                break
                
        else:
            print("Fin de la consultation.")
            break

def afficher_un_chemin(L, P, depart, arrivee):
    """Reconstitue et affiche le chemin entre deux sommets précis."""
    if L[depart][arrivee] == float('inf'):
        print(f"Aucun chemin n'existe entre le Noeud {depart} et le Noeud {arrivee}.")
        return

    print(f"Coût : {L[depart][arrivee]}, Chemin : {depart} -> ", end="")
    
    if depart == arrivee:
        print(f"{arrivee}")
        return

    temp = arrivee
    P_noeud_actuel = []
    
    while P[depart][temp] != depart:
        P_noeud_actuel.append(P[depart][temp])
        temp = P[depart][temp]
    
    for k in range(len(P_noeud_actuel)-1, -1, -1):
        print(f"{P_noeud_actuel[k]} -> ", end="")

    print(arrivee)


