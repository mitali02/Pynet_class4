from netmiko import ConnectHandler
import os

cisco4 = {
    'host' : 'cisco4.lasthop.io',
   # 'snmp_port' : '161',
   # 'ssh_port' : '22',
    'username' : 'pyclass',
    'password' : '',
    'device_type' : 'cisco_ios',
    'session_log' : 'ping_cisco4b.txt',
}

net_connect = ConnectHandler(**cisco4)

net_connect2 = net_connect.find_prompt()
print (net_connect2)

net_connect3 = net_connect.send_command_timing("ping",strip_prompt=False, strip_command=False )
print (net_connect3)

#net_connect3 = net_connect.send_command("\n",expect_string = r"Protocol [ip]:" )
net_connect3 = net_connect.send_command_timing("\n",strip_prompt=False, strip_command=False)
print (net_connect3)

net_connect4 = net_connect.send_command_timing("8.8.8.8\n")
print (net_connect4)

net_connect4 = net_connect.send_command_timing("\n")
print (net_connect4)
net_connect4 = net_connect.send_command_timing("\n")
print (net_connect4)
net_connect4 = net_connect.send_command("\n",expect_string = r"Extended commands" )
print (net_connect4)
net_connect4 = net_connect.send_command_timing("\n" )
print (net_connect4)
net_connect4 = net_connect.send_command("\n",strip_prompt=False, strip_command=False)
print (net_connect4)



#output = net_connect.send_command('show version')
#print (output)
#net_connect = net_connect4
net_connect.disconnect()

#print (net_connect3)

 
