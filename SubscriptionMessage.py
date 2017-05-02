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
import SolverAggregatorInterface as interface

	# solver message format
MessageLength = 82
MessageID = 3
Rules = 1
Physical = 0
Transmitters = 2
SensorPort = 7007
Mask = 0xffffffffffffffff

def RequestSubscription():
	SubscriptionMessage = (MessageLength, MessageID, Rules, Physical, Transmitters, 0,SensorPort, Mask , Mask, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, Mask, Mask, 0)

	Packer = struct.Struct('!'+'I B I b I 2Q 2Q 16B 2Q Q')
	DataPacket = Packer.pack(*SubscriptionMessage)
	interface.SendRequest(DataPacket)
		