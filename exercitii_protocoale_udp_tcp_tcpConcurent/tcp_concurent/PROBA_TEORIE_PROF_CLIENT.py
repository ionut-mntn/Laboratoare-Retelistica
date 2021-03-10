import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

##################################s.send("Baga mare bro")

lista = []
inp = raw_input()

#while inp is not None:
while inp:
	lista.append(inp)
	inp = raw_input()

# ATENTIE! SA NU UITAM DE s.close() !!
s.close()
