import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
cs, addr = s.accept()

buff = cs.recv(105)
print "Am primit de la clientul ", addr, " string-ul: ", buff

for elem in buff.split():
	print elem

###minn = buff.split()[0]
#minn = filter(lambda x: x if x < minn, buff.split())
###minn = filter(lambda x: x < minn, buff.split())

###print "minn este:", minn

print(buff.split())
print "min=", min( buff.split() )


cs.send( str( max([float(x) for x in buff.split()]) )) # nu exista double in python!
# cred ca le compara lexicografic aici !!!

cs.close()
