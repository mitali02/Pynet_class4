import yaml

cisco4 = {
    'host' : 'cisco4.lasthop.io',
    'username' : 'pyclass',
    'password' : 'p2p',
    'device_name' : 'cisco4',
}

cisco3 = {
    'host' : 'cisco3.lasthop.io',
    'username' : 'pyclass',
    'password' : 'p2p',
    'device_name' : 'cisco3',
}

my_data = [cisco3,cisco4]

#x = list(range(10))
#my_data["x"] = x
my_data["null_value"] = None
my_data["a_bool"] = False

filename = "pracw.yml"

with open(filename,"wt") as f:
    yaml.dump(my_data,f,default_flow_style = True)
