import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

s.send(sys.argv[1])

print s.recv(10)
s.close()
