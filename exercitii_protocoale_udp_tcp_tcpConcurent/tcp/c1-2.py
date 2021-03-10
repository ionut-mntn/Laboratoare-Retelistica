import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP

s.connect(("127.0.0.1",7777))

#s.sendto(sys.argv[1])

s.send(sys.argv[1])

b = s.recv(10)

print "Serverul mi-a spus ca lungimea cuvantului este:", b

s.close()
