import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

s.send(" ".join(sys.argv[1:]))

b = s.recv(105)

print "Serverul imi spune ca in lista pasata sunt ", b, " cuvinte."

s.close()
