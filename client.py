__author__ = 'liuzhigang'
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.137.1',8888))
while True:
    time.sleep(3)
    s.send("hello")
    print s.recv(1024)
s.close