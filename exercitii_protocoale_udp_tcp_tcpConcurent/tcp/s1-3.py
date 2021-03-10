import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
cs, addr = s.accept()
###s.listen(5) !!!! NU !!! INTAI ASCULT, APOI ACCEPT CONEXIUNI!!
####cs, addr = s.connect() !!! NU!!! LISTEN ERA	!!

buff = cs.recv(105)
print "Am primit de la", addr, buff

vocale = 'aeiouAEIOU'

nr = 0
for char in buff:
	if char in vocale:
		nr = nr + 1

cs.send(str(nr)) ## atentie!!!!!! eu trimit pe client socket !!!

cs.close() ### si inchid client socket ul !!!!!!
