# Pour cet exercice j'ai pris la liberté non seulement de compter le nombre de coups mais aussi le nombre de boucles parcourues
# En effet je voulais tester ma version du tri a bulles comparée a celle qu'on peut trouver sur internet
# Dans ma version j'utilise un "trick" proposé par Rodolphe lorsque je fesais le jeux de sudoku qui générait des grilles aléatoire en C

# Voici ma version
def test_tri(liste):
    count = 0
    i = 1
    number_loop = 0 
    while i < len(liste):
        number_loop += 1
        if liste[i] < liste[i-1]:
            liste[i], liste[i-1] = liste[i-1], liste[i]
            count += 1
        i += 1
    # print(moves_count)
    if count > 0:
        return 1 ,count, number_loop
    else:
        return 0, count, number_loop
        
    
def tri(liste):
    finish_count = 1
    total_count = 0
    total_loops = 0
    while finish_count != 0 :
        finish_count -= 1
        finish_count, moves_count, number_loop = test_tri(liste)
        total_count += moves_count
        total_loops += number_loop
    print(f"Nombre de total de coups nécessaires pour trier la liste : {total_count}")
    print(f"Nombre total de boucles : {total_loops}")
    return liste

L4= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
L3 = [64, 34, 25, 12, 22, 11, 90]
L = [1,2,3,5,4,6,7,8,9,10,11,12,13,14,15]
print("\n----------Résultats de ma version du tri à bulles----------\n")
print(f"Liste triée : {tri(L)}\n")

# ALgorithme trouvé sur internet
def tri_bulles(tableau):
    n = len(tableau)
    coups = 0
    boucles = 0

    for i in range(n):
        for j in range(0, n-i-1):
            boucles += 1
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
                coups += 1

    return tableau, coups, boucles

L4= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
L3 = [64, 34, 25, 12, 22, 11, 90]
L = [1,2,3,5,4,6,7,8,9,10,11,12,13,14,15]
tri, nombre_coups, nombre_boucles = tri_bulles(L)
print("----------Résultats du tri à bulles trouvé sur internet----------\n")
print("Tableau trié:", tri)
print("Nombre de coups pour le tri à bulles:", nombre_coups)
print("Nombre total de boucles parcourues:", nombre_boucles, "\n")

# Nous pouvons observer que plus la liste et grande et moins il y a d'objets à trier, mon algorithme parcours bcp moins de boucles
# Testons maintenant pour une liste complétement désordonée:
# Le nombres de boucles est supérieure que celle trouvé sur internet mais la difference est très petite
# Teston maintenant une liste ordonée à l'envers:
# Pour ce qui est d'une liste ordonée à l'envers ma version parcourt bcp plus de fois que celle d'internet
# 90 pour la mienne et 45 pour celle d'internet
# 
# J'en conclut donc que ma version n'est pas optimale pour tous le cas de figure
# Si la liste est longue et il y a juste un chiffre à changer c'est les conditions idéales de mon algorithme: 28 pour la mienne et 105 pour celle d'internet
# Si la liste est desordonée les deux algorithmes sont similaires
# Pour le pire cas d'utilisation de ma version, la liste ordonée dans l'autre sens ce n'est vraiment pas la meilleure solution 

# Une autre option qui serait je pense que la meilleure pour le tri a bulles, 
# utiliser un booléen entre les deux boucles qui si il y a eu un changement elle devient false

