import socket


ENC = 'utf-8'
HOST = '127.0.0.1'
PORT = '5454'

with socket.create_connection((HOST, PORT)) as s:
	data = s.recv(1024)
	print(data.decode(ENC))
	
	message = input("Please enter your message here:")
	s.sendall(message.encode(ENC))
