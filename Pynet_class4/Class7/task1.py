from lxml import etree
#myxml = open("show_security_zones.xml")
#xmldata = myxml.read()
#print(xmldata)
#data = etree.parse(xmldata)
#print(data)
#print(data.getroot())
#xmdata = etree.fromstring(data)

#print (xmldata)
with open("show_security_zones.xml", "r") as infile:
    # Parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

print(show_security_zones)
print(type(show_security_zones))

print(etree.tostring(show_security_zones).decode())
print(show_security_zones.tag)
print(show_security_zones[0].tag)
print(show_security_zones.getchildren()[0].tag)
trust_zone = show_security_zones[0]
print(f"Security zone: {trust_zone[0].text}")
for child in trust_zone:
    print(child.tag)
print("\n\n")
