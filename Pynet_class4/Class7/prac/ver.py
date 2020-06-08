import xmltodict
from pprint import pprint
xmlfile = open("show_ver.xml")
xmldata = xmlfile.read()

print(xmldata)

myxml = xmltodict.parse(xmldata)
print(myxml)
pprint(myxml.keys())
pprint(myxml.values())
pprint(myxml['software-information'])
pprint(myxml['software-information'].keys())
pprint(myxml['software-information'].values())

print ("Juniper version is %s" %myxml['software-information']['package-information']['comment'])
