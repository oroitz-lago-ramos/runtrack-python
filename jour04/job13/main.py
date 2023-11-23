def get_length(liste):
    length = 0

    while True:
        try:
            element = liste[length]
            length += 1
        except IndexError:
            break

    return length

def test_tri(liste,length):
    count = 0
    i = 1
    while i < length:
        if liste[i] < liste[i-1]:
            liste[i], liste[i-1] = liste[i-1], liste[i]
            count += 1
        i += 1
    if count > 0:
        return 1
    else:
        return 0
        
    
def tri(liste):
    length = get_length(liste)
    finish_count = 1
    while finish_count != 0 :
        finish_count -= 1
        finish_count += test_tri(liste, length) 
    return liste 

L = [10,20,30,20,10,50,60,40,80,50,40]
print(L)

# Fonction nous permettant de remplacer les dupes par les X pour après remplir une liste en sautant les X
# Celle ci est la première solution "Faite maison" qui m'est venue à la tête.
# J'ai du regarder d'autres personnes pour me rendre compte que ce n'était pas la meilleure option
# def remove_dupes_funny(liste):
#     length = get_length(liste)
#     liste = tri(liste)
#     i = 1
#     while i < length:
#         if liste[i] == liste[i - 1]:
#             liste[i-1] = "X"
#         i += 1

#     list_no_dupes = []
#     i = 0 
#     while i < length:
#         if liste[i] != "X":
#             list_no_dupes += [liste[i]]
#         i += 1
#     return list_no_dupes

# L_funny = remove_dupes_funny(L)
# print(L_funny)

# Maintenant je veux réaliser la méthode qui consiste a creer une liste vide 
# et d'insèrer un à un les chiffres de notre liste si le chiffre n'y est pas encore
#  Je veux eviter le not in car je le considère une méthode systhème
def is_not_in(element, liste):
    i = 0
    length = get_length(liste)
    while i < length:
        if liste[i] == element:
            return False
        i += 1
    return True 

def remove_dupes(liste):
    length = get_length(liste)
    liste_no_dupes = []
    i = 0
    while i < length:
        if is_not_in(liste[i], liste_no_dupes) == True:
            liste_no_dupes += [liste[i]]
        i += 1
    return liste_no_dupes

L_normal = remove_dupes(L)
print(L_normal)
    
            