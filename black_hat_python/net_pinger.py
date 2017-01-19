import sys
import threading
import subprocess
import netaddr
import ipaddress

#input: ip address (string)
#output: 
#description: executes ping command against an ip address, prints a message if the address is pingable
def pinger(address):
	try:
		response = subprocess.check_output('/bin/ping -c 1 ' + address, shell=True)
		print '[*] Address %s found' % address
	except Exception as e:
		pass

#input:
#output:
#description: main function, converts ip address and netmask into network object, creates threads to
#execute pings for each address in the network range
def main():
	netmask = ''
	ip_addr = ''
	
	try:
		ip_addr = sys.argv[1]
		netmask = sys.argv[2]
	except:
		print 'Usage: net_pinger.py [start IP] [netmask]'
		print
		print 'Example: net_pinger.py 10.30.6.0 255.255.255.0'
		sys.exit(0)

	try:
		netmask = netaddr.IPAddress(netmask).netmask_bits()
		network = ipaddress.ip_network(unicode(ip_addr + '/' + str(netmask)))
	except Exception as e:
		print 'Error creating network: ' + str(e)
		sys.exit(0)
	
	for addr in network:
		t = threading.Thread(target=pinger, args=(str(addr),))
		t.start()

if __name__ == '__main__':
	main()