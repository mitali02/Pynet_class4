import json
from pprint import pprint 
filename = 'task4.json'

with open(filename) as f:
     arp_data = json.load(f)

pprint (arp_data)

#print (type(arp_data))

#print (arp_data.keys())

ip_info = arp_data['ipV4Neighbors']

pprint (ip_info)
new_dict = {}
#ip_info = ip_info[0]
for i in range(0,len(ip_info)):
    print(ip_info[i])
    for k,v in ip_info[i].items():
        ip = ip_info[i]['address']
        MAC = ip_info[i]['hwAddress']
#    print(ip)
#    print(MAC)
    new_dict[ip] = MAC 

pprint(new_dict)
