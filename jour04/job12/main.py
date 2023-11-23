L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
print(L)

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

tri(L)
print(L)
