import socket

target_host = 'localhost'
target_port = 99

try:
	print '[client]: Connecting to %s:%d' % (target_host, target_port)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((target_host, target_port))
	print '[client]: Connection Succesful.'
except Exception as e:
	print '[client]: Error connecting - ' + str(e)

data = 'Testing. Hello World!'

print '[client]: Sending data: %s' % (data,)

try:
	client.send(data)
	print '[client]: Data sent.'
except Exception as e:
	print '[client]: Error sending data - ' + str(e)

print '[client]: Response from %s' % (target_host,)

response = client.recv(4096)

print response
