# Il y deux methodes de resoudre, soit on le trie avec un algorithme propre soit avec la méthode sorted
# On utilisera la methode sorted puisque dans le job12 nous devrons faire un algorithme de tri
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
# L = sorted(L)
# print(f'la valeur max est : {L[0]}')
# print(f'la valeur min est : {L[-1]}')

# Une autre méthode est en utilisant min et max
print(f'la valeur max est : {max(L)}')
print(f'la valeur min est : {min(L)}')

# Une derniere methode consiterait a trouver la valeur minumum et maximum en parcourant la liste
# min = L[0]
# max = L[0]
# for i in L:
#     if i > max:
#         max=i
#     if i < min:
#         min = i
# print(f'la valeur max est : {max}')
# print(f'la valeur min est : {min}')
    