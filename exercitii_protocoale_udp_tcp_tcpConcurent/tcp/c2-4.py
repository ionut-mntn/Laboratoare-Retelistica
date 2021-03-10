import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777)) # 127.0.0.1 -> loopback

s.send( " ".join(sys.argv[1:]) )

buff = s.recv(105)

print "Clientul a primit de la server: ", buff

s.close()
