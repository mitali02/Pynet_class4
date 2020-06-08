arp_data = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

#print(arp_data)
#print(type(arp_data))

arp_data = arp_data.splitlines()

#print(arp_data)
#print(type(arp_data))

arp_data = arp_data[2:len(arp_data)]

#print(arp_data)
#print(type(arp_data))
#print(len(arp_data))

final_list = []
for i in arp_data:
 #   print (i)
    x = i.split()
  #  print (x) 
    mac_addr = x[3]
    ip_addr= x[1]
    interface = x[5]
    dict = {
       "MAC" : mac_addr,
       "IP" : ip_addr,
        "INT" : interface,
    }
    final_list.append(dict)

print (final_list)
