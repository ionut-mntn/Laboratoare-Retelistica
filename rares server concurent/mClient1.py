import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7778))
s.send("Salut, sunt clientul 1")
print s.recv(10)
s.close()
