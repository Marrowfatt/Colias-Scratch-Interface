import scratch
import serial
import sys
import time

ScratchConnect = False
ColiasConnect = False
port = '/dev/rfcomm0'

#Initialise Colias Connection

while ColiasConnect == False:
	print '---------------------------------------\nAttempting to connect to port: %s' % port
	#Connect to default serial port for Bluetooth module
	try:		
		ser = serial.Serial(
			port=port,
			baudrate=115200,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS
		)
		#ser.isOpen()
		ColiasConnect = True
		print 'Port connection succesfull.\n'
	except:
		print 'Error connecting to port.\n'

	#Initialise settings and test if Communcation is working
	try:
			time.sleep(3)
			ser.write('MD2 30 30' + '\r\n')
			time.sleep(1)
			ser.write('MD3 50 50' + '\r\n')
			time.sleep(1)		
			ser.write('MD4 33 38' + '\r\n')
			time.sleep(1)
			ser.write('MD5 35 35' + '\r\n')
			print 'Colias Connected and initialised'
	except:
		print 'initialisation failed, Ensure Colias is switched on'
		ColiasConnect = False
		print 'Enter new port, leave blank to retry default port, type \'wired\' to try default wired port, type \'exit\' to Quit'
		userinput = raw_input()
		if userinput == '':
			port = '/dev/rfcomm0'
		elif userinput == 'wired':
			port = '/dev/ttyUSB0'
		elif userinput == 'exit':
			sys.exit(0)
		else:
			port = userinput
		

#Initialise Scratch Connection
while ScratchConnect == False:
	try:
		s = scratch.Scratch()
		ScratchConnect = True
		print 'Scratch Connected'
	except:
		print 'Error Connecting to Scratch, Ensure Remote Sensor Connections are enabled'
		time.sleep(5)

#Detect Broadcasts
def listen():
	while True:
		try:
			yield s.receive()
		except scratch.ScrachError:
			raise StopIteration

if ColiasConnect == True and ScratchConnect == True:
	print 'Interface Initialised, listening for Scratch'
	for msg in listen():
		#seperate broadcasts by 1 millisecond to prevent traffic
		time.sleep(0.1)
		if msg[0] == 'broadcast':
			if msg[1] == 'Foward':
				print 'foward message received'
				ser.write('MF' + '\r\n')
			elif msg[1] == 'Left':
				print 'Left message received'
				ser.write('ML' + '\r\n')
			elif msg[1] == 'Right':
				print 'Right message received'
				ser.write('MR' + '\r\n')
			elif msg[1] == 'Backward':
				print 'Backward message received'
				ser.write('MB' + '\r\n')
			elif msg[1] == 'Stop':
				print 'Stop message received'
				ser.write('MS' + '\r\n')
			elif msg[1] == 'Exit':
				False
		elif msg [0] == 'sensor-update':
			print 'sensor broadcast received'
else:
	print 'Connections could not be initialised, Exiting interface'
	sys.exit(0)