def round_to_int(number):
    # Si la partie décimale du chiffre est < 0.5 alors le chiffre = int(chiffre)
    # Sinon chiffre = int(chiffre) + 1
    int_part = int(number)
    decimal_part = number - int_part
    if decimal_part < 0.5:
        return int_part
    else:
        return int_part + 1

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

def get_length(list):
    length = 0

    while True:
        try:
            element = list[length]
            length += 1
        except IndexError:
            break

    return length
 
def round_list(list):
    length = get_length(list)
    i = 0
    while i < length:
        rounded_element = round_to_int(list[i])
        list[i] = rounded_element
        i += 1
    list = tri(list)
    return list

liste_chiffres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
liste_arrondie = round_list(liste_chiffres)
print(liste_arrondie)

