from jinja2 import Template

filename = "bgp_config.j2"

with open(filename) as f:
    bgp_config = f.read()
bgp_var = {
    "local_as" : "10",
    "peer1_ip" : "10.1.20.2" ,
    "peer1_as" : "20", 
    "peer2_ip" : "10.1.30.2",
    "peer2_as" : "30",
}
j2_template = Template(bgp_config)
output = j2_template.render(**bgp_var)
#output = j2_template.render(local_as = 10, peer1_ip = "10.1.20.2" , peer1_as= 20, peer2_ip = "10.1.30.2", peer2_as = 30)
print(output)
