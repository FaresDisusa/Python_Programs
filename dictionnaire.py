inventaire = {
    "banane" : 5800,
    "orange" : 4350,
    "chocoloat": 402,
} 
traduction = {
    "bonjour":"hello",
    "oiseaux":"birds",
    "merde":"shit",
}
"""
associer quelque chose à quelque chose
nom_dicionnaire = {
    key1 : value1 ,
    key2 : value2,
}
ps: les clés ne peuvent pas etres rassosier contrairemant au valeurs
"""
inventaire.values() #afficher tout les valeur du dictionnaire 
inventaire.keys() #afficher tout les clé du dictionnaire
len(inventaire) #afficher le nombre des associations
inventaire["abricots"] = 8900 #ajouter une nouvelle association au dictionnaire

print(inventaire.get('banane', 0)) #si banane existe dans le dicionnaire , ca affiche ca valeur sinon afficher 0

inv1 = ["tozina", "bagra", "5rouf" "dina"]
inventaire.fromkeys(inv1, "defaut")  #ajouter une liste à un dicionnaire 
                                     # nom_dicionnaire.fromkeys(nom_liste, valeur_à_assigner)

inventaire.pop("orange") #dissocier une clé de ca valeurs et puis afficher ca valeur (la clé aprés ne sera plus existante)