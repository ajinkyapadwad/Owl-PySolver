"""
	Python Solver - Server 
	AJINKYA PADWAD
	MARCH 2017
"""


import socket
import struct
import time

# ------------------- SETUP ----------------------- 

host = 'localhost'
port = 7009

NewSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
NewSocket.bind((host,port))
print "	Connected to client."

print " Fake Aggregator Listening on ", host, ": ", port
NewSocket.listen(100)

Connection,Address = NewSocket.accept()

# ---------------- HANDSHAKE ---------------------------

HandshakeMessage = (21, 'GRAIL solver protocol',0 ,0)
Wrapper = struct.Struct('!'+'I 21s b b')
Packet = Wrapper.pack(*HandshakeMessage)

print "	Sending Handshake..."
Connection.sendall(Packet)

print "	Sent:	", Packet

Data = Connection.recv(40)
if not Data:
	print " ERROAR ! "
	Connection.close()
print "	Received:", Data

print "Handshake complete. "

# ----------------------------------------------------------