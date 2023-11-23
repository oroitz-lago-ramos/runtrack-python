def swap_first_last(liste):
    # temp = liste[0]
    # liste[0] = liste [-1]
    # liste[-1] = temp
    liste[0], liste[-1] = liste[-1], liste[0]
    return liste

L = [1,2,3,4,5]
print(L)
L = swap_first_last(L)
print(L)