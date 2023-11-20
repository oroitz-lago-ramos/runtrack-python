montant_initial = 11_000
taux_rendement_annuel = 2
gain_annuel = (montant_initial * taux_rendement_annuel / 100)
montant_total = gain_annuel + montant_initial
print(f'Le gain annuel est de : {gain_annuel}€')

# Supposons que l'utilisateur augmente le capital la même année
montant_initial += 5_000
taux_rendement_annuel += 2
gain_annuel = (montant_initial * taux_rendement_annuel / 100)
print(f'Le nouveau gain annuel après avoir rajouté 5000€ est de : {gain_annuel}€')

# Supposons que l'utilisateure retrait 10% du montant total après une année
montant_total = montant_initial + gain_annuel
print(f'Le montant total après une année est : {montant_total}€')
montant_total -= (montant_total * 10 / 100)
print(f'Le nouveau montant total après retrait est : {montant_total}€')
montant_initial = montant_total
taux_rendement_annuel -= 1
gain_annuel = (montant_initial * taux_rendement_annuel / 100)
print(f'Le gain annuel est donc de : {gain_annuel}€')
