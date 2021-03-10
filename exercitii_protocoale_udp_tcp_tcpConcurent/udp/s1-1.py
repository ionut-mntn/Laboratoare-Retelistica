# udp bind cu sendto(addr)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("0.0.0.0", 5555)) # oricine poatre trimite la adresa mea ip, in portul 5555
buff, addr = s.recvfrom(105)

print("Am primit de la client litera:", buff)
#print(buff)

s.sendto(2 * buff, addr) # socket-ul primeste din toate partile, dar trebuie sa stie unde trimite!
s.sendto("ceva", addr)
