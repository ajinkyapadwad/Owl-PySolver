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

# ------------------------------------------------------------- 
