import socket
import time
from board import *
import pickle

serverIP = "192.168.1.161"
serverPort = 60001
clientIP = None
clientPort = None

myboard = board()
myboard.set("tony")


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', serverPort))
sock.setblocking(False)

rxdata = []

while (True):

    try:
        (data, addr) = sock.recvfrom(65536)
        rxdata = data
    except:
        pass

    if len(rxdata) > 0:
        print("Got it *-*")
    
    sock.sendto(pickle.dumps(myboard), ("192.168.1.179", 60001))