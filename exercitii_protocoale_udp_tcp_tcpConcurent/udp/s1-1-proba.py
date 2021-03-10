import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("0.0.0.0", 5555)) # oricine poatre trimite la adresa mea ip, in portul 5555

buff, addr = s.recvfrom(105)
buff2, addr2 = s.recvfrom(105)
#CONCLUZIE!! DECI POT PRIMI PRIN ACELASI SOCKET DIN MAI MULTE PARTI!!


print("Am primit de la client ", addr, " litera: ", buff)
print("Am primit de la client litera:", addr2, " litera: ", buff2)

#print(buff)

s.sendto(2 * buff, addr) # socket-ul primeste din toate partile, dar trebuie sa stie unde trimite!
s.sendto(2 * buff2, addr2)
