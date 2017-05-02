"""
OWL PLATFORM @ RUTGERS WINLAB
PYTHON LIBRARY : FAKESENSOR
AUTHOR : AJINKYA PADWAD

MAIN REFERENCE : https://git.owlplatform.com/wiki/index.php/Category:GRAIL_RTLS_v3_Documentation

GRAIL FAKE SENSOR
"""
import socket
import struct
import HandshakeMessage
import SubscriptionMessage
from termcolor import colored
import time


host = 'localhost'
port = 7008

MessageBuffer = 50

def GetHost():
	return host
def GetPort():
	return port

def SetHost(newhost):
	host = newhost	
def SetPort(newport):
	host = newport	

def IsConnected():
	try:
		global NewSocket
		NewSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# ( IPv4, socket constant )
		NewSocket.connect((host, port))	# attach socket to remote address
		print "		Host:",host
		print "		Port:",port
		return True
	except:
		print " Connection Error !\n"
		return False

def SendHandshake(DataPacket):

	print colored('	Sending handshake message..', 'cyan')

	Received = NewSocket.recv(MessageBuffer)
	print "Received:",Received

	NewSocket.sendall(DataPacket)
	print 'Sent    :',DataPacket

	print colored('\n\n 	Handshake complete.','green')

def SendRequest(DataPacket):
	NewSocket.sendall(DataPacket)
		# print 'Sent    :',DataPacket

	Received = NewSocket.recv(MessageBuffer)
		# print " Received :	", Received

	print""
	print colored('\n\n 	Subscription Complete.','green')

def ExtractSamples():
	Packer = struct.Struct('!'+'I B B 16B 16B Q f 2B')
	i=0
	while 1:
		time.sleep(1)
		data = NewSocket.recv(52)
		SensorData = Packer.unpack(data)

		print colored("Got Sample ", 'green'), i
		print  " : ", SensorData
		i=i+1