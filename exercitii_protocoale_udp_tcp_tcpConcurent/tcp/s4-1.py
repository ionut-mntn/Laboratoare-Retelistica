import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
cs, addr = s.accept()

buff = cs.recv(105)
print "Am primit de la clientul cu portul", addr[1], " string-ul: ", buff # addr e un tuple!!

cs.send( str( sum( [ int(char) for char in str(addr[1]) ] ) ) )

cs.close()
