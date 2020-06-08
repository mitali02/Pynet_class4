from netmiko import ConnectHandler
nxos1 = {
    'host' : 'nxos1.lasthop.io',
   # ssh_port = 22
   # nxapi_port = 8443
    'username' : 'pyclass',
    'password' : '88newclass',
    'device_type' : 'cisco_nxos'
}

print (nxos1)
print (type(nxos1))

net_connect = ConnectHandler(
        host = 'nxos1.lasthop.io',                                          
        username = 'pyclass',                                               
        password = '88newclass',                                           
        device_type ='cisco_nxos',
        session_log = 'nxos1.txt'
)

print(net_connect.find_prompt())

