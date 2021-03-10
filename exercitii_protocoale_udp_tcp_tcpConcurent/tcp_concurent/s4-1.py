import socket

from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def f(cs, addr, i): # client_socket-ul, adresa clientului si nr de ordine al clientului
	print "Incep sa tratez clientul ", addr, " cu nr de ordine ", i
	buff = cs.recv(105)
	dict_cifre = { 1: "una", 2: "doua", 3: "trei", 4: "patru", 5:"cinci", 6:"sase", 7:"sapte",
	8: "opt", 9:"noua" }
	# dict_cifre_unitati =

	numar_citit =""
	buff = [int(elem) for elem in buff]
	for cifra in buff:
		if cifra is not 0:
			numar_citit = numar_citit + dict_cifre.get(cifra)

s.bind(("0.0.0.0", 7777))
s.listen(5)

i = 0
while True:
	i = i + 1

	cs, addr = s.accept()
	t = Thread(target = f, args=(cs, addr, i)
	t.start()
