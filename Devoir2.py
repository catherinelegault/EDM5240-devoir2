# coding: utf-8

import csv

fichier = "grants.csv"

f1 = open(fichier)
lignes = csv.reader(f1)

n = 0


x = "Aide aux éditeurs"
y = "Innovation commerciale"
z = "Initiatives collectives"

#boucle pour ressortir les données dans lignes
#https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
for ligne in lignes:
	if any("x" in s for s in ligne) or any("y" in s for s in ligne) or any("z" in s for s in ligne):	
		print(ligne)

#ajouter la date 		
		date = ligne[13]
		annee = date.split("-")

		n += 1
		print(n, annee[0], ligne)