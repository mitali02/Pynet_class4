import json

filename = 'task4.json'

with open(filename) as f:
     arp_data = json.load()

print (arp_data)

