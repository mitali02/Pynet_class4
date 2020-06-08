import json

from pprint import pprint

#filename = input("Input filename: ")
filename = "nap.json"
with open(filename) as f:
    data = json.load(f)
pprint(data)

#pprint(type(data))
#pprint(len(data))
#pprint(data.keys())
#pprint(type(data.keys()))
#pprint(data.values())

output = data.values()

pprint(output)
pprint(type(output))
pprint(len(output))
#pprint(output[0].items())
#for i range(0,len(output)):
#    x1 = output['ipv4'].values()
#print(x1)



#    pprint(data[i].keys)
#    pprint(data[i].values)
