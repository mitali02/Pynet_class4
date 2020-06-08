import ipdb
from ncclient import manager
from pprint import pprint
from ncclient.xml_ import new_ele

conn = manager.connect(
    host = "srx2.lasthop.io",
    #host = "cisco3.lasthop.io",
    port = 830,
    username = "pyclass",
    password = "88newclass",
    device_params = {"name" : "csr"},
    hostkey_verify = False,
    allow_agent = False,
    look_for_keys = False,
    timeout =60,
) 

ipdb.set_trace()
config = conn.get_config(source="running")
config_xml = config.data_xml
pprint(config_xml)

#    pprint(netconf_manager.server_capabilities.__dict__)
