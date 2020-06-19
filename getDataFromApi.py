import requests
import json


#URL for FHIR-resource

url = 'https://syntheticmass.mitre.org/v1/fhir/Patient?_count=1&apikey=vcz49RdhJpe8vVl6fGWW8a2W9nAezIxr' #'https://www.vg.no/'
response = requests.get(url)

response_json= response.json()

#print(response_json[])


data = response.text


#print(response_json['entry'][0]['resource']['address']) #address


print( response_json['entry'][0]['resource']['name'][0]['family']) #

birth_date = response_json['entry'][0]['resource']['birthDate']
name = response_json['entry'][0]['resource']['name'][0]['given'][0] + ' ' + response_json['entry'][0]['resource']['name'][0]['family']


print(name)
print(birth_date)

print(response.status_code)


