"""
OWL PLATFORM @ RUTGERS WINLAB
PYTHON LIBRARY : COMMON
AUTHOR : AJINKYA PADWAD

MAIN REFERENCE : https://git.owlplatform.com/wiki/index.php/Category:GRAIL_RTLS_v3_Documentation

GRAIL FAKE SENSOR
"""
from termcolor import colored
import struct
import socket

# default solver message format

MessageLength = 82
Mask = 0xffffffffffffffff

MessageID = 3
Rules = 1
Physical = 0
Transmitters = 2
SensorPort = 7007



def SetMessageID(newID):
	try:
		MessageID = newID
	except:
		print " Error at setting MessageID "

def SetRules(newRules):
	try:
		Rules = newRules
	except:
		print " Error at setting Rules "

def SetPhysicalLayer(newPhysical):
	try:
		Physical = newPhysical
	except:
		print " Error at setting Physical Layer "

def SetTransmitters(newTransmitters):
	try:
		Transmitters = newTransmitters
	except:
		print " Error at setting Transmitters "

def SetSensorPort(newPort):
	try:
		SensorPort = newPort
	except:
		print " Error at setting SensorPort "

def RequestSubscription():
	import interface.SolverAggregatorInterface as interface
	
	SubscriptionMessage = (MessageLength, MessageID, Rules, Physical, Transmitters, 0,SensorPort, Mask , Mask, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, Mask, Mask, 0)

	Packer = struct.Struct('!'+'I B I b I 2Q 2Q 16B 2Q Q')
	DataPacket = Packer.pack(*SubscriptionMessage)
	interface.SendRequest(DataPacket)
		