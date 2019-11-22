# -*- coding: utf-8 -*-

import requests
import json
from colorama import init, Fore, Style
from dotenv import load_dotenv
load_dotenv()
import os

subscription_key = os.getenv('SUBSCRIPTION_KEY')


print()


imagem = input ("Digite o nome da imagem que vc quer consultar: ")

passW = os.getenv('PASSW')
print()
print(Fore.GREEN, passW)


vision_service_address = "https://brazilsouth.api.cognitive.microsoft.com/vision/v2.0/"

address = vision_service_address + "analyze"

parameters  = {'visualFeatures':'Description',
               'language':'pt'}

# Open the image file to get a file object containing the image to analyze
#image_path = "./TestImages/dog4.jpg"
image_path = "./TestImages/" + imagem

image_data = open(image_path, "rb").read()

headers = {"Content-Type": "application/octet-stream", "Ocp-Apim-Subscription-Key": subscription_key}


response = requests.post(address, params= parameters, headers = headers, data = image_data)

print()

response.raise_for_status()

results = response.json()
#print(json.dumps(results))

tgs = results["description"]["tags"]

encontrado = False

for perdido in tgs:
    if perdido == "cachorro":
        encontrado = True

if encontrado:
    print(Fore.RED ,Style.BRIGHT, 'Cachorro encontrado na imagem')
    print(Fore.WHITE, Style.NORMAL)
else:
    print(Fore.BLUE, 'Não há cachorros na imagem')
    print(Fore.WHITE)

print()

Style.RESET_ALL