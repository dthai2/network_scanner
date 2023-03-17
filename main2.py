import nmap

# Initialize the nmap scanner
nm = nmap.PortScanner()

# Define the IP range to scan
ip_range = "192.168.1.1-255"

# Scan the network and store the results
nm.scan(hosts=ip_range, arguments="-O -sV")

# Print the scan results
for host in nm.all_hosts():
    print "----------------------------------------------------"
    print "Host: %s (%s)" % (host, nm[host].hostname())
    print "State: %s" % nm[host].state()

    # Print the operating system information
    if 'osmatch' in nm[host]:
        for osmatch in nm[host]['osmatch']:
            print "OS Match: %s (%s%%)" % (osmatch['name'], osmatch['accuracy'])

    # Print the open ports and services
    for proto in nm[host].all_protocols():
        print "Protocol: %s" % proto

        lport = list(nm[host][proto].keys())
        lport.sort()

        for port in lport:
            print "Port: %s\tService: %s" % (port, nm[host][proto][port]['name'])
