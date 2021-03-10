import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 7777))
s.listen(5)
cs, addr = s.accept()

buff = cs.recv(105)
print "Am primit de la clientul ", addr, " stringul: ", buff

nr = 0
vocale = 'aeiouAEIOU'
for char in buff:
	if char.isalpha() and char not in vocale: # str.isalpha() -> Return true if all characters in the 
		nr = nr + 1			  # string are alphabetic and there is at least one
						  # character, false otherwise.
cs.send(str(nr))

cs.close()
