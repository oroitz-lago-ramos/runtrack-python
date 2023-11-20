nom = "RTX 4090"
prix_unitaire = 2500
quantite_stock = 10

print(f'{nom} - Prix: {prix_unitaire}€; Qte.: {quantite_stock}')
choix_utilisateur = input(f'Combien de {nom} souhaitez vous acheter? : ')
if (int(choix_utilisateur) <= quantite_stock):
    quantite_stock -= int(choix_utilisateur)
    print(f'Vous devez payer {int(choix_utilisateur) * prix_unitaire}€')
else:
    print("Désolé nous n'avons pas assez de stock pour ce produit")
    
print(f'{nom} - Prix: {prix_unitaire}€; Qte.: {quantite_stock}')

print("Attention! A cause de l'inflation les prix ont augmenté de 10%")
print("Voici les informations mises à jour :")
prix_unitaire += (prix_unitaire * 10 / 100)
print(f'{nom} - Prix: {prix_unitaire}€; Qte.: {quantite_stock}')
