def getLength(liste):
    length = 0
    for i in liste:
        length += 1
    return length+


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
    length = getLength(liste)
    finish_count = 1
    while finish_count != 0 :
        finish_count -= 1
        finish_count += test_tri(liste, length)
    return liste 

L = [10,20,30,20,10,50,60,40,80,50,40]
print(L)
length = getLength(L)
L = tri(L)
print(L)
i = 1
while i < length:
    if L[i] == L[i - 1]:
        L[i-1] = "X"
    i += 1
print(L)
list_no_dupes = []
i = 0 
while i < length:
    if L[i] != "X":
        list_no_dupes += [L[i]]
    i += 1
L=list_no_dupes
print(L)
            