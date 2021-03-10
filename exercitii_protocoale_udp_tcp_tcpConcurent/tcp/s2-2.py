import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
#cs, addr = s.connect() ### nu connect aicea!!
cs, addr = s.accept() # accepta conexiunea, deci vezi socketul clientului (..cred)

buff = cs.recv(105) # recv, nu "rec"
print "Am primit de la clientul ", addr, " string-ul: ", buff

cs.send( str(len( buff.split() ) ) ) # atentie la cs aici! bun.

cs.clse()


