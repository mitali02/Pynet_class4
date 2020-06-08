from netmiko import ConnectHandler

cisco4 = {
    'host' : 'cisco4.lasthop.io',
   # 'snmp_port' : '161',
   # 'ssh_port' : '22',
    'username' : 'pyclass',
    'password' : '88newclass',
    'device_type' : 'cisco_ios',
}

cisco3 = {
    'host' : 'cisco3.lasthop.io',
    'username' : 'pyclass',
    'password' : '88newclass',
    'device_type' : 'cisco_ios',
}

nxos1 = {
    'host' : 'nxos1.lasthop.io',
    'username' : 'pyclass',
    'password' : '88newclass',
    'device_type' : 'cisco_nxos',
    "global_delay_factor": 2,
}

srx2 = {
    'host' : 'srx2.lasthop.io',
    'username' : 'pyclass',
    'password' : '88newclass',
    'device_type' : 'juniper',
}
#devices = [cisco3,cisco4,nxos1,srx2]

devices = [nxos1]

for i in (devices):
    net_connect = ConnectHandler(**i)

    net_connect2 = net_connect.find_prompt()
    print (net_connect2)

    net_connect3 = net_connect.send_command("show clock")
    print (net_connect3)

    net_connect2 = net_connect.send_command("show lldp neighbor")

    output = net_connect.send_command('show clock')
    print (output)
    
    print ('######################################')
    net_connect3 = net_connect.send_command("show clock")
    print (net_connect3)

    net_connect2 = net_connect.send_command("show lldp neighbor",delay_factor = 16)

    output = net_connect.send_command('show clock')
    print (output)
    net_connect.disconnect()

#print (net_connect3)

 
