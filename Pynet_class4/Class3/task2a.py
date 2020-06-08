import yaml
from pprint import pprint


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

nxos1 = {
    'host' : 'nxos1.lasthop.io',
    'username' : 'pyclass',
    'password' : 'p2p',
    'device_name' : 'nxos1',
}

srx2 = {
    'host' : 'srx2.lasthop.io',
    'username' : 'pyclass',
    'password' : 'p2p',
    'device_name' : 'srx2',
}

devices = [cisco3,cisco4,nxos1,srx2]

print (devices)

with open("my.devices.yml","w") as f:
    yaml.dump(devices,f,default_flow_style=False)
