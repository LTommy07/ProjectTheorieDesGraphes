def afficher_matrice(matrice):
    result = []
    for ligne in matrice:
        result.append(" | ".join(f"{str(val):15}" for val in ligne))
    return "\n".join(result)

def lecture_automate(fichier):
    # Initialisation des variables que l'on va utiliser
    tableau = [["X"]] # Tableau de base que l'on va remplir et retourner
    tab_text = []

    with open(fichier, 'r') as fichier: # Chaque ligne du fichier texte entré est mis dans un élément du tableau
        for ligne in fichier:
            tab_text.append(ligne.strip())

    nb_sommets = int(tab_text[0])  # nombre de sommets
    nb_arcs = int(tab_text[1])  # nombre d'arcs

    for i in range(0, nb_sommets):
        tableau[0].append(i)   # Création des sommets dans la première ligne du tableau

    for i in range(0, nb_sommets):
        tableau.append([i])    # Création des sommets pour chaque ligne

    # Initialisation matrice vide
    for i in range(1, nb_sommets+1):    # On met +1 en raison des titres des sommets
        for j in range(1, nb_sommets+1):
            tableau[i].append("")

    # Remplissage des transitions (à partir de la ligne 3 du fichier)
    for k in range(2, 2 + nb_arcs):
        ligne = tab_text[k].split()  # Sépare "3 1 25" en ["3","1","25"]

        sommet_depart = int(ligne[0])
        sommet_arrivee = int(ligne[1])
        valeur = int(ligne[2])

        # On remplit la matrice (+1 en raison des titres des sommets)
        tableau[sommet_depart + 1][sommet_arrivee + 1] = valeur

    return tableau