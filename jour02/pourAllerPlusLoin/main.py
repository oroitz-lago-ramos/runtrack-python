a = float(input("Coté a: "))
b = float(input("Coté b: "))
c = float(input("Coté c: "))
longueurs = sorted([a,b,c])
if longueurs[-1] < longueurs[0] + longueurs[1]:
    if a == b == c:
        print("Le triangle est constructible et équilatéral")
    elif a == b or a == c or b == c:
        if (longueurs[-1] ** 2) == (longueurs[0] ** 2 + longueurs[1] ** 2):
            print("Le triangle est constructible, rectangle et isocèle")
        else:
            print("Le triangle est constructible et isocèle")
    elif (longueurs[-1] ** 2) == (longueurs[0] ** 2 + longueurs[1] ** 2):
        print("Le triangle est rectangle")
    else:
        print("Le triangle est constructible et quelconque")
else:
    print("Le triangle n'est pas constructible")

