import subprocess


		
def SSideD():
	subprocess.call('iperf -s -P 0 -i 1 -p 5001 -f k', shell=True)

def SSideC():
	PCT = raw_input('\nNumber of parallel client threads to run :')
	IS = raw_input('\nSeconds between periodic bandwidth reports :')
	Port = raw_input('\nTarget Port: ')
	Form = raw_input('\nFormat to report: Kbits(k), Mbits(m), KBytes(K), MBytes(M): ')
	subprocess.cal('iperf -s -P {} -i {} -p {} -f {}'.format(PCT, IS, Port, Form), shell=True)
	
def CSideD():
	IP = raw_input('\nTarget IP: ')
	Port = raw_input('\nTarget Port: ')
	subprocess.call('iperf -c {} -P 1 -i 1 -p {} -f M -t 10 -T 1'.format(IP, Port), shell=True)
	
def CSideC():
	IP = raw_input('\nTarget IP: ')
	Port = raw_input('\nTarget Port: ')
	PCT = raw_input('\nNumber of parallel client threads to run :')
	IS = raw_input('\nSeconds between periodic bandwidth reports :')
	time = raw_input('\nTime for the test in seconds: ')
	Form = raw_input('\nFormat to report: Kbits(k), Mbits(m), KBytes(K), MBytes(M): ')
	TTL = raw_input('\nTime-to-live, for multicast')
	subprocess.call('iperf -c {} -P {} -i {} -p {} -f {} -t {} -T {}'.format(IP, PCT, IS, Port, Form, time, TTL), shell=True)
	
	
