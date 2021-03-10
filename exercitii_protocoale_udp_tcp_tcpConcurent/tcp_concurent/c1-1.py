import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("127.0.0.1", 7777)) # aici nu mai stiu sigur daca pot primi prin acelasi socket de la
# altcineva... de trimis prin socket-ul asta aproape sigur nu.. de testat

s.send(

