def liste(type, saison):
    fruits = {"ete": "Poire, fraise, cassis", "hiver": "orange, mandarine et kiwi"}
    legumes = {"ete": "artichaut, aubergine,navet", "hiver": "carotte, topinambour, endive"}
    if type == "fruits":
        print(fruits[saison])
    elif type == "legume":
        print(legumes[saison])
        
liste("fruits", "ete")