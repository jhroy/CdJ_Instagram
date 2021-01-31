# coding: utf-8
# ©2020 Jean-Hugues Roy. GNU GPL v3.

import csv
import spacy
from spacymoji import Emoji

# Chargement de la bibliothèque spacy et du module de détection des emojis
tal = spacy.load("fr_core_news_md")
emoji = Emoji(tal)
tal.add_pipe(emoji, first=True)

# Le fichier source utilisé dans ce script
# contient les colonnes de texte
# qui ont été retranchées du fichier rendu public dans ce répertoire
fichierIN = "mediasfrancoinstagram-fichierSource.csv"

# On crée des fichiers de sortie pour les cinq types d'éléments lexicaux que ce script va générer
# Il s'agit essentiellement de cinq listes de ces éléments et de la somme des interactions des publications dans lesquelles ils se retrouvent
fichEmojis = "insta-emojis.csv"
fichHastags = "insta-hastags.csv"
fichMotsSeuls = "insta-motsseuls.csv"
fichBigrams = "insta-bigrammes.csv"
fichTrigrammes = "insta-trigrammes.csv"

n = 0

# Lecture du fichier source
f = open(fichierIN)
posts = csv.reader(f)
next(posts)

# Boucle pour traiter chacune des publications de notre corpus
for post in posts:
	n += 1
	
	# On réunit les éléments textuels de chaque publication (titre, description et texte obtenu par reconnaissance optique des caractères [s'il y a lieu])
	texte = post[13] + " " + post[14] + " " + post[15]

	# Et on effectue une série d'opérations pour nettoyer le texte (retrancher caractères invisibles, double espaces, etc.); spacy fait normalement un travail semblable, mais ici, il est requis parce que les mots-clics ne seront pas extraits en passant par spacy, car ce dernier sépare le «#» du mot-clic par défaut
	# Ici, on transforme tous les alinéas en simples espaces
	texte = texte.replace("\n", " ")
	# On insère un espace devant chaque «#» pour retrancher des hashtags collés les uns sur les autres, le plus long étant celui-ci:
	# #roman#literature#romancier#élection#france#présidentielle#président#alexandrejardin#politique#citoyen#parrainage#lookatme#photography#photo#photooftheday#green#fredkihn#adocphotos
	texte = texte.replace("#"," #")
	
	# Uniformisation des espaces, des apostrophes et des traits-d'union
	espaces = ["\u2028", "\u2002", "\u2003", "\u2009", "\u200A", "\u200B", "\u200D", "\u200E", "\u202F", "\u2640", "\u00A0", "\uFFFC", "\u2060", "\u2063", "\u3000", "\uFEFF"]
	apostrophes = ["\u2018", "\u2019", "\u02BC", "\u0060", "\u00B4", "\u02B9"]
	traits = ["\u2011", "\u2012", "\u2013", "\u2014", "\u2015"]
	
	for espace in espaces:
		if espace in texte:
			texte = texte.replace(espace, " ")

	for apostrophe in apostrophes:
		if apostrophe in texte:
			texte = texte.replace(apostrophe, "'")

	for trait in traits:
		if trait in texte:
			texte = texte.replace(trait, "-")

	# Cette boucle retranche tous les double-espaces du texte
	while "  " in texte:
		texte = texte.replace("  ", " ")

	# Et on termine en retranchant les espaces superflus au début et à la fin du texte
	texte = texte.strip()

	print(texte)
	print("~"*40)

	# On réunit les données d'interactions («j'aime», commentaires et nombre de vues)
	interactions = int(post[7]) + int(post[8]) + int(post[9])
	
	# On passe le texte dans la «moulinette» de spacy
	try:
		doc = tal(texte)

		# EXTRACTION DES EMOJIS

		# Pour repérer les emojis, on va directement analyser le «doc» pondu par spacy
		# en examinant un à un les «tokens» contenus dans les éléments textuels de la publication
		for token in doc:

			# Testons s'il s'agit d'un emoji à l'aide de la bibliothèque spacymoji importée d'entrée de jeu
			if token._.is_emoji:

				# Si le «token» est bel et bien un emoji
				# on le consigne dans la liste ci-dessous
				# avec la somme des interactions suscitées par la publication qui fait en ce moment l'objet de l'analyse
				infoEmoji = [token,interactions]
				print(infoEmoji)

				# et on l'ajoute au CSV qui contiendra tous les emojis trouvés
				insta = open(fichEmojis, "a")
				gram = csv.writer(insta)
				gram.writerow(infoEmoji)

		print("~"*40)

		# EXTRACTION DES MOTS-CLICS (HASHTAGS)

		# Pour les mots-clis, on a recours à une stratégie plus simple
		# Comme spacy les sépare («#france» est séparé en deux éléments lexicaux: «#» et «france»)
		# on conserve nos mots-clics en effectuant un simple .split en fonction d'un espace, ce qui nous crée une liste de mots
		motsPourHashtags = texte.split()

		# Puis, on examine chacun des mots contenus dans cette liste:
		for element in motsPourHashtags:

			# Si son premier caractère est un dièse et que sa longueur est supérieure à un caractère, on est en présence d'un mot-clic
			if element[0] == "#" and len(element) > 1:

				# On le consigne alors dans la petite liste ci-dessous
				# en prenant soin de le mettre en minuscules et de le nettoyer un brin en retranchant certains caractères indésirables («_», «'», «(» ou «@», par exemple)
				hashtag = element.lower().replace(".","").replace(",","").replace("'","").replace('"','').replace("1)","").replace("2)","").replace("(","").replace(")","").replace("@","").replace("[","").replace("]","").replace("-","").replace("{","").replace("}","").replace(" ","").replace("!","").replace("?","").replace(";","").replace(":","").replace("»","").replace("…","").replace("_","").strip()
				# et en ajoutant la somme des interactions suscitées par la publication qui fait en ce moment l'objet de l'analyse
				infoHashtag = [hashtag,interactions]
				print(infoHashtag)

				# et on l'ajoute au CSV qui contiendra tous les mots-clics trouvés
				insta = open(fichHastags, "a")
				gram = csv.writer(insta)
				gram.writerow(infoHashtag)
		
		print("~"*40)

		# EXTRACTION DES MOTS ET N-GRAMS

		# On génère enfin un grand sac de mots
		# qui consiste à lemmatiser et à mettre en minuscule tous les éléments lexicaux qui
		# ne sont pas des mots vides («à», «de», «la», «des», etc.)
		# ne sont pas des signes de ponctuation
		# ont une longueur supérieure à deux caractères
		# ne contiennent ni espaces ni alinéas
		# et ne sont pas des URL.
		mots = [token.lemma_.lower() for token in doc if token.is_stop == False and token.is_punct == False and len(token) > 1 and " " not in token.text and "\n" not in token.text and "http" not in token.text]
		print(mots)
		# Puis on y fait trois boucles

		# La première pour consigner les mots seuls et la somme des interactions de la publication dans laquelle ils se retrouvent
		for mot in mots:
			infoMot = [mot,interactions]
			print(infoMot)
			
			# On l'ajoute au CSV qui contiendra tous les mots seuls de notre corpus
			insta = open(fichMotsSeuls, "a")
			gram = csv.writer(insta)
			gram.writerow(infoMot)

		print("~"*40)

		# La 2e pour consigner les bigrammes (paires de mots)
		for x, y in enumerate(mots[:-1]):

			# Il s'agit simplement de coller le mot qu'on traite (mots[x]) et le suivant (mots[x+1])
			infoBigramme = ["{} {}".format(mots[x],mots[x+1]),interactions]
			print(infoBigramme)

			# On l'ajoute au CSV qui contiendra tous bigrammes créés
			insta = open(fichBigrams, "a")
			gram = csv.writer(insta)
			gram.writerow(infoBigramme)

		print("~"*40)

		# La 3e pour les trigrammes (vous avez compris le principe)
		for x, y in enumerate(mots[:-2]):

			infoTrigramme = ["{} {} {}".format(mots[x],mots[x+1],mots[x+2]),interactions]
			print(infoTrigramme)

			# On l'ajoute au CSV qui contiendra tous les trigrammes créés
			insta = open(fichTrigrammes, "a")
			gram = csv.writer(insta)
			gram.writerow(infoTrigramme)

	except:
		print("Spacy n'a pas été en mesure d'analyser ce texte...")

	print("#"*40)
	print("   >>> ", n, " <<<")
	print("#"*40)
