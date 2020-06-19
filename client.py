import asyncio
import sys
sys.path.insert(0, "..")
import logging
from asyncua import Client, Node, ua


url = "opc.tcp://localhost:4840/freeopcua/server/"

client = Client(url)

client.connect()

print("client connecterd")



while True:
    print("test")