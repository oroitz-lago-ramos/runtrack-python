import string
print("\nPremière méthode en écrivant l'alphabet dans un print")
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ\n")

# print("Deuxième solution en important le module string, l'alphabet etant string.ascii\n")
# print("Alphabet minuscule:")
# for letter in string.ascii_lowercase:
#    si on n'utilise pas end les lettres seront affichées l'une en dessous de l'autre
#    end si on mettait end = " " il mettrait un espace entre chaque caractère
# 	print(letter, end ="")
# print("\nAlphabet majuscule:")
# for letter in string.ascii_uppercase:
#    print(letter, end ="")

# Après quelques recherches il n'y a pas besoin de boucler dans les ascii donc nous pouvons directement 
print("Deuxième solution en important le module string, l'alphabet etant string.ascii")
print('Alphabet minuscule: ' + string.ascii_lowercase + "\n")
print("Alphabet majuscule: " + string.ascii_uppercase + "\n")