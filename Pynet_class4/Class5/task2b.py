from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

nxos1_var = {
    "port" : "1/1",
    "ip" : "10.1.100.1" ,
    "mask" : "24", 
    "local_as" : "22",
    "peer_ip" : "10.1.100.2",
}

nxos2_var = {
    "port" : "1/1",
    "ip" : "10.1.100.2" ,
    "mask" : "24",
    "local_as" : "22",
    "peer_ip" : "10.1.100.1",
}
template_filename = "nxos.j2"
j2_template = env.get_template(template_filename)
output = j2_template.render(**nxos1_var)
#output = j2_template.render(local_as = 10, peer1_ip = "10.1.20.2" , peer1_as= 20, peer2_ip = "10.1.30.2", peer2_as = 30)
print(output)

output2 = j2_template.render(**nxos2_var)
print(output2)

