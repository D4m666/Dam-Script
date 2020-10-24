import nmap


def rhost():
# ask user the target
	target = raw_input("\nTarget IP: ")
	target_ports = raw_input("Target PORTS(x-y): ")

# initialize the port scanner
	nmScan = nmap.PortScanner()

# scan localhost for ports in range 21-443
	nmScan.scan(target, target_ports)

# run a loop to print all the found result about the ports
	for host in nmScan.all_hosts():
		print("\n--------------------")
		print('Host : %s (%s)' % (host, nmScan[host].hostname()))
		print('State : %s' % nmScan[host].state())
		for proto in nmScan[host].all_protocols():
			print('\n----------')
			print('Protocol : %s' % proto)
 
			lport = nmScan[host][proto].keys()
			lport.sort()
			for port in lport:
				print ('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))

