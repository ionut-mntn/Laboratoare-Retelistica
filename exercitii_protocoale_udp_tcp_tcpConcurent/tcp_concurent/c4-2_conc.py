import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

inp = input("Introduceti numarul de trimis server-ului:")

s.send(str(inp))

buff = s.recv(105)
print "Am primit de la server: ", buff

s.close()
