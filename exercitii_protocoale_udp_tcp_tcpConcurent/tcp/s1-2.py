import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)

cs, addr = s.accept() #fara parametru

buff = cs.recv(10)

##cs.sendto(str(len(buff))) # "send", nu "sendto"!!!

print "Am primit de la client: ", buff

cs.send(str(len(buff)))

cs.close()
