from netmiko import ConnectHandler

cisco3 = {
    'host' : 'cisco3.lasthop.io',
   # 'snmp_port' : '161',
   # 'ssh_port' : '22',
    'username' : 'pyclass',
    'password' : '',
    'device_type' : 'cisco_ios',
    'session_log' : 'cisco3_show_run.txt'

}

net_connect = ConnectHandler(**cisco3)

net_connect2 = net_connect.find_prompt()
print (net_connect2)

net_connect3 = net_connect.send_command("show run")
print (net_connect3)
net_connect.disconnect()

