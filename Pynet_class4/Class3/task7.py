from ciscoconfparse import CiscoConfParse
from pprint import pprint

bgpconfig = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out

"""

pprint(bgpconfig)

bgp = CiscoConfParse(bgpconfig.splitlines())
pprint(bgp)

#bgp_find = bgp.find_objects(parentspec = r"^neighbor", childpsec = r"^remote-as")
bgp_find = bgp.find_objects_w_child(parentspec = r"^router bgp", childspec = r"^\s+neighbor")
print(bgp_find)
print(bgp_find[0])
print(bgp_find[1])
print(bgp_find[0].text)  
ip = []
for i in range(0,len(bgp_find)):
    print(bgp_find[i].text)
    neighbor_ip = bgp_find[i].text
#    ip =i neighbor_ip.find(r"neighbor \D+")
    ip_detail = neighbor_ip.strip('neighbor ') 
    ip.append(ip_detail)
print(ip)
print(bgp_find[0].text.children())
#print(bgp_find[0].parent())
