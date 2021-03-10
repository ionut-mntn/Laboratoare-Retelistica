import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
s.bind(("0.0.0.0", 7777))
s.listen(5)
cs, addr = s.accept()

buff = cs.recv(105)

print "Serverul a primit de la clientul ", addr, " : ", buff

#def nr_vocale(s):
#	vocale = 'aeiouAEIOU'
#	nr = 0
#	for char in s:
#		if char in vocale:
#			nr = nr + 1
#	return nr

#cs.send(max(buff.split(), key = nr_vocale))

vocale = 'aeiouAEIOU'
lista_cuvinte = buff.split()
cuvant_retinut = ""
maxx = 0
for cuvant in lista_cuvinte:
	nr = 0
	for caracter in cuvant:
		if caracter in vocale:
#			nr++
			nr = nr + 1
	print cuvant, " ", nr
	if nr > maxx:
		cuvant_retinut = cuvant
		maxx = nr
		print cuvant, "--NOU"
if cuvant_retinut == "" :
	print "Eroare... niciun cuvant detectat"
else:
	cs.send(cuvant_retinut)
cs.close()
