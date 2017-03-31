"""
	Python Solver - Client 
	AJINKYA PADWAD
	MARCH 2017
"""
# No Exception Handling !

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

Length = 82
MsgID = 3
Rules = 1
Physical = 0
Transmitters = 2
SensorPort = 7007
Mask = 0xffffffffffffffff

SubscriptionMessage = (Length, MsgID, Rules, Physical, Transmitters, 0,SensorPort, Mask , Mask, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, Mask, Mask, 0)

Wrapper2 = struct.Struct('!'+'I B I b I 2Q 2Q 16B 2Q Q')
Packet2 = Wrapper2.pack(*SubscriptionMessage)

print " Subscription request message sent. "

NewSocket.sendall(Packet2)


data = NewSocket.recv(90)
print " Got Subscription Response :	", data

print""
print" Subscription complete !"
#time.sleep(2)

# ----------------------------- EXTRACT SAMPLES ---------------

Wrapper3 = struct.Struct('!'+'I B B 16B 16B Q f 2B')
i=0
while 1:
	time.sleep(1)
	data = NewSocket.recv(52)
	#print " Got :	", data
	SensorData = Wrapper3.unpack(data)

	print " Sample ", i, " : ", SensorData
	i=i+1

# --------------------------------- END ----------------------
