from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

#env = Environment(undefined=StrictUndefined)
env = Environment()
env.loader = FileSystemLoader([".", "./templates/"])

int_list = []
for intf in range(1,24):
    int_name = f"GigEther1/1/{intf}"
    int_list.append(int_name)

print (int_list)
intf_var = {
    "int_list" : int_list
}


template_filename = "intf3.j2"
j2_template = env.get_template(template_filename)
output = j2_template.render(**intf_var)
#output = j2_template.render(local_as = 10, peer1_ip = "10.1.20.2" , peer1_as= 20, peer2_ip = "10.1.30.2", peer2_as = 30)
print(output)
