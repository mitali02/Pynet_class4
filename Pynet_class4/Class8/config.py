from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from jnpr.junos.utils.config import Config
from getpass import getpass
from pprint import pprint

a_device = Device(host="srx2.lasthop.io", user="pyclass", password="")
a_device.open()
cfg = Config(a_device)
cfg.lock()

cfg.load("set system host-name test123", format="set", merge=True)
cfg.unlock()

