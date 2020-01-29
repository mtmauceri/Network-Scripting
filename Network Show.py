from napalm import get_network_driver
import json


driver = get_network_driver('ios')
iosvl2 = driver('192.168.244.210', 'cisco', 'cisco')
iosvl2.open()

option=(raw_input( 'Type 1 for Environment, 2 for Interfaces, 3 for Mac Table: '))
for devices in option:
#used to return uptime,vendor,model...exc
    if option =="1":
        ios_output = iosvl2.get_environment()
        print (json.dumps(ios_output, indent=4))

#returns if interface is up ,description,speed , and mac
    if option == "2":
        ios_output = iosvl2.get_interfaces()
        print (json.dumps(ios_output, indent=4))

#returns mac address table
    if option == "3":
        ios_output = iosvl2.get_mac_address_table()
        print (json.dumps(ios_output, indent=4))

    else:
        break
