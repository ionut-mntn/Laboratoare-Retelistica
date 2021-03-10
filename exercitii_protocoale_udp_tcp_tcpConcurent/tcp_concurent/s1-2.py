import socket
import time
from threading import Thread

def f(cs, i):
	print "Tratez clientul ", i

	b = cs.recv(105)
	print "fac ceva pe aicea cu ce am primit:", b

	cs.send("ceva") # trimit ceva inapoi
	cs.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
i = 0
while True:
	i = i + 1
	cs, addr = s.accept()
	t = Thread(target = f, args=(cs, i)) # s ar putea sa mai trebuiasca o virgula aici
	t.start() # close-ul la socket-ul clientului il facem
	
