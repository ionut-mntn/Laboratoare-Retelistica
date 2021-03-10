import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

print " Introuceti numerele, urmate de tasta enter. Daca ati terminat, apasati enter fara a mai introduce vreun numar."

lista = []
inp = raw_input()
while inp != '':
	lista.append(inp)
	inp = raw_input()

s.send(" ".join(lista))

s.close()
