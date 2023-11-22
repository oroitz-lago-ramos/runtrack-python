def pair_or_not(nombre):
    if type(nombre) == int and nombre > 0:
        if nombre % 2 == 0:
            print("Le chiffe est pair")
        else:
            print("Le chiffre est impair")
    else:
        print("Le chiffre doit être un entier positif N")
        
pair_or_not(8)
pair_or_not(5)
pair_or_not(-50)