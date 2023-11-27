def arrondir_note(note):
    if note < 40:
        return note
    if note % 5 >= 3:
        while note % 5 != 0:
            note += 1
    return note
            


def arrondir_liste(liste):
    for i in range(len(liste)):
        liste[i] = arrondir_note(liste[i])
    return liste

liste_notes = [82,78,64,67,21,34,98,74,58,53,17,12,16,88]
liste_notes = arrondir_liste(liste_notes)
print(liste_notes)