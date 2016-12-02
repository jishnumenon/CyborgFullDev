import serial

#Set number

theSetNo = 1

# all serial data initialised
serialSensor = serial.Serial('/dev/ttyACM0','115200')


def theTentOrButton(nowSerial):
	#Check if the serial data is from the Tentacle or Button press
	print "Checking what type of serial command"
	# Return 1 if a Tentacle is hit.
	# Return 2 if a Button is pressed.
	# Return 0 if serial data is invalid
	
	if (nowSerial.split("%")[1] == 'T'):
		serialCommand = 1
		print ("A tentacle has been Hit ")
	elif (nowSerial.split("%")[1] == 'B'):
		serialCommand = 2
		print ("A button has been pressed")
	else:
		print ("Unexpected Serial Data")
		serialCommand = 0
	return serialCommand

def findTent(tentNo):
	tentNo.split("%")[2].split(":")[1]
	
#################################################################################
# Play tentacle Sounds

def tentacle1Play():
	print ("Play tentacle 1 sound ,set " + str(theSetNo)+"\n")

def tentacle2Play():
        print ("Play tentacle 2 sound ,set " + str(theSetNo))

def tentacle3Play():
        print ("Play tentacle 3 sound ,set " + str(theSetNo))

def tentacle4Play():
        print ("Play tentacle 4 sound ,set " + str(theSetNo))

def tentacle5Play():
        print ("Play tentacle 5 sound ,set " + str(theSetNo))
#################################################################################

while 1:
	theSerial = serialSensor.readline()
	if( theTentOrButton(theSerial) == 1):
		# play the sound as the tentacle number
		if (theSerial.split("%")[2].split(":")[1] == '1'):
			tentacle1Play()
		elif (theSerial.split("%")[2].split(":")[1] == '2'):
			tentacle2Play()
		elif (theSerial.split("%")[2].split(":")[1] == '3'):
                        tentacle3Play()
		elif (theSerial.split("%")[2].split(":")[1] == '4'):
                        tentacle4Play()
		elif (theSerial.split("%")[2].split(":")[1] == '5'):
                        tentacle5Play()
		elif (theSerial.split("%")[2].split(":")[1] == '6'):
                        tentacle6Play()

		
	elif ( theTentOrButton(theSerial) == 2):
		print "Buton Handling \n"
	elif ( theTentOrButton(theSerial) == 0):
		print "Invalid Serial Data"
	else :
		print "Logical error in infinite while loop"
	
	
