from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

#env = Environment(undefined=StrictUndefined)
env = Environment()
env.loader = FileSystemLoader([".", "./templates/"])

vrf_var = {
    "vrf_name" : "blue",
    "Route_Distinguisher" : "100:1" ,
    "ipv4_af" : False,
    "ipv6_af" : False, 
}


template_filename = "vrf.j2"
j2_template = env.get_template(template_filename)
output = j2_template.render(**vrf_var)
#output = j2_template.render(local_as = 10, peer1_ip = "10.1.20.2" , peer1_as= 20, peer2_ip = "10.1.30.2", peer2_as = 30)
print(output)
