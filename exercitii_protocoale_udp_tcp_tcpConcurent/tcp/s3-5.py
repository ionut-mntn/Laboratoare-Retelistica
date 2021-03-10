import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
cs, addr = s.accept()

buff = cs.recv(105)
print "Am primit de la clientul ", addr, " string-ul: ", buff

buff = buff.split()
cs.send( str( min( float(buff[0]), float(buff[1])) ) ) # nu exista double in python!

cs.close()
