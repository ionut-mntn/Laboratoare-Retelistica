import socket
import time
from threading import Thread


def f(cs, i):
	print "Procesez client" + str(i)
	b = cs.recv(105)
	print b
	time.sleep(10) # ??? ce e cu sleep-ul asta aici ???
	cs.send(str(i))
#	inp = raw_input()
#	print "Am preluat input-ul de la clientul" + str(i)
	print "Finalizare client" + str(i)
	cs.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)

i = 0
while True:
	i = i + 1
	cs, addr = s.accept()
	# thread t(target = f, args=cs,i)
	t = Thread(target=f, args=(cs,i)) # ce e cu virgula asta aici?
	t.start()
#	cs.close() # asta nu mai aici? NU! Se inchide in thread !
