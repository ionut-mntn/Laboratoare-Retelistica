import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("0.0.0.0", 7777))

buff, addr = s.recvfrom(105)

print "Am primit de la client numarul: ", buff

s.sendto(str(28 + int(buff)), addr)
