"""
OWL PLATFORM @ RUTGERS WINLAB
PYTHON LIBRARY : FAKESENSOR
AUTHOR : AJINKYA PADWAD

MAIN REFERENCE : https://git.owlplatform.com/wiki/index.php/Category:GRAIL_RTLS_v3_Documentation

GRAIL FAKE SOLVER
"""

# -------------------- DEPENDENCIES -----------------------------
import socket	
import struct
import binascii
import time
import sys
from termcolor import colored


# ------------------- CONNECTION SETUP ------------------------------------- 

BadExit = False

def main(host,port):

	# handshake message values
	StringLength = 21
	ProtocolMessage = 'GRAIL sensor protocol'
	Version = 0
	ReservedBits = 0

	# solver message format
	MessageLength = 82
	MessageID = 3
	Rules = 1
	Physical = 0
	Transmitters = 2
	SensorPort = 7007
	Mask = 0xffffffffffffffff
	
	MessageBuffer = 100

	try:
		# create new socket for TCP / IP connection
		print colored("\n	Connecting to the Aggregator server ...", 'green')
		
		time.sleep(1)

		NewSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		NewSocket.connect((host,port))

		print colored("	Connection Successful !", 'green')

	 # ------------------ HANDSHAKE -------------------------------------
		
	 	HandshakeMessage = (StringLength, ProtocolMessage, Version, ReservedBits)

		print colored('	Handshake Initiated ...\n', 'green')
		

		Packer = struct.Struct('!'+'I 21s b b')				# declare a new struct object
		DataPacket = Packer.pack(*HandshakeMessage)	

		
		print colored('	Sending Handkshake Message..', 'cyan')

		NewSocket.sendall(DataPacket)
		print 'Sent    :',DataPacket

		Received = NewSocket.recv(MessageBuffer)
		print "Received:",Received

		print colored('\n\n 	Handshake Complete.','green')

		# ----------------------------- SUBSCRIPTION MESSAGE ------------------------- 
		
		SubscriptionMessage = (MessageLength, MessageID, Rules, Physical, Transmitters, 0,SensorPort, Mask , Mask, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, Mask, Mask, 0)

		print colored('	Sending Subscription Request..', 'cyan')

		Packer = struct.Struct('!'+'I B I b I 2Q 2Q 16B 2Q Q')
		DataPacket = Packer.pack(*SubscriptionMessage)


		NewSocket.sendall(DataPacket)
		# print 'Sent    :',DataPacket

		Received = NewSocket.recv(MessageBuffer)
		# print " Received :	", Received


		print""
		print colored('\n\n 	Subscription Complete.','green')
		
		# ----------------------------- EXTRACT SAMPLES ---------------
		print colored('\n 	Now Extracting Sensor Data...', 'blue')
		time.sleep(1)

		Packer = struct.Struct('!'+'I B B 16B 16B Q f 2B')
		i=0
		while 1:
			time.sleep(1)
			data = NewSocket.recv(52)
			#print " Got :	", data
			SensorData = Packer.unpack(data)

			print colored("Got Sample ", 'green'), i
			print  " : ", SensorData
			i=i+1

	except Exception as Err:
		ErrorText = colored('\n\n 	One or more errors have occurred !\n', 'red')
		print(ErrorText)
		print "ERROR:", Err
		print " 	socket disconnected\n"
		BadExit = True
		#NewSocket.close()
		#sys.exit()


if __name__ == '__main__':
	try:
		# take command line arguments :
		host = sys.argv[1]
		port = int(sys.argv[2]) 

		if len(sys.argv) is 3:
			print "		Host:" , host
			print "		Port:" , port
			main(host,port)	
			sys.exit()

	except:
		if BadExit is False:
			print colored("	Please input appropriate host name and port number.\n",'red') 	
			print colored("	Syntax: python <filename.py>  <hostname>  <portnumber>", 'yellow')
			print colored("\n\n Try Default : \n 	Hostname - localhost \n 	port - 7007 ", 'blue')
			sys.exit()
		else:
			sys.exit()



# ----------------- END --------------------------------------------------------------------------

