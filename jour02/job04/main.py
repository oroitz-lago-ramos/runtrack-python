choix_table = int(input("Entrez un entier supérieur à zero (N): "))
if choix_table > 0:
    for i in range(1, choix_table + 1):
        print(f"Table de multiplication de {i} :")
        for j in range(1, 11):
            resultat = i * j
            print(f"{i} x {j} = {resultat}")
        print("\n")
else:
    print("Nous sommes désolés, le chiffre n'est pas valide")