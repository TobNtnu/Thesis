import sys
sys.path.insert(0, "..")
from random import randint
import time
import xml.etree.ElementTree as ET

import datetime

import time

from opcua import ua, Server

server = Server()
url = "opc.tcp://localhost:4840/freeopcua/server/"
server.set_endpoint(url)

name = "Opc_UA__Patient_data_Server"
addspace = server.register_namespace(url)

node = server.get_objects_node()

param = node.add_object(addspace, "Parameters")




Temp = param.add_variable(addspace, "Temperature", 0)  # addressspace, parameterName, initial value

Press = param.add_variable(addspace, "Pressure", 0) # AddressSpace, parameretname, initialValue

T = param.add_variable(addspace, "Time", 0)

#Set values as writeable

Temp.set_writable()
Press.set_writable()
T.set_writable()

#Start server
server.start()
print("Server has started at: {}".format(url))

# Set values as random, or use an own logic for setting the values

while True:
    Temperature =randint(10, 50)
    Pressure = randint(200, 999)
    Time = datetime.datetime.now()
    
    print(Temperature, Pressure, Time)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    T.set_value(Time)


    #Set a delay to two seconds, note: This one does not use ms as a standard format
    time.sleep(2)




