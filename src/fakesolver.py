"""
OWL PLATFORM @ RUTGERS WINLAB
PYTHON LIBRARY : FAKESENSOR
AUTHOR : AJINKYA PADWAD

MAIN REFERENCE : https://git.owlplatform.com/wiki/index.php/Category:GRAIL_RTLS_v3_Documentation

GRAIL FAKE SOLVER
"""

import socket	
import struct
import binascii
import time
import sys
from termcolor import colored

import messages.HandshakeMessage as handshake
import messages.SubscriptionMessage as subs
import interface.SolverAggregatorInterface as interface


BadExit = False

def main(host,port):
	
	try:
	
		interface.SetHost(host)
		interface.SetPort(port)

		print colored("\n	Connecting to the Aggregator server ...", 'green')

		if interface.IsConnected():

			print colored("	Connection Successful !", 'green')

			print colored('	Handshake initiated ...\n', 'green')

			handshake.StartHandshake()

	 		print colored('	Sending Subscription Request..', 'cyan')


			MessageID = 3
			Rules = 1
			Physical = 0
			Transmitters = 2
			SensorPort = 7007

			subs.SetMessageID(MessageID)
			subs.SetRules(Rules)
			subs.SetPhysicalLayer(Physical)
			subs.SetTransmitters(Transmitters)
			subs.SetSensorPort(SensorPort)


	 		subs.RequestSubscription()


			print colored('\n 	Now Extracting Sensor Data...', 'blue')
			time.sleep(1)

			interface.ExtractSamples()


	except Exception as Err:
		ErrorText = colored('\n\n 	One or more errors have occurred !\n', 'red')
		print(ErrorText)
		print "ERROR:", Err
		# exc_type, exc_obj, exc_tb = sys.exc_info()
		# fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		# print(exc_type, fname, exc_tb.tb_lineno)
		print " 	socket disconnected\n"
		BadExit = True

if __name__ == '__main__':
	try:
		# take command line arguments :
		host = sys.argv[1]
		port = int(sys.argv[2]) 

		main(host,port)	

	except:
		if BadExit is False:
			print colored("	Please input appropriate host name and port number.\n",'red') 	
			print colored("	Syntax: python <filename.py>  <hostname>  <portnumber>", 'yellow')
			print colored("\n\n Try Default : \n 	Hostname - localhost \n 	port - 7007 ", 'blue')
			sys.exit()
		else:
			sys.exit()
