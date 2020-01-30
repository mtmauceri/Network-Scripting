from napalm import get_network_driver
import json


driver = get_network_driver('ios')


device_connection = (raw_input('Type 1 for E-1, 2 for E-2, 3 for E-3: '))
for devices in device_connection:
        if device_connection == "1":
            ip = '192.168.244.209'

        if device_connection == "2":
            ip = '192.168.244.208'

        if device_connection == "3":
            ip = '192.168.244.210'

        else:
            break
iosvl2 = driver((ip), 'cisco', 'cisco')
iosvl2.open()

option=(raw_input( 'Type 1 for Environment, 2 for Interfaces, 3 for Mac Table, 4 for arp table, 5 to see users: '))
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

#returns the arp table
    if option == "4":
        ios_output = iosvl2.get_arp_table()
        print(json.dumps(ios_output, indent=4))
#returns the lldp neighbors
    if option == "5":
        ios_output = iosvl2.get_users()
        print(json.dumps(ios_output, indent=4))

    else:
        print'That was not an option'
