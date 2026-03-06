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
