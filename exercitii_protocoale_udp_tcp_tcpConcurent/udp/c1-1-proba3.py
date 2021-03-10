import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("ceva", ("127.0.0.1", 6666))
s.sendto("ceva2", ("127.0.0.1", 7777))
