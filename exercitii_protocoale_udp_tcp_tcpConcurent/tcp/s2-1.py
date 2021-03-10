import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 7777))
s.listen(5)
cs, addr = s.accept()

buff = cs.recv(105)
#print type(buff)
print "Am primit de la clientul ", addr, " lista de cuvinte: ", buff

# print "CEVA".join(buff) # eu asa ii pasam un string ceea ce nu era bine pentru ca cred ca
# .split() lucreaza pe obiecte iterabile, iar un string este iterabil caracter cu caracter!
# deci trebuia sa transform string-ul primit de la client intr-o lista, pe care apoi sa fac .split()
print "CEVA".join(buff.split())

#### cs.sendto("".join(buff)) # nu e sendto!!! e send!!!
cs.send( "".join( buff.split() ) )

cs.close() # buuuuuuuuuuuuun... am inchis din prima aici
