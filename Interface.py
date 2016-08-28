import scratch
import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

#ser.open()
ser.isOpen()

s = scratch.Scratch()
while True:
	msg = s.receive()
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
	elif msg[1] == 'Exit':
		False
