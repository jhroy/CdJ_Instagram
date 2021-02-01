# coding utf-8
# ©2020 Jean-Hugues Roy. GNU GPL v3.

import csv, os, json
from collections import Counter

fout = "instaOUT.csv"
n = 0

fichiers = os.listdir()

lieux = []
celebrites = []
categories = []
etiquettes = []

for fichier in fichiers:
	if fichier.endswith(".json"):
		n += 1
		# print(n,fichier)
		with open(fichier) as lefichier:
			donnees = json.load(lefichier)
			# print(donnees.keys())
			
				# print(cat.keys())
				# print(cat["name"])
			try:
				# print(len(donnees["categories"][0]["detail"]["landmarks"]))
				if len(donnees["categories"][0]["detail"]["landmarks"]) > 0:
					for landmark in donnees["categories"][0]["detail"]["landmarks"]:
						# print(landmark["name"])
						lieux.append(landmark["name"])
				# print("*"*8)
			except:
				prout = 0
			try:
				if len(donnees["categories"][0]["detail"]["celebrities"]) > 0:
					for celebrity in donnees["categories"][0]["detail"]["celebrities"]:
						# print(celebrity["name"])
						celebrites.append(celebrity["name"])
			# 	print("*"*8)
			except:
				prout = 0

			for cat in donnees["categories"]:
				# print(cat["name"])
				categories.append(cat["name"])

			for tag in donnees["description"]["tags"]:
				# print(tag)
				etiquettes.append(tag)

			try:
				for vignette in donnees["description"]["captions"]:
					# print(vignette["text"])
					vignettes.append(vignette["text"])
			except:
				prout = 0
			print("*"*8)

freq = Counter(categories)
print(freq.most_common(100))
print(len(categories))

freq = Counter(etiquettes)
print(freq.most_common(100))
print(len(etiquettes))

freq = Counter(celebrites)
print(freq.most_common(100))
print(len(celebrites))