# socketul e ca un mailbox!! eu poate nu stiu ce am primit, dar vad pe geam ca a venit postasul
# si mi-a lasat ceva in posta si ma duc la cutia postala si vad acolo ce si de la cine am primit

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 7777))

buff, addr = s.recvfrom(105)

print buff, addr

s.sendto("ceva de la server", addr)
