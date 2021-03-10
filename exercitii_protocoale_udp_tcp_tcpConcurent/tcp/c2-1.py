import socket
import sys # atentie !!

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777)) #atentie la paranteze

#print(sys.argv[1], sys.argv[2])
s.send(" ".join(sys.argv[1:])) # nu era bun asa pt ca "mama tata bunica era vazut ca un singur string, cred)
#s.send(" ".join(sys.argv[1:].split()))

buff = s.recv(105)
print "Serverul mi-a returnat string-ul: ", buff

s.close()
