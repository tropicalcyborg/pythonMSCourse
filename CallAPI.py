

import requests
import json

SUBSCRIPTION_KEY = "e86e5b9b398e44928db10c2c4e25c697"
vision_service_address = "https://brazilsouth.api.cognitive.microsoft.com/vision/v2.0/"

address = vision_service_address + "analyze"


parameters  = {'visualFeatures':'Description',
               'language':'pt'}

# Open the image file to get a file object containing the image to analyze
image_path = "./TestImages/dog.jpg"

image_data = open(image_path, "rb").read()

print()
print("Image found")
print()

headers = {"Content-Type": "application/octet-stream", "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY}

#headers    = {'Content-Type': 'application/octet-stream',
#             'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

response = requests.post(address, params= parameters, headers = headers, data = image_data)

print()

response.raise_for_status()

results = response.json()
#print(json.dumps(results))

tgs = results["description"]["tags"]

for perdido in tgs:
    if perdido == "cachorro":
        encontrado = True
    else:
        encontrado = False

    if encontrado:
        print("Cachorro encontrado na imagem")

print()