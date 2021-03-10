import socket
import os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",7778))
s.listen(5)
while True:
	cs,addr=s.accept()
	if os.fork() == 0:
		b=cs.recv(50)
		print b
		cs.send("Hello")
		cs.close()
		os._exit(0)
