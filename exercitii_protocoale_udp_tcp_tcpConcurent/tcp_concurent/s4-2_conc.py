import socket
import time
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def f(cs, addr, i):
	print "Procesez clientul ", addr, " cu numarul de ordine ", i
	buff = cs.recv(105)
	# time.sleep(10)
	cs.send( str( 28 + int(buff) ) )
	print "Am terminat de procesat clientul ", i
	cs.close()

s.bind(("0.0.0.0", 7777))
s.listen(5)

i = 0
while True:

	i = i + 1
	cs, addr = s.accept()
	t = Thread(target = f, args=(cs, addr, i))
	t.start()
