import socket
import time
from threading import Thread

def f(cs, i): # client_socket si al catalea este acest client
	print "Procesez client" + str(i)
	buff = cs.recv(10)
	time.sleep(10)
	cs.send(str(i)) # aici cred ca ii trimit ce vreau eu
	cs.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)

i = 0
while True:
	i = i + 1
	cs, addr = s.accept()
	t = Thread(target = f, args=(cs,i))
	t.start()
