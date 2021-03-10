import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

s.send(" ".join(sys.argv[1:]))

buff = s.recv(105)
print "Serverul spune ca in string-ul trimis sunt ", buff, " consoane."
# obs: vad ca a mers si fara sa inchid socketul !!
# dar il voi inchide, totusi
s.close()
