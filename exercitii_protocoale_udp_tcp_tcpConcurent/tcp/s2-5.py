import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 7777))
s.listen(5)
cs, addr = s.accept()

buff = cs.recv(105)
print "Am primit de la clientul: ", addr, " string-ul: ", buff

vocale = 'aeiouAEIOU'
# buff = buff.split()
cs.send( max(buff.split(), key = lambda cuv: len( [letter for letter in cuv if letter not in vocale] )) )
#cs. send( max(buff.split(), key = sum( lambda letter: letter not in vocale ) ) )
# sau mai multe variante aici.. cu map cu sum
cs.close()
