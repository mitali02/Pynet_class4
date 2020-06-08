from netmiko import ConnectHandler

cisco4 = {
    'host' : 'cisco4.lasthop.io',
   # 'snmp_port' : '161',
   # 'ssh_port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',
    'device_type' : 'cisco_ios',
    'session_log' : 'task4.txt',
     'fast_cli' : 'True',
}


net_connect = ConnectHandler(**cisco4)

net_connect2 = net_connect.find_prompt()
print (net_connect2)

set = ["ip name-server 1.1.1.1","ip name-server 1.1.0.1","ip domain-lookup"]
net_connect3 = net_connect.send_config_set(set)

print (net_connect3)

output = net_connect.send_command('ping www.google.com')
print (output)

net_connect3 = net_connect.save_config()

net_connect.disconnect()

#print (net_connect3)

 
