import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 7777)) # loopback

s.send("cuvant")

buff = s.recv(105)

print "Lungimea este:"
print buff
