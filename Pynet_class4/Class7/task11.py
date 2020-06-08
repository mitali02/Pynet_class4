from lxml import etree
myxml = open("show_security_zones.xml")
xmldata = myxml.read()
#print(xmldata)
data = etree.parse(xmldata)
print(data)
print(data.getroot())
xmdata = etree.fromstring(data)

print (xmldata)

#print(#######################)
with open("show_security_zones.xml", "r") as infile:
    # Parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

print(show_security_zones)
print(type(show_security_zones))
print(show_security_zones.tag)
print(show_security_zones.getroot)
