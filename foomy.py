import socket
import time
import board
import pickle

serverIP = "192.168.1.161"
serverPort = "60001"
clientIP = None
clientPort = None

myboard = board()
myboard.set("tony")


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', serverPort))
sock.blocking(False)

while (True):
    
    try:
        (data, addr) = sock.recvfrom(65536)
    except:
        pass

    if len(data) > 0:
        print("Got it *-*")
    
    sock.sendto(pickle.dumps(myboard), ("192.168.1.179", 60001))