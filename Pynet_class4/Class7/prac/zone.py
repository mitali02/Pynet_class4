import xmltodict
from pprint import pprint
xmlfile = open("show_security_zones.xml")
xmldata = xmlfile.read()

print(xmldata)

myxml = xmltodict.parse(xmldata)
print(myxml)
pprint(myxml.keys())
pprint(myxml.values())
#pprint(myxml.len())
zones = myxml["zones-information"]["zones-security"]
for index, zone in enumerate(zones):
    print(f"Security Zone #{index + 1}: {zone['zones-security-zonename']}")
print("\n\n")
for i in myxml['zones-information']['zones-security']:
    pprint(i['zones-security-zonename'])
#pprint(myxml['software-information'].keys())
#pprint(myxml['software-information'].values())

#print ("Juniper version is %s" %myxml['software-information']['package-information']['comment'])
