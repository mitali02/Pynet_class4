from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass
from pprint import pprint

a_device = Device(host="srx2.lasthop.io", user="pyclass", password="")
a_device.open()
ports = EthPortTable(a_device)
ports.get()
pprint(ports)
pprint(ports.keys())
pprint(ports.values())

for k,v in ports.items():
    print(k)
    print( v)
