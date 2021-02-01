# coding utf-8
# ©2020 Jean-Hugues Roy. GNU GPL v3.

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import sys, csv, time, os, requests, json

cle = "b5866b1129ee45a6aa29e93ed71a3d81" ### CHANGE POUR TA CLÉ À TOI
point = "https://instafranco.cognitiveservices.azure.com/" ### CHANGE POUR TON ENDPOINT À TOI
# fin = "donneesUDA.csv"
fout = "instaOUT.csv"
# oeil = ComputerVisionClient(point, CognitiveServicesCredentials(cle))

analyze_url = point + "vision/v3.0/analyze"

fichiers = os.listdir()

for fichier in fichiers:
	if fichier.endswith(".jpg"):
		print(fichier)
		image_data = open(fichier, "rb").read()

		entetes = {'Ocp-Apim-Subscription-Key': cle,'Content-Type': 'application/octet-stream'}
		params = {'visualFeatures': 'Categories,Description,Color'}
		response = requests.post(analyze_url, headers=entetes, params=params, data=image_data)
		response.raise_for_status()

		analyse = response.json()
		print(analyse)

		fichierjson = fichier.replace(".jpg",".json")
		# print(fichiesrjson)

		with open(fichierjson, "w") as prout:
			json.dump(analyse, prout)

		time.sleep(3)