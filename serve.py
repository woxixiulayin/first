__author__ = 'liuzhigang'
import socket
import time
import threading

def tcplink(sock, addr):
    while True:
        print sock.recv(1024)
        #print  addr
        #sock.send("I hear you")
    sock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.137.1',8888))
s.listen(5)
print "wait for connection"
#s.send("asd")
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
