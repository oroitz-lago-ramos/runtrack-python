chaine = "Salut je suis une chaine de caracteres"
count = 0
for i in chaine:
    if (i == "e"):
        count += 1
if count > 0:
    print(f'Il y a {count} "e" dans la chaîne de caractères')
else:
    print("Il n'y a pas de \"e\" dans la chaîne de caractères")