import datetime
import socket

def bwcs():
	HOST = raw_input("Server Adress: ")
	PORT = 50000
	BUFFER = 4096

	testdata = b'x' * BUFFER * 4

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST,PORT))
	for i in range(1, 1000000):
		sock.send(testdata)
		sock.close()
