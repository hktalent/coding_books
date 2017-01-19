import socket
import sys

#input: target host ip address or hostname (string), target port (string)
#output:
#description: creates socket and connects to host:port, continuous prompts for data to be sent, and displays response to this data
def client_sender(target_host, target_port):
	try:
		print '[*] Connecting to ' + target_host + ':' + str(target_port)
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client_socket.connect((target_host, target_port))
		print '[*] Connection successful'
	except Exception as e:
		print '[!] Error connecting: ' + str(e)
		sys.exit(0)

	while True:
		print '[*] Enter data to send: '
		data_buffer = raw_input('')

		try:
			print '[*] Sending data'
			client_socket.send(data_buffer)
		except:
			print '[!] Error sending data'
			sys.exit(0)

		response = ''

		try:
			while True:
				data = client_socket.recv(4096)
				if not data:
					break
				response += data

			print '[*] Server Response:'
			print response
			print
		except:
			print '[!] Error receiving data from target'
			sys.exit(0)

#input:
#output:
#description: main functions, launches other functions based on command line input
def main():
	try:
		target_host = sys.argv[1]
		target_port = int(sys.argv[2])
	except:
		print 'Usage: tcp_client.py [targethost] [targetport]'
		sys.exit(0)

	client_sender(target_host, target_port)

if __name__ == '__main__':
	main()
