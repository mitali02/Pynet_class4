from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

a_device = Device(host="srx2.lasthop.io", user="pyclass", password="88newclass")
a_device.open()
pprint(a_device.facts['serialnumber'])