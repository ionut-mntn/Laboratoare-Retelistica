import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

s.send(" ".join(sys.argv[1:]))

print "Am primit de la server: ", s.recv(105)

s.close()
