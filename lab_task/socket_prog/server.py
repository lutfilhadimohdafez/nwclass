import socket


ENC = 'UTF-8'
HOST = ''
PORT = 5454

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen(5)
	print(f"Server listening on {HOST}:{PORT}")

	while True:
		c, addr = s.accept()
		with c:
			print("Got connection from",addr)
			c.sendall("Thank you for connecting ._.".encode(ENC))
			# b is to encode string to byte
			
			print(c.recv(1024).decode(ENC))
			
