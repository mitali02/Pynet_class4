from netmiko import ConnectHandler

cisco4 = {
    'host' : 'cisco4.lasthop.io',
   # 'snmp_port' : '161',
   # 'ssh_port' : '22',
    'username' : 'pyclass',
    'password' : '',
    'device_type' : 'cisco_ios',
}

net_connect = ConnectHandler(**cisco4)

net_connect2 = net_connect.find_prompt()
print (net_connect2)

net_connect3 = net_connect.send_command("show clock")
print (net_connect3)

output = net_connect.send_command('show version')
print (output)
#net_connect.disconnect()

#print (net_connect3)

 
