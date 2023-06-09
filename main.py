#!usr/bin/python3
import socket
import subprocess

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

#subnet
last_dot = ip_address.rfind('.')
network_addr = ip_address[:last_dot] + '.0'
subnet = network_addr + '/24'

#print("Hostname:" + hostname)
#print("IP address:" + ip_address)
#print("subnet:" + subnet)

# define the nmap command to scan the network
cmd = ['nmap', '-sP', subnet]

# execute the nmap command and capture the output
output = subprocess.check_output(cmd)

# parse the output to extract device information
#print(output)
devices = [] #creating list of devices on the network
for line in output.splitlines():
    line = line.decode('utf-8')
    #print(line)
    if 'Nmap scan report for' in line:
        print('\n')
        device = {} #new device found
        tempLine = line.split()
        if len(tempLine) == 6: #host name found
            device['ip_address'] = line.split()[5]
            device['hostname'] = line.split()[4]
        else:
            device['ip_address'] = line.split()[4]
            device['hostname'] = "Unknown Host" #socket.gethostbyaddr('192.168.1.1')
        print('IP Address: ' + device['ip_address'])
        print('Hostname: ' + device['hostname'])
        devices.append(device)
    elif 'MAC Address' in line:
        device['mac_address'] = line.split()[2]
        print('MAC Address: ' + device['mac_address'])
        #print(device['mac_address'])
    elif 'OS details' in line:
        device['operating_system'] = line.split(':')[1].strip()
        print('Operating System: ', device.get('operating_system', 'Unknown'))
    elif 'open' in line:
        port = line.split()[0]
        service = line.split()[2]
        device['ports'] = device.get('ports', [])
        device['ports'].append((port, service))
        if device.get('ports', []): #only prints if device has an open por
            print('Open Ports:')
            for port, service in device.get('ports', []):
                #print(f"\t{port}/{service}")
                print('\t{}/{}'.format(port, service))
   
'''
# print the device information
for device in devices:
    print('IP Address: ' + device['ip_address'])
    print('Hostname: ' + device['hostname'])
    #print('MAC Address: ' + device['mac_address'])
    print(device['mac_address'])
    print('Operating System: ', device.get('operating_system', 'Unknown'))
    if device.get('ports', []): #only prints if device has an open por
        print('Open Ports:')
        for port, service in device.get('ports', []):
            #print(f"\t{port}/{service}")
            print('\t{}/{}'.format(port, service))
    print("\n") '''