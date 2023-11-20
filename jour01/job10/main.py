montant_initial = 11_000
taux_rendement_annuel = 2 / 100
gain_annuel = (montant_initial * taux_rendement_annuel)
print(f'Le gain annuel est de : {gain_annuel}€')

montant_initial += 5_000
taux_rendement_annuel += (2 / 100)
gain_annuel = (montant_initial * taux_rendement_annuel)
print(f'Le gain annuel est de : {gain_annuel}€')

# L'utilisateure retrait 10% du montant total

montant_total = montant_initial + gain_annuel
print(f'Le montant total est : {montant_total}€')
montant_total -= (montant_total * 10 / 100)
print(f'Le nouveau montant total est : {montant_total}€')
montant_initial = montant_total
gain_annuel -= (1 / 100)
print(f'Le gain annuel est de : {gain_annuel}€')
