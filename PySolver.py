"""
	Python Solver - Client 
	AJINKYA PADWAD
	MARCH 2017
"""

import socket
import struct
import time


# ------------------- SETUP ------------------------------------- 

host = 'localhost'
port = 7008

NewSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

NewSocket.connect((host,port))

print " Connected to Aggregator ! "

# -------------------- HANDSHAKE ----------------------------

HandshakeMessage = (21,'GRAIL solver protocol', 0, 0)

Wrapper = struct.Struct('!'+'I 21s b b ')

Packet = Wrapper.pack(*HandshakeMessage)

print " Handshake initiated... "

data = NewSocket.recv(36)
print " Got :	", data

NewSocket.sendall(Packet)
print " Sent:	",Packet

print "Handshake complete. "

# ----------------------------- SUBSCRIPTION MESSAGE ------------------------- 

SubscriptionMessage = (82, 3, 1, 0, 2, 0,7007, 0xffffffffffffffff,0xffffffffffffffff, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, 0xffffffffffffffff,0xffffffffffffffff, 0)

Wrapper2 = struct.Struct('!'+'I B I b I 2Q 2Q 16B 2Q Q')
Packet2 = Wrapper2.pack(*SubscriptionMessage)

print " Subscription request sessage sent. "

NewSocket.sendall(Packet2)


data = NewSocket.recv(90)
#print " Got :	", data

# ----------------------------- EXTRACT SAMPLES ---------------
