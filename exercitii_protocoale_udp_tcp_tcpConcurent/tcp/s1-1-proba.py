import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 7777))
s.listen(5)

cs, addr = s.accept() # cs vine de la client socket
buff = cs.recv(10) # aici dispare cuvantul `from`

cs.send(2 * buff)
cs.close()

