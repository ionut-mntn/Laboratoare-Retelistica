import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 7777))

s.send(" ".join(sys.argv[1:])) # nu mai precizez unde pentru ca e tcp, conexiune mai rezistenta

buff = s.recv(105)

print "Serverul imi spune ca sunt ", buff, " vocale in string-ul pasat"

s.close()
