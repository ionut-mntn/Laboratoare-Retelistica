import socket
import sys

# print "Introduceti numele utilizatorului: " # pai asta se afiseaza abia dupa ce apelezi script-ul!

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

s.send(" ".join(sys.argv[1:]))

buff = s.recv(105)
print "Am primit de la server string-ul:\'",buff,"\' reprezentand suma cifrelor din portul de la care serverul a primit mesajul ( acest port )."

s.close()
