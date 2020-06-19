import sys
sys.path.insert(0, "..")
from random import randint
import time
import datetime
import time
from opcua import ua, Server


server = Server()
url = "opc.tcp://localhost:4840/"
server.set_endpoint(url)

#opc.tcp://192.168.10.160:4840/freeopcua/server/

name = "Opc_UA__Patient_data_Server"
addspace = server.register_namespace(url)




node = server.get_objects_node()

param = node.add_object(addspace, "Patient")


#Define parameters for node

#name, profileValue, ExtensionUrl, oid, city, systemValue, birthDate, home, streetname, city, state, postalCode, countryValue



import requests
import json


#URL for FHIR-resource

url1 = 'https://syntheticmass.mitre.org/v1/fhir/Patient?_count=1&apikey=vcz49RdhJpe8vVl6fGWW8a2W9nAezIxr'
response = requests.get(url1)

#Check whether the response-code is 200

print(response.status_code)


response_json= response.json()

data = response.text



birth_date = response_json['entry'][0]['resource']['birthDate']
given_name = response_json['entry'][0]['resource']['name'][0]['given'][0] 
sur_name = response_json['entry'][0]['resource']['name'][0]['family']



#Add values to addressspace

given = param.add_variable(addspace, "GivenName", given_name)  # addressspace, parameterName, initial value
sur = param.add_variable(addspace, "SurName", sur_name)
birth = param.add_variable(addspace, "Age", birth_date) 



#Start server
server.start()
print("Server has started at: {}".format(url))



startStop = True
yolo = 1

#As long as the start-stop condition is true, print the values
while startStop:

    print(birth_date)
    print(given_name)
    print(sur_name)

    #Set a delay to two seconds to the while-loop, note: This one does not use ms as a standard format
    time.sleep(2)



