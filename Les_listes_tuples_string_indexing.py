# ------------- Crée des listes : -------------

liste_num=[1, 4, 5, 12, 19] #Liste avec des int
villes=['tunis', 'paris', 'alger', 'berlin', 'rome'] #Liste avec chaine de caractére
all=[liste_num, villes] #Liste de liste
umpty=[] #Liste vide

# ------------- Crée des tuples : -------------

tuple_prix=[20, 48, 36, 871, 47] 
#Un tuple a les meme caractéristique que les listes sauf que lui est protége et on peut pas changé ses valeurs par la suite et à son execution il est plus rapide et prend moins de mémoire que les listes mais son utilisation reste rare

# ------------- Crée des string : -------------

game="valorant" #une variable string est considérer comme une liste ou chaine de caractére aussi 

# ------------- Indexing : -------------

print(villes[0]) #afficher le premier élemant (le index 0)
print(villes[1]) #afficher le second élemant (le index 1)
print(villes[-1]) #afficher le dernier élemant (le index -1)
print(villes[-2]) #afficher le avant dernier élemant (le index -2)

print(villes[0:4:2]) #nom_liste[index_debut : index_fin : pas]
                     # les index du début et de fin peuvent etre ignorer si on commence du tout debut ou jusqu'à la fin ( ou les deux) et les pas peuvent etres aussi ignirer car c'est 1 par défaut
                     # exemple : nom_liste[::pas] 
                     # ou aussi : nom_liste[:index_fin]
print[liste_num[::-1]] #afficher toute la liste mais en commancant pas la fin


villes[2]= "tlemcen" #modifier modifier une certaine séquence d'une liste

# ------------- Méthodes sur les listes : -------------

villes.append('madrid') #ajouter une séquence à la fin d'une liste
villes.insert(2, "amsterdame") #ajouter une séquence au milieu d'une liste exemple : liste.insert(num_index, séquence)

villes2=['bizerte', 'nice', 'kiev']
villes.extend(villes2) #ajouter les séquence d'une liste à une autre liste exemple : liste1.extend(liste2)

len(villes) #pour savoir le nombre des séquence d'une liste

villes.sort() #pour trier les séquence d'une liste à l'ordre alphabétique ou croissant si c'est des entiers
villes.sort(reverse=True) #pour trier les séquence d'une liste à l'ordre anti alphabétique ou décroissant si c'est des entiers

villes.count('tunis') #pour compter combien de fois une séquence est apparus dans une liste

umpty.clear() #pour effacer tout le comptenu d'une liste

liste_num.remove(48) #pour effacer une séquence d'une liste

# ------------- Utiliser les if / else / for avec des listes : -------------

if 'tunis' in villes :
    print("True")
else:
    print("False")

for i in villes:
    print(i)      #afficher tout les séquence d'une liste aprés avoir attribué à la variable i le contenu de la liste villes

for index, valeur in enumerate(villes):
    print(index, valeur)                 #afficher tout les séquence d'une liste numéroté grace à l'attribution du enumerate à index et de la liste villes à valeur

for a, b in zip(villes, liste_num):
    print(a, b)                       #afficher tout les séquence de deux liste en paraléle
                                      # ps : l'affichage s'arretera quand la plus petite liste finira