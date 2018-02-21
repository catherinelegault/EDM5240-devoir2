# coding: utf-8

### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

import csv

### Je commence par modifier légèrement le nom du fichier afin de permettre à ton code de rouler sur mon ordi

fichier = "../grants.csv"

f1 = open(fichier)
lignes = csv.reader(f1)

n = 0

x = "Aide aux éditeurs"
y = "Innovation commerciale"
z = "Initiatives collectives"

### Bonne documentation dans ton code

#boucle pour ressortir les données dans lignes
#https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string

for ligne in lignes:

### En mettant des guillemets, ton «if» vérifie si les lettres «x», «y» ou «z» se retrouvent quelque part dans la ligne
### Pour vérifier la présence du texte contenu dans tes variables, il fallait retrancher les guillemets

	# if any("x" in s for s in ligne) or any("y" in s for s in ligne) or any("z" in s for s in ligne):
	if any(x in s for s in ligne) or any(y in s for s in ligne) or any(z in s for s in ligne):
		print(ligne)

#ajouter la date 
		date = ligne[13]

### Astucieuse méthode pour trouver la date.
### Je n'y avais pas pensé!
### Ma méthode était plutôt celle-ci : annee = ligne[13][:4]
### Les deux sont bonnes :)

		annee = date.split("-")

		n += 1
		print(n, annee[0], ligne)

### Code intéressant, mais qui ne permet malheureusement pas de filtrer les subventions du Fonds du Canada pour les périodiques (FCP)
### Ton code original trouve 79582 subventions.
### En le corrigeant comme je l'ai fait à la ligne 32, ça se réduit à 4844
### L'ennui, c'est que certaines «Initiatives collectives» ne concernent pas le Fonds du Canada pour les périodiques et touchent plutôt le monde du livre

### La solution, un seul «if», mais avec un «or»:
### «if "Fonds du Canada pour les périodiques" in ligne[17] or "FCP -" in ligne[17]:»
### Cela t'en donne 4608 et se rapproche davantage de ce que l'on cherche.