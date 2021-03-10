import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777)) # "0.0.0.0" aiciiii!!!
s.listen(5)
cs, addr = s.accept()

buff = cs.recv(105)

print "Am primit de la ", addr, " string-ul:", buff

cs.send( max(buff.split(), key=len) )

cs.close()
