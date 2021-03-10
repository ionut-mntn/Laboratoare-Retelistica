import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777)) # in udp nu mai aveam nevoie nici macar de bind... trimiteam direct !!

s.send(" ".join(sys.argv[1:])) # le joinuiesc cu spatiu ca sa mi-l faci string si trimite-l

buff = s.recv(105)

print "Serverul zice ca cel mai lung string din lista trimisa este: ", buff

s.close() # sa nu uitam sa inchidem !!
