# coding: utf-8

import csv
import spacy

tal = spacy.load("fr_core_news_sm")

fichierIN = "mediasfrancoinstagram-fichierSource.csv"

n = 0

f = open(fichierIN)
posts = csv.reader(f)
next(posts)

for post in posts:
	n += 1
	nomFichier = "txtMois/{}.txt".format(post[5])
	print(n,nomFichier)

	texte = post[13] + " " + post[14] + " " + post[15]

	doc = tal(texte)
	mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False and len(token) > 1 and " " not in token.text and "\n" not in token.text and "http" not in token.text]

	lepost = ""

	for mot in mots:
		lepost += mot + " "

	lepost.strip()

	with open(nomFichier, "a") as f:
		print("{}\n".format(lepost), file=f)
