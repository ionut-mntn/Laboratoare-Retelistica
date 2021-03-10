import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(sys.argv[1], ("127.0.0.1", 5555))
# ATENTIE! Cred ca bind-ul care se face in server spune ca: "acest socket (sau cale de comunicare
# bidirectionala) va ramane pentru comunicarea intre aceas (ip, port) - clientul si (ip-ul, port-ul)
# serverului! "Bind" inseamna conecteaza, leaga!

buff = s.recvfrom(105)
print("Am primit de la server:")
print(buff)
