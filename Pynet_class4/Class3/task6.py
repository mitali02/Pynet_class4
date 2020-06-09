from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

cisco4 = {
    'host' : 'cisco4.lasthop.io',
   # 'snmp_port' : '161',
   # 'ssh_port' : '22',
    'username' : 'pyclass',
    'password' : '',
    'device_type' : 'cisco_ios',
    'session_log' : 'cisco4_show_run.txt'
}

net_connect = ConnectHandler(**cisco4)

net_connect_output = net_connect.send_command("show run")
#print(net_connect_output)
net_connect.disconnect()

cisco_obj = CiscoConfParse(session_log)
interface = cisco_obj.find_objects_w_child(parentspec=r"^interface",childspec = r"^ip address")
print(interface)
#net_connect.disconnect()
