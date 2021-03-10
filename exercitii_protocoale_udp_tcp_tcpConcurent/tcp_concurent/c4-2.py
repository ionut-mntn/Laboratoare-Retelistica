import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

inp = input("Introduceti un numar si apasati enter: ") # raw_input

s.sendto(str(inp), ("127.0.0.1", 7777))

buff, addr = s.recvfrom(105)

print "Am primit de la server: ", buff
