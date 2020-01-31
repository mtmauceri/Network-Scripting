from napalm import get_network_driver
from netmiko import ConnectHandler
import json
from getpass import getpass


driver = get_network_driver('ios')


#with open('commands_file') as f:
#    commands_list = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()



for f in devices_list:
  currentline = f.split(",")
  multiple_devices = (raw_input('What combinatin of devices would you like to do 1, 2, 3: '))
  
  list_devices = []
  for select_devices in multiple_devices:
    if multiple_devices == '1':
      ip_address_of_device=list_devices.append('1')

    elif multiple_devices == '2' :
      ip_address_of_device=list_devices.append('1')
      

    elif multiple_devices == '3' :
      ip_address_of_device=list_devices.append('1')
   


username = (raw_input('Enter your username here: '))

password = getpass()

for devices in devices_list:
  print 'Connecting to device ' + devices
  ip_address_of_device = devices
  ios_device = {
    'device_type': 'cisco_ios',
    'ip': ip_address_of_device,
    'username': username,
    'password' : password
}



iosvl2 = driver((ip_address_of_device), (username), (password))
iosvl2.open()


which_options = (raw_input('Press 1 to use vlan scripts and 2 to use show commands: '))   #unsure how to run it back to here
for devices in which_options:

    if which_options == '1':


        net_connect = ConnectHandler(**ios_device)

        vlan_number =int(raw_input('How many vlans would you like to make: '))


####Vlan options
        for n in range(int(vlan_number)):
           print 'Creating VLAN ' + str(n)
           config_commands = ['vlan ' + str(n), 'name VLAN ' + str(n)]
           configuration = net_connect.send_config_set(config_commands)
           print configuration
       # output= net_connect.send_command('show vlan br')
       # print output




    if which_options == '2':

        option=(raw_input( 'Type 1 for Environment, 2 for Interfaces, 3 for Mac Table, 4 for arp table, 5 to see users: '))

        for which_options in option:
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
