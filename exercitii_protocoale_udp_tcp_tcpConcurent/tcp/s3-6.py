import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
cs, addr = s.accept()

buff = cs.recv(105)
print "Am primit de la clientul ", addr, " string-ul: ", buff

cs.send( str(sum(map(lambda x: int(x), buff.split()))) ) # nu exista double in python!

cs.close()
