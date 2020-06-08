from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

#env = Environment(undefined=StrictUndefined)
env = Environment()
env.loader = FileSystemLoader([".", "./templates/"])

intf_var = {}


template_filename = "intf2.j2"
j2_template = env.get_template(template_filename)
output = j2_template.render(**intf_var)
#output = j2_template.render(local_as = 10, peer1_ip = "10.1.20.2" , peer1_as= 20, peer2_ip = "10.1.30.2", peer2_as = 30)
print(output)
